<!-- approved 14:20:02 · session dd5dac5e -->

# Spec — session 1237, 2026-10-01

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

```then
update:
- slug: rule-documentation
  replace:
  - old: 'The reads below are the ones your job is known to need; make them without a flag. When you need a read they do not name, make it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault: no read is forbidden to you (case 558.1). Open a page under `vault/wiki/` for these four reasons:'
    new: 'No read is forbidden to you. A read this frame says your job does not need — the reads listed below as ones your job does not need, and the earlier yaml and the archived page the synthesis names — you make when you need it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault. Any other read needs no flag: a page under `vault/wiki/` but the text of a Decision page, the scripts'' own files, and the reads below (cases 558.1, 567.1). Your job opens a page under `vault/wiki/` for these four reasons:'
  - old: Name every page you open in the report, with the reason and the outcome.
    new: Name in the report each page you open for one of the first three reasons, with the reason and the outcome; a page you open for a fact of the brief, or for any other need, is not named, and the one read of `ledger.md` below stays named (case 567.1).
  - old: A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame does not name it (case 558.1).
    new: A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame says your job does not need it (cases 558.1, 567.1).
  - old: reads three inputs and the reads its frame names, and flags in the brief any other read it makes, so the frame learns what the job needs (case 558.1).
    new: reads three inputs and what its job needs, and flags in the brief a read its frame says the job does not need, so the frame learns what it lacks (cases 558.1, 567.1).
  change: the librarian flags only a read the frame says its job does not need, and names in the report only a page opened for one of the first three reasons and the one read of the ledger (case 567.1)
- slug: rule-brief
  replace:
  - old: read it from the page and name the page in the report.
    new: read it from the page; the page is not named in the report (case 567.1).
  change: a page read for a fact of the brief is not named in the report (case 567.1)
- slug: estimate-documentation-completes
  set:
    status: pending
  change: the Criterion replaced whole — only a read the frame says the job does not need is flagged; the report names only the pages behind a judgment and the one read of the ledger (case 567.1)
  sections:
    Criterion: |-
      When:
      `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

      Then:
      `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
      **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
      **＋** Every read in its event log that its frame says the job does not need has its line under Flags of the new `vault/wiki/brief.md`: `plan.md`, the text of a page under `vault/wiki/decisions/`, a search of the text of the pages under `vault/archive/`, `ledger.md` beyond its one allowed read, `spec.md` beyond its unticked lines and the lines the run ticked, a `materialize.yaml` that `guppi materialize` did not name, and an archived page opened at the synthesis.
      **＋** Its report names each page opened to judge whether a create is the same page or a near one, whether a lesson shares its root cause, or why a script failed, with the reason and the outcome, and the one allowed read of `ledger.md`.
      **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
      **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
      **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
      **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
      **－** Any other read needs no line under Flags and no name in the report: a page under `vault/wiki/` outside `vault/wiki/decisions/`, read for a fact of the brief, the field names of a page or any other need, and the scripts' own files.
      **－** A read that has its line under Flags fails nothing, whatever it read: a Decision page, a Spec, the ledger or the archive.
      **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
      **－** The librarian refuses an instruction of the handoff to repair a yaml entry. It names what was asked and why in the report, and the refusal does not stop the run.
```

```tasks
- [x] update `rule-documentation` — the flagged reads are the ones the frame says the job does not need; the report names only the pages behind a judgment and the one ledger read
- [x] update `rule-brief` — a page read for a fact of the brief is not named in the report
- [x] update `estimate-documentation-completes` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes` — at the first librarian run whose agent file holds this Render: its event log against the Flags of its brief and its report
```

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

```then
update:
- slug: rule-brief
  replace:
  - old: 'each read you made beyond the reads your frame names, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (case 558.3).'
    new: 'each read you made that your frame says your job does not need, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (cases 558.3, 567.2).'
  - old: nothing from the previous brief (case 168).
    new: 'nothing from the previous brief (case 168). The fields are the page''s own: an Estimate''s `status`, its `target` — the rule — and its `method`, and the `status` of that rule (case 567.2).'
  change: Flags carry each read the frame says the job does not need; Readings due names the fields it reads (case 567.2)
