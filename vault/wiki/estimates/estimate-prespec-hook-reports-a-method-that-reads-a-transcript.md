---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec reports a method that the plan writes, or that the live page keeps under a new Criterion, whose reading by hand reads the transcript of a session off a sprint page, by one predicate of .guppi/guppi/lint.py, and leaves alone a sprint page, a Criterion written back unchanged, a part with no by hand and the live pages
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k transcript
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file, or the `method` that the live page of an Estimate keeps under an `update` that replaces its Criterion whole.
**＋** Or the check of `.guppi/guppi/casecheck.py` runs the same `judge` of `.guppi/guppi/prespec.py` over the file of a Case that `case-guppi` wrote.
**＋** Or `.guppi/tests/test_prespec.py` and `.guppi/tests/test_lint.py` run them over a made-up plan, made-up pages and made-up methods.

Then:
A `method` that the plan writes, with a part between two `;` that holds `by hand` and names the word `transcript` or the folder `~/.claude/projects/`, gives one line `case N: <create|update> <slug>: method reads the transcript of a session off a sprint page — a lasting method reads a text that ships, and a one-off Estimate of the sprint page reads the transcript`.
**＋** A `method` kept on the live page with such a part gives one line `case N: update <slug>: the method on the page reads the transcript of a session — set a method that reads a text that ships, and read the transcript by a one-off Estimate of the sprint page`.
**＋** The judgment of such a part is one function of `.guppi/guppi/lint.py`, which `.guppi/guppi/prespec.py` imports.
**＋** The check of `.guppi/guppi/casecheck.py` sends back a Case file with the same line.
**－** An Estimate whose target is a sprint page `entity-sprint-<id>`, by `is_sprint_page` of `.guppi/guppi/ledger.py` — the `ref` of a `create`, the `target` that an `update` sets or that the live page holds — gives no such line.
**－** A kept `method` gives no such line when each line of the new Criterion, read by `new_criterion` and `criterion_line` of `.guppi/guppi/prespec.py`, equals the line in its place of the `## Criterion` of the live page, empty lines aside, as when a Criterion is written back to set the Estimate `pending` again.
**－** An `update` that sets `passed` or `failed` by the person's decision, or that names a part of the page alone, keeps no `method` and gives no such line.
**－** A part with no `by hand`, such as a test run over a made-up transcript, gives no such line.
**－** `uv run --project .guppi guppi lint` of `.guppi/guppi/lint.py` over the live Estimate pages gives no finding by this function.
**－** The line replaces no other finding of the same `method`, such as the line of a `method` that waits for another session.

## Result

2026-11-26, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
