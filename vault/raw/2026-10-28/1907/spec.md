<!-- approved 22:23:18 · session 20e2347c -->

# Session 1907 — the sprint plugin: a case reference in the tests of the case check

## Case 892 — The tests hold no reference to a case outside a bracket

> **context:**
> `guppi ship --check` reads each file that the clean copy takes outside `vault/`. In a test file under `.guppi/tests/` it reads only the comments and the docstrings, and it flags any reference to a case that does not stand in a bracket of its own. `check`, `judged` and `leftovers` of `.guppi/guppi/ship.py` decide this, together with `outside` and `masked_strings` of `.guppi/guppi/pointers.py`. `masked_strings` puts aside every string that is not a docstring, but it does not put aside a code span inside a docstring. The tests that Case 890 added hold `Case 5` in the docstring of `built_again_sibling` and in the comment on the first line of `test_subagent_session_clash_with_a_case_built_again_takes_its_stored_value`. The number names the made-up Case of the test data, not a decision. The brief of session 0118 reports the result under Flags as `Lint: ship — .guppi/tests/test_casecheck.py:2695 and :2740, a reference to a case: Case 5`, and under Readings at the close as `uv run --project .guppi guppi check: 14 lines (exit 1), as in Flags`. `rule-clean-branch` says that a Case rewords such text at its source. The person chose to drop the number and call that Case the sibling Case, so that no fake pointer stands in a bracket. Neither Estimate of `rule-clean-branch` promised that the live test files pass the check. The Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` names `.guppi/guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`. The Criterion of `estimate-clean-branch-ships-the-tests` promises how the check reads a test file, not that the test files pass it. The person chose to widen the first Estimate to `.guppi/tests/`. This Case replaces its Criterion and sets its `purpose` and `method` anew, since both state the old set of folders. Three lines of the old Criterion are not carried word for word, and each one is replaced by its widened form. The `when` names `ship.py` by its path. The first `then` line adds `.guppi/tests/`. The first `－` line speaks of any rewording, no longer only of the bare case numbers in `.guppi/guppi/`. The other paths of that Criterion stay as the person's answer left them. `Makefile` and the root `pyproject.toml` are not in `ROOT_FILES` or `TREES` of `ship.py`, so `--check` prints no line on them. A Grep of the repository outside `vault/archive/` and `vault/raw/` for `estimate-clean-branch-code-holds-pointers-only-in-brackets` printed `vault/wiki/log.md` and `vault/wiki/rules/rule-clean-branch.md`, and no file under `.guppi/tests/`, so no test reads that page live. The line of `rule-clean-branch` that hits is its `estimates` field and a History line, and neither one changes. The person chose to fix only the two lines and add no earlier guard to Work Mode.

> **problem:**
> A docstring and a comment of `.guppi/tests/test_casecheck.py` name test data as `Case 5`, outside a bracket. `guppi ship --check` flags them, and `guppi check` reports them. No Estimate promises that the test files pass this check.

> **recommend:**
> - **How are the two lines reworded?**
>   - Recommended: (a) name the Case without its number, as the sibling Case.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix?**
>   - Recommended: (a) widen the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` to cover `.guppi/tests/`.
>   - Answer: agreed, (a).
> - **Does this Case also stop a new test from bringing the defect back?**
>   - Recommended: (a) fix the two lines only.
>   - Answer: agreed, (a).

> **given:**
> `.guppi/tests/test_casecheck.py`: the tests whose docstring and comment name test data by a case number.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-clean-branch`: the rule that a pointer stands in a bracket of its own and that a Case rewords such text at its source.
> **＋** `.guppi/guppi/ship.py`: the check `guppi ship --check`.
> **＋** `.claude/`: the harness, whose lines of `--check` stay out of this promise.
> **＋** `CLAUDE.md`: the root file whose lines of `--check` stay out of this promise.
> **＋** `rule-retro`: the rule that makes a red of `guppi check` a note for the handoff.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges the working tree, and `uv run --project .guppi guppi ship --review <folder>` builds the clean version into an empty folder.

> **then:**
> `uv run --project .guppi guppi ship --check` prints no line on a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
> **－** The rewording changes no line but a comment or a docstring, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
> **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

```then
update:
- slug: estimate-clean-branch-code-holds-pointers-only-in-brackets
  set:
    status: pending
    purpose: Whether the code, the tests and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
    method: 'by hand, at Retro: the lines of uv run --project .guppi guppi ship --check over the working tree, and of uv run --project .guppi guppi ship --review into an empty temporary folder, on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion'
  change: the Criterion replaced whole — the tests under .guppi/tests/ hold pointers only in brackets too
