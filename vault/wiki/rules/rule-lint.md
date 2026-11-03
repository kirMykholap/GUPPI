---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: built
enforcement: check
implementation_ref: [.guppi/guppi/lint.py, .guppi/guppi/check.py, .guppi/tests/test_lint.py, .guppi/tests/test_check.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-lint-catches]]", "[[estimate-lint-finds-a-broken-link]]", "[[estimate-lint-checks-the-statuses]]", "[[estimate-lint-checks-the-method]]", "[[estimate-lint-catches-a-broken-fence]]", "[[estimate-lint-reports-a-method-tied-to-a-one-off-moment]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Purpose

Prevents a page that breaks its schema, points at nothing, claims a status its
Estimates do not support, or waits for a reading nobody took from sitting in the vault
unnoticed. Pages are written by the generator;
both drift, and nothing else reads the whole graph at once. Red is a signal, not a
gate: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again; a placeholder is red with the count of its defers.
`uv run --project .guppi guppi check` runs it after `guppi render --check`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds. Where the command `ship` is missing, as in a project that installed GUPPI, it prints one line that it skips that step and runs the other five. All six only report, so no step writes to the tree. It runs every step even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red. With `--exit-zero` it prints one last line `exit code: <n>`, the exit code of the run without the flag, and exits 0, so `/work` loads while the check finds something, and the librarian's run and the job `lint` of CI, which run it with no flag, stay red. It needs no tool but `uv`, so a project runs it on any machine. `parent: rule-harness` names the
MOC of the harness tools: lint runs with the renderer, in no phase of the session. Where the module of the command `ship` stands, as in the repository that builds the clean version of GUPPI, `guppi lint` also reports each rule or entity with `core: true` that is `draft` and whose History holds no line that set it `built`, or one of whose Estimates stands `failed`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line. Where the module of the command `ship` is missing, lint also gives no finding on a `draft` rule or entity with every Estimate `passed`, since the clean version keeps the status of a page and writes only its `passed` Estimates. The
classes and their order live in the docstring of `.guppi/guppi/lint.py`.

## History

- 2026-11-03 shipped with GUPPI
