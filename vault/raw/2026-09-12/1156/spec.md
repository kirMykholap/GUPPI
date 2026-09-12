<!-- approved 15:32:24 · session d08a5ca5 -->

# Spec — 2026-09-12, session J

## Case 70 — a lesson that names a fault that did not happen

> **context:**
> Session I wrote `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`
> with `root_cause: not yet found`, and the librarian clustered it with session F's lesson
> under `insight-ledger-hook-reads-only-the-final-text`. The reading of F24 (session J)
> shows the trigger is false: no LEDGER block of session I was dropped; the eight Cases
> never had one. The finding is recorded as
> `lesson-ledger-preview-in-ratification-taken-for-the-record`.

> **problem:**
> A Lesson page whose trigger and root cause are wrong stays live, in the index and in
> `ask-guppi`'s answers, and holds an Insight at severity 2 over a pattern that has one
> real member. The schema has no state for a lesson found wrong.

> **given:**
> `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`: `status: clustered`,
> `insight: insight-ledger-hook-reads-only-the-final-text`, origin `raw/2026-09-12/ledger.md#L101`.
> **＋** Referenced by that Insight (`children`, severity 2), by
> `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (History line), by
> `lessons-index.md`, `log.md` and `brief.md`.
> **＋** §5: `delete` sets `status: deleted` after an impact analysis, the librarian
> archives, `origin` is kept; §8: an Insight is never a Decision target; `severity` is
> recomputed by lint as the count of children not archived.
> **＋** `guppi pretask --check` (case 59.1) reports an item of a `then` block with no
> decision line of its Case, so the preview-for-record mistake is caught in the same session.
> **－** `lessons/schema.md` has `archived` only for a lesson whose Insight is `actioned`;
> a lesson archived by `delete` is a case the schema does not name, and this Case does not
> change the schema.

> **when:**
> The librarian runs `guppi generate` and `guppi cleanup` on this session's yaml.

> **then:**
> The lesson page carries `status: deleted` in the yaml and moves to
> `vault/archived/migration/2026-09-12/lessons/`; its line leaves `lessons-index.md`.
> **＋** `insight-ledger-hook-reads-only-the-final-text` keeps the slug in `children`;
> lint recomputes `severity` to 1; the librarian's brief names the Insight as one to judge.
> **＋** The new lesson `lesson-ledger-preview-in-ratification-taken-for-the-record` is
> generated `new` and compared at synthesis with the children of
> `insight-ledger-line-written-unchecked`.
> **－** `guppi/ledger.py` and `rule-ledger-write` are not changed.

```then
delete:
  - slug: lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn
    impact: |
      Its trigger is false (the reading of F24, session J): every LEDGER block of session I
      was the last text of its turn and every line reached the ledger; the eight Cases had
      no block. Referenced by `insight-ledger-hook-reads-only-the-final-text` (children,
      severity 2 → 1 by lint), by the History of
      `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, by `lessons-index.md`,
      `log.md` and `brief.md`. The Insight is the librarian's to judge at synthesis; the
      ledger lines of session I stay as the trace. No code and no Rule page change.
```

```tasks
- [x] no file of the repository changes for this Case in Work Mode; the librarian's `generate` and `cleanup` apply the delete
- [x] tests/test_ledger.py: one test that a LEDGER block in a text message followed by a tool_use record of the same turn is collected from the transcript (inside the criterion of `estimate-ledger-write-lifts`, no contract change)
- [ ] the handoff names `insight-ledger-hook-reads-only-the-final-text` (one live child after the delete) and `lesson-ledger-preview-in-ratification-taken-for-the-record` (compare with the children of `insight-ledger-line-written-unchecked`) for the librarian
```

## Case 71 — two Estimates signed in session I and never logged

> **context:**
> Cases 59.6 and 59.8 (session I) created `rule-governed-files-hook` and `rule-claude-md`,
> each with a nested `estimate` in its `then` block: `estimate-governed-files-hook-refuses`
> and `estimate-claude-md-rendered`, criterion and method ratified there. Neither got a
> paired `create` line, so neither has a yaml entry or a page; both Rule pages carry
> `estimates: []` and cannot become `built`. The brief names this under "What the next
> session does first", item 3. Recorded as
> `lesson-pretask-nested-estimate-exempt-from-the-line-check`.

> **problem:**
> Two decisions: how the two pages come to exist now, and how a Leaf's nested Estimate
> reaches the yaml without a step the agent can forget.

> **given:**
> `index.md` §5: a Leaf `create` also logs a paired `create` for its Estimate; §3 "Paired
> Estimate on create" shows the two lines. `materialize.find_item` reads the nested block
> only for a decision line with the Estimate's slug (test
> `test_the_nested_estimate_is_its_own_create_entry`, seeded with that line).
> **＋** `pretask.items_of` marks a nested `estimate` as `nested: True`, "covered by its
> parent's line since case 53.1"; Case 53.1 says "a lesson entry writes the lesson only;
> no paired Estimate" and nothing about Leaf creates.
> **＋** `rule-pretask` Render: "It prints one line for every decision line of this session
> that has no item under its own Case in the plan, for every item that has no line, …".
> `estimate-pretask-reconciles` Criterion: "a line without an item, an item without a
> line, and an item under another sub-case's heading are each one finding, exit 1".
> **＋** `generate` on a `create` of category `estimates` with `ref` appends the slug to
> the target's `estimates` and its `## Estimates` section (`generate.py` lines 278–281,
> 335–341). Both slugs are free in `wiki/` and `archived/`.
> **＋** Tags: `rule-governed-files-hook` [hooks, harness, render], `rule-claude-md`
> [harness, render]; the Estimates take their Rule's tags, as a nested one would.
> **－** Case 68 (deferred) is the other wording of `rule-pretask`, the `defer`-only
> exemption; this Case does not touch it.

### Case 71.1 — the two pages, born of this Case with the text of 59.6 and 59.8

> **when:**
> The librarian runs `guppi materialize`, `generate` and `cleanup` on this session's yaml.

> **then:**
> `estimate-governed-files-hook-refuses` exists, `pending`, `target:
> rule-governed-files-hook`, Criterion and Method the text of 59.6; `rule-governed-files-hook`
> lists it in `estimates` and `## Estimates`.
> **＋** `estimate-claude-md-rendered` exists, `pending`, `target: rule-claude-md`,
> Criterion and Method the text of 59.8; `rule-claude-md` lists it.
> **＋** Both pages carry `origin: raw/2026-09-12/ledger.md#case-71.1`; their Context
> section names 59.6 and 59.8 as the Cases that signed the criterion.
> **－** The pages of `decision-case-59.6` and `decision-case-59.8` are not changed.

