---
type: decision
case: "468.1"
status: current
update: ["[[rule-retro]]", "[[estimate-retro-report-holds-each-fact-once]]"]
origin: raw/2026-09-27/2050/ledger.md#case-468.1
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness, render]
---

## Context

`/retro` opens with a numbered list of what is not done. The list holds every unticked box of `raw/<date>/<hi HHMM>/spec.md`, per Case, each marked as waiting for the librarian, waiting for a later session, or debt. At Retro most of these boxes are the page and render lines of the session's own Cases, so the list names each Case and its pages. The close then names every ratification per Case with the same pages, and "what got done" and "what is not done" repeat parts of the opening list. At the `/retro` of session 1819, `estimate-retro-report-holds-each-fact-once` was read `failed` for this reason (line 39 of `raw/2026-09-27/1819/ledger.md`), and the person asked for one standard. `handoff.md` has the same defect. The handoff of session 1819 named the failed reading both in `## Notes from memory` and in `## What actually got done`, and named the next-session items in the notes and again in the instructions to the librarian.
The person chose one standard for both documents. The frontier numbers only what needs an end in this Retro. The librarian's boxes are one count line, and the later-session `read` lines are one line of slugs. The close has three parts, each fact in one part only. A reading or a lesson that ends an item of the frontier is named under What is not done, not under What got done. The handoff's `## What actually got done` carries the close. The librarian does not read the chat, so this is the one repeat, across two documents for two readers. Inside `handoff.md` each fact stands in one section. The handoff's What is not done differs from the close in three ways, because the file has no frontier. It names each open item in a few words. The text of a note for the handoff, one of the four ends that `rule-retro` allows, stands there as that item's end. The two lines under the frontier stand under it, because the paragraph of `rule-retro` on the readings already sends the later-session Estimates to the handoff.
What the frame changes: the frontier paragraph and the close paragraph of the Render of `rule-retro`, the `purpose` of `estimate-retro-report-holds-each-fact-once`, and the section list of the Render of `rule-handoff`. The section names stay, so `rule-brief` still reads "Where things stand" from `## What actually got done`. `estimate-brief-written` still finds its "handoff flag with a question" in the notes or among the open items. `estimate-retro-loads` promises the readings, not the form of the report, so it is not touched. `estimate-handoff-dispatches` promises the three sections, the dispatch and no commit, which still hold, so it is not touched. `estimate-end-of-work-order` promises the order of the steps, which does not change. The Purpose of `rule-handoff` ("what actually got done") still holds. The one `create` has a `ref`, so no vault query ran. A Glob of `vault/**/` finds no page for `estimate-handoff-holds-each-fact-once`.
Not done: the form of `brief.md` does not change.

## Problem

The account of a session repeats itself. The Retro report names the same Cases, pages and open items in the frontier and in each part of the close. The handoff names the same facts in more than one section. The person reads everything several times, and no text of the vault says which part holds which fact.

## Given

`rule-retro` — its Render, the frontier and the close of `/retro`
**＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
**＋** `estimate-retro-report-holds-each-fact-once` — the promise of the report, its Criterion replaced whole and its `purpose` rewritten
**＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, with its unticked boxes
**＋** `uv run guppi tail` — the Tail of the session's ledger
**＋** `make test` and `make style` — the checks the skill loads before the first turn
**＋** `estimate-retro-loads` — the promise of the readings at Retro, unchanged

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#case-468.1
