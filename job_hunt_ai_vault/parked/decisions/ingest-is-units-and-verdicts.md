---
title: "Ingest is units with verdicts, because «fully processed» has to be a question a script can answer"
type: decision
status: current
authority: ingest-completeness
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", ".claude/skills/ingest/SKILL.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md"]
tags: [process, testing]
---

# Ingest is units with verdicts

**Decided by the owner on 2026-08-13**, during the very first migration, and correctly.

The earlier definition was "read the document and file its sections". That is a wish, not an
operation: it cannot be checked, it only works on documents written to our own template, and it has
no answer at all to the question the owner actually asked — **how do I know a document has been
turned into knowledge completely?**

## What replaced it

A source is split into units **by a script**. A unit is one claim: a heading, a table row, a
bullet, a numbered item, or the opening line of a paragraph. (It was "a paragraph or bullet opening
in **bold**" until 2026-08-13, and that narrowness hid whole sections written in plain prose.)
**Content inside a code fence is not a unit at all** — see [[vault-scripts]] for what that leaves
uncovered.

Every unit gets exactly one verdict, in a sidecar beside the immutable source
(`<source>.coverage.tsv`):

| verdict | meaning |
|---|---|
| `page:<name>` | compiled into that wiki page |
| `journal` | session state, not knowledge; stays in `raw/` |
| `elsewhere:<where>` | belongs to `CLAUDE.md`, the code, or the tracker |
| `skip:<reason>` | deliberately not compiled, and why |

**There is no fifth option.** "Is this finished?" becomes "are there units without a verdict?"

And `page:X` is not a plan to write X later: **the verdict is the write**, asserted in the same act
— [[the-verdict-is-the-write]].

## Why the script must produce the units

If the party that accounts for the units also decides what the units *are*, a forgotten section
never appears on the list, and its absence is invisible.

That is not hypothetical. On the first migration §1 of `docs/HANDOFF.md` was lost entirely **while
the ingest log recorded that §1 had been read**. Nothing caught it until an outside reviewer
compared the two by hand. A mechanical denominator is what makes that failure impossible rather
than merely unlikely.

## Coverage is not fidelity

**Coverage** — nothing dropped. Mechanical, free, 100% required.

**Fidelity** — what was compiled says what the source said. **No script can check it.** The
Critical of the same migration — a page describing behaviour a later slice had replaced — passes
coverage without a murmur: the page exists and its identifiers match.

Fidelity is checked by **sampling** (the sidecar carries the source line, so ten random pairs read
side by side take ten minutes) and by the acceptance questions. A review agent is worth its cost
only when a whole document moves.

Running one and calling it the other is the mistake this page exists to prevent.

## Where it is written down, and what it obliges

The operation lives in `.claude/skills/ingest/SKILL.md`; the two scripts that make it mechanical
are [[vault-scripts]]. Two obligations follow from this decision and are worth naming separately:

- **the sidecar is the gate on retiring a source.** `docs/HANDOFF.md` is not retired until every
  unit `scripts/vault-units.sh` finds in it carries a verdict, and the gate is the script rather
  than the number: [[handoff-retires-only-when-every-unit-has-a-verdict]]. The two numbers that
  appear when it is run are both right — `vault-units.sh` emitted **362** lines for that file on
  2026-08-13 and `vault-coverage.sh` reported **332 of 332**, because the arbiter does not count
  the 30 headings, which carry verdicts anyway;
- **a fidelity failure passes coverage in silence.** The instance that proves it is
  [[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]].

The question that produced this definition was the owner's, and it was a question about checking:
[[the-owners-question-was-how-would-you-check-that]].