```then
create:
  - slug: estimate-governed-files-hook-refuses
    type: estimate
    kind: QA
    tags: [hooks, harness, render]
    context: |
      Signed as the nested Estimate of `rule-governed-files-hook` in Case 59.6 (session I,
      2026-09-12); no paired `create` line was written, so the page is born of Case 71.1
      with the criterion of 59.6 unchanged.
    criterion: |
      Unit, against a temp vault with one governing page per file: an `Edit`, `Write` or
      `MultiEdit` on a governed path exits 2 naming the rule and the file; another tool,
      an ungoverned path and an unreadable payload exit 0. Live: one probe in the session
      that registers the hook —
      an `Edit` on `.claude/skills/hi/SKILL.md` refused, the rule named, the call in the
      event log.
    method: |
      pytest in `tests/test_guard.py` with piped payloads; the live probe once by hand,
      written into the estimate line.
  - slug: estimate-claude-md-rendered
    type: estimate
    kind: QA
    tags: [harness, render]
    context: |
      Signed as the nested Estimate of `rule-claude-md` in Case 59.8 (session I,
      2026-09-12), kept by Case 66; no paired `create` line was written, so the page is
      born of Case 71.1 with the criterion of 59.8 unchanged.
    criterion: |
      After `uv run guppi render`, `CLAUDE.md` equals the Render of `rule-claude-md` with
      the text of `rule-case-protocol` between its markers; the first such render leaves
      a `git diff` of marker lines only; `guppi render --check` then exits 0; every
      session after it loads the same text, the two `@` imports expanded.
    method: |
      the live reading at the first render after the page exists, by hand, written into
      the estimate line; `tests/test_render.py` already pins a full page with a partial
      child.
```

```tasks
- [x] no file of the repository changes for this Case in Work Mode; the librarian's `materialize` and `generate` create the two pages and list them on their Rules
- [x] take the reading of estimate-governed-files-hook-refuses: unit (`tests/test_guard.py`) and the live probe, one refused Edit on `.claude/skills/hi/SKILL.md` in this session, after the render registers the hook; write the estimate line
- [x] take the reading of estimate-claude-md-rendered at this session's first `uv run guppi render`; write the estimate line
```

## Case 72 — the Estimate is derived from the Case

> **context:**
> Cases 70 and 71 showed the seam: the Estimate of a Leaf is signed in the `then` block
> but reaches the vault only through a second ledger line the agent writes by hand, its
> criterion is a second wording of the Case's `when` and `then`, and a contract change
> rewrites it by hand with `replace` (the class of
> `insight-workflow-contract-change-leaves-its-derived-text-stale`). The owner and the
> agent settled the scheme in session J: one Leaf, one Estimate; the Case's `when` and
> `then` are its Criterion, paragraph by Case; the Case's `problem` is its Context, once;
> the agent writes `method` on a `create` and `contract: same|changed` on an `update`,
> nothing else; the scripts do the rest.

> **problem:**
> Six pieces of the harness say or do the old thing: the Case form (`case-schema.md`,
> `index.md`, the glossary, the Render of `rule-case-protocol`), the two page schemas
> (estimates, decisions), `materialize`, `generate`, `pretask --check` and `lint`. Each is
> one contract; each is a sub-case below.

> **given:**
> `case-schema.md`: "The Estimate's criterion is the `when` and `then` of the Case, copied
> without change" — never done; a Leaf `create` holds a nested `estimate` with its own
> `criterion` and `method`; "An `update` that changes a Leaf's contract carries, in the
> same block, the `update` of its Estimate". `index.md` §3 "Paired Estimate on create"
> shows two lines; §5 row `create — (Leaf)`: "Also log a paired `create` for its
> Estimate"; §7: a contract change "updates the `Criterion` of that page's existing
> Estimate ... in the same Case". Glossary row `Types`: "a Leaf brings a paired Estimate
> `create`".
> **＋** `estimates/schema.md` body: Context, Criterion, Method required, Result optional,
> "`Result` is overwritten, not appended". `decisions/schema.md` body: Context, Problem,
> Given, When; "What was decided (`then`) lives on the target pages, not here."
> **＋** `materialize.find_item` reads a nested `estimate` only for a line with its slug;
> `_lift_item` maps `context`, `criterion`, `method` into sections. `generate` writes an
> Estimate from a `create` entry with `ref`, appends the slug to the target's `estimates`
> (lines 278–281, 335–341), and on an `estimate` entry overwrites `## Result`.
> `pretask.items_of` exempts a nested estimate; `pretask --check` has no finding for a
> missing `method`, a missing `contract`, or two contracts in one Case. `lint` requires
> `## When` on a decision page with a kind other than `defer`.
> **＋** Slugs in `wiki/estimates/` are hand-named; a derived slug
> `estimate-<target minus its prefix>` collides with none of the 34.
> **＋** The Rule pages touched: `rule-case-protocol` (render, governs `CLAUDE.md`,
> `estimate-case-protocol-loaded`), `rule-materialize` (check, `estimate-materialize-assembles`),
> `rule-page-generation` (check, `estimate-generate-writes`), `rule-pretask` (render,
> `estimate-pretask-reconciles`), `rule-lint` (check, `estimate-lint-catches`).
> **－** Case 53.2 stays: a second Estimate on one target only for a condition that fails
> and is fixed apart, named by `slug` in that Case. Case 68 (deferred, the `defer`-only
> wording of `rule-pretask`) is not taken up here.
> **－** MOC pages get an Estimate the same way, only when a Case gives them `method`;
> without it, none.

### Case 72.1 — the form of the Case: `method` and `contract` in the `then` block

> **when:**
> The agent writes the `then` block of a Case, and someone reads `case-schema.md`,
> `index.md` §3, §5, §7, the glossary or the Case protocol in `CLAUDE.md`.

> **then:**
> A `create` of a Leaf carries `method` (required), `kind` (`QA` default) and `slug`
> (only on a collision); no nested `estimate`, no paired line.
> **＋** An `update` of a Leaf carries `contract: same` or `contract: changed`; `method`
> only when the way of checking changes.
> **＋** The texts say: `when` and `then` are the Criterion paragraph of the Estimate,
> `problem` its Context at birth, `{supersedes:case N}` removes the paragraph of case N,
> one contract per Case or sub-case.
> **－** `recommend`, `ratification` and the section order do not change.

