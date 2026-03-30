# Training Stack for Agentic/Multi-Agentic Systems

## What This Topic Is

Training in this repo means both model-centric improvement and data/environment choices that shape agent behavior.

## Common Beginner Confusion

- Not every agent improvement comes from training; many gains come from better runtime design and evaluation.
- Debate or self-play traces are not automatically useful unless they correspond to a meaningful objective.

## Pre-train
- Sets priors for tool-use behavior, long-context robustness, and reasoning/coding ceilings.

## Mid-train (environment shaping)
- Interactive environments shape decomposition, recovery, and action discipline.

## Post-train
- SFT: tool-call format and process compliance.
- RL/verifier training: long-horizon reliability optimization.
- Self-play/debate: useful only with strict process-level evaluation loops, but still part of the field's scope when backed by data or benchmarks.

## Practical Judgment
In 2025–2026 production settings, **post-train + evaluation loop quality** matters more than fancy coordination topologies.

## Scope Reminder

Training coverage in this repo includes both deployment-oriented reliability work and broader MAS behavior-shaping evidence such as interaction-trace datasets.
