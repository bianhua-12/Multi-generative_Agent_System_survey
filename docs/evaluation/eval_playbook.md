# Evaluation Playbook

## Three-Layer Evaluation
1. Outcome metrics: success rate, cost, latency.
2. Process diagnostics: failure classes, tool misuse rate, rollback rate.
3. Safety metrics: privilege violations, injection success rate, leak risk.

## Key Trends
- SWE-bench Verified/Live reflects migration from static tasks to realistic software-engineering distributions.
- Final-score-only evaluation hides process fragility; trace-level diagnosis is mandatory.

## Recommended Practice
- Run benchmark regressions for every model/policy update.
- Include live tasks to reduce contamination risk.
- Tie evaluation thresholds directly to deployment gates.
