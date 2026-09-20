<!-- approved 18:59:23 · session 122e02e9 -->

# Spec — 2026-09-18, session 1252

## Case 235 — `rule-render-harness`: a render line opens with the command

> **context:**
> `rule-render-harness` (`draft`) governs `guppi/render.py`: the plain `guppi render` writes the governed files and, on exit 0, ticks the render lines in the `spec.md` of every unit under `raw/` whose yaml is applied whole (case 226.2). A render line of the Spec has the form `- [ ] `uv run guppi render`: `<file>`` — the command in the first code span. Today `RENDER_LINE` matches any unticked line that holds `guppi render` in a code span anywhere. The reading line `- [ ] read `estimate-render-harness-ticks-the-spec`: pytest, plus the `guppi render` lines …` of the 1119 Spec matched it and stands `[x]` without a reading taken; the brief named it in Flags. The Case touches one Estimate, `estimate-render-harness-ticks-the-spec` (`pending`); it does not touch `estimate-render-harness-reproduces` or `estimate-render-sync-reports`.

> **problem:**
> The Criterion of 226.2 says "a line holding `guppi render` in a code span" and the code does exactly that, so a reading line that names the command is ticked as a render done. The tick is false: the reading is not taken, and Retro does not count it.

> **given:**
> `guppi render` without a flag writes every governed file and exits 0, or writes nothing and exits 1.
> **＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied`.
> **＋** `tests/test_render.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi render` without a flag wrote the files and exits 0.

> **then:**
> In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`; nothing else changes.
> **－** A line where `guppi render` sits in a later code span — a `read `<slug>`` line, a line that names the command in its description — is not ticked.
> **－** `--check` and `--sync` tick nothing; exit 1 ticks nothing.
> **－** A unit without a yaml, with an unapplied or `failed` entry, or marked by `carry.md`, is not touched.

```then
update:
  - slug: rule-render-harness
    replace:
      - old: "it ticks every unticked task line holding `guppi render` in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check`, `--sync` and an exit 1 tick nothing (case 226.2)."
        new: "it ticks every unticked task line that opens with a code span holding `guppi render` — the render lines of the Spec, never a `read` line that names the command later — in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check`, `--sync` and an exit 1 tick nothing (cases 226.2, 235)."
    change: a render line opens with the code span holding guppi render; a read line that names the command later is not ticked (case 235)
  - slug: estimate-render-harness-ticks-the-spec
    set: {status: pending}
    change: the Criterion replaced whole — a render line opens with the code span holding guppi render (case 235)
```

```tasks
- [x] `guppi/render.py`: `RENDER_LINE` — the code span holding `guppi render` directly after `- [ ] `
- [x] `tests/test_render.py`: a `read` line with `guppi render` in a later code span stays `[ ]`
- [x] update `rule-render-harness`: the How-it-works sentence of 226.2 — a line that opens with the code span holding the command
- [x] update `estimate-render-harness-ticks-the-spec`: `status: pending`, the Criterion replaced whole
- [x] one-off: `raw/2026-09-17/1119/spec.md` — the reading line of `estimate-render-harness-ticks-the-spec` returned to `[ ]`
- [x] read `estimate-render-harness-ticks-the-spec`: pytest, plus this session's Spec after the librarian's run — the `uv run guppi render` lines ticked, this reading line not
```

## Case 236 — `rule-sprint`: a collapsed milestone names its items

> **context:**
> `rule-sprint` (`draft`) governs `guppi/sprint.py`: `guppi sprint` writes `vault/wiki/sprint.md` from the page `entity-sprint-<id>`; a closed milestone is one line `### [x] <name>`, the current one renders whole with its items, statuses and `deferred_by`, each later one is one line `### [ ] <name> — N items` (case 229.2). Today the line of Slice 4 says "1 item" and Slice 5 "3 items", and the reader of `sprint.md` cannot see what the items are without opening the page. The page holds them word for word; only the render loses them. The Case touches one Estimate, `estimate-sprint-renders-the-backlog` (`pending`); it does not touch `estimate-sprint-checks-the-file` — `--check` compares this same render and does not change.

> **problem:**
> The collapsed line exists so that `/hi` takes the Frontier from the current milestone only and the file stays short, but a count without names hides the plan: what stands in the queue after Slice 3b cannot be read from `sprint.md`. The question is how to show the items of a later milestone without blurring the edge of the current one.

