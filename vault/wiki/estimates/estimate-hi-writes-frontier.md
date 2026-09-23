---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
method: "one reading by hand at the first /hi of the next session, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
checked: 2026-09-23
origin: raw/2026-09-12/ledger.md#case-59.2
sprint: migration
created: 2026-09-12
tags: [session, harness, workflow]
---

## Criterion

Given:
The librarian writes `brief.md` by the frame — the Render of `rule-brief`; `/hi` reads `sprint.md`, `brief.md`, the tail of the ledger, `git status` and the output of its own commands — and nothing else.
**＋** `prespec.check_frontier`: the id is the first token after `[ ]`, the closer the last segment after ` · `; a line without `[ ]` is not checked.
**＋** The reading of `estimate-brief-written` is by hand after the librarian's run; of `estimate-hi-writes-frontier` by hand at the first `/hi` of the next session.

When:
The person invokes `/hi`, and the agent assembles the Frontier.

Then:
The Frontier, written to `raw/<date>/<hi HHMM>/frontier.md`, is two lists: `## Cases`, lines `- [ ] C<n> — <title> · <source>`, and `## Work`, lines `- [ ] W<n> — <title> · <source>`; an item of the current milestone is a line of its own whose title opens with the slug of each of its pages in a code span (354.3); closed by appending the closer and keeping the source — `- [x] C2 — <title> · sprint · case 315` (case 314.1) — `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`, and `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5); a line of the sprint never closes `· defer case N` (356.2).
**＋** The kind comes from the source. Cases: on a plan branch the unfinished plan, first; the items of the current milestone of `sprint.md`; the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:` — the same thing `render --sync` printed at session start; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
**＋** The milestone is the current one only; a later one, the Backlog and Closed are not items; a decision line of the Tail is not an item.
**＋** In the chat the Cases are shown as a list with their detail — the agenda of Plan Mode; the Work as one block; sub-cases are cut in Cases only.
**＋** A `W` that turns out to need a decision closes `· case N`; a `C` that needs none closes `· work`.
**－** `Pull:` and `Open issues:` are a Cases item only when `sprint.md` names no decision on them; named, they are not an item — `rule-git-context` says the same.
**－** `/pre-spec` finds an open line under `## Cases`; a `W` line stands open until its work is done and closes `· work` in Work Mode (356.1).
**＋** Claude Code's plan mode is on at `/hi`; the agent writes `frontier.md` and closes its lines all the same, with no refusal in the chat (363).

## Result

2026-09-23, the /hi of session 1355 read by hand: plan mode on, frontier.md written with no refusal; ## Cases C1–C8 and ## Work W1–W3 in the line form; C1 the one item of the current milestone Slice 4 with its slug in a code span, Slice 5 and the Backlog not items; C2 from the brief's Next session, C3–C6 its Deferred list, C7–C8 added; W1–W3 the brief's Work list; the failed pull and gh not items, sprint.md names decisions 11.1 and 11.2; closers kept the source (C1 · sprint · sprint, C3 · defer case 380); no W turned into a Case and no C closed · work — that leg had no instance

## History

- 2026-09-12 created · [[decision-case-59.2]]
- 2026-09-12 criterion: case 73.3 added · [[decision-case-73.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L151
- 2026-09-13 criterion: case 101.4 added · [[decision-case-101.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L37
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-18 updated: the Criterion replaced whole — the Frontier from the current milestone, the lines and their closing kept (case 229.3) · [[decision-case-229.3]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L2
- 2026-09-20 updated: the word moved: /pre-task → /pre-spec in the Criterion, guppi prespec --check and tests/test_prespec.py in method; the promise and the reading unchanged, passed kept (case 265) · [[decision-case-265]]
- 2026-09-20 updated: the Criterion replaced whole — the Frontier in two lists, the kind of an item by its source, pull and gh by the sprint page; method names prespec (case 268.2) · [[decision-case-268.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L10
- 2026-09-22 updated: the closer `· sprint` (case 310.5) · [[decision-case-310.5]]
- 2026-09-22 updated: the closer is appended, the source stays (case 314.1) · [[decision-case-314.1]]
- 2026-09-23 updated: the Criterion names the line of a sprint item with its slugs in code spans (case 354.3) · [[decision-case-354.3]]
- 2026-09-23 updated: the Criterion names the W line open until its work is done (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: the Criterion names the sprint line never deferred (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 updated: the Criterion names the write of frontier.md in plan mode (case 363) · [[decision-case-363]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L44
