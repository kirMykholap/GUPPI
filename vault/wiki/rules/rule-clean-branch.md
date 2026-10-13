---
type: rule
kind: Leaf
purpose: Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install
status: built
enforcement: check
implementation_ref: [guppi/ship.py, tests/test_ship.py, .github/workflows/prod.yml]
estimates: ["[[estimate-clean-branch-writes-a-clean-copy]]"]
applies_to: ["[[entity-guppi-repository]]"]
origin: raw/2026-10-13/1753/ledger.md#case-804.6
sprint: plugin
created: 2026-10-13
tags: [ci, git, plugin]
---

## Purpose

Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes. It exits 1 on each reference to a case, link to a page or a file it does not write, mention of a session of this repository, or section of a page without `core: true` that remains; a Case rewords that text at its source.

The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).

## History

- 2026-10-13 created · [[decision-case-804.6]]
- 2026-10-13 estimate estimate-clean-branch-writes-a-clean-copy added · [[decision-case-804.6]]
- 2026-10-13 status: draft → built · cascade
