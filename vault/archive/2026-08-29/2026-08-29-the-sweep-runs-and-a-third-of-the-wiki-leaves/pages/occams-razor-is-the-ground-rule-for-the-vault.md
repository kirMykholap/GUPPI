---
title: "Occam's razor is the ground rule of this store: no new entity where an existing one can carry the claim"
type: decision
status: archived
authority: entity-admission
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
sources: ["scripts/vault-authority.sh", "scripts/vault-check.sh", "CLAUDE.md"]
tags: [vault, process, architecture]
binding: prohibition
---

# Decided 2026-08-21, after the owner was shown what the store had become

- **479 pages and 2.9 MB under `wiki/` in nine days**, every one `status: current` and not a single
  one `deprecated`. By folder: 189 `decisions/`, 121 `lessons/`, 102 `concepts/`, 33 `entities/`,
  24 `proposals/`, 10 `rules/`. Created per day since 2026-08-13: 80, 16, 19, 23, 110, 49, 43, 124,
  15 — a curve that is not settling.
- **`archive/` holds 27 pages and 216 KB.** Retirement has fired 27 times against 479 live pages,
  and every one of those firings was a direct replacement.
- **`/ingest` has no valve on its intake.** A unit of knowledge becomes a page by default. The only
  clamp that exists is retire-on-direct-replacement, which cannot fire on a page that is merely
  adjacent to one already written — and adjacency is what 479 pages in nine days is made of.

> «Бритва Оккама. Не плодим сущности… Иначе наша сессия превращается в бесконечную гонку с собой,
> правки и правки правок, потому что появилась новая правка. Это должно стать основой всего. Наша
> задача строить, а не «прикручивать».»

**That is the ruling and it is the ground of the three decisions taken with it**
([[authority-becomes-the-index-and-is-required-outside-rules]],
[[a-decision-declares-whether-it-binds]]). It is stated here as a decision so that it can be cited;
the text a librarian is actually held to is
[[no-new-entity-where-an-existing-one-can-carry-the-claim]], which is where the imperative lives
and which the harness renders.

# The claim, stated as the constraint it is

**A new entity earns its place only when no existing one can carry the claim.** Correcting,
extending or superseding an existing page is the first repair to reach for; writing a new page is
what is left when that repair does not exist. Lifting this is a conversation with the owner and
never a session's call, which is what `binding: prohibition` on this page says.

**The rule is decided by a lookup, not by an impression**, which is the whole reason
[[authority-becomes-the-index-and-is-required-outside-rules]] was taken in the same breath: a rule
you cannot look anything up for is an exhortation. `bash scripts/vault-authority.sh --near <slug>`
is that lookup and it is what the librarian owes before it writes.

# Rejected: leave the intake open and clean up periodically

This was argued, and it is the alternative anyone reaches for first — let the corpus grow, and
schedule a prune.

**It was refused on two grounds.** A periodic clean-up is a one-off against a standing cause: the
cause is that `/ingest` admits by default, and a sweep that does not change the admission rule
buys one tidy corpus and pays again at the next ingest, forever. That is the same argument
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]] already makes about a stale copy,
applied to a stale *store*.

**And in this project nothing may be deleted.** A clean-up therefore moves pages to `archive/`; it
shrinks what is *read* and never what is *stored*, so the disk and the git history keep every page
while the reader's index gets shorter. The clamp has to sit at the moment of writing or it is not a
clamp on the corpus at all.

**Rejected alongside it: raising the retirement rate instead.** Retirement answers "this claim was
replaced". Most of the 479 are not replacements of each other, they are neighbours, and no
supersession relation is true of them.

# The danger the owner named and accepted: a visible failure becomes an invisible one

This is the cost of the rule and it is stated here rather than discovered later.

**Two `current` pages sharing an `authority` are a contradiction the gate finds mechanically** —
rule 3 of `vault-check.sh`, every run, no judgement involved. **A wrong merge looks like a healthy
page.** A claim folded into a page it does not belong on leaves one page, one slug, one green
check, and a reader who will never learn that the two things were ever separate. The rule converts
a failure the store can see into one it cannot.

**It was accepted knowingly, and against the store's own root principle** —
[[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]] — so the compensation has to be built
rather than assumed. It is a trail, in two halves, and both are obligatory:

- **the lookup is written down.** Every merge, and every page written despite a family being
  returned, says in `log.md` what `--near` returned and why a new page was still right. That is the
  only record that the judgement was made at all;
- **the addition is dated in the page itself.** An extended page names the day the material was
  added and the journal it came from, so a reader can see where one page stops and the graft
  begins.

Neither restores a mechanical detector. They make the wrong merge *reviewable*, which is the
weaker property the owner took in exchange for a corpus that stops racing itself.

# The editing boundary, which is what keeps this rule from eating fidelity

The rule says "extend the existing page". Left unbounded that is a licence to rewrite the corpus,
and this store has an instrument that a rewrite would silently break.

**Allowed: appending to a page, reordering it, and marking a sentence false.** Marking is the
operation — the sentence stays, dated, with what replaced it beside it.

**Never: rewriting a sentence a source asserted.** `raw/` is immutable and the coverage sidecar is
keyed by the source's line number, so a rewritten sentence leaves a verdict pointing at text that
is gone. The sidecar keeps reporting the unit as compiled, against a page that no longer says what
the line said, and nothing in the fidelity sample can see the substitution
([[fidelity-to-a-source-and-fidelity-to-the-tree]]). Fidelity to the source is the one axis this
store actually checks; the merge rule may not be paid for out of it.

# What it does not touch

**It is not a size threshold and it does not replace one.** The brief's own size is still the
growth alarm for a sprint ([[the-growth-signal-is-the-brief]]) — that instrument measures what the
next session has to read, this rule governs what is admitted, and they answer different questions.

**It is not an argument for writing less down.** A unit of knowledge that reaches no page is lost,
and the handoff's coverage verdict still owes an account of every one. What changed is where the
unit lands: on the page that already owns the question, wherever such a page exists.

# The first live use caught a real duplicate, against the session's own inclination — 2026-08-21

**Superseding `governs-becomes-a-property-of-any-page` needed a slug, and the session was about to
mint one.** `bash scripts/vault-authority.sh --near governs-scope` answered *"that question has a
page, do not write a second"* and pointed at the page being overturned. **The slug was inherited by
the successor** ([[governs-is-a-property-of-wiki-rules-alone]]).

**A new slug beside the old one would have left `governs-scope` grouped in the register and carried
by no live page** — the stale half `--check` exists to catch, in the direction where a lookup
returns a family whose answer no longer exists.

**Worth recording because the rule disagreed with the writer and won.** The lookup is cheap, it was
run because the rule says to run it, and what it returned was not what the session expected.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
