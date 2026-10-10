---
type: decision
case: "268.1"
status: archived
update: ["[[rule-brief]]", "[[estimate-brief-written]]", "[[rule-carry-over]]"]
origin: raw/2026-09-20/0958/ledger.md#case-268.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, librarian, session, render]
---

## Context

`/hi` assembles the Frontier as one list `F<n>`, and every line closes as `case N`, `work` or `defer case N`, or `/pre-spec` refuses. One list holds items that need a judgment, readings and commits that are simply done, and `git pull`/`gh`, whose decision already stands in `sprint.md` — closed anew every session. The kind of an item the agent decides today by re-reading the brief; the librarian judges it already — it writes "a Case of the next Plan Mode", "readings due", "standing" in Flags — but as one text. When the brief carries that sort explicitly, `/hi` copies it without opening a page: the kind comes from the source. `prespec.check_frontier` reads the id as the first token and the closer as the last segment — any id fits. The Case changes `rule-brief` with `estimate-brief-written` and `rule-skill-hi` with `estimate-hi-writes-frontier`; `estimate-hi-no-read-calls`, `rule-prespec` and its tests are not touched.

## Problem

One list mixes three kinds of item, the agent cannot see where sub-cases are cut, and what is decided comes back every session. Needed: the kind of an item set by its source, not by reading pages; the librarian sorts, `/hi` places.

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#case-268.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
