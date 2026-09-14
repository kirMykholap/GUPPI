<!-- approved 19:58:45 · session 80e13d37 -->

# Spec — 2026-09-14, session P (hi 16:33)

## Case 142 — `insight-harness-yaml-entry-shape-assumed`: an entry fails alone, the entry shape in one place

> **context:**
> An Insight of severity 2, `open`, two children of 2026-09-10: `generate` crashed on a `replace` mapping (one entry stopped the run); `materialize` built its index over `e["line"]` and crashed on the three librarian entries without `line`. Pattern: `materialize.yaml` has four writers — materialize, the `then` block of the Spec, the librarian, the marks of `generate` — and each script reads the file as if it alone had written it. Proposal: (1) the shape of an entry is stated in one place and every script reads through it; (2) the rule of Case 47 — an entry fails alone — is extended from `generate` to `materialize`.

> **problem:**
> Both children were fixed in place: `generate` catches any exception per entry since Case 47; `materialize` skips entries without `line`. But `assemble` in `materialize.py` has no guard per entry: any exception while lifting a line is "materialize.yaml not written", exit 1, the walk stops, no entry of the unit is written. And the field list of `rule-materialize` (case 49) is behind: no `path`, `decision`, `derived`, `criterion_block`, `set`, `case_removed`, `status`/`result` of a folded reading, the librarian's marks (`near`, `librarian`, `synthesis`), `superseded_by` from another unit (130.2). Decide: action the Insight by work, reject it, or defer it.

