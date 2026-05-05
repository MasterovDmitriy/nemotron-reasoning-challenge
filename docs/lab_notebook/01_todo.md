# To-do — Ideas Backlog

Ideas to try, prioritized. Move items to [`07_processed_ideas.md`](./07_processed_ideas.md) once tried.

**Priority scale:**
- 🔴 **High** — likely big impact, should try soon
- 🟡 **Med** — worth trying, not urgent
- 🟢 **Low** — speculative or low-impact

**Status:**
- 📋 planned • 🔄 running • ✅ done • ❌ rejected • ⏸️ paused

| ID | Idea | Priority | Expected Effect | Cost | Status | Date Added | Source / Link |
|----|------|----------|-----------------|------|--------|------------|---------------|
| T01 | Read competition rules end-to-end | 🔴 High | Avoid invalid solution | 30 min | 📋 | 2026-05-05 | Kaggle page |
| T02 | Set up Kaggle API and download dataset | 🔴 High | Unblock all data work | 1h | 📋 | 2026-05-05 | — |
| T03 | EDA: token length distribution, problem types | 🔴 High | Decide max_new_tokens | 2h | 📋 | 2026-05-05 | — |
| T04 | Baseline: zero-shot + greedy on dev set | 🔴 High | Establish reference score | 2h | 📋 | 2026-05-05 | — |
| T05 | Chain-of-Thought prompting | 🔴 High | +5–10% on math reasoning | 1h | 📋 | 2026-05-05 | Wei et al. 2022 |
| T06 | Self-consistency (N=5, majority vote) | 🟡 Med | +3–5% on top of CoT | GPU-hours | 📋 | 2026-05-05 | Wang et al. 2022 |
| T07 | Few-shot prompting (k=3, k=5) | 🟡 Med | +2–4% | 1h per k | 📋 | 2026-05-05 | — |
| T08 | LoRA fine-tuning on synthetic CoT data | 🟢 Low | Hard to predict | 10+ GPU-hours | 📋 | 2026-05-05 | — |
| T09 | Synthetic data generation with stronger model | 🟢 Low | Quality of train set | High | 📋 | 2026-05-05 | — |

## Notes

- Always link the corresponding experiment ID once started: status `🔄 running → EXP-...`
- When done, move the row to [`07_processed_ideas.md`](./07_processed_ideas.md)
