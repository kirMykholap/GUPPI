## Case 904 — The case check and the example test drop their fallbacks

> **context:**
> Two fallbacks were kept until a new way of work was live. The `SubagentStop` check of `rule-case-check` reads the files `case-<N>.md` that `case-guppi` wrote; when the record of the agent's calls names no such file and its newest output holds a Case heading, `subagent` of `.guppi/guppi/casecheck.py` checks that text by `answer_of`, stores it and writes the file itself by `write_case_files` (case 645.2). The test `.guppi/tests/test_case_schema.py` reads the example Case from `vault/wiki/case-example.md`, and from `vault/wiki/case-schema.md` when the first does not stand, in its function `example` (case 717.1). Both conditions are met: `estimate-case-build-writes-the-case` stands `passed` (2026-10-29), and `vault/wiki/case-example.md` stands. What goes wrong is the text the fallbacks left: the Criterion of `estimate-case-check-sends-back-a-faulty-case` and of `estimate-case-example-passes-the-check` each says that a Case of a later session removes the path, which is false in a project that installs GUPPI, and this session's reading of `estimate-clean-branch-ships-neutral-texts` listed both sentences as true only in the repository of GUPPI. The person chose to remove both paths (Q1 to Q5, all (a)). The rule of each choice: the frame of `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, says that a Case of a later session removes the old form once the reading of the writer passes, which a lasting fallback would break; the rules schema, `vault/wiki/rules/schema.yaml`, says that a Leaf that still carries `## How it works` keeps it until its next touch, when the section leaves, so the false clause of `rule-spec-reconcile` leaves with its whole section by hand, as case 589.2 did for `rule-case-check`; `vault/wiki/case-schema.md` asks an `update` of each Estimate whose Criterion speaks of the change, so the line of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` on the old path is reworded in Case 904.2. The code read: `subagent`, `answer_of`, `write_case_files`, `written_case_files`, `is_fact`, `shape_findings`, `against_store` and `stop` of `.guppi/guppi/casecheck.py`. Once the path is gone, a Case that `case-guppi` gives only in the text of its answer is not stored, and `against_store`, which `stop` runs on each Case the main agent shows, refuses it as not built and checked by `case-guppi`; after three refusals the showing passes and the Spec hook compares it at ratification, as the Purpose of `rule-case-check` sets it. `shape_findings` judges only a text that holds its top-level Case, whether the text comes from a file or an answer, and the parametrized shape test of `.guppi/tests/test_casecheck.py` already gives it a file of sub-case 9.1 alone, so the reworded line holds on the code as it stands. A Grep of `answer_of|write_case_files|old path|old way` over `.guppi/` printed `.guppi/guppi/casecheck.py`, `.guppi/tests/test_casecheck.py` and `.guppi/tests/test_ratified.py`; the hit in `test_ratified.py` is the name of a test of the Spec hook, `test_write_the_answer_of_case_guppi_not_the_showing`, which calls no `subagent` and stands. Most tests of `test_casecheck.py` give the check a Case as answer text through its helper `answer`, so Case 904.1 changes that helper to write the Case into its file first. A Grep of `old path|old way|writer is live` over `vault/wiki/` outside `decisions/` printed `log.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-case-check-sends-back-a-faulty-case.md`, `rules/rule-spec-reconcile.md`, `rules/rule-case-check.md`, `lessons/lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes.md`, `estimates/estimate-generate-rewords.md` and `estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape.md`, and over `.claude/` nothing; the hit of `rule-case-check` is a History line, the one of `estimate-clean-branch-ships-neutral-texts` is its Result, which reports the reading, the lesson speaks of another path, and the one of `estimate-generate-rewords` is the words "hold paths" of its `method`, so these stand; the rest enter this Case. The lines of `estimate-case-check-requires-each-question-of-the-rounds` and `estimate-case-check-notes-a-then-line-shared-by-siblings` on an answer of sub-cases alone stand, since a file can hold sub-cases alone. A Grep of `test_case_schema` over `vault/wiki/` outside `decisions/` printed `brief.md`, `log.md`, `estimates/estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read.md` and `estimates/estimate-case-example-passes-the-check.md`: no page names the test in a field of its code, so Case 904.3 adds it to `implementation_ref` of `rule-case-example`, which other render rules such as `rule-ratification` carry too. Of the tests that read a live file of `vault/`, `test_case_schema.py` reads `vault/wiki/case-example.md` and the schema files and runs `check_answer`, which this Case does not change; no test reads the pages this Case changes. The last run, under `## Readings at the close` of `vault/wiki/brief.md`: `uv run --project .guppi guppi test`: 1792 passed, 6 skipped, 1 deselected. Cases 902 and 903 of the session change none of these pages, by a Grep of their files for these slugs and paths. The other sentences of that reading of `estimate-clean-branch-ships-neutral-texts` are left to other Cases.

