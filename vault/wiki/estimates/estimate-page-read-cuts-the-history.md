---
type: estimate
kind: QA
status: pending
target: "[[rule-page-read]]"
purpose: A Read of a vault page returns its frontmatter and body, and its History only when asked for
method: uv run pytest tests/test_pageread.py, then by hand a Read of a vault page in the main agent and in a subagent after the render
origin: raw/2026-09-25/1228/ledger.md#case-420.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
---

## Criterion

When:
An agent — the main agent or a subagent — calls `Read` on a file under `vault/wiki/`.

Then:
When the call carries neither `offset` nor `limit` and the file holds its own `## History` heading, `uv run guppi pageread` on `PreToolUse` sets `limit` to the line before that heading by `updatedInput`, and the agent gets the frontmatter and the body alone.
**＋** After such a call, `uv run guppi pageread --after` on `PostToolUse` adds one line of `additionalContext`: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows how the page changed.
**＋** The heading is found by the walk of `split_sections` in `guppi/pages.py`, so a `## History` inside a render block of the page does not count.
**＋** An `Edit` of the page after the cut read works as after a whole read.
**－** A call with its own `offset` or `limit`, a file with no `## History`, and a file outside `vault/wiki/` are not changed, and no line is added.
**－** The page on disk is not changed: in Obsidian it shows whole.

## History

- 2026-09-25 created · [[decision-case-420.1]]
