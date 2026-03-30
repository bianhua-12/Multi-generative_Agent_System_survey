# Beginner Primer: What LLM-MAS Is, How It Works, and Where It Fails

This page is the shared starting point for readers coming from either research or engineering. The goal is to explain the field before judging which directions are worth building or publishing.

## 1) What Is LLM-MAS?

- **LLM agent**: an LLM-driven system that does more than answer in one turn; it can use tools, maintain intermediate state, and act over multiple steps.
- **Agentic system**: a broader term covering workflow-style systems, tool-using assistants, planner/executor loops, and multi-agent teams.
- **Multi-agent system (MAS)**: a system where multiple agent roles or units coordinate to solve a task, for example planner + executor + verifier, or multiple debate participants.
- **Workflow agent** and **multi-agent system** are not the same thing: many useful agentic systems are still effectively single-agent with tools and typed state.

## 2) What Are The Main Building Blocks?

- **Orchestrator / runtime**: decides which step happens next and how handoffs are controlled.
- **Tool gateway**: exposes APIs, databases, browsers, or other external systems to the model.
- **Memory / state**: keeps track of what the system knows, what it has already done, and what remains to be done.
- **Verifier / critic / reviewer**: checks outputs or trajectories instead of trusting the first generation.
- **Protocol layer**: standardizes how tools or external agents are connected, for example via MCP-like interfaces.

Common beginner confusion:
- More agents does not automatically mean a better system.
- Vector retrieval is not the same thing as workflow state.
- A prompt with several personas is not automatically a meaningful MAS.

## 3) How Are These Systems Built?

Three broad families appear repeatedly:

1. **Single-agent + tools**: one main model, plus tools, memory, and guardrails.
2. **Planner / executor / verifier pipelines**: explicit task decomposition and checking loops.
3. **Multi-role or graph-based systems**: several roles, agents, or nodes coordinate through an orchestrated state machine.

The main design question is not "how many agents?" but:
- where decomposition helps
- where verification adds real independence
- where state transitions need to be explicit

## 4) How Are They Trained Or Improved?

- **Pre-train** sets the upper bound for reasoning, coding, and long-context behavior.
- **Post-train / fine-tune** shapes tool-use discipline, output format, and process behavior.
- **Environment shaping** exposes agents to delayed feedback and interactive tasks, for example SWE-style environments.
- **Verifier and judge signals** improve checking, rejection, and reranking behavior.
- **Runtime engineering** often matters as much as training: better state, better tools, and better evaluation can improve systems even without changing the base model.

The 2025–2026 literature suggests that MAS training is still less mature than MAS runtime and evaluation engineering.

## 5) How Are They Evaluated?

Good evaluation now spans four layers:

1. **Outcome**: success, cost, latency
2. **Process**: failure classes, tool misuse, retry loops, rollback rate
3. **Safety**: privilege violations, injection success, leakage risk
4. **Behavior realism**: role consistency, convergence quality, and interaction dynamics for debate or social tasks

Representative benchmark families:
- **AgentBench** for historical context
- **SWE-bench Verified / Live** for realistic software-engineering evaluation
- **MAST / MAST-Data** for failure diagnosis
- **DEBATE / M-MAD** for coordination and social-behavior evaluation

## 6) What Are The Main Limitations?

- **Coordination overhead**: more agents can increase latency, cost, and failure surface.
- **Shared blind spots**: planner and verifier may agree for the wrong reasons.
- **State drift**: free-form handoffs can lose key facts or invent progress.
- **Benchmark mismatch**: good leaderboard performance may not transfer to real workflows.
- **Contamination and staleness**: static tasks overestimate capability.
- **Protocol and tool risk**: external tools introduce trust, permission, and supply-chain problems.
- **Weak transfer from demos**: role-play or debate traces can look impressive without reflecting robust task behavior.

## 7) Where To Go Next?

### Research Path

- `resources/papers/foundations_2023_2024.md`
- `resources/papers/2025.md`
- `resources/papers/2026_q1.md`
- `resources/papers/{architecture,coordination,memory_state,evaluation,training,infra,safety,applications}.md`
- `docs/overview/2026_thesis.md`

### Builder Path

- `docs/protocols/protocol_landscape.md`
- `docs/infra/production_checklist.md`
- `resources/frameworks/frameworks.md`
- `resources/protocols/protocols.md`
- `docs/industry/industry_signals_2025_2026q1.md`

## 8) How To Read `tier`

`tier` means evidence strength, not educational value:

- `Tier A`: strong primary-source or anchor artifact
- `Tier B`: representative line-setting evidence
- `Tier C`: weak-signal item kept only to avoid a blind spot

You should learn some `Tier B` topics even if you never plan to ship them, because they explain how the field evaluates itself and where current systems still fail.
