<!-- approved 02:02:05 · session c9c18452 -->

# Spec — 2026-09-23, session 0034

## Case 354 — a sprint item passed over goes to the Backlog

> **context:**
> A session that passes over a milestone item closes its Frontier line `[-] … · sprint` (case 310.5). No page keeps a trace of it: `deferred_by` does not grow, and `frontier.md` goes to the archive with its session. `rule-work-mode` and `rule-subagent-guppi` have stood in Slice 3b since 2026-09-12: 19 defers before 310.5 and one pass by `· sprint` after it. The trace of these passes is only in the 33 archived `frontier.md` files.
> `rule-sprint` stands `built` and changes Milestones and Backlog only by the `update` of a Case; `rule-page-generation` stands `draft`, and `generate` is the only writer to `wiki/`; the vault answers that no page sets a threshold or moves an item by itself, and that the three counts of today are separate. The Estimates of `rule-sprint` — `estimate-sprint-renders-the-backlog` on the render, `estimate-sprint-checks-the-file` on `--check`, `estimate-sprint-ticks-the-spec` on the ticks — do not speak of a move and are not touched; the move is a step after the cascade, so `estimate-generate-cascades` is not touched.

> **problem:**
> A sprint item can be passed over without end, and nothing takes it off the agenda. A script must count the passes in a row and move the item to the Backlog at three, with no judgment of the agent.

### Case 354.1 — the move of an item passed over in three sessions in a row

> **given:**
> `generate` is the only writer to `wiki/`, the sprint page `entity-sprint-<id>` included.
> **＋** A milestone item is a line under `### <name>` in `## Milestones`; its pages are every `[[slug]]` before the first ` — `, by `sprint.item_slugs` (case 313).
> **＋** Every session writes `frontier.md` into its folder; `guppi archive` moves the folder whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`.
> **＋** A Frontier line is closed `[-]` when its item was put off (`· sprint`, `· defer case N`), and `[x]` when it was taken up (`· case N`, `· work`).
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi generate` has applied every entry of the run and run the cascade.

> **then:**
> For every item under `## Milestones`, the script reads the `frontier.md` of `raw/` and of the archive, from the newest session to the oldest by date and `HHMM`, and counts the lines whose title — the text before the first ` · ` — holds one of the item's slugs in a code span.
> **＋** A `[-]` line adds one; an `[x]` line stops the count; a session without such a line is passed by.
> **＋** At a count of 3 or more, the item's line leaves its milestone, unchanged, for the end of `## Backlog`.
> **＋** The History of the sprint page gets the line `moved to the Backlog: <slug> passed over in <N> sessions in a row — <HHMM>, … · generate`, and stdout one line on the move.
> **－** An open `[ ]` line is not counted.
> **－** A note — a line with no `[[slug]]` before the ` — ` — is not counted and not moved; the items of `## Backlog` and `## Closed` are not counted.

```then
update:
  - slug: rule-sprint
    set: {implementation_ref: [guppi/sprint.py, tests/test_sprint.py, guppi/generate.py, tests/test_generate.py]}
    replace:
      - old: "the backlog changes by an `update` of the sprint page, a Case."
        new: "the backlog changes by an `update` of the sprint page, a Case, and by one move of `generate`: a milestone item passed over in three sessions in a row goes to the Backlog (case 354.1)."
    change: a milestone item passed over in three sessions in a row goes to the Backlog by generate (case 354.1)
  - slug: rule-page-generation
    replace:
      - old: "never by hand (case 104). Once an entry is applied"
        new: "never by hand (case 104). After the cascade, the script moves a milestone item of the sprint page passed over in three sessions in a row to its Backlog, by the Frontiers of `raw/` and the archive (`rule-sprint`, case 354.1). Once an entry is applied"
    change: after the cascade, the move of a passed-over sprint item to the Backlog (case 354.1)
create:
  - slug: estimate-sprint-moves-a-passed-over-item
    type: estimate
    ref: rule-sprint
    kind: QA
    purpose: A milestone item passed over in three sessions in a row goes to the Backlog by generate, never by hand
    method: pytest tests/test_generate.py, the tests of the move, plus one reading of the History of the sprint page after the librarian's run
    tags: [sprint, harness]
```

```tasks
- [x] update `rule-sprint` — one `replace` pair in Purpose, `implementation_ref` + `guppi/generate.py`, `tests/test_generate.py`
- [x] update `rule-page-generation` — one `replace` pair in Purpose
- [x] create `estimate-sprint-moves-a-passed-over-item`
- [x] `guppi/generate.py` — the move as a step after `cascade()`, on `sprint.split_milestones` and `sprint.item_slugs`, no second parse; the History line `· generate`, not `· cascade`; the docstring names the move
- [x] `tests/test_generate.py` — three `[-]` in a row move the item; an `[x]` between them does not; a session without the line is passed by; a note is not moved; the History line; `raw/` and the archive read together
- [x] read `estimate-sprint-moves-a-passed-over-item`
```

### Case 354.2 — a milestone the move left empty leaves the Milestones

> **given:**
> The current milestone is the first `### ` under `## Milestones` with an item not done, or with no item (case 229.3); `/hi` takes the Frontier from the current milestone only.
> **＋** By 354.1, `generate` moves the line of an item from its milestone to `## Backlog`.
> **＋** A note — a line with no `[[slug]]` before the ` — ` — is not moved and keeps its milestone open (case 313).
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi generate` moves, by 354.1, the last item line out of a milestone.

> **then:**
> The heading `### <name>` of that milestone leaves `## Milestones`; the next milestone becomes the current one.
> **＋** The History of the sprint page gets the line `milestone <name> left the Milestones: its items moved to the Backlog · generate`, and stdout one line.
> **－** A milestone with no item before the run stays: rule 229.3 does not change for it.
> **－** A milestone where a note is left stays.
> **－** Nothing is written to `## Closed`: nothing of that milestone was built.