```then
update:
  - file: vault/wiki/case-schema.md
    change: "the then block (case 72.1): a Leaf create carries method (required), kind (QA by default) and slug (only when the derived slug collides); no nested estimate, no paired line; a Leaf update carries contract: same or contract: changed, and method only when the way of checking changes; the example block shows method and contract; the section 'when and then are the criterion' says the scripts copy them as the ### case N block of the Estimate's Criterion, problem as its Context at birth, and that {supersedes:case N} removes the block of case N; the sentence 'An update that changes a Leaf's contract carries, in the same block, the update of its Estimate' is replaced by contract: changed; one contract per Case or sub-case, pre-task asks to split otherwise; the Estimate slug is estimate-<target minus its prefix>"
  - file: vault/wiki/index.md
    change: "§3 'Paired Estimate on create' rewritten: a Leaf create writes method in its then item, the Estimate is derived, one ledger line; §5 row 'create — (Leaf)': its method in the then block makes the Estimate's create entry, no line of its own; §7: a contract change is contract: changed on the update, the Case's when and then are appended as a ### case N block and the Estimate goes pending, a supersedes removes the block of case N, Context is the problem of the Case that made the Estimate, the slug is estimate-<target minus its prefix>, a second Estimate only by case 53.2 with a slug named in the Case (case 72.1)"
  - file: vault/wiki/glossary.md
    change: "row Types: '(a Leaf brings its Estimate through method in the then block)'; row Estimate: its Criterion is the when and then of its Cases, one block per Case, its Context the problem of the Case that made it; row 'ref, slug, supersedes': a supersedes also removes the Case's block from the Estimate's Criterion (case 72.1)"
  - slug: rule-case-protocol
    replace:
      - old: "`when` and `then` together are the criterion of the Estimate the Case creates."
        new: "`when` and `then` together are the criterion of the Estimate the Case creates or changes: the scripts copy them as its `### case N` block and `problem` as its Context at birth; a Leaf `create` carries `method`, a Leaf `update` `contract: same` or `changed`; one contract per Case or sub-case."
      - old: "The page content itself — fields, prose sections, the Estimate — is a YAML"
        new: "The page content itself — fields, prose sections, the `method` of its check — is a YAML"
    change: "the Estimate is derived from the Case: when and then as its Criterion block, method on a create, contract on an update (case 72.1)"
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "without a read call; and a reply"
        new: "without a read call, and the `then` block of a Leaf `create` it writes carries `method` and no nested `estimate` (case 72.1); and a reply"
    set: {status: pending}
    change: "the then block form of case 72.1 joins the criterion; pending for the next session's reading"
```

```tasks
- [x] vault/wiki/case-schema.md: the then block form (method, kind, slug on collision; contract on a Leaf update), the example, the criterion section, the contract-change sentence, one contract per Case
- [x] vault/wiki/index.md: §3 Paired Estimate on create, §5 row create — (Leaf), §7 Estimates
- [x] vault/wiki/glossary.md: rows Types, Estimate, ref/slug/supersedes
- [ ] rule-case-protocol and estimate-case-protocol-loaded change at the librarian's run; CLAUDE.md follows at the next session's render (governed)
- [ ] take the reading of estimate-case-protocol-loaded at the next session's start; write the estimate line
```

### Case 72.2 — the two schemas: what an Estimate page and a Decision page hold

> **when:**
> Someone reads `estimates/schema.md` or `decisions/schema.md` (and their yaml twins);
> lint and generate read them.

> **then:**
> Estimate body: `## Context` written once from the Case's `problem`, never by an
> update; `## Criterion` is one block per Case, `### case N` then `When` and `Then`
> verbatim with their operands, in ledger order; `## Method` from the Case; `## Result`
> as before.
> **＋** Decision body: `## Context`, `## Problem`, `## Given`, no `## When`;
> `## Criterion` holds `[[estimate-x]] § case N` for every Estimate the Case shaped;
> `## Note` as before.
> **－** Pages written before this Case keep their sections; lint accepts both shapes
> (72.6).

```then
update:
  - file: vault/wiki/estimates/schema.md
    change: "Body: ## Context is written once, from the problem of the Case that made the Estimate, and no update touches it; ## Criterion is one block per Case — ### case N, then When and Then verbatim with their operands — in ledger order, a supersedes removes the block of case N; ## Method is the method of the Case; ## Result as before; the paragraph 'Result is overwritten, not appended' gains 'Criterion is appended, block by Case' (case 72.2)"
  - file: vault/wiki/estimates/schema.yaml
    change: "Criterion may hold ### case N sub-blocks; Context, Criterion, Method stay required (case 72.2)"
  - file: vault/wiki/decisions/schema.md
    change: "Body table: the ## When row is removed for pages written after case 72 (earlier pages keep theirs); a ## Criterion row — when the Case shaped an Estimate, one line per Estimate, [[estimate-x]] § case N; the sentence 'What was decided (then) lives on the target pages, not here' moves to the Criterion row as 'when and then live on the Estimate, the then block on the target' (case 72.2)"
  - file: vault/wiki/decisions/schema.yaml
    change: "When no longer required; Criterion optional (case 72.2)"
```

```tasks
- [x] vault/wiki/estimates/schema.md and schema.yaml: Context once, Criterion by Case, Method
- [x] vault/wiki/decisions/schema.md and schema.yaml: no When, a Criterion row
```

### Case 72.3 — `materialize` derives the Estimate entries from the Case

> **when:**
> `guppi materialize` reads a `create` line whose `then` item carries `method`, or an
> `update` line whose item carries `contract: changed`, or a line with `{supersedes:case N}`.

> **then:**
> The `create` yields a second entry: category `estimates`, slug `estimate-<target minus
> prefix>` or the item's `slug`, `ref` the target, `tags` the target's, `origin` and
> `decision` the line's, sections Context (the Case's `problem`), Criterion (the Case's
> `when` and `then` as one `### case N` block), Method; no line of its own.
> **＋** The `update` with `changed` yields an `update` entry of the target's Estimate:
> a Criterion block appended, `set: {status: pending}`, Method replaced when given.
> **＋** A `supersedes` yields a removal of the `### case N` block from that Estimate.
> **＋** The decision group carries `criterion: [{estimate, case}]` for the page's link.
> **－** `contract: same` yields nothing; a nested `estimate` in an old Spec is read as
> before, for old ledgers.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "A Leaf's nested `estimate` becomes its own `create` entry; a standalone estimate `create` with `ref` maps `context`, `criterion` and `method` into `sections` the same way, so the page gets its Criterion and Method sections whichever way it was born."
        new: "A Leaf `create` whose item carries `method` yields a second entry for its Estimate, with no line of its own (case 72.3): category `estimates`, slug `estimate-<target minus its prefix>` or the item's `slug`, `ref` the target, `tags` the target's, `origin` and `decision` the line's, sections Context (the Case's `problem`), Criterion (`### case N`, then the Case's `when` and `then` verbatim with their operands) and Method. An `update` of a Leaf whose item carries `contract: changed` yields an `update` entry of the target's Estimate: `criterion_block` (`### case N` with `when` and `then`), `set: {status: pending}`, `sections: {Method}` when the item carries `method`; `contract: same` yields nothing. A line with `{supersedes:case N}` also yields a `remove_criterion` entry for the Estimate case N shaped. The decision entry carries `criterion`, one `{estimate, case}` per Estimate the Case shaped. A nested `estimate` in an older Spec becomes its own `create` entry as before, for a line with its slug; a standalone estimate `create` with `ref` maps `context`, `criterion` and `method` into `sections` the same way, so the page gets its Criterion and Method sections whichever way it was born."
    change: "a Leaf create with method and an update with contract: changed yield the Estimate's entries; supersedes removes a criterion block; the decision entry names the Estimates shaped (case 72.3)"
  - slug: estimate-materialize-assembles
    replace:
      - old: "the nested estimate is its own create entry;"
        new: "the nested estimate is its own create entry; a Leaf create with method yields its Estimate's create entry with the derived slug, ref, tags, Context from problem, Criterion as a ### case N block of when and then, and Method; an update with contract: changed yields an update entry of the target's Estimate with the criterion block and status pending, contract: same yields none; a supersedes yields the removal of the block of case N; the decision entry names the Estimates the Case shaped;"
    set: {status: pending}
    change: "the derived Estimate entries of case 72.3 join the criterion; pending until the unit reading"
