# Branching Plan (Explicit)

To satisfy the requirement of a main knowledge-base line plus a dedicated survey-rewrite line, the repository uses:

- `work`: primary knowledge-base maintenance (`README/docs/resources/data`)
- `survey-2026-rewrite`: arXiv draft development (LaTeX expansion, figures, references, tables)

## Current Status (2026-03-30)

- `survey-2026-rewrite` includes the knowledge-base rewrite commit and the `survey/main.tex` draft.
- All deeper LaTeX writing work is done on `survey-2026-rewrite`.

## Recommended Workflow

1. Update evidence layers on `work` (`resources/` + `data/`).
2. Periodically merge high-value updates from `work` into `survey-2026-rewrite`.
3. Convert judgment-oriented docs into formal academic narrative and evidence tables in LaTeX.
4. Before release, run:
   - bibliography/timeline regeneration
   - LaTeX compile checks
   - chapter-to-evidence consistency checks
