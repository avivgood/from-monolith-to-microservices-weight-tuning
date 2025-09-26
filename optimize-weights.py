from concurrent.futures.process import ProcessPoolExecutor
import itertools
import sys
from ax import RangeParameterConfig
from ax.service.ax_client import AxClient
from ax.core import RangeParameter, OptimizationConfig, Objective
from ax.service.utils.instantiation import ObjectiveProperties
import papermill
import json
from statistics import mean
import scrapbook as sb


def parse_metrics(trial_output: dict) -> float:
    norm_cohesion = 1 - trial_output["cohesion"]
    norm_coupling = trial_output["avg_cop"] / trial_output["total_w"]
    return mean([norm_cohesion, norm_coupling])

def run_and_collect_metrics(project: dict, w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float):
    papermill.execute_notebook(
        "1-System_analysis.ipynb",
        output_path=f"outputs/output_step_1_{project["name"]}.ipynb",
        parameters={
            "project": project["name"],
            "read_from_file": project["has_refinement"],
            "update_refinement": False,
            "headless": True
        }
    )
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
            "headless": True
        }
    )
    avg = parse_metrics(sb.read_notebook(f"outputs/output_step_2_{project["name"]}.ipynb").scraps.data_dict)
    print(f"finished executing {project['name']}, {avg=}", file=sys.stderr)
    return avg

def run_with_weights(w_persists: float, w_calls: float, w_uses: float, w_references: float):
    w_extends = 1 - w_persists - w_calls - w_uses - w_references
    try:
        with open("projects.json", "r") as f:
            projects = json.load(f)

        with ProcessPoolExecutor(max_workers=10) as executor:
            results = executor.map(run_and_collect_metrics, projects, itertools.repeat(w_persists), itertools.repeat(w_calls), itertools.repeat(w_uses), itertools.repeat(w_references), itertools.repeat(w_extends))

        return mean(list(results))

    except Exception as e:
        print(e, file=sys.stderr)
        raise


client = AxClient()
client.create_experiment(
    name="Weight Optimization For Monolith Decomposition",
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

for _ in range(25):
    data = client.get_next_trials(max_trials=1)
    client.complete_trial(trial_index=list(data[0].keys())[0],
                          raw_data={"decomposition_metric_mean": run_with_weights(**list(data[0].values())[0])})

print(client.get_best_parameters())
print(client.get_best_trial())
print(data)