<!-- approved 17:31:55 · session 131b9375 -->

# Spec — 2026-09-21, session 1315

## Case 291 — an `update` of an Estimate names the part it changes; a part not named is the whole Criterion

> **context:**
> `materialize` assembles one entry per ledger line. For an `update` of an Estimate, `lift_criterion` in `guppi/materialize.py` always puts `sections.Criterion` on the entry — the `given`, `when` and `then` of the Case — and sets `set.status: pending`, unless the item wrote a Criterion or a status itself. That is right for a change of the promise: the Case schema says such an `update` carries `set: {status: pending}` and `change`, and the Criterion is replaced whole (cases 204, 211). But an `update` that sets one field takes the same path: 290.3 set `purpose` on two Estimates, and the Criterion of 286 on `estimate-generate-ticks-the-spec` and of 288.1 on `estimate-internal-context-loaded` were replaced by the text of 290.3, whose own `then` said the Criterion does not change. Neither pre-spec nor the librarian caught it. The first case of the same root cause is `lesson-estimate-update-must-carry-its-criterion-whole` (session 0958); the second is the lesson of this session.
> The pages: `rule-materialize` `draft` (`estimate-materialize-carries-addresses` pending), an `update` with a `ref`, no vault query; of the ten Estimates of the rule the Case touches one, `estimate-materialize-assembles` (`passed`; its line "`set: {status: pending}` unless the item set a status itself" is the promise), the other nine not. `rule-case-protocol` is not touched: the schema already says only a replaced Criterion sets `pending`, and the `update` form of a promise change already carries `set: {status: pending}` — that is the signal.

> **problem:**
> The script knows one kind of `update` of an Estimate — the change of the promise — and replaces the signed Criterion on every `update`. The two Criteria signed in 286 and 288.1 do not stand on their pages; the reading of `estimate-internal-context-loaded` has nowhere to land.

### Case 291.1 — the item names the part; a part not named is the whole Criterion

> **given:**
> An `update` of an Estimate that changes the promise carries `set: {status: pending}` and `change`; the Criterion is replaced whole — by the text of the Case or by the text written under `sections: Criterion` (cases 204, 211); only a replaced Criterion sets `pending`.
> **＋** The `then` block is what is signed; its keys `set`, `replace` and `sections` name a part of the page; the decision line of the ledger is markup only.
> **＋** `lift_criterion` in `guppi/materialize.py` runs on every `create` and `update` entry of the category `estimates`; `generate` applies `sections` whole, `set` as fields, `replace` as pairs.
> **＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger.
> **－** `generate` and pre-spec do not change.

> **when:**
> `guppi materialize` assembles the entry of an `update` of an Estimate.

> **then:**
> An item that names no part — `change` alone — or names `status`: the whole replacement, as today — a written `sections.Criterion` stands, else the `given`, `when` and `then` of its Case are lifted; `set.status` `pending` unless the item set a status itself.
> **＋** An item that names a part — `set` without `status`, `replace`, `sections` without `Criterion` — and writes no `sections.Criterion`: that part alone changes; nothing is lifted, no status is set, the Criterion of the page stands.
> **＋** An item with `sections.Criterion` and any other part: the written Criterion, the part as named, `pending` unless a status is set.
> **－** A `create` of an Estimate does not change: its Criterion is always written or lifted, else `incomplete: [criterion]`.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204)."
        new: "a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204). An `update` item names the part it changes: one that names a part — `set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes that part alone, nothing lifted and no status set; one that names no part, or names `status`, replaces the Criterion whole (case 291.1)."
    change: an update item of an Estimate that names a part changes that part alone; a part not named is the whole Criterion (case 291.1)
  - slug: estimate-materialize-assembles
    set: {status: pending}
    change: one line of the Criterion — an update item that names a part of the page keeps the Criterion and the status; one that names none, or names status, replaces the Criterion whole (case 291.1)
    sections:
      Criterion: |
        Given:
        A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
        **＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements, `replace` and `reword` as pairs, and writes every field of a `create` entry's `fields` into the frontmatter.
        **＋** The `schema.yaml` of each category lists the fields of its page: `required` and `optional` (case 214).
        **＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

        When:
        `guppi materialize` lifts a record line of a ledger against its Spec.

        Then:
        One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented (case 258.3).
        **＋** `reword` is a list of `{old, new}` pairs, carried as written; a mapping or a scalar under `reword` is `incomplete: [reword]` (case 274.3).
        **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` entry, and of a `defer` entry but for `type` and `purpose` — the defer's own keys, which reach `fields` whatever the target's category, for the placeholder page and for the `## Deferred` of the Decision page; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before, and a `defer` without `purpose` is `incomplete: [purpose]` (cases 214.1, 266).
        **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
        **＋** An `update` entry for an Estimate that names no part of the page — `change` alone — or names `status` carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own. One that names a part — `set` without `status`, `replace`, `sections` without `Criterion` — and writes no Criterion carries that part alone: nothing lifted, no status set (case 291.1).
        **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
        **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
        **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
        **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
        **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
        **－** A line the grammar does not parse goes under `unparsed`; the run goes on.
