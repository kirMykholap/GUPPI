---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether every Grep over vault/wiki/ or a folder that holds it runs with !**/decisions/** at the end of its glob, added by the PreToolUse hook, and prints nothing under vault/wiki/decisions/
method: uv run --project .guppi pytest .guppi/tests/test_grepguard.py, then by hand in Work Mode a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/, recorded in the estimate line
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
---

## Criterion

When:
The main agent or any subagent calls Grep, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

Then:
When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
**＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
**＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
**＋** A call of the librarian is changed in the same way as a call of any other agent.
**－** A Grep of an agent other than `ask-guppi` whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
**－** A Grep whose `path` is one file outside `vault/wiki/decisions/`, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
**－** The hook refuses no call but a Read or a Grep of `ask-guppi` on a Decision page, which `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads; a payload it cannot read or an error lets the call pass unchanged.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
