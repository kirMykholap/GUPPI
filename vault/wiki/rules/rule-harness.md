---
type: rule
kind: MOC
purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
status: built
children: ["[[rule-render-harness]]", "[[rule-settings]]", "[[rule-lint]]", "[[rule-page-schemas]]", "[[rule-vault-layout]]", "[[rule-governed-files-hook]]", "[[rule-claude-md]]", "[[rule-bash-guard]]", "[[rule-tests-clock-pinned]]", "[[rule-context-size]]", "[[rule-page-read]]", "[[rule-guppi-config]]", "[[rule-search-leaves-out-decisions]]", "[[rule-shell-write-check]]", "[[rule-powershell-guard]]", "[[rule-guppi-package]]"]
estimates: []
applies_to: ["[[entity-guppi]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Purpose

Prevents the tools of the harness from drifting apart from the pages that describe them. The harness is the files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents under `.claude/`, `CLAUDE.md`, `case-schema.md` and `guppi.toml`. Three rules belong to no phase of the session: the renderer, the page
`.claude/settings.json` is assembled from, and lint. They run together in `uv run --project .guppi guppi check`, with the checks of `rule-sprint` and `rule-backlog` (children of `rule-documentation`) between them, in this order: the harness files are checked against their pages, the sprint file against its page, the backlog file against its sources, the glossary file against its page, then the pages. More belong here and run in no pipeline: the folder of the code of GUPPI and the command that runs it, the settings file of guppi, `guppi.toml`, the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash, a file write or an interpreter it feeds, the hook that refuses a PowerShell here-string piped into an interpreter, the hook that repairs or names a file a shell call left with CRLF line endings, a byte-order mark or bytes that are not UTF-8, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, the hooks that read a page of the vault without its History, and the file under `.claude/rules/` that keeps the text of Decision pages out of a search. The clean version of GUPPI holds no `Makefile`.

## History

- 2026-11-03 shipped with GUPPI
