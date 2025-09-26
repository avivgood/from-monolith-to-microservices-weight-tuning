from concurrent.futures.process import ProcessPoolExecutor
import itertools
import sys
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
"""
TODO:
---> 18 cohesion = sum(cohesion_dict.values())/n_micros

ZeroDivisionError: division by zero
[INFO 09-26 21:15:04] ax.generation_strategy.dispatch_utils: Using Generators.BOTORCH_MODULAR since there is at least one ordered parameter and there are no unordered categorical parameters.
[INFO 09-26 21:15:04] ax.generation_strategy.dispatch_utils: Using Bayesian Optimization generation strategy: GenerationStrategy(name='Sobol+BoTorch', steps=[Sobol for 8 trials, BoTorch for subsequent trials]). Iterations after 8 will take longer to generate due to model-fitting.
[INFO 09-26 21:15:04] ax.service.ax_client: Generated new trial 0 with parameters {'w_persists': 0.023341, 'w_calls': 0.165267, 'w_uses': 0.259332, 'w_references': 0.467158} using model Sobol.
Executing:  97%|█████████▋| 36/37 [00:05<00:00,  6.69cell/s]
Executing: 100%|██████████| 37/37 [00:08<00:00,  4.62cell/s]
Executing: 100%|██████████| 37/37 [00:10<00:00,  3.38cell/s]
Executing: 100%|██████████| 37/37 [00:14<00:00,  2.63cell/s]
Executing: 100%|██████████| 37/37 [00:14<00:00,  2.59cell/s]
Executing: 100%|██████████| 37/37 [00:15<00:00,  2.37cell/s]
Executing: 100%|██████████| 37/37 [00:19<00:00,  1.90cell/s]
Executing: 100%|██████████| 25/25 [00:19<00:00,  1.29cell/s]
Executing:  41%|████      | 15/37 [00:27<00:31,  1.45s/cell]finished executing spring-petclinic, avg=0.017569566934807244
Executing:  88%|████████▊ | 22/25 [00:17<00:02,  1.26cell/s]
Executing: 100%|██████████| 25/25 [00:16<00:00,  1.50cell/s]
Executing:  22%|██▏       | 8/37 [00:02<00:06,  4.65cell/s]finished executing jhipster-sample-application, avg=4.970542995712376e-16
Executing: 100%|██████████| 25/25 [00:17<00:00,  1.42cell/s]
Executing:  92%|█████████▏| 23/25 [00:16<00:00,  4.50cell/s]finished executing springblog, avg=0.0047551955016344825
Executing: 100%|██████████| 25/25 [00:17<00:00,  1.43cell/s]
finished executing jpetstore, avg=0.0633481506586355
Executing: 100%|██████████| 37/37 [00:36<00:00,  1.00cell/s]
Executing: 100%|██████████| 25/25 [00:15<00:00,  1.58cell/s]
finished executing realworld-spring, avg=0.050155056228180166
Executing: 100%|██████████| 37/37 [00:13<00:00,  2.70cell/s]
Executing:  88%|████████▊ | 22/25 [00:14<00:01,  1.51cell/s]
Executing:  88%|████████▊ | 22/25 [00:12<00:01,  1.73cell/s]
Executing: 100%|██████████| 37/37 [00:32<00:00,  1.13cell/s]
Executing:  88%|████████▊ | 22/25 [00:11<00:01,  1.87cell/s]
Executing: 100%|██████████| 37/37 [01:06<00:00,  1.79s/cell]
Executing:  88%|████████▊ | 22/25 [00:11<00:01,  1.86cell/s]
Executing: 100%|██████████| 37/37 [02:06<00:00,  3.41s/cell]
Executing: 100%|██████████| 37/37 [03:04<00:00,  4.98s/cell]
Executing: 100%|██████████| 25/25 [00:52<00:00,  2.12s/cell]
finished executing thingsboard, avg=0.026602331572171647
Executing: 100%|██████████| 25/25 [03:08<00:00,  7.53s/cell]
finished executing broadleaf-commerce, avg=0.01328790791392992
Executing: 100%|██████████| 37/37 [05:39<00:00,  9.17s/cell]
Executing: 100%|██████████| 25/25 [00:17<00:00,  1.40cell/s]
finished executing airsonic-advanced-106, avg=0.09047791935988123
Executing: 100%|██████████| 37/37 [16:20<00:00, 26.49s/cell]
Executing:  88%|████████▊ | 22/25 [00:07<00:01,  2.79cell/s]
Exception from project shopizer-2x 0.023341026791032404, 0.1652671734694801, 0.2593324578241566, 0.46715830185915247, 0.08490104005617843
concurrent.futures.process._RemoteTraceback: 

Traceback (most recent call last):
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/optimize-weights.py", line 36, in run_and_collect_metrics
    )
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/.venv/lib/python3.12/site-packages/papermill/execute.py", line 131, in execute_notebook
    raise_for_execution_errors(nb, output_path)
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/.venv/lib/python3.12/site-packages/papermill/execute.py", line 251, in raise_for_execution_errors
    raise error
papermill.exceptions.PapermillExecutionError:
---------------------------------------------------------------------------
Exception encountered at "In [15]":
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In[15], line 18
     15 for k in range(n_micros):
     16     cohesion_dict[k] = inside_w[k] / outside_w[k]
---> 18 cohesion = sum(cohesion_dict.values())/n_micros

ZeroDivisionError: division by zero


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.12/concurrent/futures/process.py", line 263, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/process.py", line 212, in _process_chunk
    return [fn(*args) for args in chunk]
            ^^^^^^^^^
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/optimize-weights.py", line 55, in run_and_collect_metrics
    except Exception as e:
        ^^^^^^^^^^^^^^^^^^^
ValueError: Exception from project shopizer-2x 0.023341026791032404, 0.1652671734694801, 0.2593324578241566, 0.46715830185915247, 0.08490104005617843


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/optimize-weights.py", line 118, in <module>
    for _ in range(25):
                        
  File "/home/aviv/Desktop/seminar/code/from-monolith-to-microservices-weight-tuning/optimize-weights.py", line 65, in run_with_weights
    
  File "/usr/lib/python3.12/concurrent/futures/process.py", line 642, in _chain_from_iterable_of_lists
    for element in iterable:
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 619, in result_iterator
    yield _result_or_cancel(fs.pop())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 317, in _result_or_cancel
    return fut.result(timeout)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
ValueError: Exception from project shopizer-2x 0.023341026791032404, 0.1652671734694801, 0.2593324578241566, 0.46715830185915247, 0.08490104005617843

"""

def parse_metrics(trial_output: dict) -> float:
    norm_cohesion = 1 - trial_output["cohesion"]
    norm_coupling = trial_output["avg_cop"] / trial_output["total_w"]
    return mean([norm_cohesion, norm_coupling])

def run_and_collect_metrics(project: dict, w_persists: float, w_calls: float, w_uses: float, w_references: float, w_extends: float):
    try:
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
client = AxClient(
    generation_strategy=gs,
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