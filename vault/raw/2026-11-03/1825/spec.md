<!-- approved 19:37:25 · session badff418 -->

# Session 1825 — the sprint plugin

## Case 1019 — The session start reads the transcript a method names, and a past build is read by a one-off check

> **context:**
> `estimate-case-build-reads-the-readers-of-a-new-files-folder` promises a lasting behaviour of `case-guppi`, but its `method` reads the agent transcript of one later build. Its event came in session 2155, whose Case 1012 adds `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py`, as line W1 of `vault/raw/2026-11-03/0316/frontier.md` gives it. Nobody took the reading. The handoff of session 0316 says the method reads the transcript of an earlier session, "which no session may read". The source is the W-line step of `rule-skill-hi`, which ends with "read no transcript of an earlier session (case 670.5)". The end-of-session review reads only the Estimates its own session creates or updates (`rule-retro`, case 781). So a reading whose event came in a later session goes from the handoff to the brief as a proposal to defer it (`rule-brief`). Case 670 set that rule to save cost; the Problem of `decision-case-670` says that each `/hi` "pays to read the same Estimates again".
>
> The person found it absurd that a needed transcript cannot be read, and chose that `/hi` reads the transcript a method names, in parts, only once its event has come. `/hi` finds the transcript by the stamp of that session. `stamp` of `.guppi/guppi/spec.py` writes the first line of each `spec.md` as `<!-- approved HH:MM:SS · session <stamp> -->`. That stamp comes from `session_stamp` of `.guppi/guppi/event.py`, which takes the first eight characters of the session id. The first line of `vault/raw/2026-11-03/0316/spec.md` holds `session 5c8c941f`, and `~/.claude/projects/c--PROJECTS-GUPPI/5c8c941f-70e2-416c-8f86-83ce2f6f7765.jsonl` exists. The read rules of `rule-permissions` already let the session read this project's saved transcripts. Case 1019.1 changes that one sentence and replaces the Criterion of `estimate-hi-takes-its-readings`, whose line "It reads no transcript of an earlier session" the change makes false; its `purpose` is set anew. Its `method` reads the new Render at the Retro of this session, so it stands. The step for an `A` line still opens no saved chat: the person chose a transcript reading only for a `W` line whose `method` names one. The Purpose of `rule-skill-hi` speaks of the blocks the skill loads, so it stands, and so do `estimate-hi-no-read-calls` and `estimate-hi-takes-a-conserved-spec`, which speak of the blocks and of a conserved Spec. The sentence of `rule-brief` that proposes a defer stands for the readings that still cannot run.
>
> The person asked how such an Estimate reaches the clean version. `ships` and `shipped_page` of `.guppi/guppi/ship.py` write each `passed` Estimate of a page with `core: true` with its `method` as it stands. They set `origin`, `sprint` and `created` to the shipped value and cut `## Result` to one line. So a `method` that names one of our sessions ships, and a result does not. The person chose a split. Case 1019.2 gives the lasting Estimate the `method` its siblings use, a reading of the Render in `.claude/agents/case-guppi.md`, and keeps its Criterion. Case 1019.3 creates a one-off Estimate with `once: true` on `entity-sprint-plugin`, as `rule-estimates-schema` sets that field (case 969.1). It reads the transcript of that build once, in the Work Mode of this session, and leaves with the sprint page. A Grep `Build Case 1012` over `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl` counted 2 matches. A Glob found the case file at `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, and I did not read it. A Grep `^once: true` over `vault/wiki/estimates/` counted one match in each of `estimate-sprint-plugin-check-finds-no-bare-slug-link.md`, `estimate-sprint-plugin-link-graph-is-gone.md` and `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link.md`, all on `entity-sprint-plugin`, so the new one follows their form. The Purpose of `entity-sprint-plugin` says the sprint is done when every one of its Estimates passes. The new one is read in this session, so it does not hold the close back.
>
> The person kept the split to this Estimate. Other lasting Estimates read a transcript after an event. Of `rule-case-build`, these are `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-case-build-runs-the-vault-query-first` and `estimate-case-build-goes-on-after-a-live-compaction`, whose events have not come, and `estimate-case-build-searches-the-names-of-what-it-changes`. That last one reads the agent transcript of each `case-guppi` of the session in which the hook of `rule-case-check` sent the note, and its `read` box stands open in the Spec of session 2155. Of other rules, these are `estimate-prespec-finds-a-reader-of-a-new-files-folder` of `rule-prespec`, whose event is line W2 of `vault/raw/2026-11-03/0316/frontier.md`, and `estimate-ask-searches-at-prespec` of `rule-ask`. Each stands by the person's answer that the split covers this Estimate alone. After Case 1019.1, `/hi` can take their readings from the transcript once the brief puts them under `Work`. Whether they are split too is the question of the backlog line of Case 1019.4, which `entity-sprint-plugin` gains under `## Backlog`. By `deferred` of `.guppi/guppi/backlog.py`, a line that names no page by a link stands by its text. `estimate-backlog-renders` of `rule-backlog` checks this, and its method `uv run --project .guppi pytest .guppi/tests/test_backlog.py` runs over a made-up vault, so the `when` and `then` of Case 1019.4 speak of that test. Its Criterion stands, and no new Estimate is made for the line.
>
> At `/pre-spec`, `ask-guppi` found that `rule-raw-archive` says of an applied session that "nothing reads it again". Case 1019.1 reads the first line of an archived `spec.md`, and Case 1019.3 reads an archived case file. The person chose that Case 1019.1 updates its Purpose: nothing changes an archived session, and `/hi` may still read the first line of its `spec.md`. A Glob found `vault/archive/plugin/2026-11-02/2155/raw/spec.md`. The row `raw/` of `glossary.md` gives the archived path as `vault/archive/<sprint>/<date>/<HHMM>/raw/`, so the Render and the Criterion name that path. A Glob found `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f.jsonl` beside the folder of the same name that holds `subagents/`. The Purpose of `rule-raw-archive` touches no Estimate. Its Estimates, `estimate-raw-archive` and `estimate-raw-archive-files-a-session-by-its-sprint`, speak of what `guppi archive` moves and where, so they stand. I read the docstring of `.guppi/guppi/archive.py`. It sets which units move, where they go, and that no file is cut and no pointer rewritten, which lint still resolves in the archive. It says nothing about who reads an archived session, so it stands. The check of this file also listed `rule-cleanup`, `rule-documentation`, `estimate-sprint-close-sweeps-raw`, `estimate-render-harness-ticks-the-spec`, `sprint_close.py`, `cleanup.py`, `materialize.py` and `test_archive.py`. Judged by their purpose lines and paths, they speak of moving pages and sessions, of the steps of the librarian's run and of the ticks of the Spec, not of who reads an archived session, so they stand. The step for an `A` line now says that the agent does not open that chat, rather than that it cannot, since the step for a `W` line now opens a saved transcript.
>
> A Grep `no transcript|may not open|670\.5` over `{vault/wiki,.claude,.guppi/guppi}/**`, in the mode of paths, printed 14 files. `rule-skill-hi.md`, its render `.claude/skills/hi/SKILL.md` and `estimate-hi-takes-its-readings.md` change here. `log.md` is not read. `lesson-brief-lists-transcript-readings-under-work.md` names the root cause this Case fixes. It is a lesson of an earlier session, so it gets no mark. `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of.md` speaks of a text an `A` line asks about, which stands. The hits of `orchestration.md`, `rule-orchestration.md`, `estimate-orchestration-states-a-subagent-fact-from-its-transcript.md`, `estimate-librarian-report-copy-writes-the-file.md`, `estimate-close-commits.md`, `estimate-case-check-notes-the-files-that-name-what-a-case-changes.md`, `ratified.py` and `casecheck.py` speak of a subagent's report, of the librarian's report file, of a librarian's method and of checks of code, not of what `/hi` reads, so they stand. A Grep `skills/hi|rule-skill-hi|hi/SKILL` over `.guppi/tests/` printed `test_guard.py`, `test_ratified.py`, `test_ship.py`, `test_lint.py` and `test_prespec.py`. Each one builds its files under a temporary folder or holds the path as a string, so no test reads the live skill. The ledger of this session holds no `error` lesson.
>
> The new Criterion of `estimate-hi-takes-its-readings` words four lines of the old one anew on purpose: the line on the `A` questions and the line on the search for their text are joined, the line that forbids a transcript gives way to the line that reads one in parts, and the line on the steps that open pages names the transcript. The check of this file listed the files that name `rule-skill-hi`, `SKILL.md`, `/hi` and `entity-sprint-plugin`. Judged by its purpose, `estimate-work-mode-takes-the-work-readings` lets `/work` take a reading whose moment came in an earlier session, which agrees with the change. `estimate-orchestration-acknowledges-the-opening-with-the-frontier` speaks of when the readings of `/hi` are taken, not of what they read. `lesson-hi-unread-sprint-reading-made-a-case-line` speaks of the readings of the sprint page. `estimate-brief-carries-the-run-facts` speaks of the brief. `entity-sprint` says that the `## Backlog` of a sprint page holds the items without a turn, which the new line is. Each of these stands. The other listed files speak of other skills, other hooks or other parts of the sprint page. The Criteria of Case 1019.2 and Case 1019.3 share most of their words on purpose: the first promises the lasting behaviour, and the second reads one past build of it once. I read the finished file of Case 1020 of this session, `vault/raw/2026-11-03/1825/cases/case-1020.md`. It changes `rule-clean-branch`, creates `estimate-clean-branch-leaves-out-the-source-pictures` and moves the source pictures of the icon to `plugin/assets/`. It changes neither a page this Case changes nor the moment of `/hi`. The functions `ships` and `shipped_page` of `.guppi/guppi/ship.py`, which this `context` cites, stay as they are under that Case, which judges a file of `plugin/assets/` only. So the two Cases do not clash.

