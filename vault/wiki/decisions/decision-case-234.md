---
type: decision
case: "234"
status: current
update: [entities-schema-yaml]
origin: raw/2026-09-17/1119/ledger.md#case-234
sprint: migration
created: 2026-09-17
tags: []
---

## Context

`entities/schema.md` names `## Milestones`, `## Backlog` and `## Closed` as the sections of the sprint page (case 229.1). Lint compares the prose of a schema with its `schema.yaml` (`schema-prose`) and printed, in Work Mode: `schema.md names section ## Milestones, schema.yaml does not`. Case 229.1 named the `.md` alone; the yaml is its own Rule-class file, `entities-schema-yaml`, and is not edited without a ledger line. A fork of Work Mode, brought back as a Case.

## Problem

One lint finding that was not there before Work Mode; a one-line edit of the yaml, unratified.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-234
