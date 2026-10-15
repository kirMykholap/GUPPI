---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py for the version of the highest tag, a tag of another form and a commit with no such tag; by hand, after a run of .github/workflows/prod.yml on a tag prod-x.y.z of a commit of plugin that writes prod, before the close of the sprint plugin: its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote, the version in .claude-plugin/plugin.json of prod and the on: block of .github/workflows/prod.yml read against the Criterion; the person's answer at the close of plugin when no such run comes before it"
checked: 2026-10-14
origin: raw/2026-10-10/1713/ledger.md#case-756.5
sprint: plugin
created: 2026-10-10
tags: [sprint, ci, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-x.y.z`, such as `prod-0.2.0`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.
**＋** `uv run --project .guppi guppi ship <folder>` runs on a commit with no tag `prod-x.y.z` in its history.

Then:
The run writes the clean version that `uv run --project .guppi guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
**＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
**＋** `prod` holds each page with `core: true` and no other page.
**＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository; a sample, as `rule-clean-branch` sets it, such as a string of a test, is no reference.
**＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
**＋** The `version` of `.claude-plugin/plugin.json` on `prod` is the number of the highest tag `prod-x.y.z` in the history of the commit it was built from, such as `0.2.0` for `prod-0.2.0`, and a tag of another form, such as `prod-2`, gives no version.
**＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
**－** `uv run --project .guppi guppi ship <folder>` with no tag `prod-x.y.z` in that history exits 1 and writes nothing, and `uv run --project .guppi guppi ship --check` reads no tag.
**－** A run whose `uv run --project .guppi guppi ship` exits 1 fails and writes nothing to `prod`, as it does while a page with `core: true` stands `draft`, which `estimate-clean-branch-refuses-a-draft-core-page` checks.
**－** A run whose clean version equals the last commit of `prod` adds no commit.

## Result

2026-10-14, Retro of session 1536, gh run view 38585781386 (tag prod-2, commit c95e7579) and git grep over origin/prod: the run succeeded and pushed through the ruleset bypass with the deploy key of PROD_DEPLOY_KEY ("Bypassed rule violations for refs/heads/prod", 34ae3bee..c363e8a9 HEAD -> prod); c363e8a9 is one new commit on top of 34ae3bee, "The clean version of GUPPI, built from c95e75791a69…"; prod holds 85 pages, the same set as the 85 pages with core: true at c95e7579; no frontier.md, sprint.md, brief.md, backlog.md, log.md, guppi.toml, .github/, raw/ or archive/; every case id left stands in a code span, a fenced block or the form [case N], and the schema.yaml origins raw/2026-09-08/… are the example pages of its examples block; the on: block runs on a push to main and to a tag prod-*; the two − lines were read from the workflow text, not from a run

## History

- 2026-10-10 created · [[decision-case-756.5]]
- 2026-10-10 updated: the Criterion replaced whole — CI starts on a commit to the branch plugin, where the sprint commits · [[decision-case-767]]
- 2026-10-13 updated: the Criterion replaced whole — the run on a tag prod-* of plugin, the commit on top of prod, prod holds exactly the pages with core: true, the push with the deploy key of PROD_DEPLOY_KEY (case 804) · [[decision-case-804.7]]
- 2026-10-14 status: pending → failed · raw/2026-10-14/1536/ledger.md#L3
- 2026-10-14 status: failed → passed · raw/2026-10-14/1536/ledger.md#L10
- 2026-10-15 updated: the Criterion replaced whole — the run on a tag prod-x.y.z writes prod with the version of that tag, and guppi ship exits 1 with no such tag in the history · [[decision-case-816.2]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