```

```tasks
- [x] `.guppi/tests/test_casecheck.py`: the docstring of `built_again_sibling` opens with `The sibling Case stands in the plan as ratified`, and the comment after `plan_with(working, PLANNED_5)` reads `the plan's sibling Case sets status built`, in a code span as it stands; no other line changes.
- [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
- [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`
```

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

```then
update:
- slug: rule-clean-branch
  replace:
  - old: '`.claude/`, `CLAUDE.md`, `.gitattributes`, the `schema.yaml` of each category,'
    new: '`.claude/`, `CLAUDE.md`, `.gitattributes`, `vault/.gitignore`, whose lines keep the daily event logs under `vault/raw/` and `vault/archive/` out of git, the `schema.yaml` of each category,'
  change: the clean version writes vault/.gitignore, which keeps the event logs out of git
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
    purpose: 'Whether guppi ship writes the code under .guppi/ without its cache folders, the harness, vault/.gitignore for the event logs and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes'
  change: the Criterion replaced whole — the copy writes vault/.gitignore, which keeps the event logs out of git
defer:
- slug: rule-clean-branch
  type: rule
  purpose: 'The rest of the rewrite of the sentences inside the Criterion of shipped Estimates that hold only in the repository of GUPPI: estimate-compact-recall-reloads (an example session folder of the repository of GUPPI), estimate-orchestration-forwards-a-discussion-question (the answer translated into Russian), estimate-synthesis-keeps-actioned-by-the-mark (a case number with no word case before it), estimate-synthesis-clusters (a pointer to estimate-documentation-completes, which does not ship), estimate-permissions (the folder c--PROJECTS-GUPPI) and estimate-ask-query-before-a-create (Russian and English), whose new readings wait for a later moment, so that a Criterion replaced now would set each pending and its rule draft until that moment; estimate-case-check-sends-back-a-faulty-case, whose sentence goes when a Case removes the old path of the check from .guppi/guppi/casecheck.py; and the pointers in estimate-case-build-checks-the-finished-case, estimate-case-build-reads-by-need-and-in-parts, estimate-case-protocol-case-form, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-signs-a-batch-together and estimate-sprint-close-next-session-opens-the-sprint, which hold once the pending Estimate each names passes and ships; put off again in session 1907, once the clean version keeps the event logs out of git by vault/.gitignore'
```

```tasks
- [x] `vault/.gitignore`: a new file of three lines, `# The daily event logs that the hooks write: debugging material, kept out of git.`, `raw/*/event_log.md` and `archive/*/*/event_log.md`.
- [x] `.gitignore`: the comment on the event logs and its two lines `vault/raw/*/event_log.md` and `vault/archive/*/*/event_log.md` are removed; no other line changes.
- [x] `.guppi/guppi/ship.py`: `plan` takes `vault/.gitignore` into the copy when it stands in the working tree, and the module docstring names it among the files the copy writes.
- [x] `.guppi/tests/test_ship.py`: `tree` writes `vault/.gitignore` with the two lines, `test_it_writes_the_code_the_harness_and_the_core_pages_only` expects it in the set of written files, and a new test asserts that the copy holds it with the same text.
- [ ] update `rule-clean-branch`
- [ ] defer `rule-clean-branch`
- [ ] update `estimate-clean-branch-writes-a-clean-copy`
- [ ] read `estimate-clean-branch-writes-a-clean-copy`
```

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

```then
update:
- slug: estimate-clean-branch-ships-neutral-texts
  set:
    method: 'by hand, after the librarian''s run of session 1907, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line'
  change: put-off taken up — the clean version keeps the event logs out of git by vault/.gitignore; the method waits for the librarian's run of session 1907
```

```tasks
- [ ] update `estimate-clean-branch-ships-neutral-texts`
```

## Case 894 — The guard writes the file of case-guppi, so no permission prompt comes

> **context:**
> `case-guppi` writes the file of its Case by `Write` and fixes it by `Edit`. Its agent file sets `permissionMode: auto`, and `rule-permissions` keeps every path under `cases/` off the allow list on the claim that Claude Code keeps that mode for a subagent while the session is in Plan Mode (case 698). That claim no longer holds, so in this session each write of a Case file asked the person for permission. The section "Permission modes" of https://code.claude.com/docs/en/sub-agents says that when the main conversation is in `plan` mode the subagent stays in plan mode whichever `permissionMode` is set, and that in `bypassPermissions`, `acceptEdits` or auto mode the subagent takes that mode and the value set is ignored; the value applies only when the main conversation is in `default` or `dontAsk`. An allow rule does not help either: the person said that the main agent's write of `frontier.md`, which the allow list names, asked in this session too, and https://code.claude.com/docs/en/permission-modes says only that edits stay blocked until the plan is approved. The section "Hook approvals in plan mode" of https://code.claude.com/docs/en/permissions says that an `"allow"` of a `PreToolUse` hook has no effect on a file edit in plan mode, and its section on precedence says that a hook that exits with code 2 stops the tool call before permission rules are evaluated. A hook runs as a process of its own and writes with no tool call, as the hooks of `rule-spec-write` and `rule-case-check` already write the plan and the store. So the guard of `rule-spec-reconcile`, which already reads each `Edit`, `Write` and `MultiEdit` of `case-guppi` on its case file, makes the write itself and stops the call with exit 2, and no prompt comes. Option (c) of the round, a session started with `--allow-dangerously-skip-permissions`, breaks the Purpose of `rule-default-mode`, which keeps a session from writing anything before a Case is ratified, and the same page of permission modes says that the VS Code chat panel keeps the blocks of plan mode with that flag; the person did not take it.
> In `.guppi/guppi/ratified.py` the guard reads a call by `guard_refusal`, which lets a call of `case-guppi` on a file under `cases/` through and refuses any other agent there, and next by `held_number`, which refuses a number another `agent_id` holds in the store, writes the entry of a first call, and on its own error prints one line and lets the call run; `guard` exits 2 on a refusal after one event-log line `ratified refused`. `written_case_files` of `.guppi/guppi/casecheck.py` takes each case file that a `Write`, `Edit` or `MultiEdit` tool use of the subagent names, whatever the result of the call, so the `SubagentStop` check still finds a file the hook wrote from a stopped call, and `subagent` keeps the files that stand; it needs no change. A Grep for `old_string|replace_all` over `.guppi/guppi/` printed nothing, so no code applies an `Edit` today, and the new code is no second copy of a judgment.
> A Grep for `permissionMode` over `vault/wiki/` and `.claude/` printed `vault/wiki/rules/rule-case-build.md`, `vault/wiki/rules/rule-permissions.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/estimates/estimate-permissions.md`, `vault/wiki/estimates/estimate-case-protocol-case-form.md`, `vault/wiki/log.md` and `.claude/agents/case-guppi.md`. Case 894.2 changes the two sentences of `rule-permissions` that rest on the mode, and Case 894.3 the clause of `rule-case-build` and the line of its Estimate; the History lines of these pages and `log.md` are not read; the hit in `estimate-case-protocol-case-form` is a reading in its Result and stands; `permissionMode: auto` stays in the agent file, by the person's answer. The Purpose of `rule-spec-reconcile` stands: a hook still refuses any edit of a case file unless `case-guppi` makes it. The sentences of `rule-case-build` and `estimate-case-build-writes-the-case` that say `case-guppi` writes its file by `Write` stand, since it still calls `Write`, and the guard carries the call out. The Criterion of `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` stands: the number check is unchanged and runs before the write, and on its own error it still lets the call run; its tests under `-k number_held` that expect a passing call to exit 0 change under Case 894.1. A Grep for `case-guppi\.md|rule-case-build|rule-spec-reconcile\.md|rule-permissions` over `.guppi/tests/` printed one docstring line of `.guppi/tests/test_guppi_package.py`, so no test reads the live files this Case renders. The Render of `rule-permissions` does not change, so `.claude/settings.json` stays as it is. The Criterion of `estimate-spec-write-exits-2-on-an-error` stands: its line that the guard keeps exit 0 with its line on stderr on its own error still holds, since an error of the number check or of the write lets the call run with exit 0 and one line; its `method`, all of `.guppi/tests/test_ratified.py`, runs the tests that Case 894.1 changes. Whether Claude Code knows the file as read after a call the guard stopped is not settled: the section "Edit tool behavior" of https://code.claude.com/docs/en/tools-reference says that an `Edit` needs a read of the file in the conversation, that a newer model may edit an unread file when reading it would not ask, and that a file changed on disk since the last read can still be edited when `old_string` matches its current text; it does not say whether these checks run before the `PreToolUse` hooks. So `case-guppi` reads its file by `Read` after a write of the guard and before its next `Edit`, which asks nothing inside the project. That read is in Case 894.3. Whether the client asks at the write is the promise of `estimate-permissions` alone (Case 894.2); the Criterion of Case 894.1 does not repeat it, since its `method` cannot see a prompt.

> **problem:**
> In Plan Mode Claude Code asks the person before each write of `case-guppi` to its Case file, though the person ratifies each Case anyway. The setting the harness relied on, `permissionMode: auto`, is ignored in plan mode, and the allow list does not stop the prompt there.

> **recommend:**
> - **How does the write of a Case file stop asking?**
>   - Recommended: no option recommended, since the documentation does not settle whether an allow rule works in plan mode; (a), case files on the allow list, if the write of `frontier.md` did not ask.
>   - Answer: the write of `frontier.md` asked for permission in this session; what to do then, and how to keep `case-guppi` from asking. Replaced by the question who writes the Case file.
> - **What happens to the `permissionMode: auto` line of the helper?**
>   - Recommended: (a) keep the line, and fix what the pages claim for it.
>   - Answer: agreed, (a).
> - **What does the check of `rule-permissions` promise for reads outside the project?**
>   - Recommended: (a) drop that promise.
>   - Answer: agreed, (a).
> - **Who writes the Case file, so that no question comes?**
>   - Recommended: (a) the guard hook writes the file and stops the call.
>   - Answer: agreed, (a); let us try it this way.
> - **How is the hook's write checked?**
>   - Recommended: (a) rewrite the guard's check, and keep the "no question" promise in the check of `rule-permissions`, read after the first Case file written in plan mode of a later session.
>   - Answer: agreed, (a).
> - **What happens when the hook cannot make the write?**
>   - Recommended: (a) an Edit that cannot apply is stopped with its reason; an error of the hook lets the call run.
>   - Answer: agreed, (a).
> - **One Case, or one part per page?**
>   - Recommended: (a) three parts under one Case.
>   - Answer: agreed, (a).

### Case 894.1 — The guard writes the file of case-guppi and stops the call

> **given:**
> `.guppi/guppi/ratified.py`: the guard of the plan and of the case files, by `guard`, `guard_refusal` and `held_number`.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the guard.
> **＋** `rule-spec-reconcile`: the rule of the guard.
> **＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: its Criterion is replaced whole.
> **＋** `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: the number check, which runs before the write.
> **＋** `.guppi/guppi/casecheck.py`: `is_case_file`, the judgment of a case file.
> **＋** `.guppi/guppi/ledger.py`: `is_plan_file`, which judges a plan file under `.claude/plans/`, and `plan_path`.
> **＋** `vault/raw/<date>/<HHMM>/`: a session folder, whose `cases/` folder holds the case files.

> **when:**
> An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run --project .guppi guppi ratified --guard` on `PreToolUse` reads the path, the content, the agent type and the `agent_id` of the call from the hook input.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way, and so is one of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, when the hook input does not name `case-guppi` as the agent type; the reason names the file and says that `case-guppi` alone writes it.
> **＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
> **＋** A call whose hook input names `case-guppi` on a file under such a folder, which `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` neither refuses nor lets run on an error of the guard, is written by the hook itself: the content of a `Write`, or each `old_string` of an `Edit` or a `MultiEdit` replaced by its `new_string`, in order, once, or at each match with `replace_all`.
> **＋** After that write the hook exits 2 with one line on stderr that names the file, says that the hook wrote it and tells the agent not to make the call again, so the call does not run.
> **＋** A file under that folder is judged by `is_case_file` of `.guppi/guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `.guppi/guppi/ledger.py`, which `plan_path` uses too.
> **＋** A refusal writes one line `ratified refused` to the day's event log, the write of the hook one line `ratified wrote`, and neither writes a `tool` line, so `plan_path` of `.guppi/guppi/ledger.py` still names the plan file.
> **－** An `Edit` or `MultiEdit` of `case-guppi` whose old string is missing from the file, is found more than once without `replace_all`, or names a file that does not exist leaves the file as it stands: exit 2 with that reason, and nothing of a `MultiEdit` is written.
> **－** An error of the hook while it writes the file of `case-guppi` lets the call run: exit 0 with one line on stderr.
> **－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan.

```then
update:
- slug: rule-spec-reconcile
  replace:
  - old: and so does this hook for the entry that holds a number,
    new: and so does this hook for the entry that holds a number and for the file of `case-guppi`,
  - old: so no hook can create it. A refusal writes one line to the day's event log;
    new: 'so no hook can create it. On the first of these exceptions the hook makes the write itself, since Claude Code keeps a subagent in plan mode in Plan Mode whatever its `permissionMode` and asks the person before its edit: it writes the content of a `Write`, or replaces each `old_string` of an `Edit` or a `MultiEdit` by its `new_string` in order, once or at each match with `replace_all`, writes one line `ratified wrote` to the day''s event log, and exits 2 with one line that says the file is written and the call is not to be made again, so the call does not run and Claude Code asks nothing (as set in case 894.1). An old string missing from the file, found more than once without `replace_all`, or a file that does not exist leaves the file as it stands and is refused with that reason; an error of the hook while it writes lets the call run, and Claude Code may ask the person that one time (as set in case 894.1). A refusal writes one line to the day''s event log;'
  change: the guard writes the file of case-guppi itself and stops the call, so no permission prompt comes in Plan Mode (case 894.1)
- slug: estimate-spec-reconcile-refuses-an-edit-of-the-plan
  set:
    status: pending
    purpose: An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/; an edit of case-guppi under cases/ is written by the hook itself and the call stopped
    method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k guard; by hand at the Work readings of the session that changes the guard, one probe Write of the main agent under cases/, refused and in the event log
  change: the Criterion replaced whole — the guard writes the file of case-guppi itself and stops the call; the purpose and the method follow (case 894.1)
```

```tasks
- [ ] update `rule-spec-reconcile`
- [ ] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- [x] `.guppi/guppi/ratified.py`: after `guard_refusal` and `held_number` let a call of `case-guppi` on a case file through, `guard` writes the content of a `Write`, or applies the `old_string`, `new_string` and `replace_all` of an `Edit` and of each edit of a `MultiEdit` in order on the text read and written as UTF-8 with no change of line ends, writes one event-log line `ratified wrote <tool> <path>` and exits 2 with one stderr line that names the file, says that the hook wrote it and tells the agent not to make the call again; an old string missing, found more than once without `replace_all`, or a file that does not exist is refused with that reason and writes nothing; `held_number` tells its own error apart, so that on that error and on an error of the write the call runs with exit 0 and one stderr line; the module docstring says so.
- [x] `.guppi/tests/test_ratified.py`: the tests of the guard and of `-k number_held` that expect a call of `case-guppi` on a case file to exit 0 expect the hook's write and exit 2 instead, and their `Edit` calls carry an `old_string`; new tests cover a `Write` written whole, an `Edit` once and with `replace_all`, a `MultiEdit` in order, a missing old string, an old string found twice and a missing file each refused with the file unchanged, an error of the write and an error of the number check each letting the call run with exit 0, and the `ratified wrote` line with no `tool` line.
- [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
```

### Case 894.2 — The allow list says why case files stay off it

> **given:**
> `rule-permissions`: the allow list and the reason for each path on it or off it.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered allow list, unchanged.
> **＋** `.guppi/tests/test_render.py`: the JSON case that fixes the shape of the block.
> **＋** `rule-spec-reconcile`: the guard that writes the file of `case-guppi`.
> **＋** `vault/raw/**`: the session folders, whose working files the list names and whose `cases/` folders stay off it.
> **＋** `vault/wiki/brief.md`: the one file of `vault/wiki/` on the list.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI`: the folder of saved transcripts, which `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)` name.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `.guppi/tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only: the reading line records it from the person, never from the agent, whose reply does not tell an approved call from one not asked.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, since the guard of `rule-spec-reconcile` makes the write and stops its call.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** An error of the guard of `rule-spec-reconcile` while it writes that file lets the call run, and the client may ask the person that one time; that prompt is not a finding and not a `failed`.
> **－** A Read, Grep or Glob of `case-guppi` on a path outside the project that no rule of the allow list names is not bound by this Criterion: it may ask the person.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

```then
update:
- slug: rule-permissions
  replace:
  - old: 'The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: auto` of its agent file (case 698), which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16).'
    new: 'The file of a built Case under `cases/` is not on the list: in Plan Mode Claude Code keeps a subagent in plan mode whatever its `permissionMode` and asks before its edit, allow list or not, so the guard of `rule-spec-reconcile` writes the file of `case-guppi` itself, stops its call so that nothing is asked unless the guard fails to write, and keeps it inside `cases/` (as set in case 894.2).'
  - old: 'A call of `case-guppi` that these rules do not match is judged by its mode `permissionMode: auto`, with no prompt to the person, and a call they match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (case 698).'
    new: 'A call of `case-guppi` that these rules do not match is judged by the mode of the session, and by its own `permissionMode: auto` only while the session runs in `default` or `dontAsk` mode, so a read outside the project that no rule names may ask the person, in Plan Mode too; a call the rules match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (as set in case 894.2).'
  change: case-guppi stays in plan mode in Plan Mode whatever its permissionMode; the guard of rule-spec-reconcile writes its Case file, and a read outside the project that no rule names may ask (case 894.2)