```

```tasks
- [ ] update `rule-materialize`: `replace` in the Purpose — the item names the part, a part not named is the whole Criterion
- [ ] update `estimate-materialize-assembles`: the Criterion whole under `sections`, one line changed, `pending`
- [ ] `guppi/materialize.py`: `lift_criterion` — the branch "a part is named"; the docstring
- [ ] `tests/test_materialize.py`: new tests — `set: {purpose}` alone: no `sections`, no `set.status`; one `replace` pair alone: the same; `set: {purpose, status: pending}`: lifted and the field; the test of Case 17 (`change` alone) stands as it is
- [ ] read `estimate-materialize-assembles`: pytest now; live — the librarian's run of this session, by `--show`
```

### Case 291.2 — the two Criteria restored from Spec 0019

> **given:**
> Spec 0019 holds the signed `given`, `when` and `then` of Case 286 (lines 14–36) and of 288.1 (lines 172–184); the pages `estimate-generate-ticks-the-spec` and `estimate-internal-context-loaded` carry the text of 290.3, both `pending`.
> **＋** An item with `sections: Criterion` stands as written (case 204); the History of a page keeps both replacements.

> **when:**
> `guppi generate` applies the entries of this Case.

> **then:**
> The Criterion of `estimate-generate-ticks-the-spec` is the text of 286 verbatim; the Criterion of `estimate-internal-context-loaded` the text of 288.1 verbatim; both `pending`, one History line each.
> **－** The `purpose` of both pages (290.3) does not change.

```then
update:
  - slug: estimate-generate-ticks-the-spec
    set: {status: pending}
    change: the Criterion of 286 restored whole, replaced by the purpose update of 290.3 (case 291.2)
    sections:
      Criterion: |
        Given:
        A yaml entry of kind `estimate` carries `slug`, `status`, `result`, `line` and no `case`; a decision entry carries `case` and `line`, the number of its line in the ledger.
        **＋** A line `{supersedes:case N}` marks every entry of Case N `superseded_by`, in the yaml of any session under `raw/` (130.2, 175); `generate` neither applies them nor ticks their page lines (151, 200.2).
        **＋** The lines of a superseded Case are not counted at Retro — its work stands under the superseding Case (282).
        **＋** The Spec of a session lies beside its `materialize.yaml` — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
        **＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
        **＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
        **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec with a yaml of its own in another session folder.
        **－** A Rule-class file entry `generate` does not apply — "applied by hand".

        When:
        `guppi generate` applied an entry and marked it `applied`.

        Then:
        For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
        **＋** Two entries of one kind and slug in one Case tick two lines, in order.
        **＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
        **＋** In the Spec beside the yaml, a `read` line in the section of a Case whose first decision entry of the yaml carries a `line` greater than the `line` of the `estimate` entry is not the reading's line — the Case was ratified after it; the search goes on to the next line, then to the other sessions.
        **＋** In any Spec, a `read` line in the section of a Case whose entries in the yaml of that session are marked `superseded_by` is not the reading's line — its work stands under the superseding Case; the search goes on. For the Spec beside the yaml the marks are the run's entries; for the Spec of another session its `materialize.yaml` beside it, read for the marks alone; no yaml beside it — nothing is skipped there.
        **＋** A `create` entry with `folded` ticks both lines: the page line and the reading line; its Case is the reading's Case, the filter of 280 does not apply to it; the filter by `superseded_by` does.
        **－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
        **－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
        **－** A Spec under `vault/archive/` is not read; the Specs of the other sessions are not filtered by `line`.
  - slug: estimate-internal-context-loaded
    set: {status: pending}
    change: the Criterion of 288.1 restored whole, replaced by the purpose update of 290.3 (case 291.2)
    sections:
      Criterion: |
        Given:
        The `/hi` skill is the Render of `rule-skill-hi` with its children in markers; `rule-internal-context` is the block of `@` lines Claude Code expands when the skill is invoked.
        **＋** A subagent receives the `CLAUDE.md` hierarchy and not the content of an invoked skill (Claude Code docs, sub-agents).
        **＋** `guppi recall` prints the `@` lines of the skill file after a compaction (287).
        **＋** `guppi render --check` keeps the skill file equal to the page.

        When:
        The person invokes `/hi`.

        Then:
        The text of `sprint.md`, `brief.md`, `case-schema.md` and `glossary.md` is present in the first turn's context, in that order, without a read call.
        **＋** The glossary reaches a session through this block alone; after a compaction its path is in the list of `guppi recall`.
        **－** A subagent — `librarian-guppi`, `ask-guppi`, one of Work Mode — carries no glossary; its prompt names what it needs.
