---
name: handoff
description: Write the session journal at the end of a session, from the template, into the vault's raw/handoffs/. Use when a session is ending, when work is being handed over, or when asked to write up what happened.
---

# Write the handoff

The handoff is the **only** channel from this session to the librarian, which did not watch it.
Everything the vault will ever know about today is what you write here.

**Find the vault first.** It is the top-level directory containing a `wiki/`; its name is the name
Obsidian displays and the owner changes it, so never hard-code one:

```bash
VAULT=$(ls -d */wiki 2>/dev/null | head -1 | sed 's|/wiki$||')
```

0. **`/retro` runs first.** Its file, `.superpowers/sdd/retro.md`, is the main input to everything
   below: each of its sections carries a `→ handoff:` line naming which section here receives it,
   and **you read those lines there rather than deciding it again**. If the file is absent, say so
   in the first line of your report - a session that skipped the retro produces a journal with no
   confessions in it, and that looks exactly like a session with nothing to confess. Then empty
   the retro file back to its header, as with the feedback draft below.
1. Copy `.claude/templates/handoff.md` to
   `$VAULT/raw/handoffs/<YYYY-MM-DD>-<short-slug>.md`. **The template lives outside the vault and
   this skill carries no copy of it** - a pointer is checkable and a copy is not. The older
   `$VAULT/raw/handoffs/TEMPLATE.md` is superseded and is not the one to copy.
2. Fill the frontmatter. `commits:` is the range this session produced — get it with
   `git log --oneline <first>..HEAD`. The handoff is testimony; git is the evidence, and the range
   is what lets the two be compared. **Write the resolved ids on both ends**, not `HEAD`: `raw/` is
   immutable, so a range ending in `HEAD` means something different every time it is read
   afterwards. The first handoff written from this template says `2620998..HEAD`, and that is the
   defect this line exists to stop repeating.
3. Fill every section. **An empty section is a legal answer — write "none" — but the section must
   stay.** Nobody misses `Feedback to the librarian` on their own; it has to be asked.
4. `Feedback to the librarian` carries what the session filed as it worked. **Its source is
   `.superpowers/sdd/vault-feedback.md`, not your memory of the session** — copy every line across,
   then empty the file back to its header. A miss recorded at 11am and reconstructed at 8pm is the
   one that goes missing, which is why that draft exists. If the file holds nothing, the section is
   "none" — but say so having looked, not having assumed. Its `- harness:` lines go to `Harness`
   instead, which is the last section and a work queue rather than an account of the session.

   **You do not write that file and neither does any session.** It is filled by
   `.claude/hooks/catch-the-feedback.ps1` on `MessageDisplay`, which lifts a fenced
   `VAULT-FEEDBACK` block out of the reply that spoke it. The rule obliging a session to write the
   line itself broke eight recorded times, every one of them because **plan mode forbids a session
   to write files** — the party the rule binds, disarmed exactly when it notices something.

   **Four session kinds as of 2026-08-24**: `miss:` (something went wrong and where it surfaced),
   `measure:` (a number and its conditions), `decision:` (what was decided, **by whom**, and
   against what), `harness:` (a decided change to the files that instruct an agent). `lint:` and
   `process:` are the librarian's words now; a journal written before that date carries them and
   they transfer unchanged.

   **Emptying this file is the one moment the catcher must not fight you**, and it does not: it
   remembers the file's size at the turn's first sighting and files nothing more in a turn where
   the file has shrunk ([[whoever-filed-a-feedback-line-empties-it]]). The line is not lost — it
   leaves with the journal you are writing.
5. Do not edit an existing handoff. `raw/` is immutable — a correction is a new line in a later
   handoff, not a rewrite of an earlier one. What the session believed at the time is data.

And the rule that governs every line this journal puts in the owner's mouth:

<!-- rule: a-block-attributed-to-the-owner-is-written-in-his-own-russian -->
The owner's words enter a journal verbatim and in Russian. Where a session understood rather than
heard, it writes its own understanding in its own voice and does not sign it `owner:`.

<!-- /rule: a-block-attributed-to-the-owner-is-written-in-his-own-russian -->

And the rule those `Feedback to the librarian` lines arrive by, which is why the file you are
draining has anything in it:

<!-- rule: speak-the-feedback-in-the-turn-and-the-hook-files-it -->
**When the vault answers wrong — or anything else worth recording goes wrong — say it in your reply
in that same turn**, inside a fenced `VAULT-FEEDBACK` block. **You never write**
`.superpowers/sdd/vault-feedback.md` **yourself.** A hook on `MessageDisplay` lifts the block out of
your message and files it, which is what makes the channel usable in plan mode, where a session
cannot write a file at all.

```VAULT-FEEDBACK
- miss: what the vault failed to supply, and where that surfaced
- measure: a number, with what it does and does not mean
- decision: what was decided, by whom, and against what - naming which shape it is:
  the owner said it, the owner selected it, or the session understood it
- harness: a decided change to the files that instruct an agent
```

A `VAULT-FEEDBACK` fence nested inside another fence is an example and is ignored, so the block
above files nothing. `/handoff` drains the file into `Feedback to the librarian` and `/ingest` files
each line under the kind it names. **Recording is not arguing**: it costs a line, and whether the
corpus changes is the owner's call, later.

<!-- /rule: speak-the-feedback-in-the-turn-and-the-hook-files-it -->

This is the earliest point the paraphrase can be caught by anything mechanical: `raw/` is immutable,
so a line signed `owner:` here is a line the librarian will compile as his testimony and later
sessions will reason from as his word. `/retro` runs before this skill and puts every attributed
line to him; this is what the journal owes even when it did not.

**The section names are load-bearing and the numbers are gone.** `/ingest` cuts on heading text, so
renaming a heading silently changes where knowledge lands - which is exactly why the numbers were
dropped: a name does not move, and a number moved every time a section was inserted. The set of
names is read from `.claude/templates/handoff.md` and written down nowhere else.

**Then run the gate, before the ingest:**

```bash
bash scripts/vault-check.sh
```

Rule 8 judges a journal only while it is **uncompiled**, which is now - the form matters to the
ingest that is about to read it, and afterwards `raw/` is immutable and the form can never be
corrected. This is the one moment the journal is still being written rather than standing as
testimony. Fix what it names, then run `/ingest`.
