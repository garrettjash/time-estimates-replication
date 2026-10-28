# Time-estimate replication

Python replication of Hu, Gaertig, and Dietvorst (2025), *Management Science*, [“How Should Time Estimates Be Structured to Increase Customer Satisfaction?”](https://doi.org/10.1287/mnsc.2023.00137).

This repository is a supplement to the written replication report

- `data/raw/` — original data for Studies 1–8.
- `replication/` — one ipynb notebook for each of the eight published studies.
- `additional_robustness_checks/` — Study 2 ANOVA (trust and perceived accuracy) and pooled study-fixed-effects leave-one-study-out analysis.

## Reproduce the analyses

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run_project.py
```

To rerun just the two additional analyses:

```bash
.venv/bin/python run_project.py --extensions-only
```

Each notebook can also be run individually. The two extension notebooks produce CSV tables in `additional_robustness_checks/tables/` and figures in `additional_robustness_checks/figures/`; these generated files are not committed. 

The published datasets and original Stata code are available from [ResearchBox](https://researchbox.org/482) and [Zenodo](https://zenodo.org/records/15033033).
