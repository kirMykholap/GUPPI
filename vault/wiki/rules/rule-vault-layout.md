---
type: rule
kind: Leaf
purpose: Prevents a file from sitting in the vault in a place nobody ratified — under a category it does not belong to, under a name that is not its slug, or at the root of wiki/ with no rule that writes it
status: draft
enforcement: check
implementation_ref: [guppi/lint.py, tests/test_lint.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-vault-layout-holds]]"]
origin: raw/2026-09-22/1121/ledger.md#case-315
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Purpose

Prevents a file from sitting in the vault in a place nobody ratified. The vault is `vault/wiki/`: one folder per page category — `entities/`, `rules/`, `estimates/`, `lessons/`, `insights/`, `decisions/` — each holding its pages and the `schema.yaml` its rule renders. The filename is the slug: there is no register of identifiers, `ref` and `origin` name filenames, and a page whose `slug` is not its filename is a finding. A page belongs to the folder of its `type`.

No file of `wiki/` is written by hand. A file is a page, the Render of a page — `sprint.md` from `entity-sprint-migration` under `rule-sprint`, `glossary.md` from `entity-glossary` under `rule-glossary`, `case-schema.md` from `rule-case-protocol` — or a record a script keeps by a named rule: `backlog.md` from `guppi backlog` under `rule-backlog`, `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of tags already ratified in a Case. A `.md` at the root that no live rule page names is a finding: it reached the vault without a decision. `raw/` and `archive/` are the working folders of a session, held by `rule-raw-archive`; the shape of a page is held by its category's schema rule.

## History

- 2026-09-22 created · [[decision-case-315]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-27 updated: backlog.md named among the files at the root of wiki/ (case 451.11) · [[decision-case-451.11]]
- 2026-09-29 status: built → draft · cascade
