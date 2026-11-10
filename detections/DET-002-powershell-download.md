# DET-002 — PowerShell Web Download Pattern

## Hypothesis

PowerShell can retrieve files or scripts over the network. A command line using common download primitives deserves review, especially when launched by an unusual parent process or user.

## Data source

- Sysmon Event ID 1
- `win.eventdata.image`
- `win.eventdata.commandLine`

## Logic

PowerShell command line contains one of:

```text
Invoke-WebRequest
iwr
DownloadString
Net.WebClient
```

## Wazuh rule

`100101`

## MITRE ATT&CK

- **T1059.001 — PowerShell**
- **T1105 — Ingress Tool Transfer**

## False positives

- administrators downloading internal tools
- software bootstrap scripts
- endpoint management systems

## Analyst checks

- destination URL/domain
- parent process
- downloaded filename
- hash/reputation if a file was actually created
- subsequent execution
