# Handoff — 2026-10-05, read lines of closed Estimates, re-ratification marks, one ask-guppi at pre-spec

## Notes from memory

- Case 672: the person called the hand ticking of the eleven open `read` lines in the 0311 and 1616 Specs a one-time exception to the rule that Work Mode ticks no `read` line, and asked that it not be documented; no rule or Estimate of Work Mode names it. The person also chose no Estimate for that ticking: whether those boxes are ticked is not critical to them.
- Case 674: the person asked to weigh the two ways first, judged the per-Case `ask-guppi` runs too costly for an unclear benefit, and chose one run over the whole Spec, "to think further later". No record measures the cost of either way; the placeholder `rule-prespec-judges-the-spec-whole` holds the open question.
- At pre-spec the person left as it stands a finding on Case 672: Retro counts as debt a `read` line of an earlier Case of the session that a later `update` closes by decision, and the librarian's run then ticks it; the same gap already stands for a `delete`.

## Direct instructions to the librarian

- `rule-orchestration` takes three updates in this ledger, from Cases 672, 673 and 674.2, each a `replace` of a different sentence; apply them in ledger order and render `vault/wiki/orchestration.md` once.
- Case 674.3 carries `{supersedes:case 643}` on its `update` and a `defer` of the same page: `deferred_by` of `rule-prespec-judges-the-spec-whole` should name the Decision of 674 and no longer that of 643, and the page should stay under `## Deferred` of `backlog.md` with its new purpose.
- The Cases 672–674 were built again on the findings of pre-spec and ratified again with the same ledger lines; the ledger holds each line once.

## What actually got done

- Cases ratified: 672, 673, 674 (674.1, 674.2, 674.3).
- Code: `guppi/generate.py` — `closes_by_decision`, used by `Vault.tick`; the docstrings of the module, `Vault.tick` and `tick_read`. Tests: `tests/test_generate.py`, 8 new (`close_entry`, `CLOSE_SPEC`).
- The eleven open `read` lines of the Estimates that Cases 669.1–669.15 set `passed` are ticked in `vault/raw/2026-10-05/0311/spec.md` (5) and `vault/raw/2026-10-05/1616/spec.md` (6); the Grep of the `by hand` box over those two Specs prints nothing.
- `make test`: 1266 passed, 6 skipped. `make style`: clean.
- Readings: L1–L7 at `/hi`, all passed; L20–L22 at Retro, all passed. Lesson: L23.

## Debt

- No box of the Spec is debt; no red test, no patch.
- 20 boxes wait for the librarian.
- `estimate-hi-writes-frontier` — the `/hi` of the session after the close of the sprint.
- `estimate-hi-takes-a-conserved-spec` — the `/hi` of the session after the close of the sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the `/work` of the session that closes the sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes the sprint.
- `estimate-backlog-renders` — the librarian's run of the session that closes the sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — the librarian's run of the session that closes the sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close.
- `estimate-sprint-close-takes-the-readings-in-groups` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-lint-clean` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-merges` — the Work Mode of the session that closes the sprint.

## Observations

- `make lint` was red before the work: exit 2, 4 `deferred` and 18 `unread` lines, as `## Baseline` of `work.md` holds.
- The `/pre-spec` of this session still sent one `ask-guppi` per top-level Case, three runs: the skill changes by Case 674.1 only at this librarian's render.
- At `/hi` the agent opened three Estimate pages it did not read (`estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`) to sort the W lines, which the brief's Readings due already allowed.
- The brief item on whether `estimate-hi-takes-its-readings` and `estimate-handoff-holds-each-fact-once` need their methods rewritten needed no decision: their methods, set by case 670, are readings of the rendered skill files, and both were read at `/hi`.

## For the next session

- `rule-sprint-close` and the close of migration stay for the session that closes the sprint; every pending Estimate left waits for that session or the one after it.
- Whether the one `ask-guppi` run at pre-spec needs help on a large Spec, and whether it asks what the Cases leave open together, stands in `rule-prespec-judges-the-spec-whole`; measuring the cost of a run is one way to decide it.

## Ask the person
