import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "automation" / "alert_triage.py"
SPEC = importlib.util.spec_from_file_location("alert_triage", MODULE_PATH)
alert_triage = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(alert_triage)


class AlertTriageTests(unittest.TestCase):
    def test_severity_boundaries(self):
        self.assertEqual(alert_triage.severity_from_level(12), "critical")
        self.assertEqual(alert_triage.severity_from_level(10), "high")
        self.assertEqual(alert_triage.severity_from_level(7), "medium")
        self.assertEqual(alert_triage.severity_from_level(6), "low")

    def test_parse_alert(self):
        alert = {
            "timestamp": "2026-01-01T00:00:00Z",
            "agent": {"name": "lab"},
            "rule": {
                "id": "100100",
                "level": 10,
                "description": "test",
                "mitre": {"id": ["T1059.001"]},
            },
        }
        row = alert_triage.parse_alert(alert)
        self.assertEqual(row["agent"], "lab")
        self.assertEqual(row["severity"], "high")
        self.assertEqual(row["mitre"], "T1059.001")


if __name__ == "__main__":
    unittest.main()
