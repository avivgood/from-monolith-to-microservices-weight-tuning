from concurrent.futures.process import ProcessPoolExecutor
import itertools
import sys
from typing import Any

import ax
from ax.adapter.registry import Generators
from ax.generation_strategy.generation_node import GenerationStep
from ax.generation_strategy.generation_strategy import GenerationStrategy
from ax.service.ax_client import AxClient
from ax.service.utils.instantiation import ObjectiveProperties
import papermill
import json
from statistics import mean
import scrapbook as sb
import time
import random
import psutil
import os
import glob
from ax.storage.sqa_store.db import init_engine_and_session_factory, get_engine, create_all_tables
from ax.storage.sqa_store.structs import DBSettings
from tenacity import retry, stop_after_attempt


DB_URL = "sqlite:///ax.sqlite"
EXP_NAME = "Weight Optimization For Monolith Decomposition"
CORES = psutil.cpu_count(logical=False)


init_engine_and_session_factory(url=DB_URL)
create_all_tables(get_engine())  # idempotent


def ensure_directories():

    # ensure outputs/ exists
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("trails", exist_ok=True)

    # ensure results/ inside every applications/*/
    for app_dir in glob.glob("applications/*/"):
        results_dir = os.path.join(app_dir, "results")
        os.makedirs(results_dir, exist_ok=True)


ensure_directories()


def penalty_hhi(w):
    n = len(w)
    s = sum(w)
    if s <= 0 or n < 2:
        return 0.0
    p = [wi/s for wi in w]
    hhi = sum(pi*pi for pi in p)
    return (hhi - 1/n) / (1 - 1/n)


def penalty_precision(gamma_1: float, gamma_2: float) -> float:
    gamma_1_panelty = abs(gamma_1 - 1.0)**2
    gamma_2_panelty = abs(gamma_2 - 1.0)**2
    return mean([gamma_1_panelty, gamma_2_panelty])


def parse_metrics_fixed(trial_output: dict, w: list, gamma_1: float, gamma_2: float) -> tuple[float, dict]:
    norm_ifn = float(trial_output["ifn"]) / (float(trial_output["n_methods"]) / float(trial_output["n_micros"]))
    norm_cohesion = 1.0 - trial_output["cohesion_fixed"]
    norm_coupling = float(trial_output["avg_cop_fixed"]) / (float(trial_output["total_w_fixed"]) / float(trial_output["n_micros"]))
    norm_mcalls = float(trial_output["n_calls"]) / float(trial_output["n_calls_global"])
    norm_refs = float(trial_output["n_refs"]) / float(trial_output["n_refs_global"])

    penalty_prec = penalty_precision(gamma_1, gamma_2)
    penalty_w = penalty_hhi(w)
    penalty = mean([penalty_prec, penalty_w])
    avg =  mean([norm_cohesion, norm_coupling, norm_ifn, norm_mcalls, norm_refs, penalty])
    trail_data = dict(trial_output)
    trail_data.update({"norm_ifn": norm_ifn,
                       "norm_cohesion": norm_cohesion,
                       "norm_coupling": norm_coupling,
                       "norm_mcalls": norm_mcalls,
                       "norm_refs": norm_refs,
                       "avg": avg,
                       "penalty_w": penalty_w,
                       "penalty": penalty,
                       "penalty_prec": penalty_prec})
    return avg, trail_data


def run_and_collect_metrics(project: dict, w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float, precision_1: float, precision_2: float, trail_idx):
    try:
        # Jitter for preventing ZMQ port collisions
        time.sleep(random.uniform(0.01, 0.3))
        # Uncomment the following iff the Java code changes
        """
        papermill.execute_notebook(
            "1-System_analysis.ipynb",
            output_path=f"outputs/output_step_1_{project["name"]}.ipynb",
            parameters={
                "project": project["name"],
                "read_from_file": project["has_refinement"],
                "update_refinement": False,
                "headless": True
            },
            kernel_shutdown_timeout=5
        )
        """
        papermill.execute_notebook(
            "2-Decomposition_optimization.ipynb",
            output_path=f"outputs/output_step_2_{project["name"]}.ipynb",
            parameters={
                "project": project["name"],
                "w": {
                    "Calls": w_calls,
                    "Persists": w_persists,
                    "References": w_references,
                    "Extends": w_extends,
                    "Uses": w_uses
                },
                "headless": True,
                "precision_1": precision_1,
                "precision_2": precision_2
            },
            kernel_shutdown_timeout=5
        )
        os.makedirs(f'trails/{project["name"]}', exist_ok=True)
        output = sb.read_notebook(f"outputs/output_step_2_{project["name"]}.ipynb").scraps.data_dict
        avg, diagnostics = parse_metrics_fixed(output, [w_uses,w_references,w_extends,w_persists,w_calls], precision_1, precision_2)
        with open(f"trails/{project['name']}/{trail_idx}.json", "w") as f:
            json.dump(diagnostics, f)
        print(f"finished executing {project['name']}, {avg=}", file=sys.stderr)
        return avg

    except Exception as e:
        raise ValueError(f"Exception from project {project['name']} {w_persists}, {w_calls}, {w_uses}, {w_references}, {w_extends}") from e

