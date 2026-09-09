---
title: "`.claude/templates/` — the forms a session's account is written from"
type: entity
status: current
authority: templates-directory
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/templates/handoff.md", ".claude/templates/retro.md", "scripts/vault-check.sh"]
tags: [harness, process]
---

# A directory that did not exist before 2026-08-17

`.claude/templates/` holds the two forms the end of a session is written on, and nothing else:

| File | What it is | Where its contents go |
|---|---|---|
| `.claude/templates/handoff.md` | the journal's form, copied by `/handoff` to `raw/handoffs/<YYYY-MM-DD>-<slug>.md` | each section carries a `→ ingest:` line naming the folder it is filed into |
| `.claude/templates/retro.md` | the interrogation that precedes it ([[the-retro-step]]) | each section carries a `→ handoff:` line naming the journal section it feeds |

**The mapping lives on the sections themselves and is copied nowhere** —
[[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]. Before 2026-08-17 it existed in six
files at once and was found only because it happened to contain a distinctive string.

## What the check reads from here

Rule 8 of `vault-check.sh` builds the expected section set by reading the `## ` headings of
`.claude/templates/handoff.md`, never from a list written into the script — regenerate and compare,
the same shape as `catalogue.md` ([[the-catalogue-is-generated-not-maintained]]). The cost is
stated in the rule: **a renamed heading is indistinguishable from a dropped one plus a new one**,
and it is reported as exactly that. What that rule judges, and when it stops judging, is
[[a-journal-is-judged-only-while-it-is-uncompiled]].

## The old form was archived, not deleted

`raw/handoffs/TEMPLATE.md` — the numbered form — moved to `archive/handoffs/TEMPLATE.md` on
2026-08-17. Deleting it would have falsified provenance: seven journals were written from it and
two pages cite it. **`raw/` now holds nothing but journals**, which is what
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]] asked of it, and the exception
`vault-coverage.sh` and the lint skill each carried for a filename is gone with it
([[a-journal-is-told-from-a-form-by-a-property-not-a-filename]]).

The form as it now stands, section by section, is
[[the-handoff-template-maps-onto-the-categories]]; the decision that gave it this shape is
[[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]].