> **given:**
> `insight-harness-yaml-entry-shape-assumed`: `open`, severity 2, children `lesson-generate-replace-mapping-crashes`, `lesson-materialize-assumes-every-entry-has-a-line`, both `clustered`; the cascade of 104.2 archives them on `actioned`.
> **＋** `rule-materialize` `built`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`; its text: "An error on one date stops the walk with exit 1"; "A line the grammar does not parse goes under `unparsed`; the script continues" — for an unparsed line only. Code: `materialize_date` catches `Exception` around the whole of `assemble` → "materialize.yaml not written", return 1; `run` stops the walk at the first non-zero code.
> **＋** `rule-page-generation` `built` holds the rule of Case 47: "An entry that fails — … a field whose shape the script does not expect, any exception raised while applying it — is reported on stderr, marked `failed` and skipped; the rest apply; the exit code is 1. No entry ends the run." The three Estimates of Case 47 were archived on 09-11; no live Estimate carries the criterion, it is read through `estimate-generate-writes`. Code: `apply` sends an entry without `kind` to `vault.error("unknown kind None")` and marks it `failed` with that text.
> **＋** `archive.py` (`uncovered_lines`, `kept_reason`) and `tail.py` read entries through `isinstance(dict)` and `.get`; `known = {e["line"]: e … if "line" in e}` in `assemble` is the fix of the second lesson.
> **＋** The librarian's marks `near`, `librarian`, `synthesis` are described in `rule-documentation`; `applied`/`failed` in `rule-page-generation`; `superseded_by` from another unit in 130.2. No page lists all of them together.
> **＋** `case-schema.md` pins the shape of `replace`; `rule-index-check`, `rule-brief`, `rule-raw-archive`, `rule-ledger-tail` read the yaml by named marks — unchanged.
> **－** An Insight is not a Leaf: no `contract`, no Estimate. No other live Lesson or Insight is about a script crashing on a yaml entry (`ask-guppi`).
> **－** `rule-lint` does not read the yaml; `case-schema.md` is not touched.

### Case 142.1 — `materialize` fails an entry alone; the field list complete

> **when:**
> `guppi materialize` lifts a record line of the ledger and the lift raises — a `then` item of an unexpected shape, any error in `decision_entry`, `derived_entries`, `estimate_entry`, `lesson_entry`.

> **then:**
> The line becomes an entry `{line, text, failed: "<Type>: <message>"}` without `kind`; one line on stderr, `materialize: line N: <message>`; the other lines are lifted; the yaml is written; the unit's exit is 1; the walk goes on to the next unit.
> **＋** On the next run an entry with `failed` and no `kind` is lifted again from its line and replaced when the lift succeeds — the Spec fixed, the run repeated (the class of 53.3).
> **＋** An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run.
> **＋** The field list in "How it works" of `rule-materialize` is complete, every field with its writer: from the ledger line, from the `then` block, derived (`derived`, `decision`, `criterion_block`, `set`, `case_removed`), a folded reading (`status`, `result`, `folded`), a `file` with `path`, the marks of `generate` (`applied`, `failed`), the marks of the librarian (`near`, and `librarian` with the value `merged` or `synthesis` — by `rule-documentation`), `superseded_by` from any unit. A key the code writes and the list does not name is a finding of the reading.
> **－** A `MaterializeError` — no `ledger.md`, a Case heading in two files — still stops the walk with exit 1.
> **－** `unparsed` does not change: a line the grammar does not parse goes there, as today.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "A line the grammar does not\nparse goes under `unparsed`; the script continues."
        new: "A line the grammar does not\nparse goes under `unparsed`; the script continues. A line whose lift raises — a `then` item of an unexpected shape, any error while the entry is built — becomes an entry `{line, text, failed: \"<Type>: <message>\"}` without `kind`, reported on stderr as `materialize: line N: <message>`; the other lines are lifted, the yaml is written, the unit exits 1 and the walk goes on to the next unit; on the next run such an entry is lifted again from its line and replaced when the lift succeeds. An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run (case 142.1)."
      - old: "One entry per record line, in ledger order. Fields: `case`, `kind` (`create`,\n`update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug\nprefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`; a Rule-class file\nis `file` with its path), `slug`, `ref`, `source`, `supersedes`, `superseded_by`,\n`origin` (`raw/<date>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text` (the\nledger line), `tags` (from `{tags:...}`), `fields`, `sections`, `replace`, `change`\n(from the `then` block), `incomplete` (required fields the block lacks), `exists`\n(a create whose page is on disk with an `origin` carrying this line's `#case-N`; a page of another Case, live or archived, leaves the entry a create for `generate` to refuse as a collision, case 105.2), `folded` (the ledger lines of readings folded into\na create), `applied` and `failed` (set by `guppi generate`: the time applied, or the\nerror)."
        new: "One entry per record line, in ledger order. The fields of an entry, each with its writer (case 142.1) — from the ledger line: `case`, `kind` (`create`, `update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`; a Rule-class file is `file` with its `path`), `slug`, `ref`, `source`, `supersedes`, `tags` (from `{tags:...}`), `origin` (`raw/<date>/<HHMM>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text` (the ledger line), `decision` (`decision-case-<N>`); from the `then` block: `fields`, `sections`, `replace`, `change`, `impact`, `incomplete` (required fields the block lacks), `exists` (a create whose page is on disk with an `origin` carrying this line's `#case-N`; a page of another Case, live or archived, leaves the entry a create for `generate` to refuse as a collision, case 105.2); derived by this script: `derived`, `criterion_block`, `set`, `case_removed`, and `status`, `result`, `folded` of a reading folded into a create; `superseded_by` from a later `{supersedes}` in any unit; `failed` from a lift that raised; set by `guppi generate`: `applied` (the time applied) and `failed` (the error); set by the librarian: `near`, and `librarian` with the value `merged` or `synthesis` (`rule-documentation`). A key the code writes and this list does not name is a finding."
    change: "an entry fails alone in materialize, the walk goes on; an unreadable existing entry is left alone; the field list names every field and its writer (case 142.1)"
```

```tasks
- [x] `guppi/materialize.py`: in `assemble`, wrap the lift of one record line (`decision_entry` … `derived_entries`, `estimate_entry`, `lesson_entry`, `fold_estimate`) in a per-line guard; on an exception append `{line, text, failed}` and print `materialize: line N: <message>` to stderr; return a flag so `materialize_date` writes the yaml and returns 1; `run` continues the walk on that code (a `MaterializeError` still stops it)
- [x] `guppi/materialize.py`: in `assemble`, retry an existing entry with `failed` and no `kind` — drop it from `known` so its line is lifted again and the old entry is replaced on success
- [x] `guppi/materialize.py`: skip an existing entry that is not a mapping, or has neither `line` nor `derived`, with one stderr line, in `assemble`, `fold_estimate`, `mark_superseded` and the decisions loop (`d["case"]`)
- [x] `guppi/materialize.py`: docstring — the fail-alone paragraph
- [x] `tests/test_materialize.py`: a lift that raises (monkeypatch `decision_entry`) — the entry `{line, text, failed}`, stderr line, yaml written, exit 1, the next unit walked; a rerun with the lift fixed replaces the entry; a string entry and a mapping without `line`/`derived` in an existing yaml are left alone
- [x] `make test`, `make style`
- [x] read `estimate-materialize-assembles` (block 142.1): the tests above, and every key `materialize.py` writes found in the field list of `rule-materialize`
```

### Case 142.2 — `generate` skips an entry `materialize` failed

> **when:**
> `guppi generate` reaches an entry with `failed` and no `kind`.

> **then:**
> The entry is skipped: not applied, `failed` kept as `materialize` wrote it, one line on stderr `generate: line N: not lifted by materialize; <message>`; exit 1; the other entries apply.
> **－** An entry with `kind` and a stale `failed` of an earlier run is as today (53.3): applied, the mark dropped.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "No entry ends the run."
        new: "No entry ends the run. An entry with `failed` and no `kind` — a line `materialize` could not lift (case 142.1) — is skipped with its mark kept and one stderr line, `generate: line N: not lifted by materialize; <message>`; the exit code is 1 (case 142.2)."
    change: "an entry materialize failed is skipped, its failed mark kept (case 142.2)"
```

```tasks
- [x] `guppi/generate.py`: in `apply`, before the kind dispatch — an entry with `failed` and no `kind` is reported and skipped, its mark untouched, `vault.errors` extended so the exit is 1
- [x] `tests/test_generate.py`: such an entry in the yaml — not applied, mark unchanged, stderr line, exit 1, the next entry applied
- [x] `make test`, `make style`
- [x] read `estimate-generate-writes` (block 142.2): the test above
```

### Case 142.3 — the Insight actioned

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-harness-yaml-entry-shape-assumed`: `status: actioned`, `addressed_by: decision-case-142.3`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The two children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** No entry-schema module is made in code; `case-schema.md` does not change (`rule-documentation` changes by 142.5, pre-task).
> **－** The Frontier line F3 closes on this Case.

```then
update:
  - slug: insight-harness-yaml-entry-shape-assumed
    set: {status: actioned, addressed_by: decision-case-142.3}
    change: "actioned: materialize fails an entry alone and generate keeps its mark (142.1, 142.2); the field list of rule-materialize is the one place for the entry shape; no schema module in code (case 142.3)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the two children (142.3)
```

### Case 142.4 — `rule-materialize`: the walk does not stop on a failed line

> **given:**
> `rule-materialize` line 30: "An error on one date stops the walk with exit 1"; `estimate-materialize-walks-dates` (43) quotes the same words. 142.1 says "the walk goes on to the next unit" and "a `MaterializeError` still stops the walk" — without a change of line 30 the page contradicts itself and the Estimate contradicts block 142.1 (pre-task).

> **when:**
> `guppi materialize` walks the units and in one of them the lift of a line raised.

> **then:**
> Line 30 reads: "An error of a unit — no `ledger.md`, a Case heading in two files — stops the walk with exit 1; a line whose lift failed marks its entry, the unit exits 1 and the walk goes on (case 142.4)."
> **＋** Test: two units, a failing lift in the first — the second is written, the exit is 1.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-walks-dates
    replace:
      - old: "An error on one date stops the walk with exit 1."
        new: "An error of a unit — no `ledger.md`, a Case heading in two files — stops the walk with exit 1; a line whose lift failed marks its entry, the unit exits 1 and the walk goes on (case 142.4)."
    change: "a failed line does not stop the walk; a unit error still does (case 142.4)"
```

```tasks
- [x] `guppi/materialize.py`: `run` continues the walk after a unit whose lift failed a line and returns 1 at the end; a `MaterializeError` still returns at once
- [x] `tests/test_materialize.py`: two units, the first with a failing lift (monkeypatch) — both yamls written, exit 1
- [x] read `estimate-materialize-walks-dates` (block 142.4): the test
```

### Case 142.5 — `rule-documentation`: `failed` is also written by `materialize`

> **given:**
> The marks paragraph of the frame, line 60: "`applied` and `failed` are set by `guppi generate`". After 142.1 `materialize` sets `failed` on an entry without `kind` (pre-task).

> **when:**
> `guppi render` writes `librarian-guppi.md`.

> **then:**
> "`applied` is set by `guppi generate`; `failed` by `guppi generate`, or by `guppi materialize` on an entry without `kind` — a line it could not lift (case 142.5)"; the rest as it is. No `contract`.

```then
update:
  - slug: rule-documentation
    replace:
      - old: "Marks in `materialize.yaml`: `applied` and `failed` are set by `guppi generate`, an\nentry with either is skipped or reported;"
        new: "Marks in `materialize.yaml`: `applied` is set by `guppi generate`; `failed` by `guppi generate`, or by `guppi materialize` on an entry without `kind` — a line it could not lift (case 142.5); an\nentry with either is skipped or reported;"
    change: "failed may be set by materialize on a line it could not lift (case 142.5)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes `librarian-guppi.md`
```

## Case 143 — `insight-librarian-frame-omits-required-reads`: actioned

> **context:**
> An Insight of severity 2, `open`, two children of sessions F and G (2026-09-10…11): the librarian's frame named the reads it allows one by one, and the list was shorter than the judgments; the agent either broke a clause (read `generate.py`, read a lesson page against the ban of `rule-synthesis`) or judged on an index line alone. Pattern: the reads the work needs were found while the work ran, not when the frame was written. Proposal: derive the read clauses from the judgments — one clause per judgment, the page and the field; change every Rule that names a read in one pass; the readings of `estimate-documentation-completes` and `estimate-synthesis-clusters` after the next run show whether the list is complete.

> **problem:**
> The Proposal was carried out by Case 54 and after it. The frame (`rule-documentation`) holds exactly four reasons to open a page — one per judgment: same or near at a `create`; a shared root cause of a lesson "with another lesson or an Insight"; why a script failed an entry; a fact the brief needs (the status of an Estimate, the severity of an Insight). The children's clauses agree: `rule-index-check` ("open the page and name it in the report"), `rule-synthesis` ("read the Trigger and Root cause of the candidate", the ban lifted by 54), `rule-brief` ("read it from the page and name the page"); 58 added `Makefile`, `guppi/`, `tests/`; 90.3 — an instruction of the handoff outside the frame is refused and named in the report. No two clauses answer one act differently today (`ask-guppi`). Both Estimates `passed`; nine librarian runs since session H — no new lesson of the class; the brief of O: "the handoff's instructions were all within the frame; none was refused". Decide: the Insight `actioned`.

> **given:**
> `insight-librarian-frame-omits-required-reads`: `open`, severity 2, children `lesson-librarian-reads-beyond-the-four-inputs`, `lesson-frame-read-clauses-omit-candidate-check-and-brief`, both `clustered`; the cascade of 104.2 archives them on `actioned`.
> **＋** `rule-documentation` `built`, `estimate-documentation-completes` `passed` (last reading block 100.2, 2026-09-14): "Open a page under `vault/wiki/` for four reasons only: …" — same or near; a root cause "with another lesson or an Insight"; a page a script names in an error; a fact the brief needs; "Name every page you open in the report"; the ban on `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`, `vault/archive/`; `Makefile`, `guppi/`, `tests/` — "read them when a command's output is not enough" (58); the refusal of a handoff instruction outside the frame (90.3); the archive root (102.4).
> **＋** `rule-index-check` `built`, `estimate-index-check-merges`: "When the index line does not settle same or near, open the page and name it in the report". `rule-synthesis` `built`, `estimate-synthesis-clusters` `passed` (2026-09-12, J: every page opened named with its outcome): "read the Trigger and Root cause of the candidate … Do not read the archive" (54). `rule-brief` `built`: "read it from the page and name the page in the report".
> **＋** History of the clauses after 54: `rule-documentation` only (58, 73.8, 90.3, 102.4); `rule-index-check`, `rule-synthesis`, `rule-brief` — no change of a read clause. No two Rules answer one act differently.
> **＋** Librarian runs H…O: no new lesson about a read outside the frame; in O no page was opened for the index check, two `near` marks with their reason on index lines — within reason 1 (opening is a right, not a duty).
> **－** `rule-cleanup`, `rule-materialize`, `rule-page-generation`, `rule-raw-archive`, `rule-close` carry no read clause of the agent — nothing to compare.
> **－** An Insight is not a Leaf: no `contract`, no Estimate. No Rule changes; `librarian-guppi.md` is not rendered again.

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-librarian-frame-omits-required-reads`: `status: actioned`, `addressed_by: decision-case-143`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The two children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** `rule-synthesis` does not change: an Insight candidate is read under reason 2 of the frame; a new lesson of the class is a new Case.
> **－** The Frontier line F4 closes on this Case.

```then
update:
  - slug: insight-librarian-frame-omits-required-reads
    set: {status: actioned, addressed_by: decision-case-143}
    change: "actioned: the four reasons of the frame (54, 58, 90.3, 102.4) are one clause per judgment, the children's clauses agree, nine runs without a recurrence; no Rule changed (case 143)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the two children (143)
```

## Case 144 — `insight-materialize-lift-loses-a-schema-field`: `source` on the line, the three lessons of O, the Insight actioned

> **context:**
> An Insight of severity 2, `open`, two children (G, J): a standalone Estimate `create` put `criterion` and `method` into the frontmatter instead of sections; `parse_line` read only `tags` from the braces of a lesson line and lost `source`. Pattern: the parser decides what a page gets; the page is written without the field, and lint names the miss on the page — one step and one session after the line. Proposal: one table "field — category — where it comes from", `materialize` lifts by it; a field the source lacks is `incomplete`; a field the source holds and the table does not know is the parser's fault.

> **problem:**
> Both children are fixed: 53.3 — a standalone Estimate maps `context`, `criterion`, `method` into sections; 87 — `parse_line` returns `source` from the braces, a `knowledge` lesson without it is marked `incomplete: [source]`. The table of sources exists in code as `REQUIRED` (rules, entities, estimates, insights — the fields of a `then` item) plus the rule of 87 for a lesson; `rule-page-generation`: "A missing `source` is not invented; lint names it". The recurrence in O — three `knowledge` lessons without `source` — is not a loss by the parser: the lines carried no `{source:…}`. The cause is upstream: neither `rule-case-protocol` (the Render in `CLAUDE.md`) nor `rule-retro` tells the agent to write `{source:…}` on a `knowledge` line; only `case-schema.md` ("present only when they apply", 75.1) and the glossary say so. Decide: (1) the protocol names `source` as required on a `knowledge` line; (2) the three lessons of O get a `source`; (3) the Insight `actioned`.

> **given:**
> `insight-materialize-lift-loses-a-schema-field`: `open`, severity 2, children `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`, `lesson-materialize-lesson-line-source-dropped`, both `clustered`; the cascade of 104.2.
> **＋** `lessons/schema.yaml`: `source` under `optional` and `conditional: when kind: knowledge → required: [source]`; `schema.md`: "`knowledge`: external material studied once so the source never has to be supplied again", "`source` | `knowledge` | url or reference | Where the material came from". `rule-lint` checks by the schema — three `schema` findings on the lessons of O.
> **＋** `rule-materialize` `built` (87): "`source` when the braces of the line carry one … a `knowledge` lesson whose line carries no `source` is marked `incomplete: [source]`"; `parse_line` returns `source` for a lesson and a decision.
> **＋** `rule-page-generation` `built`: "A missing `source` is not invented; lint names it".
> **＋** `rule-case-protocol` `built`, `enforcement: render`, `governs: CLAUDE.md`, `render_mode: partial`, `estimates: [estimate-case-protocol-loaded]`; its Render in `CLAUDE.md` names the form `- lesson[...]` and `{tags:a,b}` for a `create`, not `source`. `rule-ledger-write`: writes verbatim, refuses only without `/hi`. `rule-retro`: `- lesson[...]` without `source`.
> **＋** `case-schema.md`: "`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1)"; the glossary: `source` "in a ledger line, the external origin".
> **＋** Three lessons of O, `kind: knowledge`, `status: new`, no `source`, `raw/2026-09-14/1229/materialize.yaml` `incomplete: [source]`: `lesson-gate-plan-path-cut-by-the-event-log-detail-limit` (L20), `lesson-agents-read-at-session-start-in-claude-code-2-1-228` (L29), `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` (L31).
> **－** No other live Lesson or Insight is about a field lost between the line and the page (`ask-guppi`).
> **－** An Insight is not a Leaf; a Lesson is not a Leaf: an `update` without `contract`. `case-schema.md` and `lessons/schema.*` do not change.

