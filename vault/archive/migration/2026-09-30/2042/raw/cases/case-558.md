## Case 558 — The librarian reads what its job needs and flags a read its frame does not name

> **context:**
> The librarian runs after the handoff and turns the session's ratified decisions into vault pages through the scripts, then writes the brief. Its frame is the Render of `rule-documentation`, rendered into `.claude/agents/librarian-guppi.md`. The frame names three inputs and a list of allowed reads, and bans the rest: the ledger beyond one read, the plan, `wiki/decisions/`, any search of `vault/archive/`, a Spec beyond its unticked lines, and `log.md` outside its diff. `estimate-documentation-completes` fails the whole promise on any read outside the list, even when the pages, the steps and the commit are right. Its History holds fifteen readings: nine failed and six passed. The last five in a row failed on a read outside the list. After each failure a Case widened or reworded the list (cases 349, 357, 474.1, 530.1), and the next run found another read. The reading of session 1736 on the run of 070d8e6 failed on four reads, all made for the brief. The first was a `git status` over `vault/wiki/decisions/`. The second was a `grep` of `git status` output for `vault/archive`. The third was the target, status and method of 52 Estimate pages, for Readings due. The fourth was a `grep` over every Decision page, for the page count at the close. The rounds found that each read on record served the librarian's job, mostly the brief, which asks for facts no input carries. Two of the reads came from gaps in the frame (the yaml marks undescribed, cases 44 and 58; no form of a synthesis entry, case 474.1). None was a read for its own sake. The person decided the following. The librarian decides what it needs to read. Its instructions name the reads the job is known to need and forbid no read. When it makes a read the frame does not name, it writes one line under Flags of the brief: what it read and which part of its job needed it. That line is its feedback on the frame. A read with its flag fails nothing. A read without one fails the reading. A read the handoff asks for is judged like the librarian's own reads, and only a repair of a yaml entry stays refused. The synthesis section loses its bans on reads in the same way. A `git status`, a listing or a file count may cover `vault/wiki/decisions/` and `vault/archive/`, since each prints only paths and numbers. The Glob by slug still finds an archived page that a script names in an error. What the job does not need is a search of the text of the archived pages. If the flags show too much token cost, the person takes the question up again. In the frame: `rule-synthesis` bans another session's yaml and the archive, and the Criterion of `estimate-synthesis-clusters` bans the archive, so 558.2 changes both. `estimate-brief-written` says Flags are "as before", and the person chose that it gains the new line, so 558.3 replaces its Criterion. The Purpose and `purpose` of `rule-materialize` say the script "Prevents the librarian from reading the ledger and the Spec", which the change makes false. `rule-rules-schema` requires a `purpose` that says what the rule prevents. So 558.1 rewords both texts: the script prevents the need for the ledger beyond its one read and for the Spec beyond its unticked lines, which matches the one read of the ledger that the new frame names. `estimate-synthesis-keeps-actioned-by-the-mark` speaks of `addressed_by`, and `estimate-brief-carries-the-run-facts` speaks of Readings due, so both stand. `rule-index-check` holds no ban on reads and stands. The report of `rule-close` already lists "the flags you raised", so it carries the new flags and stands. The sentence of `rule-brief` that reads a fact from a page and names the page in the report stands, because the frame names that read. The row of the glossary for the librarian names its inputs, which do not change. `lesson-handoff-instructs-a-repair-the-librarian-rule-forbids` is about a repair, which stays refused. The claims about the texts rest on three searches. First, a Grep of `librarian` near `read`, `open` or `search` over `vault/wiki/` printed so much that the harness saved it to a file. Its hits under `rules/`, `entities/` and the root pages were read. They state the librarian's reads only in `rule-documentation`, `rule-materialize`, `glossary.md` and `entity-glossary`, and the other hits there speak of readings of Estimates after the librarian's run. Its hits under `lessons/` and `insights/` were not all read. The one read is `insight-librarian-frame-omits-required-reads`, which is `actioned` and tells a history. Second, a Grep of `read no|never read|not read` over `vault/wiki/estimates/` printed one Estimate about the librarian's reads, `estimate-documentation-completes`. Third, a Grep of `read no|reads no|never read|not read` over the Estimates of `rule-documentation`, `rule-synthesis` and `rule-brief` printed it and `estimate-synthesis-clusters`. 558.1 and 558.2 replace both Criteria. The check of the answer noted six lines of the three old Criteria that the new ones do not carry. Five of them are the bans and the list of reads that the person removed. Four of those five stand in `estimate-documentation-completes`. The fifth is the archive line of `estimate-synthesis-clusters`, which 558.2 replaces. The sixth line is the line of `estimate-brief-written` that keeps Flags "as before", and 558.3 changes it. The check also noted that 558.1 and 558.3 share words on the flag. They check it from two angles: 558.1 checks that each read in the event log has its flag, and 558.3 checks the form of the line in Flags. The parent's `recommend` keeps an item for each of the two questions of the first round that the person did not answer. As the rebuilt Case 557.2 sets, each of these items says that its question was not answered and names the later question that replaced it. No hook and no code reads the frame: the librarian renders its own agent file, and the client loads it at the next session start. The first run under the new frame is therefore the librarian's run after the next session. The Case creates no page, so no vault query ran.

