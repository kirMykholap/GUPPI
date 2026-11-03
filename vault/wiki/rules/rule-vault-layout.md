---
type: rule
kind: Leaf
purpose: Prevents a file from sitting in the vault in a place nobody ratified — under a category it does not belong to, under a name that is not its slug, or at the root of wiki/ with no rule that writes it
status: built
enforcement: check
implementation_ref: [.guppi/guppi/lint.py, .guppi/tests/test_lint.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-vault-layout-holds]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Purpose

Prevents a file from sitting in the vault in a place nobody ratified. The vault is `vault/wiki/`: one folder per page category — `entities/`, `rules/`, `estimates/`, `lessons/`, `insights/`, `decisions/` — each holding its pages and the `schema.yaml` its rule renders. The filename is the slug: there is no register of identifiers, `ref` and `origin` name filenames, and a page whose `slug` is not its filename is a finding. A page belongs to the folder of its `type`.

No file of `wiki/` is written by hand but the header of `tags.md` above its table and what a merge of `main` into a branch writes: the joined text of a page that both a branch and `main` changed, which a Case signs and Work Mode writes into the page, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes`. That header is written by hand: a one-off task that a ratified Case names changes it in Work Mode. A file is a page, the Render of a page — `sprint.md` from the live sprint page `entity-sprint-<id>` under `rule-sprint`, `glossary.md` from `entity-glossary` under `rule-glossary`, `case-schema.md` from `rule-case-protocol` — or a record a script keeps by a named rule: `backlog.md` from `guppi backlog` under `rule-backlog`, `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of tags, each declared by a tag line of a ratified Case or by a `{newtag:...}` block of a lesson line, its rows written by `generate`. A `.md` at the root that no live rule page names is a finding: it reached the vault without a decision. `raw/` and `archive/` are the working folders of a session, held by `rule-raw-archive`; the shape of a page is held by its category's schema rule.

## History

- 2026-11-03 shipped with GUPPI
