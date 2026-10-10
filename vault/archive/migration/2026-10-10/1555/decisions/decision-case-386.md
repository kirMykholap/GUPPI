---
type: decision
case: "386"
status: archived
update: ["[[estimate-sprint-renders-the-backlog]]"]
origin: raw/2026-09-23/1859/ledger.md#case-386
sprint: migration
created: 2026-09-23
tags: [harness, sprint]
---

## Context

`guppi sprint` writes `sprint.md` from the page `entity-sprint-migration`. The current milestone comes out whole; a closed one and a later one as one heading line. After a whole block `render_milestones` puts a blank line; after a collapsed line it puts none, so two collapsed headings stand back to back, as Slice 4 and Slice 5 do now. Markdown reads them anyway, but every other heading of the file stands between blank lines. Only `sprint_id` in `guppi/materialize.py` reads the file by code, and it needs the first `## ` line, so the change does not touch it. `tests/test_sprint.py` fixes the lines back to back: `EXPECTED` and two assertions. The Criterion of `estimate-sprint-renders-the-backlog` describes the layout of the file, so it is replaced whole; the other four Estimates of `rule-sprint` speak of `--check`, the ticks in the Spec and the moves of milestones, and are left alone. The `update` carries a `ref`, so no vault query.

## Problem

The collapsed milestone headings in `sprint.md` stand with no blank line between them, while every other heading of the file is set off by blank lines.

## Given

`guppi/sprint.py` `render_milestones` — writes the milestone lines; the module docstring describes the file.
**＋** `tests/test_sprint.py` — fixes the render on a temp vault.
**＋** `estimate-sprint-renders-the-backlog` — the Estimate of `rule-sprint`; its Criterion describes the file.
**＋** `rule-sprint` — the rule, `governs: vault/wiki/sprint.md`.
**＋** `entity-sprint-<id>` — the one live sprint page the script reads, `entity-sprint-migration` today.
**＋** `vault/wiki/sprint.md` — the file the script writes.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-386
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
