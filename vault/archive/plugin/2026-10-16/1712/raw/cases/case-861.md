## Case 861 — estimate-guppi-tests-green takes a method that fits a MOC and leaves the backlog

> **context:**
> `guppi backlog` lists under `## Deferred` each live page whose `deferred_by` is not empty, whatever its status (`.guppi/guppi/backlog.py`). `estimate-guppi-tests-green` passed on 2026-09-29, and since then case 829 put it off, so it carries `deferred_by: ["[[decision-case-829]]"]` and `backlog.md` lists it as put off in 1 session. The pages confirm the main agent's mapping: this Estimate carries case 829 alone, and `estimate-harness-pipeline` carries cases 833 and 849. The defer of case 829 is not stale. Its Problem says that no Case gave this Estimate a `method` that fits a MOC, and that problem stands. The target `entity-guppi` is a MOC, and its `method` reads "uv run --project .guppi guppi test, 0 failed; read after each Work Mode". On a MOC, `rule-estimates-schema` takes a `make <target>` of the Makefile or `pytest` with test files, and a command of the project alone earns a finding. The brief of session 0342 reports the last run of `guppi check` under Readings at the close as "12 lines (exit 1), as in Flags", and Flags holds: "Lint: `method` — `estimate-guppi-tests-green` (a MOC's Estimate names no `make <target>` or `pytest` with test files)".
>
> The person chose a reading by hand. The new `method` keeps the command and the moment, and opens with "by hand", the one spelling of a reading. `check_method` of `.guppi/guppi/lint.py` passes `by hand` on a MOC when every counted Estimate of its children is a reading. The children of `entity-guppi` are `entity-sprint` and `entity-guppi-repository`, with no Estimate, and `entity-glossary`, whose one Estimate, `estimate-glossary-terms-defined`, has a `method` with "by hand". The new `method` names no `pytest` and no Makefile target. So lint finds nothing on it, and `guppi ship` can still write the passed Estimate into the clean version, which `rule-clean-branch` refuses for a `method` that names a target of the `Makefile`. The part "after each Work Mode:" names its event before a colon, so it waits for that event and is no finding of a later session (`rule-case-protocol`, case 781). Going back to `make test` was turned down: case 820.7 made every live rule, entity and Estimate name `guppi test` and `guppi style` in place of the Makefile targets `test` and `style` (the History of `rule-guppi-config`), while the targets that run the pipeline of a MOC stay for now (the History and the Purpose of `rule-harness`), and `rule-harness` says that the clean version holds no `Makefile`. Changing the rule so that a top MOC may name `guppi test` was turned down as a promise of its own, larger than this cleanup. Retiring the defer alone was turned down, since lint would still report the `method`.
>
> The decision line names the page by an `update` that sets `method` alone, and carries `{supersedes:case 829}`. An `update` that sets a field other than `status` changes that field, and the Criterion and the status stand (`rule-case-protocol`, case 378.4). `generate` then drops `decision-case-829` from the `deferred_by` of this page, since the Case names it (`clear_deferred_by` of `.guppi/guppi/generate.py`), and sets `decision-case-829` `superseded`, so the cascade archives it. `estimate-page-schemas-one-file-per-rule`, the other page in the `defer` list of `decision-case-829`, is not named, so it keeps its `deferred_by` and stays in the backlog (case 467.3). The person chose to leave that page out of this Case, since its `method` needs a different fix. A slug in `deferred_by` that names an archived page is no `ref` finding, since lint takes a live or an archived page as a target.
>
> By `rule-atomicity` this Case and Case 860, which clears `estimate-harness-pipeline`, stay apart: each changes a different page and retires different defers, and one can fail while the other passes. Both act at the same `guppi generate` and `guppi backlog` of the librarian's run, on different pages, and do not contradict each other.
>
> How it is checked: `estimate-lint-checks-the-method` already checks this form. Its Criterion says that on a MOC `by hand` passes when every counted Estimate of the children is a reading, so its Criterion stands. `estimate-generate-writes-the-decision-page` and `estimate-backlog-renders` check the rest: the first that a `supersedes` removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, and keeps it on a target the Case does not name; the second that `## Deferred` holds each live page with a `deferred_by` that is not empty. This Case changes neither behaviour, so both Criteria stand. The Criterion of `estimate-guppi-tests-green` does not change, so the Estimate stays `passed`.
>
> Searches. A Grep for `guppi-tests-green` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-guppi.md` and `vault/wiki/estimates/estimate-retro-red-in-the-baseline-is-not-charged.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. `entity-guppi` lists the Estimate in `estimates`, which stays true. The other Estimate says that this one still wants `guppi test` with no failed test on the branch, which the unchanged Criterion keeps true. No file under `.guppi/tests/` names the page, so no test reads it live.