```then
update:
  - slug: rule-sprint
    replace:
      - old: "goes to the Backlog (case 354.1)."
        new: "goes to the Backlog, and a milestone the move left with no line leaves the Milestones (cases 354.1, 354.2)."
    change: a milestone the move left with no line leaves the Milestones (case 354.2)
  - slug: rule-page-generation
    replace:
      - old: "by the Frontiers of `raw/` and the archive (`rule-sprint`, case 354.1)."
        new: "by the Frontiers of `raw/` and the archive, and drops a milestone the move left with no line (`rule-sprint`, cases 354.1, 354.2)."
    change: the move drops a milestone it left with no line (case 354.2)
create:
  - slug: estimate-sprint-drops-an-emptied-milestone
    type: estimate
    ref: rule-sprint
    kind: QA
    purpose: A milestone the move left with no line leaves the Milestones, so the next one becomes current
    method: pytest tests/test_generate.py, the tests of the move
    tags: [sprint, harness]
```

```tasks
- [x] update `rule-sprint` — one `replace` pair in Purpose, over the text of 354.1
- [x] update `rule-page-generation` — one `replace` pair in Purpose, over the text of 354.1
- [x] create `estimate-sprint-drops-an-emptied-milestone`
- [x] `guppi/generate.py` — in the step of the move, the heading of a milestone left with no line removed, the History line; the docstring
- [x] `tests/test_generate.py` — a milestone emptied by the move leaves; one empty before the run stays; one with a note stays; the History line
- [x] read `estimate-sprint-drops-an-emptied-milestone`
```

### Case 354.3 — a sprint item in the Frontier is one line, its slug in a code span

> **given:**
> `/hi` writes `frontier.md` by the Render of `rule-skill-hi`, the text of `.claude/skills/hi/SKILL.md`.
> **＋** By 354.1, `generate` counts a Frontier line for an item when its title holds the item's slug in a code span.
> **＋** An item names one or more pages: every `[[slug]]` before the first ` — ` (case 313).

> **when:**
> The person invokes `/hi`, and the agent writes the Frontier line of an item of the current milestone.

> **then:**
> Every milestone item is a line of its own; its title opens with the slug of each page the item names, each in a code span: ``- [ ] C1 — `rule-x`, <milestone> · sprint``.
> **－** The other lines of the Frontier keep their form.
> **－** `rule-prespec` does not change: it does not look for a line without a slug.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "`- [ ] W<n> — <title> · <source>` under `## Work`."
        new: "`- [ ] W<n> — <title> · <source>` under `## Work`. An item of the sprint's milestone is a line of its own whose title opens with the slug of each page it names, each in a code span — ``- [ ] C1 — `rule-x`, <milestone> · sprint`` — so that `generate` counts it (case 354.3)."
    change: a sprint item in the Frontier is one line, its title opening with its slugs in code spans (case 354.3)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "and `## Work`, lines `- [ ] W<n> — <title> · <source>`;"
        new: "and `## Work`, lines `- [ ] W<n> — <title> · <source>`; an item of the current milestone is a line of its own whose title opens with the slug of each of its pages in a code span (354.3);"
    change: the Criterion names the line of a sprint item with its slugs in code spans (case 354.3)
```

```tasks
- [x] update `rule-skill-hi` — one `replace` pair in the Render
- [x] update `estimate-hi-writes-frontier` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`
```

### Case 354.4 — the brief names in Flags the items moved to the Backlog

> **given:**
> The librarian writes `brief.md` by the Render of `rule-brief`, the text of `.claude/agents/librarian-guppi.md`; it runs `generate` itself and sees its stdout.
> **＋** By 354.1 and 354.2, `generate` prints one stdout line per move and one per milestone dropped.
> **＋** The Deferred list of the brief leaves out a target the sprint page names, in the Backlog too (case 229.4).

> **when:**
> The librarian writes the Flags of `brief.md` after a run in which `generate` moved an item.

> **then:**
> Flags carry one line per item moved — its slug, the milestone it left, the count and the sessions — and one line per milestone dropped, by its name.
> **＋** The frame says the sprint page changes by a Case or by the move of `generate`.
> **－** A moved item goes neither to Deferred nor to Next session; only a Case the person writes brings it back.
> **－** A run with no move adds no line.

```then
update:
  - slug: rule-brief
    replace:
      - old: "failed Estimates; MOC candidates; stale defers; contradictions; the lint output."
        new: "failed Estimates; MOC candidates; stale defers; contradictions; every item `generate` moved to the Backlog in this run — its slug, its milestone, the count and the sessions — and every milestone it dropped, from the lines it printed (case 354.4); the lint output."
      - old: "the sprint page changes by a Case, and"
        new: "the sprint page changes by a Case, or by the move of `generate` (case 354.1), and"
    change: Flags name the items generate moved to the Backlog and the milestones it dropped (case 354.4)
  - slug: estimate-brief-written
    replace:
      - old: "Where things stand, Readings due, Deferred, Flags and Readings at the close are as today, their content unchanged."
        new: "Where things stand, Readings due, Deferred, Flags and Readings at the close are as today, their content unchanged, but Flags also name every item `generate` moved to the Backlog and every milestone it dropped in the run (354.4)."
    change: the Criterion names the Flags line of a move to the Backlog (case 354.4)
```

```tasks
- [x] update `rule-brief` — two `replace` pairs in the Render: the Flags line, and the sprint page changed by a Case or by the move of `generate`
- [x] update `estimate-brief-written` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] read `estimate-brief-written`
```

## Case 355 — the chat form of a Case: the section of the person, and sub-cases in one reply

> **context:**
> `case-schema.md` describes `ratification` as the human's sign-off, question or own alternative, ending with a preview of the ledger lines. It does not forbid the agent's text there, and in Case 354 the agent wrote the effect of a first run and its own notes into `ratification`. The place for the agent's text already stands: one horizontal rule after the Case, by the section Language. The schema describes a sub-case as `### Case N.M` under its parent with its own `ratification`, and a parent's sign-off does not cover its children; it does not say whether sub-cases are shown in one reply or one by one. In Case 354 they were shown one by one: four acknowledgements, four Frontiers, and the parent's `context` out of view.
> `rule-case-protocol` stands `draft`; the live reading of its Render is `estimate-case-protocol-loaded`, `pending`; the form of a Case in the chat is read by `estimate-case-protocol-case-form`, `pending`; each gets a line in its Criterion, and the other Estimates of the rule are not touched.

