<!-- approved 02:42:51 · session 958b7a22 -->

# Session 2341 — the librarian's report of 1930 and the items of the brief of 1930

## Case 913 — The librarian's report gives each part its frame sends to it, with no limit of lines

> **context:**
> At the end of its run the librarian returns a short report, and `/handoff` or `/box` shows it to the person unchanged. The Render of `rule-close` in `.claude/agents/librarian-guppi.md` lists what the report gives, caps it at twenty lines and ends with "Nothing else". `estimate-close-reports-in-twenty-lines` checks the counts, the flags, the lint total and the twenty lines. Its reading at the start of this session was `failed` on the numbers 15, 25 and 12. `case-guppi` read the report at its source, the last message of the saved chat of the previous session (`7f200512-38a4-43be-9723-2cbf3756ed67.jsonl`, the message after the librarian's hand-back). That report gives 24 pages created, 23 updated, the `incomplete` mark of Case 905, a Flags list with the stale defer of `rule-clean-branch`, a lint of 11 lines and 19 lines in all. A Grep `12 lines|\(15\)|\(25\)` over that chat printed nothing, and the person then said they had looked at another report; the main agent writes the new reading before this Case is ratified. `brief.md` gives 23 created while its own list adds up to 24; the main agent records that as a lesson line (Q2). The report's own rule is still at fault. Other steps of the same frame send more to the report: each Grep of the index check with the number of lines it printed, each page opened for a duplicate, a cluster or a script error, the one read of `ledger.md`, a refused instruction or call, and what `guppi archive` moved or kept. So "Nothing else" is false beside them. Three Estimates set those parts, and the pointer of the new list to them leaves each Criterion true, so each stands: `estimate-index-check-merges` (each Grep and its number of lines, each page opened), `estimate-synthesis-clusters` (each page opened at the synthesis) and `estimate-documentation-completes` (each page opened, the read of `ledger.md`, the units of `guppi archive`, a refused call, a refused instruction of the handoff). `estimate-spec-box-runs-a-conserved-spec` says that `/box` shows the librarian's report unchanged with the exit code of `uv run --project .guppi guppi test`. That exit code is a line `/box` adds beside the report, not a part of the report, so that Criterion stands, and the new `then` says so. The report also held a `Tests` line and a list of files, which no step asks for. The person chose to drop the twenty-line limit, since they see no point in it. This Case rewrites the list of `rule-close`: the report gives the parts the list names and each part that another step of the frame sends to it, holds no test result and no list of files, and has no limit of lines. It replaces the Criterion, the `purpose` and the `method` of the Estimate, since all three state the old promise. The old line on the counts, the flags and the lint total is not carried word for word: the first line of the new `then` names those parts and the marks and archived pages beside them. The old line on twenty lines or fewer is dropped, as the person chose. The Case also renames the Estimate `estimate-close-reports-the-run`; a Glob `vault/**/estimate-close-reports-the-run*.md` printed nothing, so the slug is free. `estimate-close-commits`, the other Estimate of `rule-close`, speaks of the commit, not of the report, so its Criterion stands. The failure of the commit command that the report names is a Frontier item of its own (Q4). The librarian applies the ledger entries in their order (`apply` in `.guppi/guppi/generate.py`), and `Vault.estimate` there replaces the status and the Result of the page. So the new reading, written before this Case's decision lines, lands on the old Criterion before this update sets the page `pending`. The `method` waits for a librarian's run that starts with the new Render. The run of this session starts with the old one, since its render step comes later, so Retro leaves the Estimate `pending`. A Grep `twenty` (case-insensitive) over `vault/wiki/` and `.claude/` printed `brief.md`, `log.md`, `rules/rule-close.md`, `estimates/estimate-close-reports-in-twenty-lines.md`, `estimates/estimate-close-commits.md` and `.claude/agents/librarian-guppi.md`. brief.md and log.md are not read. In `estimate-close-commits.md` the word stands only in the slug on a History line. The other three are the texts this Case changes. A Grep of the slug `estimate-close-reports-in-twenty-lines` over the repository outside `vault/raw/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-close.md` and `vault/wiki/estimates/estimate-close-commits.md`. The hit in `estimate-close-commits.md` is a History line, brief.md and log.md are not read, and the rename takes the `estimates` link of `rule-close`. A Grep `librarian-guppi\.md|"librarian-guppi"|'librarian-guppi'` over `.guppi/tests/` printed `test_grepguard.py`, which names the agent type and reads no file. `rule-close` has `core: true`, and the live build test of `.guppi/tests/test_ship.py` judges its pointers, so the new sentence keeps its pointer in a bracket at its end.

> **problem:**
> The report of the librarian follows a list in `rule-close` that the other steps of its own frame contradict. That list ends with "Nothing else" and a twenty-line limit, while those steps send more parts to the report. The report then adds parts that no step asks for, such as test results and a list of files. The Estimate that checks the report checks neither those parts nor their absence.

> **recommend:**
> - **What the reading of the report stands on**
>   - Recommended: (a) a new reading from the report as shown, written by the main agent; no Case for it.
>   - Answer: agreed, (a); the person then said they had looked at another report.
> - **The created count in the brief**
>   - Recommended: (a) an error lesson line by the main agent; this Case changes nothing for it.
>   - Answer: agreed, (a).
> - **What the report may hold beyond the list of `rule-close`**
>   - Recommended: (a) Case 913 rewrites the list: the counts, the marks, the archived pages, the flags, the lint total and each read and refusal another step sends to the report; no test results and no list of files.
>   - Answer: agreed, (a).
> - **The commit command that failed once**
>   - Recommended: (a) a new Frontier item on `estimate-close-commits`; Case 913 does not cover it.
>   - Answer: agreed, (a).
> - **How the new list is checked**
>   - Recommended: (a) replace the Criterion and the purpose of `estimate-close-reports-in-twenty-lines`; it goes back to `pending`.
>   - Answer: agreed, (a).
> - **The twenty-line limit**
>   - Recommended: (a) keep twenty lines.
>   - Answer: (b) drop the limit; the person sees no point in it.
> - **How the list names the other parts**
>   - Recommended: (a) one pointer to the other steps of the frame.
>   - Answer: agreed, (a).
> - **The name of the Estimate, now that the limit is gone**
>   - Recommended: (a) rename it to `estimate-close-reports-the-run`.
>   - Answer: (a).
> - **Change**
>   - Asked: the person agreed with the fix of a pre-spec finding: name `estimate-spec-box-runs-a-conserved-spec`, and say that the exit code of the tests that `/box` shows is a line of its own beside the report, not a part of the report.
>   - Taken: `given` names that Estimate, `then` gains a `－` line on the exit code, the `method` leaves that line out of the report, and `context` says why that Criterion stands.
> - **Change**
>   - Asked: the person agreed with the fix of a pre-spec finding: name the Estimates that set the parts other steps send to the report, and add the Greps of the index check to the list of those parts.
>   - Taken: `context` names `estimate-index-check-merges`, `estimate-synthesis-clusters` and `estimate-documentation-completes` as covered by the pointer of the new list and says why each stands, and its list of parts adds each Grep of the index check with its number of lines.

> **given:**
> `rule-close`: the rule whose Render lists what the librarian's report gives.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, where that Render stands beside the steps that send parts to the report.
> **＋** `estimate-close-reports-in-twenty-lines`: its Criterion, purpose and method are replaced, and it is renamed `estimate-close-reports-the-run`.
> **＋** `.claude/skills/handoff/SKILL.md`: dispatches the librarian and shows its report unchanged.
> **＋** `.claude/skills/box/SKILL.md`: dispatches the librarian and shows its report in a session that `/box` runs.
> **＋** `estimate-spec-box-runs-a-conserved-spec`: sets the exit code of the tests that `/box` shows beside the report.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
> **＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

> **then:**
> The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
> **＋** The report gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
> **－** The report holds no test result and no list of files.
> **－** No limit of lines binds the report.
> **－** The exit code of `uv run --project .guppi guppi test` that `/box` shows beside the report is a line of `/box`, not a part of the report.

```then
update:
- slug: rule-close
  replace:
  - old: 'Then return a report of at most twenty lines: pages created and updated per category, entries marked incomplete or failed, pages archived, the flags you raised, the lint total. Nothing else.'
    new: 'Then return a report: pages created and updated per category, entries marked incomplete or failed, pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files (as set in case 913).'
  change: the report gives each part another step of the frame sends to it, no test result and no list of files, and has no limit of lines
- slug: estimate-close-reports-in-twenty-lines
  set:
    status: pending
    purpose: Whether the librarian's report, as /handoff or /box shows it, gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to it, with no test result and no list of files
    method: 'by hand, after a librarian''s run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close with no limit of lines: the person''s answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave each part the Criterion names and no test result and no list of files, the exit code of guppi test that /box adds beside the report not counted as a part of it'
  rename: estimate-close-reports-the-run
  change: the Criterion replaced whole — the report gives each part its frame sends to it, no test result and no list of files, and has no limit of lines; renamed from estimate-close-reports-in-twenty-lines
```

```tasks
- [x] update `rule-close`
- [x] update `estimate-close-reports-in-twenty-lines`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-close-reports-the-run`
```

## Case 914 — The list of rendered files ends each line with a bare line feed, on Windows too

> **context:**
> At its close the librarian commits the vault with the command of the Render of `rule-close`: `git add vault $(uv run --project .guppi guppi render --paths) && git commit ...`. `run` of `.guppi/guppi/render.py` prints each path of `--paths` by `print(governs, file=stdout)`, and `main` of `.guppi/guppi/cli.py` sets only the encoding of the output, to UTF-8. On Windows the output of Python ends each line with a carriage return and a line feed. The shell keeps the carriage return on each path. `case-guppi` read the run at its source, the saved chat of the librarian of session 1930 (`subagents/agent-a9b114d335b9583a3.jsonl` under `7f200512-38a4-43be-9723-2cbf3756ed67`): the command as written printed `Exit code 128` and `fatal: pathspec '.claude/agents/ask-guppi.md?' did not match any files`, and the next call ran the same command with `| tr -d '\\r'` after `--paths`. The report of that run, the last message of the main chat, says the same. `estimate-close-commits` was read `passed` at the /hi of this session from the end state alone: one separate commit and a clean tree. Its tests in `.guppi/tests/test_render.py` call `render.run` with an in-memory stream and split its output into lines, so they never see a line ending. The Python documentation of `io` (https://docs.python.org/3/library/io.html) says that on output `newline=None` translates each line feed to `os.linesep`, that `''` or `'\n'` translates nothing, and that `reconfigure` may change `newline` on a stream that nothing was read from. The person chose to fix the output of `--paths` alone, at its source (Q1): a Grep `\$\(uv run[^)]*guppi` over the repository outside `vault/raw/` printed `vault/wiki/rules/rule-close.md`, `.claude/agents/librarian-guppi.md`, `vault/wiki/estimates/estimate-close-commits.md` and nine files under `vault/archive/`, each hit the close command or a copy of it, so no other shell command reads the output of a `guppi` command. The fix is in code, so it holds at the librarian's run of this session, whose frame still holds the old close command, which then works as written; the Render of `rule-close` does not change. `rule-render-harness` lists `.guppi/guppi/render.py` in its `implementation_ref`, but a Grep `--paths` over `vault/wiki/estimates/estimate-render-*.md`, the files of its three Estimates, printed nothing; `estimate-close-commits`, whose target is `rule-close`, holds that promise since case 857. This Case replaces its Criterion whole (Q2): each old line stands, but its first line, on what `--paths` prints, which is not carried word for word, since the new first line adds the bare line feed to it, and a new line says that the close command as written passes each path as it stands. It also sets its `purpose` anew, since the old one does not name the close command as written; its `method` gains the test that runs `--paths` as a child process and reads its output as bytes, and keeps its reading by hand of the commit after a librarian's run. The main agent writes a new reading `failed` of the Estimate before this Case's decision lines (Q3), so that the failure lands in its Result before this update sets it `pending`. A failed close command does not go into the librarian's report by this Case (Q4); the report is the frame of Case 913, which changes another sentence of the same Render. A Grep `estimate-close-commits|render --paths` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `.claude/agents/librarian-guppi.md`, `vault/wiki/rules/rule-close.md`, `vault/wiki/estimates/estimate-close-commits.md`, `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md` and `.guppi/tests/test_render.py`. `brief.md` and `log.md` are not read; the lesson records a reading of an earlier session and stands; the close command in `rule-close` and `librarian-guppi.md` stays true once `--paths` prints bare line feeds.

> **problem:**
> On Windows the list that the close command passes to `git add` carries a carriage return on each path, so the command as written fails, and the librarian ran a changed command. The Estimate of the commit passed on the end state, and its tests cannot see a line ending.

> **recommend:**
> - **Where the line ending is fixed**
>   - Recommended: (a) `--paths` alone prints bare line feeds, set on its own output before it prints.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) replace the Criterion of `estimate-close-commits` with the line ending and the close command as written; a new test runs `--paths` as a real process and asserts no carriage return; the page goes back to `pending`.
>   - Answer: agreed, (a).
> - **What happens to the reading of passed**
>   - Recommended: (a) the main agent writes a new reading `failed` from the saved chat, before this Case's decision lines.
>   - Answer: agreed, (a).
> - **Whether a failed close command goes into the report**
>   - Recommended: (a) left out of this Case.
>   - Answer: agreed, (a).

> **given:**
> `estimate-close-commits`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `.guppi/guppi/render.py`: `run` prints the list of `--paths`.
> **＋** `.guppi/tests/test_render.py`: the tests of `guppi render --paths`.
> **＋** `rule-close`: the rule whose Render writes the close command, the target of the Estimate.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, where the close command stands.
> **＋** `rule-plugin-install`: the rule whose file the list names only in a project that holds it.
> **＋** `plugin/skills/install/SKILL.md`: the file of `rule-plugin-install` that the list may name.
> **＋** `vault/`: the folder the commit takes beside the list.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, each line ended by a bare line feed with no carriage return, on Windows too, and writes nothing.
> **＋** The close command, as `.claude/agents/librarian-guppi.md` writes it, passes each path of that list to `git add` as the path stands, with no filter added to it.
> **＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

```then
update:
- slug: estimate-close-commits
  set:
    status: pending
    purpose: The librarian's run ends in one separate commit of vault and each file the render writes, by the close command as its frame writes it, with no rendered file left modified or untracked
    method: 'uv run --project .guppi pytest .guppi/tests/test_render.py -k paths, on Windows too, where the test that runs guppi render --paths as a child process reads its output as bytes; by hand, after a librarian''s run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked'
  change: the Criterion replaced whole — guppi render --paths ends each line with a bare line feed, on Windows too, and the close command passes each path to git add as it stands
```

```tasks
- [x] `.guppi/guppi/render.py`: in `run`, the `--paths` branch sets its output stream to `newline="\n"` by `reconfigure` where the stream has it, before it prints; the docstring of `--paths` says each line ends in a bare line feed.
- [x] `.guppi/tests/test_render.py`: a test whose name holds `paths` runs `guppi render --paths` as a child process over a small vault in a temp folder and asserts that its output, read as bytes, holds no carriage return and one line per `governs` path.
- [x] update `estimate-close-commits`
- [ ] read `estimate-close-commits`
```

## Case 915 — The Case marks the lesson it fixes, and the ledger hook stops asking

> **context:**
> Today the `Stop` hook `uv run --project .guppi guppi ledger` writes the decision lines of a reply. Then, for each lesson of the session that no mark ties to a Case, it exits 2 with one stderr line asking whether a Case of the session fixed the lesson's cause: `unaddressed` and `reminder_message` of `.guppi/guppi/ledger.py`, called in `run` after `append`, judged by `unlinked_lessons` of `.guppi/guppi/materialize.py`. `untold` of the same module stays silent only while the line already stands in a refusal of the hook since the person's last message. So the question comes back at every ratification. In session 2341 the lesson `lesson-librarian-writes-a-total-no-count-printed` drew it after Case 913 and again after Case 914, and each time the answer was no. Each time it cost one more reply in the chat. The person found this noisy and pointed out two things. A later Case may still fix a lesson. Only an `error` lesson needs this judgment, since a `knowledge` lesson records a fact and has no cause for a Case to fix. The person asked for a quiet question, or an answer inside the reply that holds the Frontier.
>
> A `Stop` hook cannot ask quietly. Claude Code's hook documentation (https://code.claude.com/docs/en/hooks, the first 100 000 characters read) says that exit 2 on `Stop` "continues the conversation", and that `additionalContext` on `Stop` is "feedback that continues the conversation". The quiet way it gives, `additionalContext` on `UserPromptSubmit`, "doesn't appear as a chat message in the interface". The person chose instead that `case-guppi` weighs each `error` lesson of the session that has no mark while it builds a Case. Where the Case fixes the cause, `case-guppi` puts `{addresses:<slug>}` on a decision line of its `ratification`. The person sees the mark and ratifies it with the Case, and the main agent copies it into the reply that acknowledges the ratification, above the Frontier. The rule that governs the choice is the one rule of `ratification.md`: nothing changes without a ratified decision. A mark changes which Case the lesson entry names in `addressed_by`, so the person signs it in the Case. The person also chose that the hold of a lesson written after a Case (case 682.1) leaves out a `knowledge` lesson. That is a second promise with its own Estimate, so the Case splits: 915.1 removes the reminder, 915.2 gives `case-guppi` the judgment, and 915.3 narrows the hold.
>
> A line with the mark lands today. `off_store` of `.guppi/guppi/ledger.py` removes `{addresses:...}` by `ADDRESSES_MARK` from both the fresh line and the stored lines, which it reads by `fence_ledger_lines` of `.guppi/guppi/casecheck.py`, before it compares them. So no reader needs an old form. The kind of a lesson is read by `parse_line` of `.guppi/guppi/materialize.py`, which gives a lesson record its `kind`, `error` or `knowledge`. A Grep of `.guppi/guppi/` for `"error"|"knowledge"|== .error|lesson\[error` printed `materialize.py` and `sprint_close.py`. The second judges the `kind` of a lesson page, not of a ledger line. So the hold reads `record["kind"]` of the same parse and adds no second copy. A Grep of `.guppi/` for `unlinked_lessons|reminder|addresses`, `test_ledger.py` left out, printed `test_onward.py`, `casecheck.py`, `test_materialize.py`, `ledger.py`, `onward.py` and `materialize.py`. A Grep of `.guppi/` for `unlinked_lessons` printed only `ledger.py`, in `unaddressed` and its docstring, `materialize.py`, its definition, and two tests of `test_ledger.py`, so 915.1 removes it with them.
>
> A Grep of `vault/wiki/` for `reminder|has no mark|lesson with no mark`, `log.md` and `brief.md` left out, printed `orchestration.md`, `rules/rule-orchestration.md`, `rules/rule-prespec-onward.md`, `estimates/estimate-ledger-write-asks-for-the-mark-of-a-lesson.md`, `estimates/estimate-ledger-write-reminds-of-the-mark-on-a-decision-line.md` and `estimates/estimate-prespec-onward-sends-the-agent-on.md`. The same Grep of `.claude/` printed nothing. The hits in `orchestration.md` and `rule-orchestration.md` under the example Case 7 speak of a booking reminder and stand. The sentence of `rule-orchestration` on the reply that answers the reminder, and the three places in the Purpose of `rule-prespec-onward`, change in 915.1. The Criterion of `estimate-prespec-onward-sends-the-agent-on` stands. `guppi onward --plan` judges a refusal of the ledger hook by its command through `sent_back_last`, never by its text. The Criterion names the reminder only as one kind of such a refusal, and replacing it whole would sign the same promise again. The tests of `.guppi/tests/test_onward.py` that feed a hand-made reminder text stand for the same reason. The sentence of `ratification.md` (`rule-ratification`) on `{addresses:<lesson slug>}` sets only the form of the mark and stays true. The slug `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line` stays as it is: 915.1 replaces its Criterion and `purpose`, which now say that the hook reminds of nothing, and a rename would change its links in the middle of the readings of this session. The sentence of `rule-orchestration` around its pair, read whole under `## Writing the ledger lines`, keeps the hold of a decision line off the stored Case and the readings, and drops only the reply that answers the reminder. A Grep of `case-913.md` and `case-914.md` under `cases/` for `rule-ledger-write|rule-orchestration|rule-case-build|rule-prespec-onward|ledger\.py|onward\.py` printed nothing, so no other Case of the session writes into the pages of this Case.
>
> A Grep of `.guppi/tests/` for `case-guppi\.md|orchestration\.md|rule-ledger-write|rule-case-build|rule-orchestration` printed `test_gate.py`, `test_guppi_package.py`, `test_ledger.py`, `test_onward.py` and `test_orchestration.py`. Only `test_orchestration.py` reads a live file, `vault/wiki/orchestration.md`. It reads only the blocks tagged `showing` and `defer`, which this Case does not touch. The code changes in Work Mode of this session. `.claude/agents/case-guppi.md` and `orchestration.md` change at the librarian's render after it, so for the rest of this session nothing asks about a lesson. A lesson written after `case-guppi` built a Case, and before that Case is ratified, is not weighed against it. The person accepted that cost in the round.

> **problem:**
> The ledger hook asks the same question about a lesson with no mark after every ratification, and each time it costs one more reply in the chat. It asks about `knowledge` lessons too, though no Case fixes the cause of a fact.

> **recommend:**
> - **How often should the hook ask about a lesson with no mark?**
>   - Recommended: (a) once a lesson, at the first ratification after it, judged from the session's ledger.
>   - Answer: none of the options; a later Case may still fix the lesson, only an error lesson needs the judgment and a knowledge lesson none, and the question should be quiet or answered inside the reply that holds the Frontier; replaced by **Where should the question about an error lesson with no mark reach the agent?**
> - **Where should the question about an error lesson with no mark reach the agent?**
>   - Recommended: (b) the Case answers it when it is built: `case-guppi` weighs each open error lesson and writes the mark on its own ledger lines, which the person ratifies.
>   - Answer: agreed, (b).
> - **Which lessons does the question cover?**
>   - Recommended: (a) error lessons only, for the new question and for the hold of a lesson written after a Case.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed with the fixes that `/pre-spec` proposed: the new text of `rule-case-build` names only a lesson that stands before the decision lines of a reply, and reads the ledger by a Grep for `lesson\[error\]` and a Grep for `\{addresses:`; the pair of `rule-prespec-onward` keeps the pointer to case 688.7; the `then` of 915.1 names the new Render of `rule-orchestration` in the Spec.
>   - Taken: each fix as proposed; the `method` of `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line` adds the reading of that Render at Retro.

### Case 915.1 — The ledger hook writes a decision line after a lesson without a reminder

> **given:**
> `rule-ledger-write`: the page of the ledger hook; its Purpose names the reminder.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: its Criterion is replaced whole; its slug stays.
> **＋** `.guppi/guppi/ledger.py`: the hook; `unaddressed`, `reminder_message`, their call in `run` and the docstring.
> **＋** `.guppi/guppi/materialize.py`: `unlinked_lessons`, which only the reminder calls.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the reminder.
> **＋** `rule-orchestration`: renders `vault/wiki/orchestration.md`, which names the reply that answers the reminder.
> **＋** `rule-prespec-onward`: its Purpose names the reminder among the refusals after which it sends the agent on.
> **＋** `.guppi/guppi/onward.py`: its docstring names the reminder.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line of the session stands before them, in the session's ledger or among the lines of the same `Stop`, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

> **then:**
> The hook writes every line of the `Stop` and prints no line about the lesson.
> **＋** When no other refusal of the hook stands at that `Stop`, it exits 0.
> **＋** A decision line that carries `{addresses:<slug>}` lands in the session's ledger as any decision line of its Case does.
> **＋** `.guppi/guppi/ledger.py` holds no question about a lesson before a Case, and the new Render of `rule-orchestration` in the Spec names no reply that answers one.
> **－** The hook holds back no decision line because it lacks `{addresses:...}`.

```then
update:
- slug: rule-ledger-write
  replace:
  - old: 'It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}` (case 685.1).'
    new: 'It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and asks nothing about the lesson: the mark `{addresses:<lesson slug>}` comes on a ledger line of the Case that fixed its cause, as `case-guppi` writes it and the person ratifies it, as `rule-case-build` sets it (as set in case 915.1).'
  change: the hook no longer reminds the agent of a lesson with no mark; the Case carries the mark
- slug: estimate-ledger-write-reminds-of-the-mark-on-a-decision-line
  set:
    status: pending
    purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session with no reminder of the addresses mark, and lands a decision line that carries it
    method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault; by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion
  change: the Criterion replaced whole — no reminder of a lesson with no mark
- slug: rule-orchestration
  replace:
  - old: in the reply that answers the ledger hook's reminder of a lesson with no mark, which, when a Case of the reply fixed the cause, holds only a `LEDGER` block with one decision line of that Case or sub-case written again with `{addresses:<lesson slug>}`, and otherwise no block (case 685.1); and in the reply
    new: with each mark `{addresses:<lesson slug>}` that the summary of `case-guppi` holds on a line, and in the reply
  change: no reply answers a reminder of a lesson with no mark; the reply that acknowledges a ratification carries the mark the summary holds
- slug: rule-prespec-onward
  replace:
  - old: '— a line it refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7):'
    new: '— a line it refused or held (case 688.7):'
  - old: such as the answer that no Case fixed the cause of a lesson,
    new: such as the answer to a held decision line whose stored line is wrong,
  - old: The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop.
    new: The ledger hook tells each refused or held line once a stretch, so the hook cannot loop.
  change: the reminder of a lesson with no mark is gone from the refusals it follows
```

```tasks
- [x] update `rule-ledger-write`
- [x] update `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
- [x] update `rule-orchestration`
- [x] update `rule-prespec-onward`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] `.guppi/guppi/ledger.py`: remove `unaddressed`, `reminder_message` and the `reminders` of `run`; remove the paragraph of the module docstring on the reminder (case 685.1) and its mention in the paragraph on the hold.
- [x] `.guppi/guppi/materialize.py`: remove `unlinked_lessons`.
- [x] `.guppi/guppi/onward.py`: the docstring names a line the ledger hook refused or held, and no reminder.
- [x] `.guppi/tests/test_ledger.py`: replace the tests of the reminder and `test_unlinked_lessons_reads_the_marks_of_both_kinds` with tests that a lesson before fresh decision lines brings no stderr line and exit 0, that a decision line with `{addresses:<slug>}` lands, and that the hook holds back no decision line for the mark; `test_a_lesson_before_every_decision_line_is_not_asked` expects `(0, "")`.
- [x] `uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_onward.py`
- [x] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
```

### Case 915.2 — case-guppi marks the error lesson its Case fixes

> **given:**
> `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case.
> **＋** `estimate-case-build-marks-the-lesson-its-case-fixes`: the new check.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, which `case-guppi` reads for the lessons.
> **＋** `vault/wiki/ratification.md`: the form of the mark `{addresses:<lesson slug>}`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of the Case, whose `ratification` carries the mark.

> **when:**
> `case-guppi`, by `.claude/agents/case-guppi.md`, writes the `ratification` of a Case into its file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the session's ledger `raw/<date>/<hi HHMM>/ledger.md` holds a `lesson[error][<slug>]` line that no mark ties to a Case.

> **then:**
> `case-guppi` judges whether the Case, or one of its sub-cases, fixes the root cause of that lesson.
> **＋** Where one does, one decision line of that Case or sub-case carries `{addresses:<slug>}`, in the form of `vault/wiki/ratification.md`, and `context` names the lesson and why the Case closes it.
> **＋** The summary of `case-guppi` holds the line with the mark as the file holds it, so the person ratifies the mark with the Case.
> **－** A `lesson[knowledge]` line of the ledger gets no mark from this judgment.
> **－** A lesson with `{addressed_by:...}` on a line of its slug, or that a decision line of the ledger already marks with `{addresses:<slug>}`, is not judged again.

```then
create:
- slug: estimate-case-build-marks-the-lesson-its-case-fixes
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi weighs each error lesson of the session that no mark ties to a Case, and writes the addresses mark on a decision line of the Case or sub-case that fixes its cause
  method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: says why it stands (case 784).
    new: says why it stands (case 784). Before you write the `ratification` of a Case, read the session's ledger `raw/<date>/<hi HHMM>/ledger.md` by a Grep for `lesson\[error\]` and a Grep for `\{addresses:`, and for each `error` lesson there that no mark ties to a Case — no `{addressed_by:...}` on a line of its slug and no decision line after it with `{addresses:<slug>}` — judge whether your Case, or one of its sub-cases, fixes its root cause; where one does, add `{addresses:<slug>}` to one decision line of that Case or sub-case and say in `context` which lesson it closes and why, and add no mark for a `knowledge` lesson, since the ledger hook asks nothing about a lesson that stands before the decision lines of a reply (as set in case 915.2).
  change: case-guppi weighs each error lesson of the session with no mark and writes the addresses mark on the Case that fixes it
```

```tasks
- [x] update `rule-case-build`
- [x] create `estimate-case-build-marks-the-lesson-its-case-fixes`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-marks-the-lesson-its-case-fixes`
```

### Case 915.3 — The ledger hook holds only an error lesson for its mark

> **given:**
> `rule-ledger-write`: the page of the ledger hook; its Purpose names the hold of a lesson written after a Case.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ledger.py`: `unmarked_lessons` and the docstring of the hold.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the hold.
> **＋** `estimate-ledger-write-lifts`: the other refusals that keep a line out.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: a line refused for its tag.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<kind>][<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> For a `lesson[error]` line, at the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged." The line names no Case, however many decision lines stand before the lesson line.
> **＋** The held line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript; neither way lands it while another refusal of the hook keeps it out, as `estimate-ledger-write-lifts` sets it.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **＋** A `lesson[knowledge]` line is never held for its mark: it lands at its first `Stop`, unless another refusal of the hook keeps it out.
> **－** An unmarked line of either kind never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that stands before every decision line of the session, no line it refuses for its prefix or cannot parse, no line that the ledger of some session already holds, and no line that `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps out.
> **－** A session with no `hi` gets no question; with `stop_hook_active` set and a transcript the hook cannot read, the line lands as it stands.

```then
update:
- slug: rule-ledger-write
  replace:
  - old: It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session
    new: It holds once an `error` lesson line with no `{addressed_by:case N}` written after a decision line of the session
  - old: the line written again with the mark, or unchanged, is written (case 682.1).
    new: the line written again with the mark, or unchanged, is written (case 682.1). It never holds a `knowledge` lesson line for its mark, since such a lesson records a fact and no Case fixes its cause (as set in case 915.3).
  change: the hold of a lesson written after a Case covers only an error lesson
- slug: estimate-ledger-write-asks-for-the-mark-of-a-lesson
  set:
    status: pending
    purpose: Whether the ledger hook holds once an error lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, writes the line written again unless another refusal of the hook keeps it out, and never holds a knowledge lesson line for its mark
  change: the Criterion replaced whole — only an error lesson is held for its mark
```

```tasks
- [x] update `rule-ledger-write`
- [x] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
- [x] `.guppi/guppi/ledger.py`: `unmarked_lessons` leaves out a `knowledge` lesson line by the `kind` that `parse_line` gives, unless a line of its slug carries `{addressed_by:...}`, so that it is still dropped beside that line; the docstring of the hold (case 682.1) says so.
- [x] `.guppi/tests/test_ledger.py`: a test that a `lesson[knowledge]` line after a decision line lands at its first `Stop` with exit 0, and one that a `lesson[knowledge]` line beside a marked line of its slug is dropped.
- [x] `uv run --project .guppi pytest .guppi/tests/test_ledger.py`
- [x] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
```

## Case 916 — A change left to an item with no Case yet waits for that item's Case

> **context:**
> When `case-guppi` builds a Case and finds that part of the work belongs to another Case, it writes a line `**Other Case:**` in its summary, and the main agent sends that other Case back with the change. `vault/wiki/orchestration.md` (`rule-orchestration`, `## Who builds a Case`) and `.claude/agents/case-guppi.md` (`rule-case-build`) set the line only for another Case of the session. In session 1930 the summary of Case 902 carried such a line that named Frontier item C7, which had no Case yet: the person had chosen in a round of 902 to leave the retirement of the defer of `decision-case-885` on `estimate-close-commits` to the Case of C7 (`vault/raw/2026-10-29/1930/cases/note-902.md`). No rule said what to do with it. The handoff of session 1930 says that the main agent showed 902 as it stood and passed the change into the prompt that later dispatched Case 903. The brief adds that the `method` of `estimate-orchestration-signs-items-taken-together` does not say whether such a line is the event it waits for.
>
> The person chose that the main agent keeps the change for the Case of the named item and puts it into the prompt that dispatches that item's `case-guppi`, so the person still chooses the order of the items, as the Frontier passage of `rule-orchestration` sets it: the reply ends with the question which open item is next. When the item ends with no Case of its own, the change goes back to the Case that wrote the line, with no question, and the person agrees or not at its showing, as for a line that names a Case (case 872.3). The two sides fail apart, so the Case splits: 916.1 sets what the main agent does on `rule-orchestration` with a new Estimate, and 916.2 sets the line and the dispatch prompt on `rule-case-build` with a new Estimate. 916.1 also sets the `method` of the two waiting Estimates of `rule-orchestration` to a line that names a Case of the session. That keeps the event each one waits for: the rule of case 781 on a part of a `method` that opens with `after` and names its event before a colon holds for both new texts. A Case taken back whole after it took the change puts its pages into `backlog.md` by the take-back of `rule-orchestration`; this Case adds nothing there.
>
> A Grep of `vault/wiki/` (Decision pages left out by the hook) and `.claude/` for `Other Case` printed `brief.md`, `orchestration.md`, `log.md`, `rules/rule-case-build.md`, `rules/rule-orchestration.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `estimates/estimate-orchestration-signs-items-taken-together.md`, `estimates/estimate-case-build-writes-the-case.md`, `estimates/estimate-case-build-reads-no-sibling-file-mid-send.md`, `insights/insight-subagents-read-a-sibling-mid-flight.md` and `.claude/agents/case-guppi.md`. The Criteria of `estimate-orchestration-shows-the-built-case` and `estimate-orchestration-signs-items-taken-together` speak of the other Case a line names and stay true for a line that names a Case of the session, so they stand, and only their `method` changes. The same holds for the Criterion of `estimate-case-build-writes-the-case`, whose line names another Case of the session, and for `estimate-case-build-reads-no-sibling-file-mid-send` and the insight, which speak of Cases built at the same time. The sentence of `rule-orchestration` on a batch (case 872.5) sends back the other Case a line names, and the description of the summary under `## Who builds a Case` sets the line only for another Case of the session; `/pre-spec` found both narrow (findings 1.3 and 1.4), and 916.1 widens each to the Case of a Frontier item that no Case of the session has built. When the person takes that item up in the same batch as the Case whose line names it, the `case-guppi` of the item is already out and its prompt has gone, so the change goes to that `case-guppi` by `SendMessage`, as the person agreed at `/pre-spec`. Line 23 of the Criterion of `estimate-orchestration-signs-items-taken-together` speaks of the other Case a line names; it stands, since its `method` now waits for a line that names a Case of the session, and the new Estimate checks a line that names an item, in a batch too. The Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` sets which Cases are related by the pages they change or the moment they act at, and what the prompt holds for each (finding 2.3). The new clause names the Case that wrote the line in the prompt, with the change, even where it changes no page the item names. That Criterion only says that such a Case need not stand in the prompt, and its last `－` line holds only when no Case of the session is related. It lists what the prompt holds and forbids nothing more, so it stands, and `estimate-orchestration-passes-a-change-to-an-item-not-built` checks the change in the prompt.
>
> A Grep of `.guppi/tests/` for `orchestration\.md|case-guppi\.md|rule-orchestration|rule-case-build|signs-items-taken-together|shows-the-built-case` printed `test_onward.py`, `test_guppi_package.py` and `test_orchestration.py`. Only `test_orchestration.py` reads a live file, `vault/wiki/orchestration.md`, and it reads only the blocks tagged `showing` and `defer`, which this Case does not touch. A Grep of `.guppi/guppi/` for `Other Case` printed nothing, so no code judges the line. Case 915 of this session changes `rule-orchestration` under `## Writing the ledger lines` and `rule-case-build` after the sentence that ends with case 784; this Case changes other sentences, at the dispatch and the showing of a Case, so the two do not meet. The Glob `vault/wiki/estimates/estimate-*item-not-built*.md` printed nothing, so both new slugs are free. Both files change at the librarian's render after this session, so for the rest of the session the main agent works by the text that stands.

> **problem:**
> No rule says what the main agent does with an `**Other Case:**` line that names a Frontier item not yet built as a Case, so the change it names can be lost, and two Estimates do not say whether such a line is the event they wait for.

> **recommend:**
> - **What should the main agent do with an Other Case line that names a Frontier item not yet built as a Case?**
>   - Recommended: (a) keep the change for that item's Case: show the Case as it stands, and put the change into the prompt that dispatches the item's `case-guppi` when the person takes it up; `case-guppi` may name the item by its Frontier id.
>   - Answer: agreed, (a).
> - **What happens to the change when the named item ends with no Case?**
>   - Recommended: (a) send the change back, with no question, to the `case-guppi` of the Case that wrote the line; that Case is shown again, and the person agrees or not at that showing.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) two parts, each with a new check read at the Retro of this session against the new text in the Spec; the old checks stay as they are.
>   - Answer: agreed, (a).
> - **Should this Case also say what the two waiting checks wait for?**
>   - Recommended: (a) the `method` of `estimate-orchestration-shows-the-built-case` and of `estimate-orchestration-signs-items-taken-together` says that the line names a Case of the session.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes `/pre-spec` proposed: the change for a named item taken up in the same batch goes to that item's `case-guppi` by `SendMessage`; the description of the summary and the batch sentence of `rule-orchestration` cover a line that names such an item; `context` says why `estimate-orchestration-names-related-cases-in-the-dispatch` stands.
>   - Taken: 916.1 gains a `then` line and two `replace` pairs, its clause and the `purpose` of its new Estimate cover the batch, and `context` names the findings and why each Criterion stands.

### Case 916.1 — The main agent keeps the change for the named item, or sends it back

> **given:**
> `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets what the main agent does with an `**Other Case:**` line.
> **＋** `estimate-orchestration-passes-a-change-to-an-item-not-built`: the new check.
> **＋** `estimate-orchestration-shows-the-built-case`: its `method` names the line it waits for.
> **＋** `estimate-orchestration-signs-items-taken-together`: its `method` names the line it waits for.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose item the line names.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the summary of `case-guppi` carries, under the item of a Case, a line `**Other Case:**` that names an item of `raw/<date>/<hi HHMM>/frontier.md` by its id, an item that no Case of the session has built, and the change that item's Case needs.

> **then:**
> The main agent shows the Case as it stands, asks the person no question on the line, and sends no built Case back for it, in a batch too.
> **＋** When the person takes up the named item later, the prompt that dispatches its `case-guppi` names the Case that wrote the line, as a related Case, and the change the line names.
> **＋** When the person took up the named item in the same batch as the Case whose line names it, so that the `case-guppi` of the item is already out, the main agent sends the change to that `case-guppi` by `SendMessage`, and its Case stays in the batch.
> **＋** When the line of the named item in `raw/<date>/<hi HHMM>/frontier.md` closes with no Case of its own — put off, kept, closed as work, or its built Case dropped — the main agent, in the turn that closes it, sends the change by `SendMessage` to the `case-guppi` of the Case that wrote the line, with no question to the person.
> **＋** That Case is shown again when its `case-guppi` answers, in a batch while another Case of the session is out, and the person agrees or not at that showing.
> **－** When the Case that wrote the line is dropped or taken back before the item is taken up, the main agent passes the change to nobody.
> **－** A line `**Other Case:**` that names a Case of the session is handled as before.

```then
create:
- slug: estimate-orchestration-passes-a-change-to-an-item-not-built
  ref: rule-orchestration
  kind: QA
  purpose: Whether the main agent keeps the change that an Other Case line asks of a Frontier item with no Case yet for the prompt that dispatches that item's case-guppi, sends it to that case-guppi by SendMessage when the item is in the same batch, and sends it back to the Case that wrote the line when the item ends with no Case
  method: by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3);
    new: 'the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3); in Plan Mode a line `**Other Case:**` that names, by its id, an item of `frontier.md` that no Case of the session has built sends no built Case back, in a batch too: the Case that carries it is shown as it stands, with no question to the person, and the main agent keeps the change the line names and puts it into the prompt that dispatches the `case-guppi` of that item when the person takes it up later, beside the Case that wrote the line as a related Case, or, when the person took that item up in the same batch, so that its `case-guppi` is already out, sends the change to that `case-guppi` by `SendMessage`; when the line of that item closes with no Case of its own — put off, kept, closed as work, or its built Case dropped — the main agent, in the turn that closes it, sends the change by `SendMessage` to the `case-guppi` of the Case that wrote the line, with no question to the person, and shows that Case again when it answers, in a batch while another Case of the session is out, the person agreeing or not at that showing; and when the Case that wrote the line is dropped or taken back before the item is taken up, the change goes to nobody (as set in case 916.1);'
  - old: and, when its `context` says another Case of the session should change instead, a line `**Other Case:**`,
    new: and, when its `context` says another Case of the session, or the Case of a Frontier item that no Case of the session has built, should change instead, a line `**Other Case:**`,
  - old: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch,
    new: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, and the change for a Frontier item of the batch whose Case is not yet built goes to the `case-guppi` of that item by `SendMessage`,
  change: an Other Case line that names a Frontier item with no Case yet keeps its change for that item's Case, sends it to that item's case-guppi when the item is in the same batch, or sends it back to the Case that wrote it when the item ends with no Case
