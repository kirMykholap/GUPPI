---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: Whether pre-spec prints a note, with no exit code, for a method part that names its event before a colon behind another word, written by the plan or kept on the page by an update that replaces the Criterion whole, by one predicate of .guppi/guppi/lint.py, and leaves alone a part that opens with after or by hand, after
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k off_form
origin: raw/2026-10-31/2307/ledger.md#case-972
sprint: plugin
created: 2026-10-31
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads, in the `then` blocks of the plan file, the `method` of a `create` of an Estimate, of an `update` that carries `set: {method: …}`, or, for an `update` of an Estimate that replaces its Criterion whole, writes no `method` and sets no status `passed` or `failed`, the `method` of its live page.

Then:
A `method` with a part between two `;` that names an event before a colon behind another word — `after`, or `by hand, after`, after a word boundary but not at the start of the stripped part, such as `and by hand, after the first session start: the file read` — gives one note `note: case N: <create|update> <slug>: method names its event inside a part — open the part with after, or with by hand, after, or answer that it names a moment of this session`.
**＋** For the `method` of the live page, the note reads `note: case N: update <slug>: the method on the page names its event inside a part —` and the same words after the dash.
**＋** The note sets no exit code, so it does not hold the exit from Plan Mode.
**＋** The judgment is one predicate in `.guppi/guppi/lint.py`, built on the pattern that `waits_for_an_event` matches by, which `.guppi/guppi/prespec.py` imports.
**－** A part that opens with `after`, or with `by hand, after`, and names its event before a colon gives no such note.
**－** A part in which `after` stands with no colon after it gives no such note.
**－** The note does not replace the line of a `method` that waits for another session, of a `method` kept on the page that waits for another session, or of a `method` that names no form or that ties its reading to a one-off moment.
**－** `uv run --project .guppi guppi lint` of `.guppi/guppi/lint.py` over the live Estimate pages gives no finding by this predicate.

## Result

2026-11-01, Retro of session 2307, by uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k off_form: 3 passed — test_off_form_a_wait_behind_another_word_is_a_note (a create and an update with set method each give one note with exit 0, an update that replaces the Criterion whole of a live page with that method gives the note of the method on the page with exit 0), test_off_form_a_part_that_opens_with_the_form_gives_no_note, test_off_form_a_part_that_names_its_event_behind_another_word (true on "and by hand, after X: read" and "read after X: read", false on "by hand, after X: read", "after X: read", "after X" and "hereafter X: read"); guppi test 1856 passed, 6 skipped, 1 deselected

## History

- 2026-11-01 created · [[decision-case-972]]
- 2026-11-01 status: pending → passed · raw/2026-10-31/2307/ledger.md#L18