### Case 144.1 — `rule-case-protocol`: `{source:…}` on a `knowledge` line

> **when:**
> `guppi render` writes the Render of `rule-case-protocol` into `CLAUDE.md`; then the main agent writes a `- lesson[knowledge][...]` line.

> **then:**
> The paragraph on ledger lines in the Render carries the sentence: "A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one."
> **＋** `CLAUDE.md` carries the sentence after the render; `guppi render --check` exit 0.
> **－** `rule-ledger-write` does not change: the hook writes verbatim and checks nothing.
> **－** `rule-retro` does not change: its example lines stay; the rule is read in `CLAUDE.md`.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "A `create` line carries the ratified tags: `{tags:a,b}`.\nWrite the `- decision[...]` lines only in the reply that acknowledges ratification;"
        new: "A `create` line carries the ratified tags: `{tags:a,b}`. A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one.\nWrite the `- decision[...]` lines only in the reply that acknowledges ratification;"
    change: "a knowledge lesson line carries {source:...}, the reference the lesson studied (case 144.1)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes the sentence into `CLAUDE.md`; `guppi render --check` exit 0
- [ ] read `estimate-case-protocol-loaded` (block 144.1): the sentence in `CLAUDE.md` after the render, `--check` exit 0
```

### Case 144.2 — the three lessons of O get a `source`

> **when:**
> `guppi generate` applies the three entries; then `guppi lint` reads the lessons.

> **then:**
> `lesson-gate-plan-path-cut-by-the-event-log-detail-limit`: `source: guppi/event.py, DETAIL_LIMIT = 80, read by guppi/gate.py`. `lesson-agents-read-at-session-start-in-claude-code-2-1-228`: `source: the probe of case 139.1, Claude Code 2.1.228`. `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`: `source: .claude/skills/retro/SKILL.md, disable-model-invocation: true`.
> **＋** History of each: `updated: source added (case 144.2)`; the three `schema` findings leave lint.
> **－** `kind` does not change: `knowledge`, by the owner's choice in O.

```then
update:
  - slug: lesson-gate-plan-path-cut-by-the-event-log-detail-limit
    set: {source: "guppi/event.py, DETAIL_LIMIT = 80, read by guppi/gate.py"}
    change: "source added (case 144.2)"
  - slug: lesson-agents-read-at-session-start-in-claude-code-2-1-228
    set: {source: "the probe of case 139.1, Claude Code 2.1.228"}
    change: "source added (case 144.2)"
  - slug: lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate
    set: {source: ".claude/skills/retro/SKILL.md, disable-model-invocation: true"}
    change: "source added (case 144.2)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the three `update`s; `guppi lint` loses the three `schema` findings on `source` (144.2)
```

### Case 144.3 — the Insight actioned

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-materialize-lift-loses-a-schema-field`: `status: actioned`, `addressed_by: decision-case-144.3`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The two children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** No table of sources is made in code: `REQUIRED` in `materialize.py` and the rule of 87 are the place; a field lost by the parser is a new lesson and a new Case.
> **－** The Frontier line F5 closes on this Case.

```then
update:
  - slug: insight-materialize-lift-loses-a-schema-field
    set: {status: actioned, addressed_by: decision-case-144.3}
    change: "actioned: the children fixed by 53.3 and 87; the protocol names {source:...} on a knowledge line (144.1); the three lessons of O sourced (144.2); no table in code (case 144.3)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the two children (144.3)
```

## Case 145 — `insight-tests-clock-not-pinned`: the clock of the tests pinned in one place

> **context:**
> An Insight of severity 2, `open`, two children (2026-09-10, 09-11): the CLI tests held `TODAY = 2026-09-09` while `cli.main` read the real clock — three tests went red the next day; the helper of `test_generate.py` called `generate.run` without `now` — five tests went red a day later on the committed tree. Pattern: a test pins the date on one side of the call and the code reads the real clock on the other; it passes on the day it is written and fails later. Proposal: every entry point that reads the clock takes `now`, every helper passes the pinned date; a run under a shifted date catches the rest of the class.

> **problem:**
> The first half of the Proposal is done in place: all twelve `run()` in `guppi/` take `now=None` and read the clock only there (`datetime.now().astimezone()`); the helpers of ten test files pass `NOW`; `index`, `lint`, `render`, `tail`, `cli` read no clock, `materialize` does not use `now`. The second half does not exist: nothing stops the next helper from forgetting `now` — the error shows again on a later day, not on the day it is written. No Rule on the test suite as a whole exists in the vault; there is no `conftest.py`. Decide: close the class with one fixture file under its own Rule page, or close the Insight as done and wait for a recurrence.

> **given:**
> `insight-tests-clock-not-pinned`: `open`, severity 2, children `lesson-tests-cli-date-pinned`, `lesson-tests-generate-history-date-unpinned`, both `clustered`; both fixes were code repairs recorded in the lesson line itself, no Decision; the cascade of 104.2.
> **＋** No live Rule on the test suite; `tests/` appears only in the `implementation_ref` of thirteen Rules; no `conftest.py` (`ask-guppi`). `rule-harness` — MOC, `built`, `children: [rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md, rule-bash-guard]`, `estimates: [estimate-harness-pipeline]`; a child is added by an `update` of the MOC.
> **＋** Code: `archive`, `bashguard`, `cleanup`, `event`, `gate`, `generate`, `guard`, `ledger`, `materialize`, `pretask`, `spec` — `from datetime import datetime`, the clock read only in `run()`: `now = datetime.now().astimezone() if now is None else now`. No other clock read (`date.today`, `time.time`) in `guppi/`.
> **＋** Tests: `NOW`/`TODAY` pinned in ten files; `test_materialize`, `test_index`, `test_lint`, `test_render`, `test_tail` pass no `now` — their modules read no clock.
> **＋** `Makefile`: `make test` is `uv run pytest -q`; the partial targets `test-session-start`, `test-plan-mode`, `test-documentation`. `rules/schema.md`: a `check` Rule carries `implementation_ref` and an Estimate through `method`.
> **＋** No other live lesson about a test reading the real clock; `lesson-generate-walk-history-dated-by-yaml` is about the yaml's date against the run's date, another cause.
> **－** The slug `rule-tests-clock-pinned` is free, not in the archive. Tags `tests` ("the harness's own test suite, its fixtures and clocks"), `harness` — in `tags.md`.
> **－** An Insight is not a Leaf. No new dependency: a `datetime` subclass and pytest's `monkeypatch`.

### Case 145.1 — `create rule-tests-clock-pinned`

> **when:**
> `pytest` collects `tests/`; then any test calls the `run()` of a `guppi/` module without `now`, or the code reads `datetime.now()` somewhere outside `run()`.

