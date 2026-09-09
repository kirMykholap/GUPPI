---
title: "The repository's `CLAUDE.md` may point and may not assert"
type: proposal
status: current
authority: claude-md-assertion-ban
basis: human
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "scripts/vault-check.sh", "CLAUDE.md"]
decided_by: [[structure-work-agreed-and-not-executed]]
tags: [vault, process]
---

# The mechanism, proposed 2026-08-16 and not taken

**The rule would be one sentence: that file may point at things, and may not assert them.** A
pointer is checkable — the page, the skill or the agent it names either exists or does not. An
assertion is not, and every staleness this project has recorded in a `CLAUDE.md` has been an
assertion ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**Nothing here is decided**, and one half of it has already been declined — see below.

## The three facts from the code it rests on

1. **Rule 5b already validates every `[[wikilink]]` in the repository's `CLAUDE.md`**, and it has a
   selftest case ([[vault-scripts]]).
2. **`claude-md-scope` removed every wikilink from that file**, so the check currently guards
   nothing ([[claude-md-is-a-map-and-four-rules]]).
3. **Those links deliberately do not count towards reachability**, so nothing can hang off
   `CLAUDE.md` alone and a deleted paragraph can never strand a page.

What a cut can lose is an assertion no page carries — which is what all the observed staleness has
been, and what acceptance criterion 4 of S1 asks for a mechanism against.

## The checkable approximation

**Every normative paragraph carries at least one link into the vault.** A paragraph that tells the
reader to do or not do something, and names nothing checkable, is the finding. It is an
approximation and not a proof: a paragraph can carry a link and still assert something no page
holds. It is cheap, mechanical, and it fires exactly where the four recorded instances were.

## The owner declined the wikilink half

**He wants that file pointing at skills and agents instead**
([[the-repository-claude-md-becomes-a-dispatch-table]]), and his ground is the same one this
proposal rests on: **a named skill is checkable the same way a named page is** — it exists in
`.claude/skills/` or it does not.

So the proposal survives with its target changed: *every normative paragraph names something
checkable*, where the checkable thing is a skill, an agent or a page. What does not survive is
re-admitting wikilinks to satisfy rule 5b as written; a new check would have to validate the other
two kinds of pointer, and that check does not exist.

## What it would oblige

- A rule in `vault-check.sh` reading a file that is not a wiki page — the first of its kind, and
  the reason none of this is automatic today.
- A decision about what "normative" means mechanically. The honest fallback is that the rule is a
  `/vault-lint` item read by a librarian rather than a shell condition, which is where the other
  semantic checks already are ([[reconciling-entities-against-the-decision-register]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).
