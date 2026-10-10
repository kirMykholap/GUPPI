## Case 769 — The opening of a sprint comes before the Frontier

> **context:**
> When the last sprint is closed, the hook `guppi sprint --hi` tells the agent at `/hi` to start `/sprint-open` before the Frontier. But step 1 of `/sprint-open` assembles the Frontier first, with the line `open the next sprint` of the brief as its first Cases line, and `/hi` puts no milestone item on the Frontier while that line stands. So in session 1713 the opening was one Frontier line among six, and the first milestone of `plugin` could not be taken up in the session that opened it; the handoff of that session records that the person felt the opening was one more Frontier item rather than a step of its own. The person chose this: the opening Case comes first, before any Frontier; before the reply that acknowledges it the agent assembles and writes the whole Frontier and takes the readings that `/hi` takes, and that reply shows the Frontier and puts the Ask questions; the Frontier of that session takes the items of the first milestone from the opening Case, since `vault/wiki/sprint.md` shows the new sprint only after the librarian's run; the close of a sprint waits for the close of `plugin`, where `estimate-sprint-plugin-close-steps-run-from-the-line` judges it; the questions of the opening Case stay. Case 769.1 changes `/sprint-open`, Case 769.2 what the Frontier holds at an opening, Case 769.3 the moment of the readings of `/hi`, Case 769.4 the acknowledging reply of the opening Case, and Case 769.5 the check of the session after a close; each replaces the Criterion of the one Estimate whose Criterion speaks of its change, or creates one. Not this Case: the merge of the branch of the closed sprint at the opening (Frontier item C4) and the archive folder `guppi cleanup` picks for the pages of the opening session (C6). The hook needs no change: `hi_hook` of `guppi/sprint.py` already prints that `/sprint-open` starts before the Frontier, so `estimate-skill-sprint-open-starts-at-hi` stands. A milestone item of the opening session closes `case N` only with an `update` of the sprint page under Case N, by `updates_the_sprint` of `guppi/prespec.py`, and `apply` of `guppi/generate.py` applies the entries of a ledger in their order, so such an `update` lands after the `create` of the same session. A Grep `` open the next sprint|628\.7|before the Frontier `` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `rules/rule-skill-hi.md`, `rules/rule-skill-sprint-open.md` and `estimates/estimate-skill-sprint-open-asks-the-opening-questions.md`, `estimates/estimate-hi-writes-frontier.md` and `estimates/estimate-hi-takes-its-readings.md`, which this Case changes; `rules/rule-brief.md` and `estimates/estimate-brief-written.md`, which set that the brief writes the line, still true; `estimates/estimate-sprint-close-next-session-opens-the-sprint.md`, whose Criterion line that `/hi` writes the opening line first under `## Cases` becomes false, so Case 769.5 replaces its Criterion and points to `estimate-hi-writes-frontier` for where the line stands; its old `method` named the transcript of an earlier session and the session after a close, which the person in Case 764 left for a later Case before the close of `plugin`; the check of a kept method refused it once its Criterion is replaced, so the person chose that Case 769.5 sets it anew to the tests and a reading by hand at the Retro of this session, and the live look at the next opening stays with the person's answer that `estimate-hi-writes-frontier` asks; `estimates/estimate-hi-takes-a-conserved-spec.md`, whose trigger is the brief line and whose promise, no conserved Spec at an opening, Case 769.2 keeps; and `estimates/estimate-skill-sprint-open-starts-at-hi.md`, which stands as said. A Grep `` first reply of `?/hi|its first reply|in the first reply `` over `vault/wiki/rules/`, `vault/wiki/estimates/` and `.claude/` printed `rules/rule-case-protocol.md` and `rules/rule-skill-hi.md` in History lines; `rules/rule-orchestration.md`, whose sentence that the first reply of `/hi` keeps the form `rule-skill-hi` sets stays true; `estimates/estimate-hi-takes-its-readings.md`, which Case 769.3 changes; and `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, whose trigger is a reply with no ratification, so the acknowledging reply of the opening Case is not under it and it stands. In `rule-orchestration`, read whole, the sentence that the Frontier is written at `/hi` becomes false and Case 769.4 changes it; the four parts of the acknowledging reply stay, the Ask questions standing after the checklist and before the last question, so `estimate-orchestration-acknowledging-reply` stands. In `rule-session-start`, read whole, the sentence that the Frontier is assembled from `brief.md` and `sprint.md` and the sentence that the first turn presents it become false at an opening, and Case 769.2 replaces both; the method of `estimate-hi-writes-frontier` named the `/hi` of the session after a close, where no Frontier now stands, and Case 769.2 sets it to the reply that acknowledges the opening Case; its Estimate `estimate-session-start-context` speaks of the loaded context and stands. A Grep `` skills.{0,3}(hi|sprint-open)|rule-skill-hi|rule-skill-sprint-open|estimate-hi-writes-frontier|estimate-skill-sprint-open `` over `tests/` printed `tests/test_prespec.py`, `tests/test_guard.py`, `tests/test_ratified.py`, `tests/test_sprint.py` and `tests/test_lint.py`; they use the paths under a temporary folder or as strings, or the line of the hook, which does not change. `tests/test_orchestration.py` reads `vault/wiki/orchestration.md` live, only its blocks tagged `showing` and `defer`, and the pairs of Case 769.4 add no block. Each Criterion this Case replaces drops on purpose the lines it changes: the first two lines of the old Criterion of `estimate-skill-sprint-open-asks-the-opening-questions`, which put the Frontier before the dispatch; the lines of `estimate-hi-writes-frontier` that set the opening line open, no milestone item at an opening and the checklist of the first reply, reworded with the old closer lines joined into one line and Pre-spec named `/pre-spec`; the line of `estimate-hi-takes-its-readings` that set the readings in the first reply; and the line of `estimate-sprint-close-next-session-opens-the-sprint` that had `/hi` write the opening line. The `then` lines of the sub-cases share words, since each speaks of the same Frontier, but each signs another moment: the dispatch (769.1), what the Frontier holds (769.2), the reply in which `/hi` reads (769.3) and the reply that acknowledges the opening Case (769.4). The files of Cases 764 and 767 were read: Case 764 changes neither `rule-skill-hi` nor these Estimates, and its sentences that keep a check of a sprint close off the Frontier stay in the new Criterion of `estimate-hi-takes-its-readings`.

