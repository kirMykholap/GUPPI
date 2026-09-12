---
type: decision
case: "85.3"
status: current
update: [rule-hook-registry]
origin: raw/2026-09-12/ledger.md#case-85.3
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Context

The Frontier, the Spec and the handoff are the session's own working files under
`raw/<date>/<HHMM>/`, and the agent writes them many times in one session. Every write
asks the person for permission. The entries that would stop the question belong in
`permissions.allow`. But `.claude/settings.json` has one page for the whole file today —
`rule-hook-registry`, `render_mode: full` — and its Purpose says `defaultMode: plan`
lives there too, "one file has one source". Permissions, the mode and the hook registry
are three rules in one file.

## Problem

How to describe `settings.json` so that permissions have their own rule, the mode has
its own and the hooks have their own, while the file keeps one source.

## Given

The vault, asked through `ask-guppi`: no live or `draft` page is about permission
settings; the only live text is the `permissions` block inside the Render of
`rule-hook-registry` (`built`, `full`, `governs: .claude/settings.json`, Estimate
`estimate-hook-registry-rendered`, `passed`). The slugs `rule-settings`,
`rule-permissions`, `rule-default-mode`, `estimate-settings`, `estimate-permissions` and
`estimate-default-mode` are free; `rule-plan-mode` is taken by the phase of the session.
**＋** `render_full` replaces a `<!-- child -->` line with the child's text wrapped in its
own markers (`guppi/render.py`, `block()`); a marker line must match `^<!-- name -->$`
exactly. `render.plan` already refuses two `full` pages on one file and already requires
a `partial` child to be listed in the owner's `children`.
**＋** JSON holds no comment, so a child spliced with its markers makes the file
unparsable. This is the one thing the `rule-claude-md` pattern does not lend to a JSON
file.
**＋** A marker must be a whole line, so the comma between two JSON keys belongs to the
text of the child that precedes the other.
**＋** `guppi guard` and `guppi lint` read no marker; `pages.py` reads the markers of a
page, not of a file.
**＋** `rule-harness` is a MOC whose `children` hold `rule-hook-registry`; the new MOC
takes that slot.
**＋** The criterion of `estimate-hook-registry-rendered` is the whole file today: the
Render reproduced byte for byte, the file parses as JSON, the next session start writes
its `session-start` line.
**－** Whether Claude Code reads `settings.json` during a session or only at its start is
written nowhere in the vault. If only at the start, the questions stop at the next `/hi`.

## Criterion

- [[estimate-hook-registry-rendered]] § case 85.3

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-85.3