> **given:**
> The cascade of `generate` sets `built`; `cleanup` sets `archived`; `sprint_id` reads the first `## <id>` heading.
> **＋** The current milestone is the first `### ` under `## Milestones` with an item not done, or with no item.
> **＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.
> **－** The script writes no page of `wiki/`.

> **when:**
> `guppi sprint` runs with a live page `entity-sprint-<id>`.

> **then:**
> The file: `# Sprint`; `## <id>`; Purpose; `**Done when**` — as today; then `## Milestones`: a closed milestone as one line `### [x] <name>`; the current one as the heading `### [ ] <name>` and each item with its status and `deferred_by`, as today; each later one as one line `### [ ] <name> — N items: ` and its items separated by commas, an item with a wikilink as `[[slug]]`, an item without one by its text, with no tick and no status; then `## Backlog` — each item a line; then `## Closed` as it is.
> **＋** An item `- [[slug]] — <text>` is ticked by the status of its page, as today; an item `- <text>` without a wikilink renders `- [ ] <text>` and is never ticked.
> **＋** A milestone is closed when every item is `[x]`; with no item it is open.
> **－** A slug with no live or archived page: stderr, exit 1, the file not written. `--check` (case 227) compares this same render.

```then
update:
  - slug: rule-sprint
    replace:
      - old: "a closed one as one line, the current one whole, a later one as one line with its count"
        new: "a closed one as one line, the current one whole, a later one as one line with its count and its items by slug (case 236)"
    change: a later milestone's line names its items by slug after the count (case 236)
  - slug: estimate-sprint-renders-the-backlog
    set: {status: pending}
    change: the Criterion replaced whole — the collapsed line of a later milestone names its items (case 236)
```

```tasks
- [x] `guppi/sprint.py`: the collapsed line — the count and the list of items
- [x] `tests/test_sprint.py`: a later milestone with a wikilink item and a plain item renders as one line with the names
- [x] `uv run guppi sprint`: `vault/wiki/sprint.md` rewritten in the working tree, `make lint` without a `sprint:` line
- [x] update `rule-sprint`: the Purpose sentence on a later milestone — one line with the count and the items
- [x] update `estimate-sprint-renders-the-backlog`: `status: pending`, the Criterion replaced whole
- [x] read `estimate-sprint-renders-the-backlog`: pytest, plus `sprint.md` after the librarian's run — the lines of Slice 4 and Slice 5 with the names of their items
```

## Case 237 — `estimate-permissions`: the reading is the person's word

> **context:**
> `rule-permissions` (`built`) renders `allow` in `.claude/settings.json` — nine entries for the working files of the session — and promises in its Purpose that the session writes them "without asking". Its one Estimate `estimate-permissions` stands `passed`; its Criterion asks for a live probe "asked or not asked", and its Result holds "returned without a prompt" — read by the agent. The agent does not see the client's prompt: an approved call returns to it exactly as one that was not asked. The person sees it: in Plan Mode the prompt appears before every edit outside the plan file, allow list or not, and the person approves it each time. The Case touches `estimate-permissions`; the Purpose of the rule changes by one sentence, which touches no Estimate.

> **problem:**
> The Criterion assigns the reading to an observer who cannot observe, and the page holds `passed` on what the agent did not see. The promise "without asking" does not hold in Plan Mode by the client's mechanism, and the person accepts that — but it has to stand in the Estimate, not in memory.

> **given:**
> `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** In Plan Mode the client asks before every edit outside the plan file, allow list or not.
> **－** Nothing else under `wiki/` is allowed.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

> **then:**
> The allow list holds nine entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md` under `vault/raw/**`; Write for `carry.md` under `vault/raw/**`; Edit and Write for `vault/wiki/brief.md`.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

```then
update:
  - slug: estimate-permissions
    set:
      status: pending
      method: the nine entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of frontier.md at /hi and an edit of spec.md, recorded in the estimate line — never the agent's, which cannot see the prompt
    change: the Criterion replaced whole — the prompt is read by the person, a prompt in Plan Mode is not a finding (case 237)
  - slug: rule-permissions
    replace:
      - old: "A question before each of those writes buys\nnothing — the content is the agent's own, and the person reads it in the reply\nanyway."
        new: "A question before each of those writes buys\nnothing — the content is the agent's own, and the person reads it in the reply\nanyway. The list states that intent; in Plan Mode the client asks before every edit outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237)."
    change: the allow list as intent; in Plan Mode the client asks all the same, and the prompt is read by the person (case 237)
```

