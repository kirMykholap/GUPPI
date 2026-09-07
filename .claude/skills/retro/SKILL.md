---
name: retro
description: Interrogate the session and resolve every open question with the owner, then write the retro file that /handoff routes. Run at the end of a session, before /handoff. Use when a session is ending, when work is being wrapped up, or when asked to review how the session went.
---

# Retro

**The end of a session is a retrospective, and `/handoff` follows it.** The sprint-level ritual is
called a *sprint retrospective* and is a different thing; this skill is not it.

The two steps do different work and the split is the point. **This one interrogates: it finds what
the session would not volunteer. `/handoff` routes: it files what this one found.** If a thing can
still be argued about, it belongs here; if it can only be sorted, it belongs there.

**Conduct the conversation in the owner's language** — Russian. Everything written to a file stays
English: the retro document, the journal, commits, the vault.

<!-- rule: every-turn-of-a-retro-files-a-feedback-block -->
**Every turn of this retro files a `VAULT-FEEDBACK` block.** Mandatory, on the owner's ruling — not
once at the end, and not folded into the retro file: in the turn the thing happens.

**The two artefacts hold different things.** `.superpowers/sdd/retro.md` holds what was **resolved**;
the block holds what was **observed**, in the turn it was observed. A retro writes an artefact of its
own, which is exactly why the recording feels already done here and is not.

**A turn that genuinely produced nothing recordable says so in one line**, rather than filing nothing
silently.

<!-- /rule: every-turn-of-a-retro-files-a-feedback-block -->

## 0. Extract the session, before reading anything from memory

```bash
uv run python scripts/session-dialogue.py
```

It writes `.superpowers/sdd/session-dialogue.md` — the owner's turns, the session's replies, every
`AskUserQuestion` **with its answer**, and every `VAULT-FEEDBACK` block the session filed. Read that
file. It costs 15-30k tokens; a whole transcript is fifty times that and is mostly tool output.

**Why this step is first.** Two of the four sources below are memory, and by the end of a long
session memory is a compaction of itself. The harness has written a complete record of every session
since the beginning — 37 files and 255 MB on 2026-08-24 — and nothing in this repository had ever
read one.

**It also reaches what no hook can.** A ruling made by choosing among options is a tool result, not
a submitted prompt: in one measured session **eight of ten rulings arrived that way**, and they are
in the extract with the option label the owner took and the free text where he wrote his own.

**What it cannot give you.** `thinking` blocks are stored with empty content. The extract holds what
was **said**, never what was reasoned, so a fork resolved silently is visible only where it reached
the words. **Do not read the absence of a question as its absence from the session.**

If the script refuses — and it refuses loudly, with counts — say so in the first line of the retro
and work from memory, naming that you are.

## 1. Build the list of open questions

Not optional, and not conditional on the session feeling tidy. **A session cannot judge that it has
no open questions**, because not seeing them is the failure itself. **Reading the extract does not
discharge this step**; it supplies its evidence.

Read for them in five places, in this order:

- **the extract from step 0** — and put these four questions to the text rather than to your memory
  of it, because they name what a session walks past. Measured from what actually went missing:
  **where the owner overrode what the session proposed** (seven times in one session, and no kind
  carried them); **a fork the session resolved without asking**, with the option it dropped; **a
  fact established by probing** that would cost the same to establish again; and **the session's own
  errors, corrected mid-flight**;
- **the session's own course** — forks resolved without asking, decisions taken quietly, scope
  narrowed on the way past;
- **what the owner raised and the session stepped over.** These are the expensive ones: the owner
  already spent the attention, and the session spent it for nothing;
- **`.superpowers/sdd/vault-feedback.md`** — read it as evidence of what happened. **Do not drain
  it. `/handoff` drains it**, and a file emptied twice loses whatever landed between the two;
- **the brief's alarms**, if any are still open. An alarm carried into a second session is an
  answer nobody gave.

Show the list. One line per question, and say how many. **Say how many came from the extract and how
many you found by reading** — the difference is the only measurement this channel will ever have of
what the marks miss.

## 2. Ask the owner how to work it

Use `AskUserQuestion`:

- **grill-me** — and in which direction: the agent asks, the owner asks, or both take turns. The
  `grill-me` skill is the interview engine; this skill is the ledger it writes into.
- **the agent works the list and brings conclusions** — cheaper on the owner's attention, and
  weaker: a fork resolved by the party that created it is not reviewed.
- **no conversation this session.**

**Choosing the third is a resolution, not a skip.** The owner has deferred every open line, which
is an answer; write it down as the verdict on each. Silence is what this step exists to prevent,
and an owner's stated "later" is not silence.

## 3. Work the list

New questions surface during a retro and they are **appended, never dropped**. A question raised
while answering another is the most likely thing to be lost, because both parties are mid-thought.

Where a question can be answered by reading the repository or asking the vault, **do that instead of
asking the owner**. Their attention is the scarce input here.

## 4. The gate

**No line leaves without a verdict.** Exactly three are legal:

| verdict | meaning |
|---|---|
| `answered:` | resolved, with the answer |
| `deferred:` | put off **and written down where it can be picked up** — a sprint entry, a vault page, a harness line. A deferral naming no destination is not a deferral |
| `could-not-close:` | it could not even be put to the owner, and why |

