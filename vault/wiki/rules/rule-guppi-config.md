---
type: rule
kind: Leaf
purpose: Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision
status: draft
enforcement: render
implementation_ref: [guppi/config.py, tests/test_config.py]
governs: guppi.toml
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-guppi-config-fills-the-languages]]"]
origin: raw/2026-09-28/1318/ledger.md#case-476.1
sprint: migration
created: 2026-09-28
tags: [harness, render]
---

## Purpose

Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`. The questions asked at install and the category set stay with `rule-morph` (case 476.1).

## Render

<!-- rule-guppi-config -->
# guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
documentation_lang = "en"
chat_lang = "ru"
<!-- /rule-guppi-config -->

## History

- 2026-09-28 created · [[decision-case-476.1]]
- 2026-09-28 estimate estimate-guppi-config-fills-the-languages added · [[decision-case-476.1]]
