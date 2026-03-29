# 2025–2026Q1 Thesis (High-Signal Version)

## 1) Mainline Trend
1. **From agent prompt to agent system**: competitive advantage is moving to runtime/state/eval/safety.
2. **Protocol layer is moving upward**: MCP/A2A-like discussions indicate interoperability is now first-class.
3. **SWE and tool-heavy workflows are the real stress test**: they expose reliability, recovery, and governance limits.

## 2) What Remains Noise in 2026
- Role-play/debate setups without reproducible engineering loops.
- Social-simulation demos with weak transfer to production workflows.
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
