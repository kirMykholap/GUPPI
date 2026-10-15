---
type: rule
kind: Leaf
purpose: Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision
status: built
enforcement: render
implementation_ref: [.guppi/guppi/config.py, .guppi/guppi/commands.py, .guppi/tests/test_config.py, .guppi/tests/test_commands.py]
governs: guppi.toml
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-guppi-config-fills-the-languages]]", "[[estimate-guppi-config-runs-the-test-and-style-commands]]"]
origin: raw/2026-09-28/1318/ledger.md#case-476.1
sprint: migration
created: 2026-09-28
tags: [harness, render]
core: true
---

## Purpose

Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `.guppi/guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`.

It also sets how the project tests its code and checks its style: the key `test` and the key `style`, each a list of commands. `uv run --project .guppi guppi test` runs the commands of `test`, and `uv run --project .guppi guppi style` the commands of `style`, which `.guppi/guppi/commands.py` reads from `guppi.toml` through `.guppi/guppi/config.py`. Each runs its commands in order, in the folder of the project and with no shell between, runs each one even after a red one, lets each print its own lines, and exits non-zero when any of them does. When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1. The Render holds the commands of the repository of GUPPI, and a project that installs GUPPI takes them as they stand, so its `guppi test` runs the tests of GUPPI until the setup Case of `rule-morph` sets the project's own commands. Work Mode, Retro and the CI of the project run these two commands, so a project needs no tool but `uv` (case 820). The questions asked at setup, these two commands among them, stay with `rule-morph` (cases 476.1, 802); the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin` (case 802).

## Render

<!-- rule-guppi-config -->
# guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
documentation_lang = "en"
chat_lang = "ru"
test = ["uv run --project .guppi pytest -q"]
style = ["uv run --project .guppi ruff check .", "uv run --project .guppi ruff format --check ."]
<!-- /rule-guppi-config -->

## History

- 2026-09-28 created · [[decision-case-476.1]]
- 2026-09-28 estimate estimate-guppi-config-fills-the-languages added · [[decision-case-476.1]]
- 2026-09-28 status: draft → built · cascade
- 2026-10-13 updated: the category set leaves rule-morph for the Backlog of entity-sprint-plugin (case 802) · [[decision-case-802]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: guppi.toml sets the commands of the tests and of the style check, which guppi test and guppi style run · [[decision-case-820.2]]
- 2026-10-15 estimate estimate-guppi-config-runs-the-test-and-style-commands added · [[decision-case-820.2]]
- 2026-10-15 updated: every live rule, entity and Estimate names guppi test and guppi style in place of the targets test and style of the Makefile · [[decision-case-820.7]]
- 2026-10-15 status: built → draft · cascade
- 2026-10-15 updated: the Purpose names the setup Case of rule-morph by its new name · [[decision-case-825]]
- 2026-10-15 status: draft → built · cascade
