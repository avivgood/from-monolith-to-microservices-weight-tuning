from datetime import time

from optimize_weights import SEARCH_SPACE

import scrapbook as sb
from ax.service.ax_client import AxClient
from ax.service.utils.instantiation import ObjectiveProperties
import papermill

def run_and_collect_metrics(w_persists: float, w_calls: float, w_uses: float, w_references: float, precision_1: float, precision_2: float):
    w_extends = 1 - w_persists - w_calls - w_uses - w_references
    ifns = []
    for project_name in ["broadleaf-commerce", "jpetstore", "springblog"]:
        papermill.execute_notebook(
            "../2-Decomposition_optimization.ipynb",
            output_path=f"outputs/output_min_ifn_{project_name}.ipynb",
            parameters={
                "project": project_name,
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
        output = sb.read_notebook(f"outputs/output_min_ifn_{project_name}.ipynb").scraps.data_dict
        ifns.append(output["ifn"])

    return max(ifns)



client = AxClient()
client.create_experiment(
    name="Find min IFN",
    owners=["Aviv Vataru"],
    parameters=SEARCH_SPACE,
    objectives={
        "ifn": ObjectiveProperties(
            minimize=False
        )
    },
    parameter_constraints=[  # prevents all being 0
        "w_persists + w_calls + w_uses + w_references <= 0.99999",
    ],
)

try:
    while True:
        data = client.get_next_trials(max_trials=1)

        client.complete_trial(trial_index=list(data[0].keys())[0],
                              raw_data={"ifn": run_and_collect_metrics(**list(data[0].values())[0])})

except KeyboardInterrupt:
    print(client.get_best_trial())