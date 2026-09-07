---
title: "A journal is told from a form by a property, not by a filename"
type: concept
status: current
authority: journal-versus-form
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/vault-check.sh", ".claude/skills/vault-lint/SKILL.md"]
tags: [testing, harness]
---

# The property, and the exception it replaced

**A journal carries a date in `session:`; a form carries the placeholder.** Rule 8 of
`vault-check.sh` selects on a `session:` line whose value is an ISO date, and needs to know nothing
else about the file.

It used to skip the template **by filename**. That exception outlived what it excepted: the template
left `raw/` for `archive/handoffs/` on 2026-08-17 ([[claude-templates-directory]]), and a name-based
skip would have gone on protecting a file that is not there — silently, because a skip that matches
nothing looks exactly like a skip that was never needed.

**An exception written by filename outlives what it excepted. A property cannot go stale that way.**

## The same defect was removed twice on one day

`.claude/skills/vault-lint/SKILL.md` skipped `*/TEMPLATE.md` in its coverage loop for the same
reason, and it was dropped the same day. Measured after removing it: **seven of seven sources report
`INGEST COMPLETE`** — the skip had been protecting nothing. The migrated 2026-08-12 document, the
one candidate for needing it, carries no frontmatter at all, so no field could have filtered it
either.

**`vault-coverage.sh` never mentioned the template**, though it was said twice that it skipped one:
that claim came from prose and from intention rather than from the file
([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

## Where it generalises

Any rule that names an instance rather than a property inherits the instance's lifetime. This corpus
has the same shape in three other places, and all three broke when the thing they named moved: a
mapping keyed to a section number ([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]), a
staleness check keyed to whichever filename sorted last ([[session-hooks]]), and a selftest clearing
inbound links from a copied list rather than sweeping the real one
([[a-copied-list-drifts-and-a-sweep-cannot]]).
