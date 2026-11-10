# Windows 11 + Sysmon + Wazuh Agent

## 1. Install Sysmon

Download Sysmon from Microsoft Sysinternals.

Place `Sysmon64.exe` and this repository's:

```text
configs/windows/sysmon-lab-config.xml
```

in the same directory.

Open PowerShell as Administrator:

```powershell
.\Sysmon64.exe -accepteula -i .\sysmon-lab-config.xml
```

Verify:

```powershell
Get-Service Sysmon64
```

View telemetry in Event Viewer:

```text
Applications and Services Logs
  -> Microsoft
  -> Windows
  -> Sysmon
  -> Operational
```

## 2. Install the Wazuh agent

Use the current Windows deployment command shown by your Wazuh dashboard under:

```text
Agents management -> Deploy new agent
```

Set the manager address to the Wazuh server IP or hostname.

## 3. Collect Sysmon

The Windows Wazuh agent configuration file is normally:

```text
C:\Program Files (x86)\ossec-agent\ossec.conf
```

Add the block from:

```text
configs/windows/wazuh-agent-eventchannels.xml
```

inside an `<ossec_config>` section.

Restart:

```powershell
Restart-Service -Name Wazuh
```

## 4. Validate

Generate a benign process:

```powershell
whoami
```

Then search Wazuh for Sysmon process-creation events.

## Why Sysmon matters

Windows logs already contain useful security information. Sysmon adds deeper endpoint telemetry such as process creation with command line, network connections, DNS queries, and file activity. Sysmon itself does not decide whether activity is malicious; the SIEM/detection logic does that.
