# Python Alert Triage

`alert_triage.py` turns Wazuh JSONL alerts into a simple analyst CSV.

## Why this exists

A SOC analyst often needs to reduce raw alerts into a compact triage view.

This script extracts:

- timestamp
- agent/host
- rule ID
- Wazuh rule level
- severity label
- description
- MITRE ATT&CK IDs

## Usage

```bash
python automation/alert_triage.py samples/alerts.jsonl --output triage.csv
```

Filter out lower-level alerts:

```bash
python automation/alert_triage.py samples/alerts.jsonl --min-level 10
```

No third-party Python libraries are required.