- slug: estimate-brief-written
  set:
    status: pending
  change: the Criterion replaced whole — Flags hold a line for each read the frame says the job does not need; Readings due takes the status, target and method fields (case 567.2)
  sections:
    Criterion: |-
      When:
      The librarian rewrites `vault/wiki/brief.md` at the end of its run.

      Then:
      The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
      **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
      **＋** Where things stand, Readings due and Readings at the close are as before.
      **＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
      **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
      **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
      **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
      **＋** An item stands in one list only. A list with no item is the line "none".
      **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
      **－** The brief states no decision: the sort by kind is not a judgment of the work.
```

```tasks
- [x] update `rule-brief` — Flags carry the not-needed reads; Readings due names its fields
- [x] update `estimate-brief-written` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written` — by hand, the brief of the first librarian run whose agent file holds this Render
```

## Case 568 — A recommend item may stay on the parent

> **context:**
> Each Case that `case-guppi` builds records the questions of its rounds in `recommend`. Each item gives a question, what was recommended and the person's answer. Since case 544.2, an item whose answer changed only one sub-case must stand under that sub-case's heading, and the others stand on the parent. `case-guppi` keeps the item on the parent anyway. The reading on ledger line 45 of session 2356 marked `estimate-case-build-records-the-rounds-in-recommend` failed for this. In Case 561, the question on what done means changed only 561.11, and its item stands on the parent. The file `raw/2026-10-01/1237/cases/case-567.md` repeats the fault: the question on whether the report still names every page changed only 567.1, and its item stands on the parent. A second read of Case 561 found more items on the parent that shaped one sub-case, such as the question on what blocks leaving Plan Mode and the question on how `/pre-spec` starts with no question. The person sees no problem in an item on the parent, and chose that the parent is allowed. An item whose answer changed only one sub-case may stand on the parent or under that sub-case. Every other item stands on the parent. No script checks the place, since either place is now correct. Cases 561 and 567 stay as ratified, because under the new rule nothing in them is misplaced.
>
> The rule stands in three sentences. One is in the Render of `rule-case-build`, and two are in the Render of `rule-case-protocol`: the `recommend` row of the sections table and the paragraph on splitting. This Case rewrites all three. The Criterion of `estimate-case-build-records-the-rounds-in-recommend` is replaced whole. The check of the answer noted that the old line on the place of an item is not carried. That line changes on purpose, to the new rule, and every other line is carried word for word. The `purpose` of the Estimate changes to match. The Estimate is set `pending` and is read again on the Cases of a later session.
>
> No reader in code changes. In `guppi/casecheck.py`, `recommend_titles` collects the item titles from every Case of the answer, so the check that each question has an item passes with the item in either place. In `guppi/materialize.py`, a sub-case never reads `recommend` from its parent, and a parent with sub-cases gets a record of its own that carries the parent's `recommend`. So an item on the parent lands on the parent's Decision page.
>
> No create is made, so the vault was not queried. Searches:
> - A Grep of ``changed only one sub-case|changed it alone|changed that sub-case alone|answer changed|own items|its own `recommend`|own recommend`` over the repository, leaving out `vault/raw/` and `vault/archive/`, printed eleven files: `vault/wiki/case-schema.md`, `brief.md`, `log.md`, `rule-decisions-schema.md`, `rule-case-protocol.md`, `rule-case-build.md`, `.claude/agents/case-guppi.md`, `estimate-case-build-records-the-rounds-in-recommend.md`, `estimate-case-protocol-case-form.md`, `decisions/schema.yaml` and `decision-case-459.md`. Of the hits outside `given`, `rule-decisions-schema` says that a sub-case's Decision page carries its own items and a parent's page the rest. That stays true, since the items a sub-case carries are its own. `decisions/schema.yaml` is rendered from that page. `estimate-case-protocol-case-form` says a sub-case has its own `recommend` when it has one, which stays true. The printed line of `decision-case-459` is about lint findings, and the page was not opened. `brief.md` and `log.md` were not read, and History lines were not read.
> - A Grep of `sub-case.{0,80}recommend|recommend.{0,80}sub-case` over `vault/wiki/estimates/` printed seven files: `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-protocol-case-form`, `estimate-generate-writes-the-decision-page`, `estimate-materialize-assembles`, `estimate-spec-write-reaches-the-approved-spec` and `estimate-spec-write-copies-the-ratified-case`. All but the first copy, check or write a sub-case's `recommend` wherever it stands, so their Criteria stand.
> - A Grep of ``recommend` `` printed seven files over `vault/wiki/rules/`: `rule-case-check`, `rule-case-protocol`, `rule-case-build`, `rule-decisions-schema`, `rule-spec-write`, `rule-page-generation` and `rule-language`. Over `.claude/` it printed one file, `.claude/agents/case-guppi.md`. In `rule-case-check`, `rule-spec-write` and `rule-page-generation`, the sub-case passages copy or check a sub-case's `recommend` and set no place for an item, so they stand. `rule-language` holds no such passage.
>
> The other Estimates of `rule-case-build` and `rule-case-protocol` speak of other things: the frame, the round, the showing, the form of the Case and the loaded file. Their Criteria stand.

> **problem:**
> The rule that an item whose answer changed only one sub-case must stand under that sub-case asks `case-guppi` for a judgment it keeps missing, and the person sees no harm in the item standing on the parent. The question is where an item of `recommend` may stand in a Case with sub-cases.

> **recommend:**
> - **How do we stop answers being filed in the wrong place?**
>   - Recommended: (b) every question item goes on the parent, a sub-case carries only the Change items asked on it, and a script can refuse a question title under a sub-case.
>   - Answer: outside the options: simply allow `recommend` to be written on the parent, since the person sees no problem in it.
> - **What happens to the two Cases already ratified with misplaced entries?**
>   - Recommended: (a) leave them as they are; under the new rule nothing in them is misplaced.
>   - Answer: (a). Not answered in the first round, asked again.
> - **Must question entries stand on the parent, or may they stand there?**
>   - Recommended: (a) must, with no script check: every question item on the parent, a sub-case only with the Change items asked on it.
>   - Answer: (c) may: an item stands on the parent or under the one sub-case its answer changed, as `case-guppi` judges, and no script checks the place.

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render sets where an item of `recommend` stands
> **＋** `rule-case-protocol` — the Case schema, whose `recommend` row and splitting paragraph set the same
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the Estimate whose Criterion is replaced
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from `rule-case-build`
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `guppi/casecheck.py` — constrains: compares the question titles with the items of every `recommend` of the answer

> **when:**
> `case-guppi` answers with a Case that has sub-cases, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading.
> **＋** Every other item stands in the parent's `recommend`.
> **－** The check of `guppi/casecheck.py` refuses no item for the place it stands in, the parent or a sub-case.

```then
update:
- slug: rule-case-build
  replace:
  - old: An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, the others in the parent's, and a sub-case carries no `problem` (case 544.2).
    new: An item may stand in the parent's `recommend` whatever its answer changed; an item whose answer changed only one sub-case may stand instead in a `recommend` under that sub-case's heading, and no other item stands there; a sub-case carries no `problem` (cases 544.2, 568).
  change: an item of recommend may stand on the parent; a sub-case holds only items whose answer changed it alone (case 568)
