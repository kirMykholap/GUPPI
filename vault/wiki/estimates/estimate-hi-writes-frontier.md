---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-hi]]"
method: "by hand: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
checked: 2026-10-10
origin: raw/2026-09-12/ledger.md#case-59.2
sprint: migration
created: 2026-09-12
tags: [session, harness, workflow]
---

## Criterion

When:
The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md`, the output of the skill's commands and, in the session that opens a sprint, the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, and closes its lines in Plan Mode.

Then:
The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
**＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case of `/sprint-open`; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone of `vault/wiki/sprint.md`, or, while that opening line stands, the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file of the opening Case, with the source `sprint`; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
**＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page, or the opening Case, gives it, with the source `sprint` alone. The agent judges the sameness by meaning, with no page opened.
**＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
**＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`. An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it, and a sprint item never closes `· defer case N`.
**＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
**＋** When the first reply of `/hi` shows the Frontier, the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`, and a `C` that needs none closes `· work`.
**－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of `vault/wiki/sprint.md` is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
**－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
**－** `/pre-spec` finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `raw/<date>/<hi HHMM>/frontier.md`.

## Result

2026-10-10, by hand, the person's answer at the /hi of session 1713, the session that opens the sprint after the close of migration: "Я считаю, что все ок" — the Frontier came out as the Criterion says: raw/2026-10-10/1713/frontier.md with ## Cases, ## Work and ## Ask; `open the next sprint` the first Cases line; no milestone item and no conserved Spec; `Backlog: 3 items` last under Cases, near lines by slug; the chat showed the Cases as a checklist with no bold Case line; C3, of source brief, closed `[-] … · defer case 758` with its short Case; not exercised: an item closed `· sprint · defer` or `· backlog · kept`, and a brief line that repeats a milestone item, since no milestone stood

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
- 2026-09-25 updated: the Criterion replaced whole — the closer kept; the old Given dropped (case 421.4) · [[decision-case-421.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L32
- 2026-09-27 updated: the Criterion replaced whole — the closers of the standard, conserved Specs first, the backlog counted and its near items named, no Deferred list of the brief (case 451.1) · [[decision-case-451.1]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L18
- 2026-09-29 updated: the Criterion replaced whole — the Cases shown in the chat at /hi as a checklist, no bold line; a W line closes where its work is done (case 508.2, supersedes 507) · [[decision-case-508.2]]
- 2026-09-29 updated: the Criterion replaced whole — the Cases shown in the chat at /hi as a checklist, no bold line; a W line closes where its work is done (case 508.2, supersedes 507) · [[decision-case-508.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L31
- 2026-09-30 updated: the Criterion replaced whole — the list ## Ask with lines A<n>; the line on Pull and Open issues gone with the two commands, carried from case 528.4 (case 531.11, supersedes 528.4) · [[decision-case-531.11]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L5
- 2026-10-04 updated: the Criterion replaced whole — the opening of the next sprint first, no milestone item while it stands (case 628.7) · [[decision-case-628.7]]
- 2026-10-04 updated: the Criterion replaced whole — no conserved Spec is a Cases line while the opening of the next sprint stands (case 632.6) · [[decision-case-632.6]]
- 2026-10-05 updated: the Criterion replaced whole — an open W line whose reading cannot run now is a source of a Cases line (case 670.6) · [[decision-case-670.6]]
- 2026-10-07 updated: the Criterion replaced whole — an item closed defer or kept has no short Case but for the short Case of a take-back; the reading by hand is the person's answer at that /hi (case 723.3) · [[decision-case-723.3]]
- 2026-10-08 updated: the Criterion replaced whole — a brief line that repeats an item of the current milestone makes no line of its own (case 729) · [[decision-case-729]]
- 2026-10-08 updated: the method opens with "by hand", the one spelling of a reading, so lint reads it as one (case 731) · [[decision-case-731]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1713/ledger.md#L14
- 2026-10-10 updated: the Criterion replaced whole — at an opening the Frontier takes the first milestone from the opening Case, and the opening line stands closed · [[decision-case-769.2]]
