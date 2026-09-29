<!-- approved 19:50:26 · session 8a78b32d -->

# Spec — session 1753, 2026-09-29

## Case 520 — The glossary rows point at the page that defines them

> **context:**
> The glossary is the `## Terms` table of `entity-glossary`. Each row holds a term, a one-line meaning and a `where` link to the live page that defines the term. `guppi glossary` renders the table into `vault/wiki/glossary.md`, grouped by the parent MOC of each `where` page, and `/hi` loads it. `estimate-glossary-terms-defined` promises that each `where` page defines its row. The reading at this `/hi` failed on five rows after the librarian's run d8c1f17, which applied case 515.
> - Vault links to `rule-page-schemas`, which never says what the vault is. Its meaning also reads as "one page per category".
> - Hook links to `rule-hook-registry`, but its meaning describes the ledger writer: it reads the transcript, keeps its window across midnight, and can block. Only `rule-ledger-write` says that.
> - `deferred_by` and `origin` link to `rule-page-generation`, whose body names neither field.
> - Entity / Rule (status) links to the same page, which lists neither `archived` nor "built once every Estimate passes".
>
> The `origin` meaning also says "created or deleted" and that lint greps the field. No page body says either.
>
> The person agreed with every recommendation of the round. Each changed row links to a page that states it. A clause that no such page states is cut, and it still stands on its own page, such as midnight on `rule-ledger-write`. The rows the reading accepted only loosely stay as they are: `CLAUDE.md`, `case-schema.md`, Types and Decision.
>
> Two passes of pre-spec changed the new meanings. The person agreed to cut the `deferred_by` meaning to what its page says.
> - Hook names `rule-hook-registry` in place of "this page", which in the glossary would read as `entity-glossary`. As that page says, a hook can also stand in an agent's own frontmatter, as part of that agent's Render.
> - `deferred_by` first kept "On an Entity, Rule or Insight", which `rule-rules-schema` does not state. Then it said "On a Rule", which was too narrow: `rule-entities-schema` and `rule-insights-schema` define the same field, and a live Insight carries it. The meaning now has no qualifier and opens with the Decision pages whose `defer` targets the page. That is true for all three types and is what `rule-rules-schema` states.
> - `origin` follows `rule-decisions-schema`: its case numbers, the Case file only for a Case built by `case-guppi` from session 2026-09-27/1819 on, and the pointer that is not rewritten. It opens "On a page a Case created". That is my choice over naming the Decision page alone: the Entity, Rule and Estimate schemas give the same form for a page a Case created. A Lesson points at its ledger line, and an Insight points at no ledger line. Neither is a page a Case created, so the meaning does not claim them.
>
> The Case creates no page, so no vault query was needed. The frame reads as follows. `rule-glossary` stops the write on a `where` that names no live page, so every new link must name a live page, and each one does. The Purpose of `entity-glossary` lets a term enter, change or leave by an `update` of the page with `replace` pairs, and the split of the status row does exactly that. The Criterion of `estimate-glossary-terms-defined` stands whole, because the promise does not change, only the rows. So its status is not set to `pending` here, and its reading waits for the librarian's run that renders the table. The Estimates of `rule-glossary` speak of the render, the check and the ticks, not of these rows, and are not touched.

> **problem:**
> Five rows of the glossary link to a page that does not define their term, or give a meaning that their `where` page does not state. So the promise of `estimate-glossary-terms-defined` fails, and a reader who follows the link does not find the term.

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, grouped by the parent MOC of `where`
> **＋** `rule-glossary` — the guard: one link per `where` cell, a live page, no term twice
> **＋** `rule-vault-layout` — the new `where` page of Vault
> **＋** `rule-hook-registry` — the `where` page of Hook
> **＋** `rule-entities-schema` — the new `where` page of Entity (status)
> **＋** `rule-rules-schema` — the new `where` page of Rule (status) and `deferred_by`
> **＋** `rule-decisions-schema` — the new `where` page of `origin`