- slug: estimate-orchestration-shows-the-built-case
  set:
    method: 'by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion; after the first summary of case-guppi in Plan Mode that carries a line Other Case naming a Case of the session under that Render: the replies of the main agent from that summary to the showing of the other Case read against the Criterion, recorded in the estimate line'
  change: the method waits for a line Other Case that names a Case of the session
- slug: estimate-orchestration-signs-items-taken-together
  set:
    method: 'by hand, after the first batch of items taken up together in Plan Mode under the new Render of rule-orchestration in which a summary carries a line Other Case naming a Case of the session: the replies of the main agent from the dispatch of the batch to the reply that acknowledged it read against the Criterion, recorded in the estimate line'
  change: the method waits for a line Other Case that names a Case of the session
```

```tasks
- [x] update `rule-orchestration`
- [x] create `estimate-orchestration-passes-a-change-to-an-item-not-built`
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] update `estimate-orchestration-signs-items-taken-together`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-passes-a-change-to-an-item-not-built`
```

### Case 916.2 — case-guppi names the item not yet built, and its Case takes the change

> **given:**
> `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case and writes its summary.
> **＋** `estimate-case-build-names-an-item-not-built-on-the-other-case-line`: the new check.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose item the line names.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of the Case, whose `context` names the item.

> **when:**
> In Plan Mode `case-guppi`, by `.claude/agents/case-guppi.md`, builds a Case that leaves a change to an item of `raw/<date>/<hi HHMM>/frontier.md` that no Case of the session has built, as a bound the person chose in a round.
> **＋** Or the main agent dispatches `case-guppi` for an item with a prompt that holds a change an `**Other Case:**` line of another Case of the session asks of that item.

> **then:**
> `case-guppi` writes into `context` the Frontier id of that item and what its Case must do, and its summary repeats both on a line `**Other Case:**` under the item of its own Case.
> **＋** Dispatched with such a change, `case-guppi` takes it into the Case of the item, or answers with a round where it opens a fork, and the `context` names the Case that asked it.
> **－** For a clash with another Case of the session, `case-guppi` keeps the form `.claude/agents/case-guppi.md` sets today.

```then
create:
- slug: estimate-case-build-names-an-item-not-built-on-the-other-case-line
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi names a Frontier item with no Case yet, by its id and the change it needs, on the Other Case line of its summary, and takes into the Case of an item the change its prompt carries from such a line
  method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: in Work Mode it asks the person first (cases 637.2, 645.1, 872.3).
    new: in Work Mode it asks the person first (cases 637.2, 645.1, 872.3). Where, in Plan Mode, your Case leaves a change to an item of the Frontier that no Case of the session has built, as a bound the person chose in a round, name in `context` the item by its Frontier id and the change it needs, and again on a line `**Other Case:**` under the item of your Case in the summary that names the item by that id; the main agent keeps the change for the Case of that item, or sends it back to you when the item ends with no Case. Where your prompt holds a change that an `**Other Case:**` line of another Case of the session asks of your item, take it into your Case, or answer with a round where it opens a fork, and name in `context` the Case that asked it (as set in case 916.2).
  change: case-guppi names a Frontier item with no Case yet on the Other Case line, and the Case of that item takes the change its prompt carries
