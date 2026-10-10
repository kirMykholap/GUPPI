<!-- approved 16:50:55 · session cd5dfbba -->

# Spec — session 0200, 2026-10-09

## Case 746 — The two sprint skills sit under their phases, and their Estimates are read again

> **context:**
> Case 743 created two skill pages, `rule-skill-sprint-open` and `rule-skill-sprint-close`. Their `create` items held no `type: rule`, so `guppi materialize` marked all four `create` lines `incomplete: [type]`, and the Retro of session 2352 set `estimate-skill-sprint-open-asks-the-opening-questions` and `estimate-skill-sprint-close-leads-the-closing-session` `failed` without a reading. The pages were built anyway: `guppi/generate.py` takes the type of a new page from its category when the item gives none, so both pages hold `type: rule`, and `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/sprint-close/SKILL.md` hold the Renders that Case 743 signed. One thing went wrong. Case 743 was ratified again at `/pre-spec` with new parents, and `generate` treats a second line of the same Case, kind and slug as a repeat that changes no page (case 514). The pages kept the first `ref`, `rule-session`, and `rule-session` lists them among its children. That makes its Purpose sentence about the five phases false, and it makes false the line of `estimate-session-phases-in-order` that its children are the five phases, while that Estimate stands `passed`.
>
> The person chose to fix the live pages and not to build Case 743 again: a second `create` would collide with a page that exists, and a `{supersedes:case 743.6}` mark would set Decision pages `superseded` whose work stands. 746.1 sets `parent` on the two skill pages and `children` on `rule-session`, `rule-session-start` and `rule-plan-mode`. `case-schema.md` says that `parent` from `ref` and `children` are derivable fields, filled mechanically and not written in the `then` block. That sentence stands, since `guppi/generate.py` derives them only when it creates a page: a `create` with a `ref` sets `parent` and adds the slug to the `children` of the parent, while an `update` writes each key of its `set` onto the page as given and moves no backlink. `frontmatter` writes both fields as links, by `REF_FIELDS` of `guppi/pages.py`. So no step moves a page that exists, and the move writes both sides, the form of case 39, whose Spec in `vault/archive/migration/2026-09-10/raw/spec.md` set `parent` on `rule-hook-registry` and `children` on `rule-session-start`. The Grep `^(children|parent):` over `vault/wiki/rules/` with the glob `rule-{session-start,plan-mode,skill-hi,skill-*}.md` printed `rule-skill-hi` under `rule-session-start` and `rule-skill-grill-me` and `rule-skill-wait-what` under `rule-plan-mode`, so after the move every skill page sits under a phase. The Grep `rule-skill-sprint-(open|close)` over the repository outside `vault/archive/` and `vault/raw/` printed 15 files. Besides the pages of `given`, the hits in `rule-sprint`, `rule-orchestration`, `vault/wiki/orchestration.md`, `estimate-sprint-marks-a-closed-sprint`, `estimate-skill-sprint-open-starts-at-hi`, `lesson-case-build-rule-create-without-type`, `guppi/sprint.py` and `tests/test_sprint.py` name the skills or their hook and not their parent, so they stand. I did not read the hits in `brief.md` and `log.md`.
>
> 746.1 sends `estimate-session-phases-in-order` back for a reading with its Criterion unchanged, since the move makes its line about children true again. Its old method read the marks of a session at the close of that session, up to the librarian's commit, which comes after the session ends, so the check of the case file refused it. The person chose a method that runs at the Retro of this session: `make test-session`, the marks of the last finished session in time order, and the children that the Spec of this session sets. `estimate-session-start-context`, `estimate-plan-mode-verified` and `estimate-plan-mode-names-its-estimates` speak of the ledger hook and of the checks of Plan Mode, not of the children of their rules, so they stand. In `rule-session-start` the sentences that number the children 2 to 4 as hooks stay true, since the new child stands last. 746.2 and 746.3 send the two failed Estimates back for a reading at the Retro of this session, their Criteria unchanged and their `method` moved to this session, since the moment their old method named has passed. Their `then` blocks are the Criteria of the two Estimates as they stand, so the line of 746.2 that the opening Case is the first the session ratifies and the line of 746.3 that the closing session ratifies only the closing Case and the Cases that prepare its readings are two promises of two skills, and both stand.
>
> Not done: this Case leaves the causes to other Cases of this session. Case 748 has `materialize` fill `type` from the category and has the checks before the Spec report a missing required field, the cause of `lesson-case-build-rule-create-without-type`. Case 749 has the check of a case file send back a rebuilt Case that changes the `ref` or the tags of a `create` line, and sets `insight-ledger-ratified-line-never-withdrawn` `actioned`, whose cascade archives `lesson-ledger-rebuilt-create-keeps-the-stale-ref`. The `incomplete` and repeat marks in the `materialize.yaml` of session 2352 stay as they are, since no script reads that yaml again.

