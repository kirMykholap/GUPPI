---
type: decision
case: "1028"
status: current
children: ["[[decision-case-1028.1]]", "[[decision-case-1028.2]]"]
origin: raw/2026-11-04/0358/ledger.md#case-1028
sprint: plugin
created: 2026-11-04
tags: [ci, hooks, plugin, git, harness, render, tests, session, workflow]
---

## Problem

The agent writes a bare case number into a comment or a docstring under `.guppi/`, and nothing tells it so until the full test run at the end of Work Mode, so the fix is a second pass; the hook that tells it serves only the build of the clean copy and must not reach a project that installs GUPPI.

## Recommend

- **What catches a bare case number when it is written**
  - Recommended: (a) a hook after each write under `.guppi/`.
  - Answer: (a), the recommendation accepted.
- **Whether the hook stops the write or speaks after it**
  - Recommended: (b) a note after the write.
  - Answer: (b), the recommendation accepted.
- **Which page holds the hook**
  - Recommended: (b) a paragraph of `rule-clean-branch`.
  - Answer: (b), the recommendation accepted.
- **How the change is checked**
  - Recommended: (a) a new Estimate on the page of the hook.
  - Answer: (a), the recommendation accepted.
- **Where the leaving-out of the hook goes**
  - Recommended: (a) this Case again, with two parts.
  - Answer: (a), the recommendation accepted.
- **How the copy drops the registration**
  - Recommended: (a) one named entry, removed from both texts.
  - Answer: (a), the recommendation accepted.
- **When a text without the entry stops the build**
  - Recommended: (b) stop only where the hook is named in another form.
  - Answer: (b), the recommendation accepted.
- **Change**
  - Asked: `/pre-spec` asked where the tests of the hook live and whether the hook enters the clean copy, and the person chose that the hook does not ship, its tests staying in `test_ship.py`.
  - Taken: the hook and its registration stay out of the clean copy, set in Case 1028.2; `.claude/settings.json` joins the `implementation_ref` of `rule-clean-branch`.

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#case-1028
