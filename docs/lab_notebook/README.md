# Lab Notebook

This is the working journal for the project. It is the structured knowledge base for ideas, notes, questions, decisions, and experiment results.

The notebook lives in this repository (not in Notion or Confluence) on purpose:
- It is versioned alongside the code
- Every entry can be linked to a specific git commit, experiment ID, or PR
- It travels with the project to any contributor or reviewer

## Files

| File | Purpose | Edit Frequency |
|---|---|---|
| [`01_todo.md`](./01_todo.md) | Prioritized backlog of ideas to try | Daily |
| [`02_notes.md`](./02_notes.md) | Findings about the task and data | As needed |
| [`03_questions.md`](./03_questions.md) | Open questions to research | As needed |
| [`04_solution_progress.md`](./04_solution_progress.md) | Linear log of score improvements | Per successful experiment |
| [`05_annotations.md`](./05_annotations.md) | Architecture decision records (ADRs) | When making non-obvious choices |
| [`06_final_ensemble.md`](./06_final_ensemble.md) | Placeholder for the final ensemble strategy | Late stage |
| [`07_processed_ideas.md`](./07_processed_ideas.md) | Classified outcomes of every tried idea | Per closed experiment |
| [`experiments/`](./experiments/) | One Markdown report per experiment | Per experiment |

## Workflow

1. **Idea arrives** → add to [`01_todo.md`](./01_todo.md) with priority and expected impact
2. **About to run** → create `experiments/EXP-...md` from [`_template.md`](./experiments/_template.md), fill Hypothesis and Setup sections
3. **Experiment finishes** → fill Results and Conclusion sections
4. **If improves score** → add a one-liner to [`04_solution_progress.md`](./04_solution_progress.md)
5. **Close the loop** → move the idea from [`01_todo.md`](./01_todo.md) to [`07_processed_ideas.md`](./07_processed_ideas.md) with its outcome label

## Conventions

- Experiment IDs use the project format: `EXP-<YYYYMMDD>-<HHMMSS>-<4-hex>[-<name>]`
- Reference experiments by ID, not by description: write `EXP-20260505-143015-a3f9-baseline`, not "the baseline run from yesterday"
- When citing external sources, link the URL inline (Markdown supports it natively)
- Keep entries short and dated; the notebook is a log, not an essay
