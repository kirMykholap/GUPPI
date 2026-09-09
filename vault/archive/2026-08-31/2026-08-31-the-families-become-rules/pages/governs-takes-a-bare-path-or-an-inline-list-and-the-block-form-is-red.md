---
title: "`governs:` takes a bare path or an inline list, and the block form is red rather than silent"
type: decision
status: archived
authority: governs-value-syntax
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", "scripts/vault-inject.sh", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/rules/_schema.yaml"]
tags: [harness, vault, record-schema]
---

# The two legal spellings, 2026-08-21

**`governs: CLAUDE.md` and `governs: [CLAUDE.md]` mean the same thing, and nothing else is legal.**
The inline form is the spelling this corpus already writes `tags:` and `sources:` in, so a rule
naming two destinations is written the way every other list here is written. The pages carrying the
bare form were left exactly as they were.

**The block form is refused because the injector writes what it parses.** A spelling that is
half-parsed renders a rule into a subset of its destinations and leaves the gate reading the
remainder as drift — a silent wrong file rather than a loud refusal
([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).
**One spelling for the list, checked, beats two where one is guessed at.**

# The refusal is red, on the owner's ruling

**The session proposed a silent refusal and argued for it. The owner took the stronger form.**

**The reason is that the block form is legal YAML.** A YAML editor, and the PyYAML parser already on
the sprint list, both read it without complaint — so a silent refusal stops being a guard and
becomes a trap: the page looks right, the parser agrees, and the text lands in one file out of two
([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

**Rejected: silence**, which is what the session had designed.

**Not built.** `scripts/vault-check.sh` owes the verdict and its cases in both directions
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# What changed under it

**The field used to name one file.** [[governs-is-a-path-from-the-repository-root]] says so in those
words and stays correct about everything else it decides — a path from the repository root, resolved
against nothing else. **Only the cardinality moved**, and that page carries a dated note saying so.

**How it is parsed and how the readers stay in step:**
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]].

**Why the list was wanted at all:** a rule page rendering the shared reading discipline into more
than one agent is step one of the pre-task chain, and it could not be written while the field took
one address ([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The verdict is built, and it did not take a number — 2026-08-22

**The section above says *"Not built"*. That stopped being true on this date** and the sentence is
left standing, because it is a true statement about the day it was written
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**`scripts/vault-check.sh` names the block form**, in the frontmatter pass that already reads
`governs:`: an empty scalar followed by indented `- ` items sets a flag, and the flag is reported
before the `nogoverns` branch is reached. It fires in **any** folder, because the spelling is illegal
wherever it is written.

## It joins the frontmatter verdicts rather than becoming a numbered rule

**A retired rule number is never reused here** ([[a-retired-rule-number-is-never-reused]]), so a
number is a permanent commitment made for one comparison. The existing frontmatter verdicts —
`nogoverns`, `ruleclaim`, `slicenogoverns`, `type`, `decided` — are named and not numbered for the
same reason, and this is one more of them. The corpus already records that a verdict without a
number of its own is the ordinary case rather than an omission
([[the-sources-path-verdict-has-no-rule-number-of-its-own]]).

## What it repairs is the diagnosis, not the colour

**The block form was already red.** The scalar parses to the empty string, so `nogoverns` fired —
and it said *"a rule with no `governs:`"* about a page that names two destinations plainly, in the
lines directly under the field. **Failing loudly with the wrong diagnosis sends the reader to add a
field that is already there**, which is a failure shape this store has met before and has a page for
([[the-hook-was-stricter-than-the-rule-it-enforced]]).

**So the decision above is unchanged and only the message is new.** *Red rather than silent* was the
owner's ruling and it was already satisfied; what was missing was that the red said the wrong thing.

## Proved in the real tree, in both directions

**A rules page was rewritten into the block form** — the new verdict fired with the right diagnosis,
`nogoverns` was absent, and the gate exited 1. **Then `governs:` was stripped from it entirely** —
the old `nogoverns` verdict fired, unchanged. **Then the page was restored byte-identical to
`HEAD`.** A sandbox cannot test this check, which is why the proof is a real tree
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]],
[[a-case-that-passes-before-the-change-tests-nothing]]).

## Its first customer landed the same day

[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]] is the first page in this corpus
to write the inline-list form, naming `.claude/skills/handoff/SKILL.md` and
`.claude/skills/ingest/SKILL.md`. **The half-parsed-list failure this decision refuses is exactly
what it would have met**: one skill rendered, the other reading as drift.