> **when:**
> `uv run guppi glossary` renders `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader follows the `where` link of a row.

> **then:**
> The row Vault names `rule-vault-layout`, and its meaning says that the vault is `vault/wiki/`, one folder per page category.
> **＋** The row Hook names `rule-hook-registry`, and its meaning says only what that page says.
> **＋** The rows Entity (status) and Rule (status) replace the row Entity / Rule (status), and they name `rule-entities-schema` and `rule-rules-schema`.
> **＋** The row `deferred_by` names `rule-rules-schema`, and its meaning says only what that page says.
> **＋** The row `origin` names `rule-decisions-schema`, and its meaning says only what that page says, for a page a Case created.
> **＋** `vault/wiki/glossary.md` lists each of these rows under the parent MOC of its new `where` page.
> **－** The other rows of the table of `entity-glossary` do not change.

```then
update:
- slug: entity-glossary
  replace:
  - old: '| Vault | The folder of Markdown pages, one per category | [[rule-page-schemas]] |'
    new: '| Vault | `vault/wiki/`: one folder per page category, each page a file named by its slug | [[rule-vault-layout]] |'
  - old: '| Hook | An event-triggered script behind a Rule page, the ledger writer on `Stop`, which reads the session''s transcript back, keeps its `hi` window across midnight, and can block | [[rule-hook-registry]] |'
    new: '| Hook | A script that fires on an event of the session, behind a Rule page; registered in the `hooks` key of `.claude/settings.json`, which `rule-hook-registry` renders, or in an agent''s own frontmatter as part of that agent''s Render; a new hook in the file is an `update` of `rule-hook-registry` in the Case that creates its Rule | [[rule-hook-registry]] |'
  - old: '| `deferred_by` | On an Entity, Rule or Insight, the Decision pages whose `defer` targets it; set by `generate`, cleared by a `supersedes`, shown in the index line, followed by `ask-guppi` | [[rule-page-generation]] |'
    new: '| `deferred_by` | The Decision pages whose `defer` targets the page; written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it, so `ask-guppi` reaches the deferred decision (case 52.3) | [[rule-rules-schema]] |'
  - old: '| `origin` | The Decision that created or deleted the page, as `raw/<date>/<HHMM>/ledger.md#case-N` — the date form on older pages; kept when archived, never rewritten; `#case-N` is a grep target lint checks in `raw/` or in the archive (case 103.6) | [[rule-page-generation]] |'
    new: '| `origin` | On a page a Case created: where that Case was ratified, `raw/<date>/<HHMM>/ledger.md#case-N` — the date form `raw/<date>/ledger.md#case-N` on pages born before 2026-09-13 (case 103.6); the folder holds the Spec with the Case and, for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file (case 513); the pointer is not rewritten when the session is archived (cases 100.1, 103.6) | [[rule-decisions-schema]] |'
  - old: '| Entity / Rule (status) | `draft` / `built` / `archived`; `built` is computed once every Estimate passes, never by hand | [[rule-page-generation]] |'
    new: |-
      | Entity (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-entities-schema]] |
      | Rule (status) | `draft` / `built` / `archived`; `built` is set by the cascade of `generate` once every Estimate passes, never by hand | [[rule-rules-schema]] |
  change: the rows Vault, Hook, deferred_by and origin point at the page that defines each, their meanings cut to it; Entity / Rule (status) splits into Entity (status) and Rule (status) (case 520)
```

```tasks
- [ ] update `entity-glossary`
- [ ] `uv run guppi glossary`
- [ ] read `estimate-glossary-terms-defined`
```

## Case 521 — A comment in a short Case's `then` block is caught, and the cut defer of case 519 is taken up

> **context:**
> When the person puts a decision off, the main agent writes a short-form Case itself. The Case holds a fence tagged `then` in plain YAML with `slug`, `type` and `purpose`. The `Stop` hook of `rule-spec-write` (`guppi/ratified.py`) parses the fence. It checks that each `defer` line has an item with these three keys and no foreign key, then copies the fence into the Spec as the reply shows it. Later `materialize` parses the fence again, and `generate` writes `purpose` under `## Deferred` of the Decision page. In YAML a `#` after a space or a tab starts a comment, so a value without quotes ends before it. At the Retro of session 1432 the short Case 519 held `purpose: Correct the description of ## Criterion in the Render of rule-estimates-schema, …`, and YAML kept only "Correct the description of". That text stands in `materialize.yaml` L36 of 1432, under `## Deferred` on `decision-case-519`, and in the backlog through the `deferred_by` of `rule-estimates-schema`. No check saw it. A full Case built by `case-guppi` does not have this problem. Its values are code spans, and the hook writes their YAML itself with `yaml.dump` of `guppi/ratified.py`, which quotes a value that needs it. A search of every `spec.md` under `vault/raw/` for an unquoted value that holds ` #` found the line of case 519 and no other.
> In one round the person accepted every recommendation. The hook and `materialize` both catch a comment, by one function in `guppi/materialize.py`. Any comment in the fence is a finding, not only a comment after a value. The hook refuses, as it refuses a missing `purpose`. The deferred decision of case 519 is taken up now: the sentence is corrected and case 519 is superseded. The short-form paragraph of `rule-case-protocol` tells the agent to quote such a value.
> What `case-guppi` found in the frame. The round said that `generate` does not apply an entry that `materialize` marks `incomplete`. That is false. `rule-page-generation` says "A page is always created, even incomplete". So the mark of 521.2 names the comment in the yaml that the librarian reads, but it does not stop the page. The refusal of the hook in 521.1 is what keeps the cut text off a page. 521.2 states this as a `－` line and does not change `generate`. `estimate-spec-write-writes-a-defer` promises the checks of a defer, so 521.1 replaces its Criterion whole and keeps each earlier line word for word. The other Estimates of `rule-spec-write` speak of full Cases, the ratified copy, the approved Spec and a superseded Case, and stand. `estimate-materialize-assembles` says that what the block lacks is `incomplete`, never invented. A new reason does not make it false, so it stands. `estimate-materialize-judges-a-fence` speaks of where a fence opens and closes, not of the YAML inside it, and stands. The new promise of `materialize` is the Estimate that 521.2 creates. Its slug `estimate-materialize-marks-a-comment` is free: no page under `vault/wiki/` matches it. It has a `ref`, so no vault query was run. `estimate-estimates-schema-checked` promises the lists of the schema file and that its description and sections name no `Given:` kept on an older page. The corrected sentence keeps both, and an `update` of a Render touches no Estimate of the live reading (case 378.5), so it stands. `estimate-case-protocol-defers-in-one-reply` promises that a defer is shown and written in one reply. It says nothing about the value inside the fence and stands; its failed reading is Frontier item C8. The other hooks on `Stop` in `.claude/settings.json` are `guppi ledger`, `guppi casecheck` and `guppi context`. The ledger hook writes the `defer` line in parallel, whatever `ratified` answers.
> Pre-spec found that the Case defined a comment in two ways. The `then` lines said "after a space or a tab", but the `new` texts of `rule-spec-write` and `rule-materialize` and the sentence of 521.4 said only "after a space". The person accepted the fix. Every text now says "a `#` at the start of a line or after a space or a tab", the one definition that the shared function implements. 521.4 says "after a space or a tab" for a value.
> What the check of the answer notes, and why the notes stand. Two `then` lines of 521.2 share most of their words with 521.1: the definition of a comment, and the `－` line on a `#` inside quotes or inside a `|` or `>` block. This is on purpose. Both sides use one function and the same definition. 521.1 promises what the hook refuses, and 521.2 promises what `materialize` marks. They are separate promises with separate tests, and the test of 521.2 runs both sides over the same fence.
> Code and timing. The hook runs from the working tree as soon as 521.1 is coded, and the sentence of 521.4 reaches `case-schema.md` at the render. In that time the hook may refuse a short Case with an unquoted ` #`. Nothing is lost. The ledger line is written, and the agent shows the Case again with the value in quotes. This is the same path as a refused missing `purpose`. The form it refuses was never correct, so no old form is kept. `materialize` extends an existing yaml and never rewrites it, so L36 of 1432 is not read again.
> Not done: `generate` still applies an entry marked `incomplete`. `materialize.yaml` L36 of 1432 stays as it is. A full Case of `case-guppi` gets no new check, because its values do not pass through hand-written YAML.

