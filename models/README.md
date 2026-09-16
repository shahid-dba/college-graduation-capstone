# Model artifacts

`selected_full_model.joblib` is the complete fitted scikit-learn pipeline selected through the training-only cross-validation procedure. It contains preprocessing and the fitted random-forest estimator. The repository copy uses Joblib compression so it remains convenient to upload through GitHub's website; reloading it reproduces the canonical artifact's predictions to machine precision. `best_parameters.json` records the chosen hyperparameters.

Load the model only from a trusted copy of this repository and use the package versions recorded in `requirements_locked.txt`. Serialized Python objects can execute code when loaded and may not be compatible with materially different library versions.
