---
type: lesson
kind: knowledge
root_cause: "Claude Code picks up the .claude/settings.json that /guppi:install copies into the project within the same session, so its hooks run uv run --project .guppi at the next tool call: they build .guppi/.venv before uv sync, and fail once the rollback removes .guppi."
status: new
source: transcripts ~/.claude/projects/C--tmp-guppi-0327-a/c284601c-1d50-48ed-962d-63eac2339d96.jsonl and ~/.claude/projects/C--tmp-guppi-0327-c/56092f88-81bd-4a96-93a6-1016446027ce.jsonl
origin: raw/2026-10-29/0327/ledger.md#L44
sprint: plugin
created: 2026-10-29
tags: [plugin, hooks]
---

## Trigger

In install A of session 0327, .guppi/.venv of the project was made at 17:59:19, two seconds before /guppi:install ran uv sync at 17:59:21, which printed "Checked 9 packages"; in install C, after the rollback each command of that session showed a hook error that .guppi does not exist.

## Root cause

Claude Code picks up the .claude/settings.json that /guppi:install copies into the project within the same session, so its hooks run uv run --project .guppi at the next tool call: they build .guppi/.venv before uv sync, and fail once the rollback removes .guppi.

## History

- 2026-10-29 created · raw/2026-10-29/0327/ledger.md#L44
