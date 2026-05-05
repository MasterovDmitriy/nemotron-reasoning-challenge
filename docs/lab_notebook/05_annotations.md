# Annotations — Architecture Decision Records (ADRs)

Non-obvious decisions that shaped the project, with rationale. Future-you will thank present-you.

Each ADR explains **why** a choice was made — the choice itself can be read from the code.

---

## ADR-001 — Use Hydra for configuration management

**Date:** 2026-05-05
**Status:** Accepted
**Context:** Need a way to compose ML experiments from reusable building blocks (model, prompt, inference, data) and override values from CLI without editing code.
**Decision:** Adopt Hydra with a hierarchical config tree under `configs/`.
**Alternatives considered:**
- argparse — no composition, gets unwieldy past ~10 parameters
- Pydantic Settings — better validation but worse composition ergonomics
- Custom YAML loader — reinventing the wheel
**Consequences:**
- ✅ Trivial to swap components: `python script.py model=nemotron_super inference=sampling`
- ✅ Auto-snapshots of every run for reproducibility
- ⚠️ Magic when reading code (`@hydra.main` + `cfg.x.y` indirection)
- ⚠️ One more dependency to learn for new contributors

---

## ADR-002 — Manage Python with uv (not poetry / conda / pip)

**Date:** 2026-05-05
**Status:** Accepted
**Context:** Need a fast, modern, reproducible package manager for an ML project with mixed dependency tiers (core, dev tools, heavy LLM packages).
**Decision:** Use `uv` for everything: Python version pinning, venv, dependency resolution, lockfile.
**Alternatives considered:**
- conda — slow, mixes Python + system packages confusingly
- poetry — was a fine choice 2020–2023, but uv is now strictly faster
- pip + requirements.txt — no lock file, painful for transitive dep pinning
**Consequences:**
- ✅ 10–100× faster installs than poetry/pip
- ✅ Single tool replaces pyenv + virtualenv + pip + pip-tools
- ⚠️ Newer tool, smaller ecosystem of tutorials (mitigated by following uv's official docs)

---

## ADR-003 — Single experiment ID across MLflow, lab notebook, output dirs, git commits

**Date:** 2026-05-05
**Status:** Accepted
**Context:** With dozens of experiments, "find the run that got 0.547" becomes a 30-minute search across MLflow runs, output folders, and notes.
**Decision:** Every experiment generates an `EXP-<YYYYMMDD>-<HHMMSS>-<hex>[-name]` ID, embedded in:
- The lab notebook filename in `experiments/`
- An MLflow tag `exp_id`
- The output directory name
- Optionally the git commit message
**Consequences:**
- ✅ Search by ID becomes a one-step operation
- ✅ Forces discipline: no untraceable runs
- ⚠️ Slightly more boilerplate per experiment

---

<!-- Add new ADRs below following the same template -->

## Template

```markdown
## ADR-NNN — <short title>

**Date:** YYYY-MM-DD
**Status:** Accepted | Superseded by ADR-XXX | Deprecated
**Context:** What problem made this decision necessary?
**Decision:** What was decided?
**Alternatives considered:** What else was on the table?
**Consequences:** Pros (✅), cons (⚠️), and any follow-up work this implies.
```