- slug: rule-case-protocol
  replace:
  - old: a sub-case carries the items that changed it alone (case 544.2)
    new: an item may stand on the parent whatever it changed, and a sub-case carries only items whose answer changed it alone (cases 544.2, 568)
  - old: a sub-case carries its own `recommend` with the items whose answer changed that sub-case alone, the parent's `recommend` the rest (case 544.2)
    new: the parent's `recommend` may carry every item, and a sub-case may carry its own `recommend` with items whose answer changed that sub-case alone (cases 544.2, 568)
  change: an item of recommend may stand on the parent; a sub-case holds only items whose answer changed it alone (case 568)
- slug: estimate-case-build-records-the-rounds-in-recommend
  set:
    status: pending
    purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — each item on the parent or under the one sub-case its answer changed, and a sub-case with no problem
  change: the Criterion replaced whole — an item whose answer changed only one sub-case may stand on the parent or under that sub-case (case 568)
  sections:
    Criterion: |-
      When:
      `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

      Then:
      The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
      **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
      **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
      **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
      **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
      **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
      **＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
      **＋** A Case with sub-cases carries `problem` on the parent only.
      **－** No item quotes the person's words word for word.
      **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.
```

```tasks
- [x] update `rule-case-build` — an item may stand on the parent; a sub-case holds only items that changed it alone
- [x] update `rule-case-protocol` — the same in the `recommend` row and in the splitting paragraph
- [x] update `estimate-case-build-records-the-rounds-in-recommend` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-build-records-the-rounds-in-recommend` — by hand, the Case files of a later session after the render, each `recommend` read against the rounds of its Case in the chat
```

## Case 569 — The reply that ends Retro: one line and the ledger block, and when work.md counts as read

> **context:**
> Retro ends with one reply. That reply holds the readings and lessons of the run, and then the agent commits the session folder and calls `/handoff` in the same turn. The skill `.claude/skills/retro/SKILL.md` forbids a report, but it sets only the end of the reply, the `LEDGER` block. It does not say what may stand before that block. It also tells the agent to read `work.md`, the file in which `/work` notes the Baseline and the Expected red. It does not say whether a file the agent wrote itself in the same turn counts as read. Reading W36 of session 1237 failed `estimate-retro-runs-on-to-the-handoff` on both points. In session 4ba72976 the reply at 03:10:52 opened with five headed parts in English (What I built, Left open, Readings taken, Not taken yet, One lesson), and the `LEDGER` block came after them. The chat language is Russian. Lines 325-332 of `raw/2026-10-01/event_log.md` cover Retro, from its mark at 03:09:42 to the last Bash call before the `handoff` mark of line 333. They hold no call of the Read tool on `work.md`. The log cuts each Bash command at about 110 characters, so it cannot show on its own whether a Bash command read the file. The transcript of session 4ba72976 can show it. A Grep for `work\.md` over it printed records 8, 589, 625-627, 1030, 1047, 1084, 1089 and 1110. Of these, records 1030 and 1047 fall between the call of `/retro` and the reply. Record 1030 is the text of the skill. Record 1047 is the output of a Bash command that printed Estimate pages. So no tool call of Retro named `work.md`. The agent had written that file itself with the Write tool at 02:59:28 (event log line 259, transcript record 625). The result of that call said that the file state was current in the agent's context. The agent did not change the file after that, so the text it held was the text on disk. The glossary already names `handoff.md` as the report of Retro, and the person gets the librarian's report at the end of `/handoff`. A report in the reply therefore repeats both. The person decided three things. The reply holds one sentence in the chat language that names the commit, then the block, and nothing else. The skill's text alone holds that form, and the reading by hand checks it. While one agent does both the work and the report, the text of `work.md` that the agent wrote or changed itself in the turn counts as read. Sub-case 569.1 changes the last paragraph of the Render of `rule-retro` and replaces the Criterion of `estimate-retro-runs-on-to-the-handoff` whole. Sub-case 569.2 changes the sentence of the Render on `work.md` and replaces the Criterion of `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` whole. The first line of that Criterion says that the agent reads `work.md`, and the person's option named both Estimates that say this. The check of the answer noted the Criterion lines that the two sub-cases do not carry. Each was changed on purpose: the opening line of each Estimate gains the rule on the read, the line on the one reply gains its form, and the line on a stop gains the reply that opens with `STOP:`. The check also noted that a `then` line of 569.2 shares most of its words with one of 569.1. That is on purpose: the clause on the read stands word for word in both Criteria, so the two Estimates say the same thing about it. The two replace pairs on `rule-retro` stand in different paragraphs of the Render and do not overlap. The new sentences agree with the rest of the skill: the opening sentence against a report stays, and so does the sentence that a stop opens with `STOP:`. Not done here: the person said that once the work and the report are split between agents, reading the file becomes required. No Case takes that split up now. No hook is added. The skill is rendered at the librarian's run, and no code reads the text of this reply, so no old form is kept. The vault query was not run because no page is created. The `given` of 569.1 has more than seven lines because its `then` names each file of the session's folder, each skill of the run and the rule of the chat language. These are one behaviour, the one reply that ends Retro, and the Estimate's Criterion already named them before this Case. Searches over the frame follow. A Grep for `work\.md` over `vault/wiki/` printed 15 files: `brief.md`, `log.md`, `rule-permissions`, `estimate-permissions`, `rule-work-mode`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-runs-on-to-the-handoff`, `decision-case-479.1` to `decision-case-479.5`, `rule-retro` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`. `rule-permissions`, `estimate-permissions` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` speak of writing the file. `estimate-retro-red-in-the-baseline-is-not-charged` speaks of what its Baseline holds, not of reading it, so it is left alone. The Purpose of `rule-work-mode` says that Retro reads the mark of an expected red. That stays true, because Retro takes the mark in, by a Read or by the text it wrote itself. A Grep for `no report` over the repository outside `vault/raw/`, `vault/archive/`, `vault/wiki/decisions/`, `log.md` and `brief.md` printed `.claude/skills/retro/SKILL.md`, `rule-retro` and `estimate-retro-runs-on-to-the-handoff`. Each of them stays true or is changed here. A Grep for `ends Retro|end of Retro|ending Retro` over `vault/wiki/` outside `decisions/` printed `rule-case-protocol`, `case-schema.md`, `log.md`, `rule-retro-onward`, `rule-work-mode`, `glossary.md`, `entity-glossary`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-work-mode-takes-the-work-readings` and `estimate-retro-runs-on-to-the-handoff`. Each says that the lines stand in that one reply, or that the agent goes on after it, and none sets what else the reply holds. `case-schema.md` also says that a line closed at Retro shows no Frontier, which the new form keeps. A Grep for `ends Retro|end of Retro|reply that ends|Retro` over `.claude/` printed the skills `work`, `hi`, `retro` and `handoff`. The hit in `hi` speaks of closing a line at Retro, and `work` and `handoff` set no form for this reply. The hook of `rule-retro-onward` judges only the first word `STOP:`, which the new sentence does not open with. `estimate-retro-onward-sends-the-agent-to-the-handoff` therefore stands. `estimate-retro-loads` promises only that the rendered file equals the Render, so it stands too.

> **problem:**
> The skill forbids a report but sets only the end of the reply that ends Retro, so a report in English stood before the `LEDGER` block. The skill also tells the agent to read `work.md` without saying whether a file it wrote itself in the same turn counts as read. The question was what that reply may hold, what enforces it, and what reading `work.md` means.

> **recommend:**
> - **What does reading `work.md` mean when the agent wrote it in the same turn?**
>   - Recommended: (a) Retro opens `work.md` with the Read tool as its first step, always, even when the agent wrote it in this turn; the event log shows the Read.
>   - Answer: (b) what the agent already holds counts: the Read is needed only when the agent did not write or change the file in this turn. While one agent does the work and the report, this counts; once the work and the report are split between agents, reading the file becomes required.

### Case 569.1 — The reply that ends Retro holds one line and the ledger block

> **recommend:**
> - **What may stand before the ledger block in the reply that ends Retro?**
>   - Recommended: (a) one short line in Russian, then the block: one sentence in the chat language that names the commit, then the `LEDGER` block and nothing else; a headed part or a list before the block breaks the rule.
>   - Answer: (a).
> - **Does anything beyond the skill's text hold the form of that reply?**
>   - Recommended: (a) the text alone, checked by the reading: the skill states the form exactly, and the reading by hand of the Estimate catches a departure.
>   - Answer: (a).

> **given:**
> `rule-retro` — the rule of the skill `/retro`, whose Render sets the reply that ends Retro
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from that Render
> **＋** `estimate-retro-runs-on-to-the-handoff` — the promise whose Criterion this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the tasks of the run, whose boxes Retro sorts
> **＋** `raw/<date>/<hi HHMM>/work.md` — the Baseline and the Expected red that `/work` writes
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro, which `/handoff` writes
> **＋** `.claude/skills/work/SKILL.md` — the run that calls `/retro`
> **＋** `.claude/skills/handoff/SKILL.md` — the step after the reply that ends Retro
> **＋** `vault/wiki/where-to-stop.md` — the conditions of a stop and the reply that stops
> **＋** `rule-language` — the language of the chat

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
> **－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
> **＋** After that reply, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

```then
update:
- slug: rule-retro
  replace:
  - old: Then end the reply with one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included; the reply asks the person nothing.
    new: 'Then end the reply: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included. The reply holds nothing else — no heading, no list and no other paragraph — since `handoff.md` is the report of Retro, and it asks the person nothing (case 569.1).'
  change: the reply that ends Retro holds one sentence in the language of the chat that names the commit, then the LEDGER block, and nothing else (case 569.1)
