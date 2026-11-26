---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the Renders of the skills that ship name the main branch by {{main_branch}}, or, in the session of a ratified setup Case, by the name that Case sets, which /sprint-open writes into the prompt of the opening Case, their files by the name that rule-guppi-config sets, and the Purposes of rule-git-context and rule-work-mode by words
method: "by hand, after the librarian's run of the session that sets this method: a Grep of the pages and the files the Criterion names for main and for {{main_branch}}, and the output of uv run --project .guppi guppi render --check, read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-26/1515/ledger.md#case-1070.4
sprint: plugin
created: 2026-11-26
tags: [sprint, git, harness]
once: true
---

## Criterion

When:
After the librarian's run of the session that ratified this check, someone reads the `## Render` and the `## Purpose` of `rule-git-context`, `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-work-mode` and `rule-where-to-stop`, and the files that `guppi render` writes from them.

Then:
Each place where those Renders name the main branch of the project, in prose or in a `git` or `gh` command, writes `{{main_branch}}`.
**＋** The file each of them governs writes there the value of `main_branch` that the `## Render` of `rule-guppi-config` sets, and `uv run --project .guppi guppi render --check` exits 0.
**＋** Step 4 of the Render of `rule-skill-sprint-open` says that, in a session that ratified the setup Case of `rule-morph`, the main branch of that step is the name that the `update` of `rule-guppi-config` of that Case sets, and that the step writes that name into the prompt of the opening Case beside the branch of `Branch:`.
**＋** The paragraph of the Render of `rule-work-mode` on the branch and the fifth condition of `rule-where-to-stop` say that, where the Spec holds the setup Case of `rule-morph`, the main branch is the name that its `update` of `rule-guppi-config` sets.
**＋** The `## Purpose` of `rule-git-context` and of `rule-work-mode` names the main branch in words, not as `main`.
**－** The `gh` placeholders `{owner}` and `{repo}` of `rule-skill-sprint-close` stay as they are.

## History

- 2026-11-26 created · [[decision-case-1070.4]]
