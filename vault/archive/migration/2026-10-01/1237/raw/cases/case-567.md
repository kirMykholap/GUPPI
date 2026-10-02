## Case 567 — Make the librarian flag only the reads its frame says it does not need

> **context:**
> The librarian, `librarian-guppi`, runs alone after each session and writes the brief. Its frame, the Render of `rule-documentation`, lists four reasons to open a page in the vault. Since case 558.1, any read outside those reasons and outside the reads the frame names needs a line under Flags of the brief. The frame also asks the librarian to name in its report every page it opens. Reading W18 recorded `estimate-documentation-completes` as failed for one read. In the run of 1f43cf1c the librarian printed the first lines of `estimate-prespec-onward-sends-the-agent-on` to learn the field names of an Estimate, and then searched every Estimate page for its status, target and method for Readings due. Its report named that page among the reads it made for the brief, and the brief has no Flags line for it. The person judged that read to be part of reading the statuses, which the fourth reason covers. They also judged the flag rule too strict for live pages. From now on, a flag is due only for a read that the frame itself says the job does not need. The report names only the pages behind a judgment and, as case 349 set, the one allowed read of the ledger.
>
> The frame names the reads the job does not need in one sentence of the Render of `rule-documentation`, the one that opens with "Your job does not need": `plan.md`, the text of a page under `wiki/decisions/`, a search of the text of the pages under `vault/archive/`, `ledger.md` beyond its one allowed read, and `spec.md` beyond its unticked lines and the lines the run ticked. Two sentences of the Render of `rule-synthesis` also say that an earlier `materialize.yaml` and an archived page are not needed, and that such a read is flagged "as the frame says". They stay true unchanged, because the new frame counts those two reads among the flagged ones. This was not asked as a separate question. It follows from the title of the chosen answer: flag only the reads the instructions say the job does not need.
>
> Each replaced Criterion keeps its old lines word for word, with three exceptions. In `estimate-documentation-completes`, the line on reads beyond the frame changes, because that is the promise this Case changes, and the line on the report adds the pages behind a judgment and the one ledger read. In `estimate-brief-written`, the line on the kinds of Flags lines changes for the same reason.
>
> No create is made, so the vault was not queried. A Grep of `flag the read|beyond the reads|read you made beyond|Read beyond|Name every page|name the page in the report|names every page|in the report` over `vault/wiki/` printed 18 files: `case-schema.md`, `brief.md`, `log.md`, `rule-case-protocol.md`, `rule-documentation.md`, `rule-brief.md`, `rule-index-check.md`, `rule-synthesis.md`, `estimate-documentation-completes.md`, `estimate-brief-written.md`, `estimate-index-check-merges.md`, `estimate-synthesis-clusters.md`, `estimate-raw-archive.md`, `estimate-case-check-refuses-text-before-a-round.md`, `estimate-case-protocol-asks-in-the-grill-me-shape.md`, `decision-case-143.md`, `decision-case-197.md` and `decision-case-357.md`. The glob meant to leave out `decisions/` did not apply.
> - `case-schema.md`, `rule-case-protocol.md` and the two Estimates of `rule-case-check` and `rule-case-protocol` speak of the report of `/pre-spec`, not of the librarian.
> - The `estimate-raw-archive.md` hit is a Result line.
> - `rule-index-check`, `rule-synthesis`, `estimate-index-check-merges` and `estimate-synthesis-clusters` name a page opened for a same-or-near or a shared-cause judgment. That naming stays.
> - `brief.md` and `log.md` are not read, by the rule of this task.
> - The three Decision pages were not opened and are not changed.
>
> The same pattern over `guppi/`, `tests/` and `.claude/` printed one file, `.claude/agents/librarian-guppi.md`, the render of these pages. No code or test judges this text, so no reader in code needs an old form kept beside the new. A Grep of `Flags` over `vault/wiki/rules/` and `.claude/` printed 5 files: `rule-documentation.md`, `rule-brief.md`, `rule-carry-over.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/carry/SKILL.md`. The Flags of `rule-carry-over` and of the skill `carry` say what the vault does not know about a carried session and speak of no read, so they stand. `estimate-brief-carries-the-run-facts` speaks of how a Readings due line ends, not of the fields it is read from, so its Criterion stands. This session's librarian runs on the frame it loaded at its start, so the new frame is first read at the librarian run of a later session.