> **problem:**
> The librarian's frame bans reads by a closed list, and its Estimate fails on any read outside it. The list keeps missing reads that the job needs, mostly for the brief, so the Estimate has failed five times in a row, each time on a read its work needed, and each fix only widened the list until the next run. The question was whether the promise gets softer, what the bans protect, and how a read that the frame did not foresee becomes feedback instead of a failure.

> **recommend:**
> - **How strict the promise on reads stays**
>   Recommended: (a) check only the bans; the list of reads stays in the frame as a guide.
>   Answer: not answered; the person asked first why the librarian's reads are banned, and the later question on what a read outside the list does to `estimate-documentation-completes` replaced it.
> - **Which of the four reads of the last run become allowed**
>   Recommended: (a) all four; the ban covers the content of a page, not its name.
>   Answer: not answered; the later question on what the ban on Decision pages and the archive covers replaced it.
> - **Where the brief gets the facts that sent the librarian outside its list**
>   Recommended: (a) a script prints the facts the brief needs.
>   Answer: (b) the frame allows the reads the job needs: the librarian decides itself what it needs; if it is seen to spend too many tokens, the question is taken up again.
> - **What a read outside the list does to `estimate-documentation-completes`**
>   Recommended: (a) a read outside the list is a finding, not a failure; the Estimate fails only on a ban.
>   Answer: (a), agreed; the next round widened it, so that no read fails once the librarian records it.
> - **What the ban on Decision pages and the archive covers**
>   Recommended: (a) the ban covers the text of a page, not its name.
>   Answer: (a), with a correction: the Estimate does not fail when pages are read, since such a read is a finding that the librarian must record; the librarian's instructions speak of no hard ban, and ask it to say so when it needs a read of its own; this is the librarian's feedback on its frame.
> - **How a read beyond the frame's list reaches the next session**
>   Recommended: (a) the librarian writes each such read into Next session, `Cases`, of its brief.
>   Answer: not a Case; it is closer to a flag or a lesson.
> - **Where the librarian records a read outside its inputs**
>   Recommended: (a) a line under Flags of the brief.
>   Answer: (a), agreed.
> - **Change**
>   Asked: fix the findings of the second pre-spec run: the Purpose of `rule-materialize` says the ledger is not needed at all while the frame needs one read of it; the frame says the job does not need a search of the archive while it names the Glob by slug and a listing of the archive; the context misstates the state of Case 557.2 and the count of the lines not carried.
>   Taken: the `purpose` and the Purpose of `rule-materialize` say the ledger beyond its one read and the Spec beyond its unticked lines; the frame says the job does not need a search of the text of the pages under `vault/archive/`; the context names the rebuilt 557.2 and counts five removed bans among the six lines not carried.

### Case 558.1 — The frame names the reads the job needs and forbids none

> **recommend:**
> - **A read that the handoff asks for**
>   Recommended: (a) only the repair stays refused; a read the handoff asks for is a read like any other.
>   Answer: (a), agreed, after the main agent explained the refusals of the frame.

