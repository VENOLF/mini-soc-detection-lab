# Detection Engineering Workflow

A useful detection is not just a regex. It connects a threat idea to reliable telemetry.

## Workflow

```text
Threat behavior
    ↓
ATT&CK technique
    ↓
Required telemetry
    ↓
Detection hypothesis
    ↓
Rule
    ↓
Safe simulation
    ↓
Alert review
    ↓
Tuning
```

## Questions to ask for every rule

1. What behavior am I trying to detect?
2. Which event proves or supports that behavior?
3. Which fields are stable enough to match?
4. What legitimate activity can look similar?
5. What severity is appropriate?
6. Which MITRE ATT&CK technique fits?
7. How will I test it safely?
8. What evidence should the analyst inspect after it fires?

## Wazuh custom rule location

Use custom rule IDs in Wazuh's recommended custom range and place larger custom rule files under:

```text
/var/ossec/etc/rules/
```

This repository uses IDs `100100-100102`.

## Rule tuning

Never assume the first version is perfect.

Track:

- false positives
- missing context
- noisy parent processes
- legitimate admin scripts
- host role
- user role
- time of day

A strong portfolio shows not only that a rule fired, but also how you improved it after observing real telemetry.
