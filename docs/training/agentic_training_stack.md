# Training Stack for Agentic/Multi-Agentic Systems

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