> **problem:**
> A check whose `method` reads the transcript of a later session cannot be read. `/hi` may not open an earlier transcript, and the end-of-session review of that later session does not take it, so the check stays open. A lasting check that names one of our sessions would also ship that name in the clean version.

> **recommend:**
> - **What happens to this check**
>   - Recommended: (b) a method that reads the Case file alone.
>   - Answer: none of the options; the person does not accept that a transcript cannot be read after `/hi`, which makes it impossible to read what can and should be read, and asked for a fix.
> - **Which checks the Case covers**
>   - Recommended: (a) this check only.
>   - Answer: not answered; replaced by the question "What happens to this check's own reading" and later by "Whether the split becomes a rule".
> - **Who reads the transcript of an earlier session**
>   - Recommended: (a) `/hi` reads the transcript itself, in parts.
>   - Answer: agreed, (a).
> - **What happens to this check's own reading**
>   - Recommended: (b) a task of this session reads it now.
>   - Answer: agreed, (b).
> - **How the change is checked**
>   - Recommended: (a) replace the text of `estimate-hi-takes-its-readings`.
>   - Answer: agreed, (a).
> - **How the session start finds the transcript**
>   - Recommended: (a) the step finds it by the stamp.
>   - Answer: agreed, (a), after the person asked how such a check reaches the clean version and asked for a one-off check of the transcript beside a lasting check.
> - **How this check is split**
>   - Recommended: (a) a lasting check and a one-off check.
>   - Answer: agreed, (a).
> - **Whether the split becomes a rule**
>   - Recommended: (a) this check only.
>   - Answer: agreed, (a); and a separate backlog item asks whether checks should be made this way.
> - **Where the backlog item stands**
>   - Recommended: (a) a line in the backlog of the sprint page.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the finding that `rule-raw-archive` says nothing reads an archived session, while Case 1019.1 reads the first line of an archived `spec.md`; the person agreed to option (a), that Case 1019.1 updates the Purpose of `rule-raw-archive`.
>   - Taken: Case 1019.1 updates the Purpose of `rule-raw-archive`: nothing changes an archived session, and `/hi` may still read the first line of its `spec.md`. The fixes of the other findings of `/pre-spec` are taken as well: the archived path of `spec.md` and the place of `subagents/` are named in both texts, the `A` step says it does not open that chat, the `context` names the other lasting Estimates that read a transcript, and the `when` and `then` of Case 1019.4 speak of the test of `guppi backlog`.