```

```tasks
- [x] update `estimate-generate-ticks-the-spec`: the Criterion of 286 under `sections: Criterion`, `pending`; its read line stands in Spec 0019 line 56
- [x] update `estimate-internal-context-loaded`: the Criterion of 288.1 under `sections: Criterion`, `pending`; its read line stands in Spec 0019 line 214 — the reading in this session after the ratification, by hand, on the facts of this `/hi`
```

## Case 294 — the Case schema names the field-only `update` of an Estimate

> **context:**
> `case-schema.md` describes one form of an `update` of an Estimate: "carries `slug`, `set: {status: pending}` and `change`… the scripts replace its Criterion". After 296 there is a second form — the item names a part, the Criterion and the status stand unless the Criterion is touched — and an agent reading the schema at `/hi` does not learn it: the same two texts that led to 290.3. Case 291 proposed to leave the schema alone so that `estimate-case-protocol-loaded` would not go `pending`; pre-spec showed the cost of the silence. The pages: `rule-case-protocol` `draft`; of its Estimates the Case touches `estimate-case-protocol-loaded` (its reading `passed` in this session's ledger; the page `pending` until the librarian applies it), not `estimate-case-protocol-ledger-line-form`; an `update` with a `ref`.

> **problem:**
> The schema says every `update` of an Estimate carries `set: {status: pending}`; the mechanism of 296 tells two forms apart. Either the schema says both, or the agent learns the second from `rule-materialize` alone.

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`; an `update` of the Render touches the Estimate of the live reading of that Render (187); `render --check` keeps the file equal to the page.
> **＋** 296: an item that names a part changes that part alone; a part inside the Criterion, or a written `sections: Criterion`, sets `pending`; an item that names no part, or `status`, replaces the Criterion whole.

> **when:**
> The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

