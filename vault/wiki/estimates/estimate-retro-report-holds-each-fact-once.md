---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether the report of /retro holds each fact once — the frontier numbers only what needs an end, the boxes that wait for the librarian one count line and the read lines that wait for a later session one line of slugs; the close holds the Case ids, what got done and the numbers of the frontier with their ends
method: one reading by hand at the first /retro after the render, recorded in the estimate line
checked: 2026-09-27
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes, and the agent writes the frontier and the close.

Then:
The frontier is one numbered list of what needs an end in this Retro: each unticked box that is debt, and what the agent noticed during Work Mode.
**＋** A `read` line without its line in the Tail, whose slug this session neither creates nor updates, is debt, and so is a box of code, a test, a command or a migration left unticked.
**＋** Under the list stand two lines, not numbered: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it.
**－** The frontier names no box that waits for the librarian one by one, and holds no list of the ratifications.
**＋** The close has three parts. Ratified is one line with the ids of the Cases ratified, from `uv run guppi tail`, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page.
**＋** What got done holds the commit, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier.
**＋** What is not done holds each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier.
**－** No Case, box, reading or lesson is named in two parts of the report.

## Result

2026-09-27, by hand, the /retro of session 1819: the opening list named the unticked boxes per Case (update and create lines of each page), the close named every ratification per Case with the same pages again, and "what got done" and "what is not done" repeated parts of the opening list; the person's complaint: the retro repeats the not-done part several times and needs one standard, to be discussed in the next session

## History

- 2026-09-23 created · [[decision-case-376]]
- 2026-09-25 updated: the Criterion replaced whole — a third mark in the opening list: a read line whose reading waits for a later session (case 428.4) · [[decision-case-428.4]]
- 2026-09-27 status: pending → failed · raw/2026-09-27/1819/ledger.md#L39
- 2026-09-27 updated: the Criterion replaced whole and the purpose rewritten — the frontier numbers only what needs an end; the close holds the Case ids, what got done and the numbers with their ends (case 468.1) · [[decision-case-468.1]]
