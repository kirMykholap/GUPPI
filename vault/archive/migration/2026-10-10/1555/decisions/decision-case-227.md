---
type: decision
case: "227"
status: archived
create: ["[[estimate-sprint-checks-the-file]]"]
update: ["[[rule-sprint]]", "[[rule-lint]]"]
origin: raw/2026-09-17/1119/ledger.md#case-227
sprint: migration
created: 2026-09-17
tags: [harness, sprint, session, workflow, librarian]
---

## Context

`vault/wiki/sprint.md` is the file `guppi sprint` writes from the page `entity-sprint-migration` (case 209); `rule-sprint` (`draft`, `enforcement: check`, `governs: vault/wiki/sprint.md`) keeps it from a hand edit through the governed-files hook, and the librarian rewrites it after `render` on every run. The harness files with a Render have a second guard in `render --sync`: the `SessionStart` hook prints a diff and rewrites a file that drifted from its page, `/hi` shows it on the `Render:` line, and `make lint` catches the drift with `render --check`. `sprint.md` has neither: `render` does not know it, `make lint` does not compare it; a drift is possible when a librarian run fails between `generate` and `sprint`, or the file is edited past the hook. Flag 3 of the 2238 handoff asked whether it needs a check at `SessionStart` like `render --sync`. The Case creates one promise of `rule-sprint` and does not touch `estimate-sprint-renders-the-backlog`; the slug `estimate-sprint-checks-the-file` is free. The `Makefile` is an `implementation_ref` of `rule-lint`, not a governed file.

## Problem

The file `/hi` assembles the Frontier from is checked against its page by nobody; a drift is seen only by eye.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-227
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
