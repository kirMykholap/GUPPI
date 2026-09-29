# Handoff — 2026-09-29, Slice 3g closed; the Work readings get their trigger

## Notes from memory

- On C3 the person first wanted to see options, then chose the checklist with the detail under each line after seeing today's Frontier drawn in four looks.
- On C4 the person pushed back twice. First: the readings of the librarian's run are taken at the next `/hi`, from facts the librarian writes into the brief, not in `/work`. Second: the readings of `archive` and the commit are taken at `/hi` too. The brief stays before `archive` (case-guppi's reason: the brief reads the yamls and Specs before `archive` moves them); the librarian adds the `archive` stdout to the brief after that step.
- Caveat of 508: the new `/hi`, `/work` and librarian texts act only after this run renders them. The librarian of this run works on its old frame, so the first brief with run facts comes one run later.
- Pre-spec gave 15 findings. The person decided the one decision: 508.2 supersedes 507 and carries both `rule-skill-hi` changes and the one Criterion of `estimate-hi-writes-frontier`. The other findings went back to the `case-guppi` of 506 and 508, and both Cases were ratified again.
- The person put C2 (the form of the Retro report) off again, and then asked why the Retro report looked like code again.

## Direct instructions to the librarian

- Check first: the ledger holds the decision lines of 508.2 twice — once without and once with `{supersedes:case 507}` (the re-ratification). The entries of 507 should end `superseded_by` 508.2, and 508.2 should be applied once.
- 506.7 has a `replace` whose `old` runs across the `### Slice 3g` and `### Slice 4` headings inside `## Milestones` of `entity-sprint-migration`; the pre-spec simulation found it exactly once.
- `make lint` stopped at `backlog --check` before the work, because the defer of Case 509 raised the put-off count of `rule-retro`; `guppi backlog` of this run should clear it.
- `tests/test_schemas.py::test_an_estimate_without_method_is_one_finding` skips until `vault/wiki/estimates/schema.yaml` requires `method`. After the render, `make test` should show 2 skipped, not 3.
- The two lessons of this session share tags but name different root causes.

## What actually got done

Ratified: 506, 508, 509.

What got done: commits 35bb520 (code of 506) and ab14bec (the session folder); `guppi/lint.py`, `guppi/generate.py`; `tests/test_lint.py`, `tests/test_generate.py`, `tests/test_schemas.py`; make test 899 passed, 3 skipped; make style clean; readings L23–L66.

What is not done:
- `make lint` red at `backlog --check` — red before the work: the defer of Case 509 changes the sources of `backlog.md`, which this run renders.
- the skipped test of 506.1 — it runs once the render of this run makes `method` required.
- the failed reading of `estimate-case-build-writes-a-plain-round` — a Case item of the next brief, as the person asked.
- the failed reading of `estimate-documentation-completes` — a Case item of the next brief, as the person asked.
- the `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change` selects no test with `-k schema_change` — for a Case in the next Plan Mode.
- three readings not taken: `estimate-glossary-terms-defined` (17 rows whose term the `where` page does not hold in its text need a hand reading), `estimate-glossary-ticks-the-spec` (the 0137 Spec had no glossary line to tick), `estimate-sprint-migration-index-dissolved` (the hits in the Decision pages were not read one by one) — they stay `W` items.
- one Criterion replaced whole by two Cases of one session — lesson L69.
- the four readings whose moment came in this session — L71–L74.
- 46 `W` lines of the Frontier stay open — the brief carries them.
- the readings whose moment comes after Retro — `estimate-retro-commit-gates`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-report-holds-each-fact-once`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-end-of-work-order`, `estimate-session-phases-in-order`, `estimate-git-context-current`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-agent-writing-followed`, `estimate-permissions` — wait for a later session.
- the Retro report shown in a code block — lesson L70.

26 boxes wait for the librarian.
Read in a later session: `estimate-estimates-schema-checked`, `estimate-lint-checks-the-method`, `estimate-lint-finds-a-broken-link`, `estimate-generate-fails-alone`, `estimate-generate-writes`, `estimate-hi-takes-its-readings`, `estimate-hi-writes-frontier`, `estimate-work-mode-takes-the-work-readings`, `estimate-brief-carries-the-run-facts`.
