# The text of Decision pages stays out of every search

This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.

- Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`.
- A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`.
- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names.
- A Glob may print the path of a Decision page: a path is no text of the page.