> **problem:**
> The schema does not separate the section of the person from the agent's text, and does not say how a Case with sub-cases is shown; the agent picks the form itself.

### Case 355.1 — `ratification` holds the ledger preview alone

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the agent takes the form of a Case from it.
> **＋** The `Stop` hook writes only the lines inside a fence tagged `LEDGER`; the same lines in an untagged fence are a preview.
> **＋** The section Language allows one horizontal rule in the chat, after the Case or its last sub-case, only when the agent's own text follows.

> **when:**
> The agent shows a Case in the chat.

> **then:**
> `ratification` holds the preview of the ledger lines in an untagged fence, and nothing else.
> **＋** The agent's own text — a note, an effect, a caveat — stands after the Case, after one horizontal rule; the turn ends with a plain question.
> **＋** A fact the Case depends on — the effect of a first run, the state of a page — goes to `context`.
> **－** The human's sign-off, question or alternative is their reply; the section keeps its place among the eight.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "The human's sign-off, question, or their own alternative. Ends with a preview of the ledger lines in an untagged fence, and the turn ends with a plain question in the chat, never a picker tool."
        new: "In the chat, the preview of the ledger lines in an untagged fence and nothing else; the human's sign-off, question or own alternative is their reply. The agent's own text stands after the Case, after one horizontal rule, and the turn ends with a plain question in the chat, never a picker tool (case 355.1)."
    change: ratification in the chat is the ledger preview alone, the agent's text after one horizontal rule (case 355.1)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: |-
          **＋** The row of `ratification` says that in the chat the section is the preview of the ledger lines alone, and the agent's own text stands after the Case, after one horizontal rule (355.1).
          **＋** `render --check` after the render exits 0.
    change: the Criterion names the row of ratification (case 355.1)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: "**－** The eight sections of the chat form do not change."
        new: "**－** The eight sections of the chat form do not change; in the chat `ratification` holds the preview of the ledger lines alone, and the agent's own text stands after the Case, after one horizontal rule (355.1)."
    change: the Criterion names ratification as the ledger preview alone (case 355.1)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the row of `ratification`
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion; the page goes `pending`
- [ ] read `estimate-case-protocol-loaded`
- [ ] read `estimate-case-protocol-case-form`
```

### Case 355.2 — a Case with sub-cases is shown in one reply

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the agent takes the form of a Case from it.
> **＋** A sub-case has its own `when`, `then`, `tasks` and `ratification`; a parent's sign-off does not ratify its children (cases 60, 159).
> **＋** The acknowledging reply opens with the `LEDGER` block and ends with the Frontier and the question (case 167).

> **when:**
> The agent shows a Case that has sub-cases.

> **then:**
> One reply shows the parent's `context`, `problem` and `recommend`, then every sub-case whole, each with its own `ratification`.
> **＋** The person ratifies every sub-case at once or names the ids; the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming their ids, and one Frontier.
> **＋** A sub-case the person questions or changes is shown again alone, by the rule of a changed Case.
> **－** A sub-case born of a follow-up question after the parent was shown is shown when it is born.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "Ratifying a parent does not ratify its children."
        new: "Ratifying a parent does not ratify its children. A Case with sub-cases is shown in one reply — the parent's `context`, `problem`, `recommend`, then every sub-case whole; the person ratifies them all at once or names the ids, and the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming those ids, and one Frontier; a sub-case the person questions or changes is shown again alone (case 355.2)."
    change: a Case with sub-cases is shown in one reply, ratified at once or by ids (case 355.2)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: |-
          **＋** The section Splitting says that a Case with sub-cases is shown in one reply, ratified at once or by ids, with one `LEDGER` block and one Frontier (355.2).
          **＋** `render --check` after the render exits 0.
    change: the Criterion names the sub-cases shown in one reply (case 355.2)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: '**＋** `tasks` carries no `contract` line and no "block N" line.'
        new: |-
          **＋** `tasks` carries no `contract` line and no "block N" line.
          **＋** A Case with sub-cases is shown in one reply — the parent's `context`, `problem`, `recommend`, then every sub-case whole; a sub-case questioned or changed is shown again alone (355.2).
    change: the Criterion names the sub-cases shown in one reply (case 355.2)
  - slug: estimate-case-protocol-acknowledging-reply
    replace:
      - old: "**＋** The headings and labels are in the language of the chat."
        new: |-
          **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` naming the ids, one Frontier (355.2).
          **＋** The headings and labels are in the language of the chat.
    change: the Criterion names the one acknowledging reply of a Case with sub-cases (case 355.2)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the section Splitting
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-acknowledging-reply` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-loaded`
- [ ] read `estimate-case-protocol-case-form`
- [ ] read `estimate-case-protocol-acknowledging-reply`
```

## Case 356 — what a Frontier closer tells apart (takes up defer 352)

> **context:**
> As the page `decision-case-352` stands: Case 346 of plan 2046 deferred `rule-skill-hi` and `rule-prespec` with one question — what a Frontier closer must tell apart. Case 351 of the same plan changed the Render of `rule-prespec`, and by case 186.2 a Case that changes a page another Case of the same plan defers is a finding; so 352 deferred `rule-skill-hi` alone. The questions of the defer: whether a Work line closes in a second moment of its own; whether pre-spec requires closed lines under `Cases` alone; whether `· sprint` and `· defer case N` stay two closers or become one; and whether a session that passes over an item of the sprint leaves any trace. The trace is answered by 354.1: `guppi archive` keeps every `frontier.md`, and `generate` counts the passes from it; no page changes for it. `rule-prespec` is changed by this Case itself and needs no defer.
> `rule-skill-hi` stands `draft` with `deferred_by` 352; `rule-prespec` stands `draft`, with no defer; `rule-case-protocol` stands `draft`, and its Plan Mode paragraph says Plan Mode does not end while a line is open and lists the closers without `· sprint`; in this plan 354.3 changes `rule-skill-hi` and 355 `rule-case-protocol` too, and no defer stands in this plan, so 186.2 does not fire. `estimate-hi-writes-frontier` of `rule-skill-hi`, `estimate-prespec-checks-the-plan` of `rule-prespec` and `estimate-case-protocol-loaded`, the live reading of the Render of `rule-case-protocol`, are touched; `estimate-prespec-binds-a-sprint-line` speaks of the closer `case N` alone and `estimate-prespec-reconciles` of no kind of Frontier line — neither is touched.

> **problem:**
> The defer of a page and the change of that page stand in one plan. Either the question loses its second page, or the change waits a session.

### Case 356.1 — pre-spec checks the lines of `Cases`; a `W` line closes when its work is done

> **given:**
> `/hi` writes the Frontier in two lists, `## Cases` and `## Work`, by the Render of `rule-skill-hi`.
> **＋** `prespec.check_frontier` reads every line of `frontier.md`: the id the first token after the box, the closer the last segment after ` · `.
> **＋** The work of a `W` line — a reading, a tick, a commit — is done in Work Mode, after pre-spec.
> **＋** `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`.
> **＋** `tests/test_prespec.py` fixes `--check`.