> **problem:**
> The check of `case-guppi` and the test of the example keep a fallback path whose condition is met, and two promises say that a later Case removes it, a sentence false in any project that installs GUPPI.

> **recommend:**
> - **Is the old path of the check removed, and how do the tests follow?**
>   - Recommended: (a) remove it; the test helper writes the Case into its file first, and the tests of the old path go or assert that nothing is stored.
>   - Answer: agreed, (a).
> - **How does the sentence of `rule-spec-reconcile` on the old path leave?**
>   - Recommended: (a) the whole `## How it works` leaves the page by hand, its facts in the docstring of `.guppi/guppi/ratified.py`.
>   - Answer: agreed, (a).
> - **Does the shape check lose its line on the old path?**
>   - Recommended: (a) a part of its own replaces the Criterion, the line reworded to a file that holds sub-cases alone.
>   - Answer: agreed, (a).
> - **What does the example test do when `case-example.md` is missing?**
>   - Recommended: (a) both tests fail with a message that names the file.
>   - Answer: agreed, (a).
> - **Which page lists the example test as its code?**
>   - Recommended: (a) `rule-case-example`, in `implementation_ref`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`, which the person agreed to: in a `then` line of Case 904.1, "that file" pointed at `<plan>.checked.json`, which the hook writes.
>   - Taken: the line ends "the hook writes no file of a Case".

### Case 904.1 — The case check reads only the case files

> **given:**
> `estimate-case-check-sends-back-a-faulty-case`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/casecheck.py`: the hook loses its old path.
> **＋** `.guppi/guppi/ratified.py`: its docstring takes the facts of the section that leaves.
> **＋** `.guppi/guppi/prespec.py`: the judgment the check runs, unchanged.
> **＋** `.guppi/tests/test_casecheck.py`: its helper and its tests of the old path.
> **＋** `cases/`: the folder of a session folder that holds the files of the Cases.
> **＋** `rule-spec-reconcile`: its `## How it works` leaves the page.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: the promise of the form of a round.
> **＋** `rule-rules-schema`: a Leaf drops `## How it works` at its next touch.

> **when:**
> `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run --project .guppi guppi casecheck --subagent` takes each file `case-<N>.md` under the `cases/` folder of a session folder, judged by `is_case_file` and `case_number` of `.guppi/guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
> **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
> **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `.guppi/guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `.guppi/guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook writes no file of a Case.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
> **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
> **－** A transcript that names no file `case-<N>.md` gets no check of a Case, whatever its newest output holds: a Case given only in the text of an answer is not checked, stored or written into a file.
> **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
> **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.
> **－** A file of another name under `cases/`, such as the working note `note-<N>.md` of `case-guppi`, is no such file: it is not read as a Case, stored or sent back, and a transcript whose calls name no file `case-<N>.md`, though they name the note, is read as one that names no such file.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the check reads only the files case-<N>.md that case-guppi wrote; the old path of the answer text is gone`
> - [ ] update `rule-spec-reconcile`
>   - change: `How it works removed by hand, a one-off, its facts in the docstring of .guppi/guppi/ratified.py; the clause on the old path of rule-case-check dropped`
> - [ ] `.guppi/guppi/casecheck.py`: `subagent` reads only the files `case-<N>.md` the subagent wrote; the old path, `answer_of` and `write_case_files` are removed where nothing else calls them, and the docstring of the module, of `subagent` and of `is_fact` follow.
> - [ ] `.guppi/tests/test_casecheck.py`: the helper `answer` writes a Case text into its file with a `Write` call in the transcript when no transcript is given; each test of the old path is removed or asserts that nothing is stored.
> - [ ] by hand, in Work Mode: `## How it works` of `vault/wiki/rules/rule-spec-reconcile.md` removed; each fact of it that the docstring of `.guppi/guppi/ratified.py` does not hold moved there, the clause on the old path of `rule-case-check` not carried.
> - [ ] read `estimate-case-check-sends-back-a-faulty-case`

