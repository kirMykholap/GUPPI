<!-- approved 17:38:08 · session 649bc920 -->

# Spec — 2026-09-15, session R (`raw/2026-09-15/1448/`)

## Case 164 — `rule-page-generation`: an Insight created by the librarian at synthesis passes through `generate`

> **context:**
> `rule-synthesis` tells the librarian, on the second lesson with the same root cause, to append to `materialize.yaml` a `create` in `insights` marked `librarian: synthesis` and one `update` per lesson. `guppi generate` lays the yaml entries into pages. Case 124.2 made an Insight the target of `update` and `defer` and fixed: "an Insight is neither created nor deleted through the yaml: a `create` or `delete` with an Insight as its target is a `generate` error". The code refuses every `create` in `insights` before it looks at the `librarian` mark. The last synthesis that applied — `insight-ledger-hi-tied-to-its-session-by-position` in `0747` — ran before 124.2. In the run of session Q the entry `insight-retro-typed-command-is-never-a-tool-call` was refused, and the two lesson `update`s applied before the refusal.

> **problem:**
> `rule-synthesis` and block 124.2 contradict each other: the rule tells the librarian to create an Insight by a yaml entry, the contract of `generate` forbids it; two retro lessons stand `clustered` with an `insight` that names no page — 2 `ref` findings.