```tasks
- [x] update `estimate-permissions`: `status: pending`, `method` — the probe from the person's word, the Criterion replaced whole
- [x] update `rule-permissions`: the Purpose sentence — the list as intent; in Plan Mode the client asks all the same, the person approves
- [x] read `estimate-permissions`: nine entries in `settings.json`; the person's word in session 1252 — the prompt in Plan Mode appears, approved
```

## Case 239 — `entity-sprint-migration`: the morph mechanism in Slice 5

> **context:**
> The sprint page `entity-sprint-migration` holds three Slices under `## Milestones` and two plain lines without a page under `## Backlog`: "the categories as data of the project" and "the product model" (case 229.1). The question of the universality of the categories — objection F of `categories-discussion.md` — stands in the first Backlog line as "some day". The person decided: it is a question of Slice 5, the close, in the form of a morph mechanism — at install the person goes through an initiation in which the category set may change, and the architecture has to hold that without a rewrite of the rules. The Case touches the sprint page and creates the placeholder `rule-morph` by a `defer`; it touches no Estimate of the sprint.

> **problem:**
> A Backlog line is "without a turn", and the question got a turn and a name. An item of a milestone without a page is never ticked, and Slice 5 with one would never close; the item needs a page to point at, and the rule does not exist yet.

> **given:**
> `guppi sprint` ticks an item by the status of the page it names; an item without a wikilink is never ticked.
> **＋** A `defer` without a `ref` creates a placeholder page with a `purpose`.

> **when:**
> The librarian applies the yaml of this session and runs `guppi sprint`.

> **then:**
> `rule-morph` exists as a placeholder, `draft`, with `deferred_by: decision-case-239`.
> **＋** Slice 5 on the sprint page holds `[[rule-morph]]` as its fourth item; the Backlog holds one line — the product model.
> **＋** `sprint.md` renders Slice 5 as one line with four names (case 236).

```then
defer:
  - slug: rule-morph
    type: rule
    purpose: "The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5"
update:
  - slug: entity-sprint-migration
    replace:
      - old: "- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b\n"
        new: "- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b\n- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239\n"
      - old: "- the categories as data of the project: `generate`, `lint`, `materialize` and `ask-guppi` read the category set from `wiki/<category>/schema.yaml`; the development set — entity, rule, estimate — is the default (session 1119)\n- the product model:"
        new: "- the product model:"
    change: the morph mechanism as rule-morph in Slice 5; the Backlog line on the categories as data folded into it (case 239)
```

```tasks
- [x] defer `rule-morph`: placeholder, `purpose`
- [x] update `entity-sprint-migration`: the Backlog line on the categories removed, `[[rule-morph]]` in Slice 5
```

## Case 240 — the definitions of the categories for development

> **context:**
> The vault says in no one place what an Entity, a Rule and an Estimate are and where the edge between them runs: `glossary.md` holds a row each, `index.md` §6 the rule of the cut and the two meanings of MOC, the three `schema.md` an opening paragraph each — "Entity is the thing that gets built"; "A Rule is something that can be broken, where breaking it will be detected". Session 1119 discussed it and deferred it (case 230, `categories-discussion.md`); this session agreed the wording. The universality of the categories went to `rule-morph`, Slice 5 (case 239); the product model stays in the Backlog. The Case touches Rule-class files — `glossary.md`, `entities/schema.md`, `rules/schema.md`, `estimates/schema.md`, `index.md` §6 — by hand in Work Mode; it touches no Estimate.

> **problem:**
> The agent reads an Entity page without a definition to hold it against and fills the gap by judgment; between an Estimate on an Entity and a Rule there is no question that removes the double reading; MOC and Leaf do not say where the cut comes from; `kind: Research` does not say where it lives and what `failed` means.

> **given:**
> The glossary is imported into `CLAUDE.md` and loaded from the first turn; the `schema.md` of a category is read before a `create` of a page; `index.md` §6 at a cut.
> **＋** A Rule-class file changes only by a ratified `update`, by hand in Work Mode.
> **－** No schema changes a field or its `schema.yaml`; lint (`schema-prose`) is not touched.

### Case 240.1 — Entity, MOC and Leaf

> **when:**
> The agent forms a `create` of an Entity, or cuts a Leaf into a MOC, or reads an Entity page.

