## Case 893 — The clean copy keeps the event logs out of git, and its texts are read again

> **context:**
> `guppi ship` builds the clean copy of GUPPI that other projects install. `estimate-clean-branch-ships-neutral-texts` promises that no shipped rule, entity, `CLAUDE.md`, or `purpose` or `method` of a shipped Estimate holds a sentence true only in the repository of GUPPI. Its reading at the `/hi` of session 1805 failed. Case 881 rewrote the sentences that reading listed, but left out by the person's choice the texts that say the event log is gitignored. The handoff of session 2307 says the next reading still fails on the `.gitignore` method of `estimate-sprint-close-moves-old-event-logs`. Case 891 put the Estimate off. In this repository the two lines that keep `vault/raw/*/event_log.md` and `vault/archive/*/*/event_log.md` out of git stand in the root `.gitignore`, a file of this project that also holds lines of its own. `ROOT_FILES` of `.guppi/guppi/ship.py` holds only `CLAUDE.md` and `.gitattributes`, and `plan` of the same module takes no other root file, so the copy holds no `.gitignore` for the logs. In a project that installs GUPPI the shipped sentences that say the log is gitignored are false, and its event logs go into git. The person chose that this repository moves the two lines into a new `vault/.gitignore`, and that `guppi ship` writes that file into the copy. The git documentation at https://git-scm.com/docs/gitignore says that the patterns of a `.gitignore` match relative to the location of that file, and that a pattern with a slash in the middle is relative to the folder of that `.gitignore`. So `raw/*/event_log.md` and `archive/*/*/event_log.md` in `vault/.gitignore` match the same logs as the root lines. The install of `rule-plugin-install` copies each file of the plugin but its own, and stops when one of them already stands in the project. So `vault/.gitignore` reaches the project, and a project that already holds one cannot install, as for every other file. Its sentence that the installed files are the code, the harness, the files at the root and the core pages, as `guppi ship` built them, stands, since it describes the set by what `guppi ship` built. A Grep `gitignore` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `glossary.md`, `entities/entity-glossary.md`, `rules/rule-clean-branch.md`, `rules/rule-event-log.md`, `rules/rule-raw-archive.md`, `rules/rule-guppi-package.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-event-log-records.md`, `estimates/estimate-guppi-package-runs-from-its-own-folder.md` and `estimates/estimate-sprint-close-moves-old-event-logs.md`. Each hit stands once the copy holds `vault/.gitignore`. The row `Event log` and the sentences of `rule-event-log` and `rule-raw-archive` say the log is gitignored, and that is true in any project. `git check-ignore` in the Criterion of `estimate-event-log-records` reports the log ignored by the nearer file. The line on `.gitignore` in the Criterion and the `method` of `estimate-sprint-close-moves-old-event-logs` names a `.gitignore`, which `vault/.gitignore` is. The `rule-guppi-package` hit and its Estimate speak of `.guppi/.gitignore`, which does not change. The hit in `rule-clean-branch` is that same `.guppi/.gitignore`, and the hit in `estimate-clean-branch-ships-neutral-texts` is its Result, the record of the last reading. A Grep `gitignore` over `.guppi/` (with `.venv/` left out) printed `.guppi/tests/test_guppi_package.py`, `.guppi/tests/test_shellwrite.py`, `.guppi/tests/test_ship.py`, `.guppi/guppi/archive.py`, `.guppi/guppi/event.py`, `.guppi/guppi/ship.py` and `.guppi/guppi/sprint_close.py`. No test reads the root `.gitignore` of the working tree: `test_guppi_package.py` reads `.guppi/.gitignore`, `test_shellwrite.py` writes one under a temporary folder, and `test_ship.py` writes `.guppi/.gitignore` into its made-up tree. The docstrings of `archive.py`, `event.py` and `sprint_close.py` say the logs are gitignored, which stays true. `test_it_writes_the_code_the_harness_and_the_core_pages_only` of `test_ship.py` asserts the exact set of files the copy writes, so 893.1 adds the new file to its made-up tree and to that set. `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` builds this repository and keeps only the lines on `vault/wiki/estimates/`, so a line on `vault/.gitignore` would not fail it, and the new file holds no pointer. `check` of `ship.py` skips each file under `vault/`, so `guppi ship --check` does not judge `vault/.gitignore`; the build judges it in `settled`. The Criterion of `estimate-clean-branch-writes-a-clean-copy` lists every file the copy writes, so 893.1 replaces it whole, by the person's choice, with `vault/.gitignore` added and every other line kept word for word; the first `Then` line is the one line not carried word for word, since it is the line that gains the new file. Its `purpose` names the parts the copy writes, so it is set anew, and its `method` runs the tests of `ship` and stands. Changing `rule-clean-branch` takes up its put-off by `decision-case-882.3`, which names the `.gitignore` texts together with other Criteria of shipped Estimates. 893.1 carries `{supersedes:case 882.3}` and puts the rule off again with the rest of that list as 882.3 names it, without the `.gitignore` texts, which this Case makes true. `rule-clean-branch` is `draft` and carries no `core: true`, so its new text ships nowhere and the rule of brackets for core pages does not bind it. 893.2 takes up the put-off of Case 891 on `estimate-clean-branch-ships-neutral-texts` by an `update` that sets its `method` alone, so its Criterion and its `failed` status stand until the reading. Case 891 also put off `estimate-spec-write-writes-a-defer`, which this Case does not name; by `clear_deferred_by` of `.guppi/guppi/generate.py` that page keeps `decision-case-891` in its `deferred_by` and stays in the backlog. The person first chose to read the Estimate at the Retro of this session. Its `method` waits for the librarian's run of the session of Case 856.1 and for a tag `prod-x.y.z` in the history of HEAD. Both are past: the brief reports, under Readings due, that `git tag --merged HEAD --list 'prod-*'` prints `prod-0.2.0`, `prod-1`, `prod-2`, and that no step of its run ran `guppi ship`. At `/pre-spec` the finding was that Case 894 of this session changes the texts of the shipped rules `rule-spec-reconcile`, `rule-permissions` and `rule-case-build`, and those land only at the librarian's run, after Retro. So a reading at Retro would read their old texts. The person agreed that the `method` of the Estimate waits for the librarian's run of session 1907, so the reading is taken at the `/hi` of the next session, over a copy that holds the texts of Case 894. 893.2 sets that `method` anew, a part alone, so the Estimate keeps its Criterion and its `failed` status until that reading. The file of Case 894, read whole after its build ended, changes no page of this Case. Its sub-cases set `estimate-spec-reconcile-refuses-an-edit-of-the-plan`, `estimate-permissions` and `estimate-case-build-writes-the-case` `pending`, so the copy of that reading leaves those Estimates out until they pass. The new Criterion of `estimate-permissions` still names the folder `c--PROJECTS-GUPPI`, so that Estimate stays on the list of the put-off that 893.1 writes on `rule-clean-branch`. Case 892 of this session replaces the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets`, another Estimate of `rule-clean-branch`, on what `guppi ship --check` prints outside `vault/`; this Case changes neither that Estimate nor what `--check` judges.