- slug: estimate-permissions
  set:
    status: pending
    method: 'the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of .guppi/tests/test_render.py; by hand, after the first Case file that case-guppi writes in Plan Mode of a session after the Work Mode that changes the guard of rule-spec-reconcile: the person''s word on whether the client asked at that write, and at a Grep of a subagent whose path is the folder of the project''s saved transcripts itself and at one whose path is a file under it, recorded in the estimate line, never the agent''s, which cannot see the prompt'
  change: the Criterion replaced whole — case-guppi writes its Case file with no prompt in Plan Mode by the guard of rule-spec-reconcile, and a read outside the project that no rule names is not bound; the method follows (case 894.2)
```

```tasks
- [ ] update `rule-permissions`
- [ ] update `estimate-permissions`
- [ ] read `estimate-permissions`
```

### Case 894.3 — case-guppi takes the guard's line as the write done

> **given:**
> `rule-case-build`: the Render of the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-spec-reconcile`: the guard that writes the file of `case-guppi`.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of its case file.

> **when:**
> `case-guppi` calls `Write` or `Edit` on the file of its Case under `raw/<date>/<hi HHMM>/cases/`, as the text of `.claude/agents/case-guppi.md` sets it.

> **then:**
> It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
> **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.

```then
update:
- slug: rule-case-build
  replace:
  - old: the file of your Case is the one file this harness lets you write, in the permission mode your agent file sets, and its guard refuses any other.
    new: 'the file of your Case is the one file this harness lets you write: its guard writes the text of your `Write` or `Edit` into it itself and stops your call with a line that says the file is written, which is no failure and no call to make again, and you read the file by `Read` before your next `Edit` of it; the guard refuses any other file (as set in case 894.3).'
  change: the guard writes the Case file for case-guppi and stops the call; case-guppi takes that line as the write done (case 894.3)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
      **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
      **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
      **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

      Then:
      `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
      **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
      **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
      **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
      **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
      **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
      **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
      **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
      **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
      **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
      **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change under the number of that Case; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
      **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it writes no new file and answers with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it.
      **＋** Where the person chooses a new Case beside it, it builds that behaviour as a new top-level Case in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
      **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
      **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
      **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
      **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
      **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
      **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
      **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.
      **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
      **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
      **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
      **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
      **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
      **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
  change: the Criterion replaced whole — permissionMode auto applies only in default or dontAsk mode; in Plan Mode the guard writes the Case file, and case-guppi takes its line as the write done and reads the file before its next Edit (case 894.3)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`
```

