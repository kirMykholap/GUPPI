---
title: "One page written into `wiki/` reaches the register deadlock, and no sweep is needed for it"
type: lesson
status: current
authority: single-page-register-deadlock
basis: code
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-authority.sh", ".claude/hooks/lock-the-librarian.ps1"]
tags: [vault, harness, agents]
---

# The incident, 2026-08-30

**A session wrote one page into `wiki/decisions/` and the gate went red twice on the same act.**

- **as an orphan** — nothing linked to it yet. Closed by the next edit.
- **as a slug outside `authority.md`** — rule 13 compares the register against the tree in both
  directions, and a page carrying an unregistered `authority:` reddens it.

**The second closes a circle.** `authority.md` is a register, and the one-writer clause names the
librarian as its only writer ([[authority-md-is-a-register-the-one-writer-clause-names]]).
`.claude/hooks/lock-the-librarian.ps1` refuses to dispatch the librarian while `vault-check.sh` exits
non-zero. **So the only party permitted to write the row cannot be called because of the row.**

**It was cleared by the owner permitting the session to write that one line**
([[the-session-writes-one-authority-row-and-the-one-writer-clause-stands]]) — a permission, not a
mechanism.

# Why this is not the deadlock already on the record

**[[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]] records the same
lock and every number in it is a sweep number**: 239 pages moved, 239 rows left pointing at pages that
had left `wiki/`, `--check` red on all of them. The repair it carried is that an archived page keeps
its slug and its row — which fixes the **departure** direction and does nothing for the **arrival**
one.

**A page arriving reddens the register in the other direction, and one page is enough.** There is no
threshold, no sweep, and no warning: writing a single new page into `wiki/` with a slug not yet in
`authority.md` locks the librarian out until somebody who is not the librarian writes the row.

# What follows

**Whoever writes a page into `wiki/` writes its `authority.md` row in the same pass**, or the gate is
red between the two acts and the party permitted to close it cannot be reached. That is the librarian
in the ordinary case, and it is why an ingest never leaves a slug unregistered.

**And it is why the 53 family rules and their 53 rows must land together** — the same lock at
fifty-three times this size, with an exception granted for one line and not for fifty-three
([[the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages]]).

**The general shape is already stated and had no instance this small**: a gate that forbids the act
which clears it is a deadlock ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]],
[[a-gate-that-refuses-work-without-an-open-sprint]]).

# A third face of the same lock: both write orders are red — 2026-08-31

**The sections above are about the register. This one is about `index.md`, and it is worse, because
neither order is legal.**

**Writing the rule pages first leaves them orphaned.** Rules 4 and 5 build the linked set from `wiki/`,
`archive/`, `index.md`, `tags.md` and `sprint.md`, and nothing in the tree points at a page served by
lookup — it renders into no file and no other page cites it on the day it is created. The session ran
`scripts/build-family-rules.py` itself and got **18 orphans and a red gate**.

**Writing the `index.md` lines first leaves broken wikilinks** — 19 of them, pointing at pages that do
not exist yet.

**And a red gate locks the librarian out through `.claude/hooks/lock-the-librarian.ps1`, while the
librarian is the only party who may write `index.md`.** So the party who could clear either failure
cannot be dispatched once either has happened.

**The only legal container is one dispatch.** The generator has to run **inside** the librarian's, so
both writes land before the gate is consulted
([[the-family-rules-are-drafted-by-a-generator-inside-the-librarians-dispatch]]). The session reverted
and re-ran it that way.

**This is a property of the mechanism rather than a mistake of judgement**, which is why it is written
here and not filed as a divergence. Nothing in the store said it before the day it happened.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