> **problem:**
> The two sprint skill pages hang under `rule-session` and not under the phases that Case 743 named. `rule-session` therefore lists more than its five phases while the Estimate of that list stands `passed`. The two Estimates of the skills are `failed` without a reading, and the moment their method names has passed.

> **recommend:**
> - **What this Case does with the earlier Case**
>   - Recommended: (a) fix the live pages only; Case 743 and its ledger lines stay as they are, and the stale-line mechanism and the missing check of the type field stay separate Frontier items.
>   - Answer: agreed, (a).
> - **Where the two skill pages sit**
>   - Recommended: (a) move them under their phases as signed: `rule-skill-sprint-open` under `rule-session-start` and `rule-skill-sprint-close` under `rule-plan-mode`, and `rule-session` lists the five phases alone.
>   - Answer: agreed, (a).
> - **How the two failed Estimates get read**
>   - Recommended: (a) send both back for a reading at the Retro of this session, their Criteria unchanged and their method moved to that reading of the live pages and skill files.
>   - Answer: agreed, (a).
> - **How the move of the two skill pages is checked**
>   - Recommended: (b) send `estimate-session-phases-in-order` back for a reading, its Criterion and method unchanged, read at the close of this session.
>   - Answer: agreed, (b).
> - **When the phases Estimate is read**
>   - Recommended: (a) a method that runs at the Retro of this session: the session test run, the marks of the last finished session in time order, and the children of `rule-session` as the Spec of this Case sets them; the Criterion unchanged.
>   - Answer: agreed, (a).

### Case 746.1 — The two sprint skill pages sit under their phases

> **given:**
> `rule-skill-sprint-open`: the skill page of the opening of a sprint, whose `parent` changes.
> **＋** `rule-skill-sprint-close`: the skill page of the close of a sprint, whose `parent` changes.
> **＋** `rule-session`: the page of the phases of a session, whose `children` change.
> **＋** `rule-session-start`: the phase that takes the opening skill as a child.
> **＋** `rule-plan-mode`: the phase that takes the closing skill as a child.
> **＋** `estimate-session-phases-in-order`: the check of the children of `rule-session`, sent back for a reading.

> **when:**
> Someone reads the `parent` field of `rule-skill-sprint-open` and `rule-skill-sprint-close` and the `children` field of `rule-session`, `rule-session-start` and `rule-plan-mode`.

> **then:**
> `rule-skill-sprint-open` names `rule-session-start` as its parent, and `rule-session-start` lists it last among its children.
> **＋** `rule-skill-sprint-close` names `rule-plan-mode` as its parent, and `rule-plan-mode` lists it last among its children.
> **＋** `rule-session` lists neither skill page among its children, and its other children keep their order.
> **－** The `Purpose` and the `Render` of `rule-skill-sprint-open` and `rule-skill-sprint-close` do not change.

```then
update:
- slug: rule-skill-sprint-open
  set:
    parent: rule-session-start
  change: the parent is rule-session-start, as case 743.6 set it (case 746.1)
- slug: rule-skill-sprint-close
  set:
    parent: rule-plan-mode
  change: the parent is rule-plan-mode, as case 743.8 set it (case 746.1)
- slug: rule-session
  set:
    children:
    - rule-session-start
    - rule-plan-mode
    - rule-work-mode
    - rule-end-of-work
    - rule-documentation
  change: the children are the five phases alone; the two sprint skill pages hang under their phases (case 746.1)
- slug: rule-session-start
  set:
    children:
    - rule-skill-hi
    - rule-event-log
    - rule-ledger-write
    - rule-compact-recall
    - rule-skill-sprint-open
  change: child rule-skill-sprint-open added (case 746.1)
- slug: rule-plan-mode
  set:
    children:
    - rule-ask
    - rule-prespec-hook
    - rule-prespec
    - rule-spec-capture
    - rule-case-protocol
    - rule-spec-write
    - rule-spec-reconcile
    - rule-case-build
    - rule-case-check
    - rule-skill-grill-me
    - rule-skill-wait-what
    - rule-prespec-onward
    - rule-orchestration
    - rule-ratification
    - rule-case-example
    - rule-skill-sprint-close
  change: child rule-skill-sprint-close added (case 746.1)
- slug: estimate-session-phases-in-order
  set:
    status: pending
    method: make test-session, the pipeline over the tests of rule-session's children; then by hand at the Retro of the session of case 746 — the marks of the last finished session, the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md and the commit of its Documentation phase, read in that order, and the children of rule-session as the Spec of case 746 sets them
  sections:
    Criterion: |-
      When:
      A session has ended, and someone reads its folder, the day's event log and `git log`.

      Then:
      All five phases left a mark, and the marks ascend in time: the `hi` line of the day's event log → `frontier.md` → `spec.md` with its approved stamp → the Retro commit → `handoff.md` → the librarian's commit.
      **＋** `rule-session` is the parent of the five phases, its children in that order.
      **－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.
  change: 'sent back for a reading at the Retro of the session of case 746, the Criterion unchanged: rule-session listed the two sprint skill pages among its children (case 746.1)'
```

