---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches them only by a Read of its path, or a Grep inside vault/wiki/decisions/, for a reason their frame names
method: "by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 664.1, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line"
checked: 2026-10-05
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
---

## Criterion

When:
A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

Then:
`.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
**＋** The text of a Decision page reaches one of these agents only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi` — a page of its answer carries `deferred_by`, or the question asks why something was decided — and for no reason in the main agent.
**－** An `addressed_by` that names a Decision page is no reason to read it.
**－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
**－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
**－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

## Result

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-05, at the /hi of session 1343, by hand: the transcripts of session 0311 (6d53e05d) after the render by case 640 at the librarian's run of session 0109 — the main agent, case-guppi a565a08d267ecaa66, a1cf96ac9df5edd1c, a7b182c9a1f27f641, ask-guppi a055d35695650c13f, af56f988c579ddc06, af7cde916f5b24293: .claude/rules/search-leaves-out-decisions.md stands in all seven contexts; 9 Greps whose path is vault/, vault/wiki/ or the repository root carry no !**/decisions/** in their glob — main agent 1 (path vault, glob **/{handoff,work}.md), a565a08d267ecaa66 1 (path vault, no glob), a1cf96ac9df5edd1c 1 (root, {guppi/**,tests/**}), a7b182c9a1f27f641 5 (vault/wiki with globs of named files twice, root *.py three times), af56f988c579ddc06 1 (root, *.py, named in its own answer); none printed a line of a page under vault/wiki/decisions/; Reads of a Decision page: a565a08d267ecaa66 decision-case-442, the deferred_by of rule-ledger-write, a reason of .claude/agents/ask-guppi.md; a1cf96ac9df5edd1c decision-case-432, the addressed_by of insight-workflow-case-schema-silent-on-what-the-scripts-accept, neither reason of that frame; the main agent read none

## History

- 2026-10-05 created · [[decision-case-640]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1343/ledger.md#L10
- 2026-10-05 updated: the Criterion replaced whole — the load of the file and the reads of Decision pages only; the Greps move to estimate-search-leaves-out-decisions-by-the-grep-hook; purpose and method set anew (case 664.2) · [[decision-case-664.2]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.11]]
