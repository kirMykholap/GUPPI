<!-- approved 02:33:55 · session 98de6197 -->

# Session 2312 — the sprint plugin: the procedure for a full case-guppi

## Case 896 — The helper keeps a note and goes on after a compaction

> **context:**
> Each answer to a round, each change and each finding goes back to the same `case-guppi` by `SendMessage`, and the helper keeps all it has read and said, so its context only grows. The put-off on `rule-orchestration` says so; its Decision page, `decision-case-884`, gives that text under `## Deferred`, and its `## Problem` concerns the window of a resumed session, not this put-off, which Case 884 carried over from Case 876. Case 895 chose a remedy and a test first: Claude Code compacts the helper by size, the helper keeps a note, and after the compaction it reads the note and goes on. The test ran in Work Mode of session 1907. Its folder `scratchpad/compact-test` of that session's temporary area still stands. A Grep for `"preTokens":\d+` over the transcript `agent-a12be5ab8317687d5.jsonl` printed 72126, 74307 and 75012 on its lines 32, 64 and 92. Its `log.txt` holds `SubagentStop tester a12be5ab8317687d5` at 22:33:19 and 22:34:13, after the compactions, and `PreCompact` and `PostCompact` lines with `None` for the agent type and id and the main transcript path. Its agent file `tester.md` sets `autoCompactWindow: 100000`. So the compaction came below the set size, which fails the first Then line of `estimate-case-build-goes-on-after-a-compaction`; the other lines held (the Result of that page and lesson `lesson-case-build-subagent-compaction-fires-below-its-window`).
> The documentation read by WebFetch. https://code.claude.com/docs/en/sub-agents says that `autoCompactWindow` in the frontmatter of one subagent lowers its window to a count from `100000` to `1000000`, that `CLAUDE_CODE_AUTO_COMPACT_WINDOW` overrides it, and that a subagent transcript logs a `compact_boundary` record with `preTokens`. https://code.claude.com/docs/en/model-config says that a model with a native 1M window compacts at about 967K tokens by default, and gives no rule for how far below a set window the compaction comes, so where the helper compacts with a window of 400000 is not checked; Q3 left the choice to the person, and the new check of Case 896.3 records the real point. https://code.claude.com/docs/en/context-window says that after a compaction Claude Code reads again up to five of the files read or edited, the most recently changed first, and that a file over 5,000 tokens comes back as a path only; so the note is written last before each answer and kept short. The same pages say nothing of a `SessionStart` hook for a subagent's compaction, and the test logged no `SessionStart`; whether `guppi recall` of `rule-compact-recall` fires there is not checked, and this Case sets nothing at that moment.
> The code read. In `.guppi/guppi/ratified.py`, `guard_refusal` lets `case-guppi` write any file under a `cases/` folder of a session folder, judged by `is_case_file` of `.guppi/guppi/casecheck.py`, and refuses it any other file; `held_number` judges only a file whose name `case_number` reads, `case-<N>.md`, and passes any other; `builder_file` names any file under `cases/`, and `guard` writes it by `builder_write` and stops the call. So the guard already writes `note-<N>.md`, and its behaviour does not change. The `## How it works` of `rule-spec-reconcile` names only `case-<N>.md` as a file the hook writes itself, and the refusal of `guard_refusal` says that `case-guppi` writes the file of its Case alone; Case 896.2 adds a sentence on any other file under `cases/` to that page and rewords the refusal. `test_ratified.py` asserts only the words `outside cases/` of that refusal, and the new wording keeps them. `estimate-spec-reconcile-refuses-an-edit-of-the-plan` stands: its `＋` line on a call of `case-guppi` on a file under such a folder covers any file there, the note included. `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` stands: it does not judge a file whose name gives no id. In `.guppi/guppi/casecheck.py`, `subagent` checks each file that `written_case_files` gives, and `written_case_files` takes each file under `cases/` that a `Write`, `Edit` or `MultiEdit` call of the subagent names anywhere in its transcript; a note there would be checked as a Case. Case 896.4 makes it keep only a file whose name `case_number` reads. That function reads `CASE_NAME`, which is `CASE_FILE` of `.guppi/guppi/caseid.py`, the pattern the guard's `held_number` and the file ids of `caseid.py` read too, so the task adds no second judgment. `cases_out` and `built_after` of `.guppi/guppi/onward.py` read only files that match the glob `case-*.md`. That glob and `case_number` part on a name such as `case-x.md` with no valid id, which no writer gives. Both pass over `note-<N>.md`, and the test of Case 896.4 runs both over that name. A Grep for `written_case_files\(` over `.guppi/guppi/` printed `casecheck.py` alone, its definition and its one call in `subagent`.
> The texts read. In `rule-case-build`, three sentences of the Render become false: the file of the Case as the one file the harness lets the helper write, the guard as refusing any other file, and the list of the files it writes. Case 896.2 rewrites them. The `－` line of `estimate-case-build-writes-the-case` that lists the files the helper writes becomes false too, so Case 896.2 replaces that Criterion whole, written under `sections`, since the `when` and `then` of Case 896.2 cover only the note. The first `then` line of `estimate-case-check-sends-back-a-faulty-case` says the check takes each file under `cases/`, so Case 896.4 replaces that Criterion whole: that line names `case-<N>.md` and `case_number`, and a `－` line covers the note. It also sets that Estimate's `method` to the tests alone, since its old `method` waited for a later session. Case 896.1 writes the new `method` of `estimate-case-build-goes-on-after-a-compaction` by the procedure of the test. The one past run it reads stands in a bracket of its own, since `guppi ship` writes a passed Estimate into the clean copy, and `estimate-clean-branch-ships-neutral-texts` forbids a `method` there that holds only in this repository. A Grep for `no file but|its Case alone|one file this harness|writes only|only file` over `vault/wiki/` with the glob `!{log.md,brief.md}` printed six files: `rules/rule-case-build.md` and `estimates/estimate-case-build-writes-the-case.md`, which this Case changes; `estimates/estimate-backlog-renders.md`, on another script; `estimates/estimate-case-build-judges-by-the-state-at-the-moment.md`, on the forms of an update; `rules/rule-materialize.md`, in a History line; and `rules/rule-spec-reconcile.md`, whose Purpose says that the main agent writes only the title line of the plan. Those four stand. `estimate-case-build-reads-by-need-and-in-parts` stands: the new text tells the helper to read again after a compaction only what its next step needs, by that Estimate's own rules. No other Estimate of `rule-case-build` or `rule-orchestration` speaks of a compaction. Many Estimates of `rule-case-check`, such as `estimate-case-check-takes-a-case-built-again-from-its-file`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent` and `estimate-case-check-refuses-a-letter-outside-the-script`, open with the check reading a file under `cases/`, `case-<N>.md` where they name one. Each stays true, since the check still reads those files.
> The tests. A Grep for `case-guppi\.md|rule-case-build|rule-case-check\.md|orchestration\.md` over `.guppi/tests/` printed `test_casecheck.py` and `test_guppi_package.py`, in docstrings, and `test_onward.py` and `test_orchestration.py`. `test_orchestration.py` reads the live `vault/wiki/orchestration.md`, whose Render this Case does not change, since the `update` of `rule-orchestration` carries only `change`. `test_onward.py` names the file in its assertions only. No test reads `.claude/agents/case-guppi.md`.
> The notes of the check. Case 896.1 carries the old lines of its Criterion that the check names in new words: the second `When` line now says that the files total more than 100000 tokens; the `SubagentStop` line names the test helper; and the line on the interim file also counts the file that Claude Code puts back, as the Result of the page records. Its first `Then` line is the line this Case replaces. The `then` lines of Case 896.3 that share words with Case 896.1 speak of `case-guppi` at a size of 400000, not of the test helper at 100000, so they are two promises.
> The put-off is taken up: the decision line of Case 896.2 on `rule-orchestration` carries `{supersedes:case 884}`, the one Case in its `deferred_by`. The rule `rule-case-protocol`, rendered as `case-schema.md`, governs the forms of each update of an Estimate here, and `rule-one-judgment-one-implementation` the judgment of the name of a Case file, which Case 896.4 reuses.

> **problem:**
> The helper that builds a Case keeps everything in its context and grows towards about 967 000 tokens. The test of the remedy showed that the compaction comes below the set size, so the check of the test stands failed.

> **recommend:**
> - **Do we build the remedy for the helper's memory now?**
>   - Recommended: (a) build it now.
>   - Answer: agreed, (a).
> - **How is the failed check set right?**
>   - Recommended: (a) rewrite its first line and read it again from the saved files.
>   - Answer: agreed, (a).
> - **At what size does the helper compact?**
>   - Recommended: no single answer, since how far below the set size the compaction comes was not checked; (a), a size of 400 000, is the one that keeps the limit of 400 000 whatever that share is.
>   - Answer: agreed; read as (a), the option the main agent named after the round as the one that keeps the limit.
> - **When does the helper write its working note?**
>   - Recommended: (a) always, after each round, each answer it gets and each change.
>   - Answer: agreed, (a).
> - **Where does the working note live?**
>   - Recommended: (a) beside the Case file, as `cases/note-<N>.md`.
>   - Answer: agreed, (a).
> - **How do we check that the real helper goes on after a compaction?**
>   - Recommended: (a) a new check, read at the first real compaction of `case-guppi`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes of the findings of `/pre-spec` as proposed.
>   - Taken: the new `method` of `estimate-case-build-goes-on-after-a-compaction` describes the test by its procedure, and the one past run stands in a bracket of its own. Case 896.2 adds to `rule-spec-reconcile` the sentence that the hook writes any other file of `case-guppi` under `cases/`, and rewords the refusal of the guard; `context` names `estimate-spec-reconcile-refuses-an-edit-of-the-plan`, which stands. Case 896.4 reuses `case_number` in place of a new judgment of the note, and its `then` and the new Criterion no longer claim that a call that wrote only the note counts as no file. The claim in `context` on the other Estimates of `rule-case-check` is narrowed.

### Case 896.1 — The test check states where the compaction came

> **given:**
> `estimate-case-build-goes-on-after-a-compaction`: its Criterion is replaced whole.
> **＋** `scratchpad/compact-test` of the temporary area of session 1907: the test folder, its agent file of the test helper and its `log.txt`.
> **＋** `~/.claude/projects/`: the folder of the saved transcripts, the test helper's among them.

> **when:**
> The main agent runs `claude -p` in a test folder outside the repository, whose agent file of a test helper sets `autoCompactWindow: 100000` and tells it to read its interim file again after a compaction, and whose hooks log each `SubagentStop` and `PostCompact` event.
> **＋** The first run starts the test helper, has it read text files and write its interim file; a second run with `--resume` sends it more files, past 100000 tokens in all; a third run with `--resume` asks it to go on.

> **then:**
> The transcript of the test helper under `~/.claude/projects/` holds a `compact_boundary` record whose `preTokens` is below 100000: the helper compacts before it reaches the size its agent file sets.
> **＋** That transcript file keeps the lines of the helper before the `compact_boundary` record.
> **＋** The log of the test folder holds a `SubagentStop` line of the test helper after the compaction.
> **＋** After the compaction the interim file stands in the context of the test helper again, read by its own `Read` call or put back by Claude Code, and the helper goes on from what it says.
> **－** The size of 100000 tokens binds the test helper alone, through its agent file, and no size is set in the shell of `claude -p`.
> **－** No file of the repository changes by the test.

```then
update:
- slug: estimate-case-build-goes-on-after-a-compaction
  set:
    status: pending
    purpose: Whether a subagent with its own autoCompactWindow compacts before it reaches that size, keeps its earlier lines in its transcript file, still fires SubagentStop after the compaction, and goes on from its interim file, as the procedure for a full case-guppi rests on
    method: 'by hand, in the Work Mode of the session that replaces this Criterion: the transcript of the test helper under ~/.claude/projects/ and the log of the test folder, as a run of the test by claude -p left them, read against the Criterion and recorded in the estimate line (as set in case 896.1, which reads the saved files of the run of session 1907 with no new run)'
  change: the Criterion replaced whole — the compaction comes below the set size, as the test showed