> **problem:**
> YAML cuts a value without quotes at ` #`, and no check sees the cut. So a short-form Case can reach the Spec, the Decision page and the backlog with a value the person never wrote, as the purpose of case 519 did. The backlog item of `rule-estimates-schema` also carries that cut text, and the sentence it was meant to correct is still wrong.

### Case 521.1 — The `Stop` hook refuses a short Case whose `then` block holds a comment

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a deferred Case into the Spec
> **＋** `guppi/ratified.py` — `deferred_section`, which reads the fence tagged `then` of a short Case
> **＋** `guppi/materialize.py` — holds the one function that finds a comment in a fence tagged `then`, and `item_keys`
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, where a defer at Retro is written
> **＋** `tests/test_ratified.py` — the tests of a defer
> **＋** `estimate-spec-write-writes-a-defer` — the promise; its Criterion is replaced whole

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while Plan Mode lasts, and of `raw/<date>/<hi HHMM>/spec.md` once that file stands, at Retro: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The ratified copy `<plan>.ratified.md` gets no defer, and the check after the write does not run on it.

```then
update:
- slug: rule-spec-write
  replace:
  - old: a key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3).
    new: a key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); so is a `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — by the one function of `guppi/materialize.py`, since YAML drops the rest of the line and no page receives it (case 521.1).
  change: a short Case whose then block holds a YAML comment is refused, judged by the function of guppi/materialize.py (case 521.1)
- slug: estimate-spec-write-writes-a-defer
  set:
    status: pending
  change: the Criterion replaced whole — a then block that holds a YAML comment is refused (case 521.1)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] update `estimate-spec-write-writes-a-defer`
- [x] `guppi/materialize.py`: one function that returns the lines of a fence tagged `then` that hold a YAML comment — a `#` at the start of a line or after a space or a tab — a `#` inside a quoted value or a `|` or `>` block not counted
- [x] `guppi/ratified.py`: `deferred_section` imports that function and refuses a block with a comment, with the line and the advice to quote the value; the module docstring says so
- [x] `tests/test_ratified.py`: a short Case with `purpose: a ## b` unquoted, and one with a tab before the `#`, are refused and not written; the same value in quotes, and a `#` inside a `|` block, are written
- [ ] read `estimate-spec-write-writes-a-defer` — `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, at a later session
```

### Case 521.2 — `materialize` marks the entries of a Case whose `then` block holds a comment

> **given:**
> `rule-materialize` — the rule of the librarian's reading of the ledger and the Spec
> **＋** `guppi/materialize.py` — `then_blocks`, the entry of a decision line, the function that finds a comment, and the docstring list of `incomplete`
> **＋** `raw/<date>/<HHMM>/spec.md` — the Spec whose fences tagged `then` `materialize` reads
> **＋** `rule-spec-write` — the rule of the `Stop` hook that imports the same function
> **＋** `tests/test_materialize.py` — the tests of the lift
> **＋** `rule-page-generation` — the rule of `generate`, which writes a page even from an `incomplete` entry
> **＋** `estimate-materialize-marks-a-comment` — the new promise

