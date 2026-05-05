# EXP-YYYYMMDD-HHMMSS-XXXX-<name>

**Date:** YYYY-MM-DD
**Status:** running | done | failed | abandoned
**Author:** Dmitriy Masterov
**Git commit:** _hash_
**MLflow run:** _link or run_id_
**Config:** _path to the experiment config used, e.g. configs/experiment/baseline.yaml_

## Hypothesis

What I expect this experiment to show, and why.
- Source of the idea: paper / forum / intuition / previous experiment
- Expected metric impact: e.g., "+3–5% on dev set"
- What would falsify the hypothesis?

## Setup

Concrete configuration of this run.
- Model: _name + version_
- Prompt: _strategy + template version_
- Inference: _decoding strategy + key parameters_
- Data: _split + n_samples_
- Anything special (custom postprocessing, filtering, etc.)

Full config snapshot is at: _outputs/EXP-.../config.yaml_

## Results

| Metric | Value | Δ vs Baseline | Δ vs Previous Best |
|--------|-------|---------------|--------------------|
| _e.g., pass@1_ | _0.51_ | _+0.09_ | _+0.04_ |

Optional: include a small chart, confusion matrix, or qualitative samples.

## Observations

What I noticed in the outputs that the metric doesn't capture.
- Where does the model still fail? Sample a few errors.
- Anything surprising (good or bad)?
- Is the run stable across seeds? (If checked)

## Conclusion

What did I learn? What's next?
- Status: ship to [`04_solution_progress.md`](../04_solution_progress.md) / move to [`07_processed_ideas.md`](../07_processed_ideas.md)
- Follow-up experiment ideas → add to [`01_todo.md`](../01_todo.md)
- Linked next experiment: _EXP-... or "none yet"_
