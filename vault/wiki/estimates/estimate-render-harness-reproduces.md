---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
purpose: guppi render writes each governed harness file from its Rule pages, parses every json target before it writes, and --check names a file that differs
method: "pytest .guppi/tests/test_render.py, plus by hand on the live vault after a later librarian's render: git diff --stat, then guppi render --check"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` runs without a flag or with `--check`, and reads the Rule pages under `vault/wiki/rules/` that carry `enforcement: render`.

Then:
The Render of a `full` page becomes the whole file its `governs` names, without the page's outer markers. Each `<!-- child -->` line is replaced by that child's text in the order of `children`, and the child's markers are kept.
**＋** A file that cannot hold a comment, a `.json` target, takes each child's text without the child's markers.
**＋** A `partial` page whose file no `full` page owns is spliced between its markers in the existing file, and the markers stay. A target without those markers gives exit 1, and nothing is written.
**＋** A child without `enforcement: render` contributes nothing and needs no marker. A marker line for it in the parent's text gives exit 1, and nothing is written.
**＋** Every `.json` target is parsed before anything is written. One that does not parse stops the whole write, stderr names the file and the page that owns it, and the run exits 1.
**＋** `--check` names each file that differs, exits 1 and writes nothing. When every file is identical, it exits 0.
**＋** Against the live vault, after `uv run --project .guppi guppi render`, `git diff --stat` names only the governed files whose Rule page changed since the last render. The diff of each is the text of that page's Render, and `uv run --project .guppi guppi render --check` then exits 0.
**－** No file type other than `.json` is parsed.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
