## Case 995 — The searches for a new file's folder stand in the Case, and pre-spec checks them

> **context:**
> The Render of `rule-case-build` tells `case-guppi` what to do when a task of its Case adds a file that is no page of `vault/wiki/`. It searches `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds the file. It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder. It reads each `.gitignore` there and each reader that takes every file of such a folder. Nothing the agent leaves shows whether it did these steps. The reading of `estimate-case-build-reads-the-readers-of-a-new-files-folder` in session 2038 (line 17 of `raw/2026-11-01/2038/ledger.md`) checked the new file `.claude/skills/approve-spec/SKILL.md` of Case 987. Of 8 searches and readings, 2 were done, 1 in part and 5 missing. One missing reader was `callers()` of `.guppi/tests/test_guppi_package.py`, and `ask-guppi` at `/pre-spec` raised no finding on it. I read `callers()` whole: it takes the `Makefile` and every file under `.claude` and `.github/workflows` but `settings.local.json`. The person made three choices. First, the `context` of such a Case names each of those searches and readings (995.1); the rerun of the searches `context` names, which comes just before the summary, then covers them, as Case 979 did for a list member. Second, `ask-guppi` at the first `/pre-spec` checks that list, through a new question in the Render of `rule-prespec`, and runs its own Grep of the code for folder walks, which a new sentence of the Render of `rule-ask` allows (995.2). Third, `estimate-prespec-reconciles`, whose Criterion lists the questions of `/pre-spec`, gets the new question (995.3). That change stands in a sub-case of its own, since `case-schema.md` sets one promise per sub-case and 995.2 already creates an Estimate. The governing rule is the sentence of `rule-case-build` from case 629.5: `context` names a search only when the Case rests on it. The new sentence states the claim the searches rest on, namely that the new file makes no reader of its folders wrong. So the sentence and the Criterion of `estimate-case-build-checks-the-finished-case`, which carries the same rule, stand. The new texts of `core: true` pages put each pointer to a Case in a bracket at the end of its sentence, and the pair on `rule-prespec` adds no pointer. I read the blocks of `rule-case-build`, `rule-prespec`, `rule-ask`, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-prespec-reconciles`, `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md` and `.claude/skills/pre-spec/SKILL.md` in `.guppi/links.md`. The block of `estimate-prespec-reconciles` has an empty purpose line. Four neighbours bear on the change, and each stands. `estimate-ask-searches-at-prespec` already allows further Greps as a finding needs. `estimate-ask-finds` sets one list per question of the skill, so the new question gets its own list. Its line that `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself also stays true, since the new sentence of `rule-ask` only allows the one Grep of `.guppi/guppi/` and `.guppi/tests/` for the question that `/pre-spec` sets and does not repeat that question (finding 2.1 of `/pre-spec`). After finding 1.5 of `/pre-spec`, a second pair on `rule-prespec` adds the `tasks` block to what the dispatch tells `ask-guppi` to read for every Case, because only the `tasks` block shows which Case adds a file; 995.3 carries the same list in the Criterion of `estimate-prespec-reconciles`, so its dispatch line is not carried as it stood either. `estimate-prespec-confirms-the-findings-once` allows no Grep at the confirmation, and 995.2 keeps it that way. The other Estimates of `rule-prespec` speak of `prespec --check` and of the loop, not of the questions of `ask-guppi`. The sentence of `rule-ask` that it searches the vault at `vault/wiki/` stands, because the new sentence names the one Grep of the code beside it. A Grep `speaks of the thing the Case changes` found the texts that list the questions of `/pre-spec`. Over `vault/wiki/` it printed `rules/rule-prespec.md` and `estimates/estimate-prespec-reconciles.md`, over `.claude/` it printed `skills/pre-spec/SKILL.md`, and over `.guppi/guppi/` it printed nothing; this Case changes all three texts. A Grep `walk a folder` printed `rules/rule-case-build.md` and `estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md` over `vault/wiki/`, and `agents/case-guppi.md` over `.claude/`. A Grep `CALLERS|REPO / "\.claude"` over `.guppi/tests/` printed `test_guppi_package.py` alone. Its test over `callers()` looks for `uv run guppi` and `uv run pytest`, and the new texts hold neither. Its test over the live pages runs `Vault.reword_text` with `guppi/` and `tests/`. I read `reword_text`, `reword_pattern` and `is_path_pair` of `.guppi/guppi/generate.py` and `PATH_START` of `.guppi/guppi/lint.py`, which is `(?<![\w./-])`. A path `old` matches only where no `.` or `/` stands before it, so neither matches in `.guppi/guppi/` or `.guppi/tests/`, the only forms the new texts use. I read `check_frame` and `frame_name` of `.guppi/guppi/prespec.py`: each code span of `when` or `then` that is a slug, or that holds a `/`, must stand in the text of `given`, and the lines of `given` are written for that. The check of this file noted that some `then` lines of 995.2 and 995.3 share most of their words with lines of 995.1. They stand: 995.1 sets what `case-guppi` searches and names in `context`, 995.2 sets what `ask-guppi` checks and searches on that `context` at `/pre-spec`, and 995.3 sets the text of the question in the list of `estimate-prespec-reconciles`. These are three agents' or texts' acts on one subject, which the person chose, not one promise signed twice. The check also noted that the old line on the questions of `estimate-prespec-reconciles` is not carried. That line is carried with the new question added, which is the change. Its last `－` line, on a deferred decision, was missing from the first build and is now carried word for word. A Glob `vault/**/estimate-prespec-finds-a-reader*` printed nothing, so the new slug is free. It is a `create` with a `ref`, so no vault query runs. The Greps `lesson\[error\]` and `\{addresses:` over the ledger of session 2227 printed nothing.

> **problem:**
> `case-guppi` did few of the searches and readings that its rule sets for a new file outside the vault pages, and missed a test that reads every file of that file's folder. Nothing in the Case shows which of them it made, and `ask-guppi` at `/pre-spec` did not look for the reader it missed.

> **recommend:**
> - **What changes after the failed reading**
>   - Recommended: (a) the Case lists each search and reading it made for the new file.
>   - Answer: (a).
> - **Whether the second agent's check is part of this Case**
>   - Recommended: (a) no, this Case covers only the agent that builds Cases.
>   - Answer: (b) yes, a second part of this Case changes the plan checker too.
> - **Where the plan checker's new step goes**
>   - Recommended: (a) a new question in the `/pre-spec` list.
>   - Answer: agreed, (a).
> - **How far the plan checker looks on its own**
>   - Recommended: (b) it checks the list and also runs its own search for folder walks.
>   - Answer: agreed, (b).
> - **How the builder's part is checked**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-reads-the-readers-of-a-new-files-folder` and set it back to waiting.
>   - Answer: agreed, (a).
> - **How the plan checker's part is checked**
>   - Recommended: (a) a new check on `rule-prespec`, and `estimate-prespec-reconciles` gets the new question in its list.
>   - Answer: agreed, (a).

### Case 995.1 — The Case names each search and reading for a new file's folder

> **given:**
> `rule-case-build`: the rule whose Render, rendered into `.claude/agents/case-guppi.md`, sets the searches and readings for a new file.
> **＋** `estimate-case-build-reads-the-readers-of-a-new-files-folder`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/`: the code the searches run over.
> **＋** `.guppi/tests/`: the tests the search for folder walks runs over.
> **＋** `vault/wiki/rules/`: the Rule pages the search for a folder path runs over.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

> **then:**
> It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path of each folder that holds the new file.
> **＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It reads each ignore file of git in a folder that holds the new file.
> **＋** It reads each reader that takes every file of a folder that holds the new file.
> **＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** The `context` of the Case names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether the new file makes it wrong.
> **－** A page that a `create` adds under `vault/wiki/` starts no such search.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` each one the new file makes wrong enters the Case, or `context` names it and says why it stands (as set in case 974). ``
>   - new: `` each one the new file makes wrong enters the Case, or `context` names it and says why it stands; `context` names each of these searches, with its pattern, its paths and each file it printed or the count it printed, and each `.gitignore` and each reader you read, with whether the new file makes it wrong, since the claim that the new file makes no reader of its folders wrong rests on them (as set in cases 974 and 995.1). ``
>   - change: `the context of a Case that adds a file that is no page names each search and reading for the folders that hold it`
> - [ ] update `estimate-case-build-reads-the-readers-of-a-new-files-folder`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders that hold it and for the calls that walk a folder, reads the ignore files of git there and each reader that takes every file of such a folder, enters each one the new file makes wrong in the Case or names it in context, and names in context each of those searches and readings"
>     method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that names in context each search and reading for the folders of a new file, and in which a Case adds a file that is no page of vault/wiki/: the agent transcript of the case-guppi of that Case under ~/.claude/projects/, read for each search and reading of the Criterion, and its case file under raw/<date>/<hi HHMM>/cases/, read for the list of them in context; the count, the transcript and the case file in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the context names each search and reading for the folders of a new file`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-new-files-folder`

> **ratification:**
> ```
> - decision[case 995.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 995.1][update][estimate-case-build-reads-the-readers-of-a-new-files-folder]{ref:rule-case-build}
> ```

### Case 995.2 — ask-guppi at pre-spec looks for the readers of a new file's folder

> **given:**
> `.claude/skills/pre-spec/SKILL.md`: the skill rendered from `rule-prespec`, whose questions `ask-guppi` answers; it gains the question.
> **＋** `.claude/agents/ask-guppi.md`: the agent file rendered from `rule-ask`; it gains the Grep of the code.
> **＋** `.claude/agents/case-guppi.md`: sets the searches and readings for a new file that the question checks.
> **＋** `estimate-prespec-finds-a-reader-of-a-new-files-folder`: the new check of the question and the Grep.
> **＋** `.guppi/guppi/`: the code the Grep runs over.
> **＋** `.guppi/tests/`: the tests the Grep runs over.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`; the agent follows `.claude/agents/ask-guppi.md`, rendered from `rule-ask`; and a Case of the plan has a line in its `tasks` block that adds a file that is no page of the vault.

> **then:**
> `ask-guppi` reads the `tasks` block of each Case of the plan, as the dispatch of `.claude/skills/pre-spec/SKILL.md` tells it, and answers, for a Case with such a line, whether its `context` names each search and reading that `.claude/agents/case-guppi.md` sets for the folders that hold the new file.
> **＋** A search or a reading that the `context` misses is a finding that names the Case and what it misses.
> **＋** Beside its searches of the vault, it runs one Grep of `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`, and reads around its line each hit whose folder holds the new file.
> **＋** Each reader that takes every file of such a folder and that the Case does not name is a finding that names the Case and the reader.
> **－** A plan with no such Case starts no Grep of the code, and the question says "none".
> **－** At the confirmation of its findings, the agent runs no such Grep.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` and whether the `When` or `Then` of a Criterion a Case sets ``
>   - new: `` whether, for each Case of the plan with a line of its `tasks` block that adds a file that is no page of `vault/wiki/`, its `context` names each search and reading that `.claude/agents/case-guppi.md` sets for the folders that hold that file, and which reader that takes every file of such a folder the Case does not name; and whether the `When` or `Then` of a Criterion a Case sets ``
>   - old: `` — and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page ``
>   - new: `` —, its `tasks` block and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page ``
>   - change: `ask-guppi at pre-spec reads the tasks block of each Case and is asked about the searches and the readers of the folders of a new file that is no page`
> - [ ] update `rule-ask`
>   - old: `a question with no finding says "none" (case 626.1).`
>   - new: `` a question with no finding says "none" (case 626.1). For the question of `.claude/skills/pre-spec/SKILL.md` on a new file that is no page of `vault/wiki/`, run, beside your searches of the vault, one Grep of `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`, and read around its line each hit whose folder holds that file; this is the one search of the code you make (as set in case 995.2). ``
>   - change: `at pre-spec, ask-guppi greps the code and the tests for the folder walks that read a new file of a Case`
> - [ ] create `estimate-prespec-finds-a-reader-of-a-new-files-folder`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether ask-guppi at the first /pre-spec of a session checks, for each Case that adds a file that is no page, that its context names each search and reading for the folders that hold that file, greps the code and the tests for the calls that walk a folder, and names in a finding each reader of such a folder that the Case does not name`
>   - method: `by hand, after the first /pre-spec on the Render of rule-prespec and rule-ask that holds the question on the readers of the folders of a new file, whose plan holds a Case that adds a file that is no page of vault/wiki/: the findings of ask-guppi under that question and its Grep of .guppi/guppi/ and .guppi/tests/, read in its agent transcript under ~/.claude/projects/ against the Criterion; the count and the transcript in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-prespec-finds-a-reader-of-a-new-files-folder`

> **ratification:**
> ```
> - decision[case 995.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 995.2][update][rule-ask]{ref:rule-ask}
> - decision[case 995.2][create][estimate-prespec-finds-a-reader-of-a-new-files-folder]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 995.3 — The list of the questions of pre-spec holds the new question

> **given:**
> `estimate-prespec-reconciles`: its Criterion is replaced whole.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill rendered from `rule-prespec`, whose questions the Criterion lists.
> **＋** `.claude/agents/ask-guppi.md`: the agent file rendered from `rule-ask`, which checks the searches and readings that `.claude/agents/case-guppi.md` sets for a new file that is no page of `vault/wiki/`.
> **＋** `estimate-prespec-notes-a-page-another-case-defers`: the check of the note on a page that another Case of the plan defers.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `rule-spec-write`: its hook writes a Case built again into the plan.
> **＋** `rule-skill-hi`: sets at `/hi` the title line that names a conserved Spec.
> **＋** `entity-sprint-<id>`: a sprint page, whose Estimates the last question leaves out.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run --project .guppi guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then`, `then` block and `tasks` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** The questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out; whether, for each Case of the plan with a line of its `tasks` block that adds a file that is no page of `vault/wiki/`, its `context` names each search and reading that `.claude/agents/case-guppi.md` sets for the folders that hold that file, and which reader that takes every file of such a folder the Case does not name; and whether the `When` or `Then` of a Criterion a Case sets asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session.
> **＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The last question finds nothing where a part of the `method` waits for an event it names that brings that reading, nor in the Criterion of an Estimate whose target is a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint.
> **－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run --project .guppi guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

> **tasks:**
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the questions of /pre-spec hold the one on the readers of the folders of a new file`
> - [ ] read `estimate-prespec-reconciles`

> **ratification:**
> ```
> - decision[case 995.3][update][estimate-prespec-reconciles]{ref:rule-prespec}
> ```