> **then:**
> An autouse fixture in `tests/conftest.py` sets, before every test, into every `guppi/` module that imports `datetime` a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC` (`astimezone` gives the same second); a test that leaves the code the real clock sees the year 2001 and fails on the day it is written.
> **＋** The list of modules is built by walking `guppi/*.py` for a `datetime` attribute, not by hand: a new module with a clock is covered without a change of the fixture.
> **＋** One test, `tests/test_conftest.py`: `guppi.ledger.run` without `now` writes a time dated 2001; `datetime.strptime` and the constructor of the subclass work as before.
> **＋** `make test` is green under the fixture on the tree of this session.
> **－** A test that passes `now` does not notice the fixture: `run()` reads no clock.
> **－** The `Makefile` does not change; the `test-*` targets are covered by the same fixture.

```then
create:
  - slug: rule-tests-clock-pinned
    type: rule
    kind: Leaf
    purpose: Prevents a test from passing on the day it is written and failing later because the code read the real clock
    enforcement: check
    implementation_ref: [tests/conftest.py, tests/test_conftest.py]
    tags: [tests, harness]
    sections:
      Purpose: |
        Prevents a test from passing on the day it is written and failing later because
        the code read the real clock. Two lessons of 2026-09-10 and 09-11 went red a day
        after they were written: the test pinned a date, the code read `datetime.now()`.
        Every `run()` of `guppi/` takes `now`; this Rule makes forgetting it fail at once.
      How it works: |
        `tests/conftest.py` holds one autouse fixture. Before every test it walks every
        module under `guppi/` that carries a `datetime` attribute and replaces it, with
        pytest's `monkeypatch`, by a subclass of `datetime` whose `now(tz=None)` returns
        `2001-01-01 00:00:00 UTC`; `astimezone` gives the same second. A test that calls a
        `run()` without `now`, or code that reads the clock outside `run()`, sees the year
        2001 and fails on the day it is written, not on a later one. The list of modules is
        built by the walk, never by hand. `datetime.strptime`, `fromisoformat` and the
        constructor of the subclass work as before. A test that passes `now` does not
        notice the fixture. `tests/test_conftest.py` checks the fixture itself: a `run()`
        without `now` writes a time dated 2001 (case 145.1).
    method: "`tests/test_conftest.py` green, `make test` green under the fixture; one reading by hand, recorded in the estimate line"
```

```tasks
- [x] `tests/conftest.py`: the autouse fixture — walk `guppi/*.py` (`pkgutil` over `guppi.__path__`, `importlib.import_module`), for each module with a `datetime` attribute `monkeypatch.setattr(module, "datetime", PinnedDatetime)`; `PinnedDatetime(datetime)` with `now(cls, tz=None)` returning `datetime(2001, 1, 1, tzinfo=UTC)` (converted to `tz` when given)
- [x] `tests/test_conftest.py`: `guppi.ledger.run` (or `guppi.event.run`) called without `now` writes a stamp dated 2001-01-01; `PinnedDatetime.strptime` and `PinnedDatetime(2026, 9, 14)` behave as `datetime`
- [x] `make test`, `make style`
- [x] read `estimate-tests-clock-pinned` (block 145.1): the two tests above and `make test` green
```

### Case 145.2 — `rule-harness`: the eighth child

> **when:**
> `guppi generate` applies the entry; then someone reads `rule-harness` or `rules-index.md`.

> **then:**
> `children` of `rule-harness` ends with `rule-tests-clock-pinned`; the `## Children` section is rebuilt; History `updated: rule-tests-clock-pinned added (case 145.2)`.
> **－** `estimate-harness-pipeline` does not change: a MOC without a contract on the test pipeline.

```then
update:
  - slug: rule-harness
    set: {children: [rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md, rule-bash-guard, rule-tests-clock-pinned]}
    change: "rule-tests-clock-pinned added (case 145.2)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update` and rebuilds `## Children` (145.2)
```

### Case 145.3 — the Insight actioned

> **when:**
> `guppi generate` applies the entry; then someone reads the Insight page or the brief.

> **then:**
> `insight-tests-clock-not-pinned`: `status: actioned`, `addressed_by: decision-case-145.3`; `## Addressed by` derived; History carries `open → actioned`.
> **＋** The two children are `archived` by the cascade, moved by `cleanup`; `severity` recomputed.
> **－** The Frontier line F6 closes on this Case.

```then
update:
  - slug: insight-tests-clock-not-pinned
    set: {status: actioned, addressed_by: decision-case-145.3}
    change: "actioned: every run() takes now (the children's fixes); the clock of the tests pinned to 2001 by rule-tests-clock-pinned (145.1) (case 145.3)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the `update`, the cascade archives the two children (145.3)
```

## Case 147 — no index files: the agent takes the list of pages with one Grep

> **context:**
> `guppi index` writes four `wiki/<category>-index.md` — one line `slug: purpose` per live page (`root_cause` for lessons, `pattern` for insights, a `· deferred_by:` tail), `cleanup` rewrites them, `make lint` checks them with `index --check`. Only agents read them: `ask-guppi` (its first input, `@rules-index.md`) and the librarian at the index check and the synthesis. The owner does not read them.

> **problem:**
> An index is derived from the frontmatter, and one Grep gives the same line: `^(purpose|deferred_by):` over `vault/wiki/rules/` — `rules/rule-x.md:purpose: …`. Four files, a script, a test, a `--check` and a Rule page hold what the agent gets with a command. Decide: remove the indexes; define the "index line" as the Grep line; rewrite the clauses of six Rules and §11.

> **given:**
> `rule-index` `built`, `check`, `implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]`, `parent: rule-harness`, `estimates: [estimate-index-lists]` `passed`; `rules-index.md`, `lessons-index.md`, `insights-index.md` live, `entities-index.md` empty.
> **＋** `rule-ask` `built`, `render`, `governs: .claude/agents/ask-guppi.md`, `estimate-ask-finds`: "Rules of the vault, one line per page: @vault/wiki/rules-index.md. Start there. Read `vault/wiki/<category>-index.md` for every other category …"; "its index line is not enough to judge". The agent's tools are Read, Grep, Glob; no Bash. The harness is governed by Rule pages: a crossing with a rule the agent misses is a crooked system caught later.
> **＋** `rule-index-check` `built`, `render` partial into the librarian, `estimate-index-check-merges`: "compare its `purpose` (`root_cause` for a lesson) with every line of `vault/wiki/<category>-index.md` of the same category"; "When the index line does not settle same or near, open the page". The librarian has Grep and Bash.
> **＋** `rule-synthesis` `built`, `estimate-synthesis-clusters`: "compare its `root_cause` with every line of `lessons-index.md` and of `insights-index.md`, by meaning"; "that Insight stays live with its pattern in the index".
> **＋** `rule-documentation` MOC `built`, `governs: .claude/agents/librarian-guppi.md`, `estimate-documentation-completes`: "Your inputs are four: … the four `vault/wiki/<category>-index.md` files, and `vault/wiki/tags.md`"; the four reasons to open a page — "an index line does not tell you …".
> **＋** `rule-cleanup` `built`, `estimate-cleanup-moves`, purpose "… or the indexes from lagging behind the vault"; "Then the four indexes are rewritten with the writer of `guppi index`; an archived Estimate leaves no line, since estimates have none." Code: `cleanup.py` imports `index.plan` and calls `rewrite_indexes()`.
> **＋** `rule-lint` `built`, `implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]`: "`make lint` runs it after `render --check` and `index --check` over the four index files; all three only report"; Makefile `lint:` — three commands; `test-harness` names `tests/test_index.py`.
> **＋** `index.md` §11 "The indexes" — the definition, "what makes semantic checks affordable", "no `estimates-index.md`", "no `decisions-index.md`", "`ask-guppi` is the search mechanism over these indexes"; §10 lines 353, 355 "checks new pages against the indexes", "when the indexes reveal a duplicate"; the glossary row "Index, `ask-guppi`". `rule-harness.children` holds `rule-index`; `cleanup` removes an archived slug from the `children` of live pages.
> **＋** The lint `ref` clause "every slug in `deferred_by` an existing decision page" does not depend on the index; `brief.md` "Readings at the close" names `guppi index --check` — not schema-governed, the librarian writes by its frame.
> **－** `estimate-index-lists`: its target goes to the archive — deleted by the same Case. `guppi index` is called nowhere else (`cleanup` is the writer; removed).
> **－** Rule-class files (`index.md`, `glossary.md`) — an `update` with `file`, by hand in Work Mode.

### Case 147.1 — `delete rule-index` and `estimate-index-lists`

> **when:**
> The librarian applies the entries; then `make lint` and `make test` run over the tree.

> **then:**
> `rule-index` and `estimate-index-lists` — `status: archived`, moved by `cleanup`; `rule-harness.children` without `rule-index`.
> **＋** `guppi/index.py`, `tests/test_index.py` deleted; `guppi/cli.py` without the `index` command; the four `wiki/*-index.md` deleted from the tree; Makefile `lint:` — `render --check`, `lint`; `make help` without the line on indexes; `test-harness` without `tests/test_index.py`.
> **－** Impact: `cleanup.py` stops calling the index writer (147.6); no hook, skill or agent reads `*-index.md` after 147.2–147.5.

```then
delete:
  - slug: rule-index
    impact: "guppi/index.py and tests/test_index.py deleted; the index command leaves cli.py; the four wiki/*-index.md files deleted; Makefile lint without index --check; cleanup.py stops importing index.plan (147.6); ask-guppi and the librarian read the Grep lines instead (147.2–147.5); rule-harness.children loses rule-index by cleanup"
  - slug: estimate-index-lists
    impact: "its target rule-index is deleted by this Case; no reading of it remains"
```

```tasks
- [x] delete `guppi/index.py`, `tests/test_index.py`; remove `index` from `guppi/cli.py`
- [x] delete `vault/wiki/entities-index.md`, `rules-index.md`, `lessons-index.md`, `insights-index.md`
- [x] Makefile: `lint:` without `index --check`, the comment on line 12 and the `lint` help line without indexes, `test-harness` without `tests/test_index.py`
- [x] `tests/test_generate.py`: the assertions that read `insights-index.md` (the `deferred_by` check behind block 124.2 of `estimate-generate-writes`) rewritten against the page's `deferred_by` field; the block stays as the record of a passed reading (pre-task)
- [x] `make test`, `make style`, `make lint` (the two remaining steps)
```

### Case 147.2 — `rule-ask`: the index through Grep, the rules always

> **when:**
> `guppi render` writes `.claude/agents/ask-guppi.md`; then the agent answers a question.

> **then:**
> The Render, instead of `@vault/wiki/rules-index.md` and "Read `vault/wiki/<category>-index.md` …": "Always start with the Grep of the rules, whatever the question: pattern `^(purpose|deferred_by):` over `vault/wiki/rules/`, output with content; the harness is governed by these pages, and a proposal that crosses one of them must be named. Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`. One line per page — `<category>/<slug>.md:<field>: <text>` — is the index line; decisions and estimates have none."
> **＋** The answer names the rule the proposal crosses on its `rules` line — as today.
> **－** No read of a `*-index.md`; the files do not exist.

```then
update:
  - slug: rule-ask
    contract: changed
    replace:
      - old: "Rules of the vault, one line per page:\n@vault/wiki/rules-index.md\n\nStart there. Read `vault/wiki/<category>-index.md` for every other category the question touches (entities, lessons, insights; decisions and estimates have none). When the question is about a check,"
        new: "Always start with the Grep of the rules, whatever the question: pattern `^(purpose|deferred_by):` over `vault/wiki/rules/`, output with content; the harness is governed by these pages, and a proposal that crosses one of them must be named. Then one Grep per other category the question touches: `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, `^(pattern|deferred_by):` over `vault/wiki/insights/`. One line per page — `<category>/<slug>.md:<field>: <text>` — is the index line; decisions and estimates have none (case 147.2). When the question is about a check,"
    change: "the index lines come from one Grep per category, the rules always first; no index file (case 147.2)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes `.claude/agents/ask-guppi.md`; `guppi render --check` exit 0
- [ ] read `estimate-ask-finds` (block 147.2): the first `ask-guppi` call after the render — the rules Grep first among its calls, no `*-index.md` read, the five lines as before
```

### Case 147.3 — `rule-index-check`: the librarian runs the Grep itself

> **when:**
> The librarian does the index check.

> **then:**
> "for each `create` entry … run the Grep of its category yourself — `^(purpose|deferred_by):` over `vault/wiki/<category>/` (`root_cause` for lessons, `pattern` for insights) — and compare the entry's `purpose` (`root_cause` for a lesson) with every index line it returns"; the rest as it is.
> **＋** The report names the Grep and the number of lines compared with.
> **－** The name of the rule does not change.

```then
update:
  - slug: rule-index-check
    contract: changed
    replace:
      - old: "compare its `purpose` (`root_cause` for a lesson) with every line of `vault/wiki/<category>-index.md` of the same\ncategory."
        new: "run the Grep of its category yourself — `^(purpose|deferred_by):` over `vault/wiki/<category>/`, `root_cause` for lessons, `pattern` for insights — and compare the entry's `purpose` (`root_cause` for a lesson) with every index line it returns; name the Grep and the number of lines in the report (case 147.3)."
    change: "the index lines come from the librarian's own Grep of the category, not a file (case 147.3)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes the partial into `librarian-guppi.md`
- [ ] read `estimate-index-check-merges` (block 147.3): the report of the next librarian run names the Grep and its line count, no `*-index.md`
```

### Case 147.4 — `rule-synthesis`: the same two Greps

> **when:**
> The librarian does the synthesis.

> **then:**
> "compare its `root_cause` with every index line of `lessons/` and of `insights/` — the Greps of 147.2 — by meaning"; "that Insight stays live with its pattern in its index line".

```then
update:
  - slug: rule-synthesis
    contract: changed
    replace:
      - old: "compare its `root_cause` with every line of\n`lessons-index.md` and of `insights-index.md`, by meaning."
        new: "compare its `root_cause` with every index line of `vault/wiki/lessons/` and of `vault/wiki/insights/` — the Greps `^(root_cause|deferred_by):` and `^(pattern|deferred_by):`, run by you — by meaning (case 147.4)."
      - old: "Insight was actioned, and that Insight stays live with its pattern in the index, so\na recurrence is caught there at the cost of one index line."
        new: "Insight was actioned, and that Insight stays live with its pattern in its index line, so\na recurrence is caught there at the cost of one Grep line."
    change: "the index lines come from the librarian's own Greps of lessons and insights (case 147.4)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`s; `uv run guppi render` writes the partial into `librarian-guppi.md`
- [ ] read `estimate-synthesis-clusters` (block 147.4): the report of the next run with a lesson entry names the two Greps
```

### Case 147.5 — `rule-documentation`: three inputs

> **when:**
> `guppi render` writes `librarian-guppi.md`.

> **then:**
> "Your inputs are three: the `handoff.md` …, every `materialize.yaml` …, and `vault/wiki/tags.md`; the index lines you compare with are the Greps `rule-index-check` and `rule-synthesis` name"; the four reasons to open a page — as they are.

```then
update:
  - slug: rule-documentation
    contract: changed
    replace:
      - old: "Your inputs are four: the `handoff.md` your dispatch names, `vault/raw/<date>/<hi HHMM>/handoff.md` (the session's folder, case 73), every `materialize.yaml`\nthat `guppi materialize` names on its stdout, the four `vault/wiki/<category>-index.md`\nfiles, and `vault/wiki/tags.md`."
        new: "Your inputs are three: the `handoff.md` your dispatch names, `vault/raw/<date>/<hi HHMM>/handoff.md` (the session's folder, case 73), every `materialize.yaml`\nthat `guppi materialize` names on its stdout, and `vault/wiki/tags.md`; the index lines you compare with are the Greps of the category the index check and the synthesis name, run by you (case 147.5)."
    change: "three inputs; the index lines are the librarian's own Greps, no index file (case 147.5)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes `librarian-guppi.md`; `guppi render --check` exit 0
- [ ] read `estimate-documentation-completes` (block 147.5): the next librarian run reads no `*-index.md` and names its Greps
```

### Case 147.6 — `rule-cleanup`: no index rewrite

> **when:**
> `guppi cleanup` runs.

> **then:**
> The sentence "Then the four indexes are rewritten …" removed; purpose — "Prevents an archived page from staying among the live ones"; `cleanup.py` without the call of the index writer; the tests without the index checks.

```then
update:
  - slug: rule-cleanup
    contract: changed
    set: {purpose: "Prevents an archived page from staying among the live ones"}
    replace:
      - old: "Prevents an archived page from staying among the live ones, or the indexes from\nlagging behind the vault."
        new: "Prevents an archived page from staying among the live ones."
      - old: " Then the four indexes are rewritten with the writer of `guppi index`; an archived Estimate leaves no line, since estimates have none."
        new: ""
    change: "cleanup rewrites no index; the files are gone (case 147.6)"
```

```tasks
- [x] `guppi/cleanup.py`: remove `from guppi.index import plan`, `rewrite_indexes` and its call; the docstring sentence on the indexes
- [x] `tests/test_cleanup.py`: remove the index assertions
- [x] `make test`, `make style`
- [ ] read `estimate-cleanup-moves` (block 147.6): the tests, and the librarian's `cleanup` run writes no index
```

### Case 147.7 — `rule-lint`: `make lint` in two steps

> **when:**
> Someone reads `rule-lint`; `make lint` runs.

> **then:**
> "`make lint` runs it after `render --check`; both only report"; "lint runs with the renderer, in no phase of the session". `contract: same` — the behaviour of `guppi lint` does not change.

```then
update:
  - slug: rule-lint
    contract: same
    replace:
      - old: "`make lint` runs it after `render --check` and `index --check` over the four index files; all\nthree only report, so the Makefile's rule — no target writes to the tree — holds."
        new: "`make lint` runs it after `render --check`; both only report, so the Makefile's rule — no target writes to the tree — holds (case 147.7)."
      - old: "lint runs with the renderer and the indexes, in no phase of the session."
        new: "lint runs with the renderer, in no phase of the session."
    change: "make lint has two steps; no index --check (case 147.7)"
```

```tasks
- [ ] nothing beyond 147.1's Makefile task: the librarian's `generate` applies the `replace`s
```

### Case 147.8 — `index.md` §11 and the glossary

> **when:**
> Someone reads `index.md` or `glossary.md`.

> **then:**
> §11 "The indexes" → "The index lines": the Grep line as the definition, the fields by category, "no file: the line is computed by the reader"; the paragraphs on `estimates`, `decisions` and `ask-guppi` stay with "these indexes" → "these lines"; §10 "against the indexes", "when the indexes reveal" → "against the index lines", "when the index lines reveal". The glossary row "Index, `ask-guppi`": "the Grep of a category's frontmatter, one line per live page …".

```then
update:
  - file: vault/wiki/index.md
    change: "§11 The index lines: one Grep per category — `^(purpose|deferred_by):` over rules and entities, `^(root_cause|deferred_by):` over lessons, `^(pattern|deferred_by):` over insights — gives `<category>/<slug>.md:<field>: <text>`, one line per live page; no file, the reader computes it; §10 'against the indexes' and 'when the indexes reveal' → 'the index lines'; §1 layout: the four `*-index.md` lines (59–63) and the table row `<category>-index.md` (116) removed; §8 line 310 '`insights-index.md`' → 'its index line' (case 147.8, pre-task)"
  - file: vault/wiki/glossary.md
    change: "row Index, ask-guppi: the Grep of a category's frontmatter, one line per live page, never compared across categories; where: §11, rule-ask (case 147.8)"
  - file: vault/wiki/insights/schema.md
    change: "line 31: 'its `pattern` in `insights-index.md`' → 'its `pattern` in its index line' (case 147.8, pre-task)"
```

```tasks
- [x] `vault/wiki/index.md` §11 rewritten by hand as the `change` says; §10 lines 353 and 355; §1 lines 59–63 and 116; §8 line 310
- [x] `vault/wiki/glossary.md` row "Index, `ask-guppi`" by hand
- [x] `vault/wiki/insights/schema.md` line 31 by hand
```

### Case 147.9 — three stale sentences on the indexes

> **given:**
> `rule-render-harness` line 22: "the renderer runs with lint and the indexes"; `rule-ask` Purpose line 22: "the indexes and pages never enter the caller's"; `rule-documentation` line 94: "reads four inputs" (pre-task).

> **when:**
> Someone reads the page.

> **then:**
> "the renderer runs with lint"; "the index lines and pages never enter the caller's"; "reads three inputs". All `contract: same`.

```then
update:
  - slug: rule-render-harness
    contract: same
    replace:
      - old: "the renderer runs with lint and the indexes, in no phase of the session."
        new: "the renderer runs with lint, in no phase of the session."
    change: "no indexes in make lint (case 147.9)"
  - slug: rule-ask
    contract: same
    replace:
      - old: "the searcher's own context: the indexes and pages never enter the caller's."
        new: "the searcher's own context: the index lines and pages never enter the caller's."
    change: "index lines, not index files (case 147.9)"
  - slug: rule-documentation
    replace:
      - old: "It starts empty, reads four inputs, and opens a page only for a reason its frame names."
        new: "It starts empty, reads three inputs, and opens a page only for a reason its frame names."
    change: "three inputs (case 147.9)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the three `replace`s; the renders of 147.2 and 147.5 carry them
```

## Case 148 — the ref fields as `"[[slug]]"`; the `#L` tag

> **context:**
> The ref fields of the frontmatter — `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` on the category pages; `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by` on the Decision pages — are bare slugs. Obsidian takes only `[[slug]]` in a property as a link; the graph, backlinks, `unresolved` and Bases do not see a bare string. The owner uses the graph, backlinks and Bases and sees the structure only through the body sections `generate` duplicates from the fields, and Decision → target not at all. The `#L` tag in the tag pane comes from one line `origin #L<n>` outside a code span in the Criterion of `estimate-materialize-assembles`; `#case-9`, `#case-11`, `#case-13`, `#case-15.x` from three hand-written lines of 2026-09-09 in `log.md`. A pointer like `ledger.md#L122` is no tag: Obsidian does not read a `#` inside a word as one.

> **problem:**
> The scripts read the frontmatter in one place — `pages.read_page` (plus `materialize.page_estimates`, its own parser of the `estimates` field) — and write it in one — `generate.write_page`. Decide: write the ref fields as `"[[slug]]"`, strip the brackets on read, migrate 313 live and 86 archived pages in one run; fix the schemas; remove the four false tags.

> **given:**
> `rule-page-generation` `built`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`, "the only writer to `wiki/`"; `generate.frontmatter()`/`flow()`/`scalar()` — `scalar` quotes a string through `json.dumps` when `NEEDS_QUOTE` matches (a leading `[` does), so `[[a]]` is written quoted; unquoted, YAML reads it as a nested list; `KEY_ORDER` per category.
> **＋** `pages.read_page` — `yaml.safe_load` of the frontmatter; used by lint, index (leaves with 147), cleanup, generate, pretask, archive. `materialize.page_estimates` parses the frontmatter itself and reads `estimates`. `lint.LINK_FIELDS = (parent, children, estimates, target, addressed_by, insight, deferred_by)`; `links_of` reads `props`.
> **＋** Decision pages: `create`/`update`/`delete`/`defer` are lists of slugs "a page, or a Rule-class file such as `case-schema`"; lint: "every slug with a category prefix a live or archived page"; `supersedes`, `superseded_by` are decision slugs.
> **＋** Schemas: `rules/schema.md` `parent` "slug", `children` "ordered list of slugs", `estimates` "list of slugs", `deferred_by` "list of decision slugs"; `entities/schema.md` the same; `estimates/schema.md` `target` "slug of an Entity or Rule"; `lessons/schema.md` `insight` "slug"; `insights/schema.md` `children`, `addressed_by`, `deferred_by`; `decisions/schema.md:16` "Lists of scalars, so Obsidian shows them as lists and links".
> **＋** Obsidian ≥ 1.4: `"[[slug]]"` in a Text/List property is a link; the graph, backlinks, `unresolved` and Bases see it; a name resolves in any folder, the archive included (`rule-cleanup`: "Obsidian resolves a name in any folder"). The owner's graph is filtered `path:wiki`.
> **＋** `origin` (`raw/<date>/<HHMM>/ledger.md#case-N`), `implementation_ref`, `governs` are paths; `tags` are strings; none is a link.
> **＋** The false tags: `vault/wiki/estimates/estimate-materialize-assembles.md:27` "origin #L<n>" (the only live line with a bare `#L`); `vault/wiki/log.md:12–14` "#case-9 to #case-13", "#case-11", "#case-15.1, #case-15.2, #case-15.3" — lines of 09-09, "written by hand". `log.md` is a working file without a schema, written by `generate` and `cleanup`; no hook guards it.
> **－** `cleanup` moves files without rewriting them; the `children`/`estimates` lists it rebuilds go through the writer of `generate` — the brackets appear by themselves. `render.py` reads no frontmatter link.
> **－** Insight 138 (actioned): the derived texts are named — the body sections and lint do not change.

### Case 148.1 — `generate` writes `"[[slug]]"`, the readers strip the brackets, the migration

> **when:**
> `guppi generate` or `guppi cleanup` writes a page; any script reads a page through `pages.read_page` or `materialize.page_estimates`; a one-off migration walks `vault/wiki/` and `vault/archive/`.

> **then:**
> In the written frontmatter every value of a ref field that carries a category prefix is `"[[slug]]"`, a list `["[[a]]", "[[b]]"]`; the fields: `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by`. A slug without a category prefix (a Rule-class file in a Decision list) stays as it was.
> **＋** `read_page` and `page_estimates` strip `[[`/`]]` from these fields; a page without brackets reads the same — the migration is idempotent; lint, cleanup, pretask, materialize, archive change neither code nor contract beyond the two stripping lines.
> **＋** The migration: every page under `wiki/**` and `archive/**` read by `read_page` and written by `write_page`; body, History and key order as before; after it `guppi lint` gives the findings it gave before; `guppi render --check` exit 0; `git diff --stat` shows frontmatter only.
> **＋** Tests: the writer wraps; the reader strips; a page without brackets reads; `frontmatter()` quotes `[[…]]`.
> **＋** In Obsidian after the migration: the backlinks of an Insight are its lessons (in the archive) and its Decision; the backlinks of a Rule are its children, Estimates and Decisions; `unresolved` is empty.
> **－** The body sections stay; no CLI probe.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "Body sections follow the order of the category's `schema.yaml`:"
        new: "A ref field — `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, and on a Decision page `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by` — is written as a quoted wikilink, `\"[[slug]]\"`, a list as `[\"[[a]]\", \"[[b]]\"]`, so Obsidian's graph, backlinks and Bases see the structure; a slug without a category prefix (a Rule-class file in a Decision list) stays bare. `pages.read_page` and `materialize.page_estimates` strip the brackets on read, so every reader sees the slug; a page written without brackets reads the same (case 148.1). Body sections follow the order of the category's `schema.yaml`:"
    change: "ref fields written as quoted wikilinks; read through the brackets; one migration over wiki/ and archive/ (case 148.1)"
```

```tasks
- [x] `guppi/pages.py`: `REF_FIELDS` (the thirteen names) and `slug_of(value)` stripping `[[`/`]]`; `read_page` normalizes those fields (scalar and list) after `safe_load`
- [x] `guppi/generate.py`: `frontmatter()` wraps a value of a `REF_FIELDS` key that carries a category prefix (`PREFIXES` of `materialize`/`lint`, `decision-` included) in `[[…]]`; `scalar` already quotes it
- [x] `guppi/materialize.py`: `page_estimates` strips through `pages.slug_of`
- [x] `guppi/lint.py`: `LINK_FIELDS` imported from `pages.REF_FIELDS` or left as is (read values are already bare)
- [x] `tests/test_generate.py`: a written page carries `parent: "[[rule-x]]"`, `estimates: ["[[estimate-x]]"]`, a Decision `update: ["[[rule-x]]", "case-schema"]`; `tests/test_lint.py` or a new test in `tests/test_pages.py`: `read_page` returns bare slugs for both forms; `tests/test_materialize.py`: `page_estimates` on a bracketed page
- [x] one-off migration, run from the scratchpad: for every `*.md` under `vault/wiki/<category>/` and `vault/archive/**/<category>/` — `read_page` then `write_page` with the same props and sections; `wiki/index.md`, `glossary.md`, `case-schema.md`, `schema.md`, `brief.md`, `sprint.md`, `tags.md`, `log.md` untouched; then `guppi lint` (same findings as before), `guppi render --check` exit 0, `git diff --stat` frontmatter only
- [x] `make test`, `make style`
- [x] read `estimate-generate-writes` (block 148.1): the tests, the migration checks, and in Obsidian the backlinks of one Insight and one Rule
```

