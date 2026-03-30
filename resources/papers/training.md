# Training-Focused Resources
- Training Software Engineering Agents and Verifiers with SWE-Gym: https://arxiv.org/abs/2412.21139 — environment-driven shaping for agents and verifiers.
- Why Do Multi-Agent LLM Systems Fail?: https://arxiv.org/abs/2503.13657 — failure categories suggest what role spec, verification, and termination policies should be trained or searched over.
- DEBATE: https://arxiv.org/abs/2510.25110 — example of using real interaction traces as a training signal rather than only static labels.
- OpenAI Platform Documentation (Agents / Responses / tracing): https://platform.openai.com/docs — operationally relevant because post-train gains only matter if tool traces can be measured and debugged.
- Practical stance: keep pre-train and post-train claims tied to environments, traces, and judge signals, not only to coordination topology.
