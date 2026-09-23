---
type: decision
case: "363"
status: current
update: ["[[rule-skill-hi]]", "[[estimate-hi-writes-frontier]]"]
origin: raw/2026-09-23/1126/ledger.md#case-363
sprint: migration
created: 2026-09-23
tags: [session, harness, workflow]
---

## Context

`/hi` writes `frontier.md`, and its lines are closed in the replies of Plan Mode, all inside Claude Code's plan mode, whose text forbids any edit but the plan file. The leave exists already: `rule-permissions` counts the Frontier among the session's own working files, and `settings.json` allows `Write` of `vault/raw/**/frontier.md`; the lesson `lesson-plan-mode-frontier-refused-on-the-client-text` (2026-09-16) recorded the same refusal. Neither the page nor the lesson is in the agent's context at `/hi`, and in this session the refusal came again. The rule must stand in the text of the skill itself.
`rule-skill-hi` stands `draft`; the Case touches `estimate-hi-writes-frontier`, not `estimate-hi-no-read-calls`; the lesson is of another session, so no `{addresses:…}` mark; no `create`.

## Problem

The text of `/hi` says to write `frontier.md`; Claude Code's plan mode says to write nothing but the plan file. The agent resolves the conflict for plan mode and refuses. The rule must say that plan mode does not stop the write and the closing of the lines of `frontier.md`.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-363
