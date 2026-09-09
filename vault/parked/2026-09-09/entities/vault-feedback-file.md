---
title: "`.superpowers/sdd/vault-feedback.md` — the session-local draft that becomes the feedback section"
type: entity
status: current
authority: feedback-channel
basis: code
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/handoff/SKILL.md", ".claude/skills/vault-ask/SKILL.md"]
tags: [vault, process]
---

# The feedback draft

**Appeared 2026-08-14.** One file, git-ignored, living beside `progress.md` in
`.superpowers/sdd/`, holding lines written *during* a session about what the vault failed to
supply — and, since the same day, what a librarian call cost.

| Property   |                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------- |
| Path       | `.superpowers/sdd/vault-feedback.md`                                                                          |
| Written by | the working session, in the turn the observation is made — [[feedback-is-recorded-in-the-turn-it-is-noticed]] |
| Drained by | `/handoff`, which moves its lines into **section 7** of the journal and re-headers the file empty             |
| Read by    | `/ingest`, which files each line into `log.md` under its own kind                                             |
| Lifetime   | one session. It is not a backlog and is never carried forward                                                 |

**It carries more than misses.** Section 7 takes `- measure:` and `- lint:` lines as well, and
`/ingest` files them under those kinds rather than as misses. The measurement case is not a
convenience: a subagent cannot report its own token cost, so the figure can reach `log.md` by no
other route — [[a-subagent-cannot-report-its-own-cost]].

## Why a file and not memory

A session that keeps an observation in its head to write up at handoff time loses the two things
that make it usable: the question that was asked, and the grep that returned nothing. What arrives
at handoff instead is a mood about the vault. The draft is git-ignored because it is not knowledge
until it has been through an ingest — the journal is the record, `log.md` is the ledger, and this
is neither ([[journal-vault-brief-each-artefact-has-one-owner]]).

**Its failure mode is silence.** Nothing checks that it was drained, and nothing checks that it was
written to; a session that never opens it produces a handoff whose section 7 reads "none" and looks
identical to a session where the vault answered everything. That is the one thing to watch about
this channel.

## A fourth kind of line, decided 2026-08-16

**A harness change is written here the moment it is decided**, as a marked line, and `/ingest` cuts
it out on a section boundary rather than classifying prose for it
([[a-harness-change-is-recorded-when-it-is-decided]]). The handoff gains a `Harness` section, last,
to receive it ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]).

The reason it is captured here rather than detected later is the one this file already exists for,
sharpened: **a classifier detects presence and cannot detect absence**, so a missed rule would be
unbounded and silent. The failure mode named above — nothing checks that the file was written to —
applies to this kind of line exactly as it does to a miss.

## It is no longer the only transit file — 2026-08-17

**The retro writes `.superpowers/sdd/retro.md`, and it is deliberately not this file**
([[the-retro-writes-its-own-transit-file]]). The property that keeps them apart is the one that
makes each work: this file is written **in the turn the observation is made** and is raw; the retro
file is written **at the end** and holds what has been resolved. The retro reads this one as
evidence and does not drain it — draining stays with `/handoff`.

**The row above naming "section 7" is stale in its wording only.** The handoff's sections lost their
numbers on 2026-08-17; the destination is now the section named `Feedback to the librarian`
([[the-handoff-template-maps-onto-the-categories]]).

## Its failure mode was observed, at the worst scale so far

**Six lines sat in this file undrained**, written by the session that produced `aebb308` — a session
that wrote **no journal at all**, so `raw/` holds nothing for it. They were carried into the journal
of 2026-08-17 verbatim and marked as inherited, because attributing them to that date would have
been wrong. This is the silence named above, and it is also the off-by-one the closing ritual
produces by construction ([[the-closing-ritual-produces-what-the-journal-cannot-hold]]).

**Two of those lines used a fourth kind, `process:`, which neither this file's header nor `log.md`
defines.** A vocabulary arrived without being agreed, and the kinds are what `/ingest` files by. It
is recorded rather than resolved: the librarian transfers a line under the kind it was written with,
and whether `process:` joins `miss:`, `lint:` and `measure:` is the owner's call.

## `process:` was adopted, 2026-08-17

**The owner adopted it** as a fourth kind: a finding about the ritual or the harness rather than
about the corpus ([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]). The definition now stands in this file's
own header, and `log.md` carries the librarian's copy in matching words.

