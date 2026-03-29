# Coordination Failure Taxonomy

1. Planning drift: repeated replanning with no convergence.
2. Tool thrashing: redundant or conflicting tool calls by multiple agents.
3. Message overrun: context growth that degrades latency/cost/reliability.
4. Hidden coupling: unstated assumptions break global consistency.
5. Verification collapse: checker and executor share the same blind spots.

## Engineering Mitigations
- Enforce role contracts (typed input/output schemas).
- Use structured state passing over free-form conversational handoff.
- Add review gates, budget guards, and deterministic transition rules.