```tasks
- [x] update `rule-skill-sprint-open`
- [x] update `rule-skill-sprint-close`
- [x] update `rule-session`
- [x] update `rule-session-start`
- [x] update `rule-plan-mode`
- [x] update `estimate-session-phases-in-order`
- [x] read `estimate-session-phases-in-order`
```

### Case 746.2 — `/sprint-open` is read again against its Criterion

> **given:**
> `rule-skill-sprint-open`: the rule whose Render is the skill `/sprint-open`.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill rendered from it.
> **＋** `estimate-skill-sprint-open-asks-the-opening-questions`: the check of what the skill has the opening Case ask, sent back for a reading.
> **＋** `rule-skill-hi`: `/hi`, whose Frontier puts the line that opens the next sprint first.
> **＋** `vault/wiki/backlog.md`: the list of the items put off, which the opening Case counts.
> **＋** `vault/wiki/sprint.md`: the file whose heading marks the last sprint closed.
> **＋** `case-guppi`: the agent that builds the opening Case and puts each question to the person.
> **＋** `/sprint-close`: the skill that the close line names.

> **when:**
> The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

> **then:**
> The main agent assembles the Frontier as `rule-skill-hi` sets it, the line `open the next sprint` first under `## Cases`.
> **＋** When the person takes up that line, the main agent dispatches `case-guppi` with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
> **＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
> **＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
> **＋** The opening Case is the first Case the session ratifies.
> **－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
> **－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

```then
update:
- slug: estimate-skill-sprint-open-asks-the-opening-questions
  set:
    status: pending
    method: by hand, at the Retro of the session of case 746, the live Render of rule-skill-sprint-open and .claude/skills/sprint-open/SKILL.md read against the Criterion
  change: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.2)
```

```tasks
- [x] update `estimate-skill-sprint-open-asks-the-opening-questions`
- [x] read `estimate-skill-sprint-open-asks-the-opening-questions`
```

### Case 746.3 — `/sprint-close` is read again against its Criterion

> **given:**
> `rule-skill-sprint-close`: the rule whose Render is the skill `/sprint-close`.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill rendered from it.
> **＋** `rule-orchestration`: the rule that no longer holds the paragraph on the closing session.
> **＋** `vault/wiki/orchestration.md`: the text rendered from `rule-orchestration`.
> **＋** `entity-sprint-migration`: the sprint page whose close line takes the fixed form.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian's frame, which runs the close line.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: the check of the skill, sent back for a reading.

> **when:**
> The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

> **then:**
> When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
> **＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
> **＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
> **＋** When the sprint ran on a branch of its own, the closing Case holds a task line for the merge of that branch into the main branch, which Work Mode leaves unticked, so that the brief gives it as Work to the session that opens the next sprint.
> **＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
> **＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
> **＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
> **－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.

```then
update:
- slug: estimate-skill-sprint-close-leads-the-closing-session
  set:
    status: pending
    method: by hand, at the Retro of the session of case 746, the live Renders of rule-skill-sprint-close and rule-orchestration, .claude/skills/sprint-close/SKILL.md, vault/wiki/orchestration.md and entity-sprint-migration read against the Criterion
  change: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.3)
```

```tasks
- [x] update `estimate-skill-sprint-close-leads-the-closing-session`
- [x] read `estimate-skill-sprint-close-leads-the-closing-session`
```

## Case 747 — The round check is read by a staged run of the hook