## Case 895 — A test shows whether a helper goes on after a compaction

> **context:**
> Each answer to a round, each change and each finding goes back to the same `case-guppi` by `SendMessage`, and the helper keeps all it has read and said, so its context only grows (`lesson-case-build-agent-context-grows-on-every-resume`, which put the helper of Case 819 at 701016 tokens). In this session the task notifications of the main transcript `~/.claude/projects/c--PROJECTS-GUPPI/20e2347c-c292-4d8a-bd74-e0eb896ad1c1.jsonl` give `subagent_tokens` 87839, 101506 and 139934 for the helper of Case 893, and 82569, 104531, 142770, 184241 and 184584 for the helper of Case 894. The put-off of this growth stands on `rule-orchestration` by Case 884, carried over from Case 876.
> The person chose a procedure for a later session: a hook sees that a helper is past 400 000 tokens and has it write an interim Case with what is still to do; a compaction then comes by size, and the same helper reads its file again and goes on. The person chose to test the idea first and to build it only if it works, so this Case adds one check and one Work task, and the put-off on `rule-orchestration` stays as it stands for the Case that builds the procedure. The test writes only in a folder under the temporary area of the session, outside the repository, so nothing in the vault or the code changes by it and the one rule of `ratification.md` is kept; `rule-work-mode` runs only the approved Spec, so the test needs this Case to stand in it.
> The test rests on behaviour of Claude Code read in its documentation. https://code.claude.com/docs/en/sub-agents says that subagents compact automatically as their own context fills, that `autoCompactWindow` in the frontmatter of one subagent sets its window from 100000 to 1000000 tokens and needs v2.1.296 or later, that a size set by `CLAUDE_CODE_AUTO_COMPACT_WINDOW` in the shell overrides the field, and that a subagent can be resumed after a restart by resuming the same session; the transcript of the helper of Case 894 records version 2.1.310. The same page says that `/compact` acts on the main conversation, and https://code.claude.com/docs/en/hooks gives `PreCompact` a block and no way to add instructions to an automatic compaction, whose `custom_instructions` is null, and gives `PostCompact` no decision control, so nothing but the size starts a compaction or shapes its summary. https://code.claude.com/docs/en/context-window says that after a compaction the system prompt still applies, skill bodies come back up to 5 000 tokens each, and Claude Code reads again up to five recent files, a file over 5 000 tokens coming back as a path only. https://code.claude.com/docs/en/headless says that `claude -p` loads the hooks and subagents of its working folder unless `--bare` is set, waits for background subagents before it exits, and continues a conversation with `--resume` and a session id. https://code.claude.com/docs/en/model-config says that `opus` resolves to Opus 5.5 and that a model with a native 1M window compacts at about 967K tokens, so a helper today compacts only near that size.
> No page of the documentation that was read says whether the transcript file of a subagent keeps its earlier lines after a compaction, or whether `SubagentStop` and `PostCompact` hooks run for a subagent after one; the checks of `rule-case-check` read the earlier rounds and reads of a helper from that file. A Grep for `"subtype":"compact_boundary"` over `~/.claude/projects/c--PROJECTS-GUPPI` with the glob `*.jsonl` printed one file, the main transcript `682b0e2f-5e90-435e-be2e-7ba7f97d2ad4.jsonl`, with the record on its line 190, after the earlier lines; it printed no subagent transcript. The new Estimate checks these facts. A Glob `vault/**/estimate-case-build-goes-on-after-a-compaction.md` printed nothing, so the slug is free. No Estimate of `rule-case-build` speaks of a compaction, and this Case changes no text of the rule, so none of them is touched.

