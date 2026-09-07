---
title: "The mapping is documented at each hop and copied nowhere"
type: concept
status: current
authority: mapping-location
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/templates/retro.md", ".claude/templates/handoff.md", ".claude/skills/ingest/SKILL.md"]
tags: [harness, process]
---

# The route a finding travels, and where each leg is written down

A finding made during a session reaches a wiki page in two hops, and **each hop is documented on the
document that performs it**:

| hop | written where | in what form |
|---|---|---|
| retro finding → journal section | `.claude/templates/retro.md` | a `→ handoff:` line on every section |
| journal section → wiki folder | `.claude/templates/handoff.md` | a `→ ingest:` line on every section |

**Both skills read those lines rather than restating them.** `/handoff` reads the first template,
`/ingest` reads the second, and neither carries a copy. The cut is by heading text, so a renamed
heading changes where knowledge lands — which is why rule 8 of `vault-check.sh` compares a journal's
headings against that same file ([[a-journal-is-judged-only-while-it-is-uncompiled]]).

## Before this, the mapping existed in six copies

Dropping the section numbers on 2026-08-17 forced a sweep, and the string `section 7` turned up in
`.claude/skills/ingest/SKILL.md`, `.claude/skills/handoff/SKILL.md`,
`.claude/skills/vault-ask/SKILL.md`, `.claude/agents/vault-librarian/AGENT.md`, the repository's own
`CLAUDE.md`, and the handoff template itself.

**None of them was wrong when written.** They drifted because the template changed under them —
which is the failure [[marked-regions-and-the-prose-outside-them]] is designed to make impossible,
and this is the measured case for that design: **six copies, no detector, and the only reason all
six were found is that the thing they copied happened to be a distinctive string.** A renamed
heading would not have been.

## What the shape costs and what it buys

**A pointer is checkable and a copy is not** ([[claude-md-may-point-and-may-not-assert]]). The price
is one more file to open when tracing where something goes; the alternative price is the one already
paid — a number that moved every time a section was inserted, and five files that went on quoting it
([[no-rule-reads-a-harness-file]]).

## The agent path in the list above is left as written — noted 2026-08-20

**`.claude/agents/vault-librarian/AGENT.md` moved back to `.claude/agents/vault-librarian.md`**, and
this page is **not** repointed. The list records where a sweep found `section 7` on 2026-08-17, which
is a claim about a past reading; rewriting it would make the sentence assert something that never
happened ([[fidelity-to-a-source-and-fidelity-to-the-tree]], [[a-path-detector-for-prose-references]]).