> **when:**
> `uv run guppi materialize` lifts the entries of a Case N from its fences tagged `then` in `raw/<date>/<HHMM>/spec.md`.

> **then:**
> A fence of Case N that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of Case N `incomplete: [comment]`, and the run does not fail.
> **＋** The entry keeps the values that YAML read, and nothing is invented for the text after the `#`.
> **＋** The comment is found by the same function of `guppi/materialize.py` that the `Stop` hook of `rule-spec-write` imports, so both give the same answer for the same fence.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text and gives no mark.
> **－** `generate` still applies an entry so marked, since a page is always created, even incomplete.

```then
create:
- slug: estimate-materialize-marks-a-comment
  type: estimate
  ref: rule-materialize
  kind: QA
  purpose: 'A then block that holds a YAML comment gives each decision entry of its Case incomplete: [comment], judged by the one function the Stop hook of rule-spec-write imports'
  method: uv run pytest tests/test_materialize.py -k comment
  tags:
  - harness
  - workflow
  - ledger
update:
- slug: rule-materialize
  replace:
  - old: lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3).
    new: 'lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3). A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of its Case `incomplete: [comment]`: YAML drops the rest of the line, so the value may be cut; the judgment is one function, which the `Stop` hook of `rule-spec-write` imports (case 521.2).'
  change: 'a then block that holds a YAML comment marks the decision entries of its Case incomplete: [comment] (case 521.2)'
```

```tasks
- [ ] update `rule-materialize`
- [ ] create `estimate-materialize-marks-a-comment`
- [x] `guppi/materialize.py`: the entry of a decision line takes `incomplete: [comment]` when a fence tagged `then` of its Case holds a comment, by the function of 521.1; the docstring list of `incomplete` names `comment`
- [x] `tests/test_materialize.py`: a Spec whose short Case holds `purpose: a ## b` unquoted gives its entry `incomplete: [comment]` and `purpose: a`; a tab before the `#` gives the same mark; the value in quotes, and a `#` inside a `|` block, give no mark; one test runs the hook's check and `materialize` over the same fence and asserts they answer alike
- [ ] read `estimate-materialize-marks-a-comment` — `uv run pytest tests/test_materialize.py -k comment`, at a later session
```

### Case 521.3 — The Estimate schema says the frame of a Case stays in its Case file; the defer of case 519 is retired

> **given:**
> `rule-estimates-schema` — the rule; its Render is the schema of an Estimate page
> **＋** `vault/wiki/estimates/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `decision-case-519` — the deferred decision on this sentence, with the cut text under `## Deferred`
> **＋** `rule-page-generation` — the rule of `generate`, which retires a superseded defer
> **＋** `estimate-estimates-schema-checked` — the promise of the file; its Criterion stands

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and an agent or the person reads the description of `## Criterion` in it.

> **then:**
> The description says that the Criterion holds no `Given:`, since the frame of the Case stays in its Case file and in the Spec.
> **＋** `generate` sets `decision-case-519` `superseded` and removes it from the `deferred_by` of `rule-estimates-schema`, so the backlog no longer holds the cut text; the cascade archives the page.
> **－** The lists that lint reads from `vault/wiki/estimates/schema.yaml` do not change.

```then
update:
- slug: rule-estimates-schema
  replace:
  - old: 'no `Given:`: the frame of the Case stays on its Decision page (case 378.2)'
    new: 'no `Given:`: the frame of the Case stays in its Case file and in the Spec (cases 378.2, 513)'
  change: 'the description of ## Criterion says the frame of a Case stays in its Case file and the Spec; the defer of case 519 retired (case 521.3)'
```

```tasks
- [ ] update `rule-estimates-schema`
- [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
```

### Case 521.4 — The short-form rule tells the agent to quote a value that holds a `#`

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `rule-spec-write` — the rule of the `Stop` hook that refuses a block with a comment

> **when:**
> The main agent reads `vault/wiki/case-schema.md` and then writes a short-form Case.

> **then:**
> The paragraph of the short form says that a value of the `then` block that holds a `#` after a space or a tab stands in quotes, since YAML reads the rest of the line as a comment, and that the `Stop` hook of `rule-spec-write` refuses a block that holds a comment.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend`
    new: a `then` block with `defer:` carrying `slug`, `type` and `purpose` — a value that holds a `#` after a space or a tab stands in quotes, since YAML reads the rest of the line as a comment and the `Stop` hook of `rule-spec-write` refuses a block that holds one (case 521.4); no `recommend`
  change: 'the short form quotes a value that holds a # after a space or a tab (case 521.4)'
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 522 — A repeat ticks no line of the Spec

