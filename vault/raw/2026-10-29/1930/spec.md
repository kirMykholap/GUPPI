<!-- approved 22:19:24 · session 7f200512 -->

# Session 1930 — the items of the brief of 0327

## Case 902 — The stale defer of the defer check leaves the backlog

> **context:**
> When the person puts a check off, the page of the check gets `deferred_by`, which names the Decision page of that defer, and `guppi backlog` lists every live page with `deferred_by`. A later Case clears a defer only when it supersedes the old Decision and also names the page on a decision line of its own, as `rule-case-protocol` sets it (case 467.3). A page the later Case does not name keeps the defer and stays on the list. The cascade of `guppi generate` archives a superseded Decision page (case 104.1), and `guppi cleanup` moves it under `vault/archive/`. Case 900.2 superseded `decision-case-885` and named only `estimate-clean-branch-writes-the-session-files`, so `estimate-close-commits` and `estimate-spec-write-writes-a-defer` kept the defer while the Decision page went to `vault/archive/plugin/2026-10-29/0327/decisions/`. The brief calls this a defect, but the code did what its rules set: `clear_deferred_by` and `decision` of `.guppi/guppi/generate.py` clear only the targets the superseding Case names, `archived_by_cascade` archives each superseded Decision, and `find` reaches a page under `vault/archive/`, so a later Case can still take the defer up; for an earlier page that stands `archived`, `decision` keeps it `archived` and clears the targets the new Case names (case 683). A Grep of `deferred_by: \[.*decision-case-(885|891)` over `vault/wiki/` printed `estimate-close-commits.md` and `estimate-spec-write-writes-a-defer.md`. `estimate-spec-write-writes-a-defer` also names `decision-case-891`, which the brief does not mention; a Glob found that page under `vault/archive/plugin/2026-10-28/1907/decisions/`, superseded by Case 893.2. Both of its defers waited for the by-hand reading of a short-form defer that the person asks for. That reading was taken at the Retro of session 0118, and the page has stood `passed` since 2026-10-26, so both defers are stale. This Case takes up both defers on that page with an `update` that carries `change` alone. `materialize.py` writes such an item as a History line only: it lifts no Criterion and sets no status (case 588.2). This Case leaves the defer of `estimate-close-commits` to Case 903.1, which replaces the Criterion, `purpose` and `method` of that page and no part this Case changes. Its ratified line in the session's ledger names that page and carries `{supersedes:case 885}`, so the same run of `generate` clears that defer too. `decision-case-885` then takes both Cases into its `superseded_by`. No new Estimate is created. `estimate-generate-writes-the-decision-page`, `passed` on 2026-10-26, already checks this behaviour: its Criterion says that a `supersedes` of an earlier page that stands `archived` keeps that page archived and removes its slug from the `deferred_by` of each target that the superseding Case names. Its Criterion stands, since this Case changes no code.

> **problem:**
> `estimate-spec-write-writes-a-defer` passed its reading, but it stays on the backlog list. The two Decisions that put it off are archived and were never taken up for it.

> **recommend:**
> - **What this item fixes**
>   - Recommended: (a) no code change: take up the open defers, since `generate` already clears a defer from an archived Decision for the pages that the superseding Case names.
>   - Answer: agreed, (a).
> - **Which of the two checks this Case takes up**
>   - Recommended: (a) `estimate-spec-write-writes-a-defer` only, with a History line and both defers superseded; the defer of `estimate-close-commits` is retired by the Case that rewords its `method`.
>   - Answer: agreed, (a).

> **given:**
> `estimate-spec-write-writes-a-defer`: the check whose defers this Case takes up.
> **＋** `decision-case-885`: an archived Decision that put the check off.
> **＋** `decision-case-891`: an archived Decision that put the check off.
> **＋** `.guppi/guppi/generate.py`: clears a defer for the pages the superseding Case names.
> **＋** `vault/wiki/backlog.md`: the list of put-off items that `guppi backlog` writes.
> **＋** `rule-case-protocol`: sets how a Case takes up a defer.

> **when:**
> `uv run --project .guppi guppi generate` reads the decision line of this Case. The line names `estimate-spec-write-writes-a-defer` and supersedes `decision-case-885` and `decision-case-891`.
> **＋** `uv run --project .guppi guppi backlog` writes `vault/wiki/backlog.md` after it.

> **then:**
> `estimate-spec-write-writes-a-defer` carries no `deferred_by`. Its status, `method` and Criterion stay as they are.
> **＋** `decision-case-885` and `decision-case-891` stay `archived` in the folders where they stand, and each takes this Case into its `superseded_by`.
> **＋** `vault/wiki/backlog.md` no longer lists `estimate-spec-write-writes-a-defer`.

