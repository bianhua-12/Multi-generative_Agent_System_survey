# Coordination Failure Taxonomy

1. Planning drift: repeated replanning with no convergence.
2. Tool thrashing: redundant or conflicting tool calls by multiple agents.
3. Message overrun: context growth that degrades latency/cost/reliability.
4. Hidden coupling: unstated assumptions break global consistency.
5. Verification collapse: checker and executor share the same blind spots.
6. Premature consensus: debate or multi-view systems converge too early without real evidential pressure.
7. Role inconsistency: agents stop behaving according to their declared perspective or task boundary.

## Engineering Mitigations
- Enforce role contracts (typed input/output schemas).
- Use structured state passing over free-form conversational handoff.
- Add review gates, budget guards, and deterministic transition rules.

## Scope Reminder

- Debate, voting, and social-simulation lines remain in scope when they contribute benchmarks, datasets, or realism metrics.
- Coordination research is not only useful when it immediately maps to enterprise orchestration; it also defines how MAS behavior should be evaluated.
