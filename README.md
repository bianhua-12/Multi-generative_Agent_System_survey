# LLM-based Multi-Agent Systems (LLM-MAS) Knowledge Base (2025–2026 Q1)

> From demo-centric multi-agent prototypes to production-grade agentic systems: protocols, runtime, evaluation, safety, and industrial deployment.

## Project Positioning

This repository has been upgraded from an early survey companion into an **engineering-first, industry-oriented curated knowledge base**. It is designed to answer three practical questions:

1. Which LLM-MAS directions still create real value by 2026?
2. Why is the industry focus shifting from prompt tricks to protocol/runtime/eval/safety?
3. What is the minimum viable technical stack for shipping multi-agent applications?

## Reading Path (Priority Order)

1. `docs/overview/2026_thesis.md` — Core thesis, signal-vs-noise filter, and value boundaries.
2. `docs/infra/production_checklist.md` — Practical runtime and reliability checklist.
3. `docs/evaluation/eval_playbook.md` — How to avoid "looks smart, fails in production".
4. `docs/protocols/protocol_landscape.md` — MCP / A2A / connector interoperability and risks.
5. `resources/papers/2025.md` and `resources/papers/2026_q1.md` — Curated high-value evidence.

## How to Read the Field (2026Q1 Thesis)

- The main axis is **system controllability**, not paper volume.
- Multi-agent is **not a default win**; it works when decomposition, verification, or parallelism creates measurable gains.
- Protocolization (MCP/A2A-like directions) is becoming a watershed in tooling integration and governance.
- Evaluation is shifting from static leaderboards to live/process diagnostics (especially in SWE workflows).

## Topic Navigation

- Architecture: `docs/architecture/architecture_patterns.md`
- Coordination: `docs/coordination/coordination_failures.md`
- Protocols: `docs/protocols/protocol_landscape.md`
- Memory/State: `docs/memory/memory_state_design.md`
- Training: `docs/training/agentic_training_stack.md`
- Evaluation: `docs/evaluation/eval_playbook.md`
- Infra/Deployment: `docs/infra/production_checklist.md`
- Safety/Governance: `docs/safety/security_threat_model.md`
- Applications: `docs/applications/high_value_apps.md`
- Industry signals: `docs/industry/industry_signals_2025_2026q1.md`

## High-Value Resource Entry Points

- By time: `resources/papers/2025.md`, `resources/papers/2026_q1.md`
- By theme: `resources/papers/{architecture,evaluation,training,infra,safety,applications}.md`
- Protocol/framework/company layers: `resources/protocols/`, `resources/frameworks/`, `resources/companies/`
- Machine-readable metadata: `data/bibliography.json`, `data/bibliography.csv`, `data/timeline.csv`

## Repository Structure

```text
/docs        Judgment-oriented docs (read first)
/resources   Evidence-oriented curated entries (Tier A / strong Tier B)
/data        Script-maintained structured metadata
/survey      arXiv-oriented survey draft (LaTeX)
/scripts     Data transformation scripts
```

## Maintenance Principles

- Keep Tier A and strong Tier B evidence only.
- Every entry must answer: **why it matters**.
- Prioritize reproducibility, deployability, and auditability.
- Mark evidence uncertainty explicitly.
