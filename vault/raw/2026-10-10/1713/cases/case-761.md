## Case 761 — Each contradiction of the brief stands in Cases

> **context:**
> At the end of its run the librarian rewrites `vault/wiki/brief.md`. Its section Next session sorts the open items into three lists, and `Cases` is what needs a decision. The Render of `rule-brief` puts "a contradiction" there, and the Criterion of `estimate-brief-written` says the same. At the /hi of this session the reading of that Estimate failed: the brief of the run ab8be60f holds under Flags the contradiction that the handoff of session 1555 gave under Observations — the `－` line of `estimate-sprint-migration-merges` puts the merge on a `## Backlog` line of `entity-sprint-migration` that the page does not hold — and no line of `Cases` holds it. Both pages stand under `vault/archive/migration/2026-10-10/1555/`. The other contradiction of those Flags, on `estimate-sprint-close-settles-unread-estimates`, reached `Cases` through a line of `## For the next session` of the handoff. The Render does not say that each contradiction of Flags is meant, or what a contradiction between archived pages is, so the librarian could leave one out by a judgment the Render forbids elsewhere. The contradiction itself needs no work: the merge it speaks of is the work of Case 757. The person chose that the Render say it outright, the Criterion kept at first. The person first chose to read the Estimate at the /hi after each run of the librarian; the check of this file refused that `method`, since a `method` holds only what runs in its own session, and the person then kept the `method` as it stands, a reading at the /hi after the librarian's run of the session that closes a sprint. The Criterion of `estimate-brief-written` held the same words as the Render, "a `failed` Estimate, a contradiction, a defect the librarian found", so it did not state the two new promises; at `/pre-spec` the person chose to replace it whole. The new Criterion is the old one with the `Cases` line naming each contradiction of Flags, archived pages too, and one `－` line for a contradiction that `## For the next session` already carries; the rest stands word for word. The page goes `pending`. The person first kept its `method`, a reading at the /hi after the close of a sprint; the check of this file refused a `pending` page whose `method` waits for another session, and the person chose a reading of the rendered `.claude/agents/librarian-guppi.md` at the Retro of this session. That reading cannot run then: the `update` of `rule-brief` reaches the page at `guppi generate` and `guppi render` writes the frame after `guppi cleanup`, both in the librarian's run (steps 2 to 4 of `.claude/agents/librarian-guppi.md`), and `render` ticks the render line of this Case there (`orchestration.md`). The person then chose their own answer, on the brief the librarian writes, at the /hi after the close of `plugin`; `lint.waits_for_another_session`, the predicate the check of this file calls, leaves to another session a part of a `method` that names the person. The page has no `purpose` field that states the old promise. In `rule-brief`, read whole, the sentences that state what goes into `Cases` are the `Cases` sentence of the Render, which the pair changes; "Write facts and flags only. Add no decision and no judgment of the work." and the Purpose's "nothing in the brief is a decision", which the change follows and which stand; and the paragraph of the skill `carry`, whose `Cases` is always the line "none", which stands, since the new sentence is in the librarian's list alone. The Criterion of `estimate-brief-carries-the-run-facts` speaks of Readings due, not of `Cases`, and stands. A Grep `Next session` over `vault/wiki/rules/` printed `rule-documentation.md`, `rule-skill-hi.md`, `rule-brief.md` and `rule-carry-over.md`, and over `.claude/` printed `.claude/skills/hi/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/carry/SKILL.md`; `rule-skill-hi` and `.claude/skills/hi/SKILL.md` take the lines of `Cases` into the Frontier and read any line, `rule-documentation` names the reads the brief needs, and the carry pages set the short shape, so none of them sets the form of a contradiction line and all stand. A Grep `librarian-guppi|rule-brief|estimate-brief` over `tests/` printed one line, in `tests/test_grepguard.py`, which names the agent and reads no live file of it, so no test reads the new text.

> **problem:**
> The brief left a contradiction of its Flags out of `Cases`, though the brief rule puts a contradiction there, because the rule does not say that each contradiction is meant, archived pages too.

> **recommend:**
> - **What should change after the brief missed the contradiction?**
>   - Recommended: (a) the rule says it outright: each contradiction of Flags also gets a line in `Cases`, one between archived pages too, and one that a line of the handoff's For the next session already carries stands once; the check keeps its wording and stays failed until its next reading.
>   - Answer: agreed, (a).
> - **When should the check be read next?**
>   - Recommended: (a) keep the current timing, since the check of the Case file refuses a method that waits for another session: the check stays failed and is read next at the start of the session after the close of `plugin`.
>   - Answer: agreed, (a).
> - **What method should the check use once its wording is replaced?**
>   - Recommended: (a) read the rule text at the end of this session: the rendered librarian instructions read by hand against the new wording.
>   - Answer: agreed, (a).
> - **How can the check be read when the new rule text reaches the instructions only after this session?**
>   - Recommended: (c) your own answer on the brief at the start of the session after the close of `plugin`.
>   - Answer: agreed, (c).
> - **Change**
>   - Asked: at `/pre-spec`, replace the Criterion of `estimate-brief-written` so that it holds both new promises, the page set `pending`, its method and moment unchanged.
>   - Taken: the Case adds an `update` of `estimate-brief-written` with its Criterion replaced whole, and a reading of it; its method changes as the answer on the method of the check sets it.

> **given:**
> `rule-brief`: the rule of the brief, whose Render sets the lists of Next session.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian's frame, which holds that Render.
> **＋** `estimate-brief-written`: the check of the brief, whose Criterion is replaced whole.
> **＋** `vault/wiki/brief.md`: the brief the librarian writes.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff the brief reads.
> **＋** `vault/archive/`: the folder of the pages a sprint close moves.

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run, and its Flags hold a contradiction.

> **then:**
> `Cases` of Next session holds a line for each contradiction of Flags, with what and from where.
> **＋** A contradiction between pages that stand in `vault/archive/` gets its line too.
> **－** A contradiction that a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md` already carries gets no second line in `Cases`.

> **tasks:**
> - [ ] update `rule-brief`
>   - old: `` a `failed` Estimate, a contradiction, a defect you found — what and from where. ``
>   - new: `` a `failed` Estimate, each contradiction of Flags (one between pages in `vault/archive/` too; one that a line of `## For the next session` already carries stands in that line alone), a defect you found — what and from where (case 761). ``
>   - change: `Cases of Next session hold each contradiction of Flags, one between archived pages too, once (case 761)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] update `estimate-brief-written`
>   - set:
>     ```
>     status: pending
>     method: by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run, whether Cases hold each contradiction of Flags, one between archived pages too, and once where a line of For the next session carries it, recorded in the estimate line
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     The librarian rewrites `vault/wiki/brief.md` at the end of its run.
>
>     Then:
>     The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
>     **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
>     **＋** Where things stand, Readings due and Readings at the close are as before.
>     **＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
>     **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
>     **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
>     **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
>     **＋** An item stands in one list only. A list with no item is the line "none".
>     **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
>     **－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
>     **－** The brief states no decision: the sort by kind is not a judgment of the work.
>     ```
>   - change: `the Criterion replaced whole — Cases hold each contradiction of Flags, one between archived pages too, once; read by the person's answer on the brief after a sprint close (case 761)`
> - [ ] read `estimate-brief-written`

> **ratification:**
> ```
> - decision[case 761][update][rule-brief]{ref:rule-brief}
> - decision[case 761][update][estimate-brief-written]{ref:rule-brief}
> ```