```

```tasks
- [x] guppi/materialize.py: the derived create entry from a Leaf create with method (slug, ref, tags, Context, Criterion block, Method); the update entry from contract: changed (criterion_block, pending, Method); remove_criterion from a supersedes; criterion on the decision entry; the nested estimate of an older Spec as before
- [x] tests/test_materialize.py: one test per clause above, against the temp Spec and ledger
- [x] take the reading of estimate-materialize-assembles on the unit suite; write the estimate line
```

### Case 72.4 — `generate` writes the derived Estimate and the Decision link

> **when:**
> `guppi generate` applies an entry of 72.3.

> **then:**
> A derived `create` writes the Estimate page (`pending`, `target`, Context, Criterion,
> Method, no Result), appends the slug to the target's `estimates` and `## Estimates`,
> History `created`.
> **＋** A derived `update` appends the `### case N` block to `## Criterion`, sets
> `pending`, replaces `## Method` when given, History `criterion: case N added`; a removal
> deletes the block, History `criterion: case N removed`.
> **＋** A decision page gets `## Criterion` links and no `## When`.
> **－** Existing pages are not rewritten; the cascade to `built` is unchanged.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "A `create` with `ref` appends the slug to the parent's `children` (order kept) or, for an estimate, to the target's `estimates`, and rebuilds that section."
        new: "A `create` with `ref` appends the slug to the parent's `children` (order kept) or, for an estimate, to the target's `estimates`, and rebuilds that section; a derived Estimate create (case 72.3) writes the page `pending` with Context, Criterion and Method and no Result, and is listed on its target the same way."
      - old: "An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace-collapsed match, exactly one occurrence), and appends History."
        new: "An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace-collapsed match, exactly one occurrence), and appends History; an update carrying `criterion_block` appends the block to `## Criterion`, History `criterion: case N added`; a `remove_criterion` entry deletes the `### case N` block, History `criterion: case N removed` (case 72.4)."
      - old: "body `Context`, `Problem`, `Given`, `When` from `case_text`."
        new: "body `Context`, `Problem`, `Given` from `case_text`, and `Criterion` — one `[[estimate-x]] § case N` line per Estimate the Case shaped — when the entry carries `criterion`; no `When` (case 72.4; pages written before keep theirs)."
    change: "the derived Estimate page, the criterion block appended or removed, the decision page's Criterion links and no When (case 72.4)"
  - slug: estimate-generate-writes
    replace:
      - old: "the target's estimates and ## Estimates; an update with set"
        new: "the target's estimates and ## Estimates; a derived Estimate create yields a pending page with Context, Criterion as a ### case N block and Method, listed on its target; an update carrying a criterion block appends it to ## Criterion and sets pending, a removal deletes the block, each with its History line; an update with set"
      - old: "and the sections Context, Problem, Given, When, written before"
        new: "and the sections Context, Problem, Given, and Criterion links when the Case shaped an Estimate, no When, written before"
    set: {status: pending}
    change: "the derived Estimate page and the decision page's Criterion links join the criterion (case 72.4); pending until the unit reading"
```

```tasks
- [x] guppi/generate.py: the derived Estimate create; criterion_block appended and remove_criterion applied with their History lines; the decision page with Criterion links and without When
- [x] tests/test_generate.py: one test per clause above
- [ ] take the reading of estimate-generate-writes on the unit suite, the live half against the librarian's run of this session; write the estimate line
```

### Case 72.5 — `pretask --check` enforces the form

> **when:**
> `guppi pretask --check <plan>` runs.

> **then:**
> One finding each, exit 1: a Leaf `create` item without `method`; a Leaf `update` item
> without `contract`; a Case with two or more Leaf items that create or `changed` ("split
> the Case"); a derived Estimate slug that names an existing page and no `slug` on the
> item.
> **＋** No finding for an Estimate without its own line; the exemption text of
> `items_of` cites this Case, not 53.1.
> **－** The findings of 59.1–59.3 and 59.6 stay as they are.

```then
update:
  - slug: rule-pretask
    replace:
      - old: "and for every `file` item on a path a Rule page governs. Fix the plan or the frontier for each,"
        new: "for every `file` item on a path a Rule page governs, for every Leaf `create` item without `method`, for every Leaf `update` item without `contract`, for every Case with two or more Leaf items that create or say `contract: changed` (split the Case), and for every derived Estimate slug that names an existing page while the item has no `slug`; an Estimate has no line of its own (case 72.5). Fix the plan or the frontier for each,"
    change: "findings for a missing method, a missing contract, two contracts in one Case and a colliding derived slug; no line for an Estimate (case 72.5)"
  - slug: estimate-pretask-reconciles
    replace:
      - old: "and a `file` item on a path a Rule page governs, are each one finding."
        new: "and a `file` item on a path a Rule page governs, a Leaf `create` item without `method`, a Leaf `update` item without `contract`, a Case with two or more Leaf items that create or say `contract: changed`, and a derived Estimate slug naming an existing page with no `slug` on the item, are each one finding; a Leaf's Estimate without a line of its own is none."
    set: {status: pending}
    change: "the findings of case 72.5 join the criterion; pending until the unit reading"
```

```tasks
- [x] guppi/pretask.py: the four findings; items_of's docstring cites case 72.5; the Leaf test reads kind from the then item or the page
- [x] tests/test_pretask.py: one test per finding, and one for the Estimate without a line
- [ ] .claude/skills/pre-task/SKILL.md follows at the next session's render (governed)
- [x] take the reading of estimate-pretask-reconciles on the unit suite and at this session's /pre-task; write the estimate line
```

### Case 72.6 — `lint` accepts both shapes

> **when:**
> `guppi lint` reads a decision page or an Estimate page.

> **then:**
> `## When` is not required on a decision page; `## Criterion`, when present, holds
> links that resolve to Estimate pages.
> **＋** An Estimate's `## Criterion` may be `### case N` blocks or plain text; each
> `case N` names an existing decision page or is a finding.
> **－** Everything else lint checks is unchanged.

