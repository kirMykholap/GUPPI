---
type: estimate
kind: QA
status: archived
target: "[[rule-link-graph-at-session-start]]"
purpose: Whether the SessionStart hook writes .guppi/links.md whole at the start of a session, from the text guppi render writes, kept out of git, and stops no session on an error
method: "uv run --project .guppi pytest .guppi/tests/test_links.py, which runs guppi links --write over a vault in a temporary folder, a rendered file left unwritten and an error included; and by hand, after the first session start whose .claude/settings.json holds the hook: the time of .guppi/links.md against the session-start line of vault/raw/<date>/event_log.md, its block of .claude/skills/sprint-open/SKILL.md and the output of git status, read against the Criterion, the result in the estimate line"
checked: 2026-10-31
origin: raw/2026-10-31/1831/ledger.md#case-967.3
sprint: plugin
created: 2026-10-31
tags: [harness, session]
---

## Criterion

When:
Claude Code starts a session in the repository, and the `SessionStart` hook `uv run --project .guppi guppi links --write` runs.

Then:
It writes `.guppi/links.md` whole: one block per live page and per file that a page or a rendered file names, in the form `guppi links` prints.
**＋** It takes the text of each rendered file as `guppi render` writes it, so its result does not depend on whether `render --sync` on the same event has run.
**＋** `.guppi/.gitignore` keeps `.guppi/links.md` out of git.
**－** An error stops no session: the hook prints one line on stderr and exits 0.

## Result

2026-10-31, in Plan Mode of session 2307, by uv run --project .guppi pytest .guppi/tests/test_links.py, stat of .guppi/links.md, vault/raw/2026-10-31/event_log.md, .guppi/links.md, guppi links, guppi links --write, cmp, git check-ignore and git status: 13 passed; this session is the first start whose .claude/settings.json (line 23) holds the hook, rendered by the librarian of session 1831; the event log holds "23:06:55 8d8876d7 session-start startup" and .guppi/links.md was written at 23:06:56; its block "## .claude/skills/sprint-open/SKILL.md" stands at line 6139 and matches what guppi links prints for that path; guppi links --write run again exited 0 and wrote a file byte-identical to the one of the session start; git check-ignore names .guppi/.gitignore:2:links.md and git status does not list it; the error branch, one line on stderr and exit 0, was not met live and rests on the tests

## History

- 2026-10-31 created · [[decision-case-967.3]]
- 2026-11-01 status: pending → passed · raw/2026-10-31/2307/ledger.md#L4
- 2026-11-02 deleted · [[decision-case-999.1]]
- 2026-11-02 archived · cleanup