```

```tasks
- [x] update `rule-case-build`
- [x] create `estimate-case-build-names-an-item-not-built-on-the-other-case-line`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-names-an-item-not-built-on-the-other-case-line`
```

## Case 917 — The event log checks name vault/.gitignore

> **context:**
> When a sprint closes, `guppi sprint-close` moves old daily event logs into `vault/archive/`, and git must ignore them there. Since case 893.1 the lines that ignore the logs stand in `vault/.gitignore`, and the root `.gitignore` holds none. `guppi ship` writes `vault/.gitignore` into the clean version: the constant `VAULT_IGNORE` of `.guppi/guppi/ship.py`, which `plan` adds to the files it writes, checked by `test_it_writes_the_lines_that_keep_the_event_logs_out_of_git` in `.guppi/tests/test_ship.py`. So the brief's line that the clean version holds no `.gitignore` and that no module writes one is half wrong: the root `.gitignore` does not ship, but `vault/.gitignore` does. The defect is that two shipped Estimates name a bare `.gitignore`. The `method` of `estimate-sprint-close-moves-old-event-logs` sends the reader to "the line of .gitignore" in the tree, which reads as the root file and finds no such line there. One line of its Criterion and one line of the Criterion of `estimate-event-log-records` name the same bare file. The module docstring of `.guppi/guppi/sprint_close.py` says the same. The rule that governs these texts is the Criterion of `estimate-clean-branch-ships-neutral-texts`: no sentence of the `purpose` or `method` of a shipped Estimate may hold only in the repository of GUPPI. Its last reading listed the Criterion line of `estimate-sprint-close-moves-old-event-logs` among those that do. Both target rules, `rule-sprint-close` and `rule-event-log`, carry `core: true`, so both Estimates ship. The Criterion of `estimate-clean-branch-ships-neutral-texts` stands, since this Case changes texts it judges and not the promise.
>
> The person chose to replace the Criterion of each Estimate whole, with the one line changed to `vault/.gitignore`, and to fix the docstring. The two Estimates fail apart and need different readings, so the Case splits: 917.1 covers the close and 917.2 the event log. Each Estimate goes `pending` and is read at the Retro of this session. Its rule goes `draft` at the librarian's cascade until that reading passes, so `guppi ship` without `--allow-draft` refuses until then. The `method` of `estimate-event-log-records` asked for a `/hi` by hand in plan mode and one outside it, which wait for another session, and the check of this file refused it. The person chose to drop those two readings. The tests `test_plan_mode_hi_writes_the_line` and `test_plan_mode_hi_outside_it_is_refused` of `.guppi/tests/test_event.py` feed made-up `/hi` payloads in plan mode and in each other mode. A live payload with its mode was read once, at the reading the page's Result records, and is not read again. The new `method` keeps the tests and the ignore and timing readings by hand, all at the Retro of this session. The `purpose` of `estimate-sprint-close-moves-old-event-logs` speaks of logs kept outside git and names no file, so it stands. `estimate-event-log-records` has no `purpose` field: a Grep of its page for `^purpose:` printed nothing, and this Case adds none.
>
> A Grep of `vault/wiki/` for `\.gitignore`, with `brief.md` and `log.md` left out, printed `rules/rule-clean-branch.md`, `rules/rule-guppi-package.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-clean-branch-writes-a-clean-copy.md`, `estimates/estimate-event-log-records.md`, `estimates/estimate-guppi-package-runs-from-its-own-folder.md` and `estimates/estimate-sprint-close-moves-old-event-logs.md`. `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy` already name `vault/.gitignore`. `rule-guppi-package` and `estimate-guppi-package-runs-from-its-own-folder` speak of `.guppi/.gitignore`, and the hit in `estimate-clean-branch-ships-neutral-texts` is its Result. All of these stand. The same Grep of `.claude/` printed nothing. A Grep of `.guppi/` for `leaves the moved logs|event-log-records|sprint-close-moves`, with `.venv/` left out, printed only `.guppi/guppi/sprint_close.py`, so no test reads either Estimate page or that docstring. Frontier item C3 of this session lists the Criterion line of `estimate-sprint-close-moves-old-event-logs` among the sentences to rewrite. 917.1 rewrites it, and Case 918, which takes C3, leaves that Estimate out of its rewrite for this reason, in its finished file. Case 918 replaces the Criterion of four other Estimates and names neither Estimate of this Case. In their finished files, Case 913 changes `rule-close` and its report Estimate, Case 915 the ledger hook, `rule-orchestration`, `rule-case-build` and `rule-prespec-onward`, and Case 916 `rule-orchestration` and `rule-case-build`. None of them changes a page or a file of this Case.