### Case 148.2 — the schemas: the form of a ref field

> **when:**
> Someone reads a category's `schema.md`.

> **then:**
> In `rules/`, `entities/`, `estimates/`, `lessons/`, `insights/`, `decisions/schema.md` the form of a ref field is "wikilink `"[[slug]]"`, quoted; the scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2)"; `decisions/schema.md:16` — "Lists of wikilinks, so Obsidian shows them as links".

```then
update:
  - file: vault/wiki/rules/schema.md
    change: "parent, children, estimates, deferred_by: the value is a quoted wikilink \"[[slug]]\" (a list of them); the scripts read the slug through the brackets (case 148.2)"
  - file: vault/wiki/entities/schema.md
    change: "parent, children, estimates, deferred_by: the same wikilink form (case 148.2)"
  - file: vault/wiki/estimates/schema.md
    change: "target: a quoted wikilink \"[[slug]]\" of an Entity or Rule (case 148.2)"
  - file: vault/wiki/lessons/schema.md
    change: "insight: a quoted wikilink \"[[slug]]\" (case 148.2)"
  - file: vault/wiki/insights/schema.md
    change: "children, addressed_by, deferred_by: the wikilink form (case 148.2)"
  - file: vault/wiki/decisions/schema.md
    change: "create, update, delete, defer, supersedes, superseded_by: lists of quoted wikilinks for page slugs, a Rule-class slug bare; line 16 'Lists of scalars, so Obsidian shows them as lists and links' → 'Lists of wikilinks, so Obsidian shows them as links' (case 148.2)"
  - file: vault/wiki/index.md
    change: "§1 example page (lines 87–88): `parent: \"[[entity-discount-rules]]\"`, `estimates: [\"[[estimate-new-client-discount]]\"]` (case 148.2, pre-task)"
