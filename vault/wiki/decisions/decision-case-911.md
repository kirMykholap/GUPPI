---
type: decision
case: "911"
status: current
defer: ["[[rule-plugin-install]]"]
origin: raw/2026-10-29/1930/ledger.md#case-911
sprint: plugin
created: 2026-10-29
tags: [harness, plugin, render]
---

## Context

The person added this item in this session and put it off at the close of Plan Mode. Step 3 of `/guppi:install` refuses a project that already holds one of the files of GUPPI, such as `.claude/settings.json` or `CLAUDE.md`, and writes nothing there. No page sets how the settings, the hooks and the `CLAUDE.md` of such a project join those of GUPPI.

## Problem

No Case of this session decides how GUPPI installs into a project that already holds its own settings, hooks and `CLAUDE.md`.

## Deferred

### [[rule-plugin-install]]

Lets GUPPI install into an existing project that holds its own .claude/settings.json, hooks and CLAUDE.md, which /guppi:install now refuses whole; put off at the close of Plan Mode

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-911