> **context:**
> `guppi generate` writes the entries of `materialize.yaml` into the pages. After it applies an entry, it ticks the entry's line in the Spec beside the yaml. Case 514 made an entry a repeat when its `case`, `kind` and `slug` match those of an entry of the same yaml that is already applied. A repeat changes no page and prints `generate: <slug>: line N repeats line M of case C; nothing applied`. The built code still sends a repeat through the tick, and the handoff of session 1432 says so: "A repeat of Case 514 ticks its line of the Spec, as an applied entry does; the task line said "apply nothing"". In a real session this ticks nothing. When a Case is ratified again, the Spec holds it once with one line per page, so the first entry ticks that line and the repeat finds no open line. The tick only takes effect when a Case's section holds a second line of the same kind and slug. The test fixture of `tests/test_generate.py` holds such a line, `update `rule-root`: a second time`, and the test of two entries ticking two lines went red without the repeat's tick. A repeated `delete` also runs the tick of the `read` lines. It measures "ratified after it" from its own later ledger line, so it can tick a `read` line in a Case that was ratified between the two lines. No promise signed either tick. The person chose in the round that a repeat ticks nothing. `rule-page-generation` says the Spec's lines "are closed by the one who did the work", and a repeat does no work. The Criterion of `estimate-generate-ticks-the-spec` still says "Each further entry of one kind and slug in one Case ticks the next such line, in order". That sentence dates from case 226.1, before a second entry of one kind and slug in one Case became a repeat, so this Case replaces the Criterion whole. The rest of the Criterion stays word for word, with two changes. The trigger "applied an entry of `materialize.yaml` and marked it `applied`" now covers a repeat as well. The first line of the result is limited to an entry that was applied, and it loses its sentence on further entries. The docstring of `guppi/generate.py` says a repeat "ticks its line of the Spec as an applied entry does (case 514)" and "Two entries of one kind and slug tick two lines, in order", so both sentences change. The sentence of `rule-page-generation` "Once an entry is applied, the script ticks its line" does not exclude a repeat on its own. The same page says a repeat "is marked applied", and `estimate-generate-fails-alone` says it "is marked `applied`". Read alone, the sentence would therefore imply a tick. The page's sentence on Case 514 names the repeat, and this Case adds "ticks no line of the Spec" to it. That sentence settles the point for a repeat, so the general sentence stands as it is. `estimate-generate-fails-alone` stands. Its Criterion describes the repeat and says nothing of the Spec, so no sentence of it becomes false. `generate` is no hook, and it refuses nothing between the change of the code and the change of the text, so no old form is kept. The Case creates no page, so no vault query was needed. The reading of `estimate-generate-ticks-the-spec` waits for a later session, because the ledger hook refuses a reading of a page this session changes (case 428.1).

> **problem:**
> A repeat applies nothing, but it ticks a line of the Spec, and no promise names that tick. When a Case's section holds a second line of the same kind and slug, the repeat marks it as done although nobody did its work. A repeated `delete` can also tick a `read` line of a Case ratified after the first `delete`.

> **given:**
> `guppi/generate.py` — applies the entries and ticks the Spec
> **＋** `materialize.yaml` — the entries `generate` reads and marks
> **＋** `spec.md` — the Spec of a session folder under `vault/raw/`, whose lines `generate` ticks
> **＋** `vault/archive/` — the archived sessions, whose Specs `generate` does not read
> **＋** `tests/test_generate.py` — the tests of `generate`
> **＋** `rule-page-generation` — the rule of `generate`
> **＋** `estimate-generate-ticks-the-spec` — the promise on the ticks of the Spec

> **when:**
> `uv run guppi generate` marks an entry of `materialize.yaml` `applied`. Either it applied the entry, or it found the entry to be a repeat: a `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` already marked `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry that was applied, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes.
> **＋** For an `estimate` entry, a `create` entry with `folded` and a `delete` entry, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, for an `estimate` or a `delete` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
> **＋** A `delete` entry ticks both its page line in its own Case and the `read` lines of its slug.
> **－** A repeat ticks no line in any `spec.md`. A second line `` - [ ] <kind> `<slug>` `` in the section of its Case stays unticked, and a repeated `delete` leaves the `read` lines of its slug as they stand.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` that fails leaves the `read` lines of its slug as they stand.
> **－** A `spec.md` under `vault/archive/` is not read.

```then
update:
- slug: rule-page-generation
  replace:
  - old: is marked applied and changes no page, so a Case approved again
    new: is marked applied, changes no page and ticks no line of the Spec, so a Case approved again
  - old: changes each page once (case 514).
    new: changes each page once (cases 514, 522).
  change: a repeat ticks no line of the Spec (case 522)
- slug: estimate-generate-ticks-the-spec
  set:
    status: pending
  change: the Criterion replaced whole — a repeat ticks no line of any Spec; a second entry of one kind and slug in one Case no longer ticks the next line
```

