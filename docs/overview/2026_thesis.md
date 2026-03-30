# Advanced Thesis: High-Signal Interpretation Of 2025–2026Q1

Read this page **after** `docs/overview/beginner_primer.md`. It is an interpretation layer, not the default first stop for newcomers.

## 0) Scope Guardrail
- This repo extends a 2024 survey baseline; it is not a fresh-start pruning exercise.
- High-signal judgment should narrow conclusions, not erase representative literature lines.
- Social/debate-style MAS work stays in scope when it contributes datasets, realism metrics, or behavioral diagnostics.

## 1) Mainline Trend
1. **From agent prompt to agent system**: competitive advantage is moving to runtime/state/eval/safety.
2. **Protocol layer is moving upward**: MCP/A2A-like discussions indicate interoperability is now first-class.
3. **SWE and tool-heavy workflows are the real stress test**: they expose reliability, recovery, and governance limits.

## 2) What Remains Noise in 2026
- Role-play/debate setups without reusable data, behavioral metrics, or verification loops.
- Social-simulation claims that do not measure opinion dynamics, role consistency, or transfer value.
- Automation stacks without permission boundaries, replayability, or failure diagnostics.

## 3) When Multi-Agent Is Worth It
**Worth it:**
- Decomposable tasks (planner/executor/verifier pipelines)
- Independent checking or adversarial review paths
- Long-horizon cross-tool workflows requiring explicit state transitions

**Not worth it:**
- Short single-tool tasks
- Environments lacking observability and replay
- Strict latency/cost budgets where coordination overhead dominates

## 4) Minimum Viable Stack for Teams
- Orchestrator (graph/workflow runtime)
- Tool gateway (permissions + audit)
- State store (structured state + immutable event log)
- Eval harness (task success + process failure taxonomy)
- Safety guardrails (injection/tool abuse/supply-chain controls)

## 5) Why Some Less-Directly-Deployable Papers Stay
- `MAST` / `MAST-Data`: failure taxonomy and trajectory diagnosis.
- `DEBATE`, `M-MAD`, and cultural-alignment debate work: coordination and social-interaction evaluation coverage.
- `CIR3`-style application papers: preserve application diversity beyond SWE and enterprise ops.
