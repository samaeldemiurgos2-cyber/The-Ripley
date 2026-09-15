import unittest

from reference.evaluation_record import PublicRecordError, validate_public_record


def valid_record():
    return {
        "record_version": "public-evaluation-v1",
        "run_id": "synthetic-run-001",
        "task_class": "bounded_refactor",
        "model": "candidate-model-a",
        "harness": "controlled-harness",
        "context": "compiled-with-retraversal",
        "outcome": "accepted",
        "metrics": {
            "turns": 4,
            "tool_calls": 7,
            "input_tokens": 1200,
            "output_tokens": 650,
            "latency_ms": 9800,
            "cost_usd": 0.12,
        },
        "security": {
            "unauthorized_transitions": 0,
            "unauthorized_tool_calls": 0,
            "contained": True,
        },
        "provenance": {"source_refs": ["fixture/task-001", "fixture/acceptance-001"]},
    }


class PublicRecordContractTests(unittest.TestCase):
    def test_accepts_aggregate_record(self):
        self.assertIsNone(validate_public_record(valid_record()))

    def test_rejects_raw_trace(self):
        record = valid_record()
        record["raw_trace"] = "never publish this"
        with self.assertRaises(PublicRecordError):
            validate_public_record(record)

    def test_rejects_transcript_nested_in_metadata(self):
        record = valid_record()
        record["provenance"]["session_transcript"] = "private"
        with self.assertRaises(PublicRecordError):
            validate_public_record(record)

    def test_rejects_negative_metric(self):
        record = valid_record()
        record["metrics"]["turns"] = -1
        with self.assertRaises(PublicRecordError):
            validate_public_record(record)

    def test_rejects_absolute_local_path(self):
        record = valid_record()
        record["provenance"]["source_refs"] = ["C" + ":/private/session.json"]
        with self.assertRaises(PublicRecordError):
            validate_public_record(record)

    def test_rejects_secret_shaped_value(self):
        record = valid_record()
        record["run_id"] = "gh" + "p_" + ("x" * 40)
        with self.assertRaises(PublicRecordError):
            validate_public_record(record)


if __name__ == "__main__":
    unittest.main()
