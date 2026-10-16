## Case 860 — estimate-harness-pipeline leaves the backlog

> **context:**
> `guppi backlog` lists under `## Deferred` each live page whose `deferred_by` is not empty, whatever its status (`.guppi/guppi/backlog.py`). `estimate-harness-pipeline` carries `deferred_by: ["[[decision-case-833]]", "[[decision-case-849]]"]`. Both defers have the same problem: no Case gave the Estimate a reading moment after the librarian's run. Since then the Estimate was read and passed at the `/hi` of session 0342 (its `## Result` and the History line `status: failed → passed`). So `backlog.md` still lists it as put off in 2 sessions, although the event its defers waited for has come. The brief of session 0342 reports it under Flags: "`estimate-harness-pipeline` and `estimate-guppi-tests-green` are `passed` and keep `deferred_by` (cases 833 and 849; case 829), so `backlog.md` still lists them." The pages confirm the main agent's mapping: this Estimate carries cases 833 and 849, and `estimate-guppi-tests-green` carries case 829 alone.
>
> The fix follows "Taking up a deferred decision" of `rule-case-protocol`: one decision line names the page by an `update` with only `change`, since nothing on the page changes, and carries `{supersedes:case 833}` and `{supersedes:case 849}`. `generate` then drops both slugs from `deferred_by` and drops the empty field (`clear_deferred_by` of `.guppi/guppi/generate.py`), and the next `guppi backlog` leaves the Estimate out. An `update` of an Estimate with `change` alone writes its History and no Criterion (`.guppi/guppi/materialize.py`, case 588.2), so the status `passed`, `checked`, the Criterion and the Result stand. The marks retire the one defer of each of `decision-case-833` and `decision-case-849`, so the cascade sets both pages `superseded` and then `archived`. The person asked for the quick cleanup, so this Case gives the `method` no new reading moment; the Estimate passed with the `method` it has.
>
> By `rule-atomicity` this Case and Case 861, which clears `estimate-guppi-tests-green`, stay apart: each clears a different page by different marks, and one can fail while the other passes.
>
> How it is checked: `estimate-generate-writes-the-decision-page` already checks that a `supersedes` removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, and drops an empty `deferred_by`. `estimate-backlog-renders` checks that `## Deferred` holds each live page with a `deferred_by` that is not empty. This Case changes neither behaviour, so both Criteria stand, and the Criterion of `estimate-harness-pipeline` is not touched.
>
> Searches. A Grep for `harness-pipeline` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-harness.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. `rule-harness` lists the Estimate in `estimates`, which stays true. No file under `.guppi/tests/` names the page, so no test reads it live.

> **problem:**
> `estimate-harness-pipeline` passed, but it still carries the defers of cases 833 and 849, so `backlog.md` lists it as put off work.

> **recommend:**
> - Recommended: retire both defers by one `update` of the Estimate with only `change`, its decision line carrying `{supersedes:case 833}` and `{supersedes:case 849}`.
> - Answer: ratified as built

> **given:**
> `estimate-harness-pipeline`: the defers of `decision-case-833` and `decision-case-849` are retired.
> **＋** `rule-case-protocol`: a deferred decision is taken up by a Case that names the page and supersedes each Decision of its `deferred_by`.
> **＋** `.guppi/guppi/generate.py`: a `supersedes` clears `deferred_by` on the pages the superseding Case names.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the backlog lists each live page with `deferred_by`.

> **when:**
> `uv run --project .guppi guppi generate` applies the decision line of this Case at the librarian's run.
> **＋** `uv run --project .guppi guppi backlog` runs after it.

> **then:**
> `estimate-harness-pipeline` carries no `deferred_by`.
> **＋** `vault/wiki/backlog.md` holds no line for `estimate-harness-pipeline`.
> **－** The status `passed`, the `checked` date, the Criterion and the Result of `estimate-harness-pipeline` do not change.

> **tasks:**
> - [ ] update `estimate-harness-pipeline`
>   - change: `the defers of case 833 and case 849 retired — the Estimate passed at the /hi of session 0342`

> **ratification:**
> ```
> - decision[case 860][update][estimate-harness-pipeline]{ref:rule-harness}{supersedes:case 833}{supersedes:case 849}
> ```
