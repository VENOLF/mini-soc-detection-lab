# Linux Endpoint Setup

Use a separate Linux VM or server as a monitored endpoint.

## Install the agent

The safest method is to use:

```text
Wazuh Dashboard -> Agents management -> Deploy new agent
```

Select your Linux distribution and copy the generated installation command.

## Validate

```bash
sudo systemctl status wazuh-agent
```

The agent should appear as **Active** in the Wazuh dashboard.

## Useful telemetry

This lab focuses on:

- authentication events
- system logs
- file integrity monitoring
- package and system inventory

Wazuh's Syscollector module provides inventory information.

## Safe test

Generate a harmless syslog event:

```bash
logger "MINI-SOC-LAB: linux telemetry validation"
```