```then
update:
  - slug: rule-lint
    replace:
      - old: "a `[[decision-…]]` wikilink in a History line resolves to a page."
        new: "a `[[decision-…]]` wikilink in a History line resolves to a page; `## When` is not required (case 72.6), and every link under `## Criterion` resolves to an Estimate page. An Estimate's `## Criterion` may hold `### case N` blocks; each `case N` names an existing decision page."
    change: "no When required on a decision page; Criterion links and ### case N blocks resolve (case 72.6)"
  - slug: estimate-lint-catches
    replace:
      - old: "a lesson without estimates is not a finding."
        new: "a lesson without estimates is not a finding; a decision page without ## When is not a finding, a ## Criterion link resolving to no Estimate page is one, and a ### case N block of an Estimate naming no decision page is one."
    set: {status: pending}
    change: "the two shapes of case 72.6 join the criterion; pending until the unit reading"
```

```tasks
- [x] guppi/lint.py: When optional on decisions; Criterion links resolve; ### case N blocks resolve
- [x] tests/test_lint.py: the three classes seeded
- [x] take the reading of estimate-lint-catches on the unit suite; write the estimate line
```

## Case 73 — one session, one Spec: `raw/<date>/<hi HHMM>/`

> **context:**
> Sessions I and J both fall on 2026-09-12. `raw/<date>/` keys the Spec, the Frontier and
> the handoff by date, so the second session appends its plan under the first session's
> approved Spec, its Frontier as a second section of the first session's file, and its
> handoff under a `---`. The owner: one session, one Spec.

> **problem:**
> Where the per-session artifacts of a session live when the date already holds a
> session's, and how every hook and script finds them.

> **given:**
> `guppi/event.py` `log_path` is `raw/<date>/event_log.md`; `guppi/ledger.py`
> `hi_recorded` finds the `hi` line after this session's `session-start` across dates
> (case 55.1); the `hi` line carries the time and no session id.
> **＋** `guppi spec` writes `raw/<date>/spec.md`, appending under `---` and a stamp
> (`rule-spec-capture`); `/hi` writes `raw/<date>/frontier.md` (`rule-skill-hi`);
> `pretask --check` reads `raw/<hi date>/frontier.md` (`rule-pretask`); `materialize`
> reads `raw/<date>/spec.md` (`rule-materialize`); Retro appends under `## Deferred` of
> `raw/<date>/spec.md` (`rule-retro`); `/handoff` writes `raw/<today>/handoff.md`, `---`
> before a new document (`rule-handoff`); the librarian's first input is
> `raw/<today>/handoff.md` (`rule-documentation`); `rule-case-protocol` and
> `rule-claude-md` name `raw/<date>/spec.md` and `frontier.md` in their Renders;
> `index.md` §1 lists the six files of `raw/<date>/`; the glossary rows `Spec` and
> `Working files` name the date.
> **＋** Today: `raw/2026-09-12/spec.md` (session I, approved 10:48:13), `frontier.md`
> (F1–F18 of I, F19–F33 of J appended), `handoff.md` (I); session I's `hi` at 04:54:19,
> session J's at 11:56:22. This Plan Mode's ExitPlanMode fires the old hook, so J's plan
> lands under I's Spec before Work Mode moves it.
> **＋** Case 63 (Slice 3c, deferred): the raw lifecycle — archival of an applied date by
> run stamp, `decided_by`, the tail `/hi` prints. This Case narrows what 3c archives; it
> does not take 63 up.
> **＋** The folder name is the `hi` time, `HHMM`, ratified by the owner over a session
> letter: mechanical, sortable, found by every hook from the event log.
> **－** `ledger.md`, `event_log.md`, `materialize.yaml`, `origin` pointers and lint's
> grep targets do not move. `rule-brief` and `rule-index-check` name `handoff.md`
> without a path and do not change.

### Case 73.1 — the layout: `index.md` §1, the glossary, the one-off move

> **when:**
> Someone reads §1 of the map or the glossary; Work Mode runs the one-off once.

> **then:**
> §1 lists `raw/<date>/` with `event_log.md`, `ledger.md`, `materialize.yaml`, and under
> it `<hi HHMM>/` with `spec.md`, `frontier.md`, `handoff.md`; the glossary rows `Spec`
> and `Working files` say the same.
> **＋** The one-off moves session I's three files to `raw/2026-09-12/0454/`, cuts the
> part of `spec.md` under J's separator into `raw/2026-09-12/1156/spec.md`, and the
> F19–F33 section of `frontier.md` into `raw/2026-09-12/1156/frontier.md`.
> **－** `raw/2026-09-09` … `2026-09-11` are not touched: one session each, their files
> stay at the date root, and `materialize` reads that shape for them (73.5).

```then
update:
  - file: vault/wiki/index.md
    change: "§1 layout: raw/<date>/ holds event_log.md, ledger.md, materialize.yaml (the logs of the day, session windows by hi) and one folder <hi HHMM>/ per session with spec.md, frontier.md, handoff.md; the HHMM is the time of the session's hi line; dates before 2026-09-12 keep their files at the root (case 73.1)"
  - file: vault/wiki/glossary.md
    change: "row Spec: copied to raw/<date>/<hi HHMM>/spec.md; row Working files: raw/, the logs of the day and one folder per session named by its hi time (case 73.1)"
```

```tasks
- [x] vault/wiki/index.md §1 and vault/wiki/glossary.md rows Spec and Working files
- [x] one-off, by hand, after ExitPlanMode: git mv raw/2026-09-12/spec.md, frontier.md, handoff.md to raw/2026-09-12/0454/; cut the text under J's separator of spec.md into raw/2026-09-12/1156/spec.md; cut the F19–F33 section of frontier.md into raw/2026-09-12/1156/frontier.md; nothing of 2026-09-09 … 2026-09-11 moves
```

### Case 73.2 — `guppi spec` writes the session's Spec

> **when:**
> `ExitPlanMode` is approved in a session with a `hi`.

> **then:**
> The plan is copied to `raw/<hi date>/<hi HHMM>/spec.md`; a second approval of the same
> session appends under `---` and the stamp, as before.
> **－** Without a `hi` the hook refuses as before.

```then
update:
  - slug: rule-spec-capture
    contract: changed
    replace:
      - old: "appends the approved plan to `raw/<date>/spec.md`: a `---` separator when the file has content,"
        new: "appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` — the session's folder, named by the time of its `hi` line (case 73) — a `---` separator when the file has content,"
    change: "the Spec lands in the session's folder raw/<hi date>/<hi HHMM>/ (case 73.2)"