> **then:**
> `entities/schema.md` and the glossary row say: an Entity is a thing the developer builds, a noun the person named as part of what is built; the check before a `create` — who makes this thing: the developer → an Entity; the product's user or the running product → data, outside the vault, never a page.
> **＋** A MOC is a thing whose parts the person named as things that are built; a Leaf a thing for which the person has not done that yet; a part comes only from the person's words, through a Case; the agent proposes a cut (§6, Retro) and never makes it.
> **＋** The Estimates of a MOC measure what no child owns; a Leaf's its own scope; a Leaf with empty `estimates` is legal — the person said nothing yet.
> **＋** What is inside a Leaf — a field, a button, a function — is described in `## How it works`, not by a page.
> **－** No Entity is created for a "why": the reason lives in the Decision, the rule's `## Purpose` and the lessons through an Insight.

```then
update:
  - slug: entities-schema
    file: vault/wiki/entities/schema.md
    replace:
      - old: "Entity is the thing that gets built. It is recursive: a MOC holds children, a Leaf holds behaviour. Depth is not fixed in advance — it follows the atomicity rule and nothing else."
        new: "An Entity is a thing the developer builds: a noun the person named as part of what is built. The check before a `create`: who makes this thing? The developer → an Entity. The product's user, or the running product — a post, an account, a record → data, which lives in the product and is never a page. A developer who uses GUPPI is still the developer; \"user\" in this check is always the user of the developer's product (case 240.1).\n\nA MOC is a thing whose parts the person named as things that are built; a Leaf is a thing for which the person has not done that yet. A part comes only from the person's words, through a Case; the agent proposes a cut — in Retro, by the atomicity rule of §6 of `index.md` — and never makes it. A part is itself an Entity: its own code, its own conditions. What is not a part — a field, a button, a function inside a Leaf — is the Leaf's inner working and goes to `## How it works`, not to a page. The Estimates of a MOC measure what no child owns; a Leaf's measure its own scope; a Leaf with empty `estimates` is legal — the person said nothing yet. Depth is not fixed in advance — it follows the atomicity rule and nothing else.\n\nNo Entity for a \"why\": the reason behind a rule lives in the Decision that made it, in the rule's `## Purpose` and in the lessons behind it through an Insight; an Entity per why would be a fourth copy (case 240.1)."
    change: the definition of an Entity — a thing the developer builds, the check before a create; MOC and Leaf by the parts the person named; no Entity for a why (case 240.1)
  - slug: glossary
    file: vault/wiki/glossary.md
    replace:
      - old: "| MOC | A page with no criteria of its own; `children` lists its pages; nests to any depth | §6 |"
        new: "| MOC | A thing whose parts the person named as things that are built; `children` lists them; its Estimates measure what no child owns; a part comes from the person's words through a Case — the agent proposes a cut, never makes it (case 240.1) | §6, entities/schema.md |"
      - old: "| Leaf | A page with checkable behaviour of its own; holds `estimates` and a code pointer | §6 |"
        new: "| Leaf | A thing whose parts the person has not named; holds `estimates` — empty is legal, the person said nothing yet — and a code pointer; its inner workings are `## How it works`, not pages (case 240.1) | §6, entities/schema.md |"
      - old: "| Entity | The thing that gets built; MOC or Leaf; a Leaf carries `code_ref` | entities/schema.md |"
        new: "| Entity | A thing the developer builds, a noun the person named as part of what is built; the check before a `create`: who makes it — the developer → an Entity; the product's user or the running product → data, outside the vault; MOC or Leaf; never a page for a \"why\", that is a Decision (case 240.1) | entities/schema.md |"
    change: the rows Entity, MOC and Leaf — the definitions of case 240.1
  - slug: index
    file: vault/wiki/index.md
    replace:
      - old: "A MOC has no direct criteria — its `children` are the functional requirements, and its `estimates` cover only cross-cutting/non-functional checks that belong to no single child."
        new: "A MOC has no direct criteria — its `children` are the parts the person named as things that are built, and its `estimates` cover only what no single child owns. A part comes from the person's words, through a Case; the agent proposes a cut here, in Retro, and never makes it (case 240.1)."
    change: §6 — a MOC's children are the parts the person named; the agent proposes a cut, never makes it (case 240.1)