> **problem:**
> The procedure the person chose for a full helper rests on facts about how a subagent compacts that the documentation does not settle. Building it before those facts are seen would likely need a second Case.

> **recommend:**
> - **How do we stop the memory of the helper from growing?**
>   - Recommended: (a) a new helper rebuilds a built Case; not (b), compaction by size, since whether the checks keep their records is not checked.
>   - Answer: in the person's own words, `case-guppi` should watch its own context: a hook like the one of the main session warns past a size, and the question is what happens next.
> - **What happens once the hook finds a helper past the limit?**
>   - Recommended: (a) a new helper takes over the Case.
>   - Answer: the person disagreed with that procedure: the helper should work on, and when the hook says its context is full, a procedure saves its work and passes it on. Replaced by the question how a full helper hands its work to a fresh one.
> - **At what size is a helper past the limit?**
>   - Recommended: (a) 200 000 tokens.
>   - Answer: (b), 400 000 tokens, as in the main session.
> - **How does a full helper hand its work to a fresh one?**
>   - Recommended: (a) a handover file, then a fresh helper.
>   - Answer: the person proposed to combine the hook and the compaction: the helper writes an interim Case and what is left to do, a compaction follows, and the same helper goes on. Replaced by the question whether the hook and compaction work together on the same helper.
> - **Should the hook and compaction work together on the same helper?**
>   - Recommended: (a) the hook asks for an interim Case, then compaction comes by size.
>   - Answer: test the idea first, and build it if it works.
> - **Where do the test and the build go?**
>   - Recommended: (b) only the test now, the build in a later session.
>   - Answer: agreed, (b).
> - **How is the test run?**
>   - Recommended: (a) the main agent runs it in a test folder, with no window.
>   - Answer: agreed, (a).
> - **When does the test run?**
>   - Recommended: (a) in the Work Mode of this session.
>   - Answer: agreed, (a).
> - **What carries the test into Work Mode?**
>   - Recommended: (a) a small Case: one new check on `rule-case-build`, met by the test.
>   - Answer: agreed, (a).