> **when:**
> `guppi prespec --check` reads the session's `frontier.md`.

> **then:**
> An open line under `## Cases` is a finding, as today.
> **＋** An open line under `## Work` is no finding; it closes `· work` when its work is done, in Work Mode.
> **＋** A closed `W` line is checked as any closed line: a `case N` with no heading in the plan is a finding.
> **＋** `case-schema.md` says Plan Mode does not end while a line under `## Cases` is open.
> **－** A `W` line that turns out to be a decision closes `· case N` in Plan Mode, as today.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "`/pre-spec` fails on an open line."
        new: "`/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, in Work Mode (case 356.1)."
    change: pre-spec fails on an open Cases line; a W line closes when its work is done (case 356.1, supersedes 352)
  - slug: rule-prespec
    replace:
      - old: "(the session's folder, case 73) still open,"
        new: "(the session's folder, case 73) still open under `## Cases` — a line of `## Work` may stand open until its work is done (case 356.1) —,"
    change: an open line under Work is no finding (case 356.1)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "**－** `/pre-spec` does not change: an open line of either list is a finding."
        new: "**－** `/pre-spec` finds an open line under `## Cases`; a `W` line stands open until its work is done and closes `· work` in Work Mode (356.1)."
    change: the Criterion names the W line open until its work is done (case 356.1)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "a missing file, an open line, a `case N`"
        new: "a missing file, an open line under `## Cases` — an open line under `## Work` is clean (356.1) —, a `case N`"
    change: the Criterion names an open Work line clean (case 356.1)
  - slug: rule-case-protocol
    replace:
      - old: "Plan Mode does not end while a line is open;"
        new: "Plan Mode does not end while a line under `## Cases` is open — a `W` line closes when its work is done (case 356.1);"
    change: Plan Mode ends with no open line under Cases (case 356.1)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: |-
          **＋** The Plan Mode paragraph says Plan Mode does not end while a line under `## Cases` is open (356.1).
          **＋** `render --check` after the render exits 0.
    change: the Criterion names the open Cases line of the Plan Mode paragraph (case 356.1)
```

```tasks
- [x] update `rule-skill-hi` — one `replace` pair in the Render
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] update `estimate-hi-writes-frontier` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] update `estimate-prespec-checks-the-plan` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the Plan Mode paragraph
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] `guppi/prespec.py` — `check_frontier` tells `## Cases` from `## Work`, an open line under `## Work` no finding; the docstring
- [x] `tests/test_prespec.py` — an open `C` a finding; an open `W` none; a closed `W` with a `case N` absent from the plan a finding
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-hi-writes-frontier`
- [x] read `estimate-prespec-checks-the-plan`
- [ ] read `estimate-case-protocol-loaded`
```

### Case 356.2 — a sprint item never closes `· defer case N`

> **given:**
> A sprint item left for later closes `[-] … · sprint`, with no decision and no `deferred_by` (case 310.5).
> **＋** By 354.1, `generate` counts the passes by the `[-]` lines, whatever the closer.
> **＋** The Deferred list of the brief leaves out a target the sprint page names (case 229.4).
> **＋** `prespec.check_frontier` takes the source from the segment just before the closer (case 335).
> **＋** `tests/test_prespec.py` fixes `--check`.

> **when:**
> The agent closes a Frontier line whose source is `sprint`, and `guppi prespec --check` reads it.

> **then:**
> A line whose source is `sprint`, put off, closes `[-] … · sprint`, never `· defer case N`.
> **＋** A line whose source is `sprint` closed `· defer case N` is a finding: `frontier: C<n> defers a sprint item; an item left for later closes [-] with sprint`.
> **＋** The Plan Mode paragraph of `case-schema.md` names `[-] … · sprint` among the closers.
> **－** A line of another source closes `· defer case N` as today.
> **－** The `deferred_by` already standing on pages does not change.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "no `deferred_by` (case 310.5);"
        new: "no `deferred_by` (case 310.5), never `· defer case N` (case 356.2);"
    change: a sprint line never closes defer case N (case 356.2)
  - slug: rule-prespec
    replace:
      - old: "no Case and no `defer` needed (case 310.6),"
        new: "no Case and no `defer` needed (case 310.6), and a line whose source segment is `sprint` closed `· defer case N` is a finding — a sprint item is not deferred (case 356.2),"
    change: a sprint line closed defer case N is a finding (case 356.2)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "— no decision, no `deferred_by` (case 310.5)."
        new: "— no decision, no `deferred_by` (case 310.5); a line of the sprint never closes `· defer case N` (356.2)."
    change: the Criterion names the sprint line never deferred (case 356.2)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "`[x] … · sprint` a finding (case 310.6)."
        new: "`[x] … · sprint` a finding (case 310.6); a line whose source segment is `sprint` closed `· defer case N` a finding (356.2)."
    change: the Criterion names the finding on a deferred sprint line (case 356.2)
  - slug: rule-case-protocol
    replace:
      - old: "`· defer case N` when deferred."
        new: "`· defer case N` when deferred, `[-] … · sprint` for an item of the sprint left for later — never `· defer case N` (case 356.2)."
    change: the Plan Mode paragraph names the closer sprint (case 356.2)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: |-
          **＋** The Plan Mode paragraph names `[-] … · sprint` for a sprint item left for later, never `· defer case N` (356.2).
          **＋** `render --check` after the render exits 0.
    change: the Criterion names the closer sprint of the Plan Mode paragraph (case 356.2)
