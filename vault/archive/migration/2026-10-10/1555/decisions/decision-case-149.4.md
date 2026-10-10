---
type: decision
case: "149.4"
status: archived
update: ["[[rule-brief]]", "[[rule-skill-hi]]", "[[rule-documentation]]", "[[rule-claude-md]]"]
origin: raw/2026-09-14/1633/ledger.md#case-149.4
sprint: migration
created: 2026-09-14
tags: [harness, workflow, librarian, session, render]
---

## Context

In Obsidian's graph `brief.md`, `sprint.md`, `tags.md`, `log.md`, `index.md`, `glossary.md`, `case-schema.md` and the six `schema.md` are orphans: the rules and `index.md` name them in backticks as paths (`vault/wiki/brief.md`), never as `[[brief]]`. The layout of §1 `index.md` is a code block; Obsidian reads no link inside one. Lint checks the wikilinks in the body of a category page against the slugs of live and archived pages — `[[brief]]` would be a `ref` finding.

## Problem

The owner sees the connections by eye through the graph; the hub files are the joints between sessions and agents and should be seen connected. Decide: one place from which every hub file is reached (§1 of `index.md`), a link back from `glossary`/`case-schema` to `[[index]]`, lint accepts a wikilink to a file under `wiki/`, and the four rules whose subject is a hub file name it as a link in their Purpose.

## Given

`index.md` §1 — the layout in a ``` fence: `index.md`, `glossary.md`, `case-schema.md`, `brief.md`, `sprint.md`, `tags.md`, `log.md`, `<category>/schema.yaml schema.md`; the four `*-index.md` leave with 147.8. `glossary.md` first paragraph: "`§N` a section of `index.md`"; `case-schema.md`: "imported into `CLAUDE.md`".
**＋** `rule-lint` `built`, `estimate-lint-catches`; `check_refs`: `known = set(by_slug) | archived_slugs(wiki)`; `links_of` takes `[[slug]]` from sections outside code spans; `[[a/b]]` is the slug `a/b`; the rule's text: "every ref … as an existing page".
**＋** Obsidian resolves `[[brief]]` → `wiki/brief.md`, `[[rules/schema]]` → `wiki/rules/schema.md` by path; `[[schema]]` is ambiguous (six files) — by path only.
**＋** Purpose: `rule-brief` "Prevents the next session from starting without the facts and the flags of this one. The brief is a shop window, not storage …"; `rule-skill-hi` "Prevents a session from being loaded piecemeal by read-tool calls. …"; `rule-documentation` "… the three scripts are called from the frame by name."; `rule-claude-md` "… a change to it is an `update` of one of the two." All prose sections, written by `generate` from ratified `sections`/`replace`.
**＋** No Render holds a `[[…]]` to a hub file; `.claude/agents/*.md` and the skills read paths.
**－** `README`, `docs/` outside the vault — outside the Case. Rule-class files (`index`, `glossary`, `case-schema`) — an `update` with `file`, by hand.
**－** The owner's graph is filtered `path:wiki` — the hub files are in it.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-149.4
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
