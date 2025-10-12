from concurrent.futures.process import ProcessPoolExecutor
import itertools
import sys
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

    # ensure results/ inside every applications/*/
    for app_dir in glob.glob("applications/*/"):
        results_dir = os.path.join(app_dir, "results")
        os.makedirs(results_dir, exist_ok=True)

ensure_directories()

def parse_metrics(trial_output: dict) -> float:
    norm_ifn = 1.0 - (1.0 / float(trial_output["ifn"]))
    norm_cohesion = 1.0 - trial_output["cohesion"]
    norm_coupling = float(trial_output["avg_cop"]) / (float(trial_output["total_w"]) / float(trial_output["n_micros"]))
    norm_mcalls = float(trial_output["n_calls"]) / float(trial_output["n_calls_global"])
    norm_refs = float(trial_output["n_refs"]) / float(trial_output["n_refs_global"])
    return mean([norm_cohesion, norm_coupling, norm_ifn, norm_mcalls, norm_refs])

@retry(stop=stop_after_attempt(1))
def run_and_collect_metrics(project: dict, w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float, precision_1: float, precision_2: float):
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
        avg = parse_metrics(sb.read_notebook(f"outputs/output_step_2_{project["name"]}.ipynb").scraps.data_dict)
        print(f"finished executing {project['name']}, {avg=}", file=sys.stderr)
        return avg

    except Exception as e:
        raise ValueError(f"Exception from project {project['name']} {w_persists}, {w_calls}, {w_uses}, {w_references}, {w_extends}") from e

def run_with_weights(w_persists: float, w_calls: float, w_uses: float, w_references: float, precision_1: float, precision_2: float):
    w_extends = 1 - w_persists - w_calls - w_uses - w_references
    try:
        with open("projects.json", "r") as f:
            projects = json.load(f)

        with ProcessPoolExecutor(max_workers=CORES) as executor:
            results = executor.map(run_and_collect_metrics, projects, itertools.repeat(w_persists), itertools.repeat(w_calls), itertools.repeat(w_uses), itertools.repeat(w_references), itertools.repeat(w_extends), itertools.repeat(precision_1), itertools.repeat(precision_2))

        return mean(list(results))

    except Exception as e:
        print(e, file=sys.stderr)
        raise

generation_strat = GenerationStrategy(steps=[
    GenerationStep(generator=Generators.SOBOL,            num_trials=8),
    GenerationStep(generator=Generators.BOTORCH_MODULAR,  num_trials=20),  # or Generators.BO_MIXED for mixed spaces
])
db_settings = DBSettings(url=DB_URL)
client = AxClient(
    generation_strategy=generation_strat,
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
    for _ in range(26):
        data = client.get_next_trials(max_trials=1)
        client.complete_trial(trial_index=list(data[0].keys())[0],
                              raw_data={"decomposition_metric_mean": run_with_weights(**list(data[0].values())[0])})

    print(client.get_best_parameters())
    print("============")
    print(client.get_best_trial())
    print("============")
    print(data)