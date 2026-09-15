# RIPLEY-LUX: sanitized architecture overview

**Status:** public research summary. Operational implementation is intentionally
outside this repository.

## Design objective

RIPLEY-LUX is a persistent cognitive-agent architecture for long-running work
across models, tools, memory, and background processes. Its central design
constraint is authority separation:

> A model may propose an action or provide evidence. A model does not own the
> system's state.

This turns model output into an input to a governed transition rather than an
implicit write to truth.

## Public system boundary

```text
primary sources / task input
            │
            ▼
retrieval, context assembly, and traversal
            │
            ▼
model + harness + tools
            │
            ├── proposal or evidence
            │
            ▼
policy, evaluation, and provenance checks
            │
            ├── bounded external action
            └── persistent state transition

provenance and evaluation records accompany the path
without storing raw private content in the public portfolio
```

## Architectural principles

### State is external to the model

Persistent memory, routing decisions, learned operational context, and other
stateful effects belong to explicit stores and transition rules. The model's
response is not self-authorizing.

### Context is assembled by role

Information should enter a task with source identity, intended role, and trust
state. Retrieval and context compilation are navigation operations; they should
not erase the path back to primary evidence.

### Capability is task-conditional

Routing should consider task class, available tools, context strategy, and risk
boundary. “Best model” is not a stable property independent of the harness and
the task.

### Side effects are bounded

Tool use, memory writes, and external actions are separate from inference. They
need explicit policy, observable outcomes, and a failure mode that does not turn
an unavailable dependency into fabricated success.

### Degradation is evidence, not success

A missing dependency, malformed evaluator response, or tool failure is recorded
as its own condition. It must not silently become a model-quality score.

### Background cognition is subordinate

Idle or asynchronous synthesis may surface candidates and relationships, but it
must not silently promote generated content into authoritative memory or
routing policy. Promotion requires provenance and evaluation.

## Research surface

The private source describes a runtime fork, persistent memory layers, adaptive
skills, background synthesis, multi-surface interaction, and a governance kernel
in shadow/design stages. This public shell exports only the abstractions needed
to evaluate those ideas:

- a source/model/traversal separation;
- a model-ecology measurement plan;
- a failure taxonomy that keeps infrastructure, harness, evaluator, and model
  outcomes distinct;
- a safe reference contract for aggregate evaluation records.

No service topology, node names, network addresses, deployment manifests,
credentials, internal prompts, logs, or session material are part of this
portfolio.

## Relationship to the shared research map

RIPLEY-LUX is the persistent observer and state boundary in the broader map.
[Cognitive Diaspora](https://github.com/samaeldemiurgos2-cyber/Cognitive-Diaspora)
develops the context-topology and retraversability thesis. [Agentic Security
Research](https://github.com/samaeldemiurgos2-cyber/Agentic-Security-Research)
tests how orientation and trust fail when information crosses agentic
boundaries.
