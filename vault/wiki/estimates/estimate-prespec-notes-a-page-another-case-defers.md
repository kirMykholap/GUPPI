---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether guppi prespec --check prints a note, at every run and without blocking, for a page that one Case of the plan changes and another top-level Case of the plan puts off
method: uv run pytest tests/test_prespec.py -k defers_a_page
origin: raw/2026-10-07/2114/ledger.md#case-726.1
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check` reads the plan file of the session, where the `then` block of one Case holds a `defer` item of a page and the `then` block of another top-level Case holds a `create`, `update` or `delete` item of the same page.
**＋** Or `tests/test_prespec.py` runs it over a made-up plan.

Then:
The check prints one line that opens with `note:` for each page and pair of Cases, and it names the Case that changes the page, the page and the Case that puts it off.
**＋** A short Case under `## Deferred` of the plan file counts as a Case that puts the page off.
**＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
**＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the pair.
**－** A Case and its sub-cases are one Case here: a change and a defer of one page inside one top-level Case give no note.
**－** A page that only `defer` items name gives no note.
**－** The check of the file of a Case by `guppi/casecheck.py` prints no such note.

## Result

2026-10-07, Retro of session 2114: uv run pytest tests/test_prespec.py -k defers_a_page 4 passed — an update and a defer of one page under two Cases give one note and exit 0, a short Case under Deferred gives the same note, two sub-cases of one Case give none, a page only defer items name gives none; guppi/casecheck.py imports promise_notes and not defer_notes, so the check of the file of a Case prints no such note

## History

- 2026-10-07 created · [[decision-case-726.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L25
