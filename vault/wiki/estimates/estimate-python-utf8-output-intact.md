---
type: estimate
kind: QA
status: passed
target: "[[rule-python-utf8]]"
purpose: A Python script the agent runs through the Bash tool with no encoding set prints a dash and a character outside the code page of the locale intact, and the hooks keep their output
method: "uv run --project .guppi guppi render --check and json.load of .claude/settings.json; by hand, after a session start: a Python script run through the Bash tool with no encoding in the command prints a dash and a character outside the code page of the locale, and the tool output shows both; the Stop line of guppi context shows its dash"
checked: 2026-10-30
origin: raw/2026-09-30/0248/ledger.md#case-534.1
sprint: migration
created: 2026-09-30
tags: [harness, session]
---

## Criterion

When:
A session starts with `.claude/settings.json` as `uv run --project .guppi guppi render` wrote it from `rule-settings`, and the agent runs a Python script through the Bash tool, with no encoding set in the command, that prints a dash and a character outside the code page of the locale.
**＋** The hooks of `.claude/settings.json` run in the same session.

Then:
`.claude/settings.json` carries `"PYTHONUTF8": "1"` under `env`, the text of `rule-python-utf8`.
**＋** The script runs in UTF-8 mode, and the dash reaches the agent in the output of the Bash tool as the dash, not as U+FFFD.
**＋** The character outside the code page of the locale prints, and the script does not stop at the print.
**＋** The output of a hook of `.claude/settings.json` reaches the agent as before, its dashes kept.
**－** The Render of `rule-python-utf8` holds no key other than `PYTHONUTF8`.

## Result

2026-10-30, Retro of session 2341: uv run --project .guppi guppi render --check exit 0; json.load of .claude/settings.json gives env {'PYTHONUTF8': '1'} and no other key; python -c run through the Bash tool with no encoding in the command printed "dash — ж 中" with utf8_mode 1 and the locale code page cp1252, so the dash and two characters outside that code page reached the agent and the script did not stop; the Stop and UserPromptSubmit lines of the hooks in this session reached the agent with their dashes

## History

- 2026-09-30 created · [[decision-case-534.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L41
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-17 updated: the purpose and the method name the code page of the locale, not cp1252 · [[decision-case-875]]
- 2026-10-30 updated: the Criterion replaced whole — the character lies outside the code page of the locale, not cp1252 · [[decision-case-918.3]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L39
