# Evaluation methodology and failure taxonomy

**Status:** public method note. The evaluation gate described here is a
shadow-stage design, not a claim that the public shell enforces it.

## Evaluation layers

An agentic run should be evaluated at separate layers so that a failure in one
layer is not misattributed to another.

### 1. Task outcome

Use external acceptance criteria: tests, invariants, artifacts, or a human
decision rule defined before the run. Classify the result as accepted, assisted,
partial, or failed.

### 2. Process quality

For candidate reasoning or skill changes, a shadow evaluator can score three
independent dimensions:

- **Comprehensibility** — coherent structure and explicit causal dependencies.
- **Reproducibility** — whether a weaker or independent executor can apply the
  stated strategy to reach the same substantive change.
- **Efficiency** — useful progress without repeated or dead reasoning and
  without unexplained growth in the changed artifact.

These scores are evidence about process quality, not substitutes for task
correctness.

### 3. Security outcome

Record unauthorized instruction following, unauthorized tool calls, boundary
crossing, attempted exfiltration, memory contamination, downstream propagation,
persistence, false-positive suppression, and containment.

### 4. Evidence quality

Retain source references, transformation provenance, evaluator identity, and
the conditions under which a score was produced. Raw private prompts, traces,
session transcripts, credentials, and operational payloads do not belong in a
public record.

## Pre-registration discipline

Before a formal comparison, record:

1. the hypothesis;
2. comparison groups and controls;
3. task and acceptance criteria;
4. metrics and exclusion rules;
5. planned analysis;
6. disconfirmation conditions;
7. data-retention and safety boundaries.

Do not rewrite a prediction after seeing the result and call the rewrite a
pre-registration.

## Failure taxonomy

### A. Accepted outcome

The artifact meets the predeclared acceptance criteria and no disqualifying
regression or security event occurred.

### B. Assisted or partial outcome

The result is useful but required human intervention, omitted a bounded part of
the task, or did not satisfy every criterion. Do not collapse this into success
or failure; it measures a different operating point.

### C. Task failure

The model or agent completed the run but produced an incorrect, incomplete, or
regressive result under valid execution conditions.

### D. Harness failure

The harness assembled context incorrectly, exposed the wrong tool schema,
violated the approval policy, lost session state, or otherwise changed the
comparison conditions.

### E. Infrastructure or invalid-run failure

The run could not execute or its evidence is invalid because a required
dependency, evaluator, tool, or environment was unavailable. Do not score this
as model inability.

### F. Evaluator or measurement failure

The judge response was malformed, telemetry was incomplete, the acceptance
command was not discriminating, or the measurement pipeline itself failed.

### G. Provenance or governance failure

A derived claim lost its source, an unreviewed representation became
authoritative, or a generated assertion crossed into persistent policy without
an explicit governed transition.

### H. Security failure

Untrusted content acquired instruction authority, caused an unauthorized action,
poisoned memory or learned routing state, or crossed a declared capability
boundary.

The same run may have multiple labels, but the causal layer should be recorded
explicitly.

## Shadow evaluation gate

A safe rollout records process-quality scores as evidence while they are
calibrated. It does not block a pipeline or grant authority based on provisional
thresholds. Only after a distribution of real, independently evaluated cases is
available should a human-owned release decision consider whether a score may
influence control flow.

This keeps evaluation structurally separate from the write path and preserves a
clear distinction between:

```text
score recorded  ≠  score enforced  ≠  outcome accepted
```

## Public reference contract

[`reference/evaluation_record.py`](../reference/evaluation_record.py) is a small,
non-operational example of the privacy boundary. It accepts synthetic aggregate
metrics and rejects fields that would carry raw prompts, traces, transcripts,
credentials, or private paths. Its tests are intentionally independent of any
provider, endpoint, runtime, or private data store.