> **problem:**
> Two shipped Estimates, and the docstring of the close code, name a bare `.gitignore`. The lines that ignore the event logs stand in `vault/.gitignore`. So a reader of the `method` of `estimate-sprint-close-moves-old-event-logs` opens the root `.gitignore` and finds no such line, in this repository and in a project that installed GUPPI.

> **recommend:**
> - **How the Estimate names the ignore file**
>   - Recommended: (a) replace the Criterion whole and set the method, both naming `vault/.gitignore`; read at the Retro of this session.
>   - Answer: agreed, (a).
> - **The docstring of the close code**
>   - Recommended: (a) name `vault/.gitignore` there too.
>   - Answer: agreed, (a).
> - **The event log Estimate with the same bare name**
>   - Recommended: (a) leave it out of this Case.
>   - Answer: (b), a sub-case replaces the Criterion of `estimate-event-log-records` with `vault/.gitignore`.
> - **When the event log check can be read**
>   - Recommended: (a) drop the two `/hi` readings by hand from the `method`, so that the pytest and the ignore and timing readings all run at the Retro of this session.
>   - Answer: agreed, (a).

### Case 917.1 — The close of a sprint names vault/.gitignore

> **given:**
> `estimate-sprint-close-moves-old-event-logs`: its Criterion is replaced whole and its `method` set.
> **＋** `.guppi/guppi/sprint_close.py`: the close; its module docstring names the ignore file.
> **＋** `.guppi/tests/test_sprint_close.py`: the tests of the close over a made-up vault.
> **＋** `.guppi/guppi/ledger.py`: `session_dir` and `session_event_logs`, which find the session of the run.
> **＋** `vault/.gitignore`: the lines that leave the event logs out of git.
> **＋** `vault/raw/<date>/event_log.md`: a daily event log, beside the session folders of `vault/raw/`.
> **＋** `vault/archive/<id>/<date>/event_log.md`: where an old log goes.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the `method` of a shipped Estimate.

