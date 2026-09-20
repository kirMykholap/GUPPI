<!-- approved 23:45:01 · session 00d3bb6a -->

# Spec — 2026-09-20, session 2106

## Case 283 — a reading of a Criterion the same session replaced

> **context:**
> At `/retro` the agent takes the readings of this session's Estimates whose work is finished and writes their lines into the ledger. The librarian applies the yaml in ledger order: an `update` of an Estimate replaces its Criterion whole and sets `pending`, an `estimate[...]` line sets the status and overwrites the Result; `built` on a Rule is computed once every Estimate of it is `passed`. In session 1749 Case 282 replaced the Criterion of `estimate-retro-loads` and left the render to the librarian; the `/retro` of the same session read the old Criterion of 270.3 — the SKILL that was rendered — for the `read` line of the 1308 Spec and wrote `passed`. `generate` applied the `update` first, then the reading: the page carries the Criterion of 282, the Result of 270.3 and `passed`; `rule-retro` became `built` on it. By the order of the ledger lines the reading stands after 282, and the rule of 280 ticked the line of 282, not 1308:132 — the reading of `estimate-generate-ticks-the-spec` in this session found 280 followed as written.
> Bookkeeping: `rule-retro` `built`, its one Estimate `estimate-retro-loads` `passed`; the Case touches this Estimate; the vault not asked — an `update` with a `ref`; `generate` and the rule of 280 do not change.

> **problem:**
> A reading of a Criterion the same session has already replaced lands on the page, sets `passed` on a promise nobody measured, and computes `built` on the Rule. Neither the ledger line nor `generate` can tell it from the normal course — an `update` ratified, built and read in one session — by order or by form. No text says which Criterion a reading measures.

> **given:**
> Retro takes the readings of this session's Estimates whose work is finished and writes their lines; `generate` applies the entries of the yaml in ledger order — an `estimate` entry sets `status` and overwrites the Result (case 53.2); `built` is computed once every Estimate is `passed`.
> **＋** An `update` of an Estimate replaces its Criterion whole and sets `pending`; the render of a Rule comes with the librarian, after Retro.
> **＋** `estimate-retro-loads` is read by hand at the first `/retro` after the render.

> **when:**
> The person invokes `/retro`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
> **＋** An Estimate whose Criterion a Case of this session replaced, and whose build is not finished at Retro, gets no reading in this session: the `read` line of the old Criterion in an earlier Spec is not debt and is not read; the reading of the new Criterion closes it, at the moment its `method` names; the handoff names the Estimate as one whose reading cannot be taken yet.
> **－** Nothing in `generate` changes: an `update` and a reading of one slug in one session apply in ledger order, and the reading of a Criterion built in the session sets its status.
> **－** Nothing else in Retro changes.

```then
update:
  - slug: rule-retro
    replace:
      - old: "name in the handoff any Estimate whose reading cannot be taken yet."
        new: "name in the handoff any Estimate whose reading cannot be taken yet. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built; an Estimate whose Criterion a Case of this session replaced and whose build is not finished at Retro has no reading in this session — the `read` line of the old Criterion in an earlier Spec is not debt and is not read, the reading of the new Criterion closes it at the moment its `method` names (case 283)."
    change: a reading measures the last ratified Criterion; an Estimate whose Criterion this session replaced and whose build is not finished has no reading at this Retro (case 283)
  - slug: estimate-retro-loads
    set: {status: pending}
    change: the Criterion replaced whole — a replaced Criterion is not read at the Retro of its session; the reading of 270.3 written after 282 undone by this pending (case 283)
```

