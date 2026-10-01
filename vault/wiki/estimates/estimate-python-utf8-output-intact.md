---
type: estimate
kind: QA
status: passed
target: "[[rule-python-utf8]]"
purpose: A Python script the agent runs through the Bash tool with no encoding set prints a dash and a character outside cp1252 intact, and the hooks keep their output
method: "uv run guppi render --check and json.load of .claude/settings.json; then by hand at a later session start: a Python script run through the Bash tool with no encoding in the command prints a dash and a character outside cp1252, and the tool output shows both; the Stop line of guppi context shows its dash"
checked: 2026-10-01
origin: raw/2026-09-30/0248/ledger.md#case-534.1
sprint: migration
created: 2026-09-30
tags: [harness, session]
---

## Criterion

When:
A session starts with `.claude/settings.json` as `uv run guppi render` wrote it from `rule-settings`, and the agent runs a Python script through the Bash tool, with no encoding set in the command, that prints a dash and a character outside cp1252.
**＋** The hooks of `.claude/settings.json` run in the same session.

Then:
`.claude/settings.json` carries `"PYTHONUTF8": "1"` under `env`, the text of `rule-python-utf8`.
**＋** The script runs in UTF-8 mode, and the dash reaches the agent in the output of the Bash tool as the dash, not as U+FFFD.
**＋** The character outside cp1252 prints, and the script does not stop at the print.
**＋** The output of a hook of `.claude/settings.json` reaches the agent as before, its dashes kept.
**－** The Render of `rule-python-utf8` holds no key other than `PYTHONUTF8`.

## Result

2026-10-01, uv run guppi render --check exit 0 at the baseline of session 1237; a Python script run through the Bash tool with no encoding in the command printed "dash: —, outside cp1252: ✓ 中", stdout utf-8, utf8_mode 1, and json.load of .claude/settings.json gave env {'PYTHONUTF8': '1'}, no other key; the Stop hook guppi onward --plan reached the agent with its dashes kept in this session, and the Stop line of guppi context showed its dash, "— past 400 000", in session 2356

## History

- 2026-09-30 created · [[decision-case-534.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L41
