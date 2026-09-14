---
type: decision
case: "148.2"
status: current
update: [rules-schema, entities-schema, estimates-schema, lessons-schema, insights-schema, decisions-schema, index]
origin: raw/2026-09-14/1633/ledger.md#case-148.2
sprint: migration
created: 2026-09-14
tags: []
---

## Context

The ref fields of the frontmatter — `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` on the category pages; `create`, `update`, `delete`, `defer`, `supersedes`, `superseded_by` on the Decision pages — are bare slugs. Obsidian takes only `[[slug]]` in a property as a link; the graph, backlinks, `unresolved` and Bases do not see a bare string. The owner uses the graph, backlinks and Bases and sees the structure only through the body sections `generate` duplicates from the fields, and Decision → target not at all. The `#L` tag in the tag pane comes from one line `origin #L<n>` outside a code span in the Criterion of `estimate-materialize-assembles`; `#case-9`, `#case-11`, `#case-13`, `#case-15.x` from three hand-written lines of 2026-09-09 in `log.md`. A pointer like `ledger.md#L122` is no tag: Obsidian does not read a `#` inside a word as one.

## Problem

The scripts read the frontmatter in one place — `pages.read_page` (plus `materialize.page_estimates`, its own parser of the `estimates` field) — and write it in one — `generate.write_page`. Decide: write the ref fields as `"[[slug]]"`, strip the brackets on read, migrate 313 live and 86 archived pages in one run; fix the schemas; remove the four false tags.

## Given

`rule-page-generation` `built`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`, "the only writer to `wiki/`"; `generate.frontmatter()`/`flow()`/`scalar()` — `scalar` quotes a string through `json.dumps` when `NEEDS_QUOTE` matches (a leading `[` does), so `[[a]]` is written quoted; unquoted, YAML reads it as a nested list; `KEY_ORDER` per category.
**＋** `pages.read_page` — `yaml.safe_load` of the frontmatter; used by lint, index (leaves with 147), cleanup, generate, pretask, archive. `materialize.page_estimates` parses the frontmatter itself and reads `estimates`. `lint.LINK_FIELDS = (parent, children, estimates, target, addressed_by, insight, deferred_by)`; `links_of` reads `props`.
**＋** Decision pages: `create`/`update`/`delete`/`defer` are lists of slugs "a page, or a Rule-class file such as `case-schema`"; lint: "every slug with a category prefix a live or archived page"; `supersedes`, `superseded_by` are decision slugs.
**＋** Schemas: `rules/schema.md` `parent` "slug", `children` "ordered list of slugs", `estimates` "list of slugs", `deferred_by` "list of decision slugs"; `entities/schema.md` the same; `estimates/schema.md` `target` "slug of an Entity or Rule"; `lessons/schema.md` `insight` "slug"; `insights/schema.md` `children`, `addressed_by`, `deferred_by`; `decisions/schema.md:16` "Lists of scalars, so Obsidian shows them as lists and links".
**＋** Obsidian ≥ 1.4: `"[[slug]]"` in a Text/List property is a link; the graph, backlinks, `unresolved` and Bases see it; a name resolves in any folder, the archive included (`rule-cleanup`: "Obsidian resolves a name in any folder"). The owner's graph is filtered `path:wiki`.
**＋** `origin` (`raw/<date>/<HHMM>/ledger.md#case-N`), `implementation_ref`, `governs` are paths; `tags` are strings; none is a link.
**＋** The false tags: `vault/wiki/estimates/estimate-materialize-assembles.md:27` "origin #L<n>" (the only live line with a bare `#L`); `vault/wiki/log.md:12–14` "#case-9 to #case-13", "#case-11", "#case-15.1, #case-15.2, #case-15.3" — lines of 09-09, "written by hand". `log.md` is a working file without a schema, written by `generate` and `cleanup`; no hook guards it.
**－** `cleanup` moves files without rewriting them; the `children`/`estimates` lists it rebuilds go through the writer of `generate` — the brackets appear by themselves. `render.py` reads no frontmatter link.
**－** Insight 138 (actioned): the derived texts are named — the body sections and lint do not change.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-148.2
