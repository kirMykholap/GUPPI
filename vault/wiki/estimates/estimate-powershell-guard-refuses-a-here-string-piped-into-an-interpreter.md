---
type: estimate
kind: QA
status: passed
target: "[[rule-powershell-guard]]"
purpose: A here-string piped into an interpreter is refused before a PowerShell call runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
method: "uv run --project .guppi pytest .guppi/tests/test_powershellguard.py; after the librarian's run of this session renders rule-hook-registry: the PowerShell entry of .claude/settings.json read against the Criterion"
checked: 2026-10-13
origin: raw/2026-10-13/1426/ledger.md#case-796.2
sprint: plugin
created: 2026-10-13
tags: [hooks, harness]
---

## Criterion

When:
The agent calls `PowerShell`, and `uv run --project .guppi guppi powershellguard` of `.guppi/guppi/powershellguard.py` on `PreToolUse` reads `tool_input.command` of the payload and finds every here-string: the text from a line that ends with `@'` or `@"` to a line that opens with `'@` or `"@`.

Then:
A here-string whose closing line pipes it into an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) exits 2 with the reason on stderr: `powershellguard: here-string refused — it is piped into <interpreter>. Write a whole file with the Write tool and change a file with Edit, never through PowerShell; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
**＋** Before the refusal one line `- HH:MM:SS <stamp> powershellguard refused: <reason>` goes to `raw/<date>/event_log.md`.
**＋** `.guppi/guppi/powershellguard.py` judges the interpreter by the function of `.guppi/guppi/bashguard.py` that the Bash check calls, and keeps no list of its own.
**＋** `.claude/settings.json` registers the hook on `PreToolUse` with the matcher `PowerShell`, by the Render of `rule-hook-registry`.
**＋** A here-string not piped into an interpreter, a command without a here-string, another tool — exit 0; a payload the hook cannot read — exit 0 with one line on stderr.
**－** A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` are no reason to refuse.
**－** The hook never raises.

## Result

2026-10-13, uv run pytest tests/test_powershellguard.py and .claude/settings.json; 11 passed; the PreToolUse list holds { "matcher": "PowerShell", "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] } right after the Bash entry of uv run guppi bashguard (lines 41–42); guppi/powershellguard.py imports interpreter from guppi.bashguard and keeps no list of its own

## History

- 2026-10-13 created · [[decision-case-796.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L1
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