```

```tasks
- [x] guppi/event.py: session_dir(project_dir, now, stamp) — the date and HHMM of the hi line of this session's window, from the event logs the ledger hook walks; None without a hi
- [x] guppi/spec.py: spec_path uses session_dir; the folder is created
- [x] tests/test_spec.py: the path with a hi at 11:56 is raw/<date>/1156/spec.md; a second approval appends there
```

### Case 73.3 — `/hi` writes the Frontier into the session folder

> **when:**
> The person invokes `/hi`.

> **then:**
> The Frontier goes to `raw/<hi date>/<hi HHMM>/frontier.md`, the folder made at that
> moment; the lines and their closing are as in case 59.2.

```then
update:
  - slug: rule-skill-hi
    contract: changed
    replace:
      - old: "Write the same list to `vault/raw/<date>/frontier.md`, one line per item:"
        new: "Write the same list to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` the time of the `hi` line above (case 73) — one line per item:"
    change: "the Frontier lands in the session's folder (case 73.3)"
```

```tasks
- [ ] .claude/skills/hi/SKILL.md follows at the next session's render (governed)
```

### Case 73.4 — `pretask --check` reads the Frontier there

> **when:**
> `guppi pretask --check <plan>` runs.

> **then:**
> The frontier it checks is `raw/<hi date>/<hi HHMM>/frontier.md`; a missing file is one
> finding, as before.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "for every line of `raw/<date>/frontier.md` still open"
        new: "for every line of `raw/<hi date>/<hi HHMM>/frontier.md` (the session's folder, case 73) still open"
    change: "the frontier of the session's folder (case 73.4)"
```

```tasks
- [x] guppi/pretask.py: check_frontier reads session_dir / frontier.md
- [x] tests/test_pretask.py: the frontier path follows the hi time
- [ ] .claude/skills/pre-task/SKILL.md follows at the next session's render (governed)
```

### Case 73.5 — `materialize` reads every Spec of the date

> **when:**
> `guppi materialize` reads a date.

> **then:**
> The `then` blocks of a Case come from every `<HHMM>/spec.md` under the date, in folder
> order, and from `raw/<date>/spec.md` when the date has one (older dates); the yaml's
> `spec` field names the file the Case was found in.
> **－** Case numbers are unique across sessions; a Case found in two files is an error,
> the walk stops.

```then
update:
  - slug: rule-materialize
    contract: changed
    replace:
      - old: "reads `raw/<date>/ledger.md` and `raw/<date>/spec.md` and writes `raw/<date>/materialize.yaml`."
        new: "reads `raw/<date>/ledger.md` and every Spec of the date — `raw/<date>/<HHMM>/spec.md` in folder order, and `raw/<date>/spec.md` when the date has one (dates before case 73) — and writes `raw/<date>/materialize.yaml`; the yaml's `spec` field names the file each Case was found in, and a Case heading found in two files stops the walk with exit 1."
    change: "one Spec per session folder; all of a date's Specs are read (case 73.5)"
```

```tasks
- [x] guppi/materialize.py: the Specs of a date, the spec field per Case, the duplicate-heading error
- [x] tests/test_materialize.py: two session folders, one Case each; a root spec.md of an older date; a Case in two files
```

### Case 73.6 — Retro appends to the session's Spec

> **when:**
> `/retro` writes a short defer.

> **then:**
> It is appended under `## Deferred` of `raw/<hi date>/<hi HHMM>/spec.md`; the unticked
> `tasks` Retro counts are that file's.

```then
update:
  - slug: rule-retro
    contract: changed
    replace:
      - old: "the `tasks` of `raw/<date>/spec.md`, the unticked boxes"
        new: "the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), the unticked boxes"
      - old: "appended to `vault/raw/<date>/spec.md` under the `## Deferred` heading"
        new: "appended to `vault/raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading"
    change: "Retro reads and appends the session's Spec (case 73.6)"
```

```tasks
- [ ] .claude/skills/retro/SKILL.md follows at the next session's render (governed)
```

### Case 73.7 — `/handoff` writes the session's handoff

> **when:**
> The person invokes `/handoff`.

> **then:**
> `handoff.md` is written to `raw/<hi date>/<hi HHMM>/`, one document, no `---`; the
> librarian is dispatched with that path.

```then
update:
  - slug: rule-handoff
    contract: changed
    replace:
      - old: "Otherwise append to `vault/raw/<today>/handoff.md` (create it when missing; `---` before a new document in an existing file) a document headed"
        new: "Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed"
    change: "the handoff is one document in the session's folder; the librarian is dispatched with its path (case 73.7)"
```

```tasks
- [ ] .claude/skills/handoff/SKILL.md follows at the next session's render (governed); the dispatch line of the skill names the path
```

### Case 73.8 — the librarian reads the handoff it is given

> **when:**
> `librarian-guppi` starts.

> **then:**
> Its first input is the `handoff.md` the dispatch names, `raw/<hi date>/<hi HHMM>/handoff.md`;
> the other three inputs are unchanged.

```then
update:
  - slug: rule-documentation
    contract: changed
    replace:
      - old: "Your inputs are four: `vault/raw/<today>/handoff.md`, every `materialize.yaml`"
        new: "Your inputs are four: the `handoff.md` your dispatch names, `vault/raw/<date>/<hi HHMM>/handoff.md` (the session's folder, case 73), every `materialize.yaml`"
    change: "the handoff of the session's folder (case 73.8)"
```

```tasks
- [ ] .claude/agents/librarian-guppi.md follows at the next session's render (governed)
```

### Case 73.9 — the Case protocol names the session folder

> **when:**
> A session starts with `CLAUDE.md`.

> **then:**
> The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` (the Deferred heading,
> the ticked boxes) and the Frontier `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "under the `## Deferred` heading of `raw/<date>/spec.md`, before its ledger line (cases 56, 59.5)"
        new: "under the `## Deferred` heading of `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), before its ledger line (cases 56, 59.5)"
      - old: "The Frontier is `raw/<date>/frontier.md`, written at `/hi`;"
        new: "The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`;"
      - old: "Work Mode ticks the boxes in `raw/<date>/spec.md` in the reply that finishes the task;"
        new: "Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task;"
    change: "the Spec and the Frontier live in the session's folder (case 73.9)"
```

```tasks
- [ ] CLAUDE.md follows at the next session's render (governed)
```

### Case 73.10 — the Migration paragraph of `CLAUDE.md`

> **when:**
> A session starts with `CLAUDE.md`.

> **then:**
> The Migration paragraph says the approved plan is copied to
> `vault/raw/<date>/<hi HHMM>/spec.md`.

```then
update:
  - slug: rule-claude-md
    contract: changed
    replace:
      - old: "The approved plan is copied to `vault/raw/<date>/spec.md` by the `PostToolUse ExitPlanMode` hook `guppi spec` since Slice 2;"
        new: "The approved plan is copied to `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder, by the `PostToolUse ExitPlanMode` hook `guppi spec` since Slice 2 (the folder since case 73);"
    change: "the Migration paragraph names the session's folder (case 73.10)"
