---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data, and fails when one remains
method: "by hand, in a session of the sprint plugin before its close: the CI run that a tag prod-* on a commit of plugin starts, its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote and the on: block of .github/workflows/prod.yml read against the Criterion"
checked: 2026-10-14
origin: raw/2026-10-10/1713/ledger.md#case-756.5
sprint: plugin
created: 2026-10-10
tags: [sprint, ci, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-*`, such as `prod-1`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.

Then:
The run writes the clean version that `uv run guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
**＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
**＋** `prod` holds each page with `core: true` and no other page.
**＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository.
**＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
**＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
**－** A run whose `uv run guppi ship` exits 1 fails and writes nothing to `prod`.
**－** A run whose clean version equals the last commit of `prod` adds no commit.

## Result

2026-10-14, Retro of session 1536, gh run view 38585781386 (tag prod-2, commit c95e7579) and git grep over origin/prod: the run succeeded and pushed through the ruleset bypass with the deploy key of PROD_DEPLOY_KEY ("Bypassed rule violations for refs/heads/prod", 34ae3bee..c363e8a9 HEAD -> prod); c363e8a9 is one new commit on top of 34ae3bee, "The clean version of GUPPI, built from c95e75791a69…"; prod holds 85 pages, the same set as the 85 pages with core: true at c95e7579; no frontier.md, sprint.md, brief.md, backlog.md, log.md, guppi.toml, .github/, raw/ or archive/; every case id left stands in a code span, a fenced block or the form [case N], and the schema.yaml origins raw/2026-09-08/… are the example pages of its examples block; the on: block runs on a push to main and to a tag prod-*; the two − lines were read from the workflow text, not from a run

## History

- 2026-10-10 created · [[decision-case-756.5]]
- 2026-10-10 updated: the Criterion replaced whole — CI starts on a commit to the branch plugin, where the sprint commits · [[decision-case-767]]
- 2026-10-13 updated: the Criterion replaced whole — the run on a tag prod-* of plugin, the commit on top of prod, prod holds exactly the pages with core: true, the push with the deploy key of PROD_DEPLOY_KEY (case 804) · [[decision-case-804.7]]
- 2026-10-14 status: pending → failed · raw/2026-10-14/1536/ledger.md#L3
- 2026-10-14 status: failed → passed · raw/2026-10-14/1536/ledger.md#L10
