---
type: decision
case: "115"
status: current
update: ["[[rule-git-context]]"]
supersedes: ["[[decision-case-106]]"]
origin: raw/2026-09-14/0747/ledger.md#case-115
sprint: migration
created: 2026-09-14
tags: [session, harness, git]
---

## Context

`git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the pull brings is rendered only at the following session start. Case 89 puts the render in the librarian's phase and leaves this half open. Deferred as 98 in session K. (Case 106 as it stands.)

## Problem

The render has to run once more after the pull, inside `/hi`. It waits for the pull itself, which has no upstream to pull from yet (sprint, Slice 5). (Case 106 as it stands.)

## Given

`rule-git-context` (`Leaf`, `built`, `estimate-git-context-current` `passed`): the Render is the three lines `Pull:`, `Branch:`, `Status:`; "`git pull` happens here and only here"; a failing pull is a Frontier item, not a stop. `rule-skill-hi` carries `deferred_by: [decision-case-106]`; a supersedes clears it wherever it sits.
**＋** `guppi render --sync` (`rule-render-harness`, case 59.7): prints a unified diff for each differing file, then writes it; exit 0 always; a `.json` that does not parse stops the write. A run right after a run with nothing changed prints nothing.
**＋** The librarian commits the rendered files with the pages (case 89.2), so a pull that brings pages brings their render too; the line catches a commit made without the render and a hand edit made between the session start and the pull.
**＋** The `/hi` skill already says: "what `guppi render --sync` printed at session start is an item when it shows a hand edit" — the same sentence covers this line.
**－** Not measured: whether `!` substitutions of one skill resolve in document order, so that the render runs after the pull. The reading says; if they resolve together, the line still reports what differs, one pull late.
**－** `rule-skill-hi` is not changed here (111.4 changes it); `rule-render-harness` is not changed: the command and its contract stay.
**－** The Frontier line F3 closes on this Case.

## Criterion

- [[estimate-git-context-current]] § case 115

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-115