> **then:**
> The Spec paragraph of the schema, after the sentence on `set.method` and "(case 204)", says: an `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`; the scripts change that part, and the Criterion and the status stand unless the part is inside the Criterion, which sets `pending` (296).
> **＋** The rest of the schema does not change; `render --check` after the render exits 0.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "or keep the text the item wrote under `sections: Criterion` (case 204). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split."
        new: "or keep the text the item wrote under `sections: Criterion` (case 204). An `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`: the scripts change that part, and the Criterion and the status stand, unless the part is inside the Criterion, which sets `pending` (case 296). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split."
    change: the Spec paragraph names the field-only update of an Estimate — a part named changes alone, a part inside the Criterion sets pending (case 294)
  - slug: estimate-case-protocol-loaded
    set: {status: pending}
    change: one line of the Criterion — the Spec paragraph names the field-only update of an Estimate (case 294)
    sections:
      Criterion: |
        Given:
        `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the hook refuses a hand edit.
        **＋** The one rule stood as the first paragraph of `CLAUDE.md` until this Case (59.8, 272.1).
        **＋** `guppi render --check` keeps the file equal to the page.

        When:
        The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

        Then:
        `case-schema.md` opens with the section "The one rule" right under its title: nothing in the vault or the codebase changes without a Decision ratified by the human; the agent has full autonomy over how to implement something once its contract is ratified, and none over the contract itself; when unsure whether something needs ratification, it does; the vault is the only memory — no note outside the repository, what is worth keeping is a `lesson` line or a Case on a Rule page (272.1).
        **＋** The paragraph after it says, as before, that the schema is the Render loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, and that a session without `/hi` holds no Case.
        **＋** The Spec paragraph names the field-only `update` of an Estimate: a part named changes alone, a part inside the Criterion sets `pending` (294, 296).
        **＋** `render --check` after the render exits 0.
        **－** The other sections of the schema do not change; the description of the project is not in the schema.
```

```tasks
- [x] update `rule-case-protocol`: `replace` in the Render — one sentence after "(case 204)."
- [x] update `estimate-case-protocol-loaded`: the Criterion whole under `sections`, one line added to Then, `pending`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-loaded`: `render --check` after the render; the `/hi` of the next session, by hand
```

## Case 295 — three `given` lines of `rule-page-generation`'s Estimates: an `update` entry "carries both" — no longer always

> **context:**
> `estimate-generate-cascades`, `estimate-generate-writes-the-decision-page` and `estimate-generate-fails-alone` hold one and the same `given` line: "An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`". After 296 an entry of one field carries neither. Their `then` do not depend on the line — `generate` applies what the entry carries — but the line becomes false. Three pages `passed`; `rule-page-generation` `draft`; an `update` with a `ref` each. Before 296 the fix meant three whole Criteria (lesson 0958); after it, three `replace` pairs — the first live use of the rule, and the live reading of `estimate-materialize-assembles`. The pairs sit in `given`, inside the Criterion: the three pages go `pending`, one `pytest tests/test_generate.py` reads all three.

> **problem:**
> Three `given` lines describe a form of the entry that is no longer the only one.

> **given:**
> 296 is built: a `replace` pair whose `old` sits inside `## Criterion` yields `set: {status: pending}` and lifts nothing.
> **＋** `generate` applies the pairs in the body; the `old` stands once on each of the three pages.

> **when:**
> `guppi materialize` assembles the entries of this Case, then `guppi generate` applies them.

> **then:**
> The yaml holds three `update` entries with `replace`, `change` and `set: {status: pending}`, no `sections`.
> **＋** On each page the `given` line reads: "An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries…"; the rest of the Criterion stands; `status: pending`; one History line.

```then
update:
  - slug: estimate-generate-cascades
    replace:
      - old: "An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
        new: "An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
    change: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295)
  - slug: estimate-generate-writes-the-decision-page
    replace:
      - old: "An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
        new: "An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
    change: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295)
  - slug: estimate-generate-fails-alone
    replace:
      - old: "An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
        new: "An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1)."
    change: one given line — an update entry of an Estimate carries the Criterion and pending when it replaces the promise, not always (case 295)
```

