---
type: insight
pattern: the main agent closes a Frontier line by an Edit whose old_string holds only the end of the line and appends the closer there, so the box at the start of the line, which marks it closed, stays open and guppi prespec --check prints the line as open
status: open
children: ["[[lesson-orchestration-closes-a-frontier-line-by-its-closer-alone]]", "[[lesson-frontier-closer-appended-without-ticking-the-box]]"]
severity: 2
origin: raw/2026-11-02/1548/ledger.md#L12
sprint: plugin
created: 2026-11-02
tags: [orchestration, session, workflow]
---

## Pattern

Twice the main agent closed a Frontier line of frontier.md by an Edit that matched only the tail of the line and appended the closer, and left the box `[ ]` at its start: C7 at the ratification of Cases 977 and 978 (raw/2026-11-01/0141/ledger.md#L19), and C2, C3 and C5 in session 1548 (raw/2026-11-02/1548/ledger.md#L12). Each time the first run of guppi prespec --check printed the lines as open.

## Proposal

A suggestion, not a decision: the text of orchestration.md that sets the closers could say that a closer is the box and the tail together, written by one Edit whose old_string holds the whole line; or a command could close a Frontier line by its id, writing the box and the closer at once.

## History

- 2026-11-02 created · raw/2026-11-02/1548/ledger.md#L12
