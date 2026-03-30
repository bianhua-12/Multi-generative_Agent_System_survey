# Evaluation Playbook

## What This Topic Is

Evaluation asks not only whether a system succeeded, but how it succeeded, how reliably it failed, and whether its behavior is safe and interpretable.

## Common Beginner Confusion

- A single leaderboard score is not enough to understand an agent system.
- Process failures often matter more than final-answer quality when systems interact with tools or other agents.

## Four-Layer Evaluation
1. Outcome metrics: success rate, cost, latency.
2. Process diagnostics: failure classes, tool misuse rate, rollback rate.
3. Safety metrics: privilege violations, injection success rate, leak risk.
4. Behavior realism: interaction dynamics, role consistency, and convergence quality for social or debate-style MAS.

## Key Trends
- SWE-bench Verified/Live reflects migration from static tasks to realistic software-engineering distributions.
- Final-score-only evaluation hides process fragility; trace-level diagnosis is mandatory.
- Non-SWE MAS still need realism-oriented benchmarks such as debate/opinion-dynamics datasets; otherwise the repo undercounts a live research line.

## Recommended Practice
- Run benchmark regressions for every model/policy update.
- Include live tasks to reduce contamination risk.
- Tie evaluation thresholds directly to deployment gates.
- Keep at least one diagnostic layer and one behavior-sensitive layer in addition to end-to-end success metrics.
