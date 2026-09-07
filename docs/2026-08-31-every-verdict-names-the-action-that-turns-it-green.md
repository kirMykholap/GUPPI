# Every verdict names the action that turns it green, and the lock reads more than an exit code

**Draft proposal, prepared by the lessons agent on 2026-08-31 from `wiki/lessons/` as it stands.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

**This proposes a change to `.claude/hooks/lock-the-librarian.ps1`**, which is a file that governs
what an agent may be dispatched to do. That is named here rather than left as a consequence.

**The group, in one sentence:** three live lessons are three shapes of an instrument whose output
no party can act on, and all three end at the same place — a red gate that
`lock-the-librarian.ps1` reads as a refusal to dispatch the only writer permitted to clear it.

## The group

- `a-verdict-that-cannot-be-cleared-survived-a-third-full-design-pass` — rule 17 would have
  reddened every `repeal` decision for good: it lives forever, its target exists by definition, and
  it can never be named back. **Third instance, all three caught at the plan check and nowhere
  earlier.** Its own sentence for the class: *for every page this verdict ranges over, name the
  action that turns it green.*
- `one-page-written-into-the-wiki-reaches-the-register-deadlock` — one page with an unregistered
  `authority:` reddens rule 13; the lock refuses the librarian; the librarian is the only writer of
  `authority.md`. Cleared by the owner granting a permission, not by a mechanism.
- `an-advisory-carrying-a-debt-count-does-not-get-paid-down` — `9 of 15`, then `9 of 17`, across
  weeks with the numerator never moving. Correct, read, and it changed nothing.

**Two of the three are already the same event at different scales**, and the store says so: the
sweep of 2026-08-29 left 239 stale rows and deadlocked on all of them, and
`the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages` records the same lock at
fifty-three times the single-page size.

**The third is the opposite failure of the same omission.** A permanently red verdict and a debt
nobody pays are both instruments whose output no action discharges; one stops the store and one is
ignored.

## What it would be

**Two clauses.**

1. **A verdict is not written until somebody names, for every class of page it ranges over, the
   action that turns it green.** One sentence at design time. It is what `/pre-task` does today,
   three times, late — and nothing earlier asks the question at all, which that page names as the
   gap rather than proposing a fix for it.
2. **`lock-the-librarian.ps1` stops reading a bare non-zero exit as a refusal.** The lock exists so
   the librarian does not write onto a broken tree. It cannot distinguish *the tree is broken* from
   *the tree is broken in exactly the way only the librarian can repair*, and the second is the
   deadlock. A verdict class the librarian is the sole remedy for — rule 13's register rows are the
   worked example — should not close the lock.

## What it would take

- **`.claude/hooks/lock-the-librarian.ps1`** — the lock reads which verdicts fired rather than the
  exit code alone. `scripts/vault-check.sh` already distinguishes exit 1 from exit 2
  (`a-non-zero-exit-from-the-gate-no-longer-names-one-event`, archived), so the channel for saying
  *which* exists.
- **A list of librarian-only verdicts**, which is a drifting list and this store repairs one of
  those by deleting it. The alternative is a per-verdict mark in `vault-check.sh` beside the
  verdict itself, which does not drift because it lives where the verdict is written.
- **One `wiki/decisions/` page** for clause 1, and its instrument or a page saying why it cannot
  have one.

## What is open

- **Whether clause 2 weakens the lock into uselessness.** The lock's whole value is that it fires
  without judgement. A lock with an exception list is a lock somebody argues with, and the owner's
  standing position is that a simple rule beats a measured exemption. **The honest alternative is
  the opposite move**: keep the lock absolute and make the deadlocked act impossible, by requiring
  the page and its register row in one pass — which is already decided
  (`the-authority-rows-are-written-in-the-same-pass-as-the-rule-pages`) and which this draft may be
  proposing to duplicate.
- **Whether clause 1 has any instrument.** Three instances, one detector, and the detector runs
  late. Nothing before the plan check reads a proposed verdict against the population it ranges
  over, and this draft does not know how to build that.
- **The `index.md` direction, which is not on any page.** The journal of 2026-08-31 reports that
  both orders of the family-rule act redden the gate: the pages first leave orphans, the `index.md`
  lines first leave broken wikilinks. `index.md` is a register only the librarian writes, so that
  is a third face of the same lock and the store carries only the `authority.md` one.
- **Whether the debt half belongs in this group at all.** An advisory nobody pays and a verdict
  nobody can clear share a diagnosis and have opposite repairs: the first needs a party who owes
  the number, the second needs the verdict withdrawn or scoped.

## What it would oblige

- **A dated reading of how many live verdicts have an unclearable class.** The population is
  `scripts/vault-check.sh`'s verdict list, and nobody has walked it against clause 1.
- **The lock's behaviour becomes testable.** `scripts/vault-check-selftest.sh` is a mutation test
  of the gate; the lock is downstream of it and has no case at all.

## What it would retire

- `a-verdict-that-cannot-be-cleared-survived-a-third-full-design-pass`, on clause 1.
- `one-page-written-into-the-wiki-reaches-the-register-deadlock`, **only if clause 2 lands**. If
  the answer is instead the already-decided one-pass rule, the page stays live: it is the carrier of
  why that rule exists, it is cited three times from outside `lessons/`, and it should take the
  `index.md` direction as an extension rather than leaving.
- **Not** `an-advisory-carrying-a-debt-count-does-not-get-paid-down`. It is the store's own
  evidence against building counters, it is cited by nothing anywhere, and retiring the page that
  argues against instruments-that-nobody-acts-on into an archive nothing reads would be the claim
  proving itself.
