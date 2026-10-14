---
type: rule
kind: Leaf
purpose: Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision
status: built
enforcement: render
implementation_ref: [guppi/config.py, tests/test_config.py]
governs: guppi.toml
render_mode: full
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render]
core: true
---

## Purpose

Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`. The questions asked at install stay with `rule-morph`; the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin`.

## Render

<!-- rule-guppi-config -->
# guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
documentation_lang = "en"
chat_lang = "ru"
<!-- /rule-guppi-config -->

## History

- 2026-10-14 shipped with GUPPI