```

```tasks
- [x] the six `schema.md` files edited by hand as each `change` says; `schema.yaml` files unchanged (fields, not forms)
- [x] `vault/wiki/index.md` §1 example lines 87–88 by hand
```

### Case 148.3 — the false tags `#L`, `#case-N`

> **when:**
> Obsidian builds the tag pane.

> **then:**
> `estimate-materialize-assembles`, Criterion: "origin #L<n>" → "origin `#L<n>`"; `log.md` lines 12–14: the `#case-…` pointers in a code span. The tags `L`, `case-9`, `case-11`, `case-13`, `case-15.1`…`15.3` are gone.
> **－** The pointers `ledger.md#L<n>` and `#case-N` in History lines do not change: they are no tags.

```then
update:
  - slug: estimate-materialize-assembles
    replace:
      - old: "origin #L<n>; the unparsable line"
        new: "origin `#L<n>`; the unparsable line"
    change: "the bare #L<n> of the Criterion prose in a code span, no Obsidian tag (case 148.3)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`
- [x] one-off, by hand: `vault/wiki/log.md` lines 12–14 — `#case-9 to #case-13`, `#case-11`, `#case-15.1, #case-15.2, #case-15.3` each in a code span
```

## Case 149 — the hub files linked: `[[brief]]`, `[[sprint]]`, `[[index]]`, `[[glossary]]`, the schemas

> **context:**
> In Obsidian's graph `brief.md`, `sprint.md`, `tags.md`, `log.md`, `index.md`, `glossary.md`, `case-schema.md` and the six `schema.md` are orphans: the rules and `index.md` name them in backticks as paths (`vault/wiki/brief.md`), never as `[[brief]]`. The layout of §1 `index.md` is a code block; Obsidian reads no link inside one. Lint checks the wikilinks in the body of a category page against the slugs of live and archived pages — `[[brief]]` would be a `ref` finding.

> **problem:**
> The owner sees the connections by eye through the graph; the hub files are the joints between sessions and agents and should be seen connected. Decide: one place from which every hub file is reached (§1 of `index.md`), a link back from `glossary`/`case-schema` to `[[index]]`, lint accepts a wikilink to a file under `wiki/`, and the four rules whose subject is a hub file name it as a link in their Purpose.

> **given:**
> `index.md` §1 — the layout in a ``` fence: `index.md`, `glossary.md`, `case-schema.md`, `brief.md`, `sprint.md`, `tags.md`, `log.md`, `<category>/schema.yaml schema.md`; the four `*-index.md` leave with 147.8. `glossary.md` first paragraph: "`§N` a section of `index.md`"; `case-schema.md`: "imported into `CLAUDE.md`".
> **＋** `rule-lint` `built`, `estimate-lint-catches`; `check_refs`: `known = set(by_slug) | archived_slugs(wiki)`; `links_of` takes `[[slug]]` from sections outside code spans; `[[a/b]]` is the slug `a/b`; the rule's text: "every ref … as an existing page".
> **＋** Obsidian resolves `[[brief]]` → `wiki/brief.md`, `[[rules/schema]]` → `wiki/rules/schema.md` by path; `[[schema]]` is ambiguous (six files) — by path only.
> **＋** Purpose: `rule-brief` "Prevents the next session from starting without the facts and the flags of this one. The brief is a shop window, not storage …"; `rule-skill-hi` "Prevents a session from being loaded piecemeal by read-tool calls. …"; `rule-documentation` "… the three scripts are called from the frame by name."; `rule-claude-md` "… a change to it is an `update` of one of the two." All prose sections, written by `generate` from ratified `sections`/`replace`.
> **＋** No Render holds a `[[…]]` to a hub file; `.claude/agents/*.md` and the skills read paths.
> **－** `README`, `docs/` outside the vault — outside the Case. Rule-class files (`index`, `glossary`, `case-schema`) — an `update` with `file`, by hand.
> **－** The owner's graph is filtered `path:wiki` — the hub files are in it.

