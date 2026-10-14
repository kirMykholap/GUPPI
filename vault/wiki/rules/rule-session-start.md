---
type: rule
kind: MOC
purpose: Prevents a working session from starting against unknown state
status: built
parent: "[[rule-session]]"
children: ["[[rule-skill-hi]]", "[[rule-event-log]]", "[[rule-ledger-write]]", "[[rule-compact-recall]]", "[[rule-skill-sprint-open]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, hooks]
core: true
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

Child 4, `rule-compact-recall`, runs only after a compaction, and prints only with a `hi` in the window. The hook registry that records the registration of children 2–4 is not a step of the session; it lives under `rule-harness` with the other tools.

### Why the split is where it is

`rule-skill-hi` is itself a MOC: it holds the frame of the skill file and renders in full,
while its three children splice into that frame in order. A rendering MOC is the one case
where a MOC carries `enforcement` — the frame is not separable from the grouping, and
splitting it into "a MOC plus a Leaf holding an empty template" would be two pages
describing one thing.

Inside it, the `@`-imports from the vault fail the same way — missing file, wrong path —
so they are one Leaf. The git commands fail apart from the imports, so they are a Leaf of their own.

### The Frontier

Assembled from what was loaded: `brief.md` + `sprint.md` + the git state and the tail, plus the unfinished plan if we are on a plan branch; in the session that opens a sprint, the first milestone comes from the case file of the opening Case of `/sprint-open` instead of `sprint.md`. The agent's first turn presents it as a list — tasks, problems, debt carried over, where the sprint stands —, but in the session that opens a sprint, whose first turn starts the opening Case of `/sprint-open`: there the Frontier is assembled and written before the reply that acknowledges that Case, and that reply presents it. The human picks the order or defers
items outright.

## History

- 2026-10-14 shipped with GUPPI