```

```tasks
- [x] update `rule-skill-hi` — one `replace` pair in the Render
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] update `estimate-hi-writes-frontier` — one `replace` pair inside the Criterion
- [x] update `estimate-prespec-checks-the-plan` — one `replace` pair inside the Criterion
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the Plan Mode paragraph
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] `guppi/prespec.py` — in `check_frontier`, a finding on a line whose source is `sprint` and whose closer is `defer case N`; the docstring
- [x] `tests/test_prespec.py` — a sprint line closed `· defer case N` a finding; a `brief` line closed the same way none
- [ ] read `estimate-hi-writes-frontier`
- [x] read `estimate-prespec-checks-the-plan`
- [ ] read `estimate-case-protocol-loaded`
```

## Case 357 — the one allowed read of `ledger.md` is not refused

> **context:**
> Case 349 allowed the librarian one read of `ledger.md`: the count of its lines and the lines the yaml does not account for, named in the report. On that allowance the Criterion of `estimate-documentation-completes` and the Render of `rule-documentation` agree. But a few lines below, the same text keeps the refusal: an instruction of the handoff the frame forbids is not carried out, and the list still names "a read of `ledger.md`" with no exception; the Criterion says "to read the ledger" the same way. A handoff that asks for exactly the allowed read gets both answers. The librarian of 2046 refused for another reason: its frame is loaded at dispatch, and `librarian-guppi.md` is rendered only at step 4 of its own run; a rule page changes only at `generate`, so a change to the librarian's own frame works from the next run.
> `rule-documentation` stands `draft`, a MOC with one Estimate, `estimate-documentation-completes`, `pending`; it is touched.

> **problem:**
> The frame allows one read of the ledger and, a few lines later, orders to refuse a handoff that asks for it.

> **given:**
> The librarian's frame is the Render of `rule-documentation`, the text of `.claude/agents/librarian-guppi.md`, loaded at dispatch.
> **＋** The frame allows one read of `ledger.md`: the count of its lines and the lines the yaml does not account for, named in the report (case 349).
> **＋** An instruction of the handoff that the frame forbids is not carried out and is named in the report (case 90.3).

> **when:**
> A handoff asks the librarian to read `ledger.md`.

> **then:**
> The allowed read is carried out and named in the report, whether the handoff asked for it or not.
> **＋** An instruction to read `ledger.md` beyond that one read is refused and named in the report.
> **－** The other refusals — a repair of a yaml entry, a Spec beyond its unticked lines, a Decision page, the archive — stay.

```then
update:
  - slug: rule-documentation
    replace:
      - old: "entry, a read of `ledger.md`, a Spec beyond its unticked lines,"
        new: "entry, a read of `ledger.md` beyond the one allowed above, a Spec beyond its unticked lines,"
    change: the refusal names a read of ledger.md beyond the one allowed read (case 357)
  - slug: estimate-documentation-completes
    replace:
      - old: "or to read the ledger, a Spec beyond its `- [ ]` lines,"
        new: "or to read the ledger beyond the one read of case 349, a Spec beyond its `- [ ]` lines,"
    change: the Criterion refuses a read of the ledger beyond the one allowed (case 357)
```

```tasks
- [x] update `rule-documentation` — one `replace` pair in the Render
- [x] update `estimate-documentation-completes` — one `replace` pair inside the Criterion; the page stays `pending`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes`
```

## Case 358 — the Context of Case 347, edited after its ratification, signed after the fact

> **context:**
> Case 347 was built on the person's remark that `/carry` does not name the brief's path and the agent greps for it. At 21:49:49 a lesson in the ledger recorded that the agent took the remark as a finding and did not check it against the event log. At 21:55:09 Case 347 was ratified. Then the agent rewrote its `context` in the Spec to cite the event log instead of the remark: at 20:43:03 a grep over `.claude/agents/librarian-guppi.md`, at 20:43:05 `sed -n '77,92p'` of the same file. The librarian wrote `decision-case-347` from the edited Spec. The earlier text stands in no file: the Spec of 2046 was first committed in `8e618d1`, after the edit, so only the chat of that session held it. The edited text is checked: lines 945–946 of `vault/raw/2026-09-22/event_log.md` match in time and command; the `rule-brief` markers stand on lines 77 and 93 in commit `c1e6c36`; step 1 of `.claude/skills/carry/SKILL.md` names `vault/wiki/brief.md` in full, and step 3 commits it by name. The edit touched neither `given`, `when`, `then` nor the `then` block.
> `decision-case-347` stands `current`; `rule-carry-over` and `estimate-carry-over-writes` are not touched.

> **problem:**
> A text stands on a Decision page that nobody signed.

> **given:**
> A Decision page carries the Context, Problem, Given and When of the Spec, written by `generate` (case 52.1).
> **＋** `rule-decisions-schema` says a decision is not edited: only `status` and `superseded_by` change, both dated in History; its Render is `vault/wiki/decisions/schema.yaml`.
> **＋** An `update` with `change` alone writes one History line and changes nothing else (`Generator.update`).
> **＋** The calls the Context cites stand on lines 945–946 of `vault/raw/2026-09-22/event_log.md`.

