# Memory / State Design

- Vector storage is for retrieval; it is not a workflow state model.
- Production systems need dual tracks: event log + structured state.
- Long-horizon tasks require checkpoint / replay / rollback by design.

## Practical Layering
1. Session memory (short-term conversational context)
2. Task state (typed, serializable workflow state)
3. Organizational knowledge (RAG/KB)
4. Audit trail (immutable execution history)
