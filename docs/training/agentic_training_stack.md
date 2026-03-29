# Training Stack for Agentic/Multi-Agentic Systems

## Pre-train
- Sets priors for tool-use behavior, long-context robustness, and reasoning/coding ceilings.

## Mid-train (environment shaping)
- Interactive environments shape decomposition, recovery, and action discipline.

## Post-train
- SFT: tool-call format and process compliance.
- RL/verifier training: long-horizon reliability optimization.
- Self-play/debate: useful only with strict process-level evaluation loops.

## Practical Judgment
In 2025–2026 production settings, **post-train + evaluation loop quality** matters more than fancy coordination topologies.
