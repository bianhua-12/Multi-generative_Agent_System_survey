# Scope and Curation Alignment

## What This Repo Is

This repository extends the original 2024 LLM-MAS survey companion with a structured 2025–2026Q1 delta. It is intentionally broader than a production-only reading list.

## What Caused the Drift

An implementation rewrite over-indexed on "high-signal engineering artifacts" and implicitly treated anything outside Tier A / strong Tier B production evidence as disposable. That narrowed the literature scope beyond the source PDF.

## Scope That Must Be Preserved

- Keep representative 2023–2024 context needed to interpret later changes.
- Cover the report's main lines: architecture/orchestration, coordination, memory/state, training, applications, and safety/governance.
- Keep evaluation/diagnostics, protocols, and industry/product signals as companion layers.
- Retain socially grounded MAS work when it contributes benchmarks, datasets, realism metrics, or alignment methodology.
- Treat the original repo and its linked external paper list as the broader backdrop, even when this environment cannot fully ingest those external materials.

## Inclusion Rules

1. Include canonical benchmark and framework references needed for engineering practice.
2. Include representative academic papers that define a research line, even when they are not directly deployment-ready.
3. Include selected official product/docs/release notes when they materially change how MAS are built or evaluated.
4. Include company or product signals when they show benchmark-to-product translation, but mark them as signals rather than neutral evaluations.
5. Exclude low-information demos that add neither reusable assets nor methodological insight.

## How to Read `tier`

- `A`: strong primary-source evidence, official benchmark/framework/doc, or highly reusable artifact
- `B`: representative study, benchmark, or product signal that materially anchors a line of work
- `C`: directional or weak-signal entry kept only to avoid a topic blind spot

`tier` is evidence strength, not an excuse to prune entire subfields.

## Practical Consequence for Maintenance

- Do not replace specific paper links with search-result URLs.
- Do not delete debate/social-simulation lines just because they are not production-default.
- Do not collapse memory/state and coordination into generic architecture notes.
- If a living doc is used, record it with a snapshot date and note that it evolves.
