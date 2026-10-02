## Case 587 — make lint runs every step and reports each

> **context:**
> `make lint` runs five steps in a fixed order: `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, then the page check `guppi lint`. Each step is one line of the recipe of the target `lint` in the `Makefile`, and make stops the recipe at the first line that exits non-zero. The backlog step is red in nearly every session that puts an item off: `guppi/backlog.py` counts the `[-]` lines of every `frontier.md`, the session's own included, and only the librarian's run writes `backlog.md` again. So the Baseline that `/work` writes into `work.md` holds only the backlog line, and the findings of the glossary and page steps are not printed. The handoff of session 1725 shows this: the Baseline `make lint` gave exit 2 and stopped at its backlog step, and the agent had to run the page step by hand to get the schema, orphan and fence findings, the deferred lines and the unread lines. The Result of `estimate-retro-red-in-the-baseline-is-not-charged` shows the same stop in session 2356. The librarian's `make lint` at the brief and at the close stops in the same way; the search below printed a line of case 58 that says "`make lint` stopped at its first step". The person chose to fix this in `make lint` itself: the recipe runs every step, each prints its own lines, and the target exits non-zero when any step is red. The backlog red itself stays, as the signal that `backlog.md` waits for the librarian. `/work` and the librarian keep running `make lint` as they do now, and their text does not change. `rule-lint` lists the `Makefile` in `implementation_ref`. Its `## Purpose` says that `make lint` runs `guppi lint` after the four checks and that all five only report. That stays true, and this Case adds one sentence on the new behaviour. No test reads the recipe of `lint`: a Grep of `Makefile` over `tests/` printed only `tests/test_lint.py`, whose hits write fixture Makefiles for the method check. The Case creates `estimate-lint-runs-every-step` with `ref: rule-lint`, so the vault query for a `create` without a `ref` did not run. A Glob `vault/**/estimate-lint-runs-every-step*` found no file, so the slug is free. These Estimates speak of `make lint` and stand. `estimate-harness-pipeline` checks the order of the steps and the Purpose of `rule-harness`, and the order does not change; the person chose to keep the new promise out of it. `estimate-backlog-checks-the-file` and `estimate-sprint-checks-the-file` check the place of their step in that order, and the place does not change. `estimate-harness-make-runs-in-both-shells` wants the same exit code from both shells, no read of stdin and no write to the tree, and the new recipe keeps all three. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` wants each lint finding line as printed in the Baseline, and the Baseline now gets more of them. `estimate-sprint-migration-lint-clean` wants exit 0 at the close of the sprint, which still means every step is clean. The search with pattern `make lint` over `vault/wiki/rules/` printed `rule-close`, `rule-glossary`, `rule-harness`, `rule-lint`, `rule-case-build`, `rule-brief`, `rule-backlog`, `rule-work-mode`, `rule-sprint`, `rule-retro` and `rule-render-harness`. Outside History lines, each hit says that `make lint` runs a step, sets its order, reads its output, or tells Retro not to run it. None says that it stops at the first red, and none is made false. The same pattern over `vault/wiki/estimates/` printed 25 files: the Estimates named above, the schema-check and layout Estimates whose `method` reads `make lint`, `estimate-documentation-completes`, `estimate-glossary-checks-the-file`, `estimate-glossary-terms-defined`, `estimate-lint-checks-the-method`, `estimate-raw-archive`, `estimate-page-schemas-one-file-per-rule`, `estimate-atomicity-rendered`, `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-sprint-migration-file-route-gone` and `estimate-sprint-migration-rule-class-files-dissolved`. Each reads the findings or the exit code, and none relies on the stop. The pattern `make lint|guppi lint|--check` over `.claude/` printed `.claude/skills/work/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/agents/case-guppi.md`. They run `make lint` and keep its output, or forbid running it at Retro, and the hit in the pre-spec skill is `guppi prespec --check`. All of them stand. The pattern `first (red|step|failing)|stops at|make -k|keep-going` over `vault/wiki/` printed `brief.md` (the source of this item) and the Decision pages of cases 58, 89.1–89.4, 150.1, 326 and 569, which were not opened. No hook changes, and no reader in code reads a text this Case changes, so no old form is kept.

> **problem:**
> `make lint` stops at its first red step. The backlog step is red in nearly every session that puts an item off, so the Baseline of `/work` and the librarian's runs lose the findings of the later steps, the page findings included. The question was where the fix goes.

> **recommend:**
> - **Where the fix for the hidden findings goes**
>   - Recommended: (a) `make lint` runs every step, each prints its own findings, and it exits non-zero when any step is red; only the `Makefile` changes, and the backlog red stays as a signal.
>   - Answer: (a), agreed.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate of its own, `estimate-lint-runs-every-step` on `rule-lint`, read by hand at the next session's Baseline, where the backlog step is expected to be red; `estimate-harness-pipeline` stays as it is.
>   - Answer: (a), agreed.

> **given:**
> `Makefile` — the target `lint`, whose recipe runs the five steps
> **＋** `rule-lint` — the rule that lists the `Makefile` among its code files and says what `make lint` runs
> **＋** `estimate-lint-runs-every-step` — the new promise of `rule-lint`
> **＋** `/work` — the skill whose Baseline runs `make lint` and writes its output into `work.md`
> **＋** `.claude/agents/librarian-guppi.md` — the librarian, whose brief and close run `make lint`

> **when:**
> Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.

> **then:**
> `make lint` runs all five steps in the order `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint`, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

> **tasks:**
> - [ ] `Makefile`: the recipe of `lint` runs each of the five steps with stdin from `/dev/null`, keeps going after a step that exits non-zero, and exits non-zero at the end when any step did
> - [ ] update `rule-lint`
>   - old: `holds (cases 147.7, 227).`
>   - new: `holds (cases 147.7, 227). It runs all five even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red (case 587).`
>   - change: `make lint runs every step and exits non-zero when any is red (case 587)`
> - [ ] create `estimate-lint-runs-every-step`
>   - ref: `rule-lint`
>   - kind: `QA`
>   - purpose: `Whether make lint runs all five steps when an earlier one is red, prints the lines of each, and exits non-zero when any step is red`
>   - method: `by hand, the make lint of the Baseline of the first /work of a later session whose backlog step is red: the steps that printed, the page findings of guppi lint and the exit code, recorded in the estimate line`
>   - tags: `[harness, workflow]`
> - [ ] by hand: `make lint` on the working tree after the change, from PowerShell and from Git Bash; the steps that printed and the exit code in both shells
> - [ ] read `estimate-lint-runs-every-step` — by hand at the Baseline of the first `/work` of a later session whose backlog step is red

> **ratification:**
> ```
> - decision[case 587][update][rule-lint]{ref:rule-lint}
> - decision[case 587][create][estimate-lint-runs-every-step]{ref:rule-lint}{tags:harness,workflow}
> ```
