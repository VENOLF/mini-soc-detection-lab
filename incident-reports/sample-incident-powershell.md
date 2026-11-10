# Incident Report — Lab Encoded PowerShell

## Executive summary

**Environment:** isolated Mini SOC lab  
**Endpoint:** `win11-lab`  
**Wazuh rule:** `100100`  
**Severity:** High (lab rule level 10)  
**Classification:** Benign test / true-positive detection

A deliberately benign PowerShell process was launched with `-EncodedCommand` to validate Sysmon telemetry and the custom Wazuh detection. The alert fired as expected. No malicious payload or external system was involved.

## Detection

- Rule: `100100`
- ATT&CK: T1059.001 PowerShell
- Source: Sysmon Event ID 1
- Relevant fields: process image and command line

## Evidence

| Stage | Observation |
|---|---|
| Process | `powershell.exe` launched |
| Command line | contained `-EncodedCommand` |
| Telemetry | Sysmon recorded process creation |
| Detection | Wazuh rule 100100 generated alert |

## Analysis

Encoded PowerShell is not automatically malicious. Administrators and automation systems can use encoded commands legitimately. In this worked example, the event is the expected result of the lab simulation design.

When you run the lab yourself, replace this worked example with your own timestamps, screenshots, event fields, and conclusions.

## Response

No containment is required for the planned authorized lab test.

## Lessons

The detection is useful as a high-signal review trigger, but production use would require tuning for known automation and administrator workflows.
