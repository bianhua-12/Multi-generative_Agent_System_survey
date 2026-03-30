# Memory / State Design

## What This Topic Is

This topic is about how an agentic system stores progress, retrieves knowledge, and keeps execution coherent across multiple steps.

## Common Beginner Confusion

- Memory is not only vector retrieval.
- Context window length is not a substitute for explicit task state.

- Vector storage is for retrieval; it is not a workflow state model.
- Production systems need dual tracks: event log + structured state.
- Long-horizon tasks require checkpoint / replay / rollback by design.
- Tool and protocol layers increasingly externalize part of "memory" into connector-accessible systems, which raises both capability and governance questions.

## Practical Layering
1. Session memory (short-term conversational context)
2. Task state (typed, serializable workflow state)
3. Organizational knowledge (RAG/KB)
4. Audit trail (immutable execution history)

## Common Scope Error

Do not collapse memory into only vector retrieval. In the 2025–2026 literature, state, traces, memory backends, and protocol-mediated external context all interact.
