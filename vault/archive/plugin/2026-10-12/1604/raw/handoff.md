# Handoff — 2026-10-12, sprint plugin: readings that wait for an event

## Notes from memory

- The person agreed to every recommended answer, across one round of Case 780 and five rounds plus one /pre-spec round (Q14) of Case 781; no hesitation was voiced.
- Case 781 was shown three times: once before /pre-spec, once after its seven findings, and once more after the `casecheck` Stop check refused its 781.7 pair on `entity-glossary`, which `case-guppi` had written without reading the whole row. The ratified text is the third.
- Caveat on 781.5: `estimate-brief-written` lost its method that waited for the person after the close of a sprint; it is now read at the Retro of the session that changes `rule-brief`, as the person chose.
- The person put off the milestone item C1 (the repository on GitHub set up for pull requests from another person) with `sprint · defer`; it stays the only open item of the current milestone.

## Direct instructions to the librarian

- Check first the second `replace` pair of 781.7 on `rule-estimates-schema`: its `new` carries an indented `deferred_by: |` key under `fields`, so the rendered `vault/wiki/estimates/schema.yaml` must parse and pass the `schema-description` step of `make lint` with `deferred_by` both in `optional` and under `fields`.
- `estimate-brief-written` gets an `update` that sets a new `method` and `pending`, and a reading `passed` of the same session; apply the update before the reading.
- `estimate-hi-writes-frontier` gets an `update` (781.9) and no reading of this session.
- Case 781 is one parent with sub-cases 781.1–781.9; 781.7 has three decision lines, the `entity-glossary` one written in the third ratification.

## What actually got done

- Cases ratified: 780; 781 with sub-cases 781.1–781.9.
- Code: `guppi/lint.py` (new `waits_for_an_event`, called by `waits_for_another_session`), `guppi/prespec.py` (docstrings), `guppi/ledger.py` (docstring of `is_sprint_page`), `guppi/generate.py` (`DEFERRABLE` holds `estimates`, `deferred_by` after `checked` in the Estimate key order, docstrings).
- Tests: `tests/test_lint.py`, `tests/test_prespec.py`, `tests/test_generate.py`, `tests/test_schemas.py` — one new test each, two in `test_prespec.py`.
- `make test`: 1502 passed, 6 skipped. `make style`: clean after one `ruff format` of `tests/test_prespec.py`.
- Readings: ledger lines 20–28, all `passed`. Lesson: ledger line 29, `lesson-case-build-sub-cases-contradicted-each-other`.

## Debt

- No box of code, a test or a command is unticked.
- 36 boxes wait for the librarian: page, render, glossary and `read` lines of Cases 780 and 781.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — the person's answer at the /hi after the session whose Work Mode writes README.md.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — a pull request from a second account, in a session of the sprint before its close.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — a CI run on GitHub and the clean branch it wrote, before the close.
- `estimate-sprint-plugin-installs-as-a-plugin` — an install of the clean branch into an empty project, before the close.

## Observations

- `make lint` was red before the work with the 8 lines of the baseline (`rule-morph` deferred 4 times; 7 Estimates `unread: pending`); nothing of the work added a line. `## Expected red` of `work.md` is empty.
- The `ask-guppi` run of /pre-spec reported that it broke its frame: it Grepped `vault/wiki/estimates/` by content three times instead of reaching Estimates through the target's `estimates` field; it confirmed its two findings through that field afterwards.
- `ask-guppi` named two paths of `guppi generate` it did not check and no test covers: a `defer` of an Estimate with no page writes a placeholder `status: draft`, a value outside the Estimate schema's `status` list; and the take-up of a deferred Estimate by an `update` without `supersedes`.

## For the next session

- The cause of `lesson-case-build-sub-cases-contradicted-each-other`: `case-guppi` checks no new text of a sub-case against the new texts of its siblings, nor against the other Estimates and rows that speak of the same field, before it writes a Case with many sub-cases.
- A `defer` of an Estimate with no page: `guppi generate` writes a placeholder `status: draft`, which the Estimate schema does not allow; decide whether a defer of an Estimate needs a page, or what the placeholder holds.
- A /pre-spec check over the `When` and `Then` of a Criterion that waits for another session, left out by Cases 780 and 781 (781, Q3).

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open: did the Frontier come out as its Criterion says, with no Cases line for an open `W` reading that cannot run now?