```tasks
- [ ] update `rule-retro`: `replace` in the Render — the sentence on a replaced Criterion after "name in the handoff any Estimate whose reading cannot be taken yet"
- [ ] update `estimate-retro-loads`: the Criterion replaced whole, `pending`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads`: the first `/retro` after the render, by hand — the next session, by the rule of this Case
```

## Case 284 — `insight-session-vault-knowledge-not-loaded` reopened for a cause the same session closed

> **context:**
> The Insight holds one pattern: a fact the vault holds does not reach the session that needs it — only `brief.md`, `CLAUDE.md`, the skills and the agent frames are loaded, the rest waits for a read the agent must first think to make. Case 134 set it `actioned`: the ledger tail at `/hi` (101.2) closed the first child, the bash guard (127) the four heredoc children; the second half of the Proposal — a list of lessons on a Rule page — was rejected: a text to remember is the channel that failed. The librarian of session 1749 added a sixth child, `lesson-spec-render-line-form-unmatched-by-the-ticker`: the form of a `render` line stood in `rule-render-harness` and in no text the Spec is written from; the Insight went back to `open`, severity 1. The same session had already answered mechanically: 279.1 wrote the form of the `render` and `sprint` lines into the Case schema, the text `/hi` loads; 279.2 gave pre-spec a refusal of a line of another form. Both are built, `rule-prespec` `built`; the reading of the schema at this session's `/hi` found the form in place. The steps: the agent writes the `lesson[...]` line the moment the lesson exists (ledger line 8 of 1749), the fixes are ratified after it (lines 9–12) — and neither line knows of the other; `materialize` carries them apart; `rule-synthesis` tells the librarian, on an Insight of the same pattern, to append the `update` with `set: {status: open}` when it was `actioned` — it looks back at the pattern, never sideways at the decisions of the same yaml; `generate` applies it, the brief lists the `open` Insight under Deferred, `/hi` makes it a Frontier item, and a Case is spent on a fact the yaml already held.
> Bookkeeping: the Insight `open`, `addressed_by: decision-case-134`, five children archived, one live; the vault not asked — every page an `update` with a `ref`, the two Estimates named in the Case; `rule-case-protocol` `draft` (`estimate-case-protocol-loaded` read `passed` this session, not yet applied), `rule-materialize` `built`, `rule-synthesis` `built`; the Case touches `estimate-case-protocol-ledger-line-form` and creates two Estimates; the lesson of case 283 (`lesson-retro-reading-of-a-replaced-criterion`) is a contract gap by its root cause, not a fact of the vault unloaded — clustering is the librarian's.

> **problem:**
> The Insight stands `open` with one live child whose cause was closed in the session that bore it, and the model has no way to say so: closing an Insight is a ratified decision, reopening is mechanical, and the record holds no link from a lesson to the decision that closed its cause. Each such recurrence costs a Case for a fact already in the yaml.

### Case 284.1 — the Insight `actioned` by 279.1 and 279.2

> **given:**
> `insights/schema.md`: `actioned` when a ratified decision closed the pattern; `addressed_by` is one decision slug, the one that fixed or rejected it; not an end state — a new Lesson with the same root cause returns `open`, the old children stay archived.
> **＋** The cascade of `generate` (104.2): the children of an `actioned` Insight go `archived`, `cleanup` moves the pages, `severity` is recomputed over the live children; an `actioned` Insight is not archived by the cascade.
> **＋** `rule-case-protocol` by 279.1 carries the form of the `render` and `sprint` lines in the Spec paragraph; `rule-prespec` by 279.2 refuses a line of another form; `estimate-prespec-catches-a-command-line-off-form` `passed`.
> **－** An Insight has no Estimate; `generate` accepts its `update`, not a `create` or a `delete` (124.2).

> **when:**
> `guppi generate` applies the `update` of this Case.

> **then:**
> `insight-session-vault-knowledge-not-loaded` — `status: actioned`, `addressed_by: decision-case-284.1`; the Decision page says the sixth child was closed by 279.1 and 279.2.
> **＋** The cascade archives `lesson-spec-render-line-form-unmatched-by-the-ticker`, `cleanup` moves it; `severity` counts 0 live children.
> **＋** A new Lesson with the same root cause returns the Insight to `open`, as today.
> **－** Nothing else — neither the schema nor the page's Proposal — changes.

```then
update:
  - slug: insight-session-vault-knowledge-not-loaded
    set: {status: actioned, addressed_by: decision-case-284.1}
    change: "actioned: the sixth child, the form of a render line, closed in its own session by 279.1 (the form in the schema /hi loads) and 279.2 (pre-spec refuses a line of another form); the Proposal's first half done by 101.2, its second rejected by 134 (case 284.1)"
