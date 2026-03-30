# LLM-based Multi-Agent Systems (LLM-MAS) Knowledge Base (2024 Baseline + 2025–2026 Q1 Delta)

> A layered survey companion and engineering knowledge base that extends the original 2024 repo with 2025–2026 early literature, benchmarks, protocols, and industry signals.

## Project Positioning

This repository should be read as a **layered knowledge base built on top of the original 2024 survey materials**, not as a production-only shortlist. It is designed to answer four practical questions:

1. What changed in LLM-MAS during 2025–2026Q1?
2. Which papers, benchmarks, datasets, frameworks, and product signals define those changes?
3. Which lines are directly deployment-relevant, and which still matter mainly as diagnostic or scope-setting evidence?
4. How should a team separate evidence strength (`tier`) from inclusion scope?

## Scope Guardrail

- Preserve representative 2023–2024 context needed to interpret the 2025–2026 shift.
- Cover the report's main literature lines: architecture/orchestration, coordination, memory/state, training, applications, and safety/governance.
- Keep evaluation/diagnostics, protocols, and industry signals as first-class companion layers.
- Include representative Tier B/C entries when they anchor an important research direction, benchmark family, or application class.
- Do not collapse social/debate/role-play work into "noise" when it contributes benchmark, dataset, or alignment methodology.

## Reading Path (Priority Order)

1. `docs/overview/scope_and_curation.md` — Inclusion rules and how this repo maps back to the PDF.
2. `docs/overview/2026_thesis.md` — High-signal judgments after scope is understood.
3. `resources/papers/foundations_2023_2024.md` — Minimal historical context preserved from the pre-2025 baseline.
4. `resources/papers/2025.md` and `resources/papers/2026_q1.md` — Time-ordered delta coverage.
5. `resources/papers/{architecture,coordination,memory_state,evaluation,training,infra,safety,applications}.md` — Theme navigation.

## How to Read the Field (2026Q1 Thesis)

- The main axis is **system controllability**, not paper volume alone.
- Multi-agent is **not a default win**; it works when decomposition, verification, or parallelism creates measurable gains.
- Protocolization (MCP and adjacent directions) is becoming a watershed in tooling integration and governance.
- Evaluation is shifting from static leaderboards to live/process diagnostics, but social-behavioral benchmarks still matter for non-SWE MAS tasks.

## Topic Navigation

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

## Repository Structure

```text
/docs        Judgment-oriented docs and scope guardrails
/resources   Evidence-oriented entries across papers, benchmarks, frameworks, and signals
/data        Script-maintained structured metadata
/survey      Survey draft aligned with the layered scope
/scripts     Data transformation scripts
```

## Maintenance Principles

- `tier` records evidence strength; it is not a hard inclusion gate.
- Every entry must answer: **why it matters**.
- Prefer canonical paper/project URLs over search result pages.
- Mark living docs/specs with snapshot dates.
- Keep scope-completeness entries even when direct industrial value is indirect.
- Mark evidence uncertainty explicitly.
