# Protocol Landscape: MCP / A2A / Tool Connectors

## Why Protocols Matter Now
Protocols convert tool integration from one-off glue code into governable infrastructure: identity, authorization, auditability, and compatibility.

## MCP (Model Context Protocol)
- Value: standardized model-to-tool/data interaction surface.
- Engineering impact: reduces connector fragmentation and integration cost.
- Risk: protocol-level attack surface expansion (malicious servers, poisoned manifests, privilege abuse).

## A2A / Interoperability Directions
- Value: cross-runtime agent interoperability ambition.
- Current reality: semantic alignment and security boundaries remain immature.

## Design Recommendations
- Use zero-trust defaults for all protocol endpoints.
- Route every tool execution through policy + audit checks.
- Apply human confirmation for high-impact or irreversible actions.