**It was not carelessness that it arrived unagreed.** The other three genuinely did not cover the
two lines that used it.

## Its own header was stale, and the sweep that should have caught it could not

**This file said "section 7 of the journal" in its header until 2026-08-17**, months after the
numbers were dropped. The sweep that found the six other copies of the handoff mapping searched for
the literal string `section 7` and **did not reach this one, because the file is git-ignored**.

So the one detector that worked had a blind spot **exactly where the channel for reporting blind
spots lives**. It was found while draining the file, by reading the header — by no check at all.
The row higher up this page names the same staleness and is left standing; this is the reason it
survived a sweep ([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).

## `harness:` became a kind of its own — 2026-08-19

**The mismatch this file was carrying is resolved by the owner**: `.claude/templates/handoff.md`
routed `- harness:` lines to its `Harness` section while this file defined no such kind, so the
routing named a token that could not appear ([[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]]).

**`harness:` is the kind, and the template's sentence stands**
([[harness-is-a-feedback-kind-of-its-own]]). It is a change to the files that instruct an agent —
**decided** this session — and it is not a `process:`, which is a *finding* about the ritual.

**The vocabulary lives in a pair of files and both now carry it.** This one gained the definition on
2026-08-19; `log.md`, the librarian's copy, gained it at the ingest of 2026-08-20, and until then
the two disagreed. **That is a copy the store has already flagged**
([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]), and the durable fix — a
`wiki/rules/` page with a region in each file — **is designed nowhere**
([[no-rule-reads-a-harness-file]]).

**The failure mode named at the top of this page is unchanged and applies to the new kind exactly**:
nothing checks that the file was written to.

# The deletion has an owner from 2026-08-22

**Whichever ritual filed a line is the one that removes it.** `/handoff` drains what it drains and
`/ingest` removes what it files, so the window that used to leave a line both filed and standing is
closed rather than narrowed ([[whoever-filed-a-feedback-line-empties-it]]).

**Until that is built, a line written between a `/handoff` and its `/ingest` is filed into `log.md`
and survives in this file** — five entries stood in exactly that state after 2026-08-21, and the
duplication is visible only when the file is read at the start of the next session
([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

# Its writer changed on 2026-08-24, and no session writes it any more

**The `Written by` row above is false from this date.** The file is written by
`.claude/hooks/catch-the-feedback.ps1` on `MessageDisplay`, which lifts a fenced `VAULT-FEEDBACK`
block out of the assistant's own reply ([[the-feedback-catcher-hook]],
[[the-session-speaks-the-feedback-line-and-a-hook-files-it]]).

| Property | from 2026-08-24 |
|---|---|
| Written by | the catcher hook, out of the reply that spoke the line |
| Drained by | `/handoff` — unchanged, and the hook yields in the turn the file shrinks |
| Kinds | `miss:`, `measure:`, `decision:`, `harness:` — `lint:` and `process:` are the librarian's now ([[lint-and-process-stop-being-session-kinds-and-decision-joins]]) |

**The reason is not convenience.** The rule obliging a session to write it broke eight recorded
times, every one because plan mode forbids a session to write files
([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).

**Its header was rewritten the same day** to declare the four kinds — one of the five hand-kept
copies of that vocabulary, and the file's own header is the copy no tree sweep can see, because it
is git-ignored ([[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]]).

**And it must never be a `governs:` target**, precisely because `/handoff` empties it: a rule
rendering into it would leave the injector reporting a destination with no region, which reddens the
gate and locks the librarian out ([[a-rule-may-not-govern-a-file-the-ritual-empties]]).

# A third transit file joined it — 2026-08-24

`.superpowers/sdd/session-dialogue.md`, beside this file and `retro.md`: git-ignored, one session
long, written by `scripts/session-dialogue.py` at `/retro` step 0
([[the-session-dialogue-extract]]). **It owes the paragraph this page and `retro.md` both carry** —
why it is a third file rather than folded into one of them — and that is named as owed rather than
written.

**The owner said what the new channel is like to use**, which is the first testimony this file has
about being read rather than written:

> **owner: новый формат когда ты пишешь прямо в чате VAULT FEEDBACK, а скрипт уже пишет в
> .superpowers/sdd/vault-feedback.md - мне очень нравится. Стало удобно, я вижу детали.**
