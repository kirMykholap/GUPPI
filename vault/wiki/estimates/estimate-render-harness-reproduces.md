---
type: estimate
kind: QA
status: pending
target: "[[rule-render-harness]]"
purpose: guppi render writes each governed harness file from its Rule pages, parses every json target before it writes, and --check names a file that differs
method: "pytest tests/test_render.py, plus by hand on the live vault after a later librarian's render: git diff --stat, then guppi render --check"
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Criterion

When:
`uv run guppi render` runs without a flag or with `--check`, and reads the Rule pages under `vault/wiki/rules/` that carry `enforcement: render`.

Then:
The Render of a `full` page becomes the whole file its `governs` names, without the page's outer markers. Each `<!-- child -->` line is replaced by that child's text in the order of `children`, and the child's markers are kept.
**＋** A file that cannot hold a comment, a `.json` target, takes each child's text without the child's markers.
**＋** A `partial` page whose file no `full` page owns is spliced between its markers in the existing file, and the markers stay. A target without those markers gives exit 1, and nothing is written.
**＋** A child without `enforcement: render` contributes nothing and needs no marker. A marker line for it in the parent's text gives exit 1, and nothing is written.
**＋** Every `.json` target is parsed before anything is written. One that does not parse stops the whole write, stderr names the file and the page that owns it, and the run exits 1.
**＋** `--check` names each file that differs, exits 1 and writes nothing. When every file is identical, it exits 0.
**＋** Against the live vault, after `uv run guppi render`, `git diff --stat` names only the governed files whose Rule page changed since the last render. The diff of each is the text of that page's Render, and `uv run guppi render --check` then exits 0.
**－** No file type other than `.json` is parsed.

## Result

block 139.1, the probe 2026-09-14 session O: a new `.claude/agents/probe-guppi.md` written mid-session → Agent tool "Agent type 'probe-guppi' not found", the list unchanged (ask-guppi, librarian-guppi, built-ins); the body replaced and called again → not found again; Claude Code 2.1.228, no compaction between the steps; the file removed, `.claude/` clean — in this client the agent list is read at session start, an agent rendered mid-session is usable from the next session

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-10 updated: criterion: a full page with a child that is not a render page renders without it, and errors on a marker line for it · raw/2026-09-10/ledger.md#case-36.2
- 2026-09-12 updated: CLAUDE.md is a full render target; pending for the next session's render (cases 59.8, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L154
- 2026-09-12 criterion: case 85.1 added · [[decision-case-85.1]]
- 2026-09-12 criterion: case 88.1 added · [[decision-case-88.1]]
- 2026-09-12 updated: the stale live clause of cases 18.1 and 59.8 leaves the Criterion prose (case 88.1) · [[decision-case-88.1]]
- 2026-09-12 criterion: case 89.4 added · [[decision-case-89.4]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L48
- 2026-09-14 criterion: case 139.1 added · [[decision-case-139.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L28
- 2026-09-29 updated: the Criterion replaced whole — the unit paragraph and the blocks 85.1, 88.1 and 89.4 into one When and Then, the one-time probe of 139.1 out; purpose and method set, Context and Method out (case 498.1) · [[decision-case-498.1]]
