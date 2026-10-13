## Case 807 — A pointer stands in a bracket of its own, which guppi ship removes whole

> **context:**
> `guppi ship` builds the clean copy of GUPPI that other people install, and the workflow `.github/workflows/prod.yml` writes it to the branch `prod` as a commit of its own; `main` is never changed by the build. Today the script removes a bracket that holds only references to cases, and cuts a reference out of a longer bracket, which can leave words that mean nothing, such as `(supersedes 518)` from `(case 523, supersedes 518)`. It fails on a reference inside a sentence, on a session number and on a link to a page that does not ship, so the run of session 1753 printed 206 lines, all in `guppi/*.py` (`vault/raw/2026-10-13/1753/ship.txt`), and the CI run cannot write `prod`. The person chose a rule that ends the same work at every release: a pointer to a Case, a decision or a session stands in this repository in a bracket of its own at the end of its sentence, with the words that go with it, such as `(as set in case 12)`, and the script removes each bracket that holds a pointer whole. The person asked who checks that the script removes nothing needed: what it removes is a bracket that holds a pointer into the records of this repository, which the copy does not hold, and `--review` lists each such bracket that holds other words, so that a needed word is found once and moved out; the writing rule in `case-schema.md`, the check of the plan and a step of `make lint` keep new text in the form.
>
> The run of this session, `uv run guppi ship` at commit 6d9afab, stands in `vault/raw/2026-10-13/2118/ship.txt`; a Grep `^ship: [^g]` over it printed its lines 207 to 312, all under `vault/wiki/`: the rendered schema files, `case-example.md`, `orchestration.md`, `entity-glossary` and rule pages. Some are ids of example Cases, such as `## Case 7 — Members get a reminder before a booking` inside a fenced block of `orchestration.md`, and sample slugs in code spans of `vault/wiki/decisions/schema.yaml`, which the script reads as plain text since it masks code spans only in `.md` files. That schema file ships by right: a new project writes Decision pages of its own. In a round I said that the example of `case-example.md` cannot be fenced; the frame shows that it stands inside a fence tagged `case`, so the fence rule alone covers it, and the exemption of that file and of the Render of `rule-case-example` by name, which the person chose on my word, adds nothing today; the Case keeps it as chosen, and the person may drop it at the showing. The person first chose to reword the pages in this Case from that run; I had said that the run shows every page line that holds a pointer, which is false, since today's script cuts pointers out of longer brackets without a line, and the person then chose a Case of the next session that rewords the pages from the list of the changed script. 807.1 updates `entity-sprint-plugin` with a `change` alone, since the check of the plan asks for an update of the sprint page under a Case that works on its item, and the item stays open until that Case; Case 805 of this session defers the same page, by its line `defer case 805` in `vault/raw/2026-10-13/2118/frontier.md`, and touches no line this Case touches.
>
> The judgment. A Grep `\[Cc\]ases?|[Ss]essions?\\s|decision-case-\{` over `guppi/` printed `guppi/box.py`, `guppi/materialize.py`, `guppi/lint.py` and `guppi/ship.py`. The lines of `guppi/box.py` and `guppi/materialize.py` write a slug `decision-case-N`, and those of `guppi/lint.py` judge the words of a `method`; only `REFS`, `DECISION_LINK`, `DECISION` and `SESSION` of `guppi/ship.py` judge a pointer in prose — a reference to a case, a link or an id of a Decision page, and a mention of a session — so the check of the plan in 807.4 and `--check` in 807.1 import the judgment of `guppi/ship.py`, as `rule-one-judgment-one-implementation` sets it, and no second copy is written. `guppi/prespec.py` judges no pointer today, so the two sides cannot part on an older input.
>
> The frame. A Grep `guppi ship|all five|five steps` over `vault/wiki/` printed 12 files: `brief.md`, not read; the three `schema.yaml` files of entities, rules and estimates and their rule pages `rule-entities-schema`, `rule-rules-schema` and `rule-estimates-schema`, which name the value `guppi` of a shipped page and stand; `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy`, set anew in 807.1; `rule-lint` and `estimate-lint-runs-every-step`, which name the five steps of `make lint` and change in 807.2; and `estimate-sprint-plugin-ci-writes-a-clean-branch`, whose line that no text of the copy holds a link to a page the copy leaves out stays true, since such a link becomes a slug in a code span, so its Criterion stands and it is read after the Case of the next session. The same Grep over `.claude/` printed nothing. A Grep `case-schema\.md|rule-case-protocol|rule-lint\.md|rule-clean-branch|rule-prespec-hook|entity-sprint-plugin|estimate-lint-runs-every-step|estimate-clean-branch` over `tests/` printed `tests/test_guard.py`, `tests/test_glossary.py`, `tests/test_ship.py`, `tests/test_case_schema.py`, `tests/test_render.py`, `tests/test_lint.py`, `tests/test_prespec.py` and `tests/test_recall.py`. `tests/test_case_schema.py` reads only the block tagged `case` of the live `case-example.md` or `case-schema.md`, which no pair touches; `tests/test_recall.py` names the path of `case-schema.md` alone; the others seed pages of their own in a temporary folder. `tests/test_lint.py` copies the live `Makefile` and lists the steps of `make lint` in `LINT_STEPS`, so 807.2 changes it. In the page of `rule-case-protocol` the sentence that the story sections may name a case number speaks of text that reaches no shipped page, and stands. The Render of `rule-case-protocol` changes in 807.4 and touches no Estimate of the live reading; the behaviour it tells `case-guppi` is the one the check of 807.4 finds. The brief reports `make lint` at 0 lines and `make test` at 1601 passed and 6 skipped under `## Readings at the close`; the new step of 807.2 is red until the code is reworded in 807.3, an expected red of the same Work Mode. Case 806 of this session changes `rule-orchestration`, `rule-case-build` and `rule-work-mode`, none of the pages of this Case; its check of the plan in Work Mode runs the finding of 807.4 once the code stands. The pair of 807.4 on `rule-case-protocol` adds one sentence, after the sentence on counts, inside the long paragraph of the Language section on the story sections, `given`, `when`, `then` and the chat form, which I read whole: that paragraph lets the story sections name a case number and sets the form of the values of a task, and the new sentence speaks only of the new text of a page with `core: true`, so it contradicts neither; Case 803 of session 1753 wrote into the same page, in the paragraph on the derivable fields, and touches no sentence of this one. The new Criteria carry word for word each old line that still holds: in 807.1 the set of files written, the shipped values, the exit on a section of a page without `core: true`, the pages and files left out, and the form of a line; in 807.2 the printing of each step, the exit code, stdin and the tree. Three old lines are dropped on purpose and stand rewritten: in 807.1 the line that removes a parenthesis of references and cuts references out of a longer one, and the line that exits 1 on a link to a page left out, since the person's rule removes each bracket that holds a pointer whole and turns such a link into a slug; in 807.2 the line that names five steps, since `guppi ship --check` is a sixth. `--check` judges each file outside `vault/` that the clean version holds — `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml` and `.gitattributes`, by `TREES` and `ROOT_FILES` of `guppi/ship.py` but `uv.lock`, which it does not clean. The rewording of 807.3 covers `guppi/` and the root files edited in Work Mode; a file of `.claude/` and `CLAUDE.md` is rendered from a Rule page and changes only through it, as `rule-governed-files-hook` sets it, so a line on it goes to the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`. The run of today's script printed no line outside `guppi/` and `vault/wiki/`; the new judgment has not run. The line of 807.3 on `--check` shares words with the lines of 807.1 on `--check` and on the files the command writes, since all three name the same files, but sets another promise: 807.1 promises what the command does, 807.3 that the code of this repository passes it.

