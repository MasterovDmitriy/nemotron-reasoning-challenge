# Solution Progress — Linear Score Log

**Only entries that improved the score** make it here. This is the project's success narrative — the writeup at the end will be largely assembled from this file.

Format per entry:
1. Heading: `## <change> → <new score> (<delta>) (<EXP-ID>)`
2. Short description (2–4 sentences): what was changed, why it works, any caveats

---

<!-- Add entries below as score improves. Newest at the top. -->

_No entries yet — kick off with a baseline experiment._

---

## Template for new entries

```markdown
## + <change description> → <score> (<+delta>) (EXP-XXXXXXXX-XXXXXX-XXXX-name)

Brief description of the change. Why it likely helped. Anything noteworthy about the run (instability, edge cases, surprising behavior).
```

## Example (illustrative, not actual)

```markdown
## Baseline → 0.42 (EXP-20260506-101500-a3f9-baseline)
Nemotron Nano with zero-shot prompt, greedy decoding, on the dev set (50 samples).
First reference score. No reasoning instruction in the prompt — model often jumps to a numeric answer without working out steps.

## + Chain-of-Thought prompting → 0.51 (+0.09) (EXP-20260507-093200-bc40-cot)
Added "Let's think step by step" instruction. Big jump on math problems where the model previously skipped intermediate steps. Slight degradation on simple lookup-style questions (model over-explains).
```
