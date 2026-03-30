# Architecture Patterns

## Scope Note

This page summarizes deployable architectural patterns, but it should be read together with the broader coordination and evaluation materials. Architecture does not reduce the field to enterprise workflow DAGs alone.

## Main Families

- **Central orchestrator**: simplest governance model; strong for enterprise workflows and tool-heavy production systems.
- **Planner / executor / verifier split**: useful when verification independence is real and intermediate artifacts are inspectable.
- **Hierarchical teams**: useful for deep decomposition; requires stronger state discipline and termination rules.
- **Decentralized coordination**: flexible but expensive to debug and align; keep in scope because many research papers still evaluate this regime.
- **Graph orchestration**: makes plan/execute/verify/rollback explicit and controllable.

## Failure-Prone Zones
1. Ambiguous role boundaries causing duplicate actions or loops.
2. Plain-text messaging causing hidden state drift.
3. Missing deterministic checkpoints preventing reliable replay.
4. Coordination topology chosen for narrative appeal rather than measurable task structure.

## Reading Guidance

- For failure categories, pair this page with `MAST` / `MAST-Data`.
- For debate and social-interaction coordination patterns, do not force-fit them into workflow-only architecture language.