```then
update:
- slug: estimate-spec-write-writes-a-defer
  change: 'the defers of decision-case-885 and decision-case-891 taken up: the by-hand reading they waited for passed on 2026-10-26'
```

```tasks
- [ ] update `estimate-spec-write-writes-a-defer`
```

## Case 903 — The close check waits for a kind of run, and the report gets a check of its own

> **context:**
> `estimate-close-commits` checks that the librarian's run ends in one separate commit of `vault/` and the rendered files, leaves no rendered file modified or untracked, and returns a report of twenty lines or fewer. It is `pending`. Its `method` waits for the librarian's run of "the next session" that holds "the new Render" of `rule-close`. That moment belongs to one past session of GUPPI. The Criterion of `estimate-clean-branch-ships-neutral-texts` refuses a `method` of a shipped Estimate that waits for a moment of a past session of GUPPI, and accepts one that waits for a kind of moment that comes again in any project. `ships` of `.guppi/guppi/ship.py` ships an Estimate only when it stands `passed` and its target is a page with `core: true`, as `rule-close` is, so the `method` would be read once this page passes. A second fault blocks the reading. The `method` reads the librarian's report in the transcript of the session of the run, and `rule-skill-hi` sets that `/hi` reads no transcript of an earlier session (case 670.5). `decision-case-885` put the page off for that reason, and `lesson-brief-lists-transcript-readings-under-work` records the same stall. `/handoff` dispatches the librarian and shows its report to the person unchanged, as `.claude/skills/handoff/SKILL.md` sets it. In a session that `/box` runs, `/handoff` dispatches nothing, and step 6 of `.claude/skills/box/SKILL.md` does the same instead. Nothing in the vault keeps the report. The `method` passage of `rule-estimates-schema` sets that a reading names its moment by its kind, and that any such moment after the render counts. Its passage on the single Estimate sets that a line with a test or a reading of its own is split off. So Case 903.1 replaces the Criterion of `estimate-close-commits` without the report line, which leaves it on purpose since Case 903.2 carries that promise, sets its `purpose` and `method` anew, and waits for a librarian's run whose `.claude/agents/librarian-guppi.md` already holds the Render of `rule-close` when the run starts. The librarian loads that file when its run starts, and the render rewrites it during the run, so a run that only renders a change still follows the old text. Case 903.2 creates `estimate-close-reports-in-twenty-lines` for the report, read by the person's answer. I read `tied_to_a_one_off_moment`, `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment` and `check_unread` of `.guppi/guppi/lint.py` against both new `method` texts. Neither holds "first" before "after the render". Each opens a part with "by hand, after" and names its event before a colon, so `waits_for_an_event` accepts it. `check_unread` gives no finding for a `pending` page with such a `method`. The decision line of 903.1 carries `{supersedes:case 885}`, as Case 902 asked in its Other Case line. `case-schema.md` sets that a defer is cleared from each page the superseding Case names. The Criterion of `estimate-generate-writes-the-decision-page` sets the same for an earlier page that stands `archived`, as `decision-case-885` does, so that mark removes `decision-case-885` from the `deferred_by` of `estimate-close-commits`. Case 902 leaves this defer to Case 903.1 and no longer says that `estimate-close-commits` keeps it. It changes only `estimate-spec-write-writes-a-defer`, which this Case does not touch, and it says that `decision-case-885` takes both Cases into its `superseded_by`. A Grep of `estimate-close-commits` over `vault/wiki/`, with `decisions/` left out, printed `brief.md`, `backlog.md`, `log.md`, `rules/rule-close.md` and `lessons/lesson-brief-lists-transcript-readings-under-work.md`. `rule-close` lists the page in `estimates`, which `generate` fills. The lesson records a past fact and stands. `backlog.md` is written again by `guppi backlog`. A Glob `vault/**/estimate-close-report*.md` printed nothing, so the new slug is free. No new Estimate checks the new wording. `estimate-clean-branch-ships-neutral-texts` already checks each `method` of a shipped Estimate by this yardstick, and its Criterion stands, since this Case changes no rule of what ships.

> **problem:**
> The `method` of `estimate-close-commits` waits for a moment that comes once in GUPPI only. It also reads the librarian's report in a transcript that `/hi` may not open, so the reading is never taken.

> **recommend:**
> - **Where the librarian's report is read**
>   - Recommended: (b) split the report into its own check, answered by the person after `/box` shows the report; `estimate-close-commits` keeps what `git log` and `git status` show.
>   - Answer: agreed, (b).
> - **Which librarian's run the reading waits for**
>   - Recommended: (a) a run that starts with the current text of `rule-close` in its file.
>   - Answer: agreed, (a).
> - **What checks the new wording**
>   - Recommended: (a) no new check: `estimate-clean-branch-ships-neutral-texts` covers it.
>   - Answer: agreed, (a).