Before proposing to end, **restate the count in one line** — "N questions: a answered, b deferred,
c could not close". Then ask whether to end or continue; the owner may hold questions this skill
never saw.

`could-not-close:` is a real answer and using it is not a failure. Hiding behind "all resolved"
while one line was quietly dropped is the failure — a report that detects only presence cannot
detect absence, which is the shape this whole step exists to remove.

## 5. Ratify every decision about to be attributed to him

**List every DECISION this session is about to attribute to the owner, and put the list to him
before the retro file is written.** Typically five to fifteen. He answers each with yes, no, or a
correction.

**Build the list from the `decision:` marks in the extract, not from memory.** Each mark already
names which of the three shapes below it is, because it was written in the turn the decision was
taken — and the owner saw it in the chat then and could correct the attribution on the spot. **The
step is not weakened by that; it stops being the first time he sees the wording.** Add anything the
marks missed, and say how many you added: that number is what the attention channel failed to catch.

**A list padded from the extract is worse than a short one.** The marks record what the session
judged to be a decision at the time; a remark that settled nothing is not promoted here just because
it was marked.

**Decisions, not utterances** — his ruling, 2026-08-22. A remark that settles nothing is not
ratified and does not enter the journal as his. The step said *every line you are about to
attribute* until that date, and the session that ran it dutifully brought him
*«что сегодня делаем?»* — a session-opening question — for signature, beside seven real rulings.
A list padded with nothing is a list read less carefully.

Three shapes, and the two that look alike are the whole point:

| shape | how it is written afterwards |
|---|---|
| **he said it** | verbatim, in Russian, under `**owner:**` — his alphabet, his words, no tidying |
| **he selected it** | the option label **verbatim** under `**owner selected:**`, plus what it was chosen *against* where that changes the meaning |
| **you understood it** | in your own voice — *"the session read this as…"* — and **never signed `owner:`** |

**The middle shape was split out of the last one on 2026-08-22, and the reason is a property, not a
courtesy.** A choice made through `AskUserQuestion` does not have the defect that produced the
struck rule. That defect was never that the words were English or that the session wrote them — it
was that **nothing ever showed him the wording**. An option label was on his screen when he chose
it, so there is no interpretation step and nothing that can drift: the record quotes what he was
shown and took. Filing it as *you understood it* is over-correction, and it costs the record the
one thing worth knowing — that he ruled.

**Its own defect is different and must be written with it: the alternatives were the session's.**
He can only choose among what was offered, so a bare *"he ruled X"* hides that no alternative to X
may have been on offer. Naming what it was chosen *against* is what makes the framing auditable —
and the framing does fail: on the day this shape was ratified he selected three options at once,
because the set did not contain what he meant.

**A session whose every ruling arrived through a menu is a session the owner did not frame**, and
that is worth a line in the retro rather than a silent good mark.

**Why this step exists, measured 2026-08-21.** `wiki/decisions/advisory-is-the-default-for-a-hook.md`
carried a quote block attributed to the owner, stamped `basis: human`, stating a rule he had never
given: *"a hook may refuse an operation only where the action is irreversible and the refusal cannot
be wrong."* It was a session's English paraphrase, written into a journal under `**owner:**`,
compiled by the librarian into a quote, and reasoned from as his word for three days. It decided
three things and was one turn away from deciding a fourth. Struck on his ruling: «не было такого
правила. Это правило неправильное.»

The same sweep found **53 owner-attributed quote blocks across 44 `wiki/` pages, 28 of them in
English** — none of them his words, and no mechanism had ever asked whether any was faithful.

**The gate cannot do this and neither can a grep.** A check separates a quote from a paraphrase by
its alphabet; only the owner separates a *faithful* paraphrase from a wrong one. That is why the
step is here, in the one ritual where he is already in the conversation, and not in a script.

**It runs before the retro file, not after.** `/handoff` builds the journal from that file and
`/ingest` builds pages from the journal, so an attribution unratified here is a page tomorrow. This
is the last point at which a wrong sentence costs a question rather than a supersession.

**A decision he did not answer is `could-not-close:`, exactly as in the gate above** — never a
silent promotion to his word. The failure direction is the safe one: an unratified line written in
the session's own voice is merely weaker than it might have been, while a paraphrase signed
`owner:` is a rule nobody voted for.

## 6. Write the retro file

Copy `.claude/templates/retro.md` to `.superpowers/sdd/retro.md` and fill it. Every section stays;
write "none" rather than dropping one.

The template's sections each carry a `→ handoff:` line naming where their contents land. **That
mapping lives in the template and nowhere else** — this skill does not restate it, and neither does
`/handoff`, which reads it there.

**The file's failure mode is silence**, exactly as `.superpowers/sdd/vault-feedback.md`'s is:
nothing checks that it was written, and a session that skips this skill produces no file at all,
which looks the same from the outside as a session with nothing to confess. That is the one thing
to watch about this channel, and naming it is cheaper than discovering it.

It is git-ignored and lives one session. It is not knowledge until it has been through an ingest.

## 7. Then `/handoff`

`/handoff` reads this file, files each section where the template says, drains
`vault-feedback.md`, writes the journal, and runs the gate. `/ingest` follows it.
