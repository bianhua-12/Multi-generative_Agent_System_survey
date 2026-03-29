# Security Threat Model

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
