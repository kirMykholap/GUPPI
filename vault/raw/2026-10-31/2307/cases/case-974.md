## Case 974 — The builder reads the readers of the folder of a new file

> **context:**
> When `case-guppi` builds a Case that changes what a step writes, the Render of `rule-case-build` makes it search the rules and `.claude/` for the name of that output and read each step that reads it (cases 924, 966). A reader that takes every file of a folder holds no word of a new file there, so that search misses it. `lesson-case-build-names-a-file-without-the-readers-of-its-folder`, written at the Retro of session 1831, records such a miss: Case 967.3 added the generated file `.guppi/links.md`, and the full test run failed on the test of the live code of `test_ship.py`, since the clean copy would carry the graph; Work Mode added the file to `LEFT_OUT` of `.guppi/guppi/ship.py`. I read in `.guppi/guppi/ship.py` the function `tree_files` whole, which walks a folder by `os.walk` and takes each file but the skipped names, `TREES`, which names the folders as bare names `.guppi` and `.claude`, `LEFT_OUT`, and the lines that call `tree_files` over `TREES` and drop each name of `LEFT_OUT`; `.guppi/.gitignore` holds `links.md`, a second reader of the folder that names the file by its bare name. The person chose that, for each new file that is no page of `vault/wiki/`, the builder searches for the path of each folder that holds it and for the calls that walk a folder, reads the ignore files of git there, and reads each reader that takes every file of such a folder; a page that a `create` adds is left out, since the schema of its category and lint set its readers. The change is a new sentence of the Render, after the sentence of cases 924 and 966, and that sentence stands, since it speaks of a reader that names the output. The rule that governs the choice is `rule-atomicity`: a reader that names the output and a reader that walks a folder can fail apart and need different fixes, so the change is checked by a new Estimate, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, and the Criterion of `estimate-case-build-reads-the-readers-of-a-changed-step` stands with its pending reading. The Criteria of `estimate-case-build-reads-the-link-graph-of-what-it-changes` and `estimate-case-build-reads-each-list-of-a-new-member` speak of the link graph and of a member of a list, and stand. A Glob `vault/**/estimate-case-build-reads-the-readers-of-a-new-file*` printed nothing, so the slug is free; the `create` carries a `ref`, so no vault query runs. The lesson reopened `insight-case-build-changes-a-step-without-reading-its-readers`; the person chose that this Case sets it `actioned`, by the form that its schema sets for a decision of the same session, the bare slug `decision-case-974`. The lesson was written in session 1831, so it takes no `{addresses:...}` mark, and the ledger of this session holds no `error` lesson. The block of `rule-case-build` in `.guppi/links.md` names its Estimates and the rules it links; the block of `.claude/agents/case-guppi.md` names `rule-ask`, `rule-case-build`, `rule-guppi-config`, `rule-lint`, `rule-prespec` and `rule-skill-grill-me`, and links in from `entity-guppi` by `code_ref`; the block of the Insight names its lesson and `rule-plugin-install`. None of them states what the builder reads for a new file, so none changes. `.guppi/tests/test_guppi_package.py` takes every file under `.claude` and `.github/workflows` by `rglob` in `callers`, over `CALLERS`, and reads each one live for the old commands `uv run guppi` and `uv run pytest`; the new sentence names neither. That test is itself a reader of a folder that no search of `.guppi/guppi/` would reach, so, by a finding of `/pre-spec`, the search for the calls that walk a folder covers `.guppi/tests/` too, within the person's choice of what the builder searches. The new sentence keeps its pointer in a bracket at its end, as `vault/wiki/case-schema.md` sets for a page with `core: true`. Item C5, the failed `estimate-case-build-reads-each-list-of-a-new-member`, stays its own item by the person's choice: its miss is a list of members, another behaviour with its own fix.

> **problem:**
> A builder that searches for the readers of a new file by its name misses the code that takes every file of the folder, so the miss shows only when a test fails in Work Mode.

> **recommend:**
> - **What the builder searches for a new file**
>   - Recommended: (a) the paths of the folders that hold the file, the calls that walk a folder, and the ignore files of git, then each reader that takes every file of such a folder.
>   - Answer: (a), by the recommendation.
> - **Which new files the search covers**
>   - Recommended: (a) each new file that is no vault page.
>   - Answer: (a), by the recommendation.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, read by hand after the first `/pre-spec` of a session in which a Case adds such a file.
>   - Answer: (a), by the recommendation.
> - **What happens to the reopened pattern note**
>   - Recommended: (a) this Case sets `insight-case-build-changes-a-step-without-reading-its-readers` `actioned`.
>   - Answer: (a), by the recommendation.
> - **Whether item C5 is part of this Case**
>   - Recommended: (a) apart; C5 stays its own Frontier item.
>   - Answer: (a), by the recommendation.

> **given:**
> `rule-case-build`: the rule whose Render gains the sentence on the readers of a folder.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-reads-the-readers-of-a-new-files-folder`: the new check of the search.
> **＋** `insight-case-build-changes-a-step-without-reading-its-readers`: the pattern this Case actions.
> **＋** `.guppi/guppi/`: the code searched for the paths of folders and for the calls that walk a folder.
> **＋** `.claude/`: the harness searched for the paths of folders.
> **＋** `vault/wiki/`: the pages; its Rule pages are searched, and a new page there starts no search.
> **＋** `.guppi/tests/`: the tests searched for the calls that walk a folder.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

> **then:**
> It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path of each folder that holds the new file.
> **＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It reads each ignore file of git in a folder that holds the new file.
> **＋** It reads each reader that takes every file of a folder that holds the new file.
> **＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A page that a `create` adds under `vault/wiki/` starts no such search.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966). ``
>   - new: `` each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966). When a task of the Case adds a file that is no page of `vault/wiki/` — a generated file, a module, a test or a harness file — Grep `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds it, the bare name of the folder too, Grep `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`, and read each `.gitignore` in a folder that holds it, since a reader that takes every file of a folder holds no word of a new file there; read each reader that takes every file of a folder that holds the new file, such as a walk that copies every file of a folder; each one the new file makes wrong enters the Case, or `context` names it and says why it stands (as set in case 974). ``
>   - change: `case-guppi reads, for a new file that is no page, the readers of each folder that holds it`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-the-readers-of-a-new-files-folder`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders that hold it and for the calls that walk a folder, reads the ignore files of git there and each reader that takes every file of such a folder, and enters each one the new file makes wrong in the Case or names it in context`
>   - method: `by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of the folder of a new file and in which a Case adds a file that is no page of vault/wiki/: the agent transcript of the case-guppi of that Case, read for each search and reading of the Criterion, and the findings of ask-guppi at that /pre-spec, read in its agent transcript, for a Case that adds a file and misses a reader of its folder; both under ~/.claude/projects/, the count and the transcripts in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] update `insight-case-build-changes-a-step-without-reading-its-readers`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-974
>     ```
>   - change: `actioned: case-guppi reads the readers of each folder that holds a new file that is no page (case 974)`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-new-files-folder`

> **ratification:**
> ```
> - decision[case 974][update][rule-case-build]{ref:rule-case-build}
> - decision[case 974][create][estimate-case-build-reads-the-readers-of-a-new-files-folder]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> - decision[case 974][update][insight-case-build-changes-a-step-without-reading-its-readers]{ref:insight-case-build-changes-a-step-without-reading-its-readers}
> ```
