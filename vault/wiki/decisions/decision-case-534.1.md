---
type: decision
case: "534.1"
status: current
create: ["[[rule-python-utf8]]", "[[estimate-python-utf8-output-intact]]"]
update: ["[[rule-settings]]", "[[rule-hook-registry]]"]
origin: raw/2026-09-30/0248/ledger.md#case-534.1
sprint: migration
created: 2026-09-30
tags: [harness, session, render, hooks]
---

## Problem

The Bash tool starts each Python process of a session in the locale's code page. Unless each command sets the encoding, a dash reaches the agent as U+FFFD and other characters stop the script. That already produced one false reading and one false Frontier item. The harness should set UTF-8 once, for every Python process of the session, through a ratified rule.

## History

- 2026-09-30 created · raw/2026-09-30/0248/ledger.md#case-534.1