```

```tasks
- [x] update `estimate-case-build-goes-on-after-a-compaction`
- [x] read `estimate-case-build-goes-on-after-a-compaction`
```

### Case 896.2 — case-guppi compacts before 400 000 tokens and keeps a note

> **given:**
> `rule-case-build`: the page whose Render is `.claude/agents/case-guppi.md`.
> **＋** `.claude/agents/case-guppi.md`: the agent file of `case-guppi`.
> **＋** `raw/<date>/<hi HHMM>/cases/note-<N>.md`: the working note of `case-guppi`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: the page of the put-off this Case takes up.
> **＋** `rule-spec-reconcile`: the guard that writes the files of `case-guppi` under `cases/`.
> **＋** `.guppi/guppi/ratified.py`: the guard, its refusal of a file outside `cases/`.

> **when:**
> The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, or sends it a message by `SendMessage`.

> **then:**
> `.claude/agents/case-guppi.md` sets `autoCompactWindow: 400000`, so Claude Code compacts the context of `case-guppi` before it reaches 400000 tokens.
> **＋** Before each answer, and first when a message brings the person's answers or a change, `case-guppi` writes `raw/<date>/<hi HHMM>/cases/note-<N>.md` whole by `Write`, N the id of the top-level Case: each question of its rounds by its title with its recommendation and the person's answer, the pages and files it read for the frame, the forks still open, and what is still to do.
> **＋** When its context opens with a summary of earlier work, it reads that note by `Read` before anything else, goes on from what it says, and reads again the pages and files its next step needs.
> **－** It asks no question again whose answer its note holds.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'permissionMode: auto'
    new: |-
      permissionMode: auto
      autoCompactWindow: 400000
  - old: You decide nothing the person has not decided.
    new: |-
      You decide nothing the person has not decided.

      Claude Code compacts your context before it reaches the size that `autoCompactWindow` sets and keeps only a summary of it, so keep a working note in `raw/<date>/<hi HHMM>/cases/note-<N>.md`, N the id of the top-level Case, in {{documentation_lang}} (as set in case 896.2). Write it whole by `Write` before each answer you give, and first of all when a message brings the person's answers or a change, with four lists: each question of your rounds by its title as the round wrote it, with your recommendation and the person's answer; the pages and files you read for the frame, by path; the forks still open; and what is still to do (as set in case 896.2). Keep it short, since after a compaction Claude Code puts back whole only a recently changed file of up to 5 000 tokens (as set in case 896.2). When your context opens with a summary of earlier work, a compaction has happened: before anything else read the note by `Read` and go on from what it says, read again each page and file your next step needs, whole or in parts as the next paragraph sets for each kind of text, and ask no question again whose answer the note holds (as set in case 896.2).
  - old: 'the file of your Case is the one file this harness lets you write: its guard writes the text of your `Write` or `Edit` into it itself and stops your call with a line that says the file is written, which is no failure and no call to make again, and you read the file by `Read` before your next `Edit` of it; the guard refuses any other file (as set in case 894.3).'
    new: 'the files under `cases/` of the session folder, the file of your Case and your note among them, are the files this harness lets you write: its guard writes the text of your `Write` or `Edit` into the file itself and stops your call with a line that says the file is written, which is no failure and no call to make again, and you read the file by `Read` before your next `Edit` of it; the guard refuses a file outside a `cases/` folder of a session folder (as set in cases 894.3 and 896.2).'
  - old: Write no file but the file of your Case, the file you leave behind under an earlier number of the same Case included, and the file of a new Case you build beside a ratified Case (case 725.1), and no ledger line.
    new: Write no file but the file of your Case, the file you leave behind under an earlier number of the same Case included, the file of a new Case you build beside a ratified Case and your note, and no ledger line (as set in cases 725.1 and 896.2).
  change: case-guppi compacts before 400 000 tokens and keeps a working note it reads again after a compaction (case 896.2)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
    purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary, keeps a working note it reads again after a compaction, empties the file of a Case it drops, and undoes a change the person dropped on a ratified Case
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
      **＋** `.claude/agents/case-guppi.md` sets `autoCompactWindow: 400000`, so Claude Code compacts the context of `case-guppi` before it reaches 400000 tokens.
      **＋** Before each answer, and first when a message brings the person's answers or a change, `case-guppi` writes `raw/<date>/<hi HHMM>/cases/note-<N>.md` whole by `Write`, N the id of the top-level Case: each question of its rounds by its title with its recommendation and the person's answer, the pages and files it read for the frame, the forks still open, and what is still to do.
      **＋** When its context opens with a summary of earlier work, it reads that note by `Read` before anything else, goes on from what it says, and reads again the pages and files its next step needs.
      **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
      **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
      **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
      **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
      **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, the file of a new Case it builds beside a ratified Case and its note, and no ledger line.
      **－** It asks no question again whose answer its note holds.
      **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
  change: the Criterion replaced whole — case-guppi compacts before 400 000 tokens and keeps a working note it reads again after a compaction
- slug: rule-orchestration
  change: 'the put-off on the growing context of case-guppi taken up: it compacts before 400 000 tokens and keeps a working note (case 896.2)'
- slug: rule-spec-reconcile
  replace:
  - old: so the call does not run and Claude Code asks nothing (as set in case 894.1).
    new: so the call does not run and Claude Code asks nothing (as set in case 894.1). A call of `case-guppi` on any other file under `cases/`, such as its working note `note-<N>.md`, whose name gives no number, holds no number and is written by the hook the same way (as set in case 896.2).
  change: the hook writes any file of case-guppi under cases/, its working note included (case 896.2)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-the-case`
