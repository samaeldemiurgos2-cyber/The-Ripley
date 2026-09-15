# The-Ripley

This is the public research shell for RIPLEY-LUX: a portfolio of architecture,
evaluation, and agentic-systems research.

## Lineage

The architecture began in 2024 as **The Demiurge**, a private attempt to make
an agent's state, evidence, and authority explicit. It developed into
**RIPLEY-LUX**, a persistent cognitive-agent architecture organized around one
law:

> Model output is a proposal or evidence—not authoritative state.

The public repository is a curated research snapshot. It does not mirror the
private runtime, deployment environment, prompts, sessions, logs, credentials,
or operational infrastructure.

## Research portfolio

- [`research/architecture.md`](research/architecture.md) — sanitized system
  boundary and architectural principles.
- [`research/model-ecology-observatory.md`](research/model-ecology-observatory.md)
  — pre-registered design for measuring model × harness × context × task
  interactions.
- [`research/evaluation-and-failure-taxonomy.md`](research/evaluation-and-failure-taxonomy.md)
  — evaluation layers, failure classes, and evidence rules.
- [`reference/evaluation_record.py`](reference/evaluation_record.py) — a
  non-operational public record contract that contains no raw context or
  execution payloads.
- [`tests/test_evaluation_record.py`](tests/test_evaluation_record.py) —
  standard-library tests for the public privacy boundary.

## Related public work

- [Agentic-Security-Research](https://github.com/samaeldemiurgos2-cyber/Agentic-Security-Research)
  — orientation, trust boundaries, prompt injection, laundering, and persistent
  evidence.
- [Cognitive-Diaspora](https://github.com/samaeldemiurgos2-cyber/Cognitive-Diaspora)
  — the shared research substrate for context topology, traversal, and
  retraversability.

## Status

The private source distinguishes implemented runtime milestones from governance
and evaluation work that remains in design or shadow stages. This shell keeps
that distinction: the research documents describe proposed mechanisms and
planned experiments; they do not claim that the public shell contains or ships
the private runtime.