> **context:**
> When `case-guppi` stops, the `SubagentStop` hook `uv run guppi casecheck --subagent` reads its newest output. If that output is a round with a question out of the grill-me form, the hook exits 2 and tells the agent to give the round whole again. `estimate-case-check-sends-back-a-faulty-round` holds that promise. Case 744.2 replaced its Criterion so that the After line of an option passes with or without its list dash, and the Retro of session 2352 set it `failed` without a reading. The pytest part of its method passed, 13 tests. The by-hand part asked for a round the hook sends back live, with its stderr and the round the agent gave again, and none occurred after the change. A live send-back happens only when the agent happens to write a faulty round, so every later change of this promise can fail the same way. The last live send-back was read on 2026-10-04 (ledger line 37 of session 2041). The person chose a staged run in place of the live part: at the Retro of this session the hook command runs by hand from the repository on a copy of a real `case-guppi` transcript of this session that ends with a faulty round. The run cannot show the agent answering again. The person chose to drop that clause from the Criterion, which now ends at what the hook does. That the subagent answers again after an exit 2 is a fact of Claude Code, recorded in `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back`, and not a judgment of this check. The Criterion is replaced whole. The one old line not carried word for word is the line on the exit 2 of a round, which keeps its words up to the clause that `case-guppi` answers again and drops that clause; the other lines are carried word for word. The `purpose` of the Estimate speaks of what the check sends back and leaves alone, and not of the agent answering again, so it stands.
>
> The staged copy is cut after a round and before any `Write` of a case file. With no written case file and no Case heading in the output, `subagent` of `guppi/casecheck.py` returns from `send_back` before it reads the plan file. So the staged runs store nothing in the plan of the session. No code changes. `rule-case-check` does not state that the agent answers again, so its text stands. The Grep `round whole again|answers again` over the repository root, with the glob `{vault/wiki/**/*.md,.claude/**/*.md,guppi/*.py}`, printed `vault/wiki/log.md`, `vault/wiki/insights/insight-hi-skill-substitution-checked-by-a-model-call.md`, `vault/wiki/lessons/lesson-hooks-subagentstop-exit-2-sends-the-subagent-back.md`, `vault/wiki/rules/rule-case-build.md`, `guppi/casecheck.py`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-round.md` and `vault/wiki/estimates/estimate-case-check-sends-back-a-clash-with-another-case.md`. The hits in `log.md` and in the History of `rule-case-build` were not read. The insight speaks of a server that answers again, not of the agent. The docstring of `guppi/casecheck.py` says that the hook tells the agent to answer again, which stays true. The Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` promises that `case-guppi` answers again after a clash finding. That is another promise, read by its own method, which this Case does not touch, so it stands. Case 746 of this session sets other readings at the same Retro and touches no page of this Case.

> **problem:**
> `estimate-case-check-sends-back-a-faulty-round` stands `failed` because its method waits for a faulty round that only chance produces. One line of its Criterion promises an act of the agent that no run of this check can show.

> **recommend:**
> - **How should the failed reading of the round check be closed?**
>   - Recommended: (b) read it again at the end of this session, with a staged run of the hook command on a copy of a real agent transcript ending in a faulty round, in place of the live part.
>   - Answer: agreed, (b).
> - **Does the promise keep the line that the agent answers again?**
>   - Recommended: (a) drop that line from the promise; it ends at what the hook does, and the other lines stay word for word.
>   - Answer: (a).

> **given:**
> `estimate-case-check-sends-back-a-faulty-round`: the check of the form of a round; its Criterion is replaced whole and its `method` changes.
> **＋** `rule-case-check`: the rule of the check whose code judges the form of a round.
> **＋** `guppi/casecheck.py`: `is_round`, `QUESTION_LINE`, `round_form` and `faulty_round`, the code the check runs.
> **＋** `tests/test_casecheck.py`: the tests of the form of a round.
> **＋** `.claude/settings.json`: the `SubagentStop` registration of `uv run guppi casecheck --subagent`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template the check judges a round against.
> **＋** `.claude/agents/case-guppi.md`: the agent whose rounds the check reads.

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

> **then:**
> `uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That holds when it holds no Case heading, no line that opens with `**Fact:**` stands before its first line that opens with `❓`, and one of its lines opens with the mark `❓`, with the indent of each line set aside.
> **＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
> **＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
> **＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
> **＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line after it, before the next line that opens with `🔹` or `➡️`, that opens with `**After:**` or with `- **After:**`.
> **＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again.
> **－** A round gets none of the checks of a Case in the same run, and no earlier Case of the transcript is checked for it, so the exit 2 of a round carries the findings of its form alone.
> **－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
> **－** A round in form gives no finding and prints nothing of its own.
> **－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
> **－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
> **－** A round as the main agent shows it in the chat is not judged here.

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-round
  set:
    status: pending
    method: 'uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand at the Retro of the session of case 747, uv run guppi casecheck --subagent run from the repository with a payload on stdin of agent_type case-guppi and an agent_transcript_path to a copy, in the scratchpad, of a transcript of a case-guppi of that session cut after a round and before any Write of a case file: the copy as cut exits 0 and prints nothing; the copy with the colon removed from a title line of its last round exits 2, its stderr naming that question, the title line it misses, and telling case-guppi to answer with the round whole again; the same faulty round added again as a later output exits 0; the plan file of the session is unchanged by the runs'
  change: the Criterion replaced whole — the clause that case-guppi answers again leaves it, and the live send-back of the method gives way to a staged run of the hook command at the Retro (case 747)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-faulty-round`