### Case 149.1 — `index.md` §1: links to the hub files

> **when:**
> Someone reads `index.md`; Obsidian builds the graph.

> **then:**
> After the code block of §1 a paragraph: "As links, for the graph: [[glossary]] · [[case-schema]] · [[brief]] · [[sprint]] · [[tags]] · [[log]] · the schemas [[decisions/schema]], [[entities/schema]], [[rules/schema]], [[estimates/schema]], [[lessons/schema]], [[insights/schema]] (case 149.1)." No hub file is an orphan in the graph.

```then
update:
  - file: vault/wiki/index.md
    change: "§1: after the layout code block, one paragraph of wikilinks to the hub files — glossary, case-schema, brief, sprint, tags, log, the six <category>/schema — so none is an orphan in the graph (case 149.1)"
```

```tasks
- [x] `vault/wiki/index.md` §1 by hand: the paragraph after the code block
```

### Case 149.2 — `glossary.md`, `case-schema.md` → `[[index]]`

> **when:**
> Someone reads the file; Obsidian builds the graph.

> **then:**
> `glossary.md`: "`§N` a section of [[index]]"; `case-schema.md`: "imported into `CLAUDE.md` …; the map is [[index]]". `index.md` is not an orphan.

```then
update:
  - file: vault/wiki/glossary.md
    change: "first paragraph: '`§N` a section of `index.md`' → '`§N` a section of [[index]]' (case 149.2)"
  - file: vault/wiki/case-schema.md
    change: "first paragraph ends with '; the map of the vault is [[index]]' (case 149.2)"
```

```tasks
- [x] `vault/wiki/glossary.md` line 3 and `vault/wiki/case-schema.md` line 3 by hand
```

### Case 149.3 — `rule-lint`: a wikilink to a file under `wiki/`

> **when:**
> `guppi lint` checks a `[[…]]` in the body of a page.

> **then:**
> The link resolves when its text is the slug of a live or archived page, the stem of a file `vault/wiki/*.md` (`brief`, `sprint`, `tags`, `log`, `index`, `glossary`, `case-schema`) or the path of a file under `vault/wiki/` without `.md` (`rules/schema`); otherwise a `ref` finding as today.
> **＋** Test: `[[brief]]` and `[[rules/schema]]` in a body — no finding; `[[nowhere]]` — a finding.
> **－** Frontmatter fields — page slugs only, as today.

```then
update:
  - slug: rule-lint
    contract: changed
    replace:
      - old: "every ref (`parent`, `target`, `children`, `estimates`, `insight`) as an existing page,"
        new: "every ref (`parent`, `target`, `children`, `estimates`, `insight`) as an existing page, a `[[…]]` in a body as a live or archived page, or as a file under `vault/wiki/` by its stem (`brief`, `index`, `glossary`, `case-schema`, `sprint`, `tags`, `log`) or its path (`rules/schema`) (case 149.3),"
    change: "a body wikilink may name a hub file under wiki/ by stem or path (case 149.3)"
```

