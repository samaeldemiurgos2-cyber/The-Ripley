"""Validate a privacy-preserving, aggregate evaluation record.

This module is a public reference contract only. It performs no network I/O,
provider calls, file access, or runtime integration. The contract is designed
to make the public/private boundary executable: aggregate metrics and opaque
source references are allowed; raw context and private payloads are not.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from numbers import Real
from typing import Any


class PublicRecordError(ValueError):
    """Raised when a record violates the public aggregate contract."""


_OUTCOMES = frozenset(
    {
        "accepted",
        "assisted",
        "partial",
        "task_failure",
        "harness_failure",
        "infrastructure_failure",
        "evaluator_failure",
        "security_failure",
    }
)

_REQUIRED_TOP_LEVEL = frozenset(
    {"record_version", "run_id", "task_class", "model", "harness", "context", "outcome", "metrics", "security", "provenance"}
)

_FORBIDDEN_KEYS = frozenset(
    {
        "raw_prompt",
        "raw_input",
        "raw_context",
        "raw_trace",
        "raw_response",
        "session_transcript",
        "transcript",
        "credential",
        "credentials",
        "secret",
        "secrets",
        "password",
        "api_key",
        "access_token",
        "refresh_token",
        "private_key",
        "internal_prompt",
        "tool_args_raw",
        "tool_result_raw",
    }
)

_METRIC_KEYS = frozenset(
    {
        "turns",
        "tool_calls",
        "tool_failures",
        "input_tokens",
        "output_tokens",
        "latency_ms",
        "human_interventions",
        "files_changed",
        "regressions",
        "cost_usd",
    }
)

_SECURITY_KEYS = frozenset(
    {
        "unauthorized_transitions",
        "unauthorized_tool_calls",
        "exfiltration_attempts",
        "memory_contamination",
        "contained",
    }
)

_ABSOLUTE_PATH = re.compile(r"(?:^[A-Za-z]:[\\/])|(?:^/)|(?:^\\\\)")
_SECRET_SHAPES = re.compile(
    r"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)


def _normalise_key(key: Any) -> str:
    if not isinstance(key, str):
        raise PublicRecordError("all object keys must be strings")
    return key.strip().lower().replace("-", "_")


def _walk_for_forbidden_content(value: Any, path: str = "record") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalised = _normalise_key(key)
            if normalised in _FORBIDDEN_KEYS:
                raise PublicRecordError(f"private field is not allowed: {path}.{key}")
            _walk_for_forbidden_content(child, f"{path}.{key}")
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _walk_for_forbidden_content(child, f"{path}[{index}]")
        return
    if isinstance(value, str) and _SECRET_SHAPES.search(value):
        raise PublicRecordError(f"secret-shaped value is not allowed: {path}")


def _require_non_empty_string(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise PublicRecordError(f"{field} must be a non-empty string")
    if "\r" in value or "\n" in value:
        raise PublicRecordError(f"{field} must be single-line")
    if _ABSOLUTE_PATH.search(value):
        raise PublicRecordError(f"{field} must not contain an absolute local path")


def _validate_metrics(metrics: Any) -> None:
    if not isinstance(metrics, Mapping):
        raise PublicRecordError("metrics must be an object")
    for key, value in metrics.items():
        if _normalise_key(key) not in _METRIC_KEYS:
            raise PublicRecordError(f"unsupported metric: {key}")
        if isinstance(value, bool) or not isinstance(value, Real) or value < 0:
            raise PublicRecordError(f"metric must be a non-negative number: {key}")


def _validate_security(security: Any) -> None:
    if not isinstance(security, Mapping):
        raise PublicRecordError("security must be an object")
    for key, value in security.items():
        normalised = _normalise_key(key)
        if normalised not in _SECURITY_KEYS:
            raise PublicRecordError(f"unsupported security field: {key}")
        if normalised == "contained":
            if not isinstance(value, bool):
                raise PublicRecordError("security.contained must be boolean")
        elif isinstance(value, bool) or not isinstance(value, Real) or value < 0:
            raise PublicRecordError(f"security count must be a non-negative number: {key}")


def _validate_provenance(provenance: Any) -> None:
    if not isinstance(provenance, Mapping):
        raise PublicRecordError("provenance must be an object")
    source_refs = provenance.get("source_refs")
    if not isinstance(source_refs, Sequence) or isinstance(source_refs, (str, bytes, bytearray)) or not source_refs:
        raise PublicRecordError("provenance.source_refs must be a non-empty list")
    for index, source_ref in enumerate(source_refs):
        _require_non_empty_string(source_ref, f"provenance.source_refs[{index}]")


def validate_public_record(record: Mapping[str, Any]) -> None:
    """Validate an aggregate record; return ``None`` on success."""

    if not isinstance(record, Mapping):
        raise PublicRecordError("record must be an object")
    _walk_for_forbidden_content(record)

    keys = set(record)
    missing = _REQUIRED_TOP_LEVEL - keys
    if missing:
        raise PublicRecordError(f"missing required fields: {', '.join(sorted(missing))}")
    unexpected = keys - _REQUIRED_TOP_LEVEL
    if unexpected:
        raise PublicRecordError(f"unsupported top-level fields: {', '.join(sorted(unexpected))}")

    for field in ("record_version", "run_id", "task_class", "model", "harness", "context"):
        _require_non_empty_string(record[field], field)
    if record["outcome"] not in _OUTCOMES:
        raise PublicRecordError(f"unsupported outcome: {record['outcome']}")

    _validate_metrics(record["metrics"])
    _validate_security(record["security"])
    _validate_provenance(record["provenance"])