> **problem:**
> The rule that flags every read outside four listed reasons recorded a failure for a harmless read of a live page. Opening a page to learn its field names was a step of the fourth reason. The rule asks for flags and report lines on pages that tell nothing about a gap in the frame. Meanwhile the reads that once showed such a gap are the ones the frame already says the job does not need. The flag rule and the report rule must be narrowed to those reads and to the pages behind a judgment. The brief section must also name the fields it reads, so that no page has to be opened to learn them.

> **recommend:**
> - **Which reads must the librarian still flag in the brief?**
>   - Recommended: (b) flag only the reads the instructions say the job does not need; a live page under `vault/wiki/` is free to open with no flag.
>   - Answer: (b), agreed with the recommendations.
> - **Does the report still name every page the librarian opens?**
>   - Recommended: (a) name only the pages that decided something: a copy-or-close judgment, a shared-cause judgment, a script error.
>   - Answer: (a), agreed with the recommendations.

### Case 567.1 — The frame flags only the reads it says the job does not need

> **recommend:**
> - **Was the read outside the listed reasons?**
>   - Recommended: (b) inside; the read was one step of reading the statuses for Readings due, so the failed result was a misjudgment and the Estimate is read again at the next librarian run.
>   - Answer: (b), agreed with the recommendations; not answered in the first round, asked again.

> **given:**
> `rule-documentation` — the frame of the librarian, whose Render names the reads, the flags and the report
> **＋** `rule-brief` — the brief section spliced into the frame, whose sentence on a fact of the brief names the page in the report
> **＋** `estimate-documentation-completes` — the Estimate whose Criterion is replaced
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from these pages
> **＋** `vault/wiki/brief.md` — the brief whose Flags take the line
> **＋** `rule-synthesis` — constrains: names an earlier yaml and an archived page as not needed, flagged as the frame says
> **＋** `rule-index-check` — constrains: names in the report a page opened for a same-or-near judgment

> **when:**
> `librarian-guppi` runs after the handoff with the Render of `rule-documentation` as its frame. It writes `vault/wiki/brief.md` and its report.

> **then:**
> A read that the frame of `.claude/agents/librarian-guppi.md` names as one its job does not need has one line under Flags of `vault/wiki/brief.md`. This includes the earlier yaml and the archived page that `rule-synthesis` names.
> **＋** The report names each page opened for one of these, with the reason and the outcome:
> - to judge same or near under `rule-index-check`;
> - to judge a shared root cause under `rule-synthesis`;
> - to say why a script failed.
>
> It also names the one allowed read of the ledger.
> **－** Any other page under `vault/wiki/` that is not a Decision page needs no line under Flags and is not named in the report. This holds whether it was read for a fact of the brief, for the field names of a page or for any other need.
> **－** A read that has its line under Flags fails nothing.