- slug: estimate-retro-runs-on-to-the-handoff
  set:
    status: pending
  change: the Criterion replaced whole — the reply that ends Retro holds one sentence in the language of the chat that names the commit and the LEDGER block, no heading, list or other paragraph; work.md the agent wrote or changed in the same turn counts as read (case 569.1)
```

```tasks
- [x] update `rule-retro` — the reply that ends Retro holds one sentence that names the commit and the `LEDGER` block, nothing else
- [x] update `estimate-retro-runs-on-to-the-handoff`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-runs-on-to-the-handoff` — in a later session
```

### Case 569.2 — work.md the agent wrote in the same turn counts as read

> **given:**
> `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the promise whose Criterion this sub-case replaces
> **＋** `rule-retro` — the rule of the skill `/retro`, whose Render tells the agent to read `work.md`
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from that Render
> **＋** `.claude/skills/work/SKILL.md` — the run that writes `work.md` and its marks of an expected red
> **＋** `raw/<date>/<hi HHMM>/work.md` — the Baseline and the Expected red of the session
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro, which holds the Observations

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> The agent reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read.
> **＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md` that names the check and the page or file it waits for.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
> **－** In a session with no `work.md`, a red or a refusal of such a check is a line of `## Observations` by the agent's judgment.
> **－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