```tasks
- [ ] update `rule-page-generation`
- [ ] update `estimate-generate-ticks-the-spec`
- [x] `guppi/generate.py`: in `apply`, the repeat branch no longer calls `vault.tick`. In the docstring, the repeat sentence says that a repeat ticks no line of the Spec, and the sentence "Two entries of one kind and slug tick two lines, in order" is removed.
- [x] `tests/test_generate.py`: the test of two entries of one kind and slug is rewritten. The first entry ticks its line, the second prints the repeat line, and the line `update `rule-root`: a second time` stays `- [ ]`. A new test: a `delete` in one Case, a later Case with a `read` line of its slug, and a repeat of the `delete` after that later Case. The `read` line of the later Case stays `- [ ]`.
- [ ] read `estimate-generate-ticks-the-spec`
```

## Case 523 — The question after a defer stands as written

> **context:**
> When the person puts off an item in Plan Mode, the agent answers in one reply. The reply holds a short Case, the Frontier with that line closed, and one question at the end. The question asks which open item is next. When no line under `## Cases` is open, it asks whether to run `/pre-spec` instead. The reading of `estimate-case-protocol-defers-in-one-reply` failed in session 1134. There the defer of Case 509 closed the last Cases line, and the question asked whether to take the open W readings, not whether to run `/pre-spec`. The text of `rule-case-protocol` was already right at that time. The gap was that the W readings had no set moment before Retro. That session filled the gap with case 508: a W line now closes at `/hi`, in Work Mode or at Retro. The item came to session 1432, and the person put it off as Case 518. In the same session, Cases 517 and 518 closed the last Cases line. That reply ended with the question whether to run `/pre-spec`, with no text after it. Nobody wrote a reading for it.
>
> In one round the person made two choices. The failure in session 1134 was a slip whose cause is gone, so the text of `rule-case-protocol` stays as it is. The `method` of the Estimate now names a defer that leaves no Cases line open, because only such a defer tests the question that failed.
>
> The frame and the vault's answer:
> - `rule-case-protocol` carries `deferred_by` Case 518. This Case retires that defer: its decision line names the page with `{supersedes:case 518}`, and the `update` has only a `change`.
> - Case 521.4 of this session changes the short-form paragraph of the same page. This Case changes no text there.
> - `rule-skill-hi` gives the W lines their moments, and the question in case 461 needs no change.
> - The `when` and `then` of this Case are the current Criterion of `estimate-case-protocol-defers-in-one-reply`, word for word. The promise is not signed in a second wording.
> - The Estimate update names the `method` alone. Under `rule-case-protocol` its Criterion and its `failed` status do not change. Because a decision line of this session updates the Estimate, its reading waits for a later session.
> - The new `method` keeps the `by hand` form of `vault/wiki/estimates/schema.yaml`, as the old one did. So a finding of lint on the form of a method of a MOC, if there is one, does not change.
> - No other Estimate of `rule-case-protocol` has a Criterion that speaks of the question after a defer. No hook changes, and the Case creates no page, so no vault query was run.
>
> Not done: no sentence on the W list is added to the Render. No hook checks the question.

> **problem:**
> The rule on the question after a defer is under a defer, and its Estimate reads as failed. The rule text was right, and the one wrong question came from a gap that is now closed. The `method` of the Estimate also lets a defer that leaves Cases lines open count as a reading, and such a defer never tests the question that failed.

> **given:**
> `rule-case-protocol` — the rule of the short-form Case and of the reply that shows a defer.
> **＋** `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, and the page whose `method` this Case sets.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows and the Cases lines the question looks at.
> **＋** `rule-spec-write` — the `Stop` hook that writes the short-form Case into the plan file and `spec.md`.
> **＋** `spec.md` — the Spec of the session, at `raw/<date>/<hi HHMM>/spec.md`.
> **＋** `/pre-spec` — the check the question offers.
> **＋** `rule-prespec` — the rule of that check.

> **when:**
> The person asks in the chat to defer an item, in Plan Mode or at Retro.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file or `spec.md`: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** In Plan Mode the reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** In Plan Mode a question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec` of `rule-prespec`.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows that question.
> **－** At Retro no Frontier is shown.

```then
update:
- slug: rule-case-protocol
  change: 'the defer taken up: the question after a defer stands as written, the failure of session 1134 a slip whose cause case 508 removed (case 523, supersedes 518)'
- slug: estimate-case-protocol-defers-in-one-reply
  set:
    method: 'by hand, the first defer the person asks for after the render that leaves no line under ## Cases of frontier.md open'
  change: the method reads a defer that closes the last Cases line, the branch that failed; the Criterion and the failed status stand (case 523)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-defers-in-one-reply`
