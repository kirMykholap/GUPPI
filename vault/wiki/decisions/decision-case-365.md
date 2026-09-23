---
type: decision
case: "365"
status: current
update: ["[[rule-page-generation]]", "[[rule-materialize]]"]
origin: raw/2026-09-23/1126/ledger.md#case-365
sprint: migration
created: 2026-09-23
tags: [harness, workflow, ledger]
---

## Context

Case 321 retired the term "Rule-class"; case 320 took the `file` route out of the scripts, and `find_item` of `guppi/materialize.py` finds a `then` item by `slug` alone. The texts of the code did not follow: the docstring of `guppi/materialize.py` says the item "of a Rule-class file" is found "by `slug`, or by `file`"; the docstring of `guppi/generate.py` names "a Rule-class file entry" where the code tells any entry with no category (`unknown`) and ticks nothing for it; the docstring of `wikilink` says "a Rule-class slug" for a slug without a category prefix; three test names carry the term (`tests/test_lint.py`, `tests/test_pages.py`, `tests/test_render.py`). The grep of `estimate-sprint-migration-rule-class-files-dissolved` does not catch them: it looks for `RULE_CLASS`, `rule_class_path`, `prose_names` and "applied by hand".
`rule-page-generation` stands `draft`, `rule-materialize` `built`; only texts change and no behaviour, so no Estimate of either rule is touched; the `method` of `estimate-sprint-migration-rule-class-files-dissolved` is item C4 and does not change here; no `create`.

## Problem

The docstrings and the test names describe a route and a class of files that no longer exist, and give the reader of the code a false model — a `then` item found by `file`.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-365
