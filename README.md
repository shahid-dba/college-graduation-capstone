# Predicting Six-Year Graduation Rates at U.S. Four-Year Colleges

This repository contains the reproducible materials for Shahid Ahmad's QM640 Data Analytics Capstone at Walsh College. The study examines how affordability and institutional characteristics relate to six-year graduation rates and evaluates whether those characteristics support useful out-of-sample prediction.

## Final results

- Analytical sample: 1,669 four-year U.S. colleges
- Frozen split: 1,335 training institutions and 334 untouched test institutions
- Selected model: random forest
- Holdout MAE: 0.0672
- Holdout RMSE: 0.0913
- Holdout R-squared: 0.7677
- RMSE reduction relative to the training-mean baseline: 51.8%
- Incremental affordability contribution: 0.1168 in holdout R-squared and an 18.4% RMSE improvement

These are institution-level associations and predictions. They do not establish causal effects, rank colleges, or estimate an individual student's probability of graduating.

## Repository contents

| Path | Purpose |
| --- | --- |
| `notebooks/QM640_College_Graduation_Fully_Executed_Shahid_Ahmad.ipynb` | Fully executed, numerically authoritative notebook |
| `data/processed/college_graduation_analysis.csv` | Final 1,669-institution analytical dataset |
| `data/raw/source_manifest.json` | Source filenames, sizes, retrieval details, and SHA-256 digests |
| `reports/tables/` | 36 machine-readable result tables |
| `reports/figures/` | 11 notebook-generated figures |
| `models/` | Selected fitted pipeline and chosen hyperparameters |
| `reports/final/` | Submitted final report in PDF and executable LaTeX formats |
| `reports/automated_results_summary.md` | Compact notebook-generated result summary |
| `requirements_locked.txt` | Exact package versions used for the verified execution |
| `scripts/download_scorecard_data.py` | Optional source-data downloader and checksum verifier |

## Reproduce the analysis

Use Python 3.12 and run commands from the repository root.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements_locked.txt
jupyter notebook notebooks/QM640_College_Graduation_Fully_Executed_Shahid_Ahmad.ipynb
```

Run all cells in order. The notebook creates the raw-data folder locally, downloads the fixed College Scorecard release when necessary, validates the source, rebuilds the processed dataset, and writes the tables, figures, models, summary, and `QM640_Capstone_Outputs.zip` archive.

The raw archive and expanded source CSV are intentionally excluded from Git because of their size. To obtain them before opening the notebook, run:

```bash
python scripts/download_scorecard_data.py
```

## Data source

The analysis uses the U.S. Department of Education College Scorecard institution-level file `Most-Recent-Cohorts-Institution_06102026.zip`, released June 10, 2026. See `data/raw/README.md` and `data/raw/source_manifest.json` for the official URLs and verified checksums.

## Responsible use

The model is intended as a descriptive benchmark for institutional research and planning. Predictions should be reviewed with local evidence and should not be used for admissions, funding allocation, institutional ranking, or punitive evaluation.

## Citation

Ahmad, S. (2026). *Predicting six-year graduation rates at U.S. four-year colleges: A statistical and machine learning analysis of affordability and institutional characteristics* [Capstone project, Walsh College].

## License

Code is released under the MIT License. The College Scorecard data remain subject to the source agency's terms and documentation.
