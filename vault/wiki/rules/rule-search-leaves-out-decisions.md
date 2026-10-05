---
type: rule
kind: Leaf
purpose: Prevents the text of a Decision page from entering the context of the main agent, ask-guppi or case-guppi through a search of the vault
status: draft
enforcement: render
governs: .claude/rules/search-leaves-out-decisions.md
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-search-leaves-out-decisions-in-every-agent]]"]
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
---

## Purpose

Prevents the text of a Decision page from entering the context of the main agent, `ask-guppi` or `case-guppi` through a search of the vault. A Decision page states a Case at its moment, and the folder holds a page per Case, so a search over the whole wiki that does not leave them out fills the context with them. The frames of `ask-guppi` and `case-guppi` forbid the search, but none named a glob that works, and the one an agent wrote did not: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from the folder it searches, so `!decisions/**` over `vault/wiki/` left nothing out (case 640). The librarian follows its own frame, which flags such a read rather than forbids it. The rule stands in one file under `.claude/rules/`, which Claude Code loads into context with no `paths:` to scope it. Whether such a file loads inside a subagent was not documented when [[rule-page-read]] weighed one ([[lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction]]); this rule tries it, its Estimate reads whether it loads, and if it does not, a later Case moves the text to `CLAUDE.md`.

## Render

<!-- rule-search-leaves-out-decisions -->
# The text of Decision pages stays out of every search

This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.

- Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`.
- A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`.
- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names.
- A Glob may print the path of a Decision page: a path is no text of the page.
<!-- /rule-search-leaves-out-decisions -->

## History

- 2026-10-05 created · [[decision-case-640]]
- 2026-10-05 estimate estimate-search-leaves-out-decisions-in-every-agent added · [[decision-case-640]]