### Case 903.1 — The close commit is read after a run that holds the Render of rule-close

> **given:**
> `estimate-close-commits`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-close`: its Render sets the commit at the close.
> **＋** `.claude/agents/librarian-guppi.md`: the file that holds the Render of `rule-close`.
> **＋** `vault/`: the folder the close commit takes.
> **＋** `.guppi/guppi/render.py`: writes the rendered files and prints their list.
> **＋** `.guppi/tests/test_render.py`: the tests of `guppi render --paths`.
> **＋** `plugin/skills/install/SKILL.md`: the file that `rule-plugin-install` renders.
> **＋** `decision-case-885`: the archived Decision that put the check off.
> **＋** `rule-estimates-schema`: sets how a `method` names its moment.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, and writes nothing.
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
    purpose: The librarian's run ends in one separate commit of vault and each file the render writes, with no rendered file left modified or untracked
    method: 'uv run --project .guppi pytest .guppi/tests/test_render.py -k paths; by hand, after a librarian''s run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked'
  change: the Criterion replaced whole without the report, which estimate-close-reports-in-twenty-lines checks; the method waits for a librarian's run that holds the Render of rule-close, and reads no transcript
```

```tasks
- [ ] update `estimate-close-commits`
- [ ] read `estimate-close-commits`
```

### Case 903.2 — The person reads the librarian's report

> **given:**
> `estimate-close-reports-in-twenty-lines`: the new check of the librarian's report.
> **＋** `rule-close`: its Render sets the report.
> **＋** `.claude/agents/librarian-guppi.md`: the file that holds the Render of `rule-close`.
> **＋** `.claude/skills/handoff/SKILL.md`: dispatches the librarian and shows its report to the person.
> **＋** `.claude/skills/box/SKILL.md`: does the same in a session that `/box` runs.
> **＋** `rule-skill-hi`: `/hi` reads no transcript of an earlier session.
> **＋** `rule-estimates-schema`: sets that a line with a reading of its own is split off.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
> **＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

> **then:**
> The report reaches the person with the counts, the flags and the lint total.
> **＋** The report holds twenty lines or fewer.

```then
create:
- slug: estimate-close-reports-in-twenty-lines
  ref: rule-close
  kind: QA
  purpose: Whether the librarian's report, as /handoff or /box shows it, gives the counts, the flags and the lint total in twenty lines or fewer
  method: 'by hand, after a librarian''s run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: the person''s answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave the counts, the flags and the lint total in twenty lines or fewer'
  tags:
  - harness
  - workflow
  - librarian
```

```tasks
- [ ] create `estimate-close-reports-in-twenty-lines`
- [ ] read `estimate-close-reports-in-twenty-lines`
```

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

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
  change: the Criterion replaced whole — the check reads only the files case-<N>.md that case-guppi wrote; the old path of the answer text is gone
- slug: rule-spec-reconcile
  change: How it works removed by hand, a one-off, its facts in the docstring of .guppi/guppi/ratified.py; the clause on the old path of rule-case-check dropped
```

```tasks
- [ ] update `estimate-case-check-sends-back-a-faulty-case`
- [ ] update `rule-spec-reconcile`
- [x] `.guppi/guppi/casecheck.py`: `subagent` reads only the files `case-<N>.md` the subagent wrote; the old path, `answer_of` and `write_case_files` are removed where nothing else calls them, and the docstring of the module, of `subagent` and of `is_fact` follow.
- [x] `.guppi/tests/test_casecheck.py`: the helper `answer` writes a Case text into its file with a `Write` call in the transcript when no transcript is given; each test of the old path is removed or asserts that nothing is stored.
- [x] by hand, in Work Mode: `## How it works` of `vault/wiki/rules/rule-spec-reconcile.md` removed; each fact of it that the docstring of `.guppi/guppi/ratified.py` does not hold moved there, the clause on the old path of `rule-case-check` not carried.
- [ ] read `estimate-case-check-sends-back-a-faulty-case`
```

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

```then
update:
- slug: estimate-case-check-sends-back-a-ratified-case-in-another-shape
  set:
    status: pending
  change: the Criterion replaced whole — a file of sub-cases alone gets no finding, in place of an answer on the old path