> **when:**
> The librarian's `generate` applies this Case.

> **then:**
> The Context of `decision-case-347` stays as it stands; its History gets the line `updated: the Context rewritten after ratification to cite the event log, signed after the fact (case 358)`.
> **＋** The schema of Decisions allows one such History line: `updated:` of a Case that signs the page's text after the fact.
> **－** The Given, When, Then and the `then` block of Case 347 do not change; `rule-carry-over` and `estimate-carry-over-writes` are not touched.
> **－** The Spec of 2046 is not edited.

```then
update:
  - slug: decision-case-347
    change: the Context rewritten after ratification to cite the event log, signed after the fact (case 358)
  - slug: rule-decisions-schema
    replace:
      - old: "Only `status` and `superseded_by` ever change, and both are dated in History."
        new: "Only `status` and `superseded_by` ever change, and both are dated in History; one more History line is allowed, `updated:` of a Case that signs the page's text after the fact (case 358)."
      - old: "`- <date> created · <origin>`, `- <date> superseded by decision-case-N`."
        new: "`- <date> created · <origin>`, `- <date> superseded by decision-case-N`, and `- <date> updated: <change> · [[decision-case-N]]` of a Case that signs the text after the fact (case 358)."
    change: a Decision's History takes one updated line of a Case that signs its text after the fact (case 358)
  - slug: estimate-decisions-schema-checked
    replace:
      - old: "`examples` — the example page."
        new: "`examples` — the example page; the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact (358)."
    change: the Criterion names the updated line of a Decision's History (case 358)
```

```tasks
- [x] update `decision-case-347` — `change` alone
- [x] update `rule-decisions-schema` — two `replace` pairs in the Render
- [x] update `estimate-decisions-schema-checked` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] read `estimate-decisions-schema-checked`
```

## Case 359 — a claim no wider than its check (`insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`)

> **context:**
> Two lessons share one mechanism: a fact signed on a check narrower than the claim. The reading line of `estimate-prespec-checks-the-plan` said "72 green in the file" after one combined pytest run over three files, the per-file number split from memory; `pytest tests/test_prespec.py` alone gives 52. Case 348 was ratified on the claim that every ledger line stands in `materialize.yaml`; what was checked was the shape of the entries the agent looked at, while the yaml covers lines 1–51, 58 and 60 of 64. In both, the question put to the tool was about a sample or a shape, and the sentence signed was about a whole. Today `rule-agent-writing` asks only "Name a real source or remove the claim" — the source is named, the width of the claim is not checked.
> The Insight stands `open`, severity 2, two children; the rule stands `built`, its one Estimate `estimate-agent-writing-followed` `passed`, and it is touched.

> **problem:**
> The rule asks a claim for a source and not for a source as wide as the claim, so a narrow check signs a wide sentence.

> **given:**
> `CLAUDE.md` is loaded in every context, a subagent's too; its section `## How the agent writes` is the Render of `rule-agent-writing` (case 272.3).
> **＋** A reading line of the ledger opens with the date and the command or the place it was read (case 199).

> **when:**
> The agent writes a claim — in a Case, a reading, a ledger line, a reply.

> **then:**
> The claim is no wider than the output it rests on: a count comes from the run that printed it, and a combined run gives a combined number and nothing else.
> **＋** A claim about a whole set — every line of a ledger, every entry of a yaml — rests on a count on both sides, not on the shape of the entries read.
> **＋** Where no command covers the claim, the text says what was seen, no more.

```then
update:
  - slug: rule-agent-writing
    replace:
      - old: "Name a real source or remove the claim."
        new: "Name a real source or remove the claim. A claim is no wider than the output it rests on: a count comes from the run that printed it, and a claim about a whole set — every line, every entry — from a count on both sides; where no command covers it, write what was seen."
    change: a claim no wider than the output it rests on (case 359)
  - slug: estimate-agent-writing-followed
    replace:
      - old: "a claim names a real source or goes;"
        new: "a claim names a real source or goes, and is no wider than the output it rests on — a count from the run that printed it, a claim about a whole set from a count on both sides (359);"
    change: the Criterion names the width of a claim (case 359)
  - slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
    set: {status: actioned, addressed_by: decision-case-359}
    change: actioned by rule-agent-writing — a claim no wider than its check (case 359)
```

```tasks
- [x] update `rule-agent-writing` — one `replace` pair in the Render
- [x] update `estimate-agent-writing-followed` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — `status: actioned`, `addressed_by`
- [x] `uv run guppi render`: `CLAUDE.md`
- [ ] read `estimate-agent-writing-followed`
```

## Case 360 — one judgment, one implementation (`insight-harness-one-rule-implemented-twice-drifts`)

> **context:**
> Two lessons share one mechanism: one judgment of the pipeline was implemented in two places, and the copies drifted. `check_decision` resolved a `target_slug` against the live pages while `check_refs` resolved every other slug against live and archived pages; after 21 Estimates were archived, lint gave 25 false findings. `check_tasks` matched a reading's line by substring while `generate` ticked it by `READ_LINE`, and the four forms of a `method` were open-coded in `check_method`. Case 351 repaired these: `generate.READ_LINE`, `lint.names_a_form` and `generate.replace_once` are imported by both sides. In both, the suite stayed green, since every test was about one side.
> The vault answers that no page and no section of `CLAUDE.md` says this; the Backlog notes on reuse (case 319) speak of modules that use each other, not of one judgment written twice; `make style` is the formatter only; the slug `rule-one-judgment-one-implementation` is free. `rule-claude-md` stands `built`, a MOC with the children `rule-language` and `rule-agent-writing`; its Estimate `estimate-claude-md-rendered` stands `passed`, and its Criterion still names `vault/wiki/index.md`, gone since case 318 — the reading this Case makes due would fail on that phrase, so it is repaired here. The Insight stands `open`, severity 2.

> **problem:**
> A judgment the pipeline makes in two places can be written twice, and no text forbids it; the copies drift while the suite stays green.