> **given:**
> `rule-page-generation` (`built`, `check`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`, both `passed`): the text of the rule does not name the Insight refusal; it lives only in the code and in block 124.2 of `estimate-generate-writes`.
> **＋** `generate.create` refuses the whole category `insights` with the line `LIBRARIAN_ONLY`; `generate.delete` too; `generate` reads the `librarian` mark nowhere.
> **＋** A synthesis entry: `kind: create`, `category: insights`, `origin` the lesson's ledger line, `librarian: synthesis`, no `line` and no `case`; a decision entry carries `line`, `case`, `decision`.
> **＋** `tests/test_generate.py`: the test of 124.2 refuses a `create` of an Insight with `line` and `case`; no test seeds an entry with `librarian`.
> **＋** An entry with `failed` and `kind` is retried by the next run of `generate`; the mark is dropped on apply (53.3).
> **＋** `rule-synthesis` Render: "append to the yaml a `create` in `insights`…"; `insights/schema.md`: "Created by the librarian, never by a decision".
> **－** `decision-case-124.2` is an `update` of one page, no `defer`; the supersedes clears nothing from `deferred_by`.

> **when:**
> `guppi generate` applies a yaml entry whose target is a page of `insights/`.

> **then:**
> A `create` in `insights` marked `librarian` writes the page as any `create`: `status: open`, `severity` from the count of `children`, the entry's `origin`, `## Pattern`, `## Proposal`, `## Children` from the fields; History `created · <origin>`.
> **＋** A `defer` with an Insight as its target appends the decision slug to its `deferred_by`, as for a Rule; a `supersedes` removes it through `clear_deferred_by`.
> **＋** An `update` with `set: {addressed_by: decision-case-N}` writes the field, and on every write of an Insight page the `## Addressed by` section is derived from the field; without the field there is no section.
> **＋** An `update` with `set: {status: actioned}` goes as any `update`; the cascade of the same run archives the `clustered` children and recounts `severity`.
> **－** A `create` in `insights` without the `librarian` mark — from a ledger line — is refused as today; a `delete` of an Insight is refused always: an Insight goes to the archive by the cascade.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "Any other existing page is a collision (case 101.1)."
        new: "Any other existing page is a collision (case 101.1). A `create` in `insights/` from a ledger line is refused — an Insight is made by the librarian, never by a decision; a `create` the librarian appended at synthesis, marked `librarian`, applies as any create, its `origin` the lesson line it grew from; a `delete` of an Insight is refused always: the cascade archives it (case 164, supersedes 124.2)."
    change: "a synthesis create of an Insight, marked librarian, applies; a create from a ledger line and every delete stay refused; supersedes 124.2 (case 164)"
```

```tasks
- [ ] superseded by 166.2 before the librarian's run (found at pre-task, Case 171): no entry of this Case applies, block 164 never exists; the code tasks and the reading go under 166.2, the sentence and the removal of block 124.2 under 171
```

## Case 166 — `rule-page-generation`: the derived sections are dropped

> **context:**
> Seven body sections repeat a ref field of the frontmatter: on a Rule and an Entity `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`; on a Lesson `## Insight`; on an Insight `## Children`, `## Addressed by`. `generate` writes them at `create`, rebuilds two on `update`, derives two on every write and fills one by the cascade; `cleanup` rebuilds two when an archived page leaves the lists; four schemas require them; `lint` requires what the schema requires and checks `schema.md` against `schema.yaml`. The sections were born when the fields were bare slugs Obsidian did not see. Since 148.1 the fields are `"[[slug]]"`, and the graph, backlinks and Bases see them on their own; `target` of an Estimate has lived without a section from birth. Five live pages show a section that differs from its field. Case 165.2 deferred the removal; this Case takes it up.

> **problem:**
> A copy of a field in prose drifts, needs code in three scripts and lines in four schemas, and gives the reader nothing since 148.1; the removal touches four schemas, `generate`, `cleanup`, the tests and every live and archived page, and lifts parts of the contracts of 114 and 164.

> **given:**
> `rules/schema.yaml` and `entities/schema.yaml`: `## Estimates` required, `## Children`/`## Parent` conditional on `kind`, `## Implementation` conditional on `enforcement`, `## Code` optional; `lessons/schema.yaml`: `## Insight` conditional on `status: clustered`; `insights/schema.yaml`: `## Children` required, `## Addressed by` optional; `estimates/` and `decisions/` have no derived section.
> **＋** The `schema.md` of the four categories carry the rows of these sections in the Body table and in the examples; `lint` compares the section names of `schema.md` and `schema.yaml` and requires only the required sections — it does not name a section a page carries beyond the schema.
> **＋** `generate`: `SECTION_ORDER` lists the seven sections; `create` writes five from the fields; an `update` with `set` on `children`/`estimates` rebuilds the section; `save` derives `## Insight` and `## Addressed by`; the cascade walks the live lessons and writes `## Insight` with History `insight section derived` (114).
> **＋** `estimate-generate-writes`: block 114 — `## Insight` from the field and the cascade; block 164 (`pending`, this session) — the librarian's `create`, `defer` on an Insight, `addressed_by` and the `## Addressed by` section, `actioned` with the cascade, the refusals.
> **＋** `cleanup.unlink`: removes an archived slug from `children`/`estimates` of the live pages, rebuilds the section, writes History `child <slug> archived` / `estimate <slug> archived`; `rule-cleanup` (`built`, `estimates: [estimate-cleanup-moves]`, `passed`) says "their sections are rebuilt".
> **＋** The migration of 148.1: a script from the scratchpad, `read_page` → `write_page` over `wiki/**` and `archive/**`, no History lines, checked by `lint`, `render --check`, `git diff --stat`.
> **＋** Tests that name the sections: `test_generate.py` 11 places, `test_lint.py` 9, `test_cleanup.py` 2, `test_render.py` 1.
> **－** `## Purpose`, the `## Criterion` of a Decision page, `## History` and the History lines about fields are not touched; `docs/migration/rule-*.md` are drafts, their fate in Slice 5; `lint`, `materialize`, `ask-guppi`, `index` read no section — their contracts do not change.

### Case 166.1 — the four schemas without the derived sections

> **when:**
> `lint` reads the `schema.yaml` of a category, or a person reads its `schema.md`.

> **then:**
> `rules/schema.yaml` and `entities/schema.yaml` name none of `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code` in `required`, `optional` or `conditional`; `lessons/schema.yaml` not `## Insight`; `insights/schema.yaml` not `## Children` or `## Addressed by`; the `children` of an Insight are required by the field alone.
> **＋** In the four `schema.md` the rows of these sections leave the Body table and the example pages; the row of the field says the field is the link.
> **－** The other sections and every field stay as today.

```then
update:
  - file: vault/wiki/rules/schema.yaml
    change: "## Estimates, ## Children, ## Parent, ## Implementation leave required, optional and conditional (case 166.1)"
  - file: vault/wiki/rules/schema.md
    change: "the rows ## Estimates, ## Children, ## Parent, ## Implementation leave the Body table and the examples; the field rows say the field is the link (case 166.1)"
  - file: vault/wiki/entities/schema.yaml
    change: "## Estimates, ## Children, ## Parent, ## Code leave required, optional and conditional (case 166.1)"
  - file: vault/wiki/entities/schema.md
    change: "the rows ## Estimates, ## Children, ## Parent, ## Code leave the Body table and the examples; the field rows say the field is the link (case 166.1)"
  - file: vault/wiki/lessons/schema.yaml
    change: "## Insight leaves optional and conditional (case 166.1)"
  - file: vault/wiki/lessons/schema.md
    change: "the row ## Insight leaves the Body table and the example; the insight field row says the field is the link (case 166.1)"
  - file: vault/wiki/insights/schema.yaml
    change: "## Children and ## Addressed by leave required and optional (case 166.1)"
  - file: vault/wiki/insights/schema.md
    change: "the rows ## Children and ## Addressed by leave the Body table and the example; the field rows say the field is the link (case 166.1)"
```

```tasks
- [x] `vault/wiki/rules/schema.yaml`, `rules/schema.md`, `entities/schema.yaml`, `entities/schema.md`, `lessons/schema.yaml`, `lessons/schema.md`, `insights/schema.yaml`, `insights/schema.md` — by hand in Work Mode, as the `then` block says
- [x] `tests/test_lint.py`: the schema copies in the tests without these sections
- [x] read: `uv run guppi lint` — no `schema-prose` finding, the count of findings does not grow
```

### Case 166.2 — `generate` writes no derived section; the migration

> **when:**
> `guppi generate` writes a page of any category, or applies a yaml entry whose target is a page of `insights/`.

> **then:**
> Neither at `create`, nor at `update`, nor in `save` does `generate` write `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`, `## Insight` or `## Addressed by`; a section a page still carries is neither touched nor derived again on a write; `SECTION_ORDER` does not know them.
> **＋** A `create` with `ref` still appends the slug to the parent's `children` or to the target's `estimates`, History `child <slug> added` / `estimate <slug> added`; an `update` with `set` on a field writes the field.
> **＋** A `create` in `insights` marked `librarian` writes the page as any `create`: `status: open`, `severity` from the count of `children`, the entry's `origin`, `## Pattern` and `## Proposal` from the fields; History `created · <origin>`.
> **＋** A `defer` with an Insight as its target appends the decision slug to its `deferred_by`; a `supersedes` removes it through `clear_deferred_by`.
> **＋** An `update` with `set: {addressed_by: decision-case-N}` writes the field — and only the field.
> **＋** An `update` with `set: {status: actioned}` goes as any `update`; the cascade of the same run archives the `clustered` children and recounts `severity`.
> **－** A `create` in `insights` without the `librarian` mark is refused; a `delete` of an Insight is refused always.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "Body sections follow the order of the category's `schema.yaml`: `Purpose` from `sections` or the `purpose` line; `Estimates`, `Children` (numbered for a rule), `Parent`, `Implementation` from the fields; `Render`, `How it works`, `Context`, `Criterion`, `Method`, `Result`, `Trigger`, `Root cause`, `Pattern`, `Proposal` from `sections` or the estimate's fields."
        new: "Body sections follow the order of the category's `schema.yaml`: `Purpose` from `sections` or the `purpose` line; `Render`, `How it works`, `Context`, `Criterion`, `Method`, `Result`, `Trigger`, `Root cause`, `Pattern`, `Proposal` from `sections` or the estimate's fields. No section is derived from a ref field: `estimates`, `children`, `parent`, `implementation_ref`, `code_ref`, `insight` and `addressed_by` are the link, seen by Obsidian since 148.1, and a section a page still carries is left as it is (case 166.2)."
      - old: "A `create` with `ref` appends the slug to the parent's `children` (order kept) or, for an estimate, to the target's `estimates`, and rebuilds that section;"
        new: "A `create` with `ref` appends the slug to the parent's `children` (order kept) or, for an estimate, to the target's `estimates`;"
      - old: "an insight whose `addressed_by` is set gets `## Addressed by` holding the link the same way, rebuilt from the field on every write, and an `update` that sets `status: actioned`"
        new: "an `update` that sets `addressed_by` writes the field, and an `update` that sets `status: actioned`"
    change: "no derived section on any write; the Addressed by derivation of 124.2/164 removed; the migration over wiki/ and archive/; supersedes 164 (case 166.2)"
```

```tasks
- [x] `guppi/generate.py`: `SECTION_ORDER`, `create`, `rebuild_list`, `derive_insight`, `derive_addressed_by`, `save` — no section written; the cascade step of 114 goes by 166.3
- [x] `tests/test_generate.py`: the section tests (114, the `## Addressed by` of 124.2, the list rebuilds, `## Parent`) rewritten on the fields; a test: a page with an old section keeps it untouched after an `update`
- [x] `guppi/generate.py`: `create` lets an `insights` entry carrying `librarian` through; the refusal line stays for a decision entry; `delete` unchanged (the code of 164, superseded before it applies)
- [x] `tests/test_generate.py`: a synthesis entry (no `line`, `librarian: synthesis`, `origin` a lesson line) writes the page `open`, `severity` 2, `## Pattern` and `## Proposal`; the test of 124.2 kept
- [ ] `rule-page-generation` `update`, `contract: changed`, the three `replace` above; `estimate-generate-writes` block 166.2, `pending`; `{supersedes:case 164}` marks the entries of 164 superseded — block 164 never exists, block 124.2 is removed by 171
- [ ] read, on the same block: the librarian's run of this session retries the `failed` entry of `1110/materialize.yaml` — `insight-retro-typed-command-is-never-a-tool-call` written, `severity` 2, the 2 `ref` findings gone
- [x] one-off migration from the scratchpad: for every `*.md` under `vault/wiki/<category>/` and `vault/archive/**/<category>/` (`rules`, `entities`, `lessons`, `insights`) — `read_page`, the seven sections removed, `write_page`; no History line; then `guppi lint` (no more findings than before), `guppi render --check` exit 0, `git diff --stat`
- [ ] read `estimate-generate-writes` (block 166.2): the tests green; the librarian's run of this session writes pages without these sections — `insight-retro-typed-command-is-never-a-tool-call` with `## Pattern`, `## Proposal`, no `## Children`; in Obsidian the backlinks of one Rule and one Insight in place
```

### Case 166.3 — the cascade derives no `## Insight`

> **when:**
> The cascade of `guppi generate` runs after all entries.

> **then:**
> The cascade does not walk the lessons for `## Insight`; a lesson's `insight` field is its one link to its Insight; the History line `insight section derived` is written no more.
> **－** The other steps of the cascade — `built`/`draft`, the archive of a superseded decision, `severity`, the children of an `actioned` Insight, an Insight with no live child — as today.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "a lesson whose `insight` field is set gets `## Insight` holding the link, rebuilt from the field on every write, and the cascade fills it on every live lesson that carries the field without the section, History `insight section derived` (case 114);"
        new: "a lesson's `insight` field is its one link to its Insight, and the cascade derives no section from it (case 166.3, supersedes 114);"
    change: "the cascade step of 114 removed: no ## Insight derived on lessons; supersedes 114 (case 166.3)"
```

```tasks
- [x] `guppi/generate.py`: the cascade step of 114 removed
- [x] `tests/test_generate.py`: the test of 114 replaced by: a lesson with `insight` and no section stays without one after the cascade
- [ ] `rule-page-generation` `update`, `contract: changed`, the `replace` above; `estimate-generate-writes` block 166.3, `pending`; `{supersedes:case 114}` removes block 114
- [ ] read `estimate-generate-writes` (block 166.3): the test green; after the librarian's run no new `insight section derived` line in `log.md`
```

### Case 166.4 — `cleanup` edits the field only

> **when:**
> `guppi cleanup` moves a page to the archive and removes its slug from the lists of the live pages.

> **then:**
> `unlink` removes the slug from `children` and `estimates` and writes History `child <slug> archived` / `estimate <slug> archived`; it rebuilds no section and touches none.
> **－** What goes to the archive, what comes back and where — as today.

```then
update:
  - slug: rule-cleanup
    contract: changed
    replace:
      - old: "their sections are rebuilt and they get a History line"
        new: "they get a History line"
    change: "unlink edits the field only, no section rebuilt (case 166.4)"
```

```tasks
- [x] `guppi/cleanup.py`: `unlink` without the section rebuild
- [x] `tests/test_cleanup.py`: the two section tests rewritten on the field
- [ ] `rule-cleanup` `update`, `contract: changed`, the `replace` above; `estimate-cleanup-moves` block 166.4, `pending`
- [ ] read `estimate-cleanup-moves` (block 166.4): the tests green; the librarian's run — `cleanup` moves `decision-case-164`, `decision-case-114`, `decision-case-165.2`; the pages that lost a slug carry no rebuilt section
```

## Case 167 — `rule-case-protocol`: the `LEDGER` block opens the acknowledging reply

> **context:**
> The reply that acknowledges a ratification has four parts in a fixed order (157): the heading `## Case N — ratified` with a **Changes** paragraph, a **Notes** paragraph, the heading `## Frontier` with the checklist and the question, and the `LEDGER` block last. The `Stop` hook reads the whole text of the reply and takes the record lines from any fenced block tagged `LEDGER`, wherever it stands; its one demand is that no tool call follows the text (122). The place of the block in the text does not matter to the hook: "last" was a choice of form in 157, not a technical need. For the reader the block at the bottom sits after the question "which item is next", so the record comes after the conversation.

> **problem:**
> The order of the parts: the record block at the bottom, after the question, or at the top, before the account of the changes.

> **given:**
> `rule-case-protocol` (`draft`, `render` → `CLAUDE.md`, `estimates: [estimate-case-protocol-loaded]`; blocks 157 and 159 read `passed` today): the paragraph "The reply that acknowledges a ratification has four parts…" ends "the `LEDGER` block, last".
> **＋** `guppi/ledger.py`: the record lines are taken from a fenced block tagged `LEDGER` anywhere in the text; `last_assistant_message` and the transcript of the window are read.
> **＋** `rule-ledger-write` (122): the text before a tool call is never kept; a reply with a block ends in text — a block at the top does not break this.
> **－** `rule-ledger-write`, `guppi gate`, the form of a Case (159) and the short form of a defer do not change.

> **when:**
> The owner answers a Case with a ratification; the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order: the `LEDGER` block first; the heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; the heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last.
> **＋** The headings and labels are in the language of the chat.
> **－** The replies on readings and lessons, the reply that carries a Case and the short form of a defer stay as today; no tool call follows the block in the same reply.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "The reply that acknowledges a ratification has four parts, in this order: a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next; the `LEDGER` block, last. Headings and labels in the language of the chat (case 157)."
        new: "The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last. Headings and labels in the language of the chat (case 167, supersedes 157)."
    change: "the LEDGER block opens the acknowledging reply, the question closes it; supersedes 157 (case 167)"
```

```tasks
- [ ] `rule-case-protocol` `update`, `contract: changed`, the `replace` above; `estimate-case-protocol-loaded` block 167, `pending`; `{supersedes:case 157}` removes block 157
- [ ] `CLAUDE.md`: the librarian's render, not touched by hand
- [ ] read `estimate-case-protocol-loaded` (block 167): the next session, the first acknowledging reply after the render — the block first, the question last
- [x] no code and no test: the hook reads the block anywhere in the text
```

## Case 168 — `rule-brief`: the section "Readings due"; the Insight actioned

> **context:**
> `insight-librarian-frame-omits-required-reads` is the pattern "the frame of the librarian names the reads one by one, and the list is shorter than the judgments"; Case 143 closed it as `actioned`: the four reasons of the frame are one clause per judgment, nine runs without a recurrence. The librarian of session Q reopened it with a third lesson, `lesson-brief-next-section-has-no-source`: the Render of `rule-brief` gives a source to four of the five sections of the brief, and none to "What the next session does first". The librarian then copies the section from the previous brief and strikes nothing off: the reading of `estimate-brief-written` (124.1) stood in the section through three briefs after it passed. The brief of this session was built the same way — from the "Not done" of the handoff and the state after the run — but the rule does not ask for it. The Insight stands first in the Deferred list, severity 1.

> **problem:**
> Accept the librarian's clustering — a section without a source is the same gap of the frame — and close the Insight with the fix; or reject it and leave the lesson on its own. And what the section is for: the owner wants a section that names the Estimates left to read.

> **given:**
> `rule-brief` (`built`, `render` → `.claude/agents/librarian-guppi.md`, `estimates: [estimate-brief-written]`, `passed` on 124.1): in the Render "Where things stand" is sourced from the "What actually got done" of the handoff, which holds "what is not done", and the counts of the yaml; Deferred, Flags and Readings at the close have their sources; "What the next session does first" has none.
> **＋** "Readings at the close" already lists the `pending` and `failed` Estimates by slug; the Spec of the session carries one `- [ ] read …` line per reading with the place and the way.
> **＋** `insight-librarian-frame-omits-required-reads`: `open`, `severity` 1, `addressed_by: decision-case-143`, three children — two in the archive, `lesson-brief-next-section-has-no-source` `clustered`; History: reopened 2026-09-15.
> **＋** `generate`: an `update` of an Insight with `status: actioned` goes as any update; the cascade archives the `clustered` children and recounts `severity`.
> **＋** The model of 143: `set: {status: actioned, addressed_by: decision-case-143}`.
> **－** `rule-skill-hi` assembles the Frontier from the whole brief — unchanged; the other rules that name a read are unchanged.

> **when:**
> The librarian writes `brief.md` by its frame.

> **then:**
> The second section of the brief is "Readings due": after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per `### case N` block: the Estimate, the block, the rule that stands `draft`, and where it is read — from the unticked `- [ ] read …` line of the session's Spec, or from the `Method` of the page when there is none.
> **＋** A `failed` one stands first, with the result of its reading in one line.
> **－** Nothing from the previous brief; the "not done" of the handoff stays in "Where things stand"; the section "What the next session does first" is retired.

```then
update:
  - slug: rule-brief
    contract: changed
    replace:
      - old: "- What the next session does first."
        new: "- Readings due: after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per `### case N` block: the Estimate, the block, the rule that stands `draft`, and where it is read, from the unticked `- [ ] read …` line of the session's `spec.md` or, when there is none, from the `Method` of the page; a `failed` one first, with the result of its reading in one line; nothing from the previous brief (case 168)."
    change: "the second section is Readings due, sourced from the pending and failed Estimates after the run and the Spec's reading lines; What the next session does first retired (case 168)"
  - slug: insight-librarian-frame-omits-required-reads
    set: {status: actioned, addressed_by: decision-case-168}
    change: "actioned: the one section of the brief without a source gets one — Readings due, from the Estimates left pending or failed and the Spec's reading lines (case 168)"
```

```tasks
- [ ] `rule-brief` `update`, `contract: changed`, the `replace` above; `estimate-brief-written` block 168, `pending`
- [ ] `insight-librarian-frame-omits-required-reads` `update`: `status: actioned`, `addressed_by: decision-case-168`; the cascade archives `lesson-brief-next-section-has-no-source`
- [ ] `.claude/agents/librarian-guppi.md`: the librarian's render
- [ ] read `estimate-brief-written` (block 168): the brief of this session's run — "Readings due" names exactly the `pending`/`failed` Estimates after the run (166.2, 166.3, 166.4, 167, 168, 150), each with its place of reading from the Spec, nothing from the brief of Q
- [x] no code and no test
```

## Case 169 — a typed `/retro` passes through the gate

> **context:**
> `guppi gate` is the `PreToolUse` hook on the `Skill` tool: before `/pre-task`, `/retro` and `/handoff` it checks the Spec against the ledger (122), for `/handoff` the cleanness of the tree, and, letting the call through, leaves the mark `retro`/`handoff`/`pretask` in the event log (136.1). It sees only calls through the `Skill` tool — the agent's way of calling a skill. When the person types the command, the client expands it into the prompt, no tool is called, and no `PreToolUse` hook sees it. Case 150 removed `disable-model-invocation` and signed that both paths go through `Skill`; the reading showed the opposite: the typed `/retro` without a mark and without the gate, the agent's call with both. Two lessons and the refused Insight name one cause and propose one thing: a typed command has an event of its own — `UserPromptSubmit`, where `guppi event prompt` already reads the prompt for `/hi`. By the hooks reference of Claude Code a `UserPromptSubmit` hook with exit 2 blocks the prompt and shows its stderr to the person.

> **problem:**
> A typed `/retro` or `/handoff` bypasses the check of the Spec against the ledger and the mark; `rule-retro` stands `draft` on the false block 150.

> **given:**
> `rule-retro-commit` (`built`, `hook`, `implementation_ref: [guppi/gate.py, tests/test_gate.py, .claude/settings.json]`, `estimates: [estimate-retro-commit-gates]`): "It sees only calls made through the `Skill` tool … the handoff skill checks the tree itself for the case where the person types it".
> **＋** `gate.run`: `skill_of(payload)` reads `tool_input.skill`; without it exit 0; `spec_check`, `dirty` and `mark` are functions bound to no payload type.
> **＋** `rule-hook-registry` (`built`, `render` → `.claude/settings.json`): `UserPromptSubmit` carries one command, `uv run guppi event prompt`; the hooks of one event run in list order.
> **＋** `rule-event-log`: "The hook never fails the session … exit code is 0"; the paragraph on the marks names `guppi gate` on `PreToolUse Skill`.
> **＋** `rule-ledger-write` (122): the paragraph on the gate names `PreToolUse Skill` and the refusal text "end this reply in text with the LEDGER block, then call /<skill> in the next reply".
> **＋** `rule-retro` (`draft`, `render` → `SKILL.md`, `estimates: [estimate-retro-loads]`, `failed` on 150): block 150 — "the call goes through the Skill tool" for both paths; the Result — the typed path without mark and gate.
> **＋** The hooks reference of Claude Code: the `UserPromptSubmit` payload carries `prompt`; exit 2 blocks the prompt and shows stderr to the person; stdout goes to the context.
> **＋** `tests/test_gate.py`: payloads with `tool_name: Skill`; a payload with `prompt` is not tested.
> **－** `guppi event prompt` and `/hi` do not change; the tree check inside the `/handoff` skill stays as a second net.

### Case 169.1 — `guppi gate` reads a typed command

> **when:**
> The `UserPromptSubmit` hook calls `guppi gate` with a payload whose `prompt`, trimmed, is `/pre-task`, `/retro` or `/handoff`, with or without arguments.

> **then:**
> The gate makes the same checks as for a call through `Skill`: the Spec against the ledger of the session; for `/handoff` the cleanness of the tree; letting it through, it writes the same mark `pretask`/`retro`/`handoff` into the event log.
> **＋** A refusal is exit 2 with the reason on stderr, for the person: "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again" or "commit first"; the client blocks the prompt.
> **＋** Any other prompt, `/hi` included — exit 0, no output, no mark; a payload with `tool_name` — as today.
> **－** `guppi event prompt` does not change and does not fail; the text of `rule-event-log` and `rule-ledger-write` names the second entry, their contracts the same.

```then
update:
  - slug: rule-retro-commit
    contract: changed
    replace:
      - old: "It sees only calls made through the `Skill` tool, which is how the Retro skill calls `/handoff`; the handoff skill checks the tree itself for the case where the person types it."
        new: "It sees the agent's calls through the `Skill` tool, and — registered on `UserPromptSubmit` as well — the person's typed `/pre-task`, `/retro` or `/handoff`: the payload's `prompt`, trimmed, with or without arguments, gets the same two checks and the same mark; a refusal is exit 2 with the reason for the person — the client blocks the typed prompt — and asks them to have the agent end its reply with the LEDGER block, or to commit; any other prompt is exit 0 with no output and no mark (case 169.1). The handoff skill still checks the tree itself, a second net."
    change: "the gate reads a typed /pre-task, /retro or /handoff from the UserPromptSubmit payload: same checks, same mark, exit 2 for the person (case 169.1)"
  - slug: rule-event-log
    contract: same
    replace:
      - old: "The marks `pretask`, `retro` and `handoff` are written by `guppi gate` on `PreToolUse Skill` when it lets the call through"
        new: "The marks `pretask`, `retro` and `handoff` are written by `guppi gate` — on `PreToolUse Skill` for the agent's call, on `UserPromptSubmit` for the person's typed command (case 169.1) — when it lets the call through"
    change: "the marks name the second entry of the gate, the typed command on UserPromptSubmit (case 169.1)"
  - slug: rule-ledger-write
    contract: same
    replace:
      - old: "`guppi gate` on `PreToolUse Skill` reads"
        new: "`guppi gate` — on `PreToolUse Skill` for the agent's call, on `UserPromptSubmit` for a typed `/pre-task`, `/retro` or `/handoff` (case 169.1) — reads"
    change: "the Spec check of 122 names the second entry of the gate, the typed command (case 169.1)"
```

```tasks
- [x] `guppi/gate.py`: `skill_of` reads `prompt` beside `tool_input.skill`; the refusal text by path; `mark` the same
- [x] `tests/test_gate.py`: prompt `/retro` with an unwritten item → 2; with every line → 0 and the mark `retro`; `/handoff` on a dirty tree → 2; `/hi` and any text → 0, no mark; `/retro --check` as `/retro`
- [ ] `rule-retro-commit` `update`, `contract: changed`, the `replace` above; `estimate-retro-commit-gates` block 169.1, `pending`
- [ ] `rule-event-log` `update`, `contract: same`; `rule-ledger-write` `update`, `contract: same` — the `replace` above
- [ ] read `estimate-retro-commit-gates` (block 169.1): the tests green; in this session — a typed `/retro` while the Spec has an item without its line is refused with the reason on the screen; after the line it passes, the mark `retro` in the event log
```

### Case 169.2 — `guppi gate` on `UserPromptSubmit`

> **when:**
> `guppi render` writes `.claude/settings.json`; then the person submits a prompt.

> **then:**
> `UserPromptSubmit` carries two commands in order: `uv run guppi event prompt`, then `uv run guppi gate`, both with timeout 30.
> **－** The other events and matchers as today.

```then
update:
  - slug: rule-hook-registry
    contract: changed
    replace:
      - old: "{ \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi event prompt\", \"timeout\": 30 } ] }"
        new: "{ \"hooks\": [ { \"type\": \"command\", \"command\": \"uv run guppi event prompt\", \"timeout\": 30 },\n               { \"type\": \"command\", \"command\": \"uv run guppi gate\", \"timeout\": 30 } ] }"
    change: "UserPromptSubmit runs guppi gate after guppi event prompt (case 169.2)"
```

```tasks
- [ ] `rule-hook-registry` `update`, `contract: changed`, the `replace` above; `estimate-hook-registry-rendered` block 169.2, `pending`
- [ ] `.claude/settings.json`: the render; `guppi render --check` exit 0
- [ ] read `estimate-hook-registry-rendered` (block 169.2): after the render `settings.json` carries both commands; the day's event log gets `hi` from the first and a mark from the second
```

### Case 169.3 — `rule-retro`: two paths, both behind the gate

> **when:**
> The person types `/retro`, or the agent calls the skill `retro`.

> **then:**
> The typed `/retro` passes through `guppi gate` on `UserPromptSubmit`, the agent's call through `guppi gate` on `PreToolUse Skill`; both check the Spec against the ledger, both leave the mark `retro`; a refused typed prompt is not expanded.
> **＋** The frontmatter of `SKILL.md` without `disable-model-invocation`: the agent calls `/retro` when the tasks of the Spec are ticked.
> **－** Retro still stops at the lessons and the readings; `/handoff` behind the gate of the tree and of 122.

```then
update:
  - slug: rule-retro
    contract: changed
    replace:
      - old: "The scope rule is mechanical: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise."
        new: "The scope rule is mechanical: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise. Retro opens by two paths, both behind `guppi gate`: the person's typed `/retro` on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`; each checks the Spec against the ledger and leaves the mark `retro`, and a refused typed prompt is not expanded (case 169.3, supersedes 150)."
    change: "the two paths of Retro, typed and called, both behind the gate; supersedes 150 (case 169.3)"
```

```tasks
- [ ] `rule-retro` `update`, `contract: changed`, the `replace` above in Purpose; `estimate-retro-loads` block 169.3, `pending`; `{supersedes:case 150}` removes block 150
- [ ] `.claude/skills/retro/SKILL.md`: the render, unchanged in text
- [ ] read `estimate-retro-loads` (block 169.3): in this session — `/retro` typed and called by the agent; the event log carries two marks `retro`, both after the check
```

## Case 171 — `rule-page-generation`: 164 superseded before it applies; its text and the removal of block 124.2

> **context:**
> Case 166.2 carries `{supersedes:case 164}`. By `rule-materialize` the entries of a superseded Case get `superseded_by`, and by 151 they are not applied: the `replace` of 164 never lands on the page, block 164 never appears, and the `remove_criterion` of block 124.2 that the line of 164 yielded is skipped too. After the run `estimate-generate-writes` would hold block 124.2 "an Insight is never created through the yaml" beside block 166.2 "the librarian's create applies", and the text of the rule would say nothing about the librarian's create. Found at pre-task.

> **problem:**
> Who removes block 124.2 and who puts the sentence of 164 on the page, when 164 itself is not applied.

> **given:**
> `rule-materialize`: a line with `{supersedes:case N}` marks the entries of N `superseded_by` and yields a `remove_criterion`; `rule-page-generation` (151): an entry with `superseded_by` is not applied, its Decision page written `superseded`.
> **＋** The entries of 164 in this session's yaml — the `update` with `replace`, the `criterion_block` 164, the `remove_criterion` of 124.2 — all get `superseded_by: 166.2`.
> **＋** `contract: same` yields the `update` and no block; a supersedes on such a line still yields the `remove_criterion` (`rule-materialize`).
> **＋** The `old` text of 164 — "Any other existing page is a collision (case 101.1)." — stands once on the page.
> **－** Block 166.2 does not change: the behaviour of the librarian's create is signed there.

> **when:**
> The librarian applies the entries of 171 after 166.2 and 166.3.

> **then:**
> The text of `rule-page-generation` names the refusal of a create or delete of an Insight from a ledger line and the application of a create marked `librarian` — the sentence of 164 word for word, marked `case 171`.
> **＋** Block 124.2 leaves `estimate-generate-writes`; `decision-case-124.2` is `superseded`.
> **－** No new block.

```then
update:
  - slug: rule-page-generation
    contract: same
    replace:
      - old: "Any other existing page is a collision (case 101.1)."
        new: "Any other existing page is a collision (case 101.1). A `create` in `insights/` from a ledger line is refused — an Insight is made by the librarian, never by a decision; a `create` the librarian appended at synthesis, marked `librarian`, applies as any create, its `origin` the lesson line it grew from; a `delete` of an Insight is refused always: the cascade archives it (case 171, the text of 164; supersedes 124.2)."
    change: "the sentence of 164 on the librarian's create and the refusals, carried by 171 since 164 is superseded before it applies; supersedes 124.2 (case 171)"
```

```tasks
- [ ] `rule-page-generation` `update`, `contract: same`, the `replace` of 164 above; `{supersedes:case 124.2}` removes block 124.2
- [x] the code tasks of 164 — `generate.create` lets an `insights` entry carrying `librarian` through, the refusal line stays for a decision entry, `delete` unchanged; `tests/test_generate.py`: a synthesis entry writes the page `open`, `severity` 2 — done under 166.2, read on block 166.2
- [x] no reading of its own
```

## Case 172 — `rule-page-generation`: block 148.1 without "the body sections stay"

> **context:**
> Block 148.1 of `estimate-generate-writes` — the contract of the ref fields in the form `"[[slug]]"` and of the migration of 148.1 — ends with the line "**－** The body sections stay; no CLI probe." After 166.2 the sections go, and the line stays signed. Found at pre-task.

> **problem:**
> Block 148.1 and block 166.2 say the opposite about the sections.

> **given:**
> Block 148.1: `when` — generate or cleanup writes a page, a script reads one through `read_page`/`page_estimates`, the migration over `wiki/` and `archive/`; `then` — five lines on the fields, the readers, the migration, the tests and Obsidian, the last "The body sections stay; no CLI probe".
> **＋** The sentence of 148.1 in the rule's text on the wikilink fields is right and does not change; an `update` needs a `replace` — the phrase "reads the same (case 148.1)" stands once on the page.
> **－** The code of 148.1 does not change.

> **when:**
> `guppi generate` or `guppi cleanup` writes a page; a script reads a page through `pages.read_page` or `materialize.page_estimates`.

> **then:**
> In the written frontmatter every value of a ref field that carries a category prefix is `"[[slug]]"`, a list `["[[a]]", "[[b]]"]`; the fields: `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by`; a slug without a category prefix stays as it was.
> **＋** `read_page` and `page_estimates` strip `[[`/`]]` from these fields; a page without brackets reads the same.
> **＋** In Obsidian the backlinks of an Insight are its lessons and its Decision; the backlinks of a Rule are its children, Estimates and Decisions; `unresolved` is empty.
> **－** No CLI probe.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "reads the same (case 148.1)"
        new: "reads the same (case 148.1, restated by 172 without the body sections)"
    change: "block 148.1 restated without the body sections; supersedes 148.1 (case 172)"
```

```tasks
- [ ] `rule-page-generation` `update`, `contract: changed`, the `replace` above; `estimate-generate-writes` block 172, `pending`; `{supersedes:case 148.1}` removes block 148.1
- [ ] read `estimate-generate-writes` (block 172): the tests of 148.1 green; after the migration of 166.2 the backlinks in Obsidian in place — the same reading as 166.2
```

## Deferred

## Case 165.2 — `rule-page-generation`: drop the derived sections

> **context:**
> The derived sections of a Rule, Entity, Lesson and Insight — `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`, `## Insight`, `## Addressed by` — copy the ref fields of the frontmatter as wikilinks. Since 148.1 the fields are quoted wikilinks that Obsidian's graph, backlinks and Bases see on their own; `target` of an Estimate already lives in the field alone, with no section. `generate` builds the sections at `create`, rebuilds two of them on `update`, derives two on every write; `cleanup` rebuilds two; the schemas require them; five live pages show a section that differs from its field (`rule-lint`, `rule-render-harness`, `rule-hook-registry` on `## Parent`; `rule-event-log`, `rule-ledger-write` on `## Implementation`), and lint is silent.

> **problem:**
> Seven derived sections in five schemas, in `generate`, `cleanup`, `lint`, the tests and on every live and archived page are a copy that drifts and needs code to keep; removing them is a session of its own — schemas, scripts, a one-off migration over `wiki/` and `archive/`, and a supersedes of the parts of 114 and 164 that derive `## Insight` and `## Addressed by`. The owner chose the removal over deriving the sections on every write (165.1, not taken).

```then
defer:
  - slug: rule-page-generation
    type: rule
    purpose: drop the derived sections — Estimates, Children, Parent, Implementation, Code, Insight, Addressed by — from the schemas, generate, cleanup, lint and every live and archived page, the field being the one place a ref lives since 148.1; a session of its own, after Slice 3b
```

Taken up by Case 166 in the same session: `{supersedes:case 165.2}` on the first line of 166.1.

## Case 170 — Slice 3b: Work Mode, deferred again

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since Case 29, `draft`, `deferred_by: [[decision-case-162]]`, without `kind`, `estimates` or `tags` — 8 `schema` and 2 `orphan` findings. Slice 3b is the Spec as tasks with code, the ticked boxes, what a subagent may do and the fork that comes back as a Case; `sprint.md` says "3b before 4"; the Plan Mode of a session of its own.

> **problem:**
> The owner opened session R on the Deferred list and the Flags of the brief — Cases 164–169 — and left Slice 3b for a session of its own. The two pages stay placeholders one more session; the postponement count goes to 13.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: "Slice 3b — Work Mode: the Spec as tasks with code, the ticked boxes in spec.md, the readings taken in Work Mode; the Plan Mode of a session of its own, before Slice 4"
  - slug: rule-subagent-guppi
    type: rule
    purpose: "Slice 3b — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode"
```
