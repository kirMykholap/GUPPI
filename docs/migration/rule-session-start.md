---
type: rule
kind: MOC
purpose: Prevents a working session from starting against unknown state
status: draft
children: [rule-skill-hi, rule-event-log, rule-ledger-write]
estimates: [estimate-session-start-context]
origin: TBD
sprint: TBD
created: TBD
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

Children 2–3 are hooks. They run in **every** session, ordinary ones included, and that is
precisely what lets the ledger tell the two apart.

### Order

The skill (1) resolves before the agent's first turn — bash substitutions in a command body
are not steps the agent performs, they are already done by the time it reads anything.

The ledger hook (3) must come after the event log (2), because it cannot decide whether to
write until the log has recorded whether `/hi` happened.

### Why the split is where it is

`rule-skill-hi` is itself a MOC: it holds the frame of the skill file and renders in full,
while its three children splice into that frame in order. A rendering MOC is the one case
where a MOC carries `enforcement` — the frame is not separable from the grouping, and
splitting it into "a MOC plus a Leaf holding an empty template" would be two pages
describing one thing.

Inside it, four `@`-imports from the vault fail the same way — missing file, wrong path —
so they are one Leaf. `git pull` and `gh issue list` fail differently, on merge conflicts
versus authentication, so they are separate.

## Children

1. **[[rule-skill-hi]]** — MOC, `render: full`, `governs: .claude/skills/hi/SKILL.md`.
   Holds the frame of the skill; its children splice into the markers, in order:

   - **[[rule-internal-context]]** — `render: partial`. `@wiki/sprint.md` and
     `@wiki/brief.md`. The glossary, `case-schema.md` and the category schemas arrive
     separately through `@import` in `CLAUDE.md` and are not re-read here.

   - **[[rule-git-context]]** — `render: partial`. `git pull`, then
     `git branch --show-current` and `git status --short`.

     **Branch tells us what kind of start this is.** On `main` or a working branch, no
     plan is open. On a plan branch, unfinished work exists and becomes the first Frontier
     item. This is never restated in `brief.md` — git already knows, and a second source
     of truth eventually disagrees with the first.

     **`git pull` happens here and only here.** Pulling mid-session, after the plan is
     written and half the tasks are ticked, breaks the session.

   - **[[rule-github-issues]]** — `render: partial`. `gh issue list --limit 5`. Deferred
     bugs live here rather than in the vault, so this is how they return.

2. **[[rule-event-log]]** — `hook`. Fires at session start, every session. Records tool
   calls, agent dispatches, commits, test runs. Gitignored: debugging material, not
   traceability. **The `/hi` invocation is recorded by the skill itself**, through a `!`
   substitution in its body — a command typed by the person does not pass through the
   `Skill` tool, so no hook would see it. That record is what makes the log the source of
   truth about which kind of session this is.

3. **[[rule-ledger-write]]** — `hook`, on `Stop`. Reads the reply that just finished, finds
   `- decision[...]`, `- estimate[...]` and `- lesson[...]` lines and appends them verbatim to
   `raw/<date>/ledger.md`, interpreting nothing. `Stop` and not `MessageDisplay`: the latter
   can neither block nor speak (measured 2026-08-29), the former can block with a reason the
   agent reads.

   **Checks `event_log.md` for a `/hi` invocation first.** The instruction to write those
   lines lives in `CLAUDE.md`, so the agent produces them in *any* session — including one
   with no sprint, no branch context and no brief. Without this check the hook would
   silently create a ledger for a session that was never a working session, and the
   librarian would materialize pages from it the next day.

   When the check fails it **blocks and says so**. A silent drop leaves the person
   believing their decisions were recorded.

   `ledger.md` is not created at session start. It comes into existence at the first
   ratified decision — before that there is nothing to record.

## The Frontier

Assembled from what was loaded: `brief.md` + `sprint.md` + open issues, plus the unfinished
plan if we are on a plan branch. The agent's first turn presents it as a list — tasks,
problems, debt carried over, where the sprint stands. The human picks the order or defers
items outright.

## Estimates

- [[estimate-session-start-context]] — QA. After `/hi`, the agent's context contains the
  sprint, the brief, the current branch and open issues, with no read-tool calls having
  occurred; and a `- decision[...]` line emitted without `/hi` does not reach `ledger.md`,
  with the person told why.

## History

- TBD created
