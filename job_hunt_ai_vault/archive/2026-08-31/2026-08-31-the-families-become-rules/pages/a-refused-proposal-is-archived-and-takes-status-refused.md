---
title: "A refused proposal moves to `archive/` and takes `status: refused`, and the value is not minted"
type: decision
status: archived
authority: refused-proposal-disposition
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-23
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "job_hunt_ai_vault/CLAUDE.md", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, process, record-schema]
---

# The ruling, 2026-08-23

> **owner: отклоненный proposal - уходит в архив и получает status "refused". То, что уехало в
> архив пусть там и лежит.**

**Two clauses, and the second is the one that is easy to read past.** A refused proposal leaves
`wiki/` for `archive/` and carries `refused`; and **what has gone to the archive stays there** — no
page comes back because the question was reopened. That second clause is the same statement about
what `archive/` is that he gave for the implemented case on the same day
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]): the archive is
history, not a queue.

**It is one of three dispositions of a proposal now**, and they are not variations of one rule:

| what became of it | the mark | where it lives |
|---|---|---|
| it still stands | `current` | `wiki/proposals/` |
| it was implemented | `implemented` | `archive/`, with a live page citing it |
| it was refused | `refused` | `archive/` |

# The value is not minted, and the gate refuses the word

**The schemas know `current`, `deprecated` and `implemented`.** `refused` is in none of them, so a
page carrying it is red on rule 2 — a value outside its schema's list
([[a-value-outside-the-schemas-list-is-red]],
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**That is the state of the tree and not a disagreement with the ruling.** Minting the value is a
change to `wiki/proposals/_schema.yaml`, which is the session's file rather than the librarian's
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]), and the same change has to
answer the question the `status:` block already answers once: a value legal in one folder and
absent from the other five is the shape that decision already chose.

**So until it is minted, a refusal is recorded the old way** — `deprecated` with `superseded_by:`
naming the page that asserts the claim the other way — and nothing here licenses writing the word
into a page.

# What is not decided here, and one clause of it was struck rather than restated

**Whether a refused proposal also carries `superseded_by:`.** His sentence does not say. The clause
this ruling replaced in the vault's own `CLAUDE.md` said it did, on the ground that a refusal
**has** a successor asserting the same claim the other way — which is exactly the argument that
makes an implemented proposal *not* a supersession. **That ground was neither restated nor struck
by him**, so it is carried here as an open question rather than resolved in either direction.

**Whether the safety condition applies.** `scripts/vault-archive.sh` refuses to move a page under
`kind = pages` while no live `wiki/` page names its slug ([[vault-archive-sh]]). Nothing in his
words exempts a refusal, and the script does not read `status:` at all, so the precondition binds a
refused proposal today by construction. **A refusal usually has such a page** — the decision that
refused it — so this is expected to be satisfied rather than to bite.

**Whether the proposals already retired under earlier rules come back.** They do not, on the second
clause of his sentence, and that is the one thing this page settles which the implemented ruling
left open.

# Its own history is why this page exists at all

**The defect this answers is five days old**: `status` had two values and a proposal had three
states, so `deprecated` had to carry both *built* and *refused* and said which neither time
([[the-proposal-status-cannot-tell-built-from-refused]]). That page recorded the defect and
deferred the repair; the built half was answered on 2026-08-22 and reversed on 2026-08-23, and this
is the refused half.

# Decided later on 2026-08-23: a refused proposal carries no `superseded_by:`

**The first open question above is answered, and the paragraph raising it is left standing.** A
refused proposal takes `status: refused` and `decided_by:` naming the decision that refused it, and
it carries **no** `superseded_by:`. The owner took this by approving a plan he read in Russian,
later on the same 2026-08-23 — a decision and not an utterance, so the ruling is his and the wording
of this section is the session's, unquoted and unsigned
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]],
[[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]).

**The ground disposes of the argument that was carried here rather than merely outvoting it.** A
refusal is a **cause**, and `decided_by:` is the field for a cause
([[decided-by-is-a-field-of-its-own-and-not-a-line-in-sources]],
[[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]). `superseded_by:` is a
relation between two pages **asserting the same thing differently** — one claim replaced by another
claim. The decision that refuses a proposal does not assert the proposal's claim the other way; it
asserts that we are not doing it, which is a different sentence about a different subject. So the
carried ground — that a refusal has a successor asserting the same claim the other way — is the one
this ruling rejects.

**It lands the refused case where the implemented case already stood**, and for a reason of the same
shape: an implemented proposal carries neither `deprecated` nor `superseded_by:`, because the live
page recording what was built asserts something else rather than the same thing differently
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). Two of the three
dispositions now decline the relation, and `deprecated` keeps it — a page replaced for going false is
the case supersession was made for.

**What is still not decided here.** `refused` is still not minted, so nothing may carry the word yet,
and the section above stands unchanged on that. Neither is the safety condition:
`scripts/vault-archive.sh` still refuses the move while no live `wiki/` page names the slug, and it
reads no `status:` at all ([[vault-archive-sh]]). Neither is `decided_by:` itself, which no
`_schema.yaml` declares.

# The value is minted, the field is required conditionally, and `decisions/` is not admitted to it — 2026-08-23, later the same day

**Everything the two sections above name as unbuilt is now built.** Read off the tree at the ingest
of this journal:

| what stood open | where it stands now |
|---|---|
| `refused` is not minted | declared in `wiki/proposals/_schema.yaml`, and red in every other folder |
| `decided_by:` is declared by no schema | declared in `wiki/proposals/` and `wiki/rules/` |
| nothing enforces `decided_by:` on a refusal | `scripts/vault-archive.sh` refuses the move with exit 2 |

**The requirement is conditional and no per-folder schema can state a conditional**, which is why it
lives in the script that moves the page rather than in the gate
([[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]], [[vault-archive-sh]]).

**owner selected: a refused proposal carries `decided_by:` and no `superseded_by:`** — a menu
choice, taken against his own first design, which was `superseded_by:` naming the refusing decision.
The label is his selection and the wording of this section is the session's; none of it is signed as
his own words
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**Two grounds were put to him and he took them**, and they are the same two the section above
carries: a per-folder schema states one required set for a whole folder and cannot express *required
when the status is X*; and `superseded_by:` is written in both directions on purpose, so a proposal
pointing at a decision would need that decision to claim it supersedes a proposal — which asserts a
different claim.

## `refused` is not admitted to `decisions/`, and that is a separate ruling

**A decision is not refused, it is overturned.** `deprecated` plus `superseded_by:` already records
that, and it records it correctly: the successor asserts the same claim the other way, which is
exactly the relation supersession is for.

**So the value stays legal in `wiki/proposals/` alone**, which is the same shape `implemented` has
and for the same reason: a maturity word loose in the other five folders would mean something
nobody decided ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**What nothing checks is that `decided_by:` names the *right* decision**, and therefore that the
decision was written before the page was released. The script tests presence, the gate tests the
target's type and only while the page is still live, and the order between them is a discipline
rather than a mechanism
([[the-order-of-a-refusal-and-its-archive-move-rests-on-a-written-rule-and-not-on-a-gate]]).