> **when:**
> `uv run --project .guppi guppi sprint-close --sprint <id> --apply` of `.guppi/guppi/sprint_close.py` closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault, and the session of the run is the stamp whose `hi` line `session_dir` of `.guppi/guppi/ledger.py` takes to the newest session folder of `vault/raw/`.

> **then:**
> After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the start date of the session of the run, the first date that `session_event_logs` of `.guppi/guppi/ledger.py` gives for its stamp, moves to `vault/archive/<id>/<date>/event_log.md`.
> **＋** A date folder that the moves leave empty is removed.
> **＋** `vault/.gitignore` leaves out each moved log, so git tracks none.
> **＋** Stdout holds one line per log moved.
> **－** The log of the start date and of each later date stays where it is, since the hooks of that session read them, the start date two or more days before the date of the session folder included.
> **－** With no session folder in `vault/raw/`, or with no stamp or more than one whose `hi` line `session_dir` takes to the newest session folder, no log moves, and stdout holds one line that says why.
> **－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
> **－** A refused close moves no log.

```then
update:
- slug: estimate-sprint-close-moves-old-event-logs
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log; the lines of vault/.gitignore read in the tree at Retro
  change: the Criterion replaced whole — the moved logs are left out of git by vault/.gitignore, and the method reads that file
```

