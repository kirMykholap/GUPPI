## Case 641 — The session's Estimate names a make target over the phases' tests

> **context:**
> `make lint` holds a rule for an Estimate of a MOC, a page that groups child pages. If the Estimate's `method` is a reading by hand and names no `make <target>`, every counted Estimate of the children must be a reading too. A sibling Estimate that names a target also clears the rule. Otherwise lint reports the Estimate (`check_method` in `guppi/lint.py`, cases 112.1, 212; the `method` field of `rule-estimates-schema`). The aim of the rule is that a reading by hand on the parent cannot hide the test pipelines of the children. `rule-session` is a MOC over the five phases. Its one Estimate, `estimate-session-phases-in-order`, is a reading by hand of the marks a finished session leaves, in time order. Case 637.4 set the method of `estimate-session-start-context`, an Estimate of the child `rule-session-start`, to `make test-session-start` alone. Since then that child is checked by tests only, and lint prints `estimates/estimate-session-phases-in-order: method: says by hand while estimate-session-start-context names a test file` (brief of 2026-10-04). The Estimates of the other children still pair a target with a reading by hand, or are readings. The Makefile has one pipeline per phase that has tests: `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation`. Work Mode has none, and no target runs these four together. This Case adds a target `test-session` that runs the four, after the pattern of the per-MOC pipelines. It puts that target first in the method, before the same reading by hand. A `make <target>` the Makefile holds passes a MOC's Estimate whatever else the method says, so the finding clears. The rule of lint does not change. Its Estimate, `estimate-lint-checks-the-method`, already promises that such a target passes, so its Criterion stands. Only the `method` field of `estimate-session-phases-in-order` changes. Its Criterion speaks of the marks of a session and their order, not of how the check runs. So the Criterion and the status `passed` stand. The update carries no `set.status`.
>
> Two other Estimates make promises about every target of the Makefile, and both cover the new target (pre-spec findings on this Case). Both Criteria stand. `estimate-harness-make-runs-in-both-shells`, on `rule-harness`, promises that no recipe reads the stdin of its caller and no target writes to the working tree. `test-session` has no recipe of its own. It only names the four phase targets as prerequisites, and each of their recipes already closes stdin and only runs `pytest`. `estimate-tests-clock-pinned`, on `rule-tests-clock-pinned`, promises that the targets `test` and `test-*` run under the autouse fixture that pins the clock. `test-session` runs the same `pytest` calls as the four targets, so the fixture applies to them unchanged. The `then` keeps one line on each of these two promises for the new target. Neither Estimate is set `pending`.
>
> The page changes at the librarian's `generate`, so the `make lint` of that run shows the finding gone, and the brief reports it. Work Mode runs `make test-session` once to check the new target. Two searches over the repository, `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` excluded, back this. The first, Grep `estimate-session-phases-in-order`, printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-session.md`. The hit in `rule-session.md` is its `estimates` field, which stays true. The brief and the log are not read. The second, Grep `test-session`, printed `vault/wiki/brief.md`, `vault/wiki/estimates/estimate-session-start-context.md` and `Makefile`. Each hit names `test-session-start` only, so the name `test-session` is free. Cases 638, 639 and 640 of this session touch none of these pages, the Makefile, or the lint check.

> **problem:**
> The `method` of `estimate-session-phases-in-order` is a reading by hand alone. Now that `estimate-session-start-context` is checked by a test target only, `make lint` reports the MOC's Estimate on every run. Something must clear the finding without weakening the rule that stops a reading by hand on a MOC from hiding its children's pipelines.

> **recommend:**
> - **How should the finding on the session's Estimate be cleared?**
>   - Recommended: (a) a new `make test-session` target that runs the tests of each phase that has them, named first in the method of `estimate-session-phases-in-order` before the same reading by hand; the rule of lint, its tests and the promise of the Estimate do not change.
>   - Answer: agreed, (a).

> **given:**
> `estimate-session-phases-in-order` — the Estimate of the MOC whose `method` changes
> **＋** `Makefile` — gains the target `test-session`
> **＋** `rule-session` — the MOC over the five phases, whose children's pipelines the target runs
> **＋** `guppi/lint.py` — the judgment of a MOC's `method`, which constrains
> **＋** `rule-estimates-schema` — the form of the `method` field, which constrains
> **＋** `estimate-harness-make-runs-in-both-shells` — the promise on every recipe and target of the `Makefile`, which constrains
> **＋** `estimate-tests-clock-pinned` — the promise that the `test-*` targets run under the clock fixture, which constrains

> **when:**
> `uv run guppi lint` reads the `method` of `estimate-session-phases-in-order` against the `Makefile`.
> **＋** Someone runs `make test-session`.

> **then:**
> The `method` names `make test-session`, a target of the `Makefile`, and lint prints no `method` finding for `estimate-session-phases-in-order`.
> **＋** `make test-session` runs the pipelines `test-session-start`, `test-plan-mode`, `test-end-of-work` and `test-documentation`, and passes only when all of them pass.
> **＋** The tests that `make test-session` runs use the clock fixture that `estimate-tests-clock-pinned` promises for the `test-*` targets.
> **＋** The reading by hand of the marks of a session at its close stays in the `method` after the target, in the same words.
> **－** The Criterion and the status of `estimate-session-phases-in-order` do not change.
> **－** The judgment of `guppi/lint.py` on the `method` of a MOC's Estimate does not change.
> **－** `make test-session` reads no stdin of its caller and writes nothing to the working tree, as `estimate-harness-make-runs-in-both-shells` promises for every target.

> **tasks:**
> - [ ] `Makefile` — add `test-session` to `.PHONY` and a target `test-session: test-session-start test-plan-mode test-end-of-work test-documentation` with the help text `## the pipeline over rule-session's children`
> - [ ] update `estimate-session-phases-in-order`
>   - set: `{method: "make test-session, the pipeline over the tests of rule-session's children; then by hand at the close of a session — the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md, the librarian's commit, read in that order"}`
>   - change: `the method names make test-session before the reading by hand; the lint finding on a MOC's reading clears (case 641)`
> - [ ] by hand in Work Mode: `make test-session` runs the four phase pipelines and passes

> **ratification:**
> ```
> - decision[case 641][update][estimate-session-phases-in-order]{ref:estimate-session-phases-in-order}
> ```