> **problem:**
> The clean copy cannot be written: the script fails on pointers it cannot remove safely, and it cuts pointers out of longer brackets in a way that can leave words that mean nothing. No rule says how a pointer is written so that the script can remove it, and nothing keeps new text in such a form.

> **recommend:**
> - **How should a pointer inside a sentence of the code be reworded?**
>   - Recommended: (a) move the pointer into brackets at the end of the sentence.
>   - Answer: not answered; the person stopped the round to ask what is removed from the pages and how. It was replaced by **What is the one form a pointer takes, so the script strips it at every build?**
> - **Does `guppi ship` learn to clean more forms, or is every leftover reworded at its source?**
>   - Recommended: (c) reword every leftover at its source, and the check flags each number of a list of sessions.
>   - Answer: not answered; replaced by **What is the one form a pointer takes, so the script strips it at every build?** and later by **What marks a bracket that the script removes?**
> - **Does this Case also reword the pages and the files built from them?**
>   - Recommended: (b) run `guppi ship` now and cover the pages too.
>   - Answer: not answered; replaced by **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
> - **What is the one form a pointer takes, so the script strips it at every build?**
>   - Recommended: (a) a bracket that holds only pointers to Cases, decisions or sessions; any other bracket with a pointer is listed, and each number of a list of sessions is flagged.
>   - Answer: agreed, (a); later replaced by **What marks a bracket that the script removes?**
> - **What happens to a link to a page that does not ship?**
>   - Recommended: (a) the script turns it into the slug in a code span.
>   - Answer: agreed, (a).
> - **Where is the right form checked as new text is written?**
>   - Recommended: (a) in the check of the plan for pages, told to `case-guppi` in `case-schema.md`, and in `make lint` for the code and the harness, both importing the one check of `guppi/ship.py`.
>   - Answer: agreed, (a).
> - **Does this Case also reword the page leftovers, which needs a run of the script before I build?**
>   - Recommended: (a) yes, after a run of `uv run guppi ship` saved in the session folder.
>   - Answer: agreed, (a); the run was made. Later replaced by **Does this Case still reword the pages, now that the script's list will change?**
> - **What happens to a pointer that shares a bracket with other words?**
>   - Recommended: (b) also strip a pointer that ends a bracket after a comma, a semicolon or a dash.
>   - Answer: not answered; the person asked who checks that the script removes nothing needed, and asked that a pointer and the words that go with it, session numbers and times among them, stand inside the bracket. It was replaced by **What marks a bracket that the script removes?**
> - **What marks a bracket that the script removes?**
>   - Recommended: (a) any bracket that holds a pointer is removed whole; a pointer outside a bracket fails the run; the script lists every bracket that holds a pointer and other words, so that each is reviewed once.
>   - Answer: agreed, (a).
> - **Does this Case still reword the pages, now that the script's list will change?**
>   - Recommended: (a) this Case changes the script, writes the rule, adds the two guards and rewords the code; a Case of the next session rewords the pages from the list of the changed script.
>   - Answer: agreed, (a), in place of the earlier answer.
> - **How does the script treat the ids of example Cases?**
>   - Recommended: (a) the script reads a fenced block of a Markdown file as a sample, like a code span, and leaves `case-example.md` and the Render of `rule-case-example` out of the pointer check.
>   - Answer: agreed, (a).
> - **How does the script read the text of a `schema.yaml`?**
>   - Recommended: (a) the script reads a code span in a `schema.yaml` as it reads one in Markdown.
>   - Answer: agreed, (a).
> - **How does the Case split, and how is each part checked?**
>   - Recommended: (a) three sub-cases, each with its own check.
>   - Answer: agreed, (a); later replaced by **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
> - **How is the rewording of the code checked, now that one sub-case cannot carry two checks?**
>   - Recommended: (a) four sub-cases: the new step of `make lint` and the rewording of the code are separate.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, carry each line of the old Criteria that still holds, say why a dropped line is dropped, and date the check of the plan before the Spec is approved, not before a Case is signed.
>   - Taken: 807.1 carries word for word the lines on the pages and files left out, on the sections of a page without `core: true` and on the form of a line, and the `context` says why three lines stand rewritten; the Purpose of `rule-clean-branch` says that `/pre-spec` finds a pointer before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run.
> - **Change**
>   - Asked: at pre-spec, `--check` judges every file outside `vault/` that `guppi ship` writes, the root files included, and the rewording of the code covers only the files Work Mode may edit.
>   - Taken: `--check` judges `guppi/`, `.claude/` and the root files in 807.1, 807.2 and the Purpose of `rule-clean-branch`; 807.3 rewords `guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`, and a line on `.claude/` or `CLAUDE.md` goes to the handoff with the pages.
> - **Change**
>   - Asked: at pre-spec, the `context` names `SESSION` among the patterns of `guppi/ship.py` that judge a pointer.
>   - Taken: the `context` names it.
> - **Change**
>   - Asked: at pre-spec, the line of 807.1 on `--check` leaves out `uv.lock`, as the task and the `context` do.
>   - Taken: the line says that `--check` judges each file it would write outside `vault/` but `uv.lock`.