```tasks
- [x] update `estimate-generate-cascades`: one `replace` pair in the Criterion, `pending` by the script
- [x] update `estimate-generate-writes-the-decision-page`: one `replace` pair in the Criterion, `pending` by the script
- [x] update `estimate-generate-fails-alone`: one `replace` pair in the Criterion, `pending` by the script
- [x] by hand, at Retro: `uv run guppi materialize --show` — the three entries of 295 carry `replace` and `set: {status: pending}`, no `sections`; else no handoff
- [ ] read `estimate-generate-cascades`: `pytest tests/test_generate.py` at the librarian's run of this session or the next `/hi`
- [ ] read `estimate-generate-writes-the-decision-page`: the same run
- [ ] read `estimate-generate-fails-alone`: the same run
```

## Case 296 — the item names the part; a touched Criterion sets `pending` (supersedes 291.1)

> **context:**
> As in 291: `lift_criterion` puts the `given`, `when` and `then` of the Case on every `update` entry of an Estimate and sets `pending` — 290.3 replaced two signed Criteria with one `set: {purpose}`. 291.1 tied the status to whether a part was named; that is a hole — a `replace` pair inside the Criterion changes the promise while the status stands, and a pair cannot set the status honestly, since `status` named means the whole replacement. The pages as in 291: `rule-materialize` `draft`, of its ten Estimates the Case touches `estimate-materialize-assembles` (`passed`, line 30 the promise); an `update` with a `ref`. The `replace` in the Purpose of `rule-materialize` has the `old` of 291.1, which was never applied.

> **problem:**
> Two questions were glued into one sign. *What* changes is decided by the part named. *Whether the status is reset* must be decided by whether the Criterion was touched; today neither the script nor 291.1 tells them apart.

> **given:**
> An `update` of an Estimate that changes the promise carries `set: {status: pending}` and `change`; the Criterion is the text of the Case or the text written under `sections: Criterion` (cases 204, 211); only a replaced Criterion sets `pending` (187).
> **＋** The `then` block is what is signed; `set`, `replace` and `sections` name a part of the page; the decision line of the ledger is markup only.
> **＋** `lift_criterion` in `guppi/materialize.py` runs on every `create` and `update` entry of the category `estimates`; `materialize` reads the pages of `wiki/` while it assembles; `generate` applies `sections` whole, `set` as fields, `replace` as pairs, and refuses a pair whose `old` does not stand once on the page.
> **＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger and a temp vault.
> **－** `generate` and pre-spec do not change.

> **when:**
> `guppi materialize` assembles the entry of an `update` of an Estimate.

