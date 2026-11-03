---
type: estimate
kind: QA
status: passed
target: "[[rule-claude-md]]"
purpose: CLAUDE.md equals the Render of rule-claude-md with each child between its markers, and every session loads that text
method: "by hand, after a render of CLAUDE.md: uv run --project .guppi guppi render --check, and CLAUDE.md as the file holds it and as a session that starts after the render loads it, read against the Criterion"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render]
core: true
---

## Criterion

When:
`guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

Then:
`CLAUDE.md` is: the line `<!-- project-description -->`; the heading and the description of the project; the line `<!-- /project-description -->`; the paragraph "The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
**＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
**＋** Every session and every subagent loads this text.
**－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in `vault/wiki/ratification.md`; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