### Case 1019.1 — The session start reads the transcript that a method names

> **given:**
> `rule-skill-hi`: the rule of `/hi`, whose Render sets the step that takes the open readings.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-takes-its-readings`: its Criterion and `purpose` are replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `vault/wiki/brief.md`: the brief that gives the open readings.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of a session, whose first line holds its stamp.
> **＋** `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md`: the Spec of an archived session.
> **＋** `rule-raw-archive`: the rule of the archive of sessions, whose Purpose says what reads an archived session.
> **＋** `~/.claude/projects/`: the folder of the saved transcripts of the project.
> **＋** `subagents/`: the folder inside the folder named by a session id that holds the transcripts of its agents.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** Where the method reads the transcript of a session under `~/.claude/projects/` and its event came in an earlier session, it takes the stamp of that session from the first line of its `raw/<date>/<hi HHMM>/spec.md`, or of `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md` once the session is archived, opens the transcript under `~/.claude/projects/` whose name opens with that stamp, or the transcript of one of its agents in the folder `subagents/` inside the folder of the same name, searches it by a Grep with lines of context and reads only the parts around the hits.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question. When that question asks the person to judge a text and names no path, the agent looks for the text by a Grep or a Glob over the files of the repository, such as `vault/wiki/brief.md`, the handoff of the session and the page of the Estimate. When the text is in a file of the repository, it names the path and the section of that file and quotes the part the question judges. When it finds no such file, it names the session by its date and the time of its `hi:` line and the reply that showed the text, and says in a plain sentence that it does not open that chat.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result and the place it named for the text as its source, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript whole, and no transcript that the method of an open `W` line does not name.
> **－** A session with no `spec.md`, neither `raw/<date>/<hi HHMM>/spec.md` nor `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md`, gives no stamp, and the `W` line of its reading stays open.
> **－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. The step that reads the open `W` lines opens the page of the Estimate of each of them and the transcript its method names. The step that puts the `A` lines opens the file it found or the question names, to quote it, and never a saved chat.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'from files and commands alone: the brief, `git log`, `git status`, and the files and the commands the method names; read no transcript of an earlier session (case 670.5).'
    new: 'from the brief, `git log`, `git status`, and the files and the commands the method names; where the method reads the transcript of a session under `~/.claude/projects/` and its event came in an earlier session, read that transcript too: take the stamp of that session from the first line of its `spec.md`, `vault/raw/<date>/<HHMM>/spec.md`, or `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md` once the session is archived, open the transcript under `~/.claude/projects/` whose name opens with that stamp, or the transcript of one of its agents in the folder `subagents/` inside the folder of the same name, search it by a Grep with lines of context and read only the parts around the hits, never the whole file; a session with no `spec.md` in either place gives no stamp, and its line stays open (as set in case 1019.1).'
  - old: with a plain sentence that you cannot open that chat (as set in case 921).
    new: with a plain sentence that you do not open that chat (as set in cases 921 and 1019.1).
  change: /hi reads the transcript that the method of an open Work line names, found by the stamp in the first line of that session's spec.md, live or archived, and read in parts, once its event came in an earlier session; an Ask line still opens no saved chat
- slug: rule-raw-archive
  replace:
  - old: nothing reads it again, so it moves whole into the archive of its date.
    new: nothing changes it again, so it moves whole into the archive of its date, where `/hi` may still read the first line of its `spec.md` (as set in case 1019.1).
  change: nothing changes an archived session, and /hi may read the first line of its spec.md
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, and from the transcript that a method names, found by the stamp of that session's spec.md and read in parts, never whole, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, with the place of a text the question asks the person to judge, searched for in the files of the repository when the question names no path, and a quotation of it when it stands in a file, writes the answer and that place as its reading line, and opens no page but the Estimates of its open W lines and the file it quotes
  change: the Criterion replaced whole — /hi reads the transcript that a method names, found by the stamp of its session and read in parts; the purpose set anew
```

