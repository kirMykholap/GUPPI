---
type: estimate
kind: QA
status: passed
target: "[[rule-search-leaves-out-decisions]]"
purpose: Whether every Grep over vault/wiki/ or a folder that holds it runs with !**/decisions/** at the end of its glob, added by the PreToolUse hook, and prints nothing under vault/wiki/decisions/
method: uv run --project .guppi pytest .guppi/tests/test_grepguard.py, then by hand in Work Mode a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/, recorded in the estimate line
checked: 2026-10-30
origin: raw/2026-10-05/1616/ledger.md#case-664.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, session]
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

2026-10-30, Work Mode and Retro of session 0304, uv run --project .guppi pytest .guppi/tests/test_grepguard.py and a Grep of ^origin: over vault/wiki/ with no glob: 30 passed; in the main agent the Grep printed 480 files and none under vault/wiki/decisions/, which holds 367 files; in a general-purpose subagent the same Grep printed 480 files and none there, and its transcript shows the hook's updatedInput with glob !**/decisions/**

## History

- 2026-10-05 created · [[decision-case-664.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L4
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — the hook refuses the Decision reads of ask-guppi alone (case 925.2) · [[decision-case-925.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/0304/ledger.md#L38
