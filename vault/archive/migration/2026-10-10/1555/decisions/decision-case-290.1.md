---
type: decision
case: "290.1"
status: archived
update: [glossary]
origin: raw/2026-09-21/0019/ledger.md#case-290.1
sprint: migration
created: 2026-09-21
tags: []
---

## Context

288.1 and 288.3 take the glossary out of `CLAUDE.md`, but `glossary.md` itself says in its header "Rule-class; imported into `CLAUDE.md`", and its row "`CLAUDE.md`, `case-schema.md`, `index.md`" that `@path` expands it inline. It is a Rule-class file, changed only by an `update` with `file`, by hand. 287 gives `rule-session-start` a fourth child, but the page's How it works says "Children 2–3 are hooks. They run in every session" and "the registration of children 2–3". 286 and 288.1 replaced the Criterion of two Estimates, and their `purpose` — "in the Spec beside its yaml", "sprint.md, brief.md and case-schema.md" — stayed from the old promise; the Purpose of `rule-case-protocol`, one line above the replace of 288.2, still says "loaded by `/hi` with `sprint.md` and `brief.md`".
Three pages and two Estimates; no Criterion is touched: a `purpose` is the index line, not the promise; the Purpose of a rule touches no Estimate (187). Updates with a `ref`; the vault asked at pre-spec.

## Problem

After this session's render four texts contradict what is ratified: the glossary names its old path, the page of the session start counts its children, two index lines and a Purpose describe the previous promise.

## History

- 2026-09-21 created · raw/2026-09-21/0019/ledger.md#case-290.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
