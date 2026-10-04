# Handoff — 2026-10-04, the test page closed, a line put off by the conserved Spec, readings

## Notes from memory

- The person asked to close as passed the readings whose moment no one brings on by hand: a `/work` the person types, and a refusal of the ledger hook. The agent read what had come in the transcripts against each Criterion and wrote the missing part into the line as not exercised, on the person's word. The `method` of each of those Estimates still names that moment; no Case changed it.
- The person asked to close `estimate-ask-finds` as passed. The agent found two of four dispatches against its Criterion, and the person agreed to record the reading as failed and to put the decision off.
- The person wanted to stage a Case ratified in Work Mode, for `estimate-spec-write-reaches-the-approved-spec`. No change was asked in Work Mode, so the moment did not come.
- The person counted this session as one opened without `/hi`. The reply before `/hi` carried no `LEDGER` block, so `estimate-session-start-context` still waits for a session without `/hi` whose reply carries one.
- The person proposed to take `rule-subagent-guppi` and put it off again at once, for `estimate-ratification-ledger-line-form`. A second defer is no take-up: the take-up is a full Case with a decision line other than a `defer` and one `supersedes` block per Case of `deferred_by`. Nothing was done.
- Case 620 was built again on the findings of `/pre-spec` and ratified again; the second ratification added only the update of `rule-orchestration`.
- The person put the sprint items and the three failed readings off to go to work.

## Direct instructions to the librarian

- Apply the reword of 619.1 before the delete of 619.2: the reword on `entity-reading-probe` is the first live run of a reword, and the next `/hi` reads `estimate-generate-rewords` from its stdout line, the `reworded` History line of the archived page and `log.md`.
- 620.1 sets `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan` actioned; by the cascade both of its lessons are archived.
- The defers of 621, 622 and 623 target Estimates, which `generate` gives no `deferred_by`; `backlog.md` will not list them.
- The lesson `lesson-case-build-hits-counted-as-lines` shares its root cause with `lesson-case-build-a-count-in-context-not-from-a-run`: a count written from the agent's own reading of an output, not from a command that counts the thing claimed.
- Readings that wait for a later session, with the moment each needs:
  - the librarian's run of this session, read at the next `/hi`: `estimate-generate-rewords`;
  - updated by this session: `estimate-hi-takes-a-conserved-spec` (a session that takes a conserved Spec), `estimate-prespec-checks-the-frontier` (pytest of `tests/test_prespec.py`);
  - a session without `/hi` whose reply carries a `LEDGER` block: `estimate-session-start-context`;
  - a Case ratified in Work Mode: `estimate-spec-write-reaches-the-approved-spec`;
  - a batch in Plan Mode: `estimate-orchestration-signs-a-batch-together`;
  - a take-up of a page with several Cases in `deferred_by`, and a lesson beside the Case that closes its cause: `estimate-ratification-ledger-line-form`;
  - a send-back of `rule-case-check`: `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`;
  - a Baseline whose backlog step is red: `estimate-lint-runs-every-step`;
  - the close of a sprint: `estimate-sprint-close-archives-the-decisions`, `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`, `estimate-sprint-close-settles-unread-estimates`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`.

## What actually got done

- Ratified: 619 (619.1, 619.2) and 620 (620.1, 620.2); put off: 621, 622, 623.
- Code: `guppi/prespec.py` — `conserved_blocks` and `has_defer_item`; `check_frontier` takes the plan and looks for the `defer` item of `defer case N` in the conserved Spec its title line names, by `conserved_spec_named` of `guppi/box.py`; the module docstring and the docstring of `check_frontier` say so. `tests/test_prespec.py` — three tests: a defer item of the conserved Spec is clean, a Case of it with no defer item is a finding, a folder with no `carry.md` adds no Case.
- `make test`: 1132 passed, 6 skipped; `make style` clean.
- Readings: ledger lines 1–6 and 14–16 passed, line 17 failed. Lessons: lines 22 and 23.

## Debt

None.

- Boxes that wait for the librarian: 10.
- `read` lines whose slug this session creates or updates: `estimate-hi-takes-a-conserved-spec`, `estimate-prespec-checks-the-frontier`.

## Observations

- `make lint` was red before the work, exit 2, 38 finding lines: 2 on `entity-reading-probe`, 5 `deferred`, 28 `unread: pending`, 3 `unread: failed`.
- No check was changed that reads a page this Spec updates; `## Expected red` is empty.

## For the next session

- Whether the `method` of the Estimates read on the person's word drops the moment no one brings on by hand — a `/work` the person types, a refusal of the ledger hook — or keeps it as a part not exercised.
- `rule-sprint-close` and where the close of a sprint runs, Slice 5, put off again.

## Ask the person

None.