```

```tasks
- [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
```

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

```then
update:
- slug: estimate-case-example-passes-the-check
  set:
    status: pending
  change: the Criterion replaced whole — the test reads case-example.md alone, and a missing file fails both tests with its name
- slug: rule-case-example
  set:
    implementation_ref:
    - .guppi/tests/test_case_schema.py
  change: implementation_ref names the test of the example
```

```tasks
- [ ] update `estimate-case-example-passes-the-check`
- [ ] update `rule-case-example`
- [x] `.guppi/tests/test_case_schema.py`: `example` reads `vault/wiki/case-example.md` alone; a missing file fails both tests by `pytest.fail` with a message that names it; the docstring of the module and of `example` follow, and `SCHEMA` leaves where nothing else reads it.
- [ ] read `estimate-case-example-passes-the-check`
```

## Case 908 — Three checks name the transcripts folder and the chat language by role

> **context:**
> `guppi ship` writes each `passed` Estimate whose target page it ships into the clean version of GUPPI, with its Criterion as it stands here. The reading of `estimate-clean-branch-ships-neutral-texts` at the `/hi` of this session (ledger line 1, `passed`) lists Criterion sentences that hold only in the repository of GUPPI, for a Case of a later session to rewrite. Six of them stand under the defer of `decision-case-893.1` on `rule-clean-branch`, which waited because a replaced Criterion sets its Estimate `pending`, and the cascade of `generate` sets its rule `built` only once every Estimate passes (`vault/wiki/rules/schema.yaml`, the `status` field); while a rule with `core: true` stands `draft`, `guppi ship <folder>` writes nothing to `prod`, as `rule-clean-branch` sets it. The brief names a seventh Estimate, `estimate-glossary-terms-defined`; this session's reading does not list it, so its Criterion stands. The person chose to rewrite now only the two whose cost is small. `estimate-permissions` names the transcripts folder of GUPPI, `c--PROJECTS-GUPPI`, in four sentences; its `method` waits for a Case file that `case-guppi` writes in Plan Mode, which this session holds, so the Retro of this session can read it and `rule-permissions` stands `draft` only until then. The Purpose of `rule-permissions` says that the clean version brings the read rules of GUPPI's folder until the setup Case of `rule-morph` sets the project's own, so the new sentences name the folder that the Render of `rule-permissions` names. `estimate-permissions` carries no `purpose`, which `vault/wiki/estimates/schema.yaml` keeps optional, and its `method` names the folder by role already, so both stand. `estimate-orchestration-forwards-a-discussion-question` says that the answer is shown translated into Russian; `rule-orchestration` already stands `draft`. Its `method` waited for "a later session", which `vault/wiki/case-schema.md` does not accept for a `method` (cases 670.4, 781), and it read the evidence in a transcript, which `/hi` may not open, since `.claude/skills/hi/SKILL.md` says that `/hi` reads no transcript of an earlier session (case 670.5). So, by the person's answer to a finding of `/pre-spec`, Case 908.2 sets it to be read at the Retro of a session that holds such a question, from the tool calls of that session. I read `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment`, `tied_to_a_one_off_moment` and `check_unread` of `.guppi/guppi/lint.py`: the new `method` names no later session, the librarian or `/hi`, so `waits_for_another_session` does not match it; it holds no "first", so `tied_to_a_one_off_moment` does not match; and it does not open with `after`, so `waits_for_a_later_moment` is false and `check_unread` gives `unread: pending` on the page until its reading, which is red by design. By the person's answer to another finding of `/pre-spec`, Case 908.3 replaces the Criterion of `estimate-orchestration-shows-the-built-case`, which names Russian as the language in which the main agent shows a round, the name of a Case and its short text. That page already stands `pending` and `rule-orchestration` already stands `draft`, so no status changes. Its `method` and `purpose` speak of the reading of the Render and of the showing, not of the language, so both stand. Its Criterion and that of `estimate-orchestration-forwards-a-discussion-question` already share their lines on a plain explanation, on a `**Fact:**` answer and on the translation of what `case-guppi` answers: one checks every showing of the main agent, the other the path of a discussion question alone, so each sub-case keeps the lines of the Criterion it replaces, and the two new texts name the language alike, by role. The other four, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-ask-query-before-a-create` and `estimate-compact-recall-reloads`, keep their text: their readings wait for events that may not come for a long time, and their rules stand `built` with `core: true`. So the defer of `decision-case-893.1` stays, and no line of this Case carries a mark that retires it; its text still names the two Estimates rewritten here, and the next reading of `estimate-clean-branch-ships-neutral-texts` no longer lists them. The Render of `rule-orchestration` on its rule page says that the main agent shows that reply translated into `{{chat_lang}}`, a value that the render fills from `rule-guppi-config`; only the rendered `vault/wiki/orchestration.md` holds the word Russian, so the rule names the language by role already, and this Case changes no rule page. A Grep of `estimate-permissions|estimate-orchestration-forwards-a-discussion-question|estimate-orchestration-shows-the-built-case` over `vault/wiki/` printed `brief.md`, `log.md`, `estimates/estimate-case-protocol-case-form.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `rules/rule-permissions.md` and `rules/rule-orchestration.md`; the hits in the two rules are their `estimates` field and a History line, the one in `estimate-case-protocol-case-form` is a History line, and the one in `estimate-clean-branch-ships-neutral-texts` is its Result, so all stand; over `.claude/` and `.guppi/` it printed nothing. A Grep of `wiki_root\(REPO|read_vault\(.*REPO|REPO / "vault"|ship\.ship\(REPO|estimates/estimate-` over `.guppi/tests/` printed `test_ship.py`, `test_generate.py`, `test_sprint_close.py`, `test_lint.py`, `test_guppi_package.py` and `test_schemas.py`. Of them, `test_ship.py` and `test_guppi_package.py` read the live vault: the live build of `test_ship.py` asserts no line on a page under `vault/wiki/estimates/`, and a `pending` Estimate is not shipped; `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` looks for old commands and paths that the new texts do not add. The others build pages of their own. No new Estimate is created: each sub-case replaces the Criterion of the Estimate it rewrites, and that Estimate checks it.

> **problem:**
> Two shipped checks hold a sentence that is false in a project that installed GUPPI: one names GUPPI's own transcripts folder, the other names Russian as the language of the chat, and a third check, of how a built Case is shown, names Russian too. The other four under the same defer wait, since a replaced Criterion would hold their rules `draft` for a long time.

> **recommend:**
> - **Which checks this Case rewrites**
>   - Recommended: (a) the six of the defer; the glossary check keeps its text, since this session's reading did not list it.
>   - Answer: agreed, (a).
> - **When the new texts come in**
>   - Recommended: (b) now only `estimate-permissions`, read at the Retro of this session, and `estimate-orchestration-forwards-a-discussion-question`, whose rule is already `draft`; the other four keep their text under the defer.
>   - Answer: agreed, (b).
> - **When the discussion-question check is read**
>   - Recommended: (a) the `method` names its event: by hand, after a question of the person to discuss an item.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the allow list holds one Read rule for all the paths under the transcripts folder, not one per path.
>   - Taken: the first `then` line of Case 908.1 says a Read rule for the paths under it.
> - **Change**
>   - Asked: at `/pre-spec`, the Render on the page of `rule-orchestration` names the language by a placeholder; only the rendered file holds Russian.
>   - Taken: the `context` states that fact.
> - **Change**
>   - Asked: at `/pre-spec`, the discussion-question check is read at the Retro of a session that holds such a question, from the tool calls of that session, since `/hi` reads no transcript of an earlier session.
>   - Taken: Case 908.2 sets its `method` so.
> - **Change**
>   - Asked: at `/pre-spec`, `estimate-orchestration-shows-the-built-case` names Russian as the chat language too; add a sub-case that replaces its Criterion whole, with no change of status.
>   - Taken: Case 908.3 replaces it with the chat language named by role.

### Case 908.1 — The permissions check names the transcripts folder by role

> **given:**
> `estimate-permissions`: its Criterion is replaced whole.
> **＋** `rule-permissions`: the rule whose Render writes the allow list and names the transcripts folder.
> **＋** `.claude/settings.json`: the settings file whose allow list the check reads.
> **＋** `.guppi/tests/test_render.py`: its JSON case fixes the shape of the block.
> **＋** `rule-spec-reconcile`: its guard writes the file of a Case of `case-guppi`.
> **＋** `vault/raw/**`: the working files of the session.
> **＋** `vault/wiki/brief.md`: the brief that the session writes.
> **＋** `cases/`: the folder of the files of the Cases, kept off the allow list.
> **＋** `~/.claude/projects/`: the folder that holds the saved transcripts of each project.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder of saved transcripts under `~/.claude/projects/` that the Render of `rule-permissions` names, that folder itself as its path or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, a Read rule for the folder of saved transcripts that the Render of `rule-permissions` names, and a Read rule for the paths under it.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `.guppi/tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only: the reading line records it from the person, never from the agent, whose reply does not tell an approved call from one not asked.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is that folder itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, since the guard of `rule-spec-reconcile` makes the write and stops its call.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** An error of the guard of `rule-spec-reconcile` while it writes that file lets the call run, and the client may ask the person that one time; that prompt is not a finding and not a `failed`.
> **－** A Read, Grep or Glob of `case-guppi` on a path outside the project that no rule of the allow list names is not bound by this Criterion: it may ask the person.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names that folder.

```then
update:
- slug: estimate-permissions
  set:
    status: pending
  change: the Criterion replaced whole — the transcripts folder is named as the one the Render of rule-permissions names, not by the folder name of the repository of GUPPI
```

```tasks
- [ ] update `estimate-permissions`
- [ ] read `estimate-permissions`
```

### Case 908.2 — The discussion-question check names the chat language by role

> **given:**
> `estimate-orchestration-forwards-a-discussion-question`: its Criterion and its `method` are replaced.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the Render that sets how a discussion question is passed on.
> **＋** `case-guppi`: the agent that built the Case of the item.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill that explains a text in plain words.
> **＋** `rule-case-check`: the rule of the hook that reads the answers of `case-guppi`.

> **when:**
> In Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to discuss an item whose `case-guppi` is building its Case or has shown it, or to learn something of that item, and the question is no request for a plain explanation of the agent's text.

> **then:**
> The main agent sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and makes no `Read`, `Grep` or `Glob` call of its own to answer it.
> **＋** `case-guppi` answers in plain words under a first line `**Fact:**`, with no Case heading and no round, from the pages it read, or with a round when the question opens a fork.
> **＋** The main agent shows the answer translated into the language of the chat, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
> **－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
> **－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

```then
update:
- slug: estimate-orchestration-forwards-a-discussion-question
  set:
    status: pending
    method: 'by hand, at the Retro of a session that holds a question of the person in the chat to discuss an item whose case-guppi is building its Case or has shown it: the SendMessage call, the tool calls of the main agent and the answer, read in that session'
  change: the Criterion replaced whole — the answer is shown in the language of the chat, not named as Russian; the method is read at the Retro of a session that holds such a question, from its own tool calls, not in the transcript of a later session
```

```tasks
- [ ] update `estimate-orchestration-forwards-a-discussion-question`
- [ ] read `estimate-orchestration-forwards-a-discussion-question`
```

### Case 908.3 — The showing check names the chat language by role

> **given:**
> `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets how a Case is dispatched and shown.
> **＋** `case-guppi`: the agent that builds each Case and its rounds, and `ask-guppi`, which runs only at pre-spec.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`, `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session the showing reads or closes.
> **＋** `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md`: the skills of a plain explanation and of the shape of a round.
> **＋** `rule-case-check`, `rule-prespec-onward` and `rule-spec-box`: the rules of the hooks of a showing, of the count of a ratified Case, and of a `/work` that `/box` calls.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>`: the command that prints the id of a new Case.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into the language of the chat line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in the language of the chat translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in the language of the chat, and a short text in the language of the chat on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

```then
update:
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — the round, the name of a Case and its short text are shown in the language of the chat, not named as Russian
```

```tasks
- [ ] update `estimate-orchestration-shows-the-built-case`
- [ ] read `estimate-orchestration-shows-the-built-case`
```

## Case 912 — The install copies the settings of the project after uv sync

> **context:**
> `/guppi:install` copies every file of GUPPI into the project in one step, `.claude/settings.json` with them, and only then runs `uv sync --project .guppi`. Claude Code picks up that settings file in the same session, so each hook of the copy runs `uv run --project .guppi` at the next tool call. On a good install a hook builds `.guppi/.venv/` before `uv sync` does; on a failed `uv sync` the rollback deletes `.guppi/`, and each later command of that session shows a hook error. `lesson-plugin-install-hooks-of-the-copy-run-at-once` (L44 of session 0327) records both, and the Result of `estimate-guppi-package-is-ready-after-the-install` shows the folder made by a hook two seconds before `uv sync` printed "Checked 9 packages". The hooks documentation of Claude Code (https://code.claude.com/docs/en/hooks) says that direct edits to hooks in settings files are normally picked up automatically by the file watcher; the chosen fix does not rest on that timing, since a settings file that does not stand yet runs no hook. The person chose to copy `.claude/settings.json` only after `uv sync` passes. This Case replaces Case 905, which was ratified whole: at `/pre-spec` the person agreed to a pair on step 5 of the Render, since that step checks each file of the list of step 2 and would stop on the missing settings file before `uv sync`, and chose that the Case also replace the Criterion of `estimate-guppi-package-is-ready-after-the-install`, whose sentence "After it copies the files, it runs `uv sync`" the new order makes false. That is a second promise, so the Case has two sub-cases and a new number, and its decision lines retire Case 905. Case 912.1 holds the change of `rule-plugin-install` and the new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync`, which checks that no hook runs before `uv sync` or after a rollback. Case 912.2 replaces the Criterion of the package Estimate with the order of the steps, sets its `purpose` and its `method` anew, and is read in the same installs by hand as the new Estimate. The function `cascade` of `.guppi/guppi/generate.py` sets a rule `draft` while one of its own Estimates does not stand `passed`, so `rule-guppi-package` and `rule-plugin-install` go back to `draft` at the librarian's run and stand `built` again once those readings pass; no task sets that status. In the Purpose of `rule-plugin-install` the other sentences stand, since the install still copies each file and the rollback still deletes each file it copied. In the Render, step 4 leaves out the settings file, step 5 checks the files of step 4, a new step 7 copies the settings file and checks it, and the old step 7 becomes step 8. The Render holds no case number, since `guppi ship --check` refuses one in `plugin/skills/install/SKILL.md`. A Grep for `uv sync` over `vault/wiki/` without `brief.md`, `sprint.md` and `log.md` printed five files: `rule-plugin-install.md`, `lesson-plugin-install-hooks-of-the-copy-run-at-once.md`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails.md`, `estimate-plugin-install-offers-to-install-uv.md` and `estimate-guppi-package-is-ready-after-the-install.md`. The Criteria of `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` and `estimate-plugin-install-offers-to-install-uv` stand: the rollback still deletes each file it copied, and `uv --version` still runs first. The Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` stands too, since the install still copies `.claude/settings.json` and checks each copied file. A project that already holds its own settings is outside this Case: step 3 still refuses it, and the person's new item on installing into such a project is a Case of its own. The lesson belongs to another session, so no decision line carries `{addresses:...}`.

> **problem:**
> The hooks of the copied settings run inside the install session itself: they build `.guppi/.venv/` before `uv sync`, and they fail at each command after a rollback.

> **recommend:**
> - **How the install keeps the copied hooks from running**
>   - Recommended: (a) copy `.claude/settings.json` last, after `uv sync` passes.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix**
>   - Recommended: (a) a new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync` on `rule-plugin-install`.
>   - Answer: agreed, (a).
> - **When the new check is read**
>   - Recommended: (a) by hand, after the librarian's run, like the other install Estimates: one install where `uv sync` passes and one offline.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, a pair on step 5 of the Render, so that it checks only the files that step 4 copied.
>   - Taken: Case 912.1 gains that pair.
> - **Change**
>   - Asked: at `/pre-spec`, the Case also replaces the Criterion of `estimate-guppi-package-is-ready-after-the-install`, so that it says the install copies every file but `.claude/settings.json` before `uv sync`; the Estimate goes `pending` and is read in the same installs by hand as the new Estimate.
>   - Taken: Case 912.2, under the new number 912 with sub-cases, which retires Case 905.

### Case 912.1 — No hook of the copy runs before uv sync

> **given:**
> `rule-plugin-install`: the rule of the install skill, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill that the Render writes.
> **＋** `/guppi:install`: the command by which the person runs that skill.
> **＋** `.claude/settings.json`: the settings file of the copy, which holds the hooks of the project.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `estimate-plugin-install-runs-no-hook-before-uv-sync`: the new check that no hook runs early.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.

> **then:**
> Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
> **＋** No hook of the copy has made `.guppi/.venv/` by the time `uv sync` runs.
> **＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
> **－** In a project that already holds `.claude/settings.json` or another file of the install, the agent still lists them, writes nothing and stops.

```then
create:
- slug: estimate-plugin-install-runs-no-hook-before-uv-sync
  ref: rule-plugin-install
  kind: QA
  purpose: Whether /guppi:install copies .claude/settings.json only after uv sync passes, so that no hook of the copied project builds .guppi/.venv before uv sync or fails after a rollback
  method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project where uv --version passes, /guppi:install typed, and the output of uv sync and the time .guppi/.venv was made read; in a second empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed and a command run after its rollback; the transcripts and the files of both projects read against the Criterion'
  tags:
  - plugin
  - hooks
update:
- slug: rule-plugin-install
  replace:
  - old: does not wait for it ([[rule-guppi-package]], case 819).
    new: 'does not wait for it ([[rule-guppi-package]], case 819). It copies `.claude/settings.json`, which holds the hooks of the project, only after `uv sync` passes, since Claude Code picks up that file in the same session: no hook of the copy runs before `uv sync` builds `.guppi/.venv/`, and none runs after a failed `uv sync` (as set in case 912).'
  - old: 4. Otherwise copy each file to its path in the project, with the folders it needs.
    new: 4. Otherwise copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of the project runs before then.
  - old: 5. Check that each file now stands in the project.
    new: 5. Check that each file you copied in step 4 now stands in the project.
  - old: 7. Say that GUPPI is installed,
    new: |-
      7. Copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands. When it is missing, name it and stop.
      8. Say that GUPPI is installed,
  change: the install copies .claude/settings.json only after uv sync passes, so no hook of the copy runs before uv sync or after a rollback
```

```tasks
- [ ] update `rule-plugin-install`
- [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [ ] create `estimate-plugin-install-runs-no-hook-before-uv-sync`
- [ ] read `estimate-plugin-install-runs-no-hook-before-uv-sync`
```

### Case 912.2 — The install builds the environment before it copies the settings

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion, `purpose` and `method` are set anew.
> **＋** `rule-guppi-package`: the target of that Estimate.
> **＋** `rule-plugin-install`: the rule of the install skill.
> **＋** `plugin/skills/install/SKILL.md`: the skill that `rule-plugin-install` renders.
> **＋** `uv run --project .guppi guppi ship --allow-draft <folder>`: the command that writes the clean version.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands by which the person installs the plugin.
> **＋** `/guppi:install`: the command by which the person runs the skill.
> **＋** `.claude/settings.json` and `.guppi/.venv/`: the settings file of the copy and the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill to which the install sends the person at its end.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

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
    purpose: Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv, copies every file but .claude/settings.json, builds the Python environment .guppi/.venv/ by uv sync, and copies .claude/settings.json only then, before it sends the person to /hi
    method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person''s answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync'
  change: the Criterion replaced whole — the install copies every file but .claude/settings.json before uv sync, and that file after uv sync passes
```

```tasks
- [ ] update `estimate-guppi-package-is-ready-after-the-install`
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```

## Deferred

## Case 907 — The removal of PLAIN_SPRINTS put off to the close of sprint plugin

> **context:**
> The person put off the removal of `PLAIN_SPRINTS = ("migration", "plugin")` from `.guppi/guppi/caseid.py` until after the close of sprint `plugin`, with the round of Case 906, which was dropped for this defer. The clean version ships the list with the names of the sprints of GUPPI. Once `plugin` closes, no sprint needs plain ids.

> **problem:**
> No Case of this session removes the fixed list of sprints that keep plain Case ids from the code that the clean version ships.

```then
defer:
  - slug: rule-ratification
    type: rule
    purpose: "Remove PLAIN_SPRINTS from .guppi/guppi/caseid.py after sprint plugin closes, so that only an id that already has no sprint part stays plain and the clean version holds no name of a sprint of GUPPI; with it, replace the Criterion sentence of estimate-ratification-case-id-carries-the-sprint that names the list, the test in .guppi/tests/test_caseid.py that expects plugin to get plain ids, and the sentence of the Render of rule-ratification that names the list"
```

## Case 909 — The approval of a long plan in the Claude Code CLI put off

> **context:**
> The person put off this item at the close of Plan Mode. The lesson L42 of session 0327 records that the Claude Code CLI withholds the approval of a plan of 15 KB, so a Spec of that size cannot be approved there. No Case of this session sets how GUPPI keeps the plan file short or approves the Spec another way.

> **problem:**
> No Case of this session decides how a Spec too long for the CLI gets approved.

```then
defer:
  - slug: rule-spec-capture
    type: rule
    purpose: "Lets a Spec be approved in the Claude Code CLI, which withholds the approval of a plan of 15 KB: the plan file kept short enough, or the Spec approved another way (L42 of session 0327); put off at the close of Plan Mode"
```

## Case 910 — The questions on what a new project builds put off

> **context:**
> The person put off this item at the close of Plan Mode. The lesson L43 of session 0327 records that the opening of the first sprint of a new project asks nothing of what the project builds. The item names the setup skill of `rule-morph` or the questions of `rule-skill-sprint-open` as the places to fix it. No Case of this session sets either.

> **problem:**
> No Case of this session decides where the opening of the first sprint of a new project asks what the project builds.

```then
defer:
  - slug: rule-skill-sprint-open
    type: rule
    purpose: "The opening of the first sprint of a new project asks what the project builds, by the questions of /sprint-open or by the setup skill of rule-morph (L43 of session 0327); put off at the close of Plan Mode"
```

## Case 911 — The install of GUPPI into an existing project put off

> **context:**
> The person added this item in this session and put it off at the close of Plan Mode. Step 3 of `/guppi:install` refuses a project that already holds one of the files of GUPPI, such as `.claude/settings.json` or `CLAUDE.md`, and writes nothing there. No page sets how the settings, the hooks and the `CLAUDE.md` of such a project join those of GUPPI.

> **problem:**
> No Case of this session decides how GUPPI installs into a project that already holds its own settings, hooks and `CLAUDE.md`.

```then
defer:
  - slug: rule-plugin-install
    type: rule
    purpose: "Lets GUPPI install into an existing project that holds its own .claude/settings.json, hooks and CLAUDE.md, which /guppi:install now refuses whole; put off at the close of Plan Mode"
```