```

```tasks
- [x] update `entities/schema.md`, by hand: the opening paragraphs — the definition and the check; MOC and Leaf; the why
- [x] update `glossary.md`, by hand: the rows Entity, MOC, Leaf
- [x] update `index.md` §6, by hand: the paragraph "A MOC has no direct criteria"
```

### Case 240.2 — Rule, and the criterion of the harness

> **when:**
> The agent forms a `create` of a Rule, or decides whether a thing is a Rule or an Entity, or reads a Rule page.

> **then:**
> `rules/schema.md` and the glossary row say: a Rule is a standing condition one case can break, with a guard that refuses that case when it occurs; the check — can one case refute it, and is there something to refuse it.
> **＋** A Leaf is a condition on each case; a MOC a sequence whose Estimate promises the order: one run out of order breaks it.
> **＋** A Rule is of the harness or of an Entity; on an Entity it is a checkable requirement whose Estimate promises how it is controlled.
> **＋** In the harness a thing is a Rule when its code is a guard; a thing is an Entity when it is measured and has no guard of its own — its guard is a separate Rule; the sprint is an Entity by this criterion, not an exception.
> **－** A condition without a guard is not a Rule: it is an Estimate on an Entity.

```then
update:
  - slug: rules-schema
    file: vault/wiki/rules/schema.md
    replace:
      - old: "A Rule is something that can be broken, where breaking it will be detected. That single definition covers both harness hooks and code constraints — see *Enforcement* below."
        new: "A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs. The check: can one case refute it, and is there something to refuse that case? Yes to both → a Rule, and its Estimate is the test that the guard works. A condition no single case can break — a measure of the whole — is not a Rule but an Estimate on an Entity; a condition with no guard is not one either. A Leaf is a condition on each case; a MOC a sequence whose Estimate promises the order — one run out of order breaks it. A Rule is of the harness or of an Entity: on an Entity it is a checkable requirement, and its Estimate promises how the requirement is controlled. That single definition covers both harness hooks and code constraints — see *Enforcement* below (case 240.2)."
    append:
      section: "### Enforcement"
      place: at the end of the section, before the next heading, by hand
      text: |
        In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift. A thing is an Entity when it is measured and has no guard of its own; its guard is a separate Rule. The sprint is an Entity by this criterion — its Definition of done is read, and `rule-sprint` is its guard — not an exception (case 240.2).
    change: the definition of a Rule — a standing condition one case can break, with a guard; the criterion of the harness under Enforcement (case 240.2)
  - slug: glossary
    file: vault/wiki/glossary.md
    replace:
      - old: "| Rule | How the work happens; force by `hook`, `check` or `render`; needs an Estimate | rules/schema.md |"
        new: "| Rule | A standing condition one case can break, with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it; a Leaf a condition on each case, a MOC a sequence whose Estimate promises the order; of the harness or of an Entity; force by `hook`, `check` or `render`; in the harness a thing is a Rule when its code is a guard, an Entity when it is measured and its guard is a separate Rule (case 240.2) | rules/schema.md |"
    change: the row Rule — the definition and the criterion of the harness (case 240.2)
  - slug: index
    file: vault/wiki/index.md
    replace:
      - old: "This is why our own process is described as Rule MOCs — session-start, plan-mode, work-mode, end-of-work, documentation — each holding ordered children, recursing where the atomicity rule calls for it."
        new: "This is why our own process is described as Rule MOCs — session-start, plan-mode, work-mode, end-of-work, documentation — each holding ordered children, recursing where the atomicity rule calls for it. In the harness a thing is a Rule when its code is a guard, and an Entity when it is measured and its guard is a separate Rule; the sprint is the Entity of the harness by that criterion, not an exception (case 240.2)."
    change: §6 — the criterion of the harness, guard → Rule, measured thing → Entity (case 240.2)
