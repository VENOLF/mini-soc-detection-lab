# Mini SOC / Detection Lab

A portfolio-ready blue-team lab that demonstrates endpoint telemetry collection, detection engineering, MITRE ATT&CK mapping, alert triage, and incident reporting with **Wazuh + Sysmon + Python**.

> **Status:** repository and lab blueprint are complete. Real deployment screenshots and live alert evidence should be added after the lab is run. This keeps the portfolio honest and reproducible.

## What this project demonstrates

- Deploying a small SOC architecture with Wazuh
- Collecting Windows telemetry with Sysmon
- Monitoring Linux and Windows endpoints with Wazuh agents
- Writing custom Wazuh detection rules
- Mapping detections to MITRE ATT&CK
- Running safe attack-like simulations in an isolated lab
- Triage of Wazuh alerts with Python
- Writing analyst-style incident reports
- Maintaining detections as code with CI checks

## Architecture

```text
                       +-------------------------+
                       |   Ubuntu Wazuh Server   |
                       | server + indexer + UI   |
                       +------------+------------+
                                    ^
                                    | encrypted agent telemetry
                   +----------------+----------------+
                   |                                 |
        +----------+-----------+          +----------+----------+
        | Windows 11 Endpoint  |          |   Linux Endpoint    |
        | Sysmon + Wazuh Agent |          |    Wazuh Agent      |
        +----------+-----------+          +----------+----------+
                   ^                                 ^
                   | safe lab activity               |
                   +----------------+----------------+
                                    |
                            +-------+-------+
                            | Kali / Tester |
                            | isolated lab  |
                            +---------------+
```

Recommended lab network: an **isolated host-only/private virtual network**.

## Repository map

```text
.
├── automation/              # Python alert triage tool
├── configs/                 # Wazuh/Sysmon endpoint and detection configs
├── detections/              # Detection write-ups and ATT&CK mappings
├── docs/                    # Architecture, setup, detection, IR documentation
├── incident-reports/        # Analyst report template + worked example
├── samples/                 # Synthetic alerts for testing
├── scripts/                 # Safe lab simulations
├── tests/                   # Unit tests for Python automation
└── .github/workflows/       # CI validation
```

## Quick start

1. Read [`docs/architecture.md`](docs/architecture.md).
2. Deploy Wazuh using [`docs/setup-wazuh.md`](docs/setup-wazuh.md).
3. Configure Windows with [`docs/setup-windows-sysmon.md`](docs/setup-windows-sysmon.md).
4. Add [`configs/wazuh/custom_rules.xml`](configs/wazuh/custom_rules.xml).
5. Run [`scripts/safe-simulations.ps1`](scripts/safe-simulations.ps1) **only in your own lab**.
6. Review alerts and compare them with the detection write-ups.
7. Run the Python triage tool on an alert export.
8. Complete [`docs/portfolio-checklist.md`](docs/portfolio-checklist.md) with your own evidence.

## Detection coverage

| ID | Detection | MITRE ATT&CK | Data source |
|---|---|---|---|
| DET-001 | Encoded PowerShell command | T1059.001 | Sysmon Event ID 1 |
| DET-002 | PowerShell web-download pattern | T1105, T1059.001 | Sysmon Event ID 1 |
| DET-003 | Discovery utilities | T1016, T1033 | Sysmon Event ID 1 |

## Python triage

```bash
python automation/alert_triage.py samples/alerts.jsonl --output triage.csv
```

The tool summarizes Wazuh alert severity, rule IDs, hosts, and MITRE techniques using only the Python standard library.

## What makes this interview-ready

The finished project should let you explain the whole chain:

```text
endpoint behavior
  -> Sysmon event
  -> Wazuh collection
  -> custom detection
  -> MITRE mapping
  -> analyst triage
  -> incident report
```

Before presenting this as hands-on experience, add your own screenshots, alerts, tuning notes, and incident evidence.

## Ethics

For defensive learning on systems you own or are explicitly authorized to test. The included simulations are intentionally benign and designed to generate telemetry, not compromise third-party systems.

## References

- Wazuh: https://documentation.wazuh.com/current/
- Microsoft Sysmon: https://learn.microsoft.com/sysinternals/downloads/sysmon
- MITRE ATT&CK: https://attack.mitre.org/

## License

MIT
