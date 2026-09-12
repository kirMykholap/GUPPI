---
type: rule
kind: MOC
purpose: Keeps the three rules that share .claude/settings.json from becoming two copies of one file
status: draft
enforcement: render
governs: .claude/settings.json
render_mode: full
parent: rule-harness
children: [rule-default-mode, rule-permissions, rule-hook-registry]
estimates: [estimate-settings]
origin: raw/2026-09-12/ledger.md#case-85.2
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Purpose

Keeps the three rules that share `.claude/settings.json` from becoming two copies
of one file. The permission mode a session opens in, what may be written without a
question, and which hook fires on which event are three different rules with three
different criteria, and one file carries all three. This page is the file: its body
is the whole of `settings.json`, and each `<!-- child -->` line names the page that
owns that text.

`parent: rule-harness`: the file belongs to no phase of the session.

## Render

<!-- rule-settings -->
{
  "permissions": {
<!-- rule-default-mode -->
<!-- rule-permissions -->
  },
  "hooks": {
<!-- rule-hook-registry -->
  }
}
<!-- /rule-settings -->

## Estimates

- [[estimate-settings]]

## Children

1. [[rule-default-mode]]
2. [[rule-permissions]]
3. [[rule-hook-registry]]

## Parent

- [[rule-harness]]

## History

- 2026-09-12 created · [[decision-case-85.2]]
- 2026-09-12 estimate estimate-settings added · [[decision-case-85.2]]