```tasks
- [ ] update `rule-skill-hi`
- [ ] update `rule-raw-archive`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] update `estimate-hi-takes-its-readings`
- [ ] read `estimate-hi-takes-its-readings`
```

### Case 1019.2 — The lasting check of the folders of a new file reads the Render

> **given:**
> `estimate-case-build-reads-the-readers-of-a-new-files-folder`: its `method` is set anew, and its Criterion is written again as it stands.
> **＋** `rule-case-build`: the rule of `case-guppi`, the target of that Estimate.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`, which the new `method` reads.
> **＋** `.guppi/guppi/`: the folder of the code, which the searches cover.
> **＋** `.guppi/tests/`: the folder of the tests, which the walk search covers.
> **＋** `.claude/`: the folder of the harness, which the folder search covers.
> **＋** `vault/wiki/`: the vault, whose Rule pages the folder search covers.

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

```then
update:
- slug: estimate-case-build-reads-the-readers-of-a-new-files-folder
  set:
    status: pending
    method: 'by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line'
  change: the method reads the Render of rule-case-build and no transcript; the Criterion written again as it stood; the build of session 2155 is read once by an Estimate of entity-sprint-plugin
```

```tasks
- [ ] update `estimate-case-build-reads-the-readers-of-a-new-files-folder`
- [ ] read `estimate-case-build-reads-the-readers-of-a-new-files-folder`
```

### Case 1019.3 — The past build of the folders of a new file is read once

> **given:**
> `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: the new one-off Estimate.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of that Estimate.
> **＋** `rule-case-build`: the rule whose Render that build ran on.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl`: the agent transcript of that build.
> **＋** `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`: the case file of that build.
> **＋** `.guppi/guppi/frontierguard.py`: a new file of that Case.
> **＋** `.guppi/tests/test_frontierguard.py`: a new file of that Case.
> **＋** `vault/wiki/rules/`: the Rule pages, which the folder search covers.

> **when:**
> The agent transcript `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl` of the `case-guppi` that built the Case adding `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py`, and its case file `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, are read once against this Criterion.

