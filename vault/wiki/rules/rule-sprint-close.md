---
type: rule
kind: Leaf
purpose: Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow
status: draft
enforcement: check
implementation_ref: [guppi/sprint_close.py, tests/test_sprint_close.py]
estimates: ["[[estimate-sprint-close-archives-the-decisions]]", "[[estimate-sprint-close-archives-done-insights-and-lone-lessons]]", "[[estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]]", "[[estimate-sprint-close-settles-unread-estimates]]", "[[estimate-sprint-close-runs-in-the-librarian-run]]", "[[estimate-sprint-close-takes-the-readings-in-groups]]", "[[estimate-sprint-close-next-session-opens-the-sprint]]"]
applies_to: ["[[entity-sprint]]"]
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Purpose

Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. `uv run guppi sprint-close --sprint <id>` closes `entity-sprint-<id>`: without `--apply` it prints what the close would move, what it keeps and each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`, and changes nothing; with `--apply` it sets `archived` on each page the close moves, with a History line, and runs `guppi cleanup`, which moves them (case 627.1). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4); the run takes the choices by slug, `--carry <slug>` and `--archive-unread <slug>`, an Estimate read now being read before the run, and refuses, moving nothing, while a listed Estimate has neither passed nor been named. An Estimate that the sprint page lists is read now or archived unread with the sprint page, never carried, so the close goes ahead with the sprint page's own Estimates not passed; one read now whose reading came out `failed` goes to the archive with the sprint page with no choice by name, and any other Estimate whose reading came out `failed` is carried by `--carry`; the record of the close keeps its status (case 627.4). Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Where the close runs — who calls the command and at what moment — and how the next sprint opens are set in `## How it works` of this page (case 628.1).

## How it works

The close runs in a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes: the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices; Work Mode leaves that line, Retro counts it as waiting, and the librarian runs it after `guppi generate` and before `guppi cleanup`, so that the readings of that session count; the command ticks its line, found by `render.command_line`, once it moved the pages (case 628.1).

Before the closing Case, the session sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2).

No sprint is open from the close until a Case of the next session, its first, creates `entity-sprint-<new id>`: the brief of the closing run names that opening first under the Cases of Next session, `/hi` takes no item of `sprint.md` meanwhile, the ledger hook refuses every other decision line of that session but a `defer` until the `create` stands, and every page of the run that writes the new sprint page carries the new id; `guppi sprint` and `make lint` report the missing sprint page until then, and that is expected (case 628.3). The `## Backlog` of a closed sprint page stays in `backlog.md`, since `guppi backlog` reads it under `vault/archive/` too (case 628.12).

## History

- 2026-10-03 created · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-decisions added · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-done-insights-and-lone-lessons added · [[decision-case-612.2]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest added · [[decision-case-612.3]]
- 2026-10-03 estimate estimate-sprint-close-settles-unread-estimates added · [[decision-case-612.4]]
- 2026-10-04 updated: the close is the command guppi sprint-close, its preview and its run with --apply, the choices by slug; the close goes ahead once each Estimate of the sprint page is read or archived unread, a failed reading settling it; the guard named; where the close runs pointed to How it works (case 627.1) · [[decision-case-627.1]]
- 2026-10-04 updated: where the close runs, in How it works: the librarian's run of a session of its own, from the closing Case's task line; the readings taken in groups first; the next sprint opened first by the next session; the Backlog of a closed sprint kept in backlog.md (case 628.1) · [[decision-case-628.1]]
- 2026-10-04 estimate estimate-sprint-close-runs-in-the-librarian-run added · [[decision-case-628.1]]
- 2026-10-04 estimate estimate-sprint-close-takes-the-readings-in-groups added · [[decision-case-628.2]]
- 2026-10-04 estimate estimate-sprint-close-next-session-opens-the-sprint added · [[decision-case-628.3]]
