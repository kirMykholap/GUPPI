---
type: decision
case: "209.5"
status: archived
update: ["[[rule-documentation]]", "[[estimate-documentation-completes]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209.5
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, librarian, render]
---

## Context

`sprint.md` is the backlog of the sprint `migration`: the goal, the Definition of done, the Slices. It is a working file without a schema: `index.md` §1 says the librarian writes it, lint does not check it, `rule-brief` tells the librarian to change it "only when `handoff.md` tells you to", `/hi` reads it whole through `rule-internal-context`, `cleanup` and `archive` take the sprint id from its first `## migration` heading. The vault, asked through `ask-guppi`: no sprint page, no field from an Entity to a Rule, no render of `sprint.md`; the slugs `rule-sprint` and `entity-sprint-migration` are free; the tag `sprint` is not declared. The governed-files hook (`guppi/guard.py`) refuses an edit of any file a live Rule page names in `governs`, whatever the rule's force. `built` is computed by the cascade of `generate` once every Estimate of the page is `passed`. This Case touches no Estimate: the page is new; its Estimate is created by 209.1.

## Problem

The close of an item in a session does not reach the sprint: the file is rewritten by hand a session later, and each time it is a Case of its own (F7 today, flag 5 of the handoff). No mechanism lets the `built` of a page close an item of the backlog. The sprint is the one file that says what gets built, and the one file whose state nobody computes.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-209.5
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
