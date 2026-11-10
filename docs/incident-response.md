# Incident Triage Playbook

When an alert fires, do not jump directly to "compromised." Build a timeline.

## 1. Validate the alert

Record:

- timestamp
- endpoint
- user
- Wazuh rule ID
- severity
- MITRE mapping
- process image
- command line
- parent process

## 2. Expand context

Ask:

- What happened immediately before the event?
- What happened after it?
- Did the process make a network connection?
- Was a file created?
- Did the same user execute related commands?
- Is this normal administrator activity?

## 3. Classify

Suggested lab classifications:

- Benign / expected
- Benign but suspicious-looking
- True positive, low impact
- True positive, requires containment
- Needs more evidence

## 4. Respond

In a real authorized environment, response may include endpoint isolation, credential resets, blocking confirmed malicious indicators, preserving evidence, removing persistence, and patching the root cause.

For this lab, document the response you would take rather than performing destructive actions.

## 5. Report

Use `incident-reports/template.md`.

A good report explains:

```text
what happened -> evidence -> impact -> ATT&CK -> response -> lessons
```
