---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether every Grep over vault/wiki/ or a folder that holds it runs with !**/decisions/** at the end of its glob, added by the PreToolUse hook, and prints nothing under vault/wiki/decisions/
method: uv run pytest tests/test_grepguard.py, then by hand at the /hi of a later session after the render a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/
checked: 2026-10-05
origin: raw/2026-10-05/1616/ledger.md#case-664.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, session]
---

## Criterion

When:
The main agent or any subagent calls Grep, and `uv run guppi grepguard` of `guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

Then:
When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
**＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
**＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
**＋** A call of the librarian is changed in the same way as a call of any other agent.
**－** A Grep whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
**－** A Grep whose `path` is one file, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
**－** The hook never refuses a call; a payload it cannot read or an error lets the call pass unchanged.

## Result

2026-10-05, /hi of 1831, uv run pytest tests/test_grepguard.py 15 passed; a Grep ^status: current over vault/wiki with no glob printed 0 files in the main agent and 0 in a general-purpose subagent, while the same Grep with path vault/wiki/decisions counted 1146 files, unchanged by the hook; uv run guppi grepguard registered on PreToolUse of Grep in .claude/settings.json

## History

- 2026-10-05 created · [[decision-case-664.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L4
