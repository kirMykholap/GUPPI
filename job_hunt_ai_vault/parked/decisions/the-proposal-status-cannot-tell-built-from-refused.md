---
title: "A proposal's status cannot say whether it was built or refused, and that defect stands for now"
type: decision
status: current
authority: proposal-status-defect
binding: deferral
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [vault, process]
---

# Decided 2026-08-16: recorded, not fixed

**`proposals/` is left exactly as it stands, with a mark to revisit.** The defect below is
recorded rather than repaired, which is a decision with a date and a rejected alternative — *fix it
now* — and not an omission.

## The defect

**There are two statuses and a proposal has three states.** `current` while it stands is one; but
`deprecated` has to carry both *built* and *refused*, and `superseded_by:` names a successor page
in either case without saying which happened.

That is **the question the category was created to answer**. [[proposals-are-a-folder-not-a-status]]
argues that the page's own frontmatter should answer *what became of it*, and it does not: a reader
asking "what did we plan and never do" gets the `current` set correctly, and a reader asking "what
did we plan and then refuse" cannot be answered at all without opening the successor.

## Why it stands

**`status` staying two-valued is the load-bearing half of that decision** — a third value would be
a second vocabulary to keep in step with the first, and the folder is what makes an intention
unmistakable for a record of something built. Changing it is a change to the schema, and the
schema's rulebook is not the librarian's to write ([[the-librarian-writes-unattended]]).

It is a row of [[what-the-harness-build-waits-on]], and it is the kind of gap
[[a-schema-per-type-says-what-a-record-asserts]] was written to close — that proposal's own list of
open questions does not yet include this one.

# The defect has an answer for the built case, and is still unrepaired — 2026-08-22

**The owner ruled that a built proposal stays in `wiki/proposals/` with a `built` mark rather than
retiring to `archive/`** ([[a-built-proposal-stays-in-proposals-with-a-built-mark]]). That is this
page's defect answered in its direction rather than deferred again: *two statuses cannot carry three
states* was the finding, and one of the three now has a name of its own.

**This page's claim is still true on the tree.** The mark does not exist —
`wiki/proposals/_schema.yaml` does not know it, rule 2 of `bash scripts/vault-check.sh` does not
admit it — so `status` still cannot tell built from refused, and *recorded rather than repaired* is
still what describes the state.

**What changed is that the direction is no longer open**, and what remains open is the shape:
whether the mark is a third `status` value or a field of its own, deferred by him to the next session
in his own words. **The rejected alternative on this page — *fix it now* — was taken by somebody
else, later.**

# The shape is decided and the direction reversed — 2026-08-23

**The paragraph above is false from this date in two of its clauses**
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

- **The shape is no longer open.** The mark is a **third `status` value**, not a field of its own
  ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).
- **The direction reversed the day after it was fixed.** An implemented proposal moves to
  `archive/` after all, on his ruling that the archive is history rather than a verdict
  ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

**This page's own finding — two statuses cannot carry three states — is answered rather than
deferred again.** The three are `current`, `built` and `implemented`. **Only `implemented` lands
now**: `built` means the design is complete and the task list is written, and its test needs
`wiki/tasks/`, which is deferred to S4 ([[the-folder-set-is-closed-and-tasks-is-not-in-it]]).

**So the defect this page records is half repaired and half standing.** *Built* and *refused* are
still not distinguishable on a proposal that is standing in the folder; *implemented* is, and it is
distinguishable by being gone.

# The refused half is ruled too, and the defect this page records is answered in both directions — 2026-08-23, later the same day

**The section above says *built* and *refused* are still not distinguishable on a standing
proposal.** The owner ruled the refused case hours later: a refused proposal moves to `archive/`
and takes `status: refused`, and what has gone to the archive stays there
([[a-refused-proposal-is-archived-and-takes-status-refused]]).

**So the finding — two statuses cannot carry three states — has a full answer**: `current`, `built`,
`implemented`, `refused`. **Two of the four are minted and two are not.** `built` waits on
`wiki/tasks/` and S4; `refused` waits on a schema change and is refused by the gate meanwhile.

**This page stays `current` and is not retired**, because its subject is the defect and half of the
defect is still on the tree: a proposal standing in the folder still cannot say whether it was
built. It is dated rather than edited
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).
