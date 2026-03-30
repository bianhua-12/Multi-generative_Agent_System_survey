# LLM-based Multi-Agent Systems (LLM-MAS) Knowledge Base (2024 Baseline + 2025–2026 Q1 Delta)

> A beginner-first knowledge base for understanding what LLM-MAS is, how it is built, trained, evaluated, and where it fails before diving into research or production.

## What This Repo Is

This repository extends the original 2024 LLM-MAS survey companion with a structured 2025–2026Q1 delta. It is designed for **cross-disciplinary beginners** first and advanced readers second:

- If you are new to LLM agents or multi-agent systems, this repo should tell you what the field is and how its pieces fit together.
- If you are research-oriented, it should point you to the main literature lines, benchmarks, and open problems.
- If you are builder-oriented, it should show how those ideas map to protocols, runtimes, evaluation, and deployment.

The intended beginner sequence is:

1. What is LLM-MAS?
2. How are these systems built?
3. How are they trained or improved?
4. How are they evaluated?
5. What are their limitations and failure modes?
6. Given that foundation, what are the research and production paths?

## Start Here

1. `docs/overview/beginner_primer.md` — Shared primer: what the field is, how it works, how it is trained and evaluated, and where it fails.
2. `docs/architecture/architecture_patterns.md` — Core system patterns.
3. `docs/memory/memory_state_design.md` and `docs/coordination/coordination_failures.md` — State, handoffs, and coordination logic.
4. `docs/training/agentic_training_stack.md` and `docs/evaluation/eval_playbook.md` — Training and evaluation foundations.
5. `docs/safety/security_threat_model.md` and `docs/applications/high_value_apps.md` — limitations, risks, and application boundaries.

## After The Primer

### Research Path

- `resources/papers/foundations_2023_2024.md` — minimal historical context
- `resources/papers/2025.md` and `resources/papers/2026_q1.md` — time-ordered evidence
- `resources/papers/{architecture,coordination,memory_state,evaluation,training,infra,safety,applications}.md` — themed paper/resource entry points
- `docs/overview/2026_thesis.md` — advanced interpretation layer after you know the basics

### Builder Path

- `docs/protocols/protocol_landscape.md` — MCP / interoperability / trust boundaries
- `docs/infra/production_checklist.md` — production-facing checklist
- `resources/frameworks/`, `resources/protocols/`, `resources/companies/` — framework and ecosystem references
- `docs/industry/industry_signals_2025_2026q1.md` — how the 2025–2026 shift looks in products and platforms

## Scope Guardrail

- Preserve representative 2023–2024 context needed to interpret the 2025–2026 shift.
- Cover the report's main literature lines: architecture/orchestration, coordination, memory/state, training, applications, and safety/governance.
- Keep evaluation/diagnostics, protocols, and industry signals as first-class companion layers.
- Include representative Tier B/C entries when they anchor an important research direction, benchmark family, or application class.
- Do not collapse social/debate/role-play work into "noise" when it contributes benchmark, dataset, or alignment methodology.

## Topic Navigation

- Beginner primer: `docs/overview/beginner_primer.md`
- Scope / curation: `docs/overview/scope_and_curation.md`
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

- By time: `resources/papers/foundations_2023_2024.md`, `resources/papers/2025.md`, `resources/papers/2026_q1.md`
- By theme: `resources/papers/{architecture,coordination,memory_state,evaluation,training,infra,safety,applications}.md`
- Protocol/framework/company layers: `resources/protocols/`, `resources/frameworks/`, `resources/companies/`
- Machine-readable metadata: `data/bibliography.json`, `data/bibliography.csv`, `data/timeline.csv`

## Tier Note

`tier` describes **evidence strength**, not whether a topic is educationally important.

- `Tier A`: strong primary-source evidence or highly reusable anchor artifact
- `Tier B`: representative study, benchmark, or product signal that anchors a line of work
- `Tier C`: weak-signal item kept only to avoid a topic blind spot

Beginners should not read `Tier B` as "less worth learning".

## Repository Structure

```text
/docs        Primer, topic explanations, and advanced interpretation
/resources   Evidence-oriented entries across papers, benchmarks, frameworks, and signals
/data        Script-maintained structured metadata
/survey      Survey draft aligned with the beginner-to-advanced structure
/scripts     Data transformation scripts
```

## Maintenance Principles

- Keep the first impression beginner-facing and concept-first.
- `tier` records evidence strength; it is not a hard inclusion gate.
- Every entry must answer: **why it matters**.
- Prefer canonical paper/project URLs over search result pages.
- Mark living docs/specs with snapshot dates.
- Keep scope-completeness entries even when direct industrial value is indirect.
- Mark evidence uncertainty explicitly.
