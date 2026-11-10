# Lab Architecture

## Goal

Build a small Security Operations Center lab that teaches the complete detection workflow:

```text
activity -> telemetry -> collection -> detection -> alert -> triage -> incident report
```

## Components

### 1. Wazuh server
Runs the central Wazuh components on one Linux VM:

- Wazuh server
- Wazuh indexer
- Wazuh dashboard

An all-in-one deployment is ideal for a small lab.

### 2. Windows 11 endpoint
Generates rich endpoint telemetry with:

- Microsoft Sysmon
- Wazuh agent
- Windows Security/System/Application event channels

Sysmon records detailed process, network, DNS, registry, and file activity. Wazuh forwards and analyzes those events.

### 3. Linux endpoint
Provides authentication events, system logs, file integrity monitoring, and inventory data.

### 4. Kali/test workstation
Used only to administer the lab and generate safe test activity.

## Suggested virtual network

Use an isolated network such as:

```text
192.168.56.0/24

192.168.56.10   wazuh-server
192.168.56.20   windows-11
192.168.56.30   linux-endpoint
192.168.56.40   kali-tester
```

Exact addresses do not matter. Consistency does.

## Data flow

1. A process runs on Windows.
2. Sysmon writes an event to `Microsoft-Windows-Sysmon/Operational`.
3. The Wazuh agent reads that event channel.
4. The event is sent to the Wazuh server.
5. Wazuh decodes the event and evaluates rules.
6. A matching rule generates an alert.
7. The alert is indexed and shown in the Wazuh dashboard.
8. The analyst investigates and records findings.

## Security boundaries

- Keep the lab isolated from production networks.
- Do not expose Wazuh, SMB, RDP, SSH, or intentionally vulnerable services directly to the Internet.
- Snapshot VMs before major changes.
- Use dedicated lab credentials.
