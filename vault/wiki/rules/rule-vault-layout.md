---
type: rule
kind: Leaf
purpose: Prevents a file from sitting in the vault in a place nobody ratified — under a category it does not belong to, under a name that is not its slug, or at the root of wiki/ with no rule that writes it
status: built
enforcement: check
implementation_ref: [.guppi/guppi/lint.py, .guppi/tests/test_lint.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-vault-layout-holds]]"]
origin: raw/2026-09-22/1121/ledger.md#case-315
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
core: true
---

## Purpose

Prevents a file from sitting in the vault in a place nobody ratified. The vault is `vault/wiki/`: one folder per page category — `entities/`, `rules/`, `estimates/`, `lessons/`, `insights/`, `decisions/` — each holding its pages and the `schema.yaml` its rule renders. The filename is the slug: there is no register of identifiers, `ref` and `origin` name filenames, and a page whose `slug` is not its filename is a finding. A page belongs to the folder of its `type`.

No file of `wiki/` is written by hand, but for what a merge of `main` by `/merge-main` writes: the joined text of a page that both a branch and `main` changed, which the merge Case signs and Work Mode writes into the page, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes` (case 790). The header of `tags.md` above its table is written by hand too: a one-off task that a ratified Case names changes it in Work Mode (as set in case 827.4). A file is a page, the Render of a page — `sprint.md` from `entity-sprint-migration` under `rule-sprint`, `glossary.md` from `entity-glossary` under `rule-glossary`, `case-schema.md` from `rule-case-protocol` — or a record a script keeps by a named rule: `backlog.md` from `guppi backlog` under `rule-backlog`, `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of tags, each declared by a tag line of a ratified Case or by a `{newtag:...}` block of a lesson line, its rows written by `generate`. A `.md` at the root that no live rule page names is a finding: it reached the vault without a decision. `raw/` and `archive/` are the working folders of a session, held by `rule-raw-archive`; the shape of a page is held by its category's schema rule.

## History

- 2026-09-22 created · [[decision-case-315]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-27 updated: backlog.md named among the files at the root of wiki/ (case 451.11) · [[decision-case-451.11]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-13 updated: a merge of main by /merge-main writes the joined text of a conflicted page and git joins log.md and tags.md (case 790) · [[decision-case-790]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the header of tags.md changes by a one-off task by hand; a tag enters from a Case or a lesson line (case 827.4) · [[decision-case-827.4]]