> **then:**
> An item that names no part — `change` alone — or carries `set.status`: the whole replacement, as today — a written `sections.Criterion` stands, else the `given`, `when` and `then` of its Case are lifted; `set.status` `pending` unless the item set a status itself.
> **＋** An item that names a part — `set` without `status`, `replace`, `sections` without `Criterion` — and writes no `sections.Criterion`: that part alone changes; nothing is lifted.
> **＋** The Criterion touched — the `old` of at least one `replace` pair stands in the `## Criterion` of the page on disk, or the item wrote `sections.Criterion` — the entry gets `set: {status: pending}` unless the item set a status itself.
> **＋** The Criterion not touched — `set` of fields, a pair outside `## Criterion` — no status is set; the entry carries `set`, `replace` and `change` as written.
> **－** An `old` absent from the page `materialize` does not judge — the entry carries no status, `generate` refuses the pair as today; no page on disk — nothing is read, the entry as named, pre-spec catches an `update` of an Estimate that does not exist.
> **－** A `create` of an Estimate does not change: its Criterion is always written or lifted, else `incomplete: [criterion]`.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204)."
        new: "a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204). An `update` item names the part it changes: one that names a part — `set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes that part alone, nothing lifted; it is set `pending` when the part is inside the Criterion — the `old` of a `replace` pair stands in the page's `## Criterion` — and left as it is otherwise; a written `sections.Criterion` beside any other part stands and sets `pending`; one that names no part, or carries `set.status`, replaces the Criterion whole (case 296)."
    change: an update item of an Estimate that names a part changes that part alone; a part inside the Criterion sets pending; a part not named is the whole Criterion (case 296)
  - slug: estimate-materialize-assembles
    set: {status: pending}
    change: one line of the Criterion — an update item that names a part of the page changes that part alone, pending when the part is inside the Criterion; one that names none, or carries set.status, replaces the Criterion whole (case 296)
    sections:
      Criterion: |
        Given:
        A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
        **＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements, `replace` and `reword` as pairs, and writes every field of a `create` entry's `fields` into the frontmatter.
        **＋** The `schema.yaml` of each category lists the fields of its page: `required` and `optional` (case 214).
        **＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

        When:
        `guppi materialize` lifts a record line of a ledger against its Spec.

        Then:
        One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented (case 258.3).
        **＋** `reword` is a list of `{old, new}` pairs, carried as written; a mapping or a scalar under `reword` is `incomplete: [reword]` (case 274.3).
        **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` entry, and of a `defer` entry but for `type` and `purpose` — the defer's own keys, which reach `fields` whatever the target's category, for the placeholder page and for the `## Deferred` of the Decision page; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before, and a `defer` without `purpose` is `incomplete: [purpose]` (cases 214.1, 266).
        **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
        **＋** An `update` entry for an Estimate that names no part of the page — `change` alone — or carries `set.status` carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own. One that names a part — `set` without `status`, `replace`, `sections` without `Criterion` — and writes no Criterion carries that part alone, nothing lifted; it carries `set: {status: pending}` when the `old` of a `replace` pair stands in the page's `## Criterion`, and no status otherwise; a written `sections.Criterion` beside any other part stands and sets `pending` (case 296).
        **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
        **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
        **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
        **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
        **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
        **－** A line the grammar does not parse goes under `unparsed`; the run goes on.
```

```tasks
- [x] update `rule-materialize`: `replace` in the Purpose — a part named changes alone; a part inside the Criterion sets `pending`
- [x] update `estimate-materialize-assembles`: the Criterion whole under `sections`, one line changed, `pending`
- [x] `guppi/materialize.py`: `lift_criterion` — the branch "a part is named"; `touches_criterion(page, replaces)` reads the page's `## Criterion`; the docstring
- [x] `tests/test_materialize.py`: `set: {purpose}` alone — no `sections`, no `set.status`; a pair with `old` in the Criterion — `set: {status: pending}`, no `sections`; a pair with `old` in Result — nothing; a pair with `old` not on the page — nothing; `set: {purpose, status: pending}` — lifted and the field; the test of Case 17 (`change` alone) stands
- [x] read `estimate-materialize-assembles`: pytest now; live — the librarian's run of this session, `--show`: the three entries of 295 carry `replace` and `set: {status: pending}`, no `sections`
```

## Case 297 — two Rule-class texts say the old form of an Estimate `update`

> **context:**
> `estimates/schema.md`, the row `## Criterion`: "an `update` that names the Estimate by slug replaces it whole and sets the page `pending`" — after 296 not always. `index.md` §7: "a Case that changes the promise names the Estimate by slug and its `update` replaces the Criterion whole … only a replaced Criterion does" — right for the change of a promise, silent on the second form. Both are Rule-class files: an `update` with `file`, applied by hand in Work Mode; `generate` reports the item as applied by hand. §3 ("only a replaced Criterion sets it `pending`") holds as it is — a pair inside the Criterion is a replaced Criterion.

> **problem:**
> The schema of Estimates says outright that any `update` by slug replaces the Criterion whole; after 296 that is false in the same way as the three `given` lines of 295.

> **given:**
> 296: an item that names a part alone changes that part; a part inside the Criterion sets `pending`; `change` alone or `set.status` replaces the Criterion whole.
> **＋** A Rule-class file changes by an `update` with `file` and `change`, by hand in Work Mode (case 59.8); the hook refuses no hand edit of a schema or of `index.md`.