```tasks
- [x] update `estimate-sprint-close-moves-old-event-logs`
- [x] `.guppi/guppi/sprint_close.py`: the module docstring line `` `.gitignore` leaves the moved logs out of git. `` names `vault/.gitignore`.
- [x] read `estimate-sprint-close-moves-old-event-logs`
```

### Case 917.2 — The event log check names vault/.gitignore

> **given:**
> `estimate-event-log-records`: its Criterion is replaced whole and its `method` set.
> **＋** `.guppi/guppi/event.py`: `guppi event`, which writes the event log.
> **＋** `.guppi/guppi/gate.py`: `guppi gate`, which reads the payload of a `Skill` call.
> **＋** `/hi`: the skill that opens a session, whose prompt the hook judges.
> **＋** `raw/<date>/event_log.md`: the daily event log.
> **＋** `vault/.gitignore`: the lines that leave the event logs out of git.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> A session starts, a tool call completes, the person submits a prompt, or the agent calls a skill through `Skill`; `uv run --project .guppi guppi event <name>` and `uv run --project .guppi guppi gate` read the JSON payload through a pipe, its `session_id` the stamp.

> **then:**
> After the start and one tool call, `raw/<date>/event_log.md` carries a `session-start` line with the session's stamp and a `tool` line after it.
> **＋** On `/hi` whose `permission_mode` is `plan`, when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and its `hi:` line on stdout, which names the session's folder; a second `/hi` writes nothing and prints `hi: already recorded`, with the time and the folder; exit 0.
> **＋** On `/hi` whose `permission_mode` is any other value — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` — or is missing or empty, a second `/hi` included: no line, nothing on stdout, exit 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi` again; Claude Code blocks the prompt, and the skill does not run.
> **＋** Any other prompt is silent, and its `permission_mode` is not read: exit 0; an error goes to stderr only, exit 0.
> **＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
> **＋** `git check-ignore` reports the log ignored by `vault/.gitignore`; a hook invocation with piped stdin that refuses nothing exits 0 and finishes under 2 s.

