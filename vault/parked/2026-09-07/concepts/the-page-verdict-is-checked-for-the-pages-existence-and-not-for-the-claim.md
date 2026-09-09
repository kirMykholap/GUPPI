---
title: "A `page:` verdict is checked for the page's existence and never for the claim"
type: concept
status: current
authority: page-verdict-verification
basis: code
sprint: S3
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-coverage.sh"]
tags: [vault, harness, testing]
---

# What the script actually asks

**`scripts/vault-coverage.sh` accepts four verdicts and validates one of them against the tree.**
`journal`, `elsewhere:<where>` and `skip:<reason>` are accepted on sight; `page:<name>` is looked up,
and the only failure it can report is `BAD VERDICT ... page:<name> does not exist in the wiki`.

**Nothing asks whether the named page carries the claim.** A verdict pointing at a real page that
says something else is green, and the ingest reports `INGEST COMPLETE`.

**The name parsing is deliberate and it is worth knowing**: names run up to ` — `, several are
separated by commas, and the prose after the dash is free text. Two other rules were tried and both
were wrong — truncating at the first space validated only the first name, and splitting on space
rejected the prose the file's own header promises.

# The gap has a measured instance

**A fidelity sample of ten verdicts found one wrong.** A journal line received `page:vault-scripts`;
the page received the neighbouring claim of the same paragraph, **and the observation itself, in the
owner's words, landed nowhere** — not in `wiki/`, not in `log.md`. The sidecar was complete and the
gate was green.

**This is coverage against fidelity, arriving from the direction the store already knows**
([[ingest-is-units-and-verdicts]],
[[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]).

# Where the other half of an instrument already exists

**`bash scripts/vault-check.sh --lint` already finds owner-attributed blocks**, so the machinery for
locating a marked utterance on a page exists. **What does not exist is the pairing**: a unit carrying
his words verbatim cannot take a `page:` verdict unless the named page contains those words.

**It is queued as harness work and is not built**
([[a-quote-written-for-the-librarian-carries-its-context]]).

# A page in `archive/` says the opposite about the same mechanism, and this one is right — 2026-08-29

**`a-coverage-verdict-is-checked-for-presence-and-never-for-resolvability` says
`scripts/vault-coverage.sh` resolves a `page:` verdict against the tree "not at all". It does.**
Line 109 strips everything after `" - "` and resolves each name, with nine lines of comment saying so
deliberately.

**This page is right about the same mechanism and that one is wrong.** It is named here because the
disagreement is otherwise invisible: **the two pages carry different `authority:` slugs**, so rule 3 of
the gate cannot see it, and no `CONTRADICTION` block is legal between them
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**No `CONTRADICTION` block is written and the other page is not edited.** It is in `archive/`, and what
an archived page asserts is frozen ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).
**The live answer is here**, which is the whole arrangement: `wiki/` is the source of truth and
`archive/` is history.

**The class is worth naming.** Two adjacent claims about one mechanism, given different slugs, produce a
disagreement no instrument in this store can find — the same shape the brief has been reporting about
the CRLF pair for three briefs running.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