> **when:**
> Someone reads the `## Criterion` row of `estimates/schema.md` or §7 of `index.md`.

> **then:**
> The row `## Criterion` of `estimates/schema.md` reads: "an `update` that changes the promise replaces it whole and sets the page `pending`; an `update` that names a part alone — a field, a `replace` pair — keeps it, and a pair inside it sets `pending` (case 296)".
> **＋** §7 of `index.md`, after "(cases 187, 193)", reads: "an `update` that names a part alone changes that part, `pending` when the part is inside the Criterion (case 296)".
> **－** §3 does not change.

```then
update:
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    change: the Criterion row — an update that changes the promise replaces it whole; one that names a part alone keeps it, a pair inside it sets pending (case 297)
  - slug: index
    file: vault/wiki/index.md
    change: §7 — an update that names a part alone changes that part, pending when the part is inside the Criterion (case 297)
```

```tasks
- [x] update `estimates-schema`, by hand: `vault/wiki/estimates/schema.md` — the row `## Criterion`, the sentence "an `update` that names the Estimate by slug replaces it whole and sets the page `pending`"
- [x] update `index`, by hand: `vault/wiki/index.md` §7 — one sentence after "(cases 187, 193)"
```

## Deferred

## Case 293 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft` placeholders, deferred fifteen times, the last by 289. This session took the readings due at `/hi` (W1, W2), the repair of the two Criteria replaced by a field-only `update` and the rule that an item names the part it changes (291), and the condition on new dependencies, dropped by the owner without a page, ahead of it.

> **problem:**
> The person closes this Plan Mode with one Case and goes to pre-spec; Slice 3b waits for the next session, the sixteenth defer. The lines of 289 still bear on it: a subagent loads `CLAUDE.md` and not the glossary (288.1), and `guppi recall` brings the session's load back after a compaction (287) — the rule of Work Mode is written with both.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270, the render and sprint lines in the form of case 279.1), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; a subagent loads CLAUDE.md and no glossary (case 288.1); with rule-work-mode, the first item of the next session
```

## Case 298 — a Case superseded in its own session leaves the Spec

> **context:**
> 296 superseded 291.1 before the Spec was approved. The Spec of 1315 still holds 291.1 whole — its sections, its `then` block, its five task lines — and nothing ticks or removes them: `generate` neither applies nor ticks the entries of a superseded Case (151, 200.2), `tick_read` skips its `read` lines (286), Retro does not count its lines (282). The lines stay `[ ]` for good, and an open box that nobody will close reads like debt. The rule that the replaced text stays in the Spec of its session (index §7, the Case schema) is right for a supersede from a later session, whose Spec is archived history; inside one session the Spec is the plan the person approves, and a Case superseded before the approval was never the plan.

> **problem:**
> The Spec should hold what the session is going to do. A Case superseded in the same session is removed by the agent and the superseding Case is written whole — as the schema already asks of a taken-up defer — and pre-spec catches a superseded Case still in the plan. Two scripts lean on the Case being there: `materialize` takes the decision entry's text and `then` from the Spec and would mark the entry `incomplete: [then]`; `generate` writes the Decision page of the superseded Case from that text.

```then
defer:
  - slug: rule-prespec
    type: rule
    purpose: prespec --check reads every {supersedes:case N} of the session's ledger and prints a line when ## Case N or ### Case N still stands in the plan — the superseded Case leaves the Spec, the superseding one is written whole; the check runs to a clean output like the others (owner, Retro of 1315)
  - slug: rule-materialize
    type: rule
    purpose: a decision entry marked superseded_by with no Case of its number in the Spec is complete by the mark alone — no incomplete: [then], no case_text; the replaced text is the ledger lines and the Decision page of the superseding Case
  - slug: rule-page-generation
    type: rule
    purpose: the Decision page of a Case superseded in its own session is written with status superseded and a one-line body — superseded by case N before the Spec was approved — so origin and deferred_by resolve as before; the supersede from a later session keeps the text of the archived Spec as today
```