> **then:**
> That build searched `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds `.guppi/guppi/frontierguard.py` or `.guppi/tests/test_frontierguard.py`.
> **＋** It searched `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It read each ignore file of git in a folder that holds those files.
> **＋** It read each reader that takes every file of such a folder.
> **＋** Each reader that those files make wrong entered the Case of `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, or its `context` names it and says why it stands.
> **＋** That `context` names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether those files make it wrong.

```then
create:
- slug: estimate-sprint-plugin-frontierguard-build-read-its-folders-readers
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the case-guppi that built the Case adding .guppi/guppi/frontierguard.py and its test, in session 2155, made and named in context each search and reading for the folders of a new file that rule-case-build sets; read once
  method: 'by hand, in the Work Mode of the session that creates this Estimate: the agent transcript ~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl searched by a Grep with lines of context for each search and reading of the Criterion, and the case file vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md read for the list of them in its context; the count, the transcript and the case file in the estimate line'
  once: true
  tags:
  - sprint
  - case-build
```

```tasks
- [ ] create `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`
- [x] by hand, in Work Mode: the transcript and the case file that the `method` of `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` names read against its Criterion, the count kept for its reading
- [ ] read `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`
```

### Case 1019.4 — The backlog asks whether a check that reads a transcript is always split

> **given:**
> `entity-sprint-plugin`: the live sprint page, whose `## Backlog` gains the line.
> **＋** `vault/wiki/backlog.md`: the list that shows each line of that section.
> **＋** `.guppi/guppi/backlog.py`: the script that writes `vault/wiki/backlog.md`.
> **＋** `.guppi/tests/test_backlog.py`: the test of that script.
> **＋** `rule-estimates-schema`: the schema of Estimates, which the line asks about.

> **when:**
> `.guppi/tests/test_backlog.py` runs `.guppi/guppi/backlog.py` over a made-up vault whose sprint page holds, under `## Backlog`, a line that names no page.

