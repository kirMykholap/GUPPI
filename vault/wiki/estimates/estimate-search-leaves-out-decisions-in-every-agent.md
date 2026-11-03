---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches case-guppi only for a reason its frame names, the main agent for none and ask-guppi by no call
method: "by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md and .claude/agents/ask-guppi.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line"
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, session]
core: true
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

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
