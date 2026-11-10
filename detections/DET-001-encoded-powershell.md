# DET-001 — Encoded PowerShell

## Hypothesis

A PowerShell process launched with encoded-command flags is suspicious enough to deserve analyst review because attackers frequently use PowerShell for execution and obfuscation.

## Data source

- Sysmon Event ID 1 — Process creation
- Wazuh fields:
  - `win.eventdata.image`
  - `win.eventdata.commandLine`

## Logic

```text
image ends with powershell.exe
AND
command line contains -enc or -encodedcommand
```

## Wazuh rule

`100100`

## MITRE ATT&CK

- **T1059.001 — PowerShell**

## False positives

- legitimate administrative automation
- deployment tooling
- security testing
- software installers

## Analyst checks

- parent process
- user
- full command line
- decoded command content, if available and safe to inspect
- child processes
- network connections
- related file writes