> **problem:**
> The clean copy says that the event log is gitignored but ships no file that ignores it, so in a new project those sentences are false and the logs go into git. The Estimate of neutral texts stays failed and put off, and no reading shows whether its promise now holds.

> **recommend:**
> - **How do the event logs stay out of git in an installed project?**
>   - Recommended: (a) the copy ships `vault/.gitignore`.
>   - Answer: agreed, (a).
> - **Is the Estimate read again in this session?**
>   - Recommended: (a) read at the Retro of this session.
>   - Answer: agreed, (a).
> - **How is it checked that the copy writes `vault/.gitignore`?**
>   - Recommended: (a) add the file to the list of `estimate-clean-branch-writes-a-clean-copy`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, read the Estimate of neutral texts after the librarian's run of session 1907, at the `/hi` of the next session, so that the copy holds the new texts of Case 894.
>   - Taken: 893.2 sets the `method` of `estimate-clean-branch-ships-neutral-texts` to wait for that run, and the reading at Retro is gone.

### Case 893.1 — The copy writes `vault/.gitignore` for the event logs

> **given:**
> `.gitignore`: the root file of this repository, which loses its two lines on the event logs.
> **＋** `vault/.gitignore`: the new file with the two lines on the event logs.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, which takes the new file into the copy.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `rule-clean-branch`: its Purpose names the new file; it is put off again.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `estimate-clean-branch-ships-the-tests`, `estimate-clean-branch-ships-no-ship-command`, `estimate-clean-branch-ships-the-passed-estimates`, `estimate-clean-branch-ships-the-checks-workflow` and `estimate-clean-branch-writes-the-session-files`: the Estimates the Criterion points to.
> **＋** `.claude/`, `.github/` and `.guppi/uv.lock`: parts of the project the copy writes or leaves.
> **＋** `vault/wiki/`, `vault/wiki/tags.md`, `vault/raw/` and `vault/archive/`: the folders and the file of the vault the Criterion names.
> **＋** `vault/wiki/case-example.md` and `rule-case-example`: the example Case whose fenced blocks the copy sets aside.
> **＋** `decision-case-N`: the form of the id of a Decision page, a pointer.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --review <folder>` does the same.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `.guppi/` — what it writes of its tests, its Python environment and the module of the command `ship` is what `estimate-clean-branch-ships-the-tests` and `estimate-clean-branch-ships-no-ship-command` set — then `.claude/`, `CLAUDE.md`, `.gitattributes`, `vault/.gitignore`, whose lines keep each `event_log.md` under `vault/raw/` and `vault/archive/` out of git, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link, but in a string of a test file, as `estimate-clean-branch-ships-the-tests` sets it; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — the code under `.guppi/`, `.claude/` and the files at the root of the project — but `.guppi/uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true` but the Estimates that `estimate-clean-branch-ships-the-passed-estimates` sets, nothing of `vault/raw/` or `vault/archive/`, and no `guppi.toml`; what it writes of `.github/` and in place of the session files is what `estimate-clean-branch-ships-the-checks-workflow` and `estimate-clean-branch-writes-the-session-files` set.
> **－** It writes no cache folder of Python, pytest or ruff, and `--check` does not judge one.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed; in `vault/wiki/case-example.md` and the Render of `rule-case-example` only the fenced blocks, the example Case among them, are set aside so, and the text around them is judged and cleaned like the text of any other page.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

> **tasks:**
> - [ ] `vault/.gitignore`: a new file of three lines, `# The daily event logs that the hooks write: debugging material, kept out of git.`, `raw/*/event_log.md` and `archive/*/*/event_log.md`.
> - [ ] `.gitignore`: the comment on the event logs and its two lines `vault/raw/*/event_log.md` and `vault/archive/*/*/event_log.md` are removed; no other line changes.
> - [ ] `.guppi/guppi/ship.py`: `plan` takes `vault/.gitignore` into the copy when it stands in the working tree, and the module docstring names it among the files the copy writes.
> - [ ] `.guppi/tests/test_ship.py`: `tree` writes `vault/.gitignore` with the two lines, `test_it_writes_the_code_the_harness_and_the_core_pages_only` expects it in the set of written files, and a new test asserts that the copy holds it with the same text.
> - [ ] update `rule-clean-branch`
>   - old: `` `.claude/`, `CLAUDE.md`, `.gitattributes`, the `schema.yaml` of each category, ``
>   - new: `` `.claude/`, `CLAUDE.md`, `.gitattributes`, `vault/.gitignore`, whose lines keep the daily event logs under `vault/raw/` and `vault/archive/` out of git, the `schema.yaml` of each category, ``
>   - change: `the clean version writes vault/.gitignore, which keeps the event logs out of git`
> - [ ] defer `rule-clean-branch`
>   - type: `rule`
>   - purpose: `The rest of the rewrite of the sentences inside the Criterion of shipped Estimates that hold only in the repository of GUPPI: estimate-compact-recall-reloads (an example session folder of the repository of GUPPI), estimate-orchestration-forwards-a-discussion-question (the answer translated into Russian), estimate-synthesis-keeps-actioned-by-the-mark (a case number with no word case before it), estimate-synthesis-clusters (a pointer to estimate-documentation-completes, which does not ship), estimate-permissions (the folder c--PROJECTS-GUPPI) and estimate-ask-query-before-a-create (Russian and English), whose new readings wait for a later moment, so that a Criterion replaced now would set each pending and its rule draft until that moment; estimate-case-check-sends-back-a-faulty-case, whose sentence goes when a Case removes the old path of the check from .guppi/guppi/casecheck.py; and the pointers in estimate-case-build-checks-the-finished-case, estimate-case-build-reads-by-need-and-in-parts, estimate-case-protocol-case-form, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-signs-a-batch-together and estimate-sprint-close-next-session-opens-the-sprint, which hold once the pending Estimate each names passes and ships; put off again in session 1907, once the clean version keeps the event logs out of git by vault/.gitignore`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship writes the code under .guppi/ without its cache folders, the harness, vault/.gitignore for the event logs and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes"
>     ```
>   - change: `the Criterion replaced whole — the copy writes vault/.gitignore, which keeps the event logs out of git`
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 893.1][update][rule-clean-branch]{ref:rule-clean-branch}{supersedes:case 882.3}
> - decision[case 893.1][defer][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 893.1][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> ```