```

```tasks
- [x] update `rules/schema.md`, by hand: the opening definition; the criterion of the harness under Enforcement
- [x] update `glossary.md`, by hand: the row Rule
- [x] update `index.md` §6, by hand: the last paragraph "This is why our own process…"
```

### Case 240.3 — Estimate and `kind`

> **when:**
> The agent forms a `create` of an Estimate, or reads a Result, or sets `failed`.

> **then:**
> `estimates/schema.md` and the glossary row say: an Estimate is the evidence; on a Rule a test that the guard works; on an Entity a reading of the whole, which no single case can break; which of the two, the prefix of the target says — the agent does not choose.
> **＋** `kind` stays `QA | Research`: QA — the answer is known, there is a bar; Research — the reading finds the answer.
> **＋** Research lives on an Entity only: a Rule has its criterion by definition.
> **＋** `failed` on a Research Estimate — the finding does not serve the purpose of the Estimate: no answer, or the answer "not this way"; which of the two, the person says in the reading line; both are debt — a Case on a changed approach, or archival; when a bar grows out of the finding, it becomes a QA Estimate or a Rule.
> **－** Research has no "bad" `passed`: `passed` means the finding serves the purpose.

```then
update:
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    replace:
      - old: "Three blocks: **properties**, **body**, **history**. One schema for both kinds; sections that do not apply are omitted rather than left empty."
        new: "Three blocks: **properties**, **body**, **history**. One schema for both kinds; sections that do not apply are omitted rather than left empty.\n\nAn Estimate is the evidence. On a Rule it is a test that the guard works; on an Entity it is a reading of the whole, which no single case can break. Which of the two it is, the prefix of `target` says; the agent does not choose (case 240.3)."
      - old: "Research: the result is not known, and finding it produces new content;"
        new: "Research: the result is not known, and finding it produces new content — on an Entity only, since a Rule has its criterion by definition; `failed` on a Research Estimate means the finding does not serve the purpose the Estimate was made for — no answer, or the answer \"not this way\" — which of the two, the person says in the estimate line; both are debt, a Case on a changed approach or archival; when a bar grows out of the finding, it becomes a QA Estimate or a Rule (case 240.3);"
    change: the definition of an Estimate — test on a Rule, reading on an Entity; Research on an Entity only, and what failed means for it (case 240.3)
  - slug: glossary
    file: vault/wiki/glossary.md
    replace:
      - old: "| Estimate | One promise, one way to check it, the last result with its date (case 182);"
        new: "| Estimate | The evidence: on a Rule a test that the guard works, on an Entity a reading of the whole no single case can break — the target's prefix says which; `QA` the answer is known, `Research` the reading finds it, on an Entity only, `failed` when the finding does not serve the purpose (case 240.3); one promise, one way to check it, the last result with its date (case 182);"
    change: the row Estimate — the evidence, test or reading by the target; Research on an Entity, failed (case 240.3)
```

```tasks
- [x] update `estimates/schema.md`, by hand: the opening paragraph; the `kind` row
- [x] update `glossary.md`, by hand: the row Estimate
```

## Case 241 — `entity-sprint`: the sprint as a kind, `entity-sprint-migration` its Leaf

> **context:**
> `entity-sprint-migration` is the one live Entity, `kind: MOC` with empty `children`; its `estimates` are the Definition of done, its `## Milestones` the Slices (cases 209.2, 229.1). `guppi sprint` finds the page by the prefix `entity-sprint-` (`sprint_page` in `guppi/sprint.py`); the slug `entity-sprint`, without the dash, does not match the prefix — the code does not change. The glossary (the Sprint row) and the Purpose of `rule-sprint` call the sprint "an Entity MOC `entity-sprint-<id>`". By the definitions of 240.1 the sprint "migration" is a thing with no parts named, a Leaf; the kind "sprint" is a MOC over it. `generate` writes `children` on a parent only at a `create` with `ref`, not at an `update` of the child — so `children` of `entity-sprint` and `parent` of `entity-sprint-migration` are written in the blocks here, against the sentence of `case-schema.md` that calls them derivable — derivable only on the `ref` path, which an existing child has no way to take. The vault asked: `entity-sprint` is free, live and archive; the near pages are `entity-sprint-migration` and `rule-sprint`; no MOC over the sprints exists; the tags `sprint`, `workflow`. The Case touches the sprint pages, the glossary and the Purpose of `rule-sprint`; no Estimate.

> **problem:**
> The sprint by id is recorded as a MOC without children, and the kind "sprint" does not exist; the next sprint has nothing to hang on, and the page contradicts the definition of 240.1.

> **given:**
> An Entity is a thing the developer builds; a MOC a thing with parts named, a Leaf one without (case 240.1).
> **＋** `guppi sprint` reads the page by the prefix `entity-sprint-`; `generate` writes `children` at a `create` with `ref`.
> **－** `entity-sprint` has no guard of its own: its guard is `rule-sprint`.

> **when:**
> The librarian applies the yaml of the session and runs `guppi sprint`.

> **then:**
> `entity-sprint` exists: `kind: MOC`, `purpose` — the kind "sprint", a unit of work over the project with a Definition of done and milestones; `children: [[entity-sprint-migration]]`; `estimates` empty.
> **＋** `entity-sprint-migration` is `kind: Leaf`, `parent: [[entity-sprint]]`, without the field `children`; everything else as it was.
> **＋** `guppi sprint` renders `sprint.md` from `entity-sprint-migration`, as today; `sprint --check` is silent.
> **＋** The glossary and the Purpose of `rule-sprint` call the sprint a Leaf `entity-sprint-<id>` under the MOC `entity-sprint`.
> **－** The next sprint is a new Leaf under `entity-sprint`, a `create` with `ref: entity-sprint`; `guppi sprint` still requires exactly one live page with the prefix.