```tasks
- [x] `guppi/lint.py`: `known` extended with the stems of `wiki/*.md` and the paths `<category>/schema` (any `.md` under `wiki/` that is not a category page, as `relative path without suffix`), for `check_refs` only
- [x] `tests/test_lint.py`: `[[brief]]`, `[[rules/schema]]` pass; `[[nowhere]]` fails
- [x] `make test`, `make style`
- [ ] read `estimate-lint-catches` (block 149.3): the tests, and `guppi lint` clean of `ref` on the four rules of 149.4 after the librarian's run
```

### Case 149.4 — four rules name their hub file

> **when:**
> `guppi generate` applies the `replace`; someone reads the Purpose; Obsidian builds the backlinks.

> **then:**
> `rule-brief` Purpose: "Prevents the next session from starting without the facts and the flags of this one, written to [[brief]]. [[brief]] is a shop window, not storage …". `rule-skill-hi` Purpose ends: "It puts [[brief]] and [[sprint]] into the context before the first turn." `rule-documentation` Purpose ends: "The phase ends with [[brief]] written and [[tags]] read." `rule-claude-md` Purpose ends: "The Render imports [[glossary]] and [[case-schema]] and points at [[index]]."
> **＋** History of each: `updated: the hub file linked for the graph (case 149.4)`; `contract: same` — the behaviour does not change.

```then
update:
  - slug: rule-brief
    contract: same
    replace:
      - old: "Prevents the next session from starting without the facts and the flags of this one.\nThe brief is a shop window, not storage:"
        new: "Prevents the next session from starting without the facts and the flags of this one,\nwritten to [[brief]]. [[brief]] is a shop window, not storage:"
    change: "the hub file linked for the graph (case 149.4)"
  - slug: rule-skill-hi
    contract: same
    replace:
      - old: "so no `PreToolUse` hook sees it."
        new: "so no `PreToolUse` hook sees it. It puts [[brief]] and [[sprint]] into the context before the first turn."
    change: "the hub file linked for the graph (case 149.4)"
  - slug: rule-documentation
    replace:
      - old: "the three scripts are called from the frame by name."
        new: "the three scripts are called from the frame by name. The phase ends with [[brief]] written and [[tags]] read."
    change: "the hub file linked for the graph (case 149.4)"
  - slug: rule-claude-md
    contract: same
    replace:
      - old: "a change to it is an `update` of one of the two."
        new: "a change to it is an `update` of one of the two. The Render imports [[glossary]] and [[case-schema]] and points at [[index]]."
    change: "the hub file linked for the graph (case 149.4)"
```

```tasks
- [ ] nothing to code: the librarian's `generate` applies the four `replace`s (149.4); 149.3 must be built before the librarian's lint, or the four pages carry a `ref` finding until it is
```

## Case 150 — `rule-retro`: the flag `disable-model-invocation` removed

> **context:**
> The lesson of O: `retro/SKILL.md` carries `disable-model-invocation: true`; a typed `/retro` is expanded as a prompt, the Skill tool is not called, `guppi gate` does not see it — neither the check of 122 nor the `retro` mark; `rule-event-log` and `gate.MARKS` promise three marks, the second never appears.

> **problem:**
> The owner allows the agent to start the Retro itself after Work Mode: the Retro stops at the lessons and the readings anyway, and `/handoff` stands behind the gate. Decide: remove the flag — one mechanism for the three skills, no code change.

> **given:**
> `rule-retro` `built`, `enforcement: render`, `governs: .claude/skills/retro/SKILL.md`, `estimates: [estimate-retro-loads]` `passed` (126); the Render, line 31: `disable-model-invocation: true`; the body: `Tests: !`make test``, `Style: !`make style``, `Ledger: !`uv run guppi tail``.
> **＋** `rule-event-log` `built`: the marks `pretask`, `retro`, `handoff` are written by `guppi gate` on `PreToolUse Skill`; `gate.MARKS` holds `retro`; `test_retro_and_handoff_leave_their_marks` expects both marks.
> **＋** `gate.py`: the gate of 122 — "any skill while the Spec is ahead of the ledger"; `/handoff` and `/pre-task` without the flag pass through the Skill tool and get their PostToolUse lines and marks (sessions N, O).
> **＋** `rule-retro-commit`: `/handoff` on a dirty tree is refused; the Retro calls `/handoff` through the Skill tool.
> **＋** The lesson of O stays `new`: the fact about the flag holds; after this Case it is history.
> **－** The glossary "`/retro` (the person)" does not change: the person can still type `/retro`; the agent may now call it too — after Work Mode, when the tasks of the Spec are ticked.
> **－** `rule-event-log`, `gate.py`, the tests — unchanged.

> **when:**
> `guppi render` writes `.claude/skills/retro/SKILL.md`; then the person types `/retro` or the agent calls the skill `retro`.

> **then:**
> The frontmatter of `SKILL.md` without `disable-model-invocation`; the call goes through the Skill tool: `guppi gate` checks the Spec against the ledger (122), leaves the mark `- HH:MM:SS <stamp> retro`, the event log gets `tool Skill: retro` and the PostToolUse lines.
> **＋** The agent may call `/retro` itself when the tasks of the Spec are ticked; the Retro stops at the lessons and the readings as before; `/handoff` behind the gate of the tree and of 122.
> **－** No other page and no line of code changes.
> **－** The Frontier line F8 closes on this Case; the live refusal of 122 — a reading at the event.

```then
update:
  - slug: rule-retro
    contract: changed
    replace:
      - old: "description: Review this session's work — tests, style, the ledger — before the commit and the handoff.\ndisable-model-invocation: true\n---"
        new: "description: Review this session's work — tests, style, the ledger — before the commit and the handoff.\n---"
    change: "disable-model-invocation dropped: a typed or agent-called /retro passes the Skill tool, so guppi gate sees it and writes the retro mark (case 150)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes `.claude/skills/retro/SKILL.md`; `guppi render --check` exit 0
- [ ] read `estimate-retro-loads` (block 150): the next `/retro` — a `tool Skill: retro` line and a stamped `retro` mark in the event log
```

### Case 150.1 — `rule-claude-md`: "`/retro` (the person)"

> **given:**
> The Render, line 62: "`/retro` (the person), `/handoff` (the agent, …)". After 150 the agent may call `/retro` itself (pre-task).

> **when:**
> `guppi render` writes `CLAUDE.md`.

> **then:**
> "`/retro` (the person, or the agent once the Spec's tasks are ticked), `/handoff` (the agent, …)". `contract: same`.

```then
update:
  - slug: rule-claude-md
    contract: same
    replace:
      - old: "`/retro` (the person), `/handoff` (the"
        new: "`/retro` (the person, or the agent once the Spec's tasks are ticked), `/handoff` (the"
    change: "the agent may call /retro after Work Mode (case 150.1)"
```

```tasks
- [ ] the librarian's `generate` applies the `replace`; `uv run guppi render` writes `CLAUDE.md`; `guppi render --check` exit 0
```

## Case 153 — `rule-harness`: the Purpose and the Method after 145.1 and 147.1

> **context:**
> `rule-harness` Purpose: "Four rules belong to no phase of the session: … lint and the indexes. They run together in `make lint` … the indexes before the pages. Three more belong here and run in no pipeline …"; `estimate-harness-pipeline` `passed`, its Criterion and Method name "then index --check" and `tests/test_index.py`. 145.2 changes `children` only (pre-task).

> **problem:**
> After 147.1 there is no index step and after 145.1 there is a fourth child outside `make lint`; the Purpose and the Method are wrong twice. Decide: the Purpose rewritten, the Method without `tests/test_index.py`.

> **given:**
> `rule-harness` MOC `built`, `estimates: [estimate-harness-pipeline]`; Makefile `test-harness` loses `tests/test_index.py` by 147.1.
> **－** A MOC's `update` with `contract: changed` appends the block and sets the Estimate `pending`; `method` rewrites its Method.

> **when:**
> `make lint` and `make test-harness` run; someone reads `rule-harness`.

> **then:**
> The Purpose: "Three rules belong to no phase of the session: the renderer, the page `.claude/settings.json` is assembled from, and lint. They run together in `make lint`, in this order: the harness files are checked against their pages before the pages. Four more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, and the pinned clock of the tests (cases 59.6, 59.8, 127, 145.1)."
> **＋** `estimate-harness-pipeline`: block 153, `pending`; Method: "`make test-harness` over `tests/test_render.py` and `tests/test_lint.py`; the live reading of `make lint` by hand".

```then
update:
  - slug: rule-harness
    contract: changed
    method: "`make test-harness` over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand"
    replace:
      - old: "Four rules belong to no phase of the session: the renderer, the page\n`.claude/settings.json` is assembled from, lint and the indexes. They run together in `make lint`, in this order, and\nthe order is the content: the harness files are checked against their pages before\nthe indexes, the indexes before the pages. Three more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, and the page `CLAUDE.md` is rendered from (cases 59.6, 59.8, 127)."
        new: "Three rules belong to no phase of the session: the renderer, the page\n`.claude/settings.json` is assembled from, and lint. They run together in `make lint`, in this order: the harness files are checked against their pages before the pages. Four more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, and the pinned clock of the tests (cases 59.6, 59.8, 127, 145.1)."
    change: "three rules in make lint, four outside it; the pipeline's Method without tests/test_index.py (case 153)"
```

```tasks
- [ ] nothing beyond 147.1's Makefile task: the librarian's `generate` applies the `replace` and the Method
- [ ] read `estimate-harness-pipeline` (block 153): `make test-harness` green over the two files, `make lint` by hand
```

## Case 151 — `generate` does not apply an entry with `superseded_by`

> **context:**
> Entry 112.6 in `raw/2026-09-14/0747/materialize.yaml`: a `replace` whose text was not found on the page — `failed`; Case 130.1 made the same change and marked the entry `superseded_by: '130.1'`. `generate` skips only `applied`, so it retries 112.6 every run — three runs in a row, one stderr line and exit 1. `rule-raw-archive` (130.2) counts `superseded_by` as done — the unit is not held; it goes to the archive at the first run on a later date.

> **problem:**
> A hole in the rule, not in the data: a superseded entry must not be applied — a later Case did its work. But the Decision page of the earlier Case is needed: the later one names it in `supersedes`, and the cascade sets it `superseded` → `archived`. Decide: `generate` skips the action of an entry with `superseded_by` and still writes the Decision page of its Case.

> **given:**
> `rule-page-generation` `built`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`; its text: "An entry that fails … is reported on stderr, marked `failed` and skipped; the rest apply; the exit code is 1"; "a stale `failed` mark is dropped on apply (case 53.3)". Code `apply`: `if entry.get("applied"): continue`; then `apply_decision` for the entry's Case; then the action.
> **＋** `materialize` (130.2): `{supersedes:case N}` sets `superseded_by` on the entries of Case N in any unit's yaml and in its `decisions`. `generate.decision`: the later page carries `supersedes: [decision-case-N]`; the earlier gets `superseded_by` and `status: superseded`; the cascade — `archived`.
> **＋** `rule-raw-archive`: a unit is done when every entry is `applied` or `superseded_by`; `archive.kept_reason` counts so.
> **＋** Lint: the `supersedes` of a Decision page must name a live or archived page — the Decision of the earlier Case must exist.
> **＋** Entry 112.6: `failed` × 3, `superseded_by: '130.1'`; the Decision page of 112.6 exists since session 0747 (the cascade of 130.1 archived it).
> **－** An entry superseded before its first application (a Case ratified and superseded in one session) would be applied today — not after this Case; its Decision page is written.
> **－** 142.1/142.2 (an entry without `kind` with `failed` from `materialize`) — another class, no overlap.

> **when:**
> `guppi generate` reaches an entry with `superseded_by`.

> **then:**
> The action of the entry is not done, stderr is empty, the exit code is not changed; the Decision page of its Case is written when it does not exist yet (`superseded`, the cascade — `archived`); `failed` and `superseded_by` on the entry stay as they are.
> **＋** The rule's text: "An entry with `superseded_by` is not applied — a later Case did its work — and leaves no line; its Case's Decision page is still written, `superseded`, and archived by the cascade (case 151)."
> **＋** Tests: an entry `failed` + `superseded_by` — no stderr, exit 0, the Decision page exists, the target untouched; an entry `superseded_by` without `applied` in one yaml with the superseding one — both Decision pages, the earlier `superseded`.
> **＋** The librarian's run of this session: `generate` over `0747` is silent; 112.6 is out of the Flags.
> **－** `materialize`, `archive`, `cleanup` do not change.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "No entry ends the run."
        new: "No entry ends the run. An entry with `superseded_by` is not applied — a later Case did its work — and leaves no line; its Case's Decision page is still written, `superseded`, and archived by the cascade (case 151)."
    change: "an entry with superseded_by is skipped without a line; its Decision page still written (case 151)"
```

```tasks
- [x] `guppi/generate.py`: in `apply`, an entry with `superseded_by` and no `applied` — `apply_decision` for its Case when the page does not exist, then `continue`; no stderr, no `failed` change
- [x] `tests/test_generate.py`: the two tests of the `then`
- [x] `make test`, `make style`
- [ ] read `estimate-generate-writes` (block 151): the tests, and the librarian's `generate` over `raw/2026-09-14/0747` with an empty stderr
```

Note for Work Mode: 142.2 and 151 both add a sentence after "No entry ends the run." in `rule-page-generation`; the librarian applies them in ledger order (142.2 first), and the second `replace` must target the text as it stands after the first — the `old` of 151 stays unique ("No entry ends the run." occurs once), so both apply.

## Deferred

## Case 152 — Slice 3b: Work Mode, deferred once more

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, 107, 116, 129, 141, without `kind`, `estimates` or `tags`; the two lint orphans and 8 `schema` findings. Case 141 (session O) deferred Slice 3b for the tenth time.

> **problem:**
> The owner opened session P on the readings due, the four open Insights and the Obsidian direction — Cases 142–151 — and set Slice 3b aside at `/hi` to close the other open items first. The two pages stay placeholders one more session; the postponement count goes to 11.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case; the Plan Mode of a session of its own
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case; the Plan Mode of a session of its own
```

## Case 154 — `rule-ask`: one question per `create` without `ref` and at pre-task, not per Case

> **context:**
> `rule-ask` says "One short question per Case"; `CLAUDE.md` asks the vault before a `create` without a `ref` and at pre-task. Session P dispatched `ask-guppi` six times — before Cases 142, 143, 144, 145, before the Obsidian direction (147) and at pre-task — about 355k tokens in subagents; four of the six were `update`s with a `ref`, where the Insight page and two greps would have given the `given`.

> **problem:**
> The owner finds six dispatches dearer than one and of less use. The main agent's practice from now: `ask-guppi` before a `create` without `ref` and at pre-task; for an `update` with `ref`, the page and a grep; the rule's text still says "per Case". Decide at the next Plan Mode whether `rule-ask`'s clause follows the practice.

```then
defer:
  - slug: rule-ask
    type: rule
    purpose: replace "One short question per Case" by "one question before a create without a ref, and one at pre-task; an update with a ref reads the page itself" — the Render's description line and the Purpose; a Case at the next Plan Mode
```

## Case 146 — `rule-lint`: an `actioned` Insight is not an orphan

> **context:**
> After session O `guppi lint` reports six new `orphan` findings: the six Insights actioned by 134, 135, 136.4, 137, 138, 139.2; after this session four more (142.3, 143, 144.3, 145.3). An orphan in `rule-lint` is a live entity, rule, estimate or insight no other live page names in its frontmatter. An Insight is named by its children's `insight` field; on `actioned` the cascade of 104.2 archives the children, and the Insight is left with no live inbound link by construction — while `rule-synthesis` and `index.md` §8 keep it live so a recurrence is caught by its `pattern` in the index.

> **problem:**
> Two ratified norms — the children of an actioned Insight are archived; an actioned Insight stays live — together guarantee a third's finding, `orphan`, which catches nothing: the page has a pointer out (`addressed_by`) and its Decision page names it under `update`. The owner opened a wider question first: Obsidian's own graph sees the actioned Insight as connected (its `## Children` wikilinks reach the archived pages, its `## Addressed by` the Decision), and the notion of an orphan may follow Obsidian's once the frontmatter refs are wikilinks (Case 147). Which of the two definitions lint keeps is decided after that.

```then
defer:
  - slug: rule-lint
    type: rule
    purpose: decide whether an actioned Insight is exempt from the orphan check, or whether lint adopts Obsidian's notion of an orphan (no inbound link of any kind, decision pages included) once frontmatter refs are wikilinks (147); a Case at the next Plan Mode
```