```then
update:
- slug: estimate-event-log-records
  set:
    status: pending
    method: pytest in .guppi/tests/test_event.py and .guppi/tests/test_gate.py with piped JSON payloads against a temp vault; by hand at Retro, git check-ignore on the event log of the day and one hook run through a pipe, timed, both written into the estimate line
  change: the Criterion replaced whole — git check-ignore reports the log ignored by vault/.gitignore; the method drops the /hi readings by hand
```

```tasks
- [x] update `estimate-event-log-records`
- [x] read `estimate-event-log-records`
```

## Case 918 — Four shipped checks hold in any project

> **context:**
> `guppi ship` copies into the clean version each `passed` Estimate whose target page it ships, its Criterion as it stands here (the Purpose of `rule-clean-branch`). The `/hi` reading of `estimate-clean-branch-ships-neutral-texts` in session 1930 listed Criterion sentences that hold only in the repository of GUPPI, for a Case of a later session to rewrite, and the handoff of session 1930 names those that remain. This Case takes Frontier item C3. The Criterion of `estimate-clean-branch-ships-neutral-texts` is the rule that governs these texts: no sentence of the `purpose` or `method` of a shipped Estimate may hold only in the repository of GUPPI, a sentence that states its condition, such as in the repository of GUPPI, holds, and a Criterion sentence on its list fails nothing. That Criterion stands, since this Case changes texts it judges and not its promise. By the `**Other Case:**` line of Case 917, which the main agent passed into the prompt as Case 916 sets it, `estimate-sprint-close-moves-old-event-logs` leaves this item, since Case 917.1 rewrites its line.
>
> A replaced Criterion sets its Estimate `pending`, and the cascade sets its rule `draft` until the reading passes. The person chose to rewrite now only the four whose cost is small. `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` name English, where the Render of `rule-case-build` writes `{{documentation_lang}}`; their new text names it as the language of the repository, the term that the `purpose` of the first and the Criterion of `estimate-clean-branch-ships-neutral-texts` already use. `rule-case-build` already stands `draft` (brief, Flags), and both can be read at the Retro of this session: the first by the Case files of this session against their rounds, since a render of `rule-case-build` came before them, the second by the new Render of `rule-case-build` in the Spec, which Cases 915.2 and 916.2 change. Neither Case changes these two Estimates, and Case 916 says that the Criterion of `estimate-case-build-writes-the-case` stays true for its line, so the lines carried here stand beside their new texts. `estimate-python-utf8-output-intact` names cp1252 in two lines, the code page of the machine GUPPI is built on; its `purpose` and `method` already name the code page of the locale (case 875), and the new text does too. `rule-python-utf8` goes `draft` until the Retro of this session runs one script through the Bash tool. The Purpose of `rule-python-utf8` names cp1252 as a measured fact inside a pointer bracket, and stays true.
>
> `estimate-guppi-package-is-ready-after-the-install` is `pending` and not shipped, but it ships once it passes. Its Criterion of case 912.2 opens its `When` with `guppi ship` and `rule-plugin-install`, which the clean version does not hold, and its `method` names `guppi ship` too. Each now states its condition, in the repository of GUPPI. In the `method` these words stand right after the colon, so that the method still opens with `by hand, after` and names its event, as `waits_for_an_event` of `.guppi/guppi/lint.py` judges a wait (case 781); the wait for the librarian's run of the session that sets the Criterion stands, so the person's install waits for the librarian's run of this session, and an install in this session would read the old text. `rule-guppi-package` already stands `draft`. The four Estimates still under the defer of `decision-case-893.1` on `rule-clean-branch` — `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-ask-query-before-a-create` and `estimate-compact-recall-reloads` — keep their text, as case 908 chose: their rules stand `built` with `core: true`, and their readings wait for events that may not come soon. Frontier item C1 of this session, on `rule-clean-branch`, was put off by the person and closed in `raw/2026-10-29/2341/frontier.md` as `sprint · defer`, with no Case. So the defer of `decision-case-893.1` stands, keeps holding those four, and no Case of this session retires it. The Result of `estimate-clean-branch-ships-neutral-texts` of 2026-10-29 lists five more Estimates that neither this Case nor Case 917.1 rewrites: `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-example-passes-the-check` and `estimate-ratification-case-id-carries-the-sprint`. The ledger of session 1930 holds decision lines of Cases 904.1, 904.3, 908.1 and 908.2 on the first four, made after that reading. By the person's answer at `/pre-spec`, the rewrite of these five is not part of this Case: no status changes, and a line in the handoff of this session leaves them to the next session. Each sub-case replaces the Criterion of the Estimate it rewrites, and that Estimate checks it; each `purpose` speaks of no language, code page or command of GUPPI, so each stands.
>
> A Grep of `vault/wiki/`, `log.md` and `brief.md` left out, for `case-build-records-the-rounds-in-recommend|case-build-writes-the-case|python-utf8-output-intact|guppi-package-is-ready-after-the-install` printed `estimates/estimate-case-build-reads-by-need-and-in-parts.md`, `rules/rule-case-build.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `rules/rule-guppi-package.md`, `rules/rule-python-utf8.md` and `estimates/estimate-skill-grill-me-asks-in-rounds.md`: field `estimates`, History lines and Results, all of which stand. The same Grep of `.claude/` and of `.guppi/` printed nothing. A Grep of the repository for `cp1252`, the session and archive folders, `log.md`, `brief.md` and `.guppi/.venv/` left out, printed `.guppi/tests/test_event.py`, `.guppi/tests/test_ledger.py`, `lessons/lesson-bash-tool-heredoc-escapes-interpreted.md`, `rules/rule-python-utf8.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-context-size-warns-past-the-limit.md`, `.guppi/guppi/cli.py`, `.guppi/guppi/event.py` and `estimates/estimate-python-utf8-output-intact.md`: tests that feed a Windows stdin, a lesson, measured facts and Results, which stand. Of the tests of `.guppi/tests/` that read the live vault, `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `test_ship.py` asserts no line on a shipped Estimate page, and the new texts hold no pointer; `live_pages` of `test_guppi_package.py` serves the search for old commands, `uv run guppi` and `uv run pytest`, which the new texts do not hold.

