---
type: decision
case: "508.4"
status: current
create: ["[[estimate-brief-carries-the-run-facts]]"]
update: ["[[rule-brief]]", "[[rule-documentation]]"]
origin: raw/2026-09-29/1134/ledger.md#case-508.4
sprint: migration
created: 2026-09-29
tags: [harness, workflow, librarian, session, render]
---

## Context

A reading checks one Estimate against what actually happens and writes the result into the ledger. At `/hi` each `pending` reading becomes a `W` line of the Frontier. Only `/retro` says "take the readings". By then some readings are blocked, because the ledger hook refuses a reading of an Estimate that the same session creates or updates (case 428.1). Other readings are tied to a moment that has already passed. For example, the `method` of `estimate-hi-no-read-calls` names "the /hi of the next session", and the `/hi` reply of this session did not take it; it was read later in the session. So the readings pile up: this session's Frontier opened with 89 reading lines under `## Work`. The librarian is a helper agent and writes no ledger line. Yet the `method` of 32 Estimates names the librarian, counted by a Grep of the `method` lines. The librarian lists these Estimates under Readings due of `vault/wiki/brief.md` with no result. It writes the brief before `guppi archive` and the commit, on purpose: the brief reads the yamls and Specs where they stand, and the librarian may not search `vault/archive/`.

In the rounds the person decided the following:
- `/hi` takes the readings whose `method` names `/hi` or the librarian's run, in its first reply, and closes their `W` lines there.
- A reading whose `method` also names a later moment waits for that moment.
- A reading whose `method` needs a `/hi` run of its own is not taken at `/hi`.
- `/work` gets a step after the last task that takes every other reading it can, in Frontier order, and the person can stop it.
- A `W` line that cannot be read stays open.
- The librarian writes facts, not verdicts: what its run printed or left, on each such Estimate's Readings due line, and the output of `guppi archive` right after that step.
- The commit reading is taken at the next `/hi` from `git log`, `git status` and the previous transcript.
- Each behaviour gets a new Estimate.

Frame found by `case-guppi`:
- The Render of `rule-skill-hi` and the Criterion of `estimate-hi-writes-frontier` both say a `W` line closes "in Work Mode". Closing at `/hi` makes both false, so sub-case 508.2 changes both. A reading taken by `/retro` closes its line at Retro, so the new wording names all three places.

Case 507 and why 508.2 supersedes it:
- Case 507 of this session replaced the same Criterion whole: at `/hi` the chat shows the Cases as the checklist of `frontier.md`, the detail on an indented line, never as a bold line with a paragraph. The person chose that look from four, and kept `rule-orchestration` out of it.
- Two whole replacements of one Criterion would sign it twice. So 508.2 supersedes 507 and carries both of its changes: 507's pair on `rule-skill-hi` for the chat look, and its own pair for closing a `W` line.
- The one Criterion of 508.2 is 507's with two changes. The chat look is described on its own and no longer called the form of the acknowledging reply, since that form folds closed lines and shows no detail line. The `W` closing line is changed.
- 507 leaves the Spec.
- Against the Criterion on the page today, two lines are not carried: the old chat line and the old `W` closing line.

Other frame facts:
- The Render of `rule-skill-hi` assembles the Frontier with "no page opened". That stays: only the new reading step opens the pages of the Estimates it reads.
- The `W` lines are closed in `frontier.md` before the reply that carries the `LEDGER` block, since that reply ends in text with no tool call after it.

Why some `then` lines look alike:
- The reading steps of 508.1 at `/hi` and 508.3 in `/work` use similar words on purpose. They are one kind of step at two moments, each with its own promise, and each can fail apart from the other.
- The line of 508.3 that closes the `W` line before the `LEDGER` reply repeats the matching line of 508.1 on purpose, so that each Estimate reads whole without the other.
- Some lines of 508.2 share words with 508.1 because both describe `frontier.md`.

These Estimates stand, and why:
- `estimate-hi-no-read-calls`: the reading calls come after the skill's output is already in context, so they are not calls "to get any of them".
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: it promises the tasks in order, and its `－` line about ticking no `read` box stays true.
- `estimate-brief-written`: its Criterion promises the sections, their order and their sources. Each Readings due line keeps its three parts, the Estimate, its `draft` rule and where it is read, one line per Estimate. The facts added at the end of the line are promised by the new Estimate of 508.4.
- `estimate-documentation-completes`: the librarian opens an Estimate page for "a fact for the brief", which its frame already lists, and the archive output still goes into the report.

What does not change:
- `rule-retro` keeps its reading paragraph and takes whatever is left.
- The sentence of `rule-case-protocol`, "a `W` line closes when its work is done", names no phase and stays true.

Vault query: every `create` is an Estimate with a `ref`, so no vault query was needed. A Glob found the three new slugs free.

Timing: no hook changes. The skills are rendered at the librarian's run. `/hi` and `/work` act on the new text from the next session. The librarian of this session runs on the frame it loaded at dispatch, so the new brief facts first appear one run later.

## Problem

A Work reading has no trigger before Retro. Readings tied to `/hi` or to the librarian's run pass without being taken, and the other readings pile up until some are blocked.

## Given

`rule-brief` — the page whose Render is the brief section of the librarian's frame; it adds no decision and no judgment of the work
**＋** `rule-documentation` — the page whose Render is the librarian's frame, its reasons to open a page and its archive step
**＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from both
**＋** `vault/wiki/brief.md` — the brief, whose Readings due carry the facts
**＋** `estimate-brief-carries-the-run-facts` — the promise of the facts in the brief
**＋** `rule-raw-archive` — `uv run guppi archive`, the step after the brief
**＋** `rule-close` — the commit of the librarian's run, its last step
**＋** `rule-case-protocol` — only the main agent writes ledger lines

## History

- 2026-09-29 created · raw/2026-09-29/1134/ledger.md#case-508.4
