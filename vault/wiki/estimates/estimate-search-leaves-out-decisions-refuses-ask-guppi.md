---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether the PreToolUse hook grepguard refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ made by ask-guppi, and leaves the same calls of every other agent unchanged
method: "by hand, after the librarian's run that renders vault/wiki/orchestration.md, .claude/agents/ask-guppi.md and .claude/rules/search-leaves-out-decisions.md with the trial of this hook by a deliberate start of ask-guppi: uv run --project .guppi pytest .guppi/tests/test_grepguard.py, and, in the Work Mode of the session whose brief puts this reading under Work, the main agent starts ask-guppi with a prompt that names the trial and asks it to Read one named page under vault/wiki/decisions/ and to Grep inside that folder; each of the two calls in the transcript of ask-guppi read against the Criterion, both parts recorded in one estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
---

## Criterion

When:
`ask-guppi` calls Read with a `file_path` under `vault/wiki/decisions/`, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Read` and of `Grep` in `.claude/settings.json`, reads the call with `agent_type` `ask-guppi`.

Then:
The hook refuses the call by `permissionDecision: deny`, with a reason that names the path and `rule-search-leaves-out-decisions`, and exits 0; the call does not run.
**＋** The same Read or Grep by the main agent, by `case-guppi` or by the librarian passes unchanged.
**＋** A Read of `ask-guppi` outside `vault/wiki/decisions/` passes unchanged, and a Grep of `ask-guppi` over a folder that holds `vault/wiki/decisions/` gets the exclusion at the end of its `glob`, as for any agent.
**－** A Glob of `ask-guppi` that prints the path of a Decision page passes: a path is no text of the page.
**－** A payload the hook cannot read, or an error, lets the call pass, with one line on stderr.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