### Case 807.1 — guppi ship removes each bracket that holds a pointer

> **given:**
> `rule-clean-branch`: the rule of the clean version; its Purpose is set anew.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `guppi/ship.py`: the command `guppi ship` and the one judgment of a pointer.
> **＋** `tests/test_ship.py`: the tests of the command over a sample tree.
> **＋** `entity-sprint-plugin`: the sprint page whose milestone The clean branch this Case works on.
> **＋** `vault/wiki/case-example.md` and `rule-case-example`: the example Case, whose ids are no pointers.
> **＋** `vault/wiki/decisions/schema.yaml`: a schema file of the copy whose text holds sample slugs in code spans.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff of the session, which takes the list of the pages.
> **＋** `.claude/` and `vault/wiki/tags.md`: the harness and the tag registry the command copies.
> **＋** `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock` and `.gitattributes`: the files at the root of the project that the command copies, outside `vault/`.
> **＋** `decision-case-N`: the slug of a Decision page, a pointer the command removes.
> **＋** `vault/raw/`, `vault/archive/` and `.github/`: the session records and the workflows the command leaves out.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run guppi ship --review <folder>` does the same.
> **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - sections.Purpose:
>     ```
>     Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes.
>
>     A pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — stands in this repository in a bracket of its own at the end of its sentence, together with the words that go with it, such as `(as set in case 12)` or `(measured 2026-09-25, session 0051)`, so that the sentence reads whole without it. `guppi ship` removes each bracket that holds a pointer whole, every word in it included, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays. It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. A case id in a code span or a fenced block, of a Markdown file or of the text of a `schema.yaml`, in `case-example.md` or the Render of `rule-case-example`, or in the form of a line after `[case `, `#case-` or `:case `, is no pointer. It exits 1 on each pointer that stands outside such a bracket, and on each section of a page without `core: true`; a Case rewords that text at its source. `guppi ship --review` also lists each bracket it removes that holds words beside its pointer, so that a word the sentence needs is found and moved out of the bracket. `guppi ship --check` judges in place each file outside `vault/` that the clean version holds — the code, the harness and the files at the root of the project — and `make lint` runs it; `/pre-spec` finds a pointer outside such a bracket in the new text of a page with `core: true` before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run (case 807).
>
>     The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).
>     ```
>   - change: `a pointer stands in a bracket of its own, which guppi ship removes whole; a link to a page left out becomes its slug; --review and --check (case 807.1)`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship writes only the code, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes"
>     ```
>   - change: `the Criterion replaced whole — each bracket that holds a pointer removed whole, a link to a page left out as its slug, samples and examples kept, --review and --check (case 807.1)`
> - [ ] update `entity-sprint-plugin`
>   - change: `the clean branch: guppi ship removes each bracket that holds a pointer; the pages are reworded by a Case of the next session (case 807.1)`
> - [ ] `guppi/ship.py`: the `then` of this Case. A bracket with no bracket inside it, on one line or across lines, that holds a pointer is removed whole; the pointer of a session takes each id of a list, as `REFS` does for cases; a fenced block of a Markdown file and the text of a `schema.yaml` are masked like a code span; `vault/wiki/case-example.md` and the section between the markers of `rule-case-example` are not judged; `--review` and `--check` as the `then` sets them, `--check` over `TREES` and `ROOT_FILES` but `NOT_CLEANED`. The judgment of a pointer — its patterns, the masking, the removal and the list of what remains — is one set of functions of this module, which `guppi/prespec.py` imports. The docstring names the rule.
> - [ ] `tests/test_ship.py`: the tests of the removal and of what remains follow the new rule — a bracket with words and a pointer removed whole, a bracket with no pointer kept, a session in a bracket removed, each id of a list of sessions printed, a link to a page left out written as its slug — and new tests of a fenced block, of a code span in a `schema.yaml`, of `case-example.md`, of `--review` and of `--check`.
> - [ ] `uv run guppi ship --review` into an empty temporary folder after the change: its lines under `vault/wiki/`, and its lines on `.claude/` and `CLAUDE.md`, which change only through their Rule pages, go into the handoff for the Case of the next session that rewords the pages; its lines under `guppi/` and on `Makefile`, `pyproject.toml` and `.gitattributes` are the work of 807.3.
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 807.1][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 807.1][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> - decision[case 807.1][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```

### Case 807.2 — make lint runs the pointer check of guppi ship

> **given:**
> `Makefile`: the recipe of `make lint`.
> **＋** `rule-lint`: the rule of lint, whose `implementation_ref` names the `Makefile`; its Purpose names the steps of `make lint`.
> **＋** `estimate-lint-runs-every-step`: its Criterion is replaced whole.
> **＋** `tests/test_lint.py`: runs the recipe of the live `Makefile` with a fake `uv`.
> **＋** `guppi ship --check`: the new step, as 807.1 sets it.
> **＋** `/work` and `.claude/agents/librarian-guppi.md`: where `make lint` runs.

> **when:**
> Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.
> **＋** Or `tests/test_lint.py` runs `make lint` of the `Makefile` in a temp folder, with a fake `uv` first on the search path that records each call and fails the step `guppi backlog --check`.
> **＋** Or `tests/test_lint.py` runs it the same way, with a fake `uv` that exits 0 for every step.

> **then:**
> `make lint` runs each of the steps `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

> **tasks:**
> - [ ] `Makefile`: the target `lint` runs `uv run guppi ship --check < /dev/null || status=1` after `guppi lint`, and its `##` line names the check of the pointers in the files outside `vault/` that the clean version holds.
> - [ ] `tests/test_lint.py`: `LINT_STEPS` ends with `run guppi ship --check`.
> - [ ] update `rule-lint`
>   - old: `` `make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`; all five only report, so the Makefile's rule — no target writes to the tree — holds (cases 147.7, 227). It runs all five even when one of them is red, ``
>   - new: `` `make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds (case 807.2); all six only report, so the Makefile's rule — no target writes to the tree — holds (cases 147.7, 227). It runs all six even when one of them is red, ``
>   - change: `make lint runs guppi ship --check as its last step (case 807.2)`
> - [ ] update `estimate-lint-runs-every-step`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether make lint runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, and exits non-zero when any step is red"
>     ```
>   - change: `the Criterion replaced whole — guppi ship --check is the last step of make lint (case 807.2)`
> - [ ] read `estimate-lint-runs-every-step`

> **ratification:**
> ```
> - decision[case 807.2][update][rule-lint]{ref:rule-lint}
> - decision[case 807.2][update][estimate-lint-runs-every-step]{ref:rule-lint}
> ```

### Case 807.3 — The code holds each pointer in a bracket of its own

> **given:**
> `guppi/`: the modules whose comments and docstrings hold pointers.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: the new check of the code.
> **＋** `rule-clean-branch`: the rule of a pointer in a bracket of its own.
> **＋** `guppi ship --check` and `guppi ship --review`: the judgment of the working tree and the list of brackets with words, as 807.1 sets them.
> **＋** `Makefile`, `pyproject.toml` and `.gitattributes`: the files at the root that `--check` judges, edited in Work Mode.
> **＋** `.claude/` and `CLAUDE.md`: the harness that `--check` judges too, which changes only through its Rule pages.
> **＋** `raw/<date>/<hi HHMM>/handoff.md` and `rule-retro`: where a line on the harness goes, and the note of a red check.
> **＋** `make test`: the suite of the code.

> **when:**
> At Retro of the session, `uv run guppi ship --check` judges the working tree, and `uv run guppi ship --review <folder>` builds the clean version into an empty folder.

> **then:**
> `uv run guppi ship --check` prints no line on a file under `guppi/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **－** No line of `guppi/` changes but a comment or a docstring, and `make test` has no failing test that it did not have before the change.
> **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`.

> **tasks:**
> - [ ] `guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`: each pointer that `uv run guppi ship --check` prints on these files moves, with the words that go with it, into a bracket of its own at the end of its sentence, or its sentence is reworded so that it needs no pointer; each bracket on these files that `--review` prints is split so that a word the sentence needs stands outside it.
> - [ ] create `estimate-clean-branch-code-holds-pointers-only-in-brackets`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether the code and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs`
>   - method: `by hand, at Retro: the lines of uv run guppi ship --check over the working tree, and of uv run guppi ship --review into an empty temporary folder, on guppi/, Makefile, pyproject.toml and .gitattributes, read against the Criterion`
>   - tags: `[ci, plugin]`
> - [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 807.3][create][estimate-clean-branch-code-holds-pointers-only-in-brackets]{ref:rule-clean-branch}{tags:ci,plugin}
> ```

### Case 807.4 — The check of the plan finds a pointer outside its bracket

> **given:**
> `guppi/prespec.py`: the check of the plan, `uv run guppi prespec --check`, and the hook of `ExitPlanMode`.
> **＋** `rule-prespec-hook`: the rule of the check, whose `implementation_ref` names `guppi/prespec.py`.
> **＋** `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: the new check.
> **＋** `tests/test_prespec.py`: the tests of the check.
> **＋** `guppi/ship.py` and `guppi/pages.py`: the judgment of a pointer and `is_core`, which the check imports.
> **＋** `rule-case-protocol` and `vault/wiki/case-schema.md`: the form of a Case, which tells `case-guppi` how a pointer stands.
> **＋** `decision-case-N`: the slug of a Decision page, a pointer the check finds.
> **＋** `rule-one-judgment-one-implementation`: one judgment, one implementation.

> **when:**
> `uv run guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by the judgment that `guppi ship` runs over the files it writes, imported from `guppi/ship.py`.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true`, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

> **tasks:**
> - [ ] `guppi/prespec.py`: the finding as the `then` of this Case sets it, by the judgment of `guppi/ship.py` and `is_core` of `guppi/pages.py`; the module docstring names it among the findings of `--check`.
> - [ ] `tests/test_prespec.py`: one test per line of the `then` of this Case, the names of the tests holding `pointer`.
> - [ ] create `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
>   - ref: `rule-prespec-hook`
>   - kind: `QA`
>   - purpose: `Whether the check of the plan finds a pointer to a case, a decision or a session that stands outside a bracket of its own in the new text of a page with core: true`
>   - method: `uv run pytest tests/test_prespec.py -k pointer`
>   - tags: `[harness, ci]`
> - [ ] update `rule-case-protocol`
>   - old: `such as more than 400 000 tokens, stands (case 449).`
>   - new: `` such as more than 400 000 tokens, stands (case 449). In the new text a Case writes for a page with `core: true` — the `new` of a pair, a section, a `purpose` — a pointer to a Case, a decision or a session stands in a bracket of its own at the end of its sentence, with the words that go with it, such as `(as set in case 12)`, since `guppi ship` removes that bracket whole from the clean version and the sentence must read whole without it; a pointer outside such a bracket is a finding of `/pre-spec` (case 807.4). ``
>   - change: `a pointer in the new text of a page with core: true stands in a bracket of its own (case 807.4)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`

> **ratification:**
> ```
> - decision[case 807.4][create][estimate-prespec-hook-reports-a-pointer-outside-a-bracket]{ref:rule-prespec-hook}{tags:harness,ci}
> - decision[case 807.4][update][rule-case-protocol]{ref:rule-case-protocol}
> ```