> **then:**
> The script writes that line under `## Deferred` of `vault/wiki/backlog.md` by its text.
> **＋** The line that `entity-sprint-plugin` gains under `## Backlog` names no page by a link, so `vault/wiki/backlog.md` shows it by its text in the same way: whether every Estimate whose `method` reads the transcript of a session should be a one-off Estimate of the sprint page, with a lasting Estimate beside it whose `method` reads a file that ships.
> **－** `rule-estimates-schema` does not change.

```then
update:
- slug: entity-sprint-plugin
  replace:
  - old: taken out of rule-morph (case 1017.4)
    new: |-
      taken out of rule-morph (case 1017.4)
      - Whether every Estimate whose `method` reads the transcript of a session should be a one-off Estimate of the sprint page with `once: true`, with a lasting Estimate beside it whose `method` reads a file that ships, as `rule-estimates-schema` would then set it; the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
  change: the Backlog asks whether every Estimate that reads a transcript is split into a one-off Estimate and a lasting one
```

```tasks
- [ ] update `entity-sprint-plugin`
```

## Case 1020 — The source pictures of the icon live in plugin/assets/

> **context:**
> The icon of the plugin, `.guppi/icon.png`, was made in case 1016 from two source pictures: `icon_guppi.png`, the fish alone, and `logo_guppi.png`, the logo with the word. At the stop of Work Mode of session 0316 the person put both in `guppi-assets/` at the root of the repository until a place was chosen (the handoff of session 0316). No live page names that folder: a Grep of `guppi-assets` over the repository, `vault/raw/` left out, printed `vault/wiki/brief.md` alone. A Grep of `icon_guppi|logo_guppi` over `vault/wiki/` printed `lesson-case-build-crop-spec-ignores-the-alpha-channel`, which names the source `.guppi/icon_guppi.png`, where the picture stood in session 0316; it stands, since a lesson is a record of that session. The person chose `plugin/assets/`, beside `plugin/plugin.json`, the manifest whose field `icon` names the icon, and `rule-clean-branch` as the page that says so, since its Purpose already describes the icon, the manifest and the folder `plugin/`, and its `implementation_ref` names `plugin/plugin.json` and `plugin/marketplace.json`. I read in `.guppi/guppi/ship.py` the constants `ROOT_FILES`, `TREES`, `PLUGIN_FILES` and `PLUGIN_SKILLS` and the functions `tree_files`, `plan` and `check`: `plan` takes the root files, `.guppi/` and `.claude/` by `tree_files`, the CI file, `vault/.gitignore`, the schemas, `tags.md`, the pages, the two files of `PLUGIN_FILES` by name and each file under `plugin/skills/`, and `check` judges only the files `plan` gives, so a file under `plugin/assets/` is neither written nor judged, and the sentence of the docstring of `ship.py` that no file of `plugin/` is written at its own path stays true. `lint` of `.guppi/guppi/lint.py` reports a path of `implementation_ref` for which `exists()` is false, and a folder passes that test, so `plugin/assets` stands once Work Mode has moved the pictures, before the librarian's run. `rule-rules-schema` describes the field so:
> `implementation_ref`: required on `hook` and `check`; list of paths. The hook script, or the linter/test that performs the check.
> It stands: `rule-clean-branch` already lists the data files `plugin/plugin.json` and `plugin/marketplace.json` there, `guppi lint` judges only that each path exists, and the person chose this field as the one that lists the files of the rule. A Grep of `` plugin/|["'`(]plugin["'`)] `` over `.guppi/guppi/` printed `caseid.py`, whose hit is the sprint name `plugin` in `PLAIN_SPRINTS`, and `ship.py`; a Grep of `plugin/|guppi-assets` over `.claude/` printed nothing; a Grep of ``plugin/[a-z]|`plugin/`|folder `plugin/` `` over `vault/wiki/rules/` printed `rule-clean-branch.md`, which this Case changes, and `rule-plugin-install.md`, whose hits name `plugin/skills/install/SKILL.md`, which the move does not touch. A Grep of `\bassets\b` over `{.guppi/guppi,.claude,vault/wiki/rules}/**` printed nothing. A Grep of `` ["'`(]plugin["'`)/] `` over `vault/wiki/rules/` printed `rule-clean-branch.md`, `rule-plugin-install.md` and `rule-ratification.md`, whose hit is the sprint name `plugin`; a Grep of `` ["'`(]plugin["'`)/]|\bplugin\b `` over `.claude/` printed `.claude/skills/sprint-open/SKILL.md`, whose hit is the sample sprint id `kir-plugin`; none of them reads the files of the folder. `.gitattributes` applies `* text=auto eol=lf` to every file of the repository, `plugin/assets/` included; its comment above that line says git decides by a NUL byte, so images stay untouched, and the move changes no byte of the pictures. A Grep of `os\.walk|rglob|\.glob\(|iterdir` printed 14 files under `.guppi/guppi/` and 15 under `.guppi/tests/`; of the walks that could reach `plugin/`, `tree_files` of `ship.py` walks `plugin/skills/` alone, `named_files` of `casecheck.py` walks `vault/wiki`, `.claude`, `.guppi/guppi` and `.guppi/tests` only, `callers` of `.guppi/tests/test_guppi_package.py` walks `.claude` and `.github/workflows`, and `tree` of `.guppi/tests/test_ship.py` copies `plugin/plugin.json` and `plugin/marketplace.json` by name; the others walk the vault, a session folder or a temporary folder. No `.gitignore` stands under `plugin/`, and the root `.gitignore` holds no line that matches a PNG, so git keeps tracking the pictures. The hook `guppi shellwrite` reads each file that `git ls-files -m -o --exclude-standard` lists after a shell call; I read `changed_files`, `judge` and `lines_for` of `.guppi/guppi/shellwrite.py`: `judge` returns no line for a file with a NUL byte and no UTF-16 mark, which a PNG holds in its first chunk, so the move by `git mv` trips nothing. The Purpose sentence of `rule-clean-branch` that says the clean version does not hold `plugin/` stays true and gains the new one. Of the Estimates of `rule-clean-branch`, the purposes of `estimate-clean-branch-writes-a-clean-copy` and `estimate-clean-branch-ships-the-plugin-icon` speak of what the clean version holds; I read both Criteria whole: the first lists what the build writes and its exceptions, the second the icon alone, and neither says the build writes no other file of `plugin/`, so both stand and the new Estimate makes that promise. Of the files that name `rule-clean-branch`, `ship.py`, `guppi ship`, `test_ship.py` or `prod.yml`, I read those whose purpose speaks of what the clean version holds or installs: the Then of `estimate-clean-branch-installs-as-a-plugin` says the clean version holds no folder `plugin/`, which the move keeps; the Then of `estimate-plugin-install-writes-guppi-into-an-empty-project` and step 2 of the Render of `rule-plugin-install` copy each file of the installed plugin, which holds no file of `plugin/assets/`; `estimate-sprint-plugin-installs-as-a-plugin` promises an install with no error, which the move keeps; and the Then of `estimate-guppi-package-runs-from-its-own-folder` speaks of what stands under `.guppi/`, which the move does not touch; so each stands. The others speak of pointers, drafts, the setup, the tests, the session files, schemas, lint or the install of `uv`, which the Case does not touch. The test `test_it_writes_the_code_the_harness_and_the_core_pages_only` compares the exact set of written files over a sample tree that holds no file under `plugin/assets/`, so it stands; the docstring of `.guppi/tests/test_ship.py` lists its tests by the names they hold and gains the new ones. The README of the milestone The plugin of `entity-sprint-plugin` may later show the logo from `plugin/assets/`; this Case sets nothing on it. The session's ledger holds no `error` lesson.

> **problem:**
> The two source pictures of the plugin icon sit in a folder at the root of the repository that no rule names, put there only until a place was chosen.

> **recommend:**
> - **Where the two source pictures live for good**
>   - Recommended: (b) they move to `plugin/assets/`, beside the manifest that names the icon made from them.
>   - Answer: agreed, (b).
> - **Which page says where the pictures live**
>   - Recommended: (a) `rule-clean-branch`, a sentence in its Purpose and `plugin/assets/` in its `implementation_ref`.
>   - Answer: agreed, (a).
> - **How the new place is checked**
>   - Recommended: (a) a new Estimate on `rule-clean-branch`, `estimate-clean-branch-leaves-out-the-source-pictures`, checked by a new test of `.guppi/tests/test_ship.py`.
>   - Answer: agreed, (a).

> **given:**
> `rule-clean-branch`: the rule of the clean version, whose Purpose names the icon and the folder `plugin/`.
> **＋** `estimate-clean-branch-leaves-out-the-source-pictures`: the new check that the clean version holds no source picture.
> **＋** `plugin/assets/`: the new folder of the two source pictures of the icon.
> **＋** `plugin/assets/icon_guppi.png`: the fish alone, the picture the icon is made from.
> **＋** `plugin/assets/logo_guppi.png`: the logo with the word.
> **＋** `guppi-assets/`: the folder that holds the pictures now.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, which takes files of `plugin/` only by name.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.

> **when:**
> `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, from a working tree that holds a picture under `plugin/assets/`.
> **＋** `uv run --project .guppi guppi ship --check` judges that working tree.

> **then:**
> The clean version holds no file of `plugin/assets/`, at that path or at any other.
> **＋** `uv run --project .guppi guppi ship --check` prints no line on a file of `plugin/assets/`.
> **＋** The repository of GUPPI holds `plugin/assets/icon_guppi.png` and `plugin/assets/logo_guppi.png`, and no folder `guppi-assets/`.
> **－** What the pictures under `plugin/assets/` show is no part of this promise: neither the build nor `--check` reads them.

```then
create:
- slug: estimate-clean-branch-leaves-out-the-source-pictures
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the clean version holds no file of plugin/assets/, guppi ship --check prints no line on one, and the repository keeps both source pictures of the icon there and no folder guppi-assets/
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k source_pictures
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: which no branch of this repository loads as a plugin and which the clean version does not hold (case 816).
    new: which no branch of this repository loads as a plugin and which the clean version does not hold (case 816). The folder `plugin/assets/` of this repository holds the two pictures the icon is made from, `icon_guppi.png`, the fish alone, and `logo_guppi.png`, the logo with the word; `guppi ship` writes no file of it, and `guppi ship --check` judges none (as set in case 1020).
  set:
    implementation_ref:
    - .guppi/guppi/ship.py
    - .guppi/tests/test_ship.py
    - .github/workflows/prod.yml
    - plugin/plugin.json
    - plugin/marketplace.json
    - plugin/assets
  change: the source pictures of the icon live in plugin/assets/, which the clean version does not take
```

```tasks
- [ ] update `rule-clean-branch`
- [ ] create `estimate-clean-branch-leaves-out-the-source-pictures`
- [x] `plugin/assets/icon_guppi.png`: moved from `guppi-assets/icon_guppi.png` by `git mv`, byte for byte.
- [x] `plugin/assets/logo_guppi.png`: moved from `guppi-assets/logo_guppi.png` by `git mv`, byte for byte.
- [x] `guppi-assets/`: removed once it is empty.
- [x] `.guppi/tests/test_ship.py`: tests whose names hold `source_pictures`: a sample tree with a PNG under `plugin/assets/`, whose copy holds no file of that name at any path and on which `--check` prints no line; and the working tree of the repository holds both pictures under `plugin/assets/` and no `guppi-assets/`; the module docstring names these tests and the new Estimate.
- [ ] read `estimate-clean-branch-leaves-out-the-source-pictures`
```

## Deferred

## Case 1021 — The milestone The plugin put off

> **context:**
> The brief of session 0316 gives, under the `Cases` of its Next session, the milestone The plugin: the clean version installed by hand, whose reading now also covers the setup of Case 1017, the README and the close of `plugin`. The person put it off at `/hi` of session 1825, together with the readings W1, W2 and W5 that need the same install by hand. The items stand under `## Milestones` of `entity-sprint-plugin`.

> **problem:**
> No Case of this session sets when the clean version is installed by hand, when the README is written, or when the sprint `plugin` closes.

```then
defer:
  - slug: entity-sprint-plugin
    type: entity
    purpose: "The milestone The plugin: the clean version installed by hand, the README and the close of plugin; put off at /hi of session 1825"
```
