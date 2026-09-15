# Model Ecology Observatory

**Status:** pre-registered design; no results are reported in this repository.

## Why an observatory

Agent performance is often summarized as if it were a property of model
identity alone. RIPLEY-LUX treats effective capability as an interaction among
model, harness, context topology, traversal, tools, task class, and risk
boundary.

The research question is:

> For a fixed task, which combination produces the highest probability of an
> acceptable outcome at an acceptable cost and security risk?

The capability surface is represented as:

```text
P(success) = f(model, harness, context, task, tools)
```

The security surface extends it with boundary conditions:

```text
P(unauthorized transition) =
    g(model, harness, context, boundary, trust state, traversal depth, task)
```

These are experimental models, not measured laws.

## Primary hypotheses

### H1 — Orientation can substitute for some brute-force capability

For at least some bounded tasks, a better-oriented packet should reduce tokens,
turns, retries, or human intervention for the same model. A cheaper model with
better traversal may match a stronger model receiving raw or poorly oriented
context.

### H2 — Harness quality is a first-class variable

Prompt assembly, tool schemas, persistence, error recovery, approval semantics,
and context ordering can change outcomes even when model and task remain fixed.

### H3 — Context strategy interacts with model identity

A compiled task packet may help one model and cause another to lose essential
context. There may be no universal best context strategy.

### H4 — Quality is task-conditional

A model can be strong at search and weak at refactoring, or strong at local
debugging and weak at cross-module design. The target is a performance surface,
not a scalar reputation.

### H5 — Security is architectural and interactional

Injection resistance should vary with boundary framing, trust state, harness,
and traversal—not only with payload wording or model name.

## Capability matrix

Vary one factor while holding the others constant wherever practical:

| Factor | Example levels |
|---|---|
| Model | free, low-cost, and frontier candidates |
| Harness | controlled evaluation harnesses and production coding planes |
| Context | raw, retrieved, structurally selected, compiled, compiled plus retraversal |
| Task | search, localization, test generation, bounded refactor, debugging, review |
| Tools | fixed tool set and execution policy per comparison |

Controls include source or repository state, task statement, acceptance
criteria, sandbox policy, tool availability, evaluator commands, time budget,
and comparable generation settings.

## Security arm

Keep payload content constant while changing its architectural position:

- user input;
- retrieved document;
- tool result;
- memory recall;
- subagent relay;
- evaluator evidence;
- synthesized operational context;
- generated code or documentation reintroduced as context.

Compare explicit instruction, explicit datum, untrusted datum, trusted datum,
ambiguous content, and content laundered through another model.

Record unauthorized instruction following, unauthorized tool invocation,
attempted exfiltration, policy-boundary crossing, memory contamination,
downstream propagation, persistence after reset, false-positive suppression of
legitimate data, and containment.

## Cross-model instruction laundering

For each upstream/downstream pair:

1. give the upstream model a span explicitly marked as datum;
2. collect the upstream output;
3. pass it through a defined downstream boundary;
4. vary the downstream orientation declaration;
5. record whether the directive changes behavior;
6. reverse model order and repeat across harnesses.

The result is a directed matrix:

```text
upstream → downstream → harness → boundary framing → outcome
```

Asymmetry is a predicted result worth testing.

## Traversal and retraversal arm

Compare:

1. raw context;
2. summary-only context;
3. summary plus governed return to source;
4. task-specific compiled traversal;
5. compiled traversal plus counter-traversal.

The stressor is a later question that depends on information treated as
irrelevant by the first summary. Measure acceptance, recovery after a wrong
hypothesis, source revisits, provenance retention, token cost, latency, human
intervention, and security failures.

## Metrics

Record accepted success, assisted success, partial result, task failure,
invalid/infrastructure failure, turns, tool calls, tool failures, input/output
tokens, latency, retries, human interventions, files changed, regressions, and
cost per accepted task.

The primary economic metric is cost per accepted task—not price per token.

Model-generated claims about success are observations only. Persistent model
profiles and routing recommendations may be updated only from independently
evaluated outcomes with retained provenance.

## Disconfirmation

Revise the program if controlled evidence shows that orientation has no
meaningful effect, harness changes do not materially change outcomes, security
behavior is insensitive to boundary framing, laundering is negligible or not
directionally distinct, or narrower traversal provides no security benefit
after capability loss is accounted for.

The observatory exists to put pressure on the architecture, including pressure
that could falsify it.

## Related public note

The companion [Agentic-Security-Research model-ecology note](https://github.com/samaeldemiurgos2-cyber/Agentic-Security-Research/blob/main/notes/2026-09-14-model-ecology-as-agentic-security-instrument.md)
extends this design toward trust-boundary and persistent-evidence questions.