- [x] update `rule-orchestration`
- [x] update `rule-spec-reconcile`
- [x] `.guppi/guppi/ratified.py`: the refusal of `guard_refusal` for a file of `case-guppi` outside `cases/` says that `case-guppi` writes only under `cases/` of a session folder, the words `outside cases/` kept (case 896.2).
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-the-case`
```

### Case 896.3 — The real helper goes on after a compaction

> **given:**
> `estimate-case-build-goes-on-after-a-live-compaction`: the new check of the real helper.
> **＋** `rule-case-build`: the page of `case-guppi`, which the check targets.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `raw/<date>/<hi HHMM>/cases/note-<N>.md`: the working note of `case-guppi`.
> **＋** `rule-case-check`: the check at the end of each answer, which reads the rounds from the transcript.
> **＋** `~/.claude/projects/`: the folder of the saved transcripts.

> **when:**
> `case-guppi`, run by `.claude/agents/case-guppi.md` with `autoCompactWindow: 400000`, compacts while it builds a Case in a working session.

> **then:**
> Its transcript under `~/.claude/projects/` holds a `compact_boundary` record whose `preTokens` is below 400000.
> **＋** That transcript keeps the lines of `case-guppi` before the record.
> **＋** After the compaction `raw/<date>/<hi HHMM>/cases/note-<N>.md` stands in its context again, read by its own `Read` call or put back by Claude Code, before its next round, Case or summary.
> **＋** The Case it then writes holds an item of `recommend` for each question of its rounds before and after the compaction, and the check of `rule-case-check` passes it.

```then
create:
- slug: estimate-case-build-goes-on-after-a-live-compaction
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi compacts below 400000 tokens, keeps its earlier lines, reads its working note again and builds a Case that passes the check
  method: 'by hand, after the first compaction of a case-guppi in a working session: its transcript under ~/.claude/projects/, its note under cases/ and the event log of the session read against the Criterion, the preTokens of the compact_boundary record in the estimate line'
  tags:
  - harness
  - case-build
```