- [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand in a later session after the render: the first defer that closes the last Cases line, read in the chat against the Criterion
```

## Case 524 — A quotation in a round stands as a blockquote on its own line

> **context:**
> When a round of questions quotes the words of a page, a file or a reply, the quoted words stand inline in plain double quotes. When the main agent shows the round in Russian, they stand in Russian angle quotes. So the quoted words do not stand apart from the agent's own words. Here is an example from the first round on Case 521: *The parser kept only "Correct the description of".* The four quoted words are a fragment of a page, but they read like part of the agent's sentence. The person saw this in the rounds of this session and said, translated from the chat, that the quotations "are not formatted as quotations" and that this should be fixed. Rounds quote pages often since case 512, which lets a number stand in a round only beside a quotation of the words it points to.
> In one round the person decided the following:
> - Every quotation stands as a blockquote on its own line, a fragment of a few words too.
> - The rule is for rounds only. It covers the rounds of `case-guppi` and the person's own `/grill-me`, so it is set in the grill-me template.
> - When the main agent shows a round in Russian, it keeps the blockquote and the quoted words as the source holds them.
>
> The person asked to see an example before ratifying. The example is the new text of the template in 524.1: the `new` of its first and second pairs. The first pair puts a quotation under the `**Now:**` line. The second puts one inside an `**After:**` item. In a round the `**After:**` item is written `  - **After:** …`, so its text begins four spaces in. A blockquote line indented four spaces, `    > …`, renders inside that item. With no indentation it would end the list. In the template both lines carry the four extra spaces of the code block that holds the template.
>
> Pre-spec found a fault in the first ratified text, and the person accepted the fix. In the person's words, translated from the chat: "Okay, I agree with the recommendations". 524.1 had put the third decision into the grill-me skill. But the main agent shows a round of `case-guppi` by `vault/wiki/case-schema.md`, the Render of `rule-case-protocol`: "translated into {{chat_lang}} line by line, slugs, paths and quotations unchanged". So the decision stood in a file the main agent does not read at the showing, and `estimate-case-protocol-shows-the-built-case`, which promises that showing, was named by no Case. The new sub-case 524.3 adds "each quotation in its blockquote" to that sentence and replaces the Criterion of that Estimate whole. 524.1 no longer holds the sentence on the showing, in the skill or in its Criterion. The showing is signed once, in 524.3, and the person's own `/grill-me` is not translated. Cases 521.4 and 523 of this plan also update `rule-case-protocol`. 521.4 changes a pair in the short-form paragraph, and 523 has only a `change`. The `old` of 524.3 is in the paragraph on who builds a Case, so it overlaps neither.
>
> What `case-guppi` found in the frame. `rule-case-build` says that the first round opens with "one prose paragraph under the label `**Context:**`" and that "A list in the context stands as the grill-me template sets a list". The example of this item stands in a Context, so 524.2 lets a quotation there stand as the template sets it too. The prose goes on after the blockquote, as it does after a list. Its Estimate, `estimate-case-build-writes-a-plain-round`, reads the Context and the instructions that point to the template, so its Criterion is replaced whole. `estimate-skill-grill-me-asks-in-rounds` reads the shape of a question, so 524.1 replaces its Criterion whole and adds a line on the quotation.
> The check of the answer notes four lines that are not carried word for word. Each one changes on purpose:
> - In 524.1, "The `**Context:**` paragraph of a round of `case-guppi`, its lists included…" now says "its lists and quotations included". The quotations of the Context are read by the Estimate of 524.2.
> - In 524.2, "The instructions of `case-guppi` point each question, and each list of the Context…" now names each quotation of the Context too.
> - In 524.2, "The shape of a question, and what counts as a list, are read by `estimate-skill-grill-me-asks-in-rounds`…" now names the form of a quotation in a question too.
> - In 524.3, "An answer with no Case heading and no first line `**Fact:**` is a round of questions…" now adds "each quotation in its blockquote" after "quotations unchanged". The rest of the line is the same.
>
> Every other line is carried word for word. The check also notes `then` lines of sibling sub-cases that share words: two lines of 524.2 with a line of 524.1, and the showing line of 524.3 with a line of 524.1 and a line of 524.2. The shared words are the path `.claude/skills/grill-me/SKILL.md`, "quotation", "blockquote" and common words. The 524.1 line promises that the skill asks for no sub-agent. The 524.2 lines promise the form of a list and of a quotation in the Context that `case-guppi` writes. The 524.3 line promises what the main agent keeps when it shows a round. These are separate promises with separate readings. The line "only beside a short quotation of the words it points to" stays true: the number stands in the sentence that introduces the blockquote.
> Several sentences stay true and stand:
> - `rule-language` keeps "quotations from pages" as they are. This agrees.
> - The template's "An option has nothing else under it" stays true: the blockquote stands inside the `**After:**` item, not as a second item.
> - The `"nothing exists yet"` of the template is a phrase to write, not a quotation of a source.
>
> No code reads a round. A search of `guppi/` for "round" finds only unrelated lines in `lint.py` and `render.py`, so no reader keeps an old form. The Case creates no page, so no vault query was run.
> Not done: the `context`, `problem` and `recommend` of a Case, the main agent's own chat text, and a mechanical check of a round. The person chose rounds only.

> **problem:**
> The quoted words of a page or a reply stand inside the agent's sentence in quote marks. The person cannot tell at a glance what the page says and what the agent says about it. No text of the harness sets a form for a quotation in a round.

### Case 524.1 — The grill-me template sets a quotation as a blockquote on its own line

> **given:**
> `rule-skill-grill-me` — the rule; its Render is the grill-me skill and its question template
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise on the shape of a round; its Criterion is replaced whole
> **＋** `rule-case-protocol` — the case schema, which sets how the main agent shows a round of `case-guppi`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
> **＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` item it stands indented to the text of the item, inside that item, and is no second item.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-case-protocol`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
update:
- slug: rule-skill-grill-me
  replace:
  - old: '"nothing exists yet" when nothing does>'
    new: |-
      "nothing exists yet" when nothing does>
          <a sentence that introduces a quotation and names its source, when the question quotes one>:
          > <the quoted words, as the source holds them>
  - old: |-
      **After:** <what holds with this option>

          🔹 **(b) <option name>**
    new: |-
      **After:** <what holds with this option>
              > <a quotation inside the item, indented four spaces as far as the text of the item>

          🔹 **(b) <option name>**
  - old: In the recommended answer it stands on the lines under `➡️`, which close the question.
    new: |-
      In the recommended answer it stands on the lines under `➡️`, which close the question.

      A quotation — words taken from a page, a file or a reply to show what they say — stands as a blockquote on its own line, a fragment of a few words too; it never stands inside a sentence in quote marks. The sentence that introduces it stands on the line before it and names its source, and the quoted words stand as the source holds them. In the `**Now:**` text the blockquote stands under the sentence that introduces it. Under an `**After:**` item it stands inside that item, indented four spaces as far as the text of the item, so that it renders there and is no second item. In the recommended answer it stands on the lines under `➡️`.
  change: a quotation in a round stands as a blockquote on its own line, inside an After item indented to its text (case 524.1)
- slug: estimate-skill-grill-me-asks-in-rounds
  set:
    status: pending
  change: the Criterion replaced whole — a quotation stands as a blockquote on its own line (case 524.1)
```

```tasks
- [ ] update `rule-skill-grill-me`
- [ ] update `estimate-skill-grill-me-asks-in-rounds`
- [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
- [ ] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: `uv run guppi render --check`, then one round that quotes a page read in the chat against the Criterion
```

### Case 524.2 — A quotation in the Context of a first round stands as the template sets it

> **given:**
> `rule-case-build` — the rule page whose Render holds the round instructions of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from it
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets a list and a quotation
> **＋** `estimate-case-build-writes-a-plain-round` — the promise on a readable round; its Criterion is replaced whole
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape of a question, a list and a quotation
> **＋** `rule-case-protocol` — the rule that lets the story sections of a Case keep their numbers

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
> **＋** A quotation in the `**Context:**` stands as a blockquote on its own line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a quotation.
> **＋** The instructions of `case-guppi` point each question, and each list and each quotation of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** The round says what it rests on in plain words and uses no number where plain words are enough.
> **＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** A page name in a code span is no such reference: it stays where the question is about that page.
> **－** The shape of a question, what counts as a list, and the form of a quotation in a question are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

```then
update:
- slug: rule-case-build
  replace:
  - old: A list in the context stands as the grill-me template sets a list.
    new: A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it.
  change: a quotation in the Context of a first round stands as the grill-me template sets it (case 524.2)
- slug: estimate-case-build-writes-a-plain-round
  set:
    status: pending
    purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a quotation in the Context as a blockquote, a number only beside a quotation of what it points to, and an unknown term explained
  change: the Criterion replaced whole — a quotation in the Context stands as the grill-me template sets it (case 524.2)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-a-plain-round`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round that quotes a page and one later round of `case-guppi` read in the chat against the Criterion
```

### Case 524.3 — The main agent shows a round with each quotation in its blockquote

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema, which sets how the main agent shows a round
> **＋** `vault/wiki/case-schema.md` — the file rendered from it, read by the main agent
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise on the showing; its Criterion is replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets the shape of a question and a quotation
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill by which the main agent answers a request for a plain explanation
> **＋** `rule-case-check` — the rule whose hook writes the Case file the main agent sends
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the Case file the main agent sends at a showing

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: line by line, slugs, paths and quotations unchanged — the
    new: line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the
  change: the main agent shows a round with each quotation in its blockquote (case 524.3)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — a round shown with each quotation in its blockquote (case 524.3)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-shows-the-built-case`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-shows-the-built-case` — in a later session after the render: one round of `case-guppi` that quotes a page, read in the chat against the answer and the Criterion
```

## Deferred

## Case 525 — The librarian's reading beyond its input list is put off again

> **context:**
> `estimate-documentation-completes` failed: the librarian's run of ff62585 read beyond its input list. It read the tail of `log.md`, the head of the old `brief.md`, a git diff of `sprint.md` and `backlog.md`, and a grep of `sprint.md`. Case 517 of session 1432 put the item off. The run d8c1f17 of that session reported two more breaks of its own. It listed a folder under `vault/archive/`, and it read the head of the old `brief.md`. The person put the item off again at the close of Plan Mode in session 1753.

> **problem:**
> The librarian reads files outside its input list, and `estimate-documentation-completes` stays failed.

```then
defer:
  - slug: rule-documentation
    type: rule
    purpose: "The librarian reads beyond its input list: the run ff62585 read the tail of log.md, the old brief.md, git diffs and a grep of sprint.md; the run d8c1f17 listed an archive folder and read the old brief.md; estimate-documentation-completes stays failed"
```
