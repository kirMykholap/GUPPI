# Handoff — 2026-10-04, Slice 5: the close of a sprint and the check of a Case against the session, built from the conserved Spec of 1439

## Notes from memory

- The person took the conserved Spec of session 1439 at the Frontier and chose, after the `/pre-spec` report, to run it as it stands, though `ask-guppi` found 12 findings in Cases 627–629 that this session could not fix: a session that takes a conserved Spec builds and ratifies none of its Cases again.
- The person asked how a Spec with that many findings was conserved, and asked that the question stay open: the lesson `lesson-prespec-one-ask-guppi-run-samples-the-spec` holds it.

## Direct instructions to the librarian

- The decision lines of Cases 627–631 stand in `vault/raw/2026-10-04/1439/ledger.md`; that unit's `carry.md` is deleted, so it is materialized now. This session's own ledger holds readings and one lesson, no decision line.
- `entity-sprint-migration` gets two `update` entries, 627.1 and 628.9, each with `replace` pairs on different lines and each with `{supersedes:case 615}`: check both pairs land and the defer of 615 is cleared once.
- `rule-sprint-close` gets 627.1 (Purpose, `set` of `enforcement` and `implementation_ref`) and 628.1 (`## How it works`); `rule-orchestration` gets 628.1 and 629.1; `rule-case-build` gets 629.2 and 629.5 — each pair on different anchors.
- `rule-case-rebuild-cost` is deleted by 629.2 with two `{supersedes}` marks; its two Decision pages leave `deferred_by`.
- `guppi/sprint_close.py` is new and is named in `implementation_ref` of `rule-sprint-close` by 627.1.

## What actually got done

- Cases built: 627 (627.1–627.5), 628 (628.1–628.12), 629 (629.1–629.5), all ratified in session 1439; 630 and 631 are its short-form defers.
- Code: `guppi/sprint_close.py` (new: the command `sprint-close`, its preview, `--carry`, `--archive-unread`, the refusal, the marks, `guppi cleanup`, the tick of its line), `guppi/cli.py`, `guppi/ledger.py` (no decision line but a `defer` while no sprint page is live), `guppi/materialize.py` (`opened_sprint`), `guppi/render.py` (`command_line` leaves a longer command), `guppi/backlog.py` (the Backlog of archived sprint pages), `guppi/casecheck.py` (`other_blocks`, `session_clashes`, `stored_parents`, `stored_family`); docstrings of `guppi/sprint.py`, `guppi/generate.py`, `guppi/prespec.py`.
- Tests: `tests/test_sprint_close.py` (new), `tests/test_ledger.py`, `tests/test_materialize.py`, `tests/test_sprint.py`, `tests/test_generate.py`, `tests/test_backlog.py`, `tests/test_casecheck.py`.
- `make test`: 1166 passed, 6 skipped; `make style` clean.
- Readings: L1 `estimate-ask-finds` failed, L2 `estimate-orchestration-signs-a-batch-together` passed, L3 `estimate-ratification-ledger-line-form` passed, L5 `estimate-hi-takes-a-conserved-spec` passed. Lesson: L4.

## Debt

- No box is debt.
- 84 boxes wait for the librarian or a later session: the page, render and sprint lines of the Spec, and its `read` lines.
- Readings that wait for a later session, the Spec creates or updates their Estimate: `estimate-sprint-close-archives-the-decisions`, `estimate-sprint-close-archives-done-insights-and-lone-lessons`, `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`, `estimate-sprint-close-settles-unread-estimates` — the next session, by their pytest test and the preview of migration; `estimate-synthesis-clusters` — the next librarian run with two lesson entries; `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-close-next-session-opens-the-sprint`, `estimate-hi-writes-frontier`, `estimate-brief-written`, `estimate-backlog-renders` — the session that closes a sprint and the one after it; `estimate-sprint-migration-merges`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes migration; `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-sprint-ticks-the-spec`, `estimate-generate-writes` — the next `/work` and librarian run; `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-build-writes-the-case`, `estimate-case-build-checks-the-finished-case` — the next session with live dispatches of `case-guppi` and a `/pre-spec`.
- Readings whose moment has not come: `estimate-ask-query-before-a-create` — a Case with a `create` without a `ref`; `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — a live send-back of the hook for that reason; `estimate-handoff-holds-each-fact-once` — the `/hi` of the next session, on this file; `estimate-lint-runs-every-step` — a Baseline whose backlog step is red; `estimate-session-start-context` — a session without `/hi` whose reply carries a `LEDGER` block; `estimate-spec-write-reaches-the-approved-spec` — a Case ratified in Work Mode.

## Observations

- `make lint` was red before the work with 25 finding lines, the stale defers and the unread Estimates; after the work it printed the same lines. No expected red was marked.
- The tests of 629.1 run under `-k session_clash`, as the Spec names them, and `-k clash`, the selector of `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, selects them too: pytest matches a substring.
- The ledger hook now refuses decision lines in a vault with no live sprint page, so the fixture of `tests/test_ledger.py` seeds `entity-sprint-migration` beside the event log.
- The preview `uv run guppi sprint-close --sprint migration` over the live vault lists 1093 pages to move, 51 kept and 20 unread Estimates.

## For the next session

- The 12 findings of `ask-guppi` at this session's `/pre-spec` on Cases 627–629, each a Case with `{supersedes}` before the close of migration: `## How it works` on the Leaf `rule-sprint-close`, against `rule-rules-schema`, and a Purpose that states behaviour; the `## How it works` left on the Leaf `rule-cleanup`; the sprint page's Estimates called its Definition of done by `entity-sprint`, `rule-sprint` and the Purpose of `entity-sprint-migration`, while the close goes ahead without them; `estimate-sprint-migration-lint-clean` read while five Estimates of the Spec still stand `pending`; the `then` of 628.3 against the per-unit `sprint` of `materialize`; the session that opens a sprint cannot take a conserved Spec, and two "first" in one sentence of `rule-skill-hi`; step 5 of `rule-documentation` still reads the Backlog of the sprint page only; the selector `-k session_clash` inside `-k clash`; `estimate-insights-schema-checked`, `estimate-hi-takes-a-conserved-spec`, `estimate-orchestration-asks-in-the-grill-me-shape` and `estimate-work-mode-takes-the-work-readings` not named by the Cases that change what they speak of.
- How `/pre-spec` checks a Spec so that one run of `ask-guppi` is not taken for a check of the whole, and how a Case built again on a finding is read against the vault: the lesson of this session.

## Ask the person