```

```tasks
- [ ] CLAUDE.md follows at the next session's render (governed)
```

## Case 74 — `rule-pretask`: a Case with work, not a Case with lines

> **context:**
> Case 59.3 says `guppi pretask --check` reports "a Case that has decision lines and no
> `tasks` block". At the first live run the three deferred decisions of session I (Cases
> 63–65) were reported: a defer has lines and no work, so no `tasks` block. The code
> exempts a Case whose lines are all `defer` (commit `2b7dd42`); the ratified wording does
> not. Deferred as Case 68.

> **problem:**
> The Render of `rule-pretask` and the criterion of `estimate-pretask-reconciles` say "a
> Case with decision lines". The code says "a Case with a line other than `defer`". One
> of them yields.

> **given:**
> `rule-pretask` Render: "for every ratified Case without a `tasks` block"; `deferred_by:
> [decision-case-68]`. `guppi/pretask.py` `check_tasks`: `with_work` is the Cases with a
> line whose kind is not `defer`; the finding "decision lines and no tasks block" fires
> for those only, with the comment "a defer-only Case has no work (case 59.5)".
> **＋** `estimate-pretask-reconciles` Criterion: "a Case with decision lines and no
> `tasks` block ... are each one finding"; `pending` since 72.5; its Criterion gains this
> Case's block by 72.3 and the `### case 68` removal finds nothing to remove.
> **＋** Case 59.5: a short-form defer has `context`, `problem` and a `defer` block only.
> **＋** 72.5 and 73.4 update the same Render this session; the three `replace` items
> touch different sentences.
> **－** A Case that mixes a `defer` with another kind still needs its `tasks` block.

> **when:**
> `guppi pretask --check <plan>` reads a ratified Case.

> **then:**
> A Case with a line of a kind other than `defer` and no fenced block tagged `tasks` is
> one finding; a Case whose lines are all `defer` is none.
> **＋** The Render of `rule-pretask` says so in those words.
> **－** The code does not change; the unit test of the exemption is the reading.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "for every ratified Case without a `tasks` block,"
        new: "for every ratified Case with a line of a kind other than `defer` and no `tasks` block (a defer-only Case has no work, case 74),"
    change: "a Case with work, not a Case with lines: the defer-only exemption of the code is the wording (case 74, supersedes 68)"
```

```tasks
- [x] no code change; the comment in guppi/pretask.py check_tasks cites case 74
- [x] tests/test_pretask.py: the defer-only Case without a tasks block is no finding, the mixed Case is one (if not already there)
- [ ] .claude/skills/pre-task/SKILL.md follows at the next session's render (governed)
```

## Case 75 — the ledger line is shown as it is written, and checked as it is read

> **context:**
> Every decision line of session I up to 10:09 was written `decision[58][update][slug]`;
> `materialize.parse_line` reads `decision[case 58][update][slug]` only. The agent took
> the placeholder `decision[case_id][kind][slug]` of the table "What a Case produces" in
> `case-schema.md` literally; the Render of `rule-case-protocol` shows the line only as
> `- decision[...]`. Deferred as Case 67; the 30 wrong lines stand under `unparsed`
> (`lesson-ledger-decision-line-written-without-the-case-word`). The Insight over it:
> nothing between the reply and `materialize` holds a written line against the grammar.

> **problem:**
> What the agent reads at session start does not show a decision line as the ledger
> holds it; and nothing in the session reports a line that will not parse.

> **given:**
> `case-schema.md` table: `- decision[case_id][kind][slug]{ref}{source}{supersedes}{tags:a,b}`.
> `index.md` §4: line 158 shows `decision[case 3][create][entity-x]`, line 179
> `decision[case_id][kind][slug]{ref:parent}{source:external_id}{tags:a,b}`, line 203
> `{supersedes:case1}` without the space. `rule-case-protocol` Render: "A record is a
> `- decision[...]`, `- estimate[...]` or `- lesson[...]` line"; `deferred_by:
> [decision-case-67]`.
> **＋** `materialize.parse_line`: `RECORD` then brackets; a decision needs three heads
> and `heads[0]` starting with `case `; `supersedes` goes through `_case_of`.
> **＋** `guppi pretask --check` already reads the ledgers of the window for the
> then-item comparison (59.1); `parse_line` is importable from `guppi.materialize`.
> **＋** 72.5, 73.4 and 74 update the Render of `rule-pretask` this session; 72.1 and
> 73.9 the Render of `rule-case-protocol`; each `replace` its own sentence.
> **－** The 30 unparsed lines of 2026-09-12 stay as the trace; nothing rewrites them.

### Case 75.1 — the texts show the line as written

> **when:**
> A session starts with `CLAUDE.md`; someone reads `case-schema.md` or `index.md` §4.

> **then:**
> The table of `case-schema.md`, §4 of the map and the ledger paragraph of the Render
> show `- decision[case 12][update][rule-x]{ref:rule-x}` and
> `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is `case N`
> with the word and a space, in `{supersedes:case N}` too.
> **－** The estimate and lesson rows do not change.

```then
update:
  - file: vault/wiki/case-schema.md
    change: "table 'What a Case produces', row 'ratified decision': the line shown as written — `- decision[case 12][update][rule-x]{ref:rule-x}` and `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` — with one sentence under the table: the id is `case N`, the word and a space, in `{supersedes:case N}` too; the estimate and lesson rows unchanged (case 75.1, supersedes 67)"
  - file: vault/wiki/index.md
    change: "§4: line 179 shows the line as written, `- decision[case 12][update][rule-x]{ref:rule-x}{source:external_id}{tags:a,b}`; line 203 `{supersedes:case 4}` with the space; one sentence: the id is `case N` everywhere (case 75.1)"
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "A record is a `- decision[...]`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag;"
        new: "A record is a `- decision[case 12][update][rule-x]{ref:rule-x}`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag — the id is `case N`, the word and a space, in `{supersedes:case N}` too;"
    change: "the ledger paragraph shows a decision line as written, with the word case (case 75.1, supersedes 67)"
```

```tasks
- [x] vault/wiki/case-schema.md: the table row and the sentence
- [x] vault/wiki/index.md §4: lines 179 and 203 and the sentence
- [ ] CLAUDE.md follows at the next session's render (governed)
```

### Case 75.2 — `pretask --check` reports a line that will not parse

> **when:**
> `guppi pretask --check <plan>` runs.

> **then:**
> Every record line of the session's window — the ledgers of the window's dates, on the
> `hi` date from the `hi` time on — goes through `materialize.parse_line`; each that
> returns none is one finding with its date and line number, exit 1.
> **－** Lines before the `hi` are not read; a preview outside a LEDGER block is not a
> record and is not checked.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "Fix the plan or the frontier for each, then run it again until it prints nothing."
        new: "It also runs every record line of the session's window through `materialize.parse_line` and prints one line for each that does not parse, with its date and line number (case 75.2). Fix the plan, the frontier or the line for each, then run it again until it prints nothing."
    change: "a ledger line of the window that does not parse is a finding (case 75.2)"
