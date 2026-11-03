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
estimates: ["[[estimate-guppi-config-fills-the-languages]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render]
core: true
---

## Purpose

Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `.guppi/guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`.

It also sets how the project tests its code and checks its style: the key `test` and the key `style`, each a list of commands. `uv run --project .guppi guppi test` runs the commands of `test`, and `uv run --project .guppi guppi style` the commands of `style`, which `.guppi/guppi/commands.py` reads from `guppi.toml` through `.guppi/guppi/config.py`. Each runs its commands in order, in the folder of the project and with no shell between, runs each one even after a red one, lets each print its own lines, and exits non-zero when any of them does. When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1. With `--exit-zero`, in each case, a missing file or key included, it prints one last line `exit code: <n>`, the exit code of the run without the flag, and exits 0, so a skill that runs it as a `!` command loads whatever the run finds. The Render holds the commands of the repository of GUPPI, and a project that installs GUPPI takes them as they stand, so its `guppi test` runs the tests of GUPPI until the setup Case of a project sets its own commands. Work Mode, Retro and the CI of the project run these two commands, so a project needs no tool but `uv`. The questions asked at setup, these two commands among them, belong to the setup Case of a project.

## Render

<!-- rule-guppi-config -->
# guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
documentation_lang = "en"
chat_lang = "ru"
test = ["uv run --project .guppi pytest -q .guppi/tests"]
style = ["uv run --project .guppi ruff check .", "uv run --project .guppi ruff format --check ."]
<!-- /rule-guppi-config -->

## History

- 2026-11-03 shipped with GUPPI