> **ratification:**
> ```
> - decision[case 904.1][update][estimate-case-check-sends-back-a-faulty-case]{ref:rule-case-check}
> - decision[case 904.1][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> ```

### Case 904.2 — The shape check names a file of sub-cases alone

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/casecheck.py`: the judgment of the shape, unchanged.
> **＋** `.guppi/guppi/caseid.py`: the count of the new id, unchanged.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the files of the Cases, and `raw/<date>/<hi HHMM>/cases/case-<N>.md` among them.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `vault/wiki/decisions/`: the live Decision pages, counted for the new id.
> **＋** `vault/archive/`: the archived Decision pages, counted too.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
> **＋** The finding names each such number and a new id of the sprint of Case N: one above the highest number of that sprint that the Decision pages under `vault/wiki/decisions/` and `vault/archive/`, the decision lines of the session's ledger, the keys of `<plan>.checked.json` and the names of the files under `raw/<date>/<hi HHMM>/cases/` hold.
> **＋** The judgment comes from one function of `.guppi/guppi/casecheck.py`, and the new id from `next_id` of `.guppi/guppi/caseid.py`, which the command for the next id runs too.
> **＋** The finding tells `case-guppi` to build the Case under the new id. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new id.
> **－** A file that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a file of sub-cases alone gets no finding, in place of an answer on the old path`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 904.2][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}
> ```

### Case 904.3 — The example test reads only case-example.md

> **given:**
> `estimate-case-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `rule-case-example`: its `implementation_ref` names the test.
> **＋** `.guppi/tests/test_case_schema.py`: the test loses its fallback.
> **＋** `vault/wiki/case-example.md`: the example the test reads.
> **＋** `vault/wiki/case-schema.md`: the Render that holds no example.
> **＋** `.guppi/guppi/casecheck.py`: the check the test runs, unchanged.
> **＋** `rule-case-check`: the rule of the `SubagentStop` hook whose check the test runs.
> **＋** `rule-case-protocol`: the rule rendered into `vault/wiki/case-schema.md`.

> **when:**
> `.guppi/tests/test_case_schema.py` runs under `uv run --project .guppi pytest`. It reads the block tagged `case` in `vault/wiki/case-example.md`, rendered from `rule-case-example`, and runs over it the function of `.guppi/guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file, in a temporary project that holds the schema files of the vault and the pages the example updates.

> **then:**
> `vault/wiki/case-example.md` holds one block tagged `case`, one Case with sub-cases in the chat form that `case-guppi` writes into its file, and after it one block tagged `then`.
> **＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
> **＋** The example's `context` says what the sentence around the match of its `replace` pair names.
> **＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
> **＋** `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, holds no example block and names `vault/wiki/case-example.md` where it sets the chat form and the `then` block.
> **＋** The check gives the example no finding and no note, and the test passes; a change of the check that gives the example a finding or a note fails the test, which prints it.
> **＋** The test reads the example from `vault/wiki/case-example.md` alone and the checks from `.guppi/guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/case-example.md` does not stand, or holds no block tagged `case`, both tests of `.guppi/tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `estimate-case-example-passes-the-check`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the test reads case-example.md alone, and a missing file fails both tests with its name`
> - [ ] update `rule-case-example`
>   - set:
>     ```
>     implementation_ref: [.guppi/tests/test_case_schema.py]
>     ```
>   - change: `implementation_ref names the test of the example`
> - [ ] `.guppi/tests/test_case_schema.py`: `example` reads `vault/wiki/case-example.md` alone; a missing file fails both tests by `pytest.fail` with a message that names it; the docstring of the module and of `example` follow, and `SCHEMA` leaves where nothing else reads it.
> - [ ] read `estimate-case-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 904.3][update][estimate-case-example-passes-the-check]{ref:rule-case-example}
> - decision[case 904.3][update][rule-case-example]{ref:rule-case-example}
> ```