```

```tasks
- [ ] update `insight-session-vault-knowledge-not-loaded`: `set: {status: actioned, addressed_by: decision-case-284.1}` — generate writes the field as a wikilink
```

### Case 284.2 — the mark `{addresses:<lesson slug>}` on a decision line

> **given:**
> A decision line is markup: `- decision[case N][kind][slug]{ref:...}{tags:...}`, `{supersedes:case N}` when it applies (case 75.1); the Case schema is the Render of `rule-case-protocol`, and §4 of `index.md` is the second copy of the line's form.
> **＋** A lesson line is written the moment the lesson exists — before the ratification of its fix.

> **when:**
> `/hi` loads the schema; someone reads `case-schema.md` or `index.md` §4; the agent writes the `decision[...]` lines in the reply that acknowledges a ratification.

> **then:**
> The ledger paragraph of the schema and §4 of the map say: a decision line whose Case closes the root cause of a lesson of this session carries `{addresses:<lesson slug>}`, written when the lesson line already stands in the session's ledger, one mark per lesson — two lessons, two marks.
> **＋** The agent writes the line so, and the mark stands in the preview of the ledger lines the person ratifies.
> **－** The lesson line does not change: no `{addressed_by}` on it; the estimate row and the lesson row of the table do not change.
> **－** A lesson whose fix is ratified in another session gets no mark — the Insight is open by then, and a Case is due, as today.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1)."
        new: "`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1); `{addresses:<lesson slug>}` stands on a decision line whose Case closes the root cause of a lesson of this session — written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson whose fix is ratified in another session gets no mark (case 284.2)."
    change: the mark {addresses:<lesson slug>} on a decision line whose Case closes the root cause of a lesson of this session (case 284.2)
  - slug: estimate-case-protocol-ledger-line-form
    set: {status: pending}
    change: the Criterion replaced whole — the mark {addresses:<lesson slug>} beside {source} and {supersedes} (case 284.2)
  - slug: index
    file: vault/wiki/index.md
    change: "§4, the list under the decision line: `addresses` — optional, the slug of a lesson of this session whose root cause the Case closes; carried by materialize to the lesson's entry (case 284.2)"
```

```tasks
- [ ] update `rule-case-protocol`: `replace` in the Render — the sentence on `{source}` and `{supersedes}` gains `{addresses:<lesson slug>}`
- [ ] update `estimate-case-protocol-ledger-line-form`: the Criterion replaced whole, `pending`
- [x] update `index.md` §4 by hand: the `addresses` item under the decision line
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-ledger-line-form`: `case-schema.md` and `index.md` §4 after the render, by hand
```

### Case 284.3 — materialize carries the mark to the lesson's entry

> **given:**
> `materialize` lifts `source`, `supersedes` and `tags` from the braces of a line and ignores the other keys; `superseded_by` it sets on the entries of Case N from a later `{supersedes}` of any unit.
> **＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger.

> **when:**
> `guppi materialize` assembles the yaml of a unit.

> **then:**
> A decision entry carries `addresses: [<slug>, …]`; the lesson entry of that slug in the same unit carries `addressed_by: decision-case-N` at the entry's level, not among the page's fields — the lesson page gets no field.
> **－** A mark naming a lesson not in the unit is `incomplete: [addresses]` on the decision entry, not an error.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "a mapping or a scalar under it is `incomplete: [reword]` (case 274.3)."
        new: "a mapping or a scalar under it is `incomplete: [reword]` (case 274.3). A decision line's `{addresses:<lesson slug>}` is carried to the entry as `addresses`, a list, and the lesson entry of that slug in the same unit gets `addressed_by: decision-case-N` at the entry's level, never as a page field; a mark whose lesson is not in the unit is `incomplete: [addresses]` on the decision entry (case 284.3)."
    change: the mark addresses on a decision line reaches the lesson's entry as addressed_by (case 284.3)
create:
  - slug: estimate-materialize-carries-addresses
    type: estimate
    ref: rule-materialize
    kind: QA
    purpose: A decision line's {addresses:<lesson slug>} lands on the lesson's entry as addressed_by, at the entry's level; a mark without its lesson is incomplete
    method: pytest tests/test_materialize.py on a temp ledger; the live reading the librarian's run on the first marked lesson
    tags: [harness, workflow, ledger]
