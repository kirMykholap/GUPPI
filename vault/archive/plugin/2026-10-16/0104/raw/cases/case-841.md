## Case 841 — The tag prod-0.2.0 stands on plugin before the readings of the batch

> **context:**
> `guppi ship` builds the clean version of GUPPI only when the history of HEAD holds a tag `prod-x.y.z`, which gives `.claude-plugin/plugin.json` its version; `VERSION_TAG` of `.guppi/guppi/ship.py` is the one judgment of that form, and `prod-2` gives no version. The repository holds the tags `prod-1` and `prod-2` only, as `.git/refs/tags/` shows and no packed tag adds, so each build exits 1, the local build with `--allow-draft` too, and the brief reports that `guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`. That blocks the readings of the other Cases of this batch (842 to 846). A push of such a tag starts `.github/workflows/prod.yml`, whose `on:` block takes each tag `prod-*`; its build runs without `--allow-draft`, and while a page with `core: true` stands `draft` `guppi ship` exits 1 before it reads a tag, so the run writes nothing to `prod`. The brief's Flags list seven such pages from the last `guppi check`: `entity-sprint`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `rule-ratification`, `rule-skill-hi` and `rule-work-mode`. The person chose a local tag `prod-0.2.0` on the last commit of `plugin` as the first task of Work Mode, and the push as a `stop:` task, since `rule-where-to-stop` makes a push to a remote a stop. `/pre-spec` found that Work Mode runs the tasks in the order of the Spec, as `.claude/skills/work/SKILL.md` sets it, so a push in this Case would run before the readings by hand of Cases 843 to 846, while Case 843 reads before the push. The person agreed to move the `stop:` task of the push out of this Case to run after the install readings; it stands in Case 850, so this Case keeps the local tag alone. The tag also opens the reading of `estimate-clean-branch-ships-neutral-texts`, whose `method` waits for a tag `prod-x.y.z` in the history of HEAD and for the librarian's run of the session that set that `method`, which the brief says was the run of session 1959. No Case of the plan names it, and this Case does not change it: the Retro of this session reads it by its `method`, a `guppi ship --allow-draft` into an empty folder, by the agent alone. This Case takes up the unticked `stop:` task at line 165 of `vault/raw/2026-10-15/0553/spec.md`, which named the same tag. The promise stays with `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion already covers the run on a tag `prod-x.y.z` and the run that writes nothing when `guppi ship` exits 1, and its `method` waits for a run that writes `prod` before the close of `plugin`, or the person's answer at that close. So its Criterion, `purpose` and `method` stand, the `update` carries only `change`, and Retro leaves it `pending`. The seven draft pages stay out of this Case: each becomes `built` by its own Estimates. A Grep `prod-2|prod-0\.2\.0` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `sprint.md`, `entities/entity-sprint-plugin.md`, `rules/rule-clean-branch.md` and `estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`. In `rule-clean-branch` and the Estimate, `prod-2` stands as the example of a tag of another form and `prod-0.2.0` as an example of a version, and both stay true. The milestone line of `entity-sprint-plugin`, which `guppi sprint` copies into `sprint.md`, still names a tag `prod-2`; Case 847 of this batch rewords it, so this Case leaves it.

> **problem:**
> No tag `prod-x.y.z` stands in the history of `plugin`, so no clean version is built, locally or by CI. The question is which tag is placed, when and where, and where its push stands while the draft pages with `core: true` still stop the build of `prod`.

> **recommend:**
> - **Which name does the tag take?**
>   - Recommended: (a) `prod-0.2.0`, the name the open task and `rule-clean-branch` already use.
>   - Answer: agreed, (a).
> - **When and on which commit is the tag placed?**
>   - Recommended: (a) the first task of Work Mode, on the last commit of `plugin` at that moment, local only.
>   - Answer: agreed, (a).
> - **What does the push of the tag do in this session?**
>   - Recommended: (a) a `stop:` task in this Work Mode: the tag is pushed on the person's word; the run fails on the draft pages and writes nothing to `prod`, and the Estimate stays `pending`.
>   - Answer: agreed, (a).
> - **Which Estimate checks this Case?**
>   - Recommended: (a) `estimate-sprint-plugin-ci-writes-a-clean-branch` stands as it is.
>   - Answer: agreed, (a).
> - **Are the seven draft pages with `core: true` part of this Case?**
>   - Recommended: (a) left out: this Case sets only the tag and its push.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, move the `stop:` task of the push out of this Case into Case 847, since Work Mode runs the tasks in the order of the Spec and Case 843 reads before the push; and name `estimate-clean-branch-ships-neutral-texts`, whose reading the tag opens.
>   - Taken: the push left this Case and stands in Case 850, a new Case after the install readings; this Case keeps the local tag as the first task of Work Mode, and `context` names the Estimate that the Retro of this session reads by its `method`.

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate of the run on a tag, its Criterion kept.
> **＋** `rule-clean-branch`: the rule of `guppi ship` and of the workflow that writes `prod`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which reads the tags `prod-x.y.z` in the history of HEAD.
> **＋** `.claude-plugin/plugin.json`: the manifest of the clean version, whose `version` comes from the tag.
> **＋** `vault/raw/2026-10-15/0553/spec.md`: the Spec whose `stop:` task on the tag this Case takes up.
> **＋** `vault/raw/2026-10-16/0104/cases/case-850.md`: the Case after the install readings, which holds the `stop:` task of the push of the tag.

> **when:**
> In Work Mode of this session, as its first task, the owner places the tag `prod-0.2.0` on the last commit of the branch `plugin`, and `uv run --project .guppi guppi ship --allow-draft <folder>` runs on that commit or a later one.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes the clean version, with `0.2.0` as the `version` of `.claude-plugin/plugin.json`.
> **－** The tag stays local in this Case: its push to GitHub is the `stop:` task of `vault/raw/2026-10-16/0104/cases/case-850.md`.
> **－** The pages with `core: true` that stand `draft` do not change.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - change: `the tag prod-0.2.0 placed on plugin, local; its push is a stop: task of case 850; the Criterion stands, and the reading waits for a run that writes prod`
> - [ ] `git tag prod-0.2.0` on the last commit of `plugin`, as the first task of Work Mode, before the readings of the other Cases of this batch; local only.
> - [ ] by hand: `git tag --list prod-* --merged HEAD` prints `prod-0.2.0`, and `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty folder writes `.claude-plugin/plugin.json` with `version` `0.2.0`.
> **ratification:**
> ```
> - decision[case 841][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> ```
