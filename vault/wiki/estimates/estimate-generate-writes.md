---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: What generate writes to a page for each kind of entry of a materialize.yaml, and nothing an entry does not carry
method: pytest in .guppi/tests/test_generate.py against a temp vault; the live reading once by hand
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`guppi generate` applies one entry of a yaml to a page.

Then:
A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
**＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
**＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
**＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
**＋** An `update` whose item carries `drop`, a list of section names, removes each section it names from the page, its heading and its text; an item that carries `drop` alone applies.
**＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
**＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
**＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
**＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity only.
**＋** The folders whose page takes `deferred_by` are `DEFERRABLE` of `.guppi/guppi/materialize.py`, which `.guppi/guppi/generate.py` imports; they are the folders whose `schema.yaml` under `vault/wiki/` lists `deferred_by`.
**＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
**＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
**＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
**＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
**－** A name under `drop` of a section the page does not carry fails the entry alone (`estimate-generate-fails-alone`), with the name on stderr, and nothing of `set`, `sections`, `replace` or `drop` of the item is written to the page.
**－** A name under `drop` of a section that the schema of the page's category requires of the page fails the entry the same way: `check_schema` of `.guppi/guppi/lint.py`, run over the page with the section and without it, gives a finding without it that it does not give with it.
**－** A `defer` of a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, changes no page and appends nothing to `vault/wiki/log.md`: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr.
**－** A `defer` of an Estimate or an Insight whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `.guppi/guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for an Insight.
**－** No body section is derived from a ref field; a section the entry does not name under `sections` or `drop`, or reach by `replace`, is not touched.
**－** The `set` of an `update` of an Estimate that carries `method` removes no section by itself.
**－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