```tasks
- [x] create `estimate-case-build-goes-on-after-a-live-compaction`
- [ ] read `estimate-case-build-goes-on-after-a-live-compaction`
```

### Case 896.4 — The end-of-answer check reads no note as a Case

> **given:**
> `.guppi/guppi/casecheck.py`: the check on `SubagentStop`, its `written_case_files` and its docstring.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of that check.
> **＋** `rule-case-check`: the page of the check.
> **＋** `estimate-case-check-sends-back-a-faulty-case`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/cases/note-<N>.md`: the working note of `case-guppi`.
> **＋** `.guppi/guppi/onward.py`: the hook that finds the Cases still out by the glob `case-*.md`, which the new test runs over the note.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after a `Write` or `Edit` call on `raw/<date>/<hi HHMM>/cases/note-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` takes the files under `cases/` that the calls of the subagent in its transcript name.

> **then:**
> The check takes as a file of a Case only a file whose name `case_number` of `.guppi/guppi/casecheck.py` reads, `case-<N>.md`.
> **＋** It reads no Case in `note-<N>.md`, stores nothing for it and sends nothing back for it.
> **＋** A file `case-<N>.md` that the calls of the subagent name is checked and stored as before.
> **－** A transcript whose calls name no file `case-<N>.md`, though they name the note, is read as one that names no file of a Case.

```then
update:
- slug: rule-case-check
  replace:
  - old: which the hook checks whole when the agent stops and stores, and a file that differs from its stored text is not shown or written into the Spec (cases 452.1, 645.2).
    new: which the hook checks whole when the agent stops and stores, and a file that differs from its stored text is not shown or written into the Spec (cases 452.1, 645.2). The hook takes as a file of a Case only a file named `case-<N>.md` under `cases/`, so the working note `note-<N>.md` that `case-guppi` keeps beside its Case is not checked, stored or sent back (as set in case 896.4).
  change: the check takes only a file case-<N>.md under cases/ as a file of a Case, so the working note of case-guppi is no Case (case 896.4)
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k subagent
  sections:
    Criterion: |-
      When:
      `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

      Then:
      `uv run --project .guppi guppi casecheck --subagent` takes each file `case-<N>.md` under the `cases/` folder of a session folder, judged by `is_case_file` and `case_number` of `.guppi/guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
      **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
      **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `.guppi/guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `.guppi/guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
      **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
      **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook does not write that file.
      **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
      **＋** Until a reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such file and whose newest output holds a Case heading is read the old way: that output is checked and stored as the Cases of a file are, and with no finding the hook writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the whole file when it holds the top-level Case, the section of each sub-case otherwise. A Case of a later session removes this path.
      **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
      **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
      **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.
      **－** A file of another name under `cases/`, such as the working note `note-<N>.md` of `case-guppi`, is no such file: it is not read as a Case, stored or sent back, and a transcript whose calls name no file `case-<N>.md`, though they name the note, is read as one that names no such file.
  change: the Criterion replaced whole — only a file case-<N>.md under cases/ is a file of a Case, so the working note of case-guppi is no Case; the method is the tests alone