- [x] read `estimate-case-check-sends-back-a-faulty-round`
```

## Case 748 — A new page takes its type from its folder, and a missing required field is caught before the Spec

> **context:**
> `guppi materialize` lists, in `REQUIRED` of `guppi/materialize.py`, the fields that a `create` item must write for each category: `type`, `kind`, `purpose` and `tags` for a rule or an entity, `kind`, `purpose` and `method` for an Estimate, `pattern`, `children` and `tags` for an Insight. It marks a missing one `incomplete` only after ratification, and nothing before the Spec judges these fields: `judge` of `guppi/prespec.py` checks the keys an item may hold (`check_keys`) and the conditions of a schema (`check_conditions`, case 714), and `created_page` fills `type` from the category, so a missing `type` gives no finding there. In session 2352 the `create` items of `rule-skill-sprint-open` and `rule-skill-sprint-close` (Cases 743.6, 743.8) held no `type: rule`, `materialize` marked them `incomplete: [type]`, and the Retro read the mark as a page not built, while `guppi/generate.py` had written both pages with `type: rule` taken from the category (lesson `lesson-case-build-rule-create-without-type`, Case 746). The `type` of a page never needs a judgment: it follows from the slug prefix, and `_lift_item` already fills `type: estimate` for an Estimate.
>
> The person chose two parts. 748.1 has `materialize` fill `type` from the category for every `create`, as it does for an Estimate, so a missing `type` is no longer `incomplete`; a new Estimate checks it, and `estimate-materialize-assembles` stands, since a type taken from the slug prefix is derived like `category`, not invented. `estimate-materialize-lifts-a-create-by-the-schema` stands too: its Criterion lets only the fields of the category's `schema.yaml` reach `fields`, and `type` is a required field of each `schema.yaml` of the four categories. The map from a category to its type is `SINGULAR` of `guppi/generate.py`, which `generate` and `created_page` of `guppi/prespec.py` use, while `_lift_item` writes `type: estimate` as a literal of its own; `guppi/generate.py` imports `guppi/materialize.py`, so the map moves into `guppi/materialize.py`, and the lift, `generate` and `guppi/prespec.py` all read that one map (found by the pre-spec run of `ask-guppi`). 748.2 has `judge` give a finding for a `create` item that lacks any other required field, by one function of `guppi/materialize.py` that the lift and `guppi/prespec.py` both call; it is a finding, not a note, and a new Estimate checks it, while `estimate-prespec-hook-reports-a-schema-condition-not-met` stands, since an unmet condition and a missing plain field fail apart and are fixed in different code. `judge` runs in `/pre-spec`, in the check of a case file of `rule-case-check` and in the check after a write of `rule-spec-write`, so all three take the finding with no change to those rules. The tags of a `create` stand on its decision line as well as in its item, and the lift counts either, so the check counts either too. An Estimate with no `method` already gets a finding of `check_form` (case 331), so the new check gives no second one for it.
>
> The pages stand. `rule-materialize` says that what is missing is named and not invented, and a type taken from the slug prefix is neither. `rule-prespec-hook` points to the module docstring of `guppi/prespec.py` for what the check compares, and that docstring takes the new finding in Work Mode. `case-schema.md` says that a `create` holds the fields the target schema needs a judgment for, and `type` needs none. `vault/wiki/case-example.md` writes `type`, `kind`, `purpose` and `tags` for `entity-cart` and `kind`, `purpose` and `method` for its Estimate, so the test of `tests/test_case_schema.py` that runs the check over that live file finds nothing new. The Glob `vault/**/estimate-*{fills-the-type,required-field}*.md` printed nothing, so both new slugs are free.
>
> Not done: a put-off item with no `purpose` is still marked only after ratification, by the person's choice, and the `incomplete: [parent]` of a Leaf rule with no `ref` and no `parent` stays a mark of the lift alone. The lesson came from an earlier session, so no decision line carries `{addresses:...}`.

> **problem:**
> A `create` item can reach the ratified Spec without a field that `materialize` requires, since nothing before the Spec judges those fields. Among them, `type` is one that the page writer derives anyway, so its absence raises a false mark that a Retro read as a page not built.

> **recommend:**
> - **What the fix does about the type field**
>   - Recommended: (a) fill the type, check the rest: `materialize` fills `type` from the folder for every new page, and `/pre-spec` and the check of each case file report a new page whose item lacks any other required field, by one list the tool uses; two parts with a check each.
>   - Answer: agreed, (a).
> - **Whether a missing field stops the Case or only warns**
>   - Recommended: (a) a finding, which sends the case file back and keeps `/pre-spec` from passing, as for an unmet schema condition.
>   - Answer: agreed, (a).
> - **How the filled-in type is checked**
>   - Recommended: (a) a new check of its own on `rule-materialize`, read by a test in this session; `estimate-materialize-assembles` stays as it is.
>   - Answer: agreed, (a).
> - **How the new missing-field check is checked**
>   - Recommended: (a) a new check of its own on `rule-prespec-hook`, read by a test in this session; `estimate-prespec-hook-reports-a-schema-condition-not-met` stays as it is.
>   - Answer: agreed, (a).
> - **Whether a put-off item is checked too**
>   - Recommended: (a) new pages only; a put-off item with no `purpose` is still marked only after ratification.
>   - Answer: agreed, (a).

### Case 748.1 — `materialize` takes the type of a new page from its category

> **given:**
> `guppi/materialize.py`: the lift of a `create` item into its entry.
> **＋** `guppi/generate.py`: the page writer, which takes the type of a page from the same map.
> **＋** `guppi/prespec.py`: the check of a plan, whose `created_page` takes the type from the same map.
> **＋** `tests/test_materialize.py`: the tests of the lift.
> **＋** `rule-materialize`: the rule of the lift, which the new Estimate checks.
> **＋** `estimate-materialize-fills-the-type-from-the-category`: the new check of the filled type.

> **when:**
> `uv run guppi materialize` lifts a `create` item of a page of `rules`, `entities`, `estimates` or `insights` from the `then` block of its Case.

> **then:**
> When the item writes no `type`, the `fields` of the entry hold the `type` of its category: `rule`, `entity`, `estimate` or `insight`.
> **＋** The entry carries no `incomplete: [type]`.
> **＋** The type of each category is one map of `guppi/materialize.py`, which the lift, `guppi/generate.py` and `guppi/prespec.py` read.
> **＋** A missing `kind`, `purpose`, `tags`, `method`, `pattern` or `children` is still named under `incomplete`, as before.
> **－** A `type` that the item writes stands as written.
> **－** The `type` of a `defer` item is its own key and is not filled.

```then
create:
- slug: estimate-materialize-fills-the-type-from-the-category
  ref: rule-materialize
  kind: QA
  purpose: Whether materialize gives a create item with no type the type of its category, and marks no incomplete type
  method: uv run pytest tests/test_materialize.py -k type_from_the_category
  tags:
  - harness
  - workflow
  - ledger