> **given:**
> `rule-documentation` — the frame of the librarian: its inputs, the reads its job is known to need, and its one refusal
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from the frame
> **＋** `estimate-documentation-completes` — the promise of the phase, its Criterion replaced whole
> **＋** `rule-materialize` — its Purpose says what the yaml prevents the librarian from needing
> **＋** `vault/wiki/brief.md` — the brief, whose Flags carry each read the frame does not name
> **＋** `handoff.md`, `vault/wiki/tags.md` — two of the librarian's inputs
> **＋** `rule-index-check`, `rule-synthesis` — the judgments whose Greps give the index lines
> **＋** `Makefile` — `make test-documentation` and `make lint`

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** Every read in its event log beyond its inputs and beyond the reads its frame names has its line under Flags of the new `vault/wiki/brief.md`.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** A read that has its line under Flags fails nothing, whatever it read: a Decision page, a Spec, the ledger or the archive.
> **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry. It names what was asked and why in the report, and the refusal does not stop the run.

> **tasks:**
> - [ ] update `rule-documentation`
>   - old: `` Open a page under `vault/wiki/` for four reasons only: ``
>   - new:
>     ````
>     The reads below are the ones your job is known to need; make them without a flag. When you need a read they do not name, make it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault: no read is forbidden to you (case 558.1). Open a page under `vault/wiki/` for these four reasons:
>     ````
>   - old:
>     ````
>     Never read `ledger.md`, `plan.md` or `wiki/decisions/`, never search `vault/archive/`, nor read `spec.md` beyond its unticked `- [ ]` lines
>     ````
>   - new:
>     ````
>     Your job does not need `plan.md`, the text of a page under `wiki/decisions/` or a search of the text of the pages under `vault/archive/`, nor `ledger.md` beyond the one read below, nor `spec.md` beyond its unticked `- [ ]` lines
>     ````
>   - old: `` One read of `ledger.md` is allowed and no other: ``
>   - new: `` One read of `ledger.md` is needed: ``
>   - old:
>     ````
>     only by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report; no other Glob, Grep, `grep`, `find` or `ls` runs over the archive (case 474.1).
>     ````
>   - new:
>     ````
>     by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report (case 474.1).
>     ````
>   - old:
>     ````
>     run `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`.
>     ````
>   - new:
>     ````
>     run `git status` and `git diff` on the files the scripts of this run wrote; a `git status`, a listing or a file count may cover `vault/wiki/decisions/` and `vault/archive/`, since it prints paths and numbers and no text of a page (case 558.1).
>     ````
>   - old:
>     ````
>     Read `vault/wiki/log.md` only through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added; never `Read`, `tail`, `head` or `grep` it.
>     ````
>   - new:
>     ````
>     Read `vault/wiki/log.md` through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added.
>     ````
>   - old:
>     ````
>     An instruction of the handoff that this frame forbids — a repair of an
>     entry, a read of `ledger.md` beyond the one allowed above, a Spec beyond its unticked lines, a decision page, a search of the archive or an archived page that no script named in an error — you do not
>     carry out: name it in the report, what was asked and why it was refused, and go on
>     (case 90.3).
>     ````
>   - new:
>     ````
>     An instruction of the handoff to repair an entry you do not carry out: name it in the report, what was asked and why it was refused, and go on (case 90.3). A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame does not name it (case 558.1).
>     ````
>   - old: `It starts empty, reads three inputs, and opens a page only for a reason its frame names.`
>   - new: `It starts empty, reads three inputs and the reads its frame names, and flags in the brief any other read it makes, so the frame learns what the job needs (case 558.1).`
>   - change: `the frame names the reads the job needs and forbids none; a read it does not name is made and flagged in the brief; only a repair asked by the handoff is refused (case 558.1)`
> - [ ] update `rule-materialize`
>   - set: `{purpose: "Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines, or from routing a decision by guesswork"}`
>   - old: `Prevents the librarian from reading the ledger and the Spec beyond its unticked lines (case 271), or from routing`
>   - new: `Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines (case 271), or from routing`
>   - change: `the purpose prevents the need for the reads, not the reads, since the librarian's frame forbids no read (case 558.1)`
> - [ ] update `estimate-documentation-completes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a read the frame does not name is flagged under Flags of the brief and fails nothing; only a repair asked by the handoff is refused (case 558.1)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-documentation-completes` — by hand, the first librarian run whose agent file holds this Render: its event log against the Flags of its brief

