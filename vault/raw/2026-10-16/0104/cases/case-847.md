## Case 847 — The milestone of the clean branch names the tag form that guppi ship reads

> **context:**
> The milestone "The clean branch" of `entity-sprint-plugin` says what work is left before CI writes the clean branch. Its line waits for the fix of `guppi ship` for the example Case, and then for a tag `prod-2`. That fix stands in `.guppi/guppi/ship.py`: its docstring says that the text around the example Case of `case-example.md` is judged like any other (case 815). `.git/refs/tags/prod-2` points at c95e75791a69. But `guppi ship` reads only a tag `prod-x.y.z`: with none in the history of HEAD it prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" and exits 1 (`.guppi/guppi/ship.py`, line 656), and `rule-clean-branch` says that a tag of another form, such as `prod-2`, gives no version. So the line names a run that cannot pass. Case 830 put this line off, and the page carries it in `deferred_by`; this Case takes it up. The rule of the line is `rule-sprint`: an item is `- [[slug]] — <text>`, ticked by the statuses of the slugs before the first ` — `, and the text after it is free; the new text keeps both slugs before the dash. The new line names only the form `prod-x.y.z`. Case 841 of this session sets the tag `prod-0.2.0` locally in Work Mode and pushes it later by a `stop:` task, so the two Cases agree, and the line does not go stale at the next tag. The line also says that the run writes nothing to `prod` while a page with `core: true` stands `draft`, as `rule-clean-branch` sets it. The brief of the last session lists seven such pages under `## Flags`, and Case 841 leaves them as they are. `entity-sprint-plugin` carries no `core: true`, so the pointer form of case 807.4 does not bind its new text. The Estimate that checks the change is `estimate-sprint-plugin-ci-writes-a-clean-branch`, which the line names. Its Criterion already reads the tag `prod-x.y.z` and says that a tag such as `prod-2` gives no version, so it stands, and no Estimate is set `pending`. A Grep of `prod-2` over `vault/wiki/` (with `log.md` and `brief.md` left out, and `decisions/` left out by the hook) printed `vault/wiki/sprint.md`, `vault/wiki/entities/entity-sprint-plugin.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`. The same Grep over `.claude/` printed nothing. `vault/wiki/sprint.md` changes by the render. `rule-clean-branch` and the Criterion of the Estimate name `prod-2` only as a form that gives no version, which stays true. The `## Result` of the Estimate reports the past run on `prod-2`, which also stays true. A Grep of `entity-sprint-plugin|sprint\.md` over `.guppi/tests/` printed lines of `test_archive.py`, `test_caseid.py`, `test_casecheck.py`, `test_generate.py`, `test_lint.py`, `test_ship.py`, `test_ledger.py`, `test_recall.py`, `test_cleanup.py`, `test_prespec.py`, `test_sprint.py`, `test_sprint_close.py` and `test_materialize.py`. By the printed lines, each one writes `sprint.md` under a project folder of the test or names the path or the slug as a string. None of them reads the milestone line of the live page.

> **problem:**
> The milestone line of `entity-sprint-plugin` waits for a fix that is already done, and for a tag `prod-2` that `guppi ship` does not read. It does not say that the draft core pages still stop the run.

> **recommend:**
> - **How should the line name the tag?**
>   - Recommended: (a) only the form `prod-x.y.z`, with no number.
>   - Answer: agreed, (a).
> - **What should the line list as the work left?**
>   - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
>   - Answer: agreed, (a).
> - **Which check confirms this change?**
>   - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
>   - Answer: agreed, (a).

> **given:**
> `entity-sprint-plugin`: the sprint page whose milestone line changes.
> **＋** `vault/wiki/sprint.md`: the render of the sprint page.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate that the line names, which reads the CI run.
> **＋** `rule-sprint`: the form of a milestone item.
> **＋** `rule-clean-branch`: the tag that `guppi ship` reads, and the refusal of a draft core page.

> **when:**
> Someone reads the milestone "The clean branch" of `entity-sprint-plugin`, or its render in `vault/wiki/sprint.md`.

> **then:**
> The line says that the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and names no number of a tag.
> **＋** The line says that `estimate-sprint-plugin-ci-writes-a-clean-branch` reads the CI run that the tag starts.
> **＋** The line says that this run writes nothing to `prod` while a page with `core: true` stands `draft`, as `rule-clean-branch` sets it.
> **－** The line does not wait for the fix of `guppi ship` for the example Case.

> **tasks:**
> - [ ] update `entity-sprint-plugin`
>   - old: `` what remains: once Work Mode commits the fix of `guppi ship` that cleans the text around the example Case (case 815), the owner pushes `plugin` and a tag `prod-2` on its last commit, and the CI run it starts is read by its Estimate ``
>   - new: `` what remains: the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and the CI run it starts is read by its Estimate; while a page with `core: true` stands `draft`, that run writes nothing to `prod` ``
>   - change: `the milestone The clean branch names the tag form prod-x.y.z and the draft core pages that stop the run; the defer of decision-case-830 taken up`
> - [ ] `uv run --project .guppi guppi sprint`

> **ratification:**
> ```
> - decision[case 847][update][entity-sprint-plugin]{ref:entity-sprint-plugin}{supersedes:case 830}
> ```