```

```tasks
- [x] create `estimate-materialize-fills-the-type-from-the-category`
- [x] `guppi/materialize.py`: `SINGULAR` moves here from `guppi/generate.py`; `_lift_item` fills `type` by it for every `create` item that writes none, in place of its literal `type: estimate`, and the module docstring says so.
- [x] `guppi/generate.py` and `guppi/prespec.py`: import `SINGULAR` from `guppi/materialize.py`; no second copy of the map stays.
- [x] `tests/test_materialize.py`: tests named `type_from_the_category` — a rule and an entity `create` with no `type` get it and no `incomplete: [type]`, a written `type` stands, a missing `purpose` is still `incomplete`.
- [x] read `estimate-materialize-fills-the-type-from-the-category`
```

### Case 748.2 — Pre-spec reports a `create` item without a required field

> **given:**
> `guppi/prespec.py`: the judgment of a plan, `judge`.
> **＋** `guppi/materialize.py`: the module that holds the list of required fields and the judgment of what is missing.
> **＋** `tests/test_prespec.py`: the tests of the judgment.
> **＋** `rule-prespec-hook`: the rule of the check, which the new Estimate checks.
> **＋** `rule-case-check`: the check of a case file, which runs `judge`.
> **＋** `rule-spec-write`: the check after ratification, which runs `judge`.
> **＋** `estimate-prespec-hook-reports-a-create-without-a-required-field`: the new check of the finding.

> **when:**
> `judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` item of a page of `rules`, `entities`, `estimates` or `insights` in the `then` blocks.

> **then:**
> A `create` item that lacks a field which `guppi materialize` would name under `incomplete` gives one finding that names the Case, the slug and the missing field.
> **＋** The list of required fields and the judgment of what is missing are one function of `guppi/materialize.py`, which the lift and `guppi/prespec.py` both call.
> **＋** A field counts as present when the item writes it as a key or under `sections`, and the tags count as present when the item or its decision line carries them.
> **－** The finding never names `type`, since the lift fills it from the category.
> **－** An Estimate with no `method` gives no second finding beside the one of the form of its method.
> **－** A `defer`, an `update` or a `delete` item gives no such finding.

```then
create:
- slug: estimate-prespec-hook-reports-a-create-without-a-required-field
  ref: rule-prespec-hook
  kind: QA
  purpose: Whether pre-spec reports a create item that lacks a field materialize requires, by one function of guppi/materialize.py, and gives none for a missing type
  method: uv run pytest tests/test_prespec.py tests/test_materialize.py -k required_field
  tags:
  - harness
  - workflow
  - schema