```then
create:
  - slug: entity-sprint
    type: entity
    kind: MOC
    purpose: The sprint as a kind — a unit of work over the project with a Definition of done and milestones; its children the sprints, one Leaf per id
    children: ["[[entity-sprint-migration]]"]
    estimates: []
    tags: [sprint, workflow]
    sections:
      Purpose: |
        The sprint as a kind. A sprint is a unit of work over the project: its Estimates are its Definition of done, its `## Milestones` the Slices in order, its `## Backlog` the items without a turn. Each sprint is a Leaf under this page, `entity-sprint-<id>`, one live at a time; `guppi sprint` renders `vault/wiki/sprint.md` from the live one, and `rule-sprint` is its guard. This page carries no Estimate yet — the person named none; a measure over all sprints, which no single sprint owns, goes here when one is named (case 241).
update:
  - slug: entity-sprint-migration
    set: {kind: Leaf, parent: "[[entity-sprint]]"}
    change: a Leaf under entity-sprint — the sprint by id is a thing with no parts named (cases 240.1, 241)
  - slug: rule-sprint
    replace:
      - old: "The sprint is\na page — an Entity MOC whose `estimates` are its Definition of done"
        new: "The sprint is\na page — an Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint` (case 241), whose `estimates` are its Definition of done"
    change: the sprint page is a Leaf under the MOC entity-sprint (case 241)
  - slug: glossary
    file: vault/wiki/glossary.md
    replace:
      - old: "| Sprint, `brief.md` | An Entity MOC `entity-sprint-<id>` whose Estimates are the Definition of done,"
        new: "| Sprint, `brief.md` | An Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, the sprint as a kind (case 241), whose Estimates are the Definition of done,"
    change: the Sprint row — a Leaf under entity-sprint (case 241)
```

```tasks
- [x] create `entity-sprint`
- [x] update `entity-sprint-migration`: `kind: Leaf`, `parent`
- [x] one-off: the field `children` removed from `entity-sprint-migration` by a script, as `ref` in case 225 — between this and the librarian's `set: {kind: Leaf}` lint reads a MOC without `children`: an expectation for the handoff (insight-workflow-code-live-before-the-page-it-reads), not a finding
- [x] update `rule-sprint`: the Purpose — a Leaf under the MOC
- [x] update `glossary.md`, by hand: the Sprint row
- [x] `tests/test_sprint.py`: a page `entity-sprint` beside `entity-sprint-<id>` does not disturb `sprint_page`
```

## Case 244 — `estimate-sprint-migration-lint-clean`: the facts of the sprint page after 239 and 241

> **context:**
> `estimate-sprint-migration-lint-clean` (`pending`, target `entity-sprint-migration`) promises `make lint` exit 0 at the close of the sprint and, in the second line of its `then`, lists what the sprint page looks like: an Entity MOC, Slice 5 of three Estimates and `rule-spec-box`, a Backlog of two lines (case 229.1). Cases 239 and 241 of this Spec make the page a Leaf under `entity-sprint`, add `[[rule-morph]]` to Slice 5 and leave one line in the Backlog; both said "touches no Estimate of the sprint" — pre-task found that this one is touched. The Case touches one Estimate; `-leftovers-gone` and `-merges` it does not.

> **problem:**
> The Criterion describes a page that will not exist after this Spec; the reading at the close would fail on the shape of the page, not on lint.

> **given:**
> Items 1–4 of the Definition of done are what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
> **＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.
> **＋** The sprint page is the Leaf `entity-sprint-migration` under the MOC `entity-sprint` (case 241); its Slices and its Backlog are as the page holds them at the moment of the reading (cases 229.1, 239).

> **when:**
> Someone reads `make lint` at the close of the sprint.

> **then:**
> `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
> **＋** The page `entity-sprint-migration` exists: an Entity Leaf under `entity-sprint`, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Milestones` — the Slices in order, each item a wikilink to a page or a plain line; `## Backlog` — the items without a turn; `## Closed` — Slices 0–3d in one paragraph.
> **－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.

