# Handoff — 2026-09-27, session 2050: backlog items decided on their page, the account of a session, case-guppi's first round

## Notes from memory

- Case 467 took seven rounds. The person first expected checkboxes in `backlog.md` that a script clears; the rounds showed an item already leaves when its `deferred_by` is cleared, and the person dropped the boxes. A hard refusal of every Case that touches a deferred page was rejected for its gaps (a Case like 460.5 changing a page for another reason). The person asked twice to have the gaps explained ("не понял, объясни") — a complaint about the clarity of case-guppi's round, relevant to `estimate-agent-writing-followed` and to Case 466.
- Case 467.3 has no decision line on `rule-page-generation` itself: its mechanism lives in the docstring of `guppi/generate.py`, which the code commit changed. The person accepted this.
- The rounds of case-guppi strayed from the grill-me text twice: in 465, Q2 and Q3 assumed the answer to Q1; the fourth round of 467 opened with a Q1 marked "No answer needed".
- `estimate-skill-grill-me-asks-in-rounds` is read only on the person's own `/grill-me`; case-guppi's rounds (14 in this session) do not count, so its reading may never come. A question for a later Plan Mode.
- C1 and C2 (Slice 3g) were put off again, `[-] · sprint · defer`.

## Direct instructions to the librarian

- `rule-case-protocol` is updated by two Cases, 466.2 and 467.1; each `replace` anchor is in a different paragraph (pre-spec applied both in memory, each hit once).
- `estimate-generate-writes-the-decision-page` (467.3) carries its Criterion under `sections: Criterion`; it stands as written.
- `rule-backlog` is `built`; 467.3 changes only its Purpose.
- Case 469 is a short defer of `rule-page-generation`, written at Retro under `## Deferred`.
- The ledger holds each decision line once although 466–468 were ratified twice (after pre-spec); the hook did not append them again.

## What actually got done

Ratified: 464, 465, 466.1, 466.2, 467.1, 467.2, 467.3, 468.1, 468.2, 469 (short defer).

What got done: commit 31d86d5 — `guppi/generate.py` (`clear_deferred_by` clears only the pages the superseding Case names, docstring), `guppi/prespec.py` (`deferred_pages`, `decided_on_its_page`, `check_backlog_line`, called from `check_frontier`), `guppi/casecheck.py` (`open_backlog_lines`, `check_backlog`, called from `check_answer` with the session's `frontier.md`); tests in `tests/test_generate.py`, `tests/test_prespec.py`, `tests/test_casecheck.py`. `make test` 844 passed, 2 skipped; `make style` clean. Readings: 17 — 16 `passed`, 1 `failed` (`estimate-documentation-completes`). One lesson, `lesson-test-an-absence-assert-writes-the-banned-phrase-into-the-tree`.

What is not done:
- `estimate-documentation-completes` failed: the librarian's run over 1819 grepped `vault/archive/` and read a file under `~/.claude/projects/`. A defect of the librarian run, for the next session.
- The re-supersede of an archived Decision brings it back from the archive: deferred as Case 469.
- Readings not readable now (a live case or a transcript needed): `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-context-size-warns-past-the-limit`, `estimate-event-log-records`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-spec-write-reaches-the-approved-spec` — pytest green on each. Waiting for their occasion: `estimate-case-protocol-defers-in-one-reply`, `estimate-case-protocol-ledger-line-form`. At the close of the sprint: `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`. By their method in the next session: `estimate-agent-writing-followed`, `estimate-language-followed`; after the librarian's commit: `estimate-session-phases-in-order`.
- The unticked `read` lines of `raw/2026-09-27/1819/spec.md` and `raw/2026-09-27/1255/spec.md` whose Estimates were read here are for `generate` to tick.

Boxes waiting for the librarian: 24. Readings of a later session (this session creates or updates them): `estimate-sprint-migration-file-route-gone`, `estimate-carry-over-writes`, `estimate-case-build-writes-the-case`, `estimate-case-protocol-shows-the-built-case`, `estimate-prespec-requires-a-backlog-item-decided-on-its-page`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page`, `estimate-generate-writes-the-decision-page`, `estimate-retro-report-holds-each-fact-once`, `estimate-handoff-holds-each-fact-once`.