> **problem:**
> `estimate-guppi-tests-green` passed, but its `method` names `guppi test` alone, a form that lint refuses on the Estimate of a MOC, and the defer of case 829 that waits for a fitting `method` keeps it in `backlog.md`.

> **recommend:**
> - **What should the `method` of `estimate-guppi-tests-green` say?**
>   - Recommended: (a) a reading by hand of `guppi test` after each Work Mode, read against the Criterion, 0 failed.
>   - Answer: agreed, (a). Before the answer, the person asked why a MOC may not name `guppi test`; the reply was that the rule wants a MOC's Estimate to run the tests of its own part, which on the top MOC is the whole suite, and that a rule change would be a Case of its own.
> - **How is the fix checked?**
>   - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
>   - Answer: agreed, (a).
> - **Does the other check put off by the same defer join this Case?**
>   - Recommended: (a) leave `estimate-page-schemas-one-file-per-rule` out; it stays in the backlog.
>   - Answer: agreed, (a).

> **given:**
> `estimate-guppi-tests-green`: its `method` is set anew, and the defer of `decision-case-829` is retired.
> **＋** `entity-guppi`: the MOC the Estimate checks, whose children hold readings only.
> **＋** `rule-estimates-schema`: the forms of a `method` on the Estimate of a MOC.
> **＋** `.guppi/guppi/lint.py`: `check_method` judges the `method` of each Estimate.
> **＋** `rule-case-protocol`: a deferred decision is taken up by a Case that names the page and supersedes the Decision of its `deferred_by`.
> **＋** `.guppi/guppi/generate.py`: a `supersedes` clears `deferred_by` on the pages the superseding Case names.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the backlog lists each live page with `deferred_by`.
> **＋** `estimate-page-schemas-one-file-per-rule`: the other page that `decision-case-829` puts off.

> **when:**
> `uv run --project .guppi guppi generate` applies the decision line of this Case at the librarian's run.
> **＋** `uv run --project .guppi guppi backlog` and `uv run --project .guppi guppi check` run after it.

> **then:**
> The `method` of `estimate-guppi-tests-green` is a reading by hand, after each Work Mode, of `uv run --project .guppi guppi test` against its Criterion.
> **＋** `guppi check` reports no `method` finding on `estimate-guppi-tests-green`.
> **＋** `estimate-guppi-tests-green` carries no `deferred_by`.
> **＋** `vault/wiki/backlog.md` holds no line for `estimate-guppi-tests-green`.
> **－** The status `passed`, the `checked` date, the `purpose`, the Criterion and the Result of `estimate-guppi-tests-green` do not change.
> **－** `estimate-page-schemas-one-file-per-rule` keeps `decision-case-829` in its `deferred_by` and stays in `vault/wiki/backlog.md`.

> **tasks:**
> - [ ] update `estimate-guppi-tests-green`
>   - set:
>     ```
>     method: "by hand, after each Work Mode: uv run --project .guppi guppi test, read against the Criterion, 0 failed"
>     ```
>   - change: `the method a reading by hand of guppi test, a form that fits a MOC; the defer of case 829 retired`

> **ratification:**
> ```
> - decision[case 861][update][estimate-guppi-tests-green]{ref:entity-guppi}{supersedes:case 829}
> ```