```then
update:
- slug: rule-retro
  replace:
  - old: Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3).
    new: 'Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3): when you wrote or changed it yourself in this turn, the text you hold counts as read; otherwise open it with the Read tool (case 569.2).'
  change: work.md that the agent wrote or changed itself in the same turn counts as read; otherwise Retro opens it with the Read tool (case 569.2)
- slug: estimate-retro-red-check-of-an-updated-page-is-a-handoff-note
  set:
    status: pending
  change: the Criterion replaced whole — the agent reads work.md with the Read tool unless it wrote or changed the file itself in the same turn, whose text then counts as read (case 569.2)
```

```tasks
- [x] update `rule-retro` — `work.md` that the agent wrote or changed itself in the same turn counts as read
- [x] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — in a later session
```

## Deferred

## Case 570 — The cost of rebuilding a Case waits for a later session

> **context:**
> `rule-case-rebuild-cost` holds the defer of case 566: a Case is rewritten whole and returned whole to the main agent when only a sub-case changed. In session 1237 Cases 567, 568 and 569 were each built and returned whole again after the round. The person put the remaining items off to go to work.

> **problem:**
> The decision on how a Case is rebuilt and returned is put off again.

```then
defer:
  - slug: rule-case-rebuild-cost
    type: rule
    purpose: "Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases"
```

