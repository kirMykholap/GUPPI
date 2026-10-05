# The text of Decision pages stays out of every search

This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.

- A hook adds `!**/decisions/**` at the end of the `glob` of every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, in every agent, the librarian too, whom the rest of this file does not bind; a Grep over such a folder prints nothing under `vault/wiki/decisions/`, and an exclusion written first, where it does not work, is put last by the hook (case 664.1).
- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, or by a Grep whose `path` is that folder or lies in it, which the hook leaves unchanged, and only for a reason the frame of the agent names (case 664.1).
- A Glob may print the path of a Decision page: a path is no text of the page.