> **problem:**
> Four checks that ship, or will ship once they pass, hold sentences true only in the repository of GUPPI: two name English as the language of the repository, one names the code page of GUPPI's machine, and one starts from a command and a rule that the clean version does not hold.

> **recommend:**
> - **Which checks does this Case rewrite now?**
>   - Recommended: (a) the four that cost little now — the two case-build checks, the UTF-8 check and the package check; the four put off stay put off.
>   - Answer: agreed, (a).
> - **How does the package check say that it holds only in GUPPI's repository?**
>   - Recommended: (a) open the trigger and the method with "In the repository of GUPPI", and keep the method's wait.
>   - Answer: agreed, (a).
> - **How does the UTF-8 check name the character it prints?**
>   - Recommended: (a) outside the code page of the locale, as the purpose and method say.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, item C1 was put off with no Case, so the defer of `decision-case-893.1` stands and holds the four, and the note to C1 goes.
>   - Taken: the `context` says so, and the summary carries no line `Other Case`.
> - **Change**
>   - Asked: at `/pre-spec`, name the five other Estimates that the last reading listed and leave them to the next session, with no change of status.
>   - Taken: the `context` names the five and says that their rewrite is not part of this Case, and that a line of the handoff leaves them to the next session.

### Case 918.1 — The recommend check names the language by its role

> **given:**
> `estimate-case-build-records-the-rounds-in-recommend`: its Criterion is replaced whole.
> **＋** `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case.
> **＋** `rule-case-protocol`: renders `vault/wiki/case-schema.md`, the form of a Case.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `estimate-case-check-requires-each-question-of-the-rounds`: the check of a question title with no item.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in the language of the repository, both as they stood when the person answered that question.
> **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
> **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
> **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.
> **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

```then
update:
- slug: estimate-case-build-records-the-rounds-in-recommend
  set:
    status: pending
  change: the Criterion replaced whole — the answer stands in the language of the repository, named by its role
```

```tasks
- [x] update `estimate-case-build-records-the-rounds-in-recommend`
- [x] read `estimate-case-build-records-the-rounds-in-recommend`
```

### Case 918.2 — The case-build check names the language by its role

> **given:**
> `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round.
> **＋** `vault/wiki/case-schema.md`: the form of a Case; `vault/wiki/ratification.md`: the form of the ledger lines.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `raw/<date>/<hi HHMM>/cases/note-<N>.md`: the working note of `case-guppi`.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, whose decision lines decide the number of a Case.
> **＋** `.claude/agents/ask-guppi.md`: the vault query run before a `create` without a `ref`.
> **＋** `.claude/settings.json`: the hooks registered on each event.
> **＋** `/pre-spec`: the skill whose findings come back on a Case.
> **＋** `rule-case-check`: the hook that sends findings on the file and on the summary.
> **＋** `rule-spec-reconcile`: the guard of `.guppi/guppi/ratified.py` that writes the file in Plan Mode.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
> **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in the language of the repository, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in the language of the repository in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change under the number of that Case; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
> **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it writes no new file and answers with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it.
> **＋** Where the person chooses a new Case beside it, it builds that behaviour as a new top-level Case in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
> **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
> **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
> **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.
> **＋** `.claude/agents/case-guppi.md` sets `autoCompactWindow: 400000`, so Claude Code compacts the context of `case-guppi` before it reaches 400000 tokens.
> **＋** Before each answer, and first when a message brings the person's answers or a change, `case-guppi` writes `raw/<date>/<hi HHMM>/cases/note-<N>.md` whole by `Write`, N the id of the top-level Case: each question of its rounds by its title with its recommendation and the person's answer, the pages and files it read for the frame, the forks still open, and what is still to do.
> **＋** When its context opens with a summary of earlier work, it reads that note by `Read` before anything else, goes on from what it says, and reads again the pages and files its next step needs.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
> **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
> **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, the file of a new Case it builds beside a ratified Case and its note, and no ledger line.
> **－** It asks no question again whose answer its note holds.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

```then
update:
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — the round and the Case stand in the language of the repository, named by its role
```

```tasks
- [x] update `estimate-case-build-writes-the-case`
- [x] read `estimate-case-build-writes-the-case`
```

### Case 918.3 — The UTF-8 check names the code page of the locale

> **given:**
> `estimate-python-utf8-output-intact`: its Criterion is replaced whole.
> **＋** `rule-python-utf8`: the key `PYTHONUTF8` of the settings.
> **＋** `rule-settings`: renders `.claude/settings.json`.
> **＋** `.claude/settings.json`: the settings, their `env` and their hooks.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> A session starts with `.claude/settings.json` as `uv run --project .guppi guppi render` wrote it from `rule-settings`, and the agent runs a Python script through the Bash tool, with no encoding set in the command, that prints a dash and a character outside the code page of the locale.
> **＋** The hooks of `.claude/settings.json` run in the same session.

> **then:**
> `.claude/settings.json` carries `"PYTHONUTF8": "1"` under `env`, the text of `rule-python-utf8`.
> **＋** The script runs in UTF-8 mode, and the dash reaches the agent in the output of the Bash tool as the dash, not as U+FFFD.
> **＋** The character outside the code page of the locale prints, and the script does not stop at the print.
> **＋** The output of a hook of `.claude/settings.json` reaches the agent as before, its dashes kept.
> **－** The Render of `rule-python-utf8` holds no key other than `PYTHONUTF8`.

```then
update:
- slug: estimate-python-utf8-output-intact
  set:
    status: pending
  change: the Criterion replaced whole — the character lies outside the code page of the locale, not cp1252
```

```tasks
- [x] update `estimate-python-utf8-output-intact`
- [x] read `estimate-python-utf8-output-intact`
```

### Case 918.4 — The install check states that it runs in the repository of GUPPI

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion is replaced whole and its `method` set.
> **＋** `rule-guppi-package`: the package `.guppi/` and its Python environment.
> **＋** `rule-plugin-install`: renders the skill `/guppi:install`.
> **＋** `rule-clean-branch`: `guppi ship`, which writes the clean version.
> **＋** `.guppi/guppi/lint.py`: `waits_for_an_event`, which judges the wait of a `method`.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `.claude/settings.json`: the settings of the project, copied last.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill that opens the first session of the project.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> In the repository of GUPPI, the person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** It copies each file of the install but `.claude/settings.json`, and then runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/`.
> **＋** Once `uv sync` passes, it copies `.claude/settings.json`, and then tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

```then
update:
- slug: estimate-guppi-package-is-ready-after-the-install
  set:
    status: pending
    method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: in the repository of GUPPI, the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person''s answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync'
  change: the Criterion replaced whole and the method set — both state that the install starts in the repository of GUPPI
```

```tasks
- [x] update `estimate-guppi-package-is-ready-after-the-install`
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```