```

```tasks
- [x] create `estimate-prespec-hook-reports-a-create-without-a-required-field`
- [x] `guppi/materialize.py`: one function gives the required fields that a `create` item lacks, `type` filled first; `_lift_item` calls it.
- [x] `guppi/prespec.py`: `judge` reports each missing field by that function, the tags of the decision line counted, no second finding for a missing `method`; the module docstring lists the finding.
- [x] `tests/test_prespec.py`: tests named `required_field` — a rule `create` with no `purpose` or no `tags` gives a finding, one with no `type` gives none, tags on the decision line alone count, a `defer` with no `purpose` gives none, and the lift and the check answer alike over the same items.
- [x] read `estimate-prespec-hook-reports-a-create-without-a-required-field`
```

## Case 749 — A rebuilt Case that changes the parent or tags of a new page goes back with a new number

> **context:**
> Each time the person signs a Case, its decision lines are added to the session's ledger, and no line is ever removed; only a `{supersedes:case N}` mark retires one. When the librarian builds the pages, `guppi/generate.py` applies the first line of a Case for a page, and takes a later line of the same Case, kind and slug for a repeat that changes nothing (case 514). A new page takes its `ref`, its parent, and its tags from that line, not from the signed item (`_lift_item` of `guppi/materialize.py`), so when a rebuilt Case keeps a page and changes its parent or tags, the first line wins. In session 2352 Case 743 was ratified, built again at `/pre-spec` and ratified again: ledger lines 15 and 19 create `rule-skill-sprint-open` and `rule-skill-sprint-close` with `{ref:rule-session}`, and lines 27 and 28 create them with `{ref:rule-session-start}` and `{ref:rule-plan-mode}`. Both pages were built under `rule-session`, and Case 746 of this session moves them under their phases by `update` items that `generate` applies at the librarian's run. The check of the file `case-guppi` writes already sends back a rebuilt Case that drops or renames a page, with a new number and the marks (`target_findings` of `guppi/casecheck.py`, case 671.1), but it judges only the kind and the slug of a line, so a changed `ref` or tag list passes.
>
> The person chose to extend that check and not the librarian's scripts: a rebuilt Case whose `create` line keeps its slug and changes its `ref`, or adds or removes a tag, goes back with a new number and the marks, and `case-guppi` either writes the line back as the ledger holds it or moves the Case to the new number. Only a `create` line is judged, since `guppi/generate.py` reads the `ref` of an entry only when it creates a page, and a decision line carries tags only on a `create` (`ratification.md`). The order of the tags does not count. The new promise gets an Estimate of its own. The Criterion of `estimate-case-check-sends-back-a-ratified-case-without-a-target` stands, since each of its lines speaks of its own check of a line with no item, and the two checks can fail apart. The Criterion of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` (case 610.1) stands too. Its lines speak of a Case built again in another shape, and each of its exceptions is scoped to its own check. Its line that the judgment and the new number come from one function of `guppi/casecheck.py` stays true, since the new finding takes its number from the same `new_number`. The Splitting paragraph of `rule-case-protocol` gains one sentence beside the sentence of case 671.1, which stays true. The Purpose of `rule-case-check` names neither the check of case 610.1 nor that of case 671.1, so it stands. `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` speak of the render and the form of a Case, not of a rebuilt Case, so they stand. `insight-ledger-ratified-line-never-withdrawn` is set `actioned` again, `addressed_by` this Case, so the cascade archives its `clustered` lesson `lesson-ledger-rebuilt-create-keeps-the-stale-ref`.
>
> The Grep `renamed or dropped|dropped or renamed|671\.1` over the repository, with the glob `!vault/{raw,archive}/**`, printed `guppi/casecheck.py`, `tests/test_casecheck.py`, `vault/wiki/case-schema.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/insights/insight-ledger-ratified-line-never-withdrawn.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-ratified-case-without-a-target.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The module and the test change in `tasks`. `case-schema.md` changes through the render. The hit in `rule-case-check` is a History line. The Pattern of the Insight stays as the record of what the lessons share. The hit in the Estimate is its own check, which stands. `backlog.md` is rendered from the live pages, and `log.md` is not read. The Grep `Path\(__file__\)|parents\[1\]|REPO|ROOT =` over `tests/` printed `tests/test_lint.py`, `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py`, `tests/test_materialize.py` and `tests/test_schemas.py`. The Grep `casecheck` over `tests/` printed `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_case_schema.py`, `tests/test_ledger.py`, `tests/test_onward.py`, `tests/test_orchestration.py` and `tests/test_materialize.py`, so of the six only `test_case_schema.py`, `test_orchestration.py` and `test_materialize.py` reach `guppi/casecheck.py`. `test_case_schema.py` runs `check_answer` with no store, and the check of a rebuilt Case runs only with a store. `test_orchestration.py` and `test_materialize.py` call other functions. So no test reads a live file through the new check. Case 748 of this session, which adds a check of the fields of a `create` item, was not written when this Case was built. Where it changes `guppi/casecheck.py` or the Splitting paragraph, the two texts are read side by side at `/pre-spec`.
>
> Not done: the ledger and `materialize.yaml` of session 2352 stay as they are. `guppi/generate.py` keeps its rule that a later line of the same Case, kind and slug is a repeat.

> **problem:**
> A Case that is ratified, built again and ratified again with a new parent or new tags for a page it creates leaves two `create` lines in the ledger. The librarian builds the page from the first, stale line, and no check before the Spec says so.

> **recommend:**
> - **Where the fix lives**
>   - Recommended: (a) the check of the case file sends the rebuilt Case back with a new number and the marks that retire the old lines, as it does for a dropped page.
>   - Answer: agreed, (a).
> - **Which parts of a line count as a change**
>   - Recommended: (b) the parent page and the tags.
>   - Answer: agreed, (b).
> - **Whether the pattern page closes**
>   - Recommended: (a) this Case marks `insight-ledger-ratified-line-never-withdrawn` handled, and the librarian archives the lesson of this item with it.
>   - Answer: agreed, (a).
> - **How the new check is checked**
>   - Recommended: (a) a new Estimate of its own on `rule-case-check`; `estimate-case-check-sends-back-a-ratified-case-without-a-target` stands unchanged.
>   - Answer: agreed, (a).
> - **Whether the order of the tags counts**
>   - Recommended: (a) order does not count; only a tag added or removed is a change.
>   - Answer: agreed, (a).
> - **What the send-back offers**
>   - Recommended: (a) the same two ways as for a dropped page: write the line back as the ledger holds it, or move the Case to the new number with the marks, by `Edit` alone.
>   - Answer: agreed, (a).

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`: the new check of the send-back.
> **＋** `rule-case-check`: the rule of the check of the file of a Case.
> **＋** `guppi/casecheck.py`: the check that `SubagentStop` runs on the file, beside `target_findings`.
> **＋** `tests/test_casecheck.py`: the tests of the new finding.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, whose `ratification` holds its new lines.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, which holds the lines already signed.
> **＋** `rule-case-protocol`: the rule whose Render `vault/wiki/case-schema.md` says how a rebuilt Case takes a new number.
> **＋** `insight-ledger-ratified-line-never-withdrawn`: the pattern page of this problem, set handled.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file, the decision lines of their `ratification`, and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

