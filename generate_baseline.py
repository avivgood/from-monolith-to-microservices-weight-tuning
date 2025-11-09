from optimize_weights import client, run_with_extended_weights, run_with_weights


def run_baseline():
    run_with_extended_weights(w_persists=1,w_calls=0.8,w_uses=0.6,w_references=0.2,
                              w_extends=0,precision_1=1,precision_2=1,trail_idx="baseline")


def run_improved():
    run_with_weights(trail_idx="improved",
                     projects_file="projects/projects-with-validations.json",
                     **client.get_best_parameters()[0])


if __name__ == "__main__":
    # run_baseline()
    run_improved()