```then
update:
  - slug: estimate-sprint-migration-lint-clean
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        Items 1–4 of the Definition of done are what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
        **＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.
        **＋** The sprint page is the Leaf `entity-sprint-migration` under the MOC `entity-sprint` (case 241); its Slices and its Backlog are as the page holds them at the moment of the reading (cases 229.1, 239).

        When:
        Someone reads `make lint` at the close of the sprint.

        Then:
        `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
        **＋** The page `entity-sprint-migration` exists: an Entity Leaf under `entity-sprint`, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Milestones` — the Slices in order, each item a wikilink to a page or a plain line; `## Backlog` — the items without a turn; `## Closed` — Slices 0–3d in one paragraph.
        **－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.
    change: the Criterion replaced whole — the sprint page a Leaf under entity-sprint, its Slices and Backlog as the page holds them, no item named (case 244)
```

```tasks
- [x] update `estimate-sprint-migration-lint-clean`: `status: pending`, the Criterion replaced whole under `sections: Criterion`
- [ ] read `estimate-sprint-migration-lint-clean`: `make lint` at the close of the sprint (the place from `method`)
```

## Deferred

## Case 242 — `rule-work-mode`, `rule-subagent-guppi`: Slice 3b, deferred again

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are the two items of Slice 3b, the current milestone of the sprint — placeholders since case 29 and case 183, deferred by 183, 206, 218 and 231; their drafts are `docs/migration/rule-work-mode.md` and `docs/migration/rule-subagent-guppi.md`. Session 1252 spent its Plan Mode on the definitions of the categories (240), the sprint as a kind (241) and six smaller items, and the person chose to close Plan Mode before Slice 3b rather than open a large discussion at its end. The one sentence of `insight-workflow-code-live-before-the-page-it-reads` waits for the same rule (case 238).

> **problem:**
> Slice 3b has been the current milestone for two sessions with no Case on it; each session that defers it adds a `deferred_by` and a brief; Work Mode runs without its rule, by the drafts and the habit.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes in spec.md, the test of each Estimate written first and turned green; the sentence of case 238 on a check that reads a page the same Spec updates; Slice 3b, the next session, first item
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; Slice 3b, with rule-work-mode
```

## Case 243 — `rule-git-context`, `rule-github-issues`: the close of the sprint, as before

> **context:**
> `git pull` at `/hi` fails without an upstream of `migration` (decision 11.1), and `gh` is not logged in with no GitHub remote (11.2); both are printed lines of `/hi`, items of every Frontier, deferred by case 220 to the close of the sprint and read by `estimate-sprint-migration-leftovers-gone`. Nothing changed in session 1252: the same two lines, the same decision.

> **problem:**
> The decision stands at the close of the sprint, Slice 5, and the Frontier lists the two lines every session until then.

```then
defer:
  - slug: rule-git-context
    type: rule
    purpose: the pull without an upstream at /hi — set the upstream of migration, or keep the printed failure as decision 11.1 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone
  - slug: rule-github-issues
    type: rule
    purpose: gh not logged in, no GitHub remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone
```

## Case 238 — `insight-workflow-code-live-before-the-page-it-reads`: one sentence for Work Mode, with Slice 3b

> **context:**
> `insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2) was made by the librarian of the 1119 run over two lessons: the Stop hook that refused 13 lines after case 111.3, and `make lint` red on the sprint step after cases 227 and 229.1. One Spec changes a reader in code and the text it reads on a page or in a governed file; the code of the working tree runs at once, the page lands at the librarian's run and the file at the render, so the reader is red in between by construction. Its Proposal is one sentence in `rule-work-mode`: such a check is read after the run or the render, its red in Work Mode is an expectation named in the handoff, not a finding, and a reader that drops an old form keeps it as a fallback until its writer is measured live. `rule-work-mode` is a placeholder without a body, Slice 3b, deferred by 183, 206, 218 and 231.

> **problem:**
> The Proposal is right and has no page to land on: the sentence belongs to the rule of Work Mode, and that rule does not exist yet. The person chose to take it up with the whole of Slice 3b, when `rule-work-mode` is built, rather than as a line written ahead of its rule.

```then
defer:
  - slug: insight-workflow-code-live-before-the-page-it-reads
    type: insight
    purpose: one sentence in rule-work-mode when the rule is built with Slice 3b — a check that reads a page or a file the same Spec updates is read after the librarian's run or the render, its red in Work Mode an expectation named in the handoff, a dropped form kept as a fallback until its writer is measured live; the Case that creates rule-work-mode ends in the update of this Insight, status actioned, addressed_by that Case
```