## Case 571 — The failed check of the finished Case waits for a later session

> **context:**
> `estimate-case-build-checks-the-finished-case` failed in session 2356, ledger line 44. At the `/pre-spec` of that session, `ask-guppi` found two pages that Cases 561.3 and 561.13 made false without naming them, and a clash between Case 562 and the loop of 561.1 and 561.2. The person put the remaining items off to go to work.

> **problem:**
> The decision on how `case-guppi` finds the pages a Case makes false and the rules acting at the same moment is put off.

```then
defer:
  - slug: estimate-case-build-checks-the-finished-case
    type: estimate
    purpose: "Whether case-guppi, before it answers, names each page its Case makes false and each rule acting at the same moment; failed in session 2356 with two pages and one rule missed"
```

## Case 572 — The reading of the plain-round Estimate waits again

> **context:**
> `estimate-case-build-writes-a-plain-round` failed in session 1736, and case 563 put its new reading off. Its reading needs a first and a later round of `case-guppi` after the render of case 557.3. The rounds of session 1237 ran after that render, but nobody read them for this Estimate. The person put the remaining items off to go to work.

> **problem:**
> The new reading of this Estimate is put off again.

```then
defer:
  - slug: estimate-case-build-writes-a-plain-round
    type: estimate
    purpose: "Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a quotation as a blockquote and an unknown term explained; failed in session 1736, to be read on a first and a later round after the render of case 557.3"
```

