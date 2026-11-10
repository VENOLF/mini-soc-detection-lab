# Wazuh Server Setup

This project uses an all-in-one Wazuh deployment for a small lab.

## Recommended lab server

For a small endpoint count, use a 64-bit Linux VM with approximately:

- 4 vCPU
- 8 GB RAM
- 50 GB storage

## Install

Use the current Wazuh Quickstart installation assistant from the official documentation.

At the time this repository was prepared, the current quickstart command is:

```bash
curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

The installer prints the dashboard URL and temporary admin credentials when it finishes.

> Always verify the current command in the official Wazuh Quickstart before running it. Package versions change over time.

## Validate

```bash
sudo systemctl status wazuh-manager
```

Open the dashboard:

```text
https://<WAZUH_SERVER_IP>
```

## Add custom rules

Copy:

```text
configs/wazuh/custom_rules.xml
```

to:

```text
/var/ossec/etc/rules/mini_soc_rules.xml
```

Validate:

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
sudo /var/ossec/bin/wazuh-logtest
sudo systemctl restart wazuh-manager
```

## What success looks like

- Wazuh dashboard opens
- Windows agent appears active
- Linux agent appears active
- Windows Sysmon events are searchable
- Custom rule IDs `100100-100102` can generate alerts