> **ratification:**
> ```
> - decision[case 558.1][update][rule-documentation]{ref:rule-documentation}
> - decision[case 558.1][update][rule-materialize]{ref:rule-materialize}
> - decision[case 558.1][update][estimate-documentation-completes]{ref:estimate-documentation-completes}
> ```

### Case 558.2 — The synthesis drops its bans on reads

> **recommend:**
> - **Whether the synthesis section drops its bans too**
>   Recommended: (a) yes: the synthesis says "name it" instead of "never", like the frame.
>   Answer: (a), agreed.

> **given:**
> `rule-synthesis` — the synthesis section of the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from it
> **＋** `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced whole
> **＋** `vault/wiki/lessons/`, `vault/wiki/insights/` — the pages the Greps of the synthesis index
> **＋** `vault/archive/` — the archive, which the synthesis does not need
> **＋** `estimate-documentation-completes` — the promise that each read the frame does not name is flagged

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The report names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, and the comparisons made against their lines, by meaning.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line, and the flag of such a read is the promise of `estimate-documentation-completes`.

> **tasks:**
> - [ ] update `rule-synthesis`
>   - old: `The archive is not read: a lesson is archived only when its`
>   - new: `The archive is not needed: a lesson is archived only when its`
>   - old:
>     ````
>     Read no `materialize.yaml` other than the ones `guppi materialize` names, and look for no earlier entry: the entries of the synthesis have these forms (case 474.1).
>     ````
>   - new:
>     ````
>     The entries of the synthesis have these forms, so no earlier entry and no `materialize.yaml` other than the ones `guppi materialize` names is needed (case 474.1); when you still need one, read it and flag the read as the frame says (case 558.2).
>     ````
>   - old: `Do not read the archive and do not write pages yourself.`
>   - new: `The archive is not needed: an actioned Insight stays live with its pattern in its index line; when you still need an archived page, read it and flag the read as the frame says (case 558.2). Do not write pages yourself.`
>   - change: `the synthesis forbids no read; another session's yaml or an archived page it still needs is read and flagged (case 558.2)`
> - [ ] update `estimate-synthesis-clusters`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a read of another session's yaml or of the archive fails nothing here; its flag is the promise of estimate-documentation-completes (case 558.2)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the report of the first librarian run after the render whose yaml holds at least two lesson entries

> **ratification:**
> ```
> - decision[case 558.2][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 558.2][update][estimate-synthesis-clusters]{ref:estimate-synthesis-clusters}
> ```

### Case 558.3 — Flags of the brief carry the librarian's own reads

> **given:**
> `rule-brief` — the brief section of the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from it
> **＋** `estimate-brief-written` — the promise of the form of the brief, its Criterion replaced whole
> **＋** `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/sprint.md` — the brief, the list of deferred items and the sprint
> **＋** `handoff.md`, `frontier.md` — the sources of Next session, of the librarian and of `carry`
> **＋** `rule-carry-over` — the second writer of the brief, the skill `carry`
> **＋** `rule-documentation` — the frame whose named reads decide which read is flagged

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due and Readings at the close are as before.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read of the librarian that its frame does not name, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

> **tasks:**
> - [ ] update `rule-brief`
>   - old: `failed Estimates; MOC candidates; stale defers; contradictions; the lint output.`
>   - new: `failed Estimates; MOC candidates; stale defers; contradictions; the lint output; each read you made beyond the reads your frame names, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (case 558.3).`
>   - change: `Flags carry each read of the librarian beyond the reads its frame names (case 558.3)`
> - [ ] update `estimate-brief-written`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Flags hold a line for each read of the librarian beyond the reads its frame names (case 558.3)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-written` — by hand, the brief of the first librarian run whose agent file holds this Render

> **ratification:**
> ```
> - decision[case 558.3][update][rule-brief]{ref:rule-brief}
> - decision[case 558.3][update][estimate-brief-written]{ref:estimate-brief-written}
> ```