> **then:**
> For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the `create` lines of that number in the session's ledger.
> **＋** A `create` line of the ledger gives Case N a finding when the `ratification` of that number in the file holds a `create` line of the same slug whose `ref` differs, or whose tags differ by a tag added or removed.
> **＋** The finding names the number, the slug and both lines, and the number that `new_number` of `guppi/casecheck.py` gives. It also names the marks: one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it writes the line back as the ledger holds it, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
> **－** The same tags in another order, and a line that differs only by a `{supersedes}` or `{addresses}` mark, give no finding of this check.
> **－** A `create` line of the ledger whose slug has no `create` line under that number in the file gives no finding of this check.
> **－** An `update`, `delete` or `defer` line gives no finding of this check.
> **－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.

```then
create:
- slug: estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line
  ref: rule-case-check
  kind: QA
  purpose: Whether a Case that has a create line in the session and comes back from case-guppi under its number with another ref or another set of tags on that line goes back to case-guppi with a new number to build it under
  method: uv run pytest tests/test_casecheck.py -k changed_create_line
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: never writing the whole Case again (case 671.1).
    new: never writing the whole Case again (case 671.1). A Case that has a `create` line in the session's ledger and comes back in its shape with a `create` line of the same slug under the same number whose `ref` differs, or whose tags differ by a tag added or removed, is built under a new number too, its decision lines carrying the same marks, since the librarian builds the page from the first line and takes the later one for a repeat; the check of the file case-guppi writes sends it back with the new number, and case-guppi writes the line back as the ledger holds it, or changes the number in the headings and the ledger lines by `Edit` and adds the marks, never writing the whole Case again (case 749).
  change: a rebuilt Case whose create line changes its ref or its tags takes a new number, and the check sends it back (case 749)
- slug: insight-ledger-ratified-line-never-withdrawn
  set:
    status: actioned
    addressed_by: decision-case-749
  change: 'actioned: the check of the file case-guppi writes sends back a ratified Case built again whose create line changes its ref or its tags, with the new number and the marks (case 749)'
```

```tasks
- [x] create `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`
- [x] `guppi/casecheck.py`: a finding beside `target_findings`, run where it runs, that compares each `create` line of the ledger on a number of the file with the `create` line of the same slug in the file's `ratification`, by `ref` and by the set of tags, with the new number by `new_number` and the marks by `supersede_marks`; the module docstring names it.
- [x] `tests/test_casecheck.py`: under `changed_create_line`, a changed `ref` and a tag added are sent back with the new number and the marks; the same tags in another order, a line with an added `{supersedes}` mark, an `update` line with another `ref`, and a number with sub-cases give no finding of this check.
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] update `insight-ledger-ratified-line-never-withdrawn`
- [x] read `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`
```

## Deferred

## Case 750 — The initiation at install put off again

> **context:**
> The person put off `rule-morph` at the close of Plan Mode of session 0200. The lint reports it `deferred` 2 times since case 239. No Case of this session sets the category set of a project or the initiation at install.

> **problem:**
> No Case of this session decides how the person sets the category set of a project at install.

```then
defer:
  - slug: rule-morph
    type: rule
    purpose: "The initiation at install: the person sets the category set of the project and the harness holds it as data, so a changed set rewrites no rule; put off again at the close of Plan Mode of session 0200"
```