@retry(stop=stop_after_attempt(2))
def run_with_extended_weights(w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float, precision_1: float, precision_2: float, trail_idx: Any, projects_file: str = "projects/projects.json"):
    try:
        with open(projects_file, "r") as f:
            projects = json.load(f)

        with ProcessPoolExecutor(max_workers=CORES) as executor:
            results = executor.map(run_and_collect_metrics, projects, itertools.repeat(w_persists), itertools.repeat(w_calls), itertools.repeat(w_uses), itertools.repeat(w_references), itertools.repeat(w_extends), itertools.repeat(precision_1), itertools.repeat(precision_2), itertools.repeat(trail_idx))

        return mean(list(results))

    except Exception as e:
        print(e, file=sys.stderr)
        raise

def run_with_weights(w_persists: float, w_calls: float, w_uses: float, w_references: float, precision_1: float, precision_2: float, trail_idx: int):
    w_extends = 1 - w_persists - w_calls - w_uses - w_references
    return run_with_extended_weights(w_persists, w_calls, w_uses, w_references, w_extends, precision_1, precision_2, trail_idx)


db_settings = DBSettings(url=DB_URL)
client = AxClient(
    db_settings=db_settings
)

try:
    client.load_experiment_from_database(EXP_NAME)
except Exception as e:
    client.create_experiment(
        name=EXP_NAME,
        description="Experiment for finding the best weights for the constructed graph per relationship type,"
                    " such that the best decomposition is resulted on average",
        owners=["Aviv Vataru"],
        parameters=[
            {
                "name": "w_persists",
                "type": "range",
                "bounds": [0.000001, 1.0],
                "value_type": "float"
            },
            {
                "name": "w_calls",
                "type": "range",
                "bounds": [0.000001, 1.0],
                "value_type": "float"
            },
            {
                "name": "w_uses",
                "type": "range",
                "bounds": [0.000001, 1.0],
                "value_type": "float"
            },
            {
                "name": "w_references",
                "type": "range",
                "bounds": [0.000001, 1.0],
                "value_type": "float"
            },
            {
                "name": "precision_1",
                "type": "range",
                "bounds": [0, 2.0],
                "value_type": "float"
            },
            {
                "name": "precision_2",
                "type": "range",
                "bounds": [0, 2.0],
                "value_type": "float"
            }
        ],
        objectives={
            "decomposition_metric_mean": ObjectiveProperties(
                minimize=True
            )
        },
        parameter_constraints=[  # prevents all being 0
            "w_persists + w_calls + w_uses + w_references <= 0.99999",
        ],

    )



if __name__ == "__main__":
    try:
        while True:
            pending = [t.index for t in client.experiment.trials.values()
                       if t.status.is_running or t.status.is_candidate]
            if len(pending) > 0:
                # Recover any abounded trails
                data = client.get_trial(pending[0])

                client.complete_trial(trial_index=data.index,
                                      raw_data={"decomposition_metric_mean": run_with_weights(trail_idx=data.index, **client.get_trial_parameters(data.index))})
            else:
                data = client.get_next_trials(max_trials=1)

                client.complete_trial(trial_index=list(data[0].keys())[0],
                                      raw_data={"decomposition_metric_mean": run_with_weights(trail_idx=list(data[0].keys())[0], **list(data[0].values())[0])})

    except KeyboardInterrupt:
        pass

    print(client.get_best_parameters())
    print("============")
    print(client.get_best_trial())