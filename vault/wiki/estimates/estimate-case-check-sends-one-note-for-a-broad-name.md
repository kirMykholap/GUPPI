---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends case-guppi one note with the name and the count for a name of what the Case changes that more than 20 of the searched files hold, in place of a note for each of those files
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py, passed and not skipped
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow, case-build]
core: true
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, and more than 20 of the files it searches for the names of a page or a file the Case changes hold one such name.
**＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, transcript, plan file and store.

Then:
The hook sends one note for that name, which names the Case, the name and the count of the files that hold it, and asks the agent to search for the name and to name in `context` that search and why each file it does not enter stands.
**＋** A file that holds no other name of the Case, or only other names that more than 20 of the searched files hold, gets no note of its own.
**＋** A file that also holds a name that 20 or fewer of the searched files hold keeps its own note for that name.
**－** Neither the file of the page or the file itself, nor a page under `vault/wiki/decisions/`, `log.md` or `brief.md`, adds to the count.

## Result

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