```

```tasks
- [x] `guppi/materialize.py`: the key `addresses` lifted from the braces, the join onto the lesson entry of the unit, `incomplete: [addresses]` without a pair
- [x] `tests/test_materialize.py`: the mark reaches the lesson entry; a mark without its lesson is `incomplete`; the lesson page's fields untouched
- [x] `guppi/materialize.py` docstring: `addresses` and `addressed_by` in the field list, each with its writer — the list `estimate-materialize-fails-alone` reads stays complete
- [ ] update `rule-materialize`: `replace` in the Purpose — the sentence on the mark
- [ ] create `estimate-materialize-carries-addresses`, `ref: rule-materialize`
- [ ] read `estimate-materialize-carries-addresses`: pytest; live — the librarian's run on the first marked lesson
```

### Case 284.4 — synthesis keeps an `actioned` Insight by the mark

> **given:**
> `rule-synthesis`: on an Insight of the same pattern the librarian appends an `update` with `children` plus the lesson and `set: {status: open}` when it was `actioned`; the entries it adds carry `librarian: synthesis`.
> **＋** `insights/schema.md`: `addressed_by` is one decision; the cascade of `generate` archives the children of an `actioned` Insight.
> **＋** The lesson entry carries `addressed_by: decision-case-N` when a decision line of the unit marked it (284.3).
> **－** An `open` Insight stays as today; the librarian never sets `actioned` himself.

> **when:**
> The librarian, at synthesis, finds an Insight of the same pattern, it is `actioned`, and the lesson entry carries `addressed_by`.

> **then:**
> The `update` of the Insight carries `children` plus the lesson and `set: {addressed_by: decision-case-N}` — the bare slug, `generate` writes the wikilink — with `status` kept `actioned`; the lesson is `clustered` with `insight` set, the cascade archives it; the brief reports the pair beside the synthesis, as it reports a clustering.
> **＋** Without `addressed_by` — `set: {status: open}`, as today.
> **＋** The schema of Insights, §8 of the map and the glossary name the exception: a new Lesson reopens `actioned` unless its entry carries `addressed_by`.

```then
update:
  - slug: rule-synthesis
    replace:
      - old: "the new lesson, and `set: {status: open}` when it was `actioned`; and an `update`"
        new: "the new lesson, and — when it was `actioned` — `set: {status: open}`, or `set: {addressed_by: decision-case-N}` with `status` kept when the lesson entry carries `addressed_by: decision-case-N`, the Case of this unit that closed its cause, the pair reported in the brief beside the synthesis (case 284.4); and an `update`"
    change: an actioned Insight stays actioned when the lesson entry carries addressed_by from a decision of the same unit; addressed_by moves to that decision (case 284.4)
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: "the `status` row and the Reopening section: a new Lesson reopens `actioned` unless its entry carries `addressed_by` — a decision of its own session closed its cause; then the Insight stays `actioned`, `addressed_by` moves to that decision and the Lesson is archived with the other children (case 284.4)"
  - slug: index
    file: vault/wiki/index.md
    change: "§8, the sentence `actioned` is not terminal: a new matching Lesson reopens it — unless its entry carries `addressed_by`, a decision of its own session that closed its cause; then `addressed_by` moves and the Insight stays `actioned` (case 284.4)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the Status models row of Decision, Lesson, Insight: a new Lesson reopens `actioned`, unless a decision of its own session closed its cause (case 284.4)"
create:
  - slug: estimate-synthesis-keeps-actioned-by-the-mark
    type: estimate
    ref: rule-synthesis
    kind: QA
    purpose: An actioned Insight of the same pattern stays actioned when the new lesson's entry carries addressed_by, and its addressed_by moves to that decision
    method: one reading by hand of the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight; no date
    tags: [harness, workflow, librarian]
```

```tasks
- [ ] update `rule-synthesis`: `replace` in the Render — the branch on `addressed_by`
- [x] update `insights/schema.md` by hand: the `status` row and the Reopening section
- [x] update `index.md` §8 by hand: the exception to the reopening
- [x] update `glossary.md` by hand: the Status models row
- [ ] create `estimate-synthesis-keeps-actioned-by-the-mark`, `ref: rule-synthesis`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-synthesis-keeps-actioned-by-the-mark`: the librarian's run on the first marked lesson under an actioned Insight, by hand; no date
```

## Deferred

## Case 285 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads` on a check that reads a page the same Spec changes; `rule-subagent-guppi` — what a subagent may do in Work Mode and the fork that comes back to the main agent as a Case. Both are `draft` placeholders, deferred thirteen times, the last by 281. This session spent its Plan Mode on two readings and Cases 283–284: the reading of a replaced Criterion at Retro, and the mark `{addresses}` that keeps an Insight `actioned` when its session closed the cause.

> **problem:**
> The person closes this Plan Mode with Cases 283 and 284 and goes to pre-spec; Slice 3b waits for the next session, the fourteenth defer. Two lines of this session bear on it: a reading at Retro measures the last ratified Criterion (283), and a decision line may name the lesson it closes (284.2) — Work Mode is written with both.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks, the test of each Estimate first and turned green; the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case
```
