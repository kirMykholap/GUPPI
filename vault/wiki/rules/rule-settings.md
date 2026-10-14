---
type: rule
kind: MOC
purpose: Keeps the rules that share .claude/settings.json from becoming two copies of one file
status: built
enforcement: render
governs: .claude/settings.json
render_mode: full
parent: "[[rule-harness]]"
children: ["[[rule-default-mode]]", "[[rule-permissions]]", "[[rule-hook-registry]]", "[[rule-python-utf8]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render]
core: true
---

## Purpose

Keeps the rules that share `.claude/settings.json` from becoming two copies
of one file. The permission mode a session opens in, what may be written or read without a question, which hook fires on which event, and the environment every process of the
session runs with are different rules with different criteria, and one file carries
them all. This page is the file: its body is the whole of `settings.json`, and each
`<!-- child -->` line names the page that owns that text.

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
  },
<!-- rule-python-utf8 -->
}
<!-- /rule-settings -->

## History

- 2026-10-14 shipped with GUPPI
