## Case 653 — The check of case-guppi drops the old path of a Case given as text

> **context:**
> When `case-guppi` stops, the `SubagentStop` hook `uv run guppi casecheck --subagent` of `rule-case-check` reads each file under `cases/` that the agent wrote or edited, checks it whole and stores it. Case 645.2 kept an old path beside it: when the agent writes no file and its newest output holds a Case heading, the hook checks that text, stores it and, with no finding, writes the file itself by `write_case_files`. The old path stays until a reading of `estimate-case-build-writes-the-case` passes live, and a Case of a later session removes it. Case 473.2 set that order, and `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` says the removal comes after that reading. That Estimate is `pending`, and the session's ledger holds no reading of it. In this session three live builds, Cases 650, 651 and 652, each wrote their file in Plan Mode with no permission prompt. The method of the Estimate also asks for one Case with a create without a ref, one that changes a hook, a Case the hook sent back and fixed by Edit, and a change the person asked for on one sub-case, made by Edit of that sub-case. The three builds do not cover the create without a ref or the change on a sub-case. This Case changes a hook.
>
> The person chose the following. The Case is ratified now, and its code waits for that reading. The tasks that change `guppi/casecheck.py` and `tests/test_casecheck.py` open with `stop:` and run only after the person confirms that the reading of `estimate-case-build-writes-the-case` passed in this session. A Case given as text with no file is sent back once, with nothing stored: the agent is told to write the file and answer with the summary. Both Estimates that speak of the old path get their Criterion replaced whole, one sub-case each. 653.1 replaces the Criterion of `estimate-case-check-sends-back-a-faulty-case`; its `purpose` and `method` do not name the old path, so they stand. 653.2 replaces the Criterion of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` without its exception for an answer on the old path; its `purpose` and `method` stand too. The Criterion of `estimate-case-build-writes-the-case` speaks of the writer, not of the hook, so it stands.
>
> The searches this Case rests on. A Grep of `old path` over `vault/wiki/` with the glob `!**/decisions/**` printed 6 files: `brief.md`, `log.md`, `rule-case-check`, `rule-spec-reconcile`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape` and `estimate-case-check-sends-back-a-faulty-case`. The two Estimates enter 653.1 and 653.2. In `rule-case-check` the hit is a History line, and its Purpose says nothing of the old path, so the page stands. `rule-spec-reconcile` says in How it works that the old path writes a file of `cases/` until the writer is live, and a pair in 653.1 removes those words. Case 650.1 replaces the words just before them in the same sentence. The pair of 653.1 anchors on the words after those, so both pairs apply in either order. Together the sentence reads: the hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and so does this hook for the entry that holds a number, and this hook does not judge the writes of those hooks. The context of Case 650 says that an answer of the old path under a held number is sent back. After this Case, any Case given as text is sent back, so nothing there conflicts. A Grep of `old path|old way|write_case_files` over `guppi/` and `tests/` printed `guppi/casecheck.py` and `tests/test_casecheck.py`, and over `.claude/` it printed nothing. A Grep of `SubagentStop` over `vault/wiki/rules/` printed 5 files: `rule-case-check`, `rule-spec-reconcile`, `rule-orchestration`, `rule-case-protocol` and `rule-hook-registry`. `rule-orchestration` sets what the main agent does with the summary after the hook. `rule-case-protocol` describes the test of its example, which calls `check_answer` directly. `rule-hook-registry` keeps the registration, and `.claude/settings.json` registers only this hook on `SubagentStop`. They stand. A Grep of `answer|output` over `vault/wiki/estimates/` with the glob `estimate-case-check-*.md` printed 13 files. Apart from the two Estimates of this Case, their Criteria use "answer" for the Cases that the check reads. Case 651 kept that word outside `orchestration.md`. A file can still hold sub-cases alone, so the lines on an answer of sub-cases alone stay true. `estimate-case-check-sends-back-a-faulty-round` judges only the newest output as a round. They stand.
>
> The check sent back notes, and they stand. In 653.1, four lines of the old Criterion are not carried word for word, and each was changed on purpose. The line on the old path is replaced by the line that sends a Case given as text back. The line on the store now says that the hook writes no file under `cases/`. The line on an unchanged file also covers a Case given as text again. The line on an unreadable transcript now says that `last_assistant_message` is not read. In 653.2, the line on an answer on the old path is dropped, as the person chose. One `then` line of 653.2 shares most of its words with 653.1: the exit 2 with the finding on stderr. Each sub-case still sets its own promise: 653.1 covers the check of a file and of a Case given as text, and 653.2 covers a Case built again in another shape.
>
> Not done: if the reading does not pass in this session, the `stop:` tasks stay open and Retro reports them as debt. The page texts and the Criteria still land at the librarian's run, so the readings of both Estimates stay `pending` until the code changes.

> **problem:**
> The check of `case-guppi` still reads a Case from the agent's reply text and writes its file when the agent writes none. That is a fallback for a writer that is now measured live, and it hides a builder that forgot its file. The question was when the fallback goes, what the check does with a Case given as text afterwards, and which checks prove it.

> **recommend:**
> - **When the fallback is removed**
>   - Recommended: (b) build the Case now; its code task opens with `stop:` and runs only after the check of the builder is read and passes in this session, and otherwise stays open as debt at Retro.
>   - Answer: agreed, (b).
> - **What the check does with a Case given as text and no file**
>   - Recommended: (a) send the builder back with one finding that tells it to write the Case into its file and answer with the summary; nothing is stored, and the same reply given unchanged again is not sent back again.
>   - Answer: agreed, (a).
> - **Which checks prove the change**
>   - Recommended: (a) replace the Criterion of both checks, one sub-case each: the first drops the fallback and says what the send-back does, the second drops its exception for the old path.
>   - Answer: agreed, (a).

### Case 653.1 — A Case given as text with no file goes back to case-guppi

> **given:**
> `estimate-case-check-sends-back-a-faulty-case`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the check on `SubagentStop` and its tests.
> **＋** `guppi/ratified.py` and `guppi/prespec.py`: the reading of the chat form and `judge`, which the check runs. Unchanged.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: the promise of the form of a round. Unchanged.
> **＋** `rule-spec-reconcile`: its How it works names the old path.
> **＋** `vault/raw/2026-10-05/1343/cases/case-650.md`: Case 650.1 changes the same sentence of `rule-spec-reconcile`.
> **＋** `estimate-case-build-writes-the-case`: its reading gates the code. Unchanged.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` and `<plan>.checked.json`: the file of a built Case and the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes each file under the `cases/` folder of a session folder, judged by `is_case_file` of `guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
> **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
> **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook writes no file under `cases/`.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
> **＋** A transcript that names no such file and whose newest output holds a Case heading exits 2 with one finding: `case-guppi` is told to write the Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md` and answer with the summary, and nothing is stored.
> **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice; an output with a Case heading that an earlier output of the subagent holds with the same text, trailing spaces aside, is not sent back again.
> **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
> **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, whatever `last_assistant_message` holds, and nothing is stored. A session with no plan file is not sent back for a Case or for a Case given as text.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the old path is gone: a Case given as text with no file is sent back once and not stored, and last_assistant_message is no longer read (case 653.1)`
> - [ ] update `rule-spec-reconcile`
>   - old: `` and the old path of `rule-case-check` writes a file of `cases/` the same way until the writer is live; this hook does not judge them; ``
>   - new: `` and this hook does not judge the writes of those hooks; ``
>   - change: `the old path of rule-case-check, which wrote a file of cases/ with no tool call, is gone (case 653.1)`
> - [ ] stop: `guppi/casecheck.py`, after the person confirms that the reading of `estimate-case-build-writes-the-case` passed in this session: `write_case_files` and the old path in `subagent` are removed; with no file written, a newest output that holds a Case heading is sent back with one finding and nothing stored, unless an earlier output holds the same text; the fallback of `answer_of` to `last_assistant_message` goes; the module docstring and the docstrings of `subagent` and `is_fact` say the same.
> - [ ] stop: `tests/test_casecheck.py`, after the same confirmation: the helper that feeds a Case as reply text writes it into its file with a `Write` call in the agent transcript; the tests of the file written by the hook and of the fallback to `last_assistant_message` are removed; tests `-k subagent`: a Case as text with no file is sent back, nothing stored and no file written; the same text again is not sent back; an unreadable transcript with a Case in `last_assistant_message` gets nothing; with no plan file nothing is sent back.
> - [ ] read `estimate-case-check-sends-back-a-faulty-case`

> **ratification:**
> ```
> - decision[case 653.1][update][estimate-case-check-sends-back-a-faulty-case]{ref:rule-case-check}
> - decision[case 653.1][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> ```

### Case 653.2 — The check of a Case built again in another shape drops its old-path exception

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: `shape_findings` and `new_number`, the judgment and the count of the check.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
> **＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
> **＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new number.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the exception for an answer on the old path is gone with that path (case 653.2)`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 653.2][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}
> ```
