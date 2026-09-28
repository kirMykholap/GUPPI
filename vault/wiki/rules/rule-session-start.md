---
type: rule
kind: MOC
purpose: Prevents a working session from starting against unknown state
status: draft
parent: "[[rule-session]]"
children: ["[[rule-skill-hi]]", "[[rule-event-log]]", "[[rule-ledger-write]]", "[[rule-compact-recall]]"]
estimates: ["[[estimate-session-start-context]]"]
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## Purpose

Prevents a working session from starting against unknown state — and, just as importantly,
prevents decisions being recorded into a session that has none of that state.

## How it works

### Two kinds of session

**Ordinary session** — the person opens a conversation. Nothing is loaded, no governance
applies. This is the default, and it is deliberate: not every conversation is project work.

**Working session** — the person invokes `/hi`. The skill runs, and only then may the vault
be written to.

Children 2–4 are hooks. Children 2–3 run in **every** session, ordinary ones included, and that is
precisely what lets the ledger tell the two apart.

### Order

The skill (1) resolves before the agent's first turn — bash substitutions in a command body
are not steps the agent performs, they are already done by the time it reads anything.

The ledger hook (3) must come after the event log (2), because it cannot decide whether to
write until the log has recorded whether `/hi` happened.

Child 4, `rule-compact-recall`, runs only after a compaction, and prints only with a `hi` in the window (case 287). The hook registry that records the registration of children 2–4 is not a step of the session; it lives under `rule-harness` with the other tools.

### Why the split is where it is

`rule-skill-hi` is itself a MOC: it holds the frame of the skill file and renders in full,
while its three children splice into that frame in order. A rendering MOC is the one case
where a MOC carries `enforcement` — the frame is not separable from the grouping, and
splitting it into "a MOC plus a Leaf holding an empty template" would be two pages
describing one thing.

Inside it, the `@`-imports from the vault fail the same way — missing file, wrong path —
so they are one Leaf. `git pull` and `gh issue list` fail differently, on merge conflicts
versus authentication, so they are separate.

### The Frontier

Assembled from what was loaded: `brief.md` + `sprint.md` + open issues, plus the unfinished
plan if we are on a plan branch. The agent's first turn presents it as a list — tasks,
problems, debt carried over, where the sprint stands. The human picks the order or defers
items outright.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-12
- 2026-09-09 updated: rule-hook-registry is the fourth child · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-10 updated: rule-hook-registry moves under rule-harness · raw/2026-09-10/ledger.md#case-39
- 2026-09-10 status: draft → built · cascade
- 2026-09-21 child rule-compact-recall added · [[decision-case-287]]
- 2026-09-21 updated: rule-compact-recall is the fourth child — the hook that brings the session's load back after a compaction (case 287) · [[decision-case-287]]
- 2026-09-21 updated: How it works counts four children — the fourth fires after a compaction only (case 290.2) · [[decision-case-290.2]]
- 2026-09-22 updated: the parent is rule-session, the MOC of the five phases (case 316) · [[decision-case-316]]
- 2026-09-28 status: built → draft · cascade