> **problem:**
> The opening of a sprint is one Frontier line among others, so the session that opens a sprint cannot take up the first milestone of that sprint, and the opening is not a step of its own.

> **recommend:**
> - **Is the opening a Frontier line, a step before the Frontier, or a session of its own?**
>   - Recommended: (b) a step before the Frontier: `/sprint-open` runs first, and once the opening Case is ratified the Frontier is built with the items of the new first milestone.
>   - Answer: agreed, (b).
> - **Does the close change now, or wait for the close of `plugin`?**
>   - Recommended: (a) the close waits; it is judged at the close of `plugin`, and a flaw seen then becomes a Case.
>   - Answer: agreed, (a).
> - **Do the questions of the opening Case stay as they are?**
>   - Recommended: (a) keep the questions.
>   - Answer: agreed, (a).
> - **Where do the readings and the Ask questions of `/hi` go in the session that opens a sprint?**
>   - Recommended: (a) all of it after the opening: the reply that confirms the opening Case writes the whole Frontier, takes the readings and puts the Ask questions before the question which item is next.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes of the findings of `/pre-spec`: one wording across the sub-cases for when `frontier.md` is written; the sentences of `rule-session-start` that become false replaced; the method of `estimate-hi-writes-frontier` set to the new moment; and the Criterion of `estimate-sprint-close-next-session-opens-the-sprint` replaced, its method left as it is.
>   - Taken: every sub-case says the Frontier is assembled and written before the reply that acknowledges the opening Case, which shows it; Case 769.2 replaces the sentences of `rule-session-start` on the sources and the first turn and sets the method; Case 769.5 replaces the Criterion of `estimate-sprint-close-next-session-opens-the-sprint`.
> - **How is the check of the session after a close read, now that it cannot wait for that session?**
>   - Recommended: (a) the tests of the ledger refusal and of the sprint id on the pages, and a reading by hand at the Retro of this session of the new texts of `/hi` and `/sprint-open` in its Spec.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the confirmation of `/pre-spec` found that the `purpose` of the new Estimate of Case 769.4 and the `change` line of its `rule-orchestration` update still said that the acknowledging reply writes the Frontier; the person chose to fix them.
>   - Taken: both say that the Frontier is written and the readings taken before that reply, which shows the Frontier.

