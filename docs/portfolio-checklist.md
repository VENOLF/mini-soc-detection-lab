# Portfolio Completion Checklist

This repository becomes strong evidence of hands-on experience only after you actually run the lab.

## Infrastructure

- [ ] Wazuh server deployed
- [ ] Windows 11 agent active
- [ ] Linux agent active
- [ ] Sysmon installed and logging

## Detection evidence

- [ ] Rule 100100 fired
- [ ] Rule 100101 fired
- [ ] Rule 100102 fired
- [ ] False-positive notes written
- [ ] At least one rule tuned after observing real data

## Screenshots to add

Create `evidence/` and add:

- [ ] `01-wazuh-agents.png`
- [ ] `02-sysmon-event1.png`
- [ ] `03-det001-alert.png`
- [ ] `04-det002-alert.png`
- [ ] `05-det003-alert.png`
- [ ] `06-python-triage.png`

## Analyst artifacts

- [ ] Export a small set of your own alerts
- [ ] Run `automation/alert_triage.py`
- [ ] Add a sanitized triage CSV
- [ ] Write one incident report from your own evidence
- [ ] Add a "What I learned" section to the README

## Interview preparation

Be able to explain without reading:

1. Why Sysmon is useful
2. What Wazuh agent/server/indexer/dashboard each do
3. How an event becomes an alert
4. Why `-EncodedCommand` is suspicious but not proof of compromise
5. Why low-severity discovery events matter in a sequence
6. How you mapped a rule to MITRE ATT&CK
7. One false positive you observed and how you tuned it