### Case 893.2 — The neutral texts of the copy are read again

> **given:**
> `estimate-clean-branch-ships-neutral-texts`: its put-off is taken up and its `method` set anew; its Criterion stands.
> **＋** `rule-clean-branch`: the rule of the clean version.
> **＋** `entity-guppi`, `rule-language` and `rule-case-build`: the pages the Criterion names.
> **＋** `CLAUDE.md`: the root file the Criterion names.
> **＋** `rule-guppi-config`, `rule-permissions` and `rule-morph`: the pages whose values the Criterion leaves out.

> **when:**
> Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

> **then:**
> `entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
> **＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
> **＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that names a past session of it, a line of its sprint page, its machine or a file that the clean version does not hold.
> **＋** No sentence of the `purpose` or the `method` of a shipped Estimate holds only in the repository of GUPPI, such as a `method` that waits for a moment of a past session of it.
> **＋** The reader lists, in the estimate line, each sentence of the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
> **－** A sentence of the `## Criterion` of a shipped Estimate on that list does not fail this promise.
> **－** The History of a page, a sample in a code span or a fenced block, the values of the Render of `rule-guppi-config` and the read rules of the Render of `rule-permissions`, which the setup Case of `rule-morph` sets, are no part of this promise.

> **tasks:**
> - [ ] update `estimate-clean-branch-ships-neutral-texts`
>   - set:
>     ```
>     method: "by hand, after the librarian's run of session 1907, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line"
>     ```
>   - change: `put-off taken up — the clean version keeps the event logs out of git by vault/.gitignore; the method waits for the librarian's run of session 1907`

> **ratification:**
> ```
> - decision[case 893.2][update][estimate-clean-branch-ships-neutral-texts]{ref:rule-clean-branch}{supersedes:case 891}
> ```
