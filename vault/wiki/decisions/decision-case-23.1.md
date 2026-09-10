---
type: decision
case: "23.1"
status: superseded
targets:
  - {kind: create, category: rules, slug: rule-ask, ref: rule-plan-mode}
  - {kind: create, category: estimates, slug: estimate-ask-finds, ref: rule-ask}
superseded_by: [decision-case-26.1]
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Then

```
create:
  slug: rule-ask
  type: rule
  kind: Leaf
  purpose: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
  enforcement: render
  governs: .claude/agents/ask-guppi.md
  render_mode: full
  parent: rule-plan-mode
  tags: [session, workflow, harness]
  estimate:
    slug: estimate-ask-finds
    kind: QA
    criterion: three live dispatches once the indexes exist — a question about an existing page, in English, names its slug under `exists`; the same question in Russian names the same slug; a proposal crossing a known rule (a SessionStart hook meant to block) names the rule or lesson under `rules`; each answer is the five lines, no index or page text reaches the caller's context, each dispatch is in the event log; the reading records whether `@` expanded and the tokens of one dispatch
    method: three readings by hand in one session — the exception the Method rule allows
```

Текст рендера (в файл при `full` без маркеров):

```markdown
---
name: ask-guppi
description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. One short question per Case.
model: opus
tools: Read, Grep, Glob
---
You search the vault at `vault/wiki/` for the caller and answer in five lines. You
decide nothing and propose nothing.

Rules of the vault, one line per page:
@vault/wiki/rules-index.md

Start there. Read `vault/wiki/<category>-index.md` for every other category the question
touches (entities, estimates, lessons, insights; decisions have none). Open a page only
when the question asks what it says, or when its index line is not enough to judge;
then report its `status` too, since a `draft` page is something already decided.
Grep `vault/wiki/index.md` when the proposal may cross a rule of the vault itself.
Compare meanings, not words; the aliases column of `vault/wiki/tags.md` maps Russian
words to tags. Never compare across categories.

Answer with exactly these five lines, each present, "none" when empty:
- exists: slug — what matches
- near: slug — how it differs
- missing: what the question asks for that no page covers
- rules: rule or lesson slug — what it forbids or requires here
- tags/slug: tags that fit, existing first; whether the named slug is free
```

```
update:
  slug: rule-case-protocol
  change: render text — "Use `/ask` once it exists; until then read the category folders" → "Dispatch the `ask-guppi` agent with one short question once it exists; until then read the category folders"
update:
  slug: index
  change: §3 and §11 name the mechanism "the `ask-guppi` agent"; no other wording changes
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-09 superseded by decision-case-26.1 · raw/2026-09-09/ledger.md#case-26.1
