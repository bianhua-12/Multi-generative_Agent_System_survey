# Architecture Patterns

- **Central orchestrator**: simplest governance model; strong for enterprise workflows.
- **Hierarchical teams**: useful for deep decomposition; requires stronger state discipline.
- **Decentralized coordination**: flexible but expensive to debug and align.
- **Graph orchestration**: makes plan/execute/verify/rollback explicit and controllable.

## Failure-Prone Zones
1. Ambiguous role boundaries causing duplicate actions or loops.
2. Plain-text messaging causing hidden state drift.
3. Missing deterministic checkpoints preventing reliable replay.
