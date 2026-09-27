---
type: estimate
kind: QA
status: pending
target: "[[rule-agent-writing]]"
purpose: The agent's text holds to the section How the agent writes of CLAUDE.md, and the person's complaint is the test
method: by hand in a later session — the person's messages of one session read for a complaint about the agent's text, against the section in CLAUDE.md
checked: 2026-09-27
origin: raw/2026-09-20/1308/ledger.md#case-272.3
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

When:
A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

Then:
The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
**－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
**－** The code the agent writes is not a text of this rule; `make style` judges the code.

## Result

2026-09-27, by hand, the section How the agent writes of CLAUDE.md and the replies of session 2300; counts checked against their runs held (20 task lines, 15 findings, 734 passed), but the reply that acknowledged the re-ratification of 443 to 446 said the ledger gained amended lines of 445.6 while the tail shows L25 and L26 unchanged and L31 alone new, and one reply said W32 closes with sprint, a closer the Frontier gives only to sprint items, corrected in the next reply

## History

- 2026-09-20 created · [[decision-case-272.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L4
- 2026-09-23 updated: the Criterion names the width of a claim (case 359) · [[decision-case-359]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L36
- 2026-09-27 status: failed → failed · raw/2026-09-26/2300/ledger.md#L36
- 2026-09-27 updated: the Criterion replaced whole — the person's complaint is the test of the agent's text, a slip the agent corrected itself no fault (case 450) · [[decision-case-450]]