> **given:**
> `CLAUDE.md` is loaded in every context, a subagent's too; `rule-claude-md` renders it whole, each child between its markers (case 272).
> **＋** `render --check` keeps the file equal to the page, and the hook refuses a hand edit.
> **＋** Case 351 lifted `generate.READ_LINE`, `lint.names_a_form` and `generate.replace_once` so that both sides import them.

> **when:**
> The agent writes code that judges a text another part of the pipeline already judges — a check beside a writer, a ticker or another check.

> **then:**
> The pattern or the predicate lives in one module, and both sides import it.
> **＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
> **＋** `CLAUDE.md` holds this text between the markers of `rule-one-judgment-one-implementation`.
> **－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

```then
create:
  - slug: rule-one-judgment-one-implementation
    type: rule
    ref: rule-claude-md
    kind: Leaf
    purpose: Prevents one judgment of the pipeline from living in two implementations that drift apart under a green suite
    enforcement: render
    governs: CLAUDE.md
    render_mode: partial
    tags: [harness, workflow, render, tests]
    sections:
      Purpose: |
        Prevents one judgment of the pipeline from living in two implementations that drift apart under a green suite. The rule cannot be checked in substance, so its guard is the one `rule-agent-writing` has: the text stands in `CLAUDE.md`, which every session and every subagent reads, `render --check` keeps it identical to this page, and the governed-files hook refuses a hand edit. It actions `insight-harness-one-rule-implemented-twice-drifts` (case 360).
      Render: |
        <!-- rule-one-judgment-one-implementation -->
        ## One judgment, one implementation

        Where code judges the same text in two places — a check and a writer, a ticker or another check — the pattern or the predicate lives in one module and both sides import it; a second copy of one judgment is a defect on the day it is written. Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
        <!-- /rule-one-judgment-one-implementation -->
  - slug: estimate-one-judgment-one-implementation-followed
    type: estimate
    ref: rule-one-judgment-one-implementation
    kind: QA
    purpose: CLAUDE.md holds the rule between its markers, and the code of a session keeps one judgment in one implementation
    method: render --check exit 0, then by hand the section in CLAUDE.md and the diff of the next Work Mode session — a judgment made in two places imported from one module, or a test over both sides
    tags: [harness, workflow, tests]
update:
  - slug: rule-claude-md
    replace:
      - old: "<!-- rule-agent-writing -->"
        new: |-
          <!-- rule-agent-writing -->

          <!-- rule-one-judgment-one-implementation -->
      - old: "with `rule-language` and `rule-agent-writing` spliced into their markers; a change to it is an `update` of one of the three. The Render holds the description of the project and the two children;"
        new: "with `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` spliced into their markers; a change to it is an `update` of one of the four. The Render holds the description of the project and the three children;"
      - old: "each child — `rule-language`, `rule-agent-writing` — splices into its marker line."
        new: "each child — `rule-language`, `rule-agent-writing`, `rule-one-judgment-one-implementation` — splices into its marker line."
      - old: "the description of the project and the two standing rules."
        new: "the description of the project and the three standing rules."
    change: the third child rule-one-judgment-one-implementation, its marker in the Render (case 360)
  - slug: estimate-claude-md-rendered
    replace:
      - old: "the children `rule-language` and `rule-agent-writing` in their markers;"
        new: "the children `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers;"
      - old: "`vault/`, its map `vault/wiki/index.md`, its terms"
        new: "`vault/`, its terms"
      - old: "then the text of `rule-language` and `rule-agent-writing` in their markers."
        new: "then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers."
      - old: "the `children` of `rule-claude-md` are `rule-language` and `rule-agent-writing`."
        new: "the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`."
    change: the Criterion names the third child and drops index.md, gone since case 318 (case 360)
  - slug: insight-harness-one-rule-implemented-twice-drifts
    set: {status: actioned, addressed_by: decision-case-360}
    change: actioned by rule-one-judgment-one-implementation (case 360)
```

```tasks
- [x] create `rule-one-judgment-one-implementation`
- [x] create `estimate-one-judgment-one-implementation-followed`
- [x] update `rule-claude-md` — four `replace` pairs; `children` is written by `generate` from the `ref` of the `create`
- [x] update `estimate-claude-md-rendered` — four `replace` pairs inside the Criterion; the page goes `pending`
- [x] update `insight-harness-one-rule-implemented-twice-drifts` — `status: actioned`, `addressed_by`
- [x] `uv run guppi render`: `CLAUDE.md`
- [ ] read `estimate-one-judgment-one-implementation-followed`
- [x] read `estimate-claude-md-rendered`
```

## Case 361 — `addressed_by` on an Insight is one link, the latest

> **context:**
> By the schema `addressed_by` is one link to the decision that fixed or rejected the pattern. A new lesson that reopens the Insight keeps the field; by case 284.4 the librarian's `update` moves the field to the decision of its own unit when that decision closed the cause. Case 332.2, later superseded, promised two decisions in `addressed_by`, and the brief warned that the move of 284.4 would cut a list of two to one link without a word. All 15 `actioned` Insights of the vault carry one link today.
> `rule-insights-schema` stands `built`, its Render `vault/wiki/insights/schema.yaml`; the live reading of that Render is `estimate-insights-schema-checked`, `passed`, and it is touched.

> **problem:**
> The schema names one link but does not say which decision it names when the pattern was closed twice, or where the earlier one goes; a Case once wrote a list there, and the move of 284.4 would drop it without a trace.

> **given:**
> `vault/wiki/insights/schema.yaml` is the Render of `rule-insights-schema`; lint takes the shape of a page from it.
> **＋** By case 284.4 the librarian's `update` sets `addressed_by` to the decision of its own unit and keeps `status`.

> **when:**
> A decision actions or rejects an Insight another decision addressed before, or two Cases of one plan touch one Insight.

> **then:**
> `addressed_by` names one decision: the latest that addressed the pattern.
> **＋** Of two Cases of one plan, only one actions the Insight; the other names it in its `context`.
> **－** A list under `addressed_by` is not a shape of the field.

```then
update:
  - slug: rule-insights-schema
    replace:
      - old: "The ratified decision that fixed the pattern, or rejected it (case 124)."
        new: "The ratified decision that fixed the pattern, or rejected it (case 124) — one, the latest; a list is not a shape of this field, and of two Cases of one plan only one actions the Insight (case 361)."
    change: addressed_by is one link, the latest; a list is not its shape (case 361)
  - slug: estimate-insights-schema-checked
    replace:
      - old: "`examples` — the example page."
        new: "`examples` — the example page; `fields.addressed_by` names one decision, the latest, and a list is not its shape (361)."
    change: the Criterion names the one link of addressed_by (case 361)