### Case 769.1 — The opening Case comes before any Frontier

> **given:**
> `rule-skill-sprint-open`: the skill of the opening, rendered into `.claude/skills/sprint-open/SKILL.md`.
> **＋** `estimate-skill-sprint-open-asks-the-opening-questions`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-skill-hi`: the skill `/hi`, whose Frontier waits for the opening Case.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, whose first heading marks the last sprint closed.
> **＋** `vault/wiki/brief.md`: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/backlog.md`: the items without a turn.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/sprint-close`: the skill that the close line of the new sprint page starts.

> **when:**
> The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

> **then:**
> Before any Frontier is assembled, the main agent dispatches `case-guppi` for the line `open the next sprint` of the `Cases` of Next session in `vault/wiki/brief.md`, with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
> **＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
> **＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
> **＋** The opening Case is the first Case the session ratifies.
> **－** No Frontier is assembled, written to `raw/<date>/<hi HHMM>/frontier.md` or shown, and no other item is taken up, before the person ratifies the opening Case.
> **－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
> **－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old: `` 1. Assemble the Frontier as `/hi` sets it: the line `open the next sprint` of the brief stands first under `## Cases`, and no item of the closed sprint and no conserved Spec stands there. ``
>   - new: `1. Assemble no Frontier yet: the opening Case comes first, and no other item of the session is taken up before the person ratifies it (case 769.1).`
>   - old: `` 2. When the person takes up that line, dispatch `case-guppi` for it as ``
>   - new: `` 2. Dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as ``
>   - old: `and the person ratifies the opening Case as any other.`
>   - new: `` and the person ratifies the opening Case as any other. Before the reply that acknowledges it, assemble and write the Frontier as `/hi` sets it, the items of the first milestone of the opening Case among its Cases; that reply shows it, as `vault/wiki/orchestration.md` sets that reply (case 769.4). ``
>   - change: `the opening Case comes before any Frontier, and the reply that acknowledges it brings the Frontier (case 769.1)`
> - [ ] update `estimate-skill-sprint-open-asks-the-opening-questions`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /sprint-open has the opening Case of a sprint dispatched before any Frontier, ask its id, its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
>     method: by hand, at the Retro of the session of case 769, the new Render of rule-skill-sprint-open in its spec.md read against the Criterion
>     ```
>   - change: `the Criterion replaced whole — the opening Case is dispatched before any Frontier`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] read `estimate-skill-sprint-open-asks-the-opening-questions`

> **ratification:**
> ```
> - decision[case 769.1][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 769.1][update][estimate-skill-sprint-open-asks-the-opening-questions]{ref:rule-skill-sprint-open}
> ```

### Case 769.2 — At an opening the Frontier takes the first milestone from the opening Case

> **given:**
> `rule-skill-hi`: the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`.
> **＋** `rule-session-start`: the start of a working session, whose first turn presents the Frontier.
> **＋** `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `rule-skill-sprint-open`: the skill of the opening, `/sprint-open`, whose opening Case comes first.
> **＋** `vault/wiki/orchestration.md`: the take-back of a ratified Case, which a closed line may follow.
> **＋** `entity-sprint-<id>`: the new sprint page that the opening Case creates.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of the opening Case.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`: the sources of the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the check that fails on an open Cases line.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md`, the output of the skill's commands and, in the session that opens a sprint, the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case of `/sprint-open`; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone of `vault/wiki/sprint.md`, or, while that opening line stands, the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file of the opening Case, with the source `sprint`; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page, or the opening Case, gives it, with the source `sprint` alone. The agent judges the sameness by meaning, with no page opened.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`. An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it, and a sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** When the first reply of `/hi` shows the Frontier, the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`, and a `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of `vault/wiki/sprint.md` is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `/pre-spec` finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened (case 268.2).`
>   - new: `` When the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, start `/sprint-open` first, as the hook on `/hi` says: the opening Case comes before the Frontier; before the reply that acknowledges it, assemble and write the Frontier below and take its readings, and that reply shows it and puts the questions of its `A` lines, as `vault/wiki/orchestration.md` sets that reply (case 769.2). Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened (case 268.2). ``
>   - old: `` first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line (`rule-sprint-close`, case 628.7); ``
>   - new: `` first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case (`rule-sprint-close`, cases 628.7, 769.2); ``
>   - old: `and none of a later milestone, of the Backlog or of Closed (case 229.3), and none at all while that opening line stands (case 628.7);`
>   - new: `` and none of a later milestone, of the Backlog or of Closed (case 229.3); while that opening line stands, no item of `sprint.md`, which shows the new sprint only after the librarian's run, but the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, each with the source `sprint` (case 769.2); ``
>   - change: `at the opening of a sprint the Frontier comes after the opening Case and takes the first milestone from it (case 769.2)`
> - [ ] update `rule-session-start`
>   - old: `` Assembled from what was loaded: `brief.md` + `sprint.md` + the git state and the tail, plus the unfinished plan if we are on a plan branch. ``
>   - new: `` Assembled from what was loaded: `brief.md` + `sprint.md` + the git state and the tail, plus the unfinished plan if we are on a plan branch; in the session that opens a sprint, the first milestone comes from the case file of the opening Case of `/sprint-open` instead of `sprint.md` (case 769.2). ``
>   - old: `The agent's first turn presents it as a list — tasks, problems, debt carried over, where the sprint stands.`
>   - new: `` The agent's first turn presents it as a list — tasks, problems, debt carried over, where the sprint stands —, but in the session that opens a sprint, whose first turn starts the opening Case of `/sprint-open`: there the Frontier is assembled and written before the reply that acknowledges that Case, and that reply presents it (case 769.2). ``
>   - change: `in the session that opens a sprint the Frontier takes the first milestone from the opening Case and the reply that acknowledges that Case presents it (case 769.2)`
> - [ ] update `estimate-hi-writes-frontier`
>   - set:
>     ```
>     status: pending
>     method: "by hand: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of /sprint-open, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
>     ```
>   - change: `the Criterion replaced whole — at an opening the Frontier takes the first milestone from the opening Case, and the opening line stands closed`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 769.2][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 769.2][update][rule-session-start]{ref:rule-session-start}
> - decision[case 769.2][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```

### Case 769.3 — The readings of /hi come with the Frontier

> **given:**
> `estimate-hi-takes-its-readings`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `rule-skill-hi`: the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`, whose readings come with the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `vault/wiki/brief.md`: the brief, whose Next session gives the `W` and `A` lines.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `estimate-hi-takes-its-readings`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates it reads
>     ```
>   - change: `the Criterion replaced whole — the readings come with the Frontier, which at an opening is not the first reply`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 769.3][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```

### Case 769.4 — The reply that acknowledges the opening Case brings the Frontier

> **given:**
> `rule-orchestration`: what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-acknowledges-the-opening-with-the-frontier`: the new check of the reply that acknowledges the opening Case.
> **＋** `estimate-orchestration-acknowledging-reply`: the four parts of an acknowledging reply, which stand.
> **＋** `rule-skill-sprint-open`: the skill of the opening, rendered into `.claude/skills/sprint-open/SKILL.md`.
> **＋** `rule-skill-hi`: the skill `/hi`, which sets the Frontier, its readings and its Ask questions.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.

> **when:**
> The person ratifies the opening Case of `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Before that reply, the agent writes `raw/<date>/<hi HHMM>/frontier.md` as `rule-skill-hi` sets it, and takes each reading of an open `W` line whose whole method runs now.
> **＋** The reply keeps the four parts of an acknowledging reply, in their order.
> **＋** Its `LEDGER` block holds the decision lines of the opening Case, then the `estimate[...]` line of each reading taken.
> **＋** Its `## Frontier` shows the lines of the new `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** After the lines of the Frontier and before the question which item is next, the reply puts each open `A` line to the person as `rule-skill-hi` sets it: the Estimate by slug and its question.
> **－** No tool call follows the `LEDGER` block in the same reply.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`; ``
>   - new: `` The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`, or, in the session that opens a sprint, before the reply that acknowledges the opening Case of `/sprint-open` (case 769.4); ``
>   - old: `Headings and labels in the language of the chat (case 167, supersedes 157).`
>   - new: `` Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges the opening Case of `/sprint-open` brings the Frontier, as `rule-skill-hi` sets it: before that reply the agent writes `frontier.md` and takes each reading that `/hi` takes; its `LEDGER` block holds the reading lines after the decision lines; its `## Frontier` shows the new Frontier; and after the lines of the Frontier and before the question which item is next it puts each open `A` line to the person, as `/hi` does (case 769.4). ``
>   - change: `the Frontier and the readings of /hi come before the reply that acknowledges the opening Case of a sprint, which shows that Frontier and puts its Ask questions (case 769.4)`
> - [ ] create `estimate-orchestration-acknowledges-the-opening-with-the-frontier`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the Frontier is written and the readings of /hi taken before the reply that acknowledges the opening Case of a sprint, and whether that reply shows the Frontier, holds the readings in its LEDGER block and puts the Ask questions before the question which item is next`
>   - method: `by hand, at the Retro of the session of case 769, the new Render of rule-orchestration in its spec.md read against the Criterion`
>   - tags: `[session, workflow, sprint]`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-acknowledges-the-opening-with-the-frontier`

> **ratification:**
> ```
> - decision[case 769.4][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 769.4][create][estimate-orchestration-acknowledges-the-opening-with-the-frontier]{ref:rule-orchestration}{tags:session,workflow,sprint}
> ```

### Case 769.5 — The opening line reaches the Frontier closed by the opening Case

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint`: its Criterion is replaced whole and its `method` set anew.
> **＋** `estimate-hi-writes-frontier`: sets where the opening line stands on the Frontier.
> **＋** `rule-skill-sprint-open`: the skill of the opening, `/sprint-open`, whose opening Case comes first.
> **＋** `entity-sprint-<id>`: the sprint page that the session closes.
> **＋** `entity-sprint-<new id>`: the sprint page that the next session creates.
> **＋** `/hi`: the skill that opens the next session.
> **＋** `vault/wiki/brief.md`: the brief, whose first line of `Cases` opens the next sprint.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, which shows no live sprint after the close.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `guppi ledger`, `guppi materialize`, `tests/test_ledger.py` and `tests/test_materialize.py`: the refusal of decision lines and the `sprint` field of the pages.

> **when:**
> The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the refusals of `uv run guppi ledger` in its transcript, its ledger, and the pages of its librarian's run.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` starts `/sprint-open` and writes no `frontier.md` before the opening Case is ratified; then `frontier.md` holds that line first under `## Cases`, closed `[x] … · case N` by the opening Case, and no item of `vault/wiki/sprint.md`, as `estimate-hi-writes-frontier` sets it.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

> **tasks:**
> - [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
>   - set:
>     ```
>     status: pending
>     method: "pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the Retro of the session of case 769, the new Renders of rule-skill-hi and rule-skill-sprint-open in its spec.md read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the opening line reaches frontier.md after the opening Case, closed by it; the method runs in the session of case 769`
> - [ ] read `estimate-sprint-close-next-session-opens-the-sprint`

> **ratification:**
> ```
> - decision[case 769.5][update][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}
> ```
