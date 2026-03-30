# Protocol Landscape: MCP / A2A / Tool Connectors

## What This Topic Is

Protocols matter once agentic systems connect to tools, data sources, and possibly other agents through reusable interfaces rather than one-off glue code.

## Common Beginner Confusion

- Protocols are not the whole field; they are one layer in the system stack.
- A trend signal about interoperability is weaker evidence than a launched, documented protocol with real implementations.

## Why Protocols Matter Now
Protocols convert tool integration from one-off glue code into governable infrastructure: identity, authorization, auditability, and compatibility.

## MCP (Model Context Protocol)
- Value: standardized model-to-tool/data interaction surface.
- Engineering impact: reduces connector fragmentation and integration cost.
- Risk: protocol-level attack surface expansion (malicious servers, poisoned manifests, privilege abuse).

## A2A / Interoperability Directions
- Value: cross-runtime agent interoperability ambition.
- Current reality: semantic alignment and security boundaries remain immature, and evidence quality is weaker than for MCP.

## Design Recommendations
- Use zero-trust defaults for all protocol endpoints.
- Route every tool execution through policy + audit checks.
- Apply human confirmation for high-impact or irreversible actions.

## Curation Rule

Keep a clear distinction between:
- launched or documented protocols with strong primary sources
- interoperability directions that are still mostly trend signals
