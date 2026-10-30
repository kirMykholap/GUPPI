---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches case-guppi only for a reason its frame names, the main agent for none and ask-guppi by no call
method: "by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md and .claude/agents/ask-guppi.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line (the render of case 925)"
checked: 2026-10-30
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
---

## Criterion

When:
A session starts after `uv run --project .guppi guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

Then:
`.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
**＋** The text of a Decision page reaches `case-guppi` only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md`: a page of its answer carries `deferred_by`, or the question asks why something was decided.
**＋** The text of a Decision page reaches the main agent for no reason, and reaches `ask-guppi` by no call.
**－** An `addressed_by` that names a Decision page is no reason to read it.
**－** Whether the hook refuses a Read or a Grep of `ask-guppi` on a Decision page is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
**－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
**－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
**－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

## Result

2026-10-30, Retro of session 1713, the context of the main agent and the transcripts of the ten subagents of the session: "The text of Decision pages stays out of every search" stands in each; the main agent read no Decision page; ask-guppi ran no Read or Grep on vault/wiki/decisions/; case-guppi read decision-case-834, 848, 897.3, 907, 909 and 911, each in the deferred_by of the page of its item, and decision-case-897 and 793, the parent and the superseded Case that 897.3 names, on the same page's deferred decision; no Grep inside vault/wiki/decisions/

## History

- 2026-10-05 created · [[decision-case-640]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1343/ledger.md#L10
- 2026-10-05 updated: the Criterion replaced whole — the load of the file and the reads of Decision pages only; the Greps move to estimate-search-leaves-out-decisions-by-the-grep-hook; purpose and method set anew (case 664.2) · [[decision-case-664.2]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.11]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end, and the method waits for the event it names · [[decision-case-823.1]]
- 2026-10-30 updated: the Criterion replaced whole — ask-guppi reads no Decision page, case-guppi keeps the reasons of its frame (case 925.3) · [[decision-case-925.3]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/1713/ledger.md#L28
