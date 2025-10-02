from ax.adapter.cross_validation import cross_validate, compute_diagnostics
from ax.adapter.registry import Generators
from ax.plot.diagnostic import interact_cross_validation
from ax.storage.sqa_store.db import init_engine_and_session_factory
from ax.storage.sqa_store.load import load_experiment
from ax.utils.notebook.plotting import render

EXP_NAME = "Weight Optimization For Monolith Decomposition"
DB_URL = "sqlite:///ax.sqlite"


init_engine_and_session_factory(DB_URL)
exp = load_experiment(EXP_NAME)

data = exp.fetch_data()
model = Generators.BOTORCH_MODULAR(experiment=exp, data=data)

# 3) Leave-one-out CV and diagnostics
cv = cross_validate(model)                                 # LOO by default
print(compute_diagnostics(cv))                             # e.g., log-likelihood, R^2

# 4) Quick calibration plot
render(interact_cross_validation(cv))                      # Predicted vs observed with CIs