```

```tasks
- [x] update `rule-case-check`
- [x] update `estimate-case-check-sends-back-a-faulty-case`
- [x] `.guppi/guppi/casecheck.py`: `written_case_files` keeps only a file whose name `case_number` reads; the module docstring under "The file" and the docstring of `written_case_files` say so (case 896.4).
- [x] `.guppi/tests/test_casecheck.py`: two tests whose names hold `subagent`. In the first, `case-guppi` wrote `note-<N>.md` and `case-<N>.md`, and only the Case file is checked and stored. In the second, `case-guppi` wrote only `note-<N>.md` and answered with a round, and nothing is stored or sent back for the note. In the same test, `cases_out` of `.guppi/guppi/onward.py` counts no Case out for the note, so both readers pass over `note-<N>.md` alike.
- [x] read `estimate-case-check-sends-back-a-faulty-case`
```

## Case 897 — The clean copy names no skill it lacks and no moment of a past session

> **context:**
> `guppi ship` builds the clean copy of GUPPI that other projects install, and `estimate-clean-branch-ships-neutral-texts` promises that no shipped rule, entity, `CLAUDE.md`, or `purpose` or `method` of a shipped Estimate holds a sentence true only in the repository of GUPPI. Its reading in this session, taken by the main agent by its `method` over a copy built by `guppi ship --allow-draft` into the scratchpad folder `ship-c4`, failed again. The main cause is that the copy leaves out the skills `/merge-main` and `/pr-review`: a Glob of `.claude/skills/*/SKILL.md` over that copy printed eleven skills, `box`, `carry`, `grill-me`, `handoff`, `hi`, `pre-spec`, `retro`, `sprint-close`, `sprint-open`, `wait-what` and `work`. `rule-skill-merge-main` and `rule-skill-pr-review` carry no `core`; Case 822.8 took it off while they are `draft` (their History in `log.md`), and a `＋` line of `estimate-clean-branch-refuses-a-draft-core-page` says the copy holds neither. A Grep `merge-main|pr-review` over that copy printed the shipped sentences that still name them: `rule-skill-sprint-open` (step 3, the bullet of an author who is not the owner, and the paragraph after step 4), `rule-skill-sprint-close` (step 1), `rule-where-to-stop` (condition 6) and `rule-documentation` (the first sentence of the librarian's frame), the files they render, the `purpose` and the Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, and a comment of `.gitattributes`, which stands, since the Criterion covers the rules, the entities and `CLAUDE.md` alone. The other failures read at their source in that copy: `rule-case-protocol` justifies the bracket rule by `guppi ship`, a command the copy does not hold; the `method` of `estimate-ledger-write-keeps-the-window-past-a-later-resume` checks by hand the stamp `44ee5004` and the folder `raw/2026-10-14/1907`; the `method` of `estimate-case-build-reads-the-code-it-states` opens with a reading at the Retro of the session that set it.
> The person chose to fix the failures alone (Q1): the doubtful sentences of the reading and its list of Criterion sentences stand for later Cases (Q6). The missing-skills sentences of `/sprint-open`, `/sprint-close` and the stops depend on the skill file standing in the project (Q2), so they hold in GUPPI and in a new project alike. The new text of 897.1 drops no step: where `.claude/skills/merge-main/SKILL.md` stands, the opening Case writes the merge line as before. `estimate-skill-sprint-open-asks-the-opening-questions` says the prompt asks that the opening Case write the close line as the last item of the last milestone of the new sprint page; 897.1 keeps the close line last, so that Criterion stands. The new paragraph after step 4 gives the reason the opening Case merges no `main` by step 1 of `/sprint-close`, which closes no sprint whose branch does not hold `main`. In 897.2 step 1 of `/sprint-close` tells the person to bring the branch up to `main`, in the words the Criterion of `estimate-skill-sprint-close-leads-the-closing-session` already uses, so that Criterion stands. The last `－` line of the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` leaves room for a stop that a skill the project holds sets, and `estimate-guppi-repository-stops-in-the-merge-tasks` binds the repository of GUPPI, which holds both skills, so both stand.
> For the librarian's frame the person first chose the bracket form that `rule-vault-layout`, `rule-page-generation` and the row `Librarian` of `entity-glossary` use (Q8). `/pre-spec` then found that in the copy those brackets go, so the copy's `rule-vault-layout`, `rule-page-generation` and librarian frame give no writer to what a merge of `main` writes into `vault/wiki/`, while 897.2 tells a project without `/merge-main` to bring its branch up to `main`. The premise of Q8, that the copy holds no sentence on a merge it cannot run, no longer held. The person chose to widen the exception to any merge of `main` into a branch, with no bracket and no skill name, in the librarian frame, `rule-vault-layout` and `rule-page-generation` (Change), and in the row `Librarian` of `entity-glossary` (Q10), so the four shipped texts agree; each keeps its pointer in a bracket at the end of its sentence. The copy of `.gitattributes` holds `vault/wiki/log.md merge=union` and `vault/wiki/tags.md merge=union`, so the sentence on the lines git joins holds there. `rule-documentation` carries `deferred_by: [decision-case-839]`, whose `## Deferred` says the librarian's close does not commit `plugin/skills/install/SKILL.md` that the render writes. The person chose to take that put-off up and close it (Q7, and again at `/pre-spec`): the frame now commits `vault` and each file of `guppi render --paths`, its line `git add vault $(uv run --project .guppi guppi render --paths)`. Its check, `estimate-close-commits`, stands `pending`, unread since 2026-09-29, with its `method` waiting for the librarian's run of a later session and `deferred_by: [decision-case-885]`, so the put-off closes on the text of the frame, not on a reading. 897.3 carries `{supersedes:case 839}`. `rule-page-generation` carries `deferred_by: [decision-case-793]`, whose `## Deferred` asks for an `update` that removes a section. The person chose to take it up and put it off again with the same text (Q9), as Case 893.1 did for `rule-clean-branch`: 897.3 carries `{supersedes:case 793}` and a `defer` of `rule-page-generation`. A Grep `only writer|merge` over the Estimates of `rule-vault-layout`, `rule-page-generation` and `entity-glossary` (`estimate-vault-layout-holds`, `estimate-generate-*` and `estimate-glossary-*`) printed no file, so no Criterion speaks of who writes `wiki/`.
> The bracket rule keeps its reason, said where it holds (Q3). The two methods lose their part tied to a past moment and keep the part that checks the same promise (Q4); both Estimates keep their Criterion and `passed`. The `method` of `estimate-clean-branch-ships-neutral-texts` waits for the librarian's run of this session (Q5), since the new texts land only there; its Criterion and `failed` stand until that reading. That Estimate checks 897.2 to 897.5, which change wording only; `estimate-case-protocol-loaded` checks the render of `case-schema.md`, and an `update` of a Render touches no Estimate of the live reading. 897.1 changes what the opening Case writes, so it replaces the Criterion of `estimate-skill-sprint-open-merges-the-closed-sprint-branch` whole, written under `sections`, and sets its `purpose` and `method` anew. Two lines of its old Criterion are not carried word for word, as the check notes: the line on the merge line, which becomes the close line last and the merge line before it only where the skill stands, and the line of an author who is not the owner, which gains where `/pr-review` stands; every other line is carried. The check also notes that the first `then` line of 897.2 shares words with two lines of 897.1: 897.1 speaks of what the opening Case of `/sprint-open` writes into the sprint page, 897.2 of what step 1 of `/sprint-close` tells the person, two skills and two checks, so they are two promises.
> Every new text with a pointer on a page with `core: true` keeps it in a bracket at the end of its sentence, and no new text of an Estimate holds a pointer, so `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `.guppi/tests/test_ship.py` stays green. A Grep `case-schema\.md|librarian-guppi\.md|sprint-open|sprint-close|where-to-stop|merge-main` over `.guppi/tests/` printed 8 files: `test_case_schema.py`, which reads the example block of `case-schema.md` that this Case does not touch, and `test_gate.py`, `test_onward.py`, `test_recall.py`, `test_render.py`, `test_sprint.py`, `test_sprint_close.py` and `test_ledger.py`, which name the files in strings or read made-up copies. A Grep `merge-main|pr-review` over `vault/wiki/` with the glob `!{log.md,brief.md}` printed 22 files. This Case changes `where-to-stop.md`, `glossary.md`, `entity-glossary.md`, the rules `rule-where-to-stop`, `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-documentation`, `rule-vault-layout` and `rule-page-generation`, and `estimate-skill-sprint-open-merges-the-closed-sprint-branch`. Of the rest, `rule-git-context` holds the names in a bracket with a pointer and in History; `rule-plan-mode` in `children` and History; `rule-skill-merge-main`, `rule-skill-pr-review` and their Estimates, `estimate-guppi-repository-stops-in-the-merge-tasks` and `estimate-clean-branch-refuses-a-draft-core-page` are not shipped. `estimate-where-to-stop-stops-only-on-its-conditions` and `estimate-skill-sprint-close-leads-the-closing-session` stand as said above. `estimate-clean-branch-ships-neutral-texts` holds them in its Result, and the lesson `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes` is a record. A Grep `merge-main|pr-review` over `.claude/` printed `skills/sprint-open/SKILL.md`, `skills/sprint-close/SKILL.md` and `agents/librarian-guppi.md`, which this Case renders again, and `skills/merge-main/SKILL.md` and `skills/pr-review/SKILL.md`, which are not shipped. A Grep `` removes that bracket|merge of `main` into `` over `vault/wiki/` with the same glob printed `case-schema.md`, `rules/rule-case-protocol.md`, `rules/rule-skill-sprint-open.md` and `estimates/estimate-skill-sprint-open-merges-the-closed-sprint-branch.md`, each changed here. The file of Case 896 of this session, read whole after its build ended, updates `rule-case-build`, `rule-orchestration`, `rule-spec-reconcile`, `rule-case-check`, `estimate-case-build-goes-on-after-a-compaction`, `estimate-case-build-writes-the-case` and `estimate-case-check-sends-back-a-faulty-case`, and creates `estimate-case-build-goes-on-after-a-live-compaction`. It names no page of this Case, `estimate-case-build-reads-the-code-it-states` included. That Estimate has `rule-case-build` as its target, and 897.5 sets only its `method`. The new `method` waits for the first `/pre-spec` after a Render of `rule-case-build` that holds the sentence its Criterion checks. The new Render of 896.2 keeps that sentence, so the two do not clash. No sentence of 896 sets what happens at a moment that this Case sets.

> **problem:**
> The clean copy fails its check of neutral texts again: shipped rules send a new project to two skills the copy does not hold, the schema justifies a rule by a command the copy lacks, and two shipped methods wait for a moment of GUPPI's past.

> **recommend:**
> - **How much does this Case fix now?**
>   - Recommended: (a) the failures only.
>   - Answer: agreed, (a).
> - **How is the missing-skills group fixed?**
>   - Recommended: (b) make each sentence depend on the skill being there.
>   - Answer: agreed, (b).
> - **How is the reason for the bracket rule reworded?**
>   - Recommended: (a) say where the reason holds.
>   - Answer: agreed, (a).
> - **How are the two methods fixed that wait for a past moment?**
>   - Recommended: (a) cut the part tied to the past.
>   - Answer: agreed, (a).
> - **When is the check read again?**
>   - Recommended: (a) wait for the librarian's run of this session.
>   - Answer: agreed, (a).
> - **Is the Criterion list rewritten now?**
>   - Recommended: (a) leave it for a later Case.
>   - Answer: agreed, (a).
> - **The librarian's frame carries an open put-off: what happens to it?**
>   - Recommended: (a) take up the put-off and close it.
>   - Answer: (a).
> - **How is the merge exception in the librarian's frame worded?**
>   - Recommended: (b) put the exception in a bracket with its pointer, as the two other rules do.
>   - Answer: agreed, (b).
> - **`rule-page-generation` carries a put-off of its own: what happens to it?**
>   - Recommended: (a) take up the put-off and put it off again with the same text.
>   - Answer: agreed, (a).
> - **Does the row `Librarian` of the glossary follow the three rules?**
>   - Recommended: (a) widen the row the same way.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, widen the merge exception to any merge of `main` in the librarian frame, `rule-vault-layout` and `rule-page-generation`, with no bracket and no skill name, so that the copy's texts agree, since 897.2 tells a project without `/merge-main` to bring its branch up to `main`.
>   - Taken: 897.3 rewords the three rules that way and gains the updates of `rule-vault-layout` and `rule-page-generation`; the wording of Q8 is replaced.
> - **Change**
>   - Asked: at `/pre-spec`, close the put-off of `rule-documentation` all the same, and say plainly that `estimate-close-commits` stands `pending` and put off.
>   - Taken: 897.3 keeps `{supersedes:case 839}`, and `context` says so.

### Case 897.1 — The opening Case names `/merge-main` only where the skill stands

> **given:**
> `rule-skill-sprint-open`: the page whose Render is `.claude/skills/sprint-open/SKILL.md`.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill that opens a sprint.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: its Criterion is replaced whole.
> **＋** `.claude/skills/merge-main/SKILL.md` and `.claude/skills/pr-review/SKILL.md`: the skill files whose presence the text checks.
> **＋** `rule-skill-sprint-close` and `/sprint-close`: the skill the close line starts, which closes no sprint whose branch does not hold `main`.
> **＋** `entity-sprint-<id>`: the page of the new sprint, whose last milestone takes the lines.

> **when:**
> The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint.

> **then:**
> The opening Case writes the close line of `/sprint-close` as the last item of the last milestone of `entity-sprint-<id>`.
> **＋** Where `.claude/skills/merge-main/SKILL.md` stands in the project, it writes the merge line of `/merge-main` just before that close line.
> **＋** The tasks of an author who is not the owner name `/pr-review` as the way the owner merges only where `.claude/skills/pr-review/SKILL.md` stands.
> **－** Where `.claude/skills/merge-main/SKILL.md` does not stand, the opening Case writes no line that names `/merge-main`.

```then
update:
- slug: rule-skill-sprint-open
  replace:
  - old: 3. Write into the same prompt that the opening Case writes, as the last two items of the last milestone of the page, the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own`` and then the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that `/merge-main` runs before the close (case 789.1) and the session that closes the sprint starts `/sprint-close` from the close line.
    new: 3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from the close line. Where `.claude/skills/merge-main/SKILL.md` stands in the project, write that the opening Case puts the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own`` just before the close line, so that `/merge-main` runs before the close (as set in case 789.1).
  - old: so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges the pull request by `/pr-review`.
    new: so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges the pull request, by `/pr-review` where the project holds `.claude/skills/pr-review/SKILL.md`.
  - old: 'The opening Case does not merge `main` into the closed branch: `/merge-main` did so before the close (case 789.1).'
    new: 'The opening Case does not merge `main` into the closed branch: `/sprint-close` closes no sprint whose branch does not hold `main`, so `main` was merged into it before the close (as set in case 789.1).'
  change: the opening Case writes the merge line of /merge-main and names /pr-review only where the skill stands in the project (case 897.1)
- slug: estimate-skill-sprint-open-merges-the-closed-sprint-branch
  set:
    status: pending
    purpose: Whether /sprint-open has the opening Case write the close line last, with the /merge-main line just before it only where the project holds that skill, push the closed sprint's branch and open its pull request into main after the person's word, merge it with a merge commit after its checks pass when the person is the owner, and move the work to a branch named by the new sprint, as the first tasks of Work Mode, with a stop on a refusal and no git task on main
    method: 'by hand: the Render of rule-skill-sprint-open, in .claude/skills/sprint-open/SKILL.md or, before the render writes that file, in the Spec that changes it, read against the Criterion'
  sections:
    Criterion: |-
      When:
      The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, and dispatches `case-guppi` for the opening Case of the next sprint; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

      Then:
      The prompt of the call names the branch that `/hi` printed under `Branch:` from `.claude/skills/hi/SKILL.md`, and whether the person is the owner of the repository: the login that `gh api user --jq .login` prints is the one that `gh repo view --json owner --jq .owner.login` prints.
      **＋** The opening Case writes the line ``- the close of `<id>` — `/sprint-close`, a session of its own`` as the last item of the last milestone of `entity-sprint-<id>`.
      **＋** Where `.claude/skills/merge-main/SKILL.md` stands in the project, the opening Case writes just before that close line the line ``- the merge of `main` into `<id>` — `/merge-main`, a session of its own``.
      **＋** When that branch is not `main` and the person is the owner, the opening Case holds as its first tasks, in this order, one task that opens with `stop:` and runs `git push -u origin <branch>`, `gh pr create --base main --fill`, `gh pr checks <branch> --watch` and `gh pr merge <branch> --merge`; then `git fetch origin`, `git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint.
      **＋** When that branch is not `main` and the person is not the owner, the opening Case holds as its first tasks one task that opens with `stop:` and runs `git push -u origin <branch>` and, when `gh pr view <branch>` shows no open pull request, `gh pr create --base main --fill`; then `git switch -c <id>` and `git branch -d <branch>`, so that the branch `<id>` starts from the closed branch and keeps its work until the owner merges it, by `/pr-review` where the project holds `.claude/skills/pr-review/SKILL.md`.
      **＋** Work Mode runs these tasks before any other task of the Spec, stops before the task that opens with `stop:`, on the fourth condition of `vault/wiki/where-to-stop.md`, runs it after the person's word, and runs the rest of the Spec on the branch `<id>`.
      **－** Where `.claude/skills/merge-main/SKILL.md` does not stand, the opening Case writes no line that names `/merge-main`.
      **－** The owner's pull request is merged only after its checks pass, with a merge commit and never with `--admin`, and no Case reviews it: each of its changes was ratified in its own session.
      **－** The opening Case does not merge `main` into the closed branch.
      **－** When a `git` or `gh` command of these tasks refuses, among them `gh pr checks --watch` on a red check and `gh pr merge` on a pull request that cannot be merged, the agent stops on the sixth condition of `vault/wiki/where-to-stop.md`, shows what stopped it, and goes on from where it stopped after the person's answer.
      **－** When that branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it.
      **－** The opening Case puts no question on the merge or the branch to the person.
  change: the Criterion replaced whole — the /merge-main line only where the project holds that skill, and /pr-review named the same way
```

```tasks
- [x] update `rule-skill-sprint-open`
- [x] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/sprint-open/SKILL.md`
- [x] read `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
```

### Case 897.2 — The closing session and the stops name the merge skills only where they stand

> **given:**
> `rule-skill-sprint-close`: the page whose Render is `.claude/skills/sprint-close/SKILL.md`.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill that leads the closing session.
> **＋** `rule-where-to-stop`: the page whose Render is `vault/wiki/where-to-stop.md`.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which the run stops.
> **＋** `.claude/skills/merge-main/SKILL.md` and `.claude/skills/pr-review/SKILL.md`: the skill files whose presence the text checks.

> **when:**
> Someone reads `.claude/skills/sprint-close/SKILL.md` and `vault/wiki/where-to-stop.md`, in the repository of GUPPI or in a project that holds neither `.claude/skills/merge-main/SKILL.md` nor `.claude/skills/pr-review/SKILL.md`.

> **then:**
> On a branch that does not hold `main`, step 1 of `/sprint-close` tells the person to bring the branch up to `main` first, in a session of its own, and names `/merge-main` as the way only where `.claude/skills/merge-main/SKILL.md` stands.
> **＋** The sixth condition of `vault/wiki/where-to-stop.md` stops on a refusal in the merge tasks of the opening Case of a sprint, and on a refusal or an unsettled conflict in the merge tasks of `/pr-review` and `/merge-main` only where the project holds the skill.
> **－** In the repository of GUPPI, which holds both skills, the closing session and the stops behave as before.

```then
update:
- slug: rule-skill-sprint-close
  replace:
  - old: tell the person to run `/merge-main` in a session of its own first, and stop the skill here (case 791).
    new: tell the person to bring the branch up to `main` first, in a session of its own, by `/merge-main` where `.claude/skills/merge-main/SKILL.md` stands, and stop the skill here (as set in case 791).
  change: step 1 names /merge-main only where the project holds that skill (case 897.2)
- slug: rule-where-to-stop
  replace:
  - old: 'or a `git` or `gh` command of the merge tasks of the opening Case of a sprint, of the merge task of a review Case of `/pr-review`, or of the tasks of a merge Case of `/merge-main` refuses, or the merge of a merge Case leaves in conflict a file that the merge Case does not settle:'
    new: 'or a `git` or `gh` command of the merge tasks of the opening Case of a sprint refuses; or, where the project holds `.claude/skills/pr-review/SKILL.md` or `.claude/skills/merge-main/SKILL.md`, a `git` or `gh` command of the merge task of a review Case of `/pr-review`, or of the tasks of a merge Case of `/merge-main`, refuses, or the merge of a merge Case leaves in conflict a file that the merge Case does not settle:'
  change: condition 6 names the merge tasks of /pr-review and /merge-main only where the project holds the skill (case 897.2)
```

```tasks
- [x] update `rule-skill-sprint-close`
- [x] update `rule-where-to-stop`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/where-to-stop.md`
```

### Case 897.3 — Any merge of `main` keeps its share of the wiki in every shipped text

> **given:**
> `rule-documentation`: the page whose Render is `.claude/agents/librarian-guppi.md`, and the put-off it carries.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian.
> **＋** `rule-vault-layout` and `rule-page-generation`: the rules of who writes `vault/wiki/`; the second carries a put-off.
> **＋** `entity-glossary` and `vault/wiki/glossary.md`: the row `Librarian` and its render.
> **＋** `.gitattributes`: the `merge=union` lines of `log.md` and `tags.md`.
> **＋** `estimate-close-commits`: the check of the commit of each rendered file.
> **＋** `/merge-main`: the skill the old texts named.

> **when:**
> Someone reads, in the repository of GUPPI or in the clean copy, `.claude/agents/librarian-guppi.md`, `rule-vault-layout`, `rule-page-generation` and the row `Librarian` of `vault/wiki/glossary.md`.

> **then:**
> Each of them says that `vault/wiki/` takes, besides its one writer, what a merge of `main` into a branch writes: the joined text of a page that both sides changed, written in Work Mode, and the lines of `log.md` and `tags.md` that git joins.
> **＋** The librarian frame still says that the librarian writes only through the scripts it names, and that the header of `tags.md` above its table is not its either.
> **－** None of them names `/merge-main` or holds the exception to the repository of GUPPI, so the copy keeps the exception as this repository holds it.

```then
update:
- slug: rule-documentation
  replace:
  - old: You are the only writer to `vault/wiki/` but for what a merge of `main` by `/merge-main` writes — the joined text of a conflicted page, written in Work Mode, and the lines of `log.md` and `tags.md` that git joins (case 790) — and you write only through the scripts named below.
    new: 'You are the only writer to `vault/wiki/` but for what a merge of `main` into a branch writes: the joined text of a conflicted page, written in Work Mode, and the lines of `log.md` and `tags.md` that git joins (as set in case 790). You write only through the scripts named below.'
  change: the merge exception covers any merge of main into a branch, with no skill named; the put-off on the commit of the rendered files taken up and closed, since the close commits each file the render writes (case 897.3)
- slug: rule-vault-layout
  replace:
  - old: 'No file of `wiki/` is written by hand but the header of `tags.md` above its table (in the repository of GUPPI also what a merge of `main` by `/merge-main` writes: the joined text of a page that both a branch and `main` changed, which the merge Case signs and Work Mode writes into the page, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes`, case 790).'
    new: 'No file of `wiki/` is written by hand but the header of `tags.md` above its table and what a merge of `main` into a branch writes: the joined text of a page that both a branch and `main` changed, which a Case signs and Work Mode writes into the page, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes` (as set in case 790).'
  change: the merge exception covers any merge of main into a branch, with no skill named (case 897.3)
- slug: rule-page-generation
  replace:
  - old: 'The script is the only writer to `wiki/` (in the repository of GUPPI but for what a merge of `main` by `/merge-main` writes: the joined text of a page that both a branch and `main` changed, which the merge Case signs and Work Mode writes, the script then writing the History line and the status that the Case sets, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes`, case 790).'
    new: 'The script is the only writer to `wiki/` but for what a merge of `main` into a branch writes: the joined text of a page that both a branch and `main` changed, which a Case signs and Work Mode writes, the script then writing the History line and the status that the Case sets, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes` (as set in case 790).'
  change: the merge exception covers any merge of main into a branch, with no skill named; the put-off on the removal of a section taken up and put off again (case 897.3)
- slug: entity-glossary
  replace:
  - old: 'the only writer to `wiki/` but for the header of `tags.md`, which a one-off task by hand that a Case names changes (and in the repository of GUPPI for what a merge of `main` by `/merge-main` writes: the joined text of a conflicted page, and the lines of `log.md` and `tags.md` that git joins, case 790);'
    new: 'the only writer to `wiki/` but for the header of `tags.md`, which a one-off task by hand that a Case names changes, and for what a merge of `main` into a branch writes: the joined text of a conflicted page, and the lines of `log.md` and `tags.md` that git joins (as set in case 790);'
  change: 'Librarian: the merge exception covers any merge of main into a branch, with no skill named (case 897.3)'
defer:
- slug: rule-page-generation
  type: rule
  purpose: An update of a page can remove a section, heading and text, so that a Leaf loses its How it works section at its next touch by guppi generate and not by hand; put off in the loop after the findings of /pre-spec, and put off again in session 2312, when the merge exception of the page was widened
```

```tasks
- [x] update `rule-documentation`
- [x] update `rule-vault-layout`
- [x] update `rule-page-generation`
- [x] defer `rule-page-generation`
- [x] update `entity-glossary`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run --project .guppi guppi glossary`
```

### Case 897.4 — The schema says where the reason of the bracket rule holds

> **given:**
> `rule-case-protocol`: the page whose Render is `vault/wiki/case-schema.md`.
> **＋** `vault/wiki/case-schema.md`: the form of a Case.
> **＋** `/pre-spec`: the check that reports a pointer outside its bracket.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, in the repository of GUPPI or in a project that installed the clean copy.

> **then:**
> The rule that a pointer in the new text of a page with `core: true` stands in a bracket of its own gives as its reason that, in the repository of GUPPI, `guppi ship` removes that bracket whole from the clean version.
> **－** The rule and the finding of `/pre-spec` on a pointer outside such a bracket stay as they are.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: since `guppi ship` removes that bracket whole from the clean version and the sentence must read whole without it
    new: since, in the repository of GUPPI, `guppi ship` removes that bracket whole from the clean version and the sentence must read whole without it
  change: the reason of the bracket rule says that guppi ship runs in the repository of GUPPI (case 897.4)
```

```tasks
- [x] update `rule-case-protocol`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
```

### Case 897.5 — Two shipped methods wait for no past moment

> **given:**
> `estimate-ledger-write-keeps-the-window-past-a-later-resume`: its `method` is set anew.
> **＋** `estimate-case-build-reads-the-code-it-states`: its `method` is set anew.
> **＋** `.guppi/tests/test_ledger.py`: the tests the first `method` keeps.
> **＋** `rule-case-build`: the rule whose Render the second `method` waits on.
> **＋** `/pre-spec`: the check whose findings the second `method` reads.

> **when:**
> Someone reads the `method` of `estimate-ledger-write-keeps-the-window-past-a-later-resume` and of `estimate-case-build-reads-the-code-it-states`, in the repository of GUPPI or in the clean copy.

> **then:**
> The `method` of the first runs the tests of `.guppi/tests/test_ledger.py` alone and names no stamp or folder of a session.
> **＋** The `method` of the second waits for the first `/pre-spec` after the Render of `rule-case-build` that sets its Criterion, and names no Retro of a past session.
> **－** The Criterion and the status of both Estimates stay as they are.

```then
update:
- slug: estimate-ledger-write-keeps-the-window-past-a-later-resume
  set:
    method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k later_date
  change: the method keeps the tests alone; the check by hand on a past session of GUPPI is gone
- slug: estimate-case-build-reads-the-code-it-states
  set:
    method: 'by hand, after the first /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from the Render of rule-case-build that sets this Criterion: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the function it read, the count in the estimate line'
  change: the method waits for the first /pre-spec after the Render; the reading at the Retro of a past session is gone
```

```tasks
- [x] update `estimate-ledger-write-keeps-the-window-past-a-later-resume`
- [x] update `estimate-case-build-reads-the-code-it-states`
```

### Case 897.6 — The neutral texts are read after this session's librarian

> **given:**
> `estimate-clean-branch-ships-neutral-texts`: its `method` is set anew; its Criterion stands.
> **＋** `rule-clean-branch`: the rule of the clean version.

> **when:**
> The main agent takes the reading of `estimate-clean-branch-ships-neutral-texts` by its `method`.

> **then:**
> The reading waits for the librarian's run of session 2312, so that the clean version it builds holds the new texts of this Case.
> **－** The Criterion and the `failed` status of the Estimate stand until that reading.

```then
update:
- slug: estimate-clean-branch-ships-neutral-texts
  set:
    method: 'by hand, after the librarian''s run of session 2312, with a tag prod-x.y.z in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and each sentence of the pages and the files it wrote read whole against the Criterion, never found by a keyword search, each sentence of the Criterion of a shipped Estimate that holds only in the repository of GUPPI listed in the estimate line'
  change: read again after the texts of case 897 land; the method waits for the librarian's run of session 2312
```

```tasks
- [x] update `estimate-clean-branch-ships-neutral-texts`
```
