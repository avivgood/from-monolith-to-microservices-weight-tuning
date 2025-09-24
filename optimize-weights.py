from ax import RangeParameterConfig
from ax.service.ax_client import AxClient
from ax.core import RangeParameter, OptimizationConfig, Objective
from ax.service.utils.instantiation import ObjectiveProperties
import papermill
import json

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
            "bounds": [0.0, 1.0],
            "value_type": "float"
        },
        {
            "name": "w_calls",
            "type": "range",
            "bounds": [0.0, 1.0],
            "value_type": "float"
        },
        {
            "name": "w_uses",
            "type": "range",
            "bounds": [0.0, 1.0],
            "value_type": "float"
        },
        {
            "name": "w_references",
            "type": "range",
            "bounds": [0.0, 1.0],
            "value_type": "float"
        },
        {
            "name": "w_extends",
            "type": "range",
            "bounds": [0.0, 1.0],
            "value_type": "float"
        }
    ],
    objectives={
        "decomposition_metric_mean": ObjectiveProperties(
            minimize=True
        )
    }

)

data = client.get_next_trials(max_trials=1)

def parse_metrics(trial_output: dict):
    cohesion = trial_output["cohesion"]
    coupeling



def run_with_weights(w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float):

    with open("projects.json", "r") as f:
        projects = json.load(f)


    for project in projects:
        papermill.execute_notebook(
            "1-System_analysis.ipynb",
            output_path="output.ipynb",
            parameters={
                "project": project["name"],
                "read_from_file": True,
                "update_refinement": False,
            }
        )
        papermill.execute_notebook(
            "2-Decomposition_optimization.ipynb",
            output_path="output.ipynb",
            parameters={
                "project": project["name"],
                "w": {
                    "Calls": w_calls,
                    "Persists": w_persists,
                    "References": w_references,
                    "Extends": w_extends,
                    "Uses": w_uses
                }
            }
        )
print(data)