```

```tasks
- [x] update `rule-insights-schema` — one `replace` pair in the Render
- [x] update `estimate-insights-schema-checked` — one `replace` pair inside the Criterion; the page goes `pending`
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [x] read `estimate-insights-schema-checked`
```

## Case 362 — lint checks that `addressed_by` holds one link

> **context:**
> Lint takes the shape of a page from the `schema.yaml` of its category: `required`, `optional`, `values`, `conditional`. None of these keys says a field holds one link and not a list. A list under `addressed_by` passes lint without a word: the field stands in `LINK_FIELDS`, and lint checks only that each slug exists. Since 361 a list is not a shape of that field, and nothing refuses it mechanically.
> `rule-lint` stands `draft`, its classes described in the docstring of `guppi/lint.py`; its Estimate `estimate-lint-catches` stands `pending` and is touched. `rule-insights-schema` stands `built`; the live reading of its Render is `estimate-insights-schema-checked`, touched, which 361 changes too.

> **problem:**
> The shape "one link" is written in the schema in words, while lint reads keys only, so a list passes with no finding.

### Case 362.1 — lint reads `properties.single`

> **given:**
> Lint takes the shape of a page from `vault/wiki/<category>/schema.yaml`: `properties.required`, `optional`, `values`, `conditional` with its `forbidden_values`, `body.*`, and the descriptions under `fields` and `sections`; `single` is not among them.
> **＋** Seven Estimates of the schemas say in their Given that lint reads no other key.
> **＋** `tests/test_lint.py` fixes one test per class of finding.

> **when:**
> `guppi lint` reads a page whose schema holds `properties.single`.

> **then:**
> A field of `single` whose value is a list earns one `schema` finding: `<field> holds a list; one link is its shape`.
> **＋** A field of `single` with one value earns none; a field absent from the page is not checked by this key.
> **＋** The Given of the seven Estimates of the schemas names `properties.single` among the keys lint reads.
> **－** A schema without `single` is checked as today.

```then
update:
  - slug: rule-lint
    change: the class schema reads properties.single — a field holding a list where one value is its shape (case 362.1)
  - slug: estimate-lint-catches
    replace:
      - old: "a missing required field or section, a value outside the list, a conditional not met;"
        new: "a missing required field or section, a value outside the list, a conditional not met, a field of `properties.single` holding a list (362.1);"
    change: the Criterion names the finding on a single field holding a list (case 362.1)
  - slug: estimate-decisions-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-entities-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-estimates-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-insights-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-lessons-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-rules-schema-checked
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
  - slug: estimate-page-schemas-one-file-per-rule
    replace:
      - old: "`optional`, `conditional`; a missing file is a finding; other keys it does not read."
        new: "`optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read."
    change: the Given names properties.single among the keys lint reads (case 362.1)
```

```tasks
- [x] update `rule-lint` — `change` alone; the classes live in the docstring
- [x] update `estimate-lint-catches` — one `replace` pair inside the Criterion
- [x] update `estimate-decisions-schema-checked`, `estimate-entities-schema-checked`, `estimate-estimates-schema-checked`, `estimate-insights-schema-checked`, `estimate-lessons-schema-checked`, `estimate-rules-schema-checked`, `estimate-page-schemas-one-file-per-rule` — one `replace` pair each inside the Criterion; the pages go `pending`
- [x] `guppi/lint.py` — `check_schema` reads `properties.single`; the class `schema` in the docstring
- [x] `tests/test_lint.py` — a list in a `single` field a finding; one value none; a schema without the key none
- [x] read `estimate-lint-catches`
- [x] read `estimate-decisions-schema-checked`
- [x] read `estimate-entities-schema-checked`
- [x] read `estimate-estimates-schema-checked`
- [x] read `estimate-insights-schema-checked`
- [x] read `estimate-lessons-schema-checked`
- [ ] read `estimate-rules-schema-checked`
- [x] read `estimate-page-schemas-one-file-per-rule`
```

### Case 362.2 — the Insight schema lists `addressed_by` under `single`

> **given:**
> `vault/wiki/insights/schema.yaml` is the Render of `rule-insights-schema`, `render_mode: full`.
> **＋** By 362.1 lint reads `properties.single`.
> **＋** By 361 `addressed_by` is one link, the latest.

> **when:**
> `guppi lint` reads an Insight page.

> **then:**
> An Insight whose `addressed_by` is a list earns one `schema` finding.
> **＋** An Insight with one link under `addressed_by` earns none for the field.

```then
update:
  - slug: rule-insights-schema
    replace:
      - old: "optional: [addressed_by, deferred_by]"
        new: |-
          optional: [addressed_by, deferred_by]
            single: [addressed_by]
    change: addressed_by listed under properties.single (case 362.2)
  - slug: estimate-insights-schema-checked
    replace:
      - old: "values `status: open | actioned | archived`;"
        new: "values `status: open | actioned | archived`; single `addressed_by`;"
    change: the Criterion names properties.single and addressed_by under it (case 362.2)
```

```tasks
- [x] update `rule-insights-schema` — one `replace` pair in the Render
- [x] update `estimate-insights-schema-checked` — one `replace` pair inside the Criterion; the pair on the keys lint reads is 362.1's
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [x] read `estimate-insights-schema-checked`
```
