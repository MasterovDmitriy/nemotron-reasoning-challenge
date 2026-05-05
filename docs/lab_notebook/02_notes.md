# Notes — Task and Data

Structured findings about the competition, the data, and observations made along the way.

## Competition

**Name:** NVIDIA Nemotron Model Reasoning Challenge
**Platform:** Kaggle
**URL:** https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge
**Goal:** Improve reasoning accuracy of Nemotron models on a novel benchmark from NVIDIA Research.

### Format
- _TBD — read rules and fill in_
- Code competition or CSV submission?
- Is internet access enabled during scoring?
- Submission time/compute limit?

### Allowed approaches
- _TBD — fill from rules_
- Prompting?
- Synthetic data generation?
- Light fine-tuning?
- Are external datasets allowed?

### Allowed models
- _TBD — fill from rules_
- Only Nemotron Nano? Whole family? Other LLMs?

### Metric
- _TBD — fill from rules_

### Deadlines
| Milestone | Date |
|---|---|
| Entry deadline | _TBD_ |
| Team merger deadline | _TBD_ |
| Final submission deadline | _TBD_ |

## Data

### Dataset structure
- _TBD — fill after data exploration_
- Number of train/val/test examples
- File format (jsonl / csv / parquet)
- Schema (fields, types)

### Domain breakdown
- Math: ?
- Logic: ?
- Multi-step reasoning: ?
- Other: ?

### Token length statistics
- Min / median / max input tokens: _TBD_
- Min / median / max expected output tokens: _TBD_
- Implication for `max_new_tokens` setting: _TBD_

### Quirks and gotchas
- _Found something weird? Document here with a date_
- _Example: "Some answers are LaTeX, some are plain numbers. Need normalization in eval."_

## Models (Nemotron family overview)

| Model | Params | Context | Notes |
|---|---|---|---|
| Nemotron Nano | 9B | 32K | Default candidate, fits on single G4 GPU |
| Nemotron Super | _TBD_ | _TBD_ | Check if allowed |
| Nemotron Ultra | _TBD_ | _TBD_ | Check if allowed |

## External resources

- Nemotron developer page: https://developer.nvidia.com/nemotron
- Nemotron models on Hugging Face: https://huggingface.co/nvidia
- Useful papers: _add as you find them_
