# Final Ensemble — Submission Strategy

This is a **placeholder** for the final solution composition. It will be filled in late in the competition, once we know which approaches work.

In LLM reasoning competitions, the winning solution is rarely a single model with a single prompt. It is usually an **ensemble** of multiple inference strategies, prompts, or models, combined via majority voting or weighted aggregation.

## Plan (skeleton)

| Component | Source experiment | Weight | Role |
|-----------|-------------------|--------|------|
| _TBD_ | _EXP-..._ | _x.x_ | _Best single model_ |
| _TBD_ | _EXP-..._ | _x.x_ | _Diversity / different prompt_ |
| _TBD_ | _EXP-..._ | _x.x_ | _Self-consistency layer_ |

**Aggregation method:** _TBD — majority vote / weighted vote / verifier model_

**Final submission notebook:** [`kaggle/notebooks/inference_submission.ipynb`](../../kaggle/notebooks/inference_submission.ipynb) _(to be created)_

## Pre-submission checklist

- [ ] All component experiments are reproducible (configs are committed, weights are versioned with DVC or available as Kaggle Datasets)
- [ ] Inference notebook fits within Kaggle's compute/time limit
- [ ] Notebook runs successfully **end-to-end** with internet disabled (if rules require)
- [ ] All required model weights are available as Kaggle Datasets
- [ ] Output format matches the submission spec exactly (column names, separator, decimal format)
- [ ] Smoke test: notebook runs on 5 examples and produces a valid submission file
- [ ] Final submission tagged with a git commit and corresponding lab notebook entry

## Notes

- Re-read this file before every submission — it is easy to forget a checklist item under deadline pressure.
- The final solution should be **boring**: every component should be already documented in [`04_solution_progress.md`](./04_solution_progress.md) and tested. No surprise additions in the last 24 hours.