```

```tasks
- [x] guppi/pretask.py: check_grammar over the window's record lines with materialize.parse_line
- [x] tests/test_pretask.py: a line without the word case is one finding with its date and number; a preview outside a LEDGER block is none
- [ ] .claude/skills/pre-task/SKILL.md follows at the next session's render (governed)
```

## Case 76 — `guppi materialize --show`: look before the librarian writes

> **context:**
> In Work Mode of session I the agent ran `uv run guppi materialize --date 2026-09-12`
> to see how the day's lines would parse. The command has one mode: it wrote
> `raw/2026-09-12/materialize.yaml`, the librarian's artifact, which the agent deleted
> at once. Deferred as Case 69.

> **problem:**
> The only way to see what the ledger and the Spec will become is to write the yaml.

> **given:**
> `guppi/materialize.py` `parser()` has `--date` only; `run` builds the entries and
> writes the yaml, printing one line per date. `rule-materialize` `deferred_by:
> [decision-case-69]`; `estimate-materialize-walks-dates` Criterion: "walks every
> `raw/<date>/` with a `ledger.md` in date order, extends or writes each yaml, prints one
> line per date"; `estimate-materialize-assembles` is `pending` since 72.3.
> **＋** An existing yaml is extended, never rewritten (case 41): with `--show` the
> extension is computed and printed, the file untouched.
> **＋** 72.3 and 73.5 update `rule-materialize` this session; each `replace` its own
> sentence.
> **－** `--show` prints the full yaml of the date, entries already `applied` included;
> what is new is visible by the absence of `applied`.

> **when:**
> `uv run guppi materialize --show [--date YYYY-MM-DD]` runs.

> **then:**
> Stdout holds the yaml each date would be written with — entries, `unparsed`,
> `incomplete` marks, decision groups — one document per date, and no file under
> `raw/` changes; exit 0, or 1 on an error of the walk as without `--show`.
> **＋** Without `--show` the command writes as before.

```then
update:
  - slug: rule-materialize
    contract: changed
    replace:
      - old: "An error on one date stops the walk with exit 1."
        new: "An error on one date stops the walk with exit 1. With `--show` (case 76) the same walk prints to stdout the yaml each date would be written with — entries, `unparsed`, `incomplete` marks, decision groups, one document per date — and writes nothing under `raw/`; the agent and pre-task look before the librarian runs."
    change: "a --show mode prints the yaml and writes nothing (case 76, supersedes 69)"
```

```tasks
- [x] guppi/materialize.py: --show; the yaml document per date to stdout; no write
- [x] tests/test_materialize.py: --show prints the document and leaves raw/ unchanged; the exit code on an error is the same as without it
- [x] Makefile: no new target; `make help` unchanged
```

## Case 77 — `rule-claude-md`: the stale sentence of "How it works"

> **context:**
> Case 59.8 wrote "How it works" of `rule-claude-md` before Case 66 moved
> `rule-case-protocol` under it; the brief flags the sentence as stale.

> **problem:**
> The section says "`rule-case-protocol` keeps its parent `rule-plan-mode`; it is listed
> here for the renderer only", and the frontmatter of both pages says the opposite.

> **given:**
> `rule-claude-md` `children: [rule-case-protocol]`; `rule-case-protocol` `parent:
> rule-claude-md` (case 66). The sentence is the last of "How it works". 73.10 updates
> the Render of the same page; different sentence.

> **when:**
> Someone reads "How it works" of `rule-claude-md`.

> **then:**
> The section says: "`rule-case-protocol` has this page as its parent since case 66 and
> is its one child; the renderer splices it into the marker."

```then
update:
  - slug: rule-claude-md
    contract: same
    replace:
      - old: "`rule-case-protocol` keeps its parent `rule-plan-mode`; it is listed here for the renderer only."
        new: "`rule-case-protocol` has this page as its parent since case 66 and is its one child; the renderer splices it into the marker."
    change: "the stale sentence on rule-case-protocol's parent corrected (case 77)"
```

```tasks
- [x] no file of the repository changes for this Case in Work Mode; the librarian's generate applies the replace
```

## Deferred

## Case 78 — Slice 3b: Work Mode, deferred again

> **context:**
> Case 29 (2026-09-10) deferred `rule-work-mode` and `rule-subagent-guppi` together: Work
> Mode as ratified rules — the plan, the branch and baseline, the subagent that executes
> and never decides, the four hooks of the draft in `docs/migration/rule-work-mode.md`.
> Case 59.3 dropped the separate executable plan: the `tasks` blocks of the Spec are what
> a subagent executes. The owner's clause of case 59: a fork in Work Mode is not a return
> to Plan Mode — the subagent stops, the fork is a short-form Case under `## Deferred`,
> worked next session. Deferred as 64 in session I.

> **problem:**
> Work Mode runs on the draft and on habit; the two pages are placeholders and lint
> orphans. Session J's Work Mode holds Cases 72 and 73; no room. Postponed five times now.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Governs Work Mode — the Spec's tasks executed by subagents that never decide, a fork returned as a short-form Case
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs the subagent that executes a task of the Spec and stops at a fork
```

## Case 79 — Slice 3c: the raw lifecycle, deferred again

> **context:**
> Case 45 (2026-09-10) deferred `rule-ledger-tail`: the ledger lines written after the
> librarian's commit reach the next Frontier only two sessions later, because `/hi` reads
> `brief.md` alone. Slice 3c grew around it: `decided_by`, `origin` as a ledger pointer,
> `raw/<date>/` of an applied date archived by run stamp, the fresh ledger as the tail
> `/hi` prints, lint on both fields. Deferred as 63 in session I. Case 73 (session J)
> took the session folder out of it: what 3c archives is now `raw/<date>/` with its
> session folders.

> **problem:**
> `/hi` still shows nothing of what was written after the librarian's commit; the
> memory file that carried the tail is gone (case 62). Postponed four times now.

```then
defer:
  - slug: rule-ledger-tail
    type: rule
    purpose: Shows at /hi the ledger lines written after the librarian's commit
```

## Case 80 — the archive in `ask-guppi`, deferred again

> **context:**
> Case 31 (2026-09-10) discussed and did not decide: `ask-guppi` answers from the four
> indexes, which list live pages only; a slug that was archived is reported as missing.
> `vault/archived/` holds 21 pages; `guppi cleanup` brings a page back on an `update`
> of `status`. Deferred as 65 in session I.

> **problem:**
> A Case may propose a `create` of a slug the archive already holds, and pre-task passes
> it. The fix is an `update` of `rule-ask` with its Estimate, and no session has reached
> it. Postponed five times now.

```then
defer:
  - slug: rule-ask
    type: rule
    purpose: Answers a question about the vault from the indexes, one entry point; the archive included
```
