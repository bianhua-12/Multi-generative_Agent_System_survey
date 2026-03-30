# Production Checklist (LLM-MAS)

This page belongs to the **Builder Path**. Read it after the primer and the topic pages, not before them.

- Orchestration: graph/workflow runtime with explicit transitions
- Security: authn/authz, scoped credentials, secret isolation
- Reliability: retry budgets, timeout policies, rollback paths
- Observability: tracing, structured logs, replay debugger
- Governance: approval gates, policy engine, audit export

## Scope Note

This page is intentionally narrower than the repository as a whole. It is a deployment-facing checklist, not the boundary of what literature belongs in the knowledge base.

## Cloud vs Self-Hosted
- Cloud: fast startup and ecosystem support, with compliance/lock-in tradeoffs.
- Self-hosted: stronger control and customization, with higher ops/security burden.
