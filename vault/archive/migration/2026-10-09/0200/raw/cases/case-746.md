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

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - set:
>     ```
>     parent: rule-session-start
>     ```
>   - change: `the parent is rule-session-start, as case 743.6 set it (case 746.1)`
> - [ ] update `rule-skill-sprint-close`
>   - set:
>     ```
>     parent: rule-plan-mode
>     ```
>   - change: `the parent is rule-plan-mode, as case 743.8 set it (case 746.1)`
> - [ ] update `rule-session`
>   - set:
>     ```
>     children: [rule-session-start, rule-plan-mode, rule-work-mode, rule-end-of-work, rule-documentation]
>     ```
>   - change: `the children are the five phases alone; the two sprint skill pages hang under their phases (case 746.1)`
> - [ ] update `rule-session-start`
>   - set:
>     ```
>     children: [rule-skill-hi, rule-event-log, rule-ledger-write, rule-compact-recall, rule-skill-sprint-open]
>     ```
>   - change: `child rule-skill-sprint-open added (case 746.1)`
> - [ ] update `rule-plan-mode`
>   - set:
>     ```
>     children: [rule-ask, rule-prespec-hook, rule-prespec, rule-spec-capture, rule-case-protocol, rule-spec-write, rule-spec-reconcile, rule-case-build, rule-case-check, rule-skill-grill-me, rule-skill-wait-what, rule-prespec-onward, rule-orchestration, rule-ratification, rule-case-example, rule-skill-sprint-close]
>     ```
>   - change: `child rule-skill-sprint-close added (case 746.1)`
> - [ ] update `estimate-session-phases-in-order`
>   - set:
>     ```
>     status: pending
>     method: "make test-session, the pipeline over the tests of rule-session's children; then by hand at the Retro of the session of case 746 — the marks of the last finished session, the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md and the commit of its Documentation phase, read in that order, and the children of rule-session as the Spec of case 746 sets them"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     A session has ended, and someone reads its folder, the day's event log and `git log`.
>
>     Then:
>     All five phases left a mark, and the marks ascend in time: the `hi` line of the day's event log → `frontier.md` → `spec.md` with its approved stamp → the Retro commit → `handoff.md` → the librarian's commit.
>     **＋** `rule-session` is the parent of the five phases, its children in that order.
>     **－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.
>     ```
>   - change: `sent back for a reading at the Retro of the session of case 746, the Criterion unchanged: rule-session listed the two sprint skill pages among its children (case 746.1)`
> - [ ] read `estimate-session-phases-in-order`

> **ratification:**
> ```
> - decision[case 746.1][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 746.1][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> - decision[case 746.1][update][rule-session]{ref:rule-session}
> - decision[case 746.1][update][rule-session-start]{ref:rule-session-start}
> - decision[case 746.1][update][rule-plan-mode]{ref:rule-plan-mode}
> - decision[case 746.1][update][estimate-session-phases-in-order]{ref:rule-session}
> ```

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

> **tasks:**
> - [ ] update `estimate-skill-sprint-open-asks-the-opening-questions`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at the Retro of the session of case 746, the live Render of rule-skill-sprint-open and .claude/skills/sprint-open/SKILL.md read against the Criterion"
>     ```
>   - change: `sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.2)`
> - [ ] read `estimate-skill-sprint-open-asks-the-opening-questions`

> **ratification:**
> ```
> - decision[case 746.2][update][estimate-skill-sprint-open-asks-the-opening-questions]{ref:rule-skill-sprint-open}
> ```

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

> **tasks:**
> - [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at the Retro of the session of case 746, the live Renders of rule-skill-sprint-close and rule-orchestration, .claude/skills/sprint-close/SKILL.md, vault/wiki/orchestration.md and entity-sprint-migration read against the Criterion"
>     ```
>   - change: `sent back for a reading at the Retro of the session of case 746, the Criterion unchanged; the moment of the old method passed unread (case 746.3)`
> - [ ] read `estimate-skill-sprint-close-leads-the-closing-session`

> **ratification:**
> ```
> - decision[case 746.3][update][estimate-skill-sprint-close-leads-the-closing-session]{ref:rule-skill-sprint-close}
> ```
