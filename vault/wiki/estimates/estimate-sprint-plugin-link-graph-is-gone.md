---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether, after the librarian's run that deletes the graph of links, no .guppi/links.md, no command guppi links and no SessionStart hook for it stand, its pages and Estimates are archived, no live text names them and the tests pass
method: "by hand, after the librarian's run that applies the delete of entity-link-graph and renders .claude/settings.json: the output of uv run --project .guppi guppi links entity-guppi, of git status, of uv run --project .guppi guppi test and of a Grep for links.md, guppi links and graph of the links over vault/wiki/, .claude/, .guppi/guppi/ and .guppi/tests/, and the SessionStart key of .claude/settings.json, read against the Criterion, the outputs in the estimate line"
origin: raw/2026-11-02/0039/ledger.md#case-999.1
sprint: plugin
created: 2026-11-02
tags: [sprint, harness]
once: true
---

## Criterion

When:
The librarian's run applies the `delete` of `entity-link-graph` and `rule-link-graph-at-session-start` and renders `.claude/settings.json` from `rule-hook-registry`, after the Work Mode that removes `.guppi/guppi/links.py`.

Then:
No file `.guppi/links.md` stands, and no `SessionStart` hook of `.claude/settings.json` runs `guppi links --write`.
**＋** `uv run --project .guppi guppi links` prints that the command is unknown and exits 2.
**＋** `entity-link-graph`, `rule-link-graph-at-session-start`, `estimate-link-graph-prints-the-neighbours` and `estimate-link-graph-at-session-start-writes-the-file` stand in the archive, and no live page lists them in a field.
**＋** No live page of `vault/wiki/`, no file of `.claude/` and no file of `.guppi/guppi/` or `.guppi/tests/` names `.guppi/links.md` or `guppi links`, or counts the graph of the links among the parts of GUPPI or of its harness, outside History lines, a `## Result`, a lesson, the pages under `vault/wiki/decisions/`, `log.md`, `brief.md` and `estimate-sprint-plugin-link-graph-is-gone`.
**＋** `uv run --project .guppi guppi test` reports no failed test.

## History

- 2026-11-02 created · [[decision-case-999.1]]
