from concurrent.futures.process import ProcessPoolExecutor
import itertools
import sys
from typing import Any

from ax import RangeParameterConfig
from ax.adapter.registry import Models, Generators
from ax.generation_strategy.generation_node import GenerationStep
from ax.generation_strategy.generation_strategy import GenerationStrategy
from ax.service.ax_client import AxClient
from ax.core import RangeParameter, OptimizationConfig, Objective
from ax.service.utils.instantiation import ObjectiveProperties
import papermill
import json
from statistics import mean
import scrapbook as sb
import time
import random
import networkx as nx


from ax.storage.sqa_store.structs import DBSettings

import collections

def microservice_of(node: int):
    for k in range(n_micros):
        if (x[node, k].x == 1):
            return k

def inbound_connections(g: nx.DiGraph, node: int):

    for pred_node in g.predecessors(node):
        if microservice_of(pred_node) == microservice_of(node):
            return True

    return False

def calculate_ifn() -> float:
    interface_method_sets = set()
    for i in g.nodes():
        if g.nodes[i]['type'] == 'Entity':
            break

        if inbound_connections(g, i):
            break

        entities_for_method = set()

        for j in g.successors(i):
            if g.nodes[j]['type'] == 'Entity' and microservice_of(j) == microservice_of(i):
                entities_for_method.add(j)

        interface_method_sets.add(frozenset(entities_for_method))

    return n_micros / len(interface_method_sets)

def parse_metrics(trial_output: dict) -> float:
    # TODO check
    norm_cohesion = 1 - trial_output["cohesion"]
    norm_coupling = trial_output["avg_cop"] / trial_output["total_w"]
    return mean([norm_cohesion, norm_coupling])

def run_and_collect_metrics(project: dict, w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float):
    try:
        # Jitter for preventing ZMQ port collisions
        time.sleep(random.uniform(0.01, 0.3))
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
    except Exception as e:
        raise ValueError(f"Exception from project {project['name']} {w_persists}, {w_calls}, {w_uses}, {w_references}, {w_extends}") from e

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

gs = GenerationStrategy(steps=[
    GenerationStep(generator=Generators.SOBOL,            num_trials=6),
    GenerationStep(generator=Generators.BOTORCH_MODULAR,  num_trials=20),  # or Generators.BO_MIXED for mixed spaces
])
db_settings = DBSettings(url="sqlite:///ax.sqlite")
client = AxClient(
    generation_strategy=gs,
    db_settings=db_settings
)
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
print("============")
print(client.get_best_trial())
print(data)