## Case 573 — The reading of the defer Estimate waits for these defers

> **context:**
> `estimate-spec-write-writes-a-defer` failed in session 1736, and case 564 put its new reading off onto the defers of session 2356. The defers of this reply are the first defers since that session's librarian run. The person put the remaining items off to go to work.

> **problem:**
> The new reading of this Estimate is put off. The defers of this session are its input.

```then
defer:
  - slug: estimate-spec-write-writes-a-defer
    type: estimate
    purpose: "Whether the Spec hook writes a short-form defer under the Deferred heading of the plan and of spec.md as the reply showed it; failed in session 1736, to be read on the defers of session 1237"
```

## Case 574 — The move of the main agent's rules into three files waits

> **context:**
> `rule-orchestration` holds the design ratified in case 561.13 and the defer of case 424. The main agent's rules move into a file `/hi` loads, a small shared file, and `case-schema.md` for `case-guppi` alone. The person put the remaining items off to go to work.

> **problem:**
> The move is put off again.

```then
defer:
  - slug: rule-orchestration
    type: rule
    purpose: "Prevents the main agent from loading the form of a Case it does not build, a design ratified in case 561 for a later session - a file of rule-orchestration that /hi loads in place of case-schema.md, holding what the main agent alone does; a third small file of its own rule, loaded by /hi and read by case-guppi, holding the one rule, the form of the ledger lines, atomicity and the harness; case-schema.md holding the form of a Case, read by case-guppi alone"
```

## Case 575 — How guppi onward --plan finds a Case still out waits

> **context:**
> `guppi onward --plan`, the hook of `rule-prespec-onward`, finds a Case still out by the time of its file against its last decision line in `ledger.md`. A Case built again and ratified with lines the ledger already holds adds no line, so the hook stays silent after it (handoff of session 2356, Observations). The person put the remaining items off to go to work.

> **problem:**
> The decision on what else the hook should judge a Case still out by is put off.

```then
defer:
  - slug: rule-prespec-onward
    type: rule
    purpose: "Whether guppi onward --plan judges a Case still out by something other than the ledger's last decision line, since a re-ratification with unchanged lines adds none and the hook then stays silent"
```

## Case 576 — The skipped schema test of the Estimate waits

> **context:**
> At the Work readings of session 2356, `uv run pytest tests/test_schemas.py -k estimate` gave 5 passed and 1 skipped, "no conditional on a field". The Criterion of `estimate-estimates-schema-checked` names a section required on `passed` and `failed`. Whether the skip leaves that untested was not settled. The person put the remaining items off to go to work.

> **problem:**
> The question whether the skipped test leaves the required section untested is put off.

```then
defer:
  - slug: estimate-estimates-schema-checked
    type: estimate
    purpose: "Whether the skip no conditional on a field of tests/test_schemas.py -k estimate leaves untested the section the Criterion requires on passed and failed"
```
