# Handoff — 2026-10-31, the defects of lint and the readings of Case building

## Notes from memory

- The person took each recommended answer of every round with a short "ok", in Russian or English; no option was argued.
- Case 973: the brief of session 1831 put the cause of the `ref` finding in the code spans of the Criterion of `estimate-link-graph-prints-the-neighbours`; `case-guppi` found the bare `[[slug]]` in its `## Result`. The person chose to fix the page text alone, not the cause (a check of the ledger text for bare links was left out as an item of its own).
- Case 972 changed at `/pre-spec`: the near miss of the wait form became a `note:` line, not a finding, by the person's answer, since a part with `after … :` inside may name a moment of the Case's own session.
- Case 975 was refused once at its showing by the check of `rule-case-check` (the sentence around the glossary pair not read whole); `case-guppi` read the page whole and the file did not change.
- C10 was taken as a reading in Plan Mode, not deferred: this session's start was the first with the hook of `rule-link-graph-at-session-start`.

## Direct instructions to the librarian

- Case 973 writes the `## Result` of `estimate-link-graph-prints-the-neighbours` whole by `sections: Result`; check that the status, the `## Criterion` and the `method` of that page stay as they are, and that the bare `[[slug]]` now stands in a code span.
- Case 974 sets `insight-case-build-changes-a-step-without-reading-its-readers` `actioned` with `addressed_by: decision-case-974`; the lesson `lesson-case-build-names-a-file-without-the-readers-of-its-folder` under it may archive by the cascade.
- Case 975 changes two sentences of `rule-rules-schema` and one row of `entity-glossary`; render `vault/wiki/rules/schema.yaml` and run `guppi glossary`, then check that each `replace` text stands once.
- Case 976 defers four Estimates; three of them (`estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-shows-the-built-case`) already carry `decision-case-971` in `deferred_by`; the new defer adds to that list.
- The lesson `lesson-ledger-reading-writes-a-bare-wikilink` and the lesson `lesson-orchestration-shows-a-round-after-own-text` are new; compare each against the Insights of the vault.

## What actually got done

- Cases ratified: 972, 973, 974, 975, and the short-form defer 976. Cases 972–975 were built again on the findings of `/pre-spec` and ratified again.
- Code: `.guppi/guppi/lint.py` (`names_its_event_inside_a_part`), `.guppi/guppi/prespec.py` (`kept_method`, `wait_form_notes`, `OFF_FORM_WAIT`, the module docstring; `kept_method_waits` reads by `kept_method`). Tests: `.guppi/tests/test_lint.py` (1 new), `.guppi/tests/test_prespec.py` (2 new).
- `guppi test`: 1853 passed, 6 skipped, 1 deselected at the baseline; 1856 passed, 6 skipped, 1 deselected at Retro. `guppi style`: clean.
- Readings: L1, L2, L3 passed (at `/hi`), L4 passed (in Plan Mode), the reading of `estimate-prespec-hook-reports-a-wait-off-its-form` passed (at Retro). Lessons: `lesson-ledger-reading-writes-a-bare-wikilink` and `lesson-orchestration-shows-a-round-after-own-text` (error, at Retro).

## Debt

- No box of code, test or command is left unticked.
- 15 boxes wait for the librarian: the page, render and glossary lines of Cases 972–975 and their `read` lines.
- `estimate-sprint-plugin-check-finds-no-bare-slug-link` — after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — after the `/pre-spec` of the first session whose `case-guppi` runs on the new Render of `rule-case-build` and in which a Case adds a file that is no page.
- `estimate-rules-schema-checked` — after a librarian's run that renders `vault/wiki/rules/schema.yaml` from the new Render.

## Observations

- Red before the work, in `## Baseline` of `work.md`: `guppi check` printed 19 lines, among them `backlog: vault/wiki/backlog.md differs from its sources`, which the brief of session 1831 did not report (18 lines then); the other 18 are the lines the brief names.
- `guppi caseid --next --session` takes the session id of the `hi:` line (`8d8876d7`), not the folder time `2307`; with `2307` it printed `no plan file of session 2307----`.
- Four live `passed` Estimates hold `after … :` inside a part that does not open with it (`estimate-case-build-writes-a-plain-round`, `estimate-render-harness-reproduces`, `estimate-prespec-onward-reads-the-decisions-of-the-session`, `estimate-hi-takes-a-conserved-spec`); the lint run does not call the new predicate, so they give no finding.

## For the next session

- C1, the clean branch: push `plugin` and a tag `prod-x.y.z` on its last commit, and read the CI run by `estimate-sprint-plugin-ci-writes-a-clean-branch`.
- Whether the ledger hook refuses a reading line whose text holds a bare `[[…]]` that names no page (`lesson-ledger-reading-writes-a-bare-wikilink`); the person left it out of Case 973 as an item of its own.
- Why `guppi check` reports `backlog.md differs from its sources` at the start of this session.

## Ask the person