> **given:**
> `estimate-case-build-goes-on-after-a-compaction`: the new check of a helper that compacts.
> **＋** `rule-case-build`: the rule of the helper, the target of the check.
> **＋** `lesson-case-build-agent-context-grows-on-every-resume`: the growth the later procedure answers.
> **＋** `rule-work-mode`: it runs only the approved Spec.
> **＋** `vault/wiki/ratification.md`: the one rule, kept since the test writes outside the repository.
> **＋** a test folder under the temporary area of the session: the agent file of a test helper, its hook and its text files.
> **＋** `~/.claude/projects/`: the transcripts of the test session and of its helper.

> **when:**
> The main agent runs `claude -p` in a test folder outside the repository, whose agent file of a test helper sets `autoCompactWindow: 100000` and tells it to read its interim file again after a compaction, and whose hooks log each `SubagentStop` and `PostCompact` event.
> **＋** The first run starts the test helper, has it read text files and write its interim file; a second run with `--resume` sends it more files, past 100000 tokens; a third run with `--resume` asks it to go on.

> **then:**
> The transcript of the test helper under `~/.claude/projects/` holds a `compact_boundary` record after it passes 100000 tokens.
> **＋** That transcript file keeps the lines of the helper before the `compact_boundary` record.
> **＋** The log of the test folder holds a `SubagentStop` line after the compaction.
> **＋** After the compaction the test helper reads its interim file again and goes on from what it says.
> **－** The size of 100000 tokens binds the test helper alone, through its agent file, and no size is set in the shell of `claude -p`.
> **－** No file of the repository changes by the test.

```then
create:
- slug: estimate-case-build-goes-on-after-a-compaction
  ref: rule-case-build
  kind: QA
  purpose: Whether a subagent with its own autoCompactWindow compacts past that size, keeps its earlier lines in its transcript file, still fires SubagentStop after the compaction, and reads its interim file again and goes on, as the later procedure for a full case-guppi needs
  method: 'by hand, in the Work Mode of the session that creates it: the test of the Criterion run by claude -p in a folder under the temporary area of the session, and the transcript of the test helper and the log of the folder read against the Criterion, recorded in the estimate line'
  tags:
  - harness
  - hooks
  - case-build
```

```tasks
- [ ] create `estimate-case-build-goes-on-after-a-compaction`
- [x] by hand in Work Mode: set up the test folder under the temporary area of the session (the agent file of the test helper with `autoCompactWindow: 100000`, a hook on `SubagentStop` and `PostCompact` that appends one line to a log, large text files), run `claude -p` there with `--permission-mode acceptEdits` and with `--resume` and the session id of the first run for the later runs, read the transcript of the test helper and the log, and record what the test found as a `knowledge` lesson line with the test as its source.
- [ ] read `estimate-case-build-goes-on-after-a-compaction`
```
