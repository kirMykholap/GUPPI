---
type: rule
kind: Leaf
purpose: "Prevents the text of a Decision page from entering the context of an agent through a search of the vault: a hook leaves the Decision pages out of every Grep over the wiki, and the main agent, ask-guppi and case-guppi read a Decision page only for a reason of their frame"
status: draft
enforcement: render
implementation_ref: [.guppi/guppi/grepguard.py, .guppi/tests/test_grepguard.py, .claude/settings.json]
governs: .claude/rules/search-leaves-out-decisions.md
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-search-leaves-out-decisions-in-every-agent]]", "[[estimate-search-leaves-out-decisions-by-the-grep-hook]]", "[[estimate-search-leaves-out-decisions-refuses-ask-guppi]]"]
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
core: true
---

## Purpose

Prevents the text of a Decision page from entering the context of the main agent, `ask-guppi` or `case-guppi` through a search of the vault. A Decision page states a Case at its moment, and the folder holds a page per Case, so a search over the whole wiki that does not leave them out fills the context with them. The Grep tool reads a glob that holds a slash from the working directory, the root of the project, and not from the folder it searches, so `!decisions/**` over `vault/wiki/` leaves nothing out (case 640). The rule stands in one file under `.claude/rules/`, which Claude Code loads into the context of every agent with no `paths:` to scope it (in the reading of session 1343). The file alone does not keep the Decision pages out of a Grep, so a `PreToolUse` hook on Grep adds the exclusion at the end of the glob, in every agent, the librarian too; a Grep inside `vault/wiki/decisions/` it leaves unchanged but for a call of `ask-guppi`, whose Read of a Decision page and Grep inside that folder the same hook refuses, and the file keeps the rule on reading a Decision page (nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out, in the reading of session 1343, case 664.1). The librarian follows its own frame, which flags such a read rather than forbids it; the hook filters its Greps over the wiki too, and a read of a Decision page it needs stays open to it (case 664.1).

## Render

<!-- rule-search-leaves-out-decisions -->
# The text of Decision pages stays out of every search

This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.

- A hook adds `!**/decisions/**` at the end of the `glob` of every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, in every agent, the librarian too, whom the rest of this file does not bind; a Grep over such a folder prints nothing under `vault/wiki/decisions/`, and an exclusion written first, where it does not work, is put last by the hook (case 664.1).
- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, or by a Grep whose `path` is that folder or lies in it, which the hook leaves unchanged but for a call of `ask-guppi`, and only for a reason the frame of the agent names (case 664.1).
- The frame of `ask-guppi` names no reason to read a Decision page, and one reason to try such a call: a trial of the hook that a ratified Case names, the call made to be refused; so the same hook, on `Read` and on `Grep`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` made by `ask-guppi`, and leaves such a call of another agent unchanged (as set in cases 925.1 and 954.3).
- A Glob may print the path of a Decision page: a path is no text of the page.
<!-- /rule-search-leaves-out-decisions -->

## History

- 2026-10-05 created · [[decision-case-640]]
- 2026-10-05 estimate estimate-search-leaves-out-decisions-in-every-agent added · [[decision-case-640]]
- 2026-10-05 estimate estimate-search-leaves-out-decisions-by-the-grep-hook added · [[decision-case-664.1]]
- 2026-10-05 updated: a PreToolUse hook on Grep adds !**/decisions/** at the end of the glob in every agent, a Grep inside decisions/ left unchanged; the Render keeps the rule on reads; purpose set anew (case 664.1) · [[decision-case-664.1]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the session stands in a bracket · [[decision-case-809]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the Purpose gives the reasons of the rule, its trials in brackets, and names no lesson · [[decision-case-881.10]]
- 2026-10-30 updated: the hook refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ by ask-guppi (case 925.1) · [[decision-case-925.1]]
- 2026-10-30 estimate estimate-search-leaves-out-decisions-refuses-ask-guppi added · [[decision-case-925.1]]
- 2026-10-30 status: built → draft · cascade
- 2026-10-31 updated: the frame of ask-guppi names the hook trial as its one reason to try a call on a Decision page (case 954.3) · [[decision-case-954.3]]
