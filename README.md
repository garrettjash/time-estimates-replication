# Time estimate replication

Hu, Gaertig, and Dietvorst (2025), *Management Science*. DOI: https://doi.org/10.1287/mnsc.2023.00137

- `data/raw/`: unchanged author datasets.
- `replication/study_1.ipynb` through `study_8.ipynb`: original replication analyses and saved paper comparisons; Study 7 includes Figure 7.
- `additional_robustness_checks/study2_trust_accuracy_anova.ipynb`: Study 2 trust/accuracy descriptives, ANOVAs, adjusted post-hoc tests, and a mean/CI figure.
- `additional_robustness_checks/leave_one_study_out.ipynb`: six-study fixed-effects OLS with conventional OLS errors, six study omissions, and a coefficient plot.
- `additional_robustness_checks/tables/` and `figures/`: programmatically generated extension outputs (CSV, 300-dpi PNG, vector PDF). The copied `original_study7.png` is the preserved main replication figure, not an additional result.
- `replication_report.docx` and `.md`: current report, with the two new extensions and no previous extension discussion.
- `additional_robustness_checks/authors_overlap.md`: source review and overlap qualifications.

## Run in VS Code

Open `time-estimates.code-workspace`, select `.venv/bin/python`, and run notebook cells from top to bottom. Each notebook works independently. New estimates and figures are calculated directly from the Excel data. Original study notebooks and their saved outputs are preserved.

## Reproduce from a clean environment

Use Python 3.12. From the project folder:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run_project.py
```

The runner executes all ten notebooks in fresh kernels, saves only the two additional-analysis notebooks, rebuilds the Word/text report, and checks that original notebook and dataset hashes are unchanged. It does not write original replication outputs. To rerun only the new extensions and rebuild the report:

```bash
.venv/bin/python run_project.py --extensions-only
```

`build_report.py` reads the computed extension CSVs and `report_source.md`, which preserves the existing main-study text and original appendix results. It contains no hardcoded extension estimates. After editing the preserved main text, regenerate the report with `.venv/bin/python build_report.py`. Exact package versions are pinned. A fresh macOS/Python 3.12 run was verified; the local `.venv` is not part of a submission.

## Analysis conventions

Study 2 uses the original duplicate exclusions and retains end-of-survey attention-check failures. Separate item missingness is handled within outcome; neither item is missing in the retained sample. Report classical one-way ANOVA and Welch sensitivity tests. Holm correction covers the two classical omnibus tests, separately the two Welch omnibus tests, and all six pairwise tests as one post-hoc family. Post-hoc tests use Welch standard errors; their Bonferroni intervals cover the six differences jointly at at least 95%. Figure intervals are individual within-group t intervals, not simultaneous intervals.

The pooled analysis uses Studies 1, 2, 3, 5, 6, and 7. Point/range condition codes are respectively `(1,3)`, `(1,2)`, `(1,2)`, `(1,2)`, `(2,4)`, and `(1,3)`. Study 7 uses the accurate conditions only. The outcome is the original available-item mean of the five satisfaction items. All seven fits use `satisfaction ~ C(study) + range_estimate`, conventional OLS errors, and residual-degrees-of-freedom t intervals. Omissions are sensitivity checks rather than independent confirmatory tests. Pooling assumes independent participants across experiments.

Both extensions are exploratory student analyses. The first overlaps substantially with the authors' Study 2 item-level regressions; its new elements are the explicit omnibus/adjusted inference and presentation. No equivalent six-study leave-one-study-out analysis was found in the reviewed paper, complete supplement, or 11 supplied scripts. Do not describe the item-level comparisons as an entirely new hypothesis.

Original materials: https://researchbox.org/482 (archive: https://zenodo.org/records/15033033). Historical scripts, source documents, and superseded deliverables remain outside the active project in `../time-estimates-reference-backup-2026-10-27/`.