> **tasks:**
> - [ ] update `rule-documentation` — the flagged reads are the ones the frame says the job does not need; the report names only the pages behind a judgment and the one ledger read
>   - old: `` The reads below are the ones your job is known to need; make them without a flag. When you need a read they do not name, make it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault: no read is forbidden to you (case 558.1). Open a page under `vault/wiki/` for these four reasons: ``
>   - new: `` No read is forbidden to you. A read this frame says your job does not need — the reads listed below as ones your job does not need, and the earlier yaml and the archived page the synthesis names — you make when you need it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault. Any other read needs no flag: a page under `vault/wiki/` but the text of a Decision page, the scripts' own files, and the reads below (cases 558.1, 567.1). Your job opens a page under `vault/wiki/` for these four reasons: ``
>   - old: `Name every page you open in the report, with the reason and the outcome.`
>   - new: `` Name in the report each page you open for one of the first three reasons, with the reason and the outcome; a page you open for a fact of the brief, or for any other need, is not named, and the one read of `ledger.md` below stays named (case 567.1). ``
>   - old: `A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame does not name it (case 558.1).`
>   - new: `A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame says your job does not need it (cases 558.1, 567.1).`
>   - old: `reads three inputs and the reads its frame names, and flags in the brief any other read it makes, so the frame learns what the job needs (case 558.1).`
>   - new: `reads three inputs and what its job needs, and flags in the brief a read its frame says the job does not need, so the frame learns what it lacks (cases 558.1, 567.1).`
>   - change: `the librarian flags only a read the frame says its job does not need, and names in the report only a page opened for one of the first three reasons and the one read of the ledger (case 567.1)`
> - [ ] update `rule-brief` — a page read for a fact of the brief is not named in the report
>   - old: `read it from the page and name the page in the report.`
>   - new: `read it from the page; the page is not named in the report (case 567.1).`
>   - change: `a page read for a fact of the brief is not named in the report (case 567.1)`
> - [ ] update `estimate-documentation-completes` — the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — only a read the frame says the job does not need is flagged; the report names only the pages behind a judgment and the one read of the ledger (case 567.1)`
>   - sections.Criterion:
>     ```
>     When:
>     `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.
>
>     Then:
>     `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
>     **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
>     **＋** Every read in its event log that its frame says the job does not need has its line under Flags of the new `vault/wiki/brief.md`: `plan.md`, the text of a page under `vault/wiki/decisions/`, a search of the text of the pages under `vault/archive/`, `ledger.md` beyond its one allowed read, `spec.md` beyond its unticked lines and the lines the run ticked, a `materialize.yaml` that `guppi materialize` did not name, and an archived page opened at the synthesis.
>     **＋** Its report names each page opened to judge whether a create is the same page or a near one, whether a lesson shares its root cause, or why a script failed, with the reason and the outcome, and the one allowed read of `ledger.md`.
>     **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
>     **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
>     **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
>     **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
>     **－** Any other read needs no line under Flags and no name in the report: a page under `vault/wiki/` outside `vault/wiki/decisions/`, read for a fact of the brief, the field names of a page or any other need, and the scripts' own files.
>     **－** A read that has its line under Flags fails nothing, whatever it read: a Decision page, a Spec, the ledger or the archive.
>     **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
>     **－** The librarian refuses an instruction of the handoff to repair a yaml entry. It names what was asked and why in the report, and the refusal does not stop the run.
>     ```
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-documentation-completes` — at the first librarian run whose agent file holds this Render: its event log against the Flags of its brief and its report

> **ratification:**
> ```
> - decision[case 567.1][update][rule-documentation]{ref:rule-documentation}
> - decision[case 567.1][update][rule-brief]{ref:rule-brief}
> - decision[case 567.1][update][estimate-documentation-completes]{ref:estimate-documentation-completes}
> ```

### Case 567.2 — The brief flags the not-needed reads and names the fields it reads

> **recommend:**
> - **Should the instructions name the fields the brief reads from a page?**
>   - Recommended: (a) name the fields; `rule-brief` says the librarian takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
>   - Answer: (a), agreed with the recommendations; the first round's answer agreed in principle and asked who names what.

> **given:**
> `rule-brief` — the brief section of the frame, whose Flags item and Readings due item change
> **＋** `estimate-brief-written` — the Estimate whose Criterion is replaced
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from the page
> **＋** `vault/wiki/brief.md` — the brief the librarian writes
> **＋** `rule-documentation` — constrains: names the reads the job does not need

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> Flags keep their kinds of lines and add one kind: a read that the frame of `rule-documentation` names as one the job does not need. The line gives what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.

> **tasks:**
> - [ ] update `rule-brief` — Flags carry the not-needed reads; Readings due names its fields
>   - old: `each read you made beyond the reads your frame names, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (case 558.3).`
>   - new: `each read you made that your frame says your job does not need, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (cases 558.3, 567.2).`
>   - old: `nothing from the previous brief (case 168).`
>   - new: `` nothing from the previous brief (case 168). The fields are the page's own: an Estimate's `status`, its `target` — the rule — and its `method`, and the `status` of that rule (case 567.2). ``
>   - change: `Flags carry each read the frame says the job does not need; Readings due names the fields it reads (case 567.2)`
> - [ ] update `estimate-brief-written` — the Criterion replaced whole
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Flags hold a line for each read the frame says the job does not need; Readings due takes the status, target and method fields (case 567.2)`
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
>     **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
>     **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
>     **＋** An item stands in one list only. A list with no item is the line "none".
>     **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
>     **－** The brief states no decision: the sort by kind is not a judgment of the work.
>     ```
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-written` — by hand, the brief of the first librarian run whose agent file holds this Render

> **ratification:**
> ```
> - decision[case 567.2][update][rule-brief]{ref:rule-brief}
> - decision[case 567.2][update][estimate-brief-written]{ref:estimate-brief-written}
> ```
