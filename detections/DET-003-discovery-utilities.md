# DET-003 — Discovery Utilities

## Hypothesis

Commands such as `whoami`, `ipconfig`, and `netstat` are normal utilities, but they are also frequently used during host and network discovery. The rule is intentionally low severity and is useful for learning correlation.

## Data source

- Sysmon Event ID 1

## Logic

Process image ends with:

```text
whoami.exe
ipconfig.exe
netstat.exe
```

## Wazuh rule

`100102`

## MITRE ATT&CK

- **T1016 — System Network Configuration Discovery**
- **T1033 — System Owner/User Discovery**

## Expected noise

High. These commands are used by administrators and troubleshooting scripts.

## Why keep this rule?

It teaches an important SOC lesson: a single low-severity event can become valuable when it appears in a suspicious sequence.

For example:

```text
encoded PowerShell -> whoami -> ipconfig -> outbound connection
```

is much more interesting than `ipconfig` alone.
