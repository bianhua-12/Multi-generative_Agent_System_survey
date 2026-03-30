# Safety And Security Threat Model

## What This Topic Is

Safety in LLM-MAS is not only about prompt injection. Once tools, protocols, and multiple agents are involved, the system gains new attack surfaces and new coordination failures.

## Common Beginner Confusion

- Tool use creates security problems even when the prompt looks harmless.
- Better reasoning does not remove the need for permission boundaries, audit trails, or sandboxing.

## Threats beyond prompt layer
1. Tool schema injection
2. MCP/A2A endpoint spoofing
3. Connector supply-chain compromise
4. Privilege escalation through chained tools

## Controls
- Least privilege per tool per agent
- Signed tool manifests + allowlist
- Runtime policy checks before execution
- Continuous red-team eval for agent workflows
