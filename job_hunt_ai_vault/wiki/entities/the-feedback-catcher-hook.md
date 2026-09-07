---
title: "`catch-the-feedback.ps1` — the hook that lifts a spoken feedback block into the file"
type: entity
status: current
authority: feedback-catcher-hook
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/hooks/catch-the-feedback.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, process, vault]
---

# The hook

**Appeared 2026-08-24.** Registered on `MessageDisplay`, with no matcher — the event takes none.

| Property | |
|---|---|
| File | `.claude/hooks/catch-the-feedback.ps1` |
| Event | `MessageDisplay` |
| Disposition | **speaks** — it never refuses, because a refusal is possible on `PreToolUse` alone ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]) |
| Reads | the assistant's own message, arriving as `delta` |
| Writes | `.superpowers/sdd/vault-feedback.md`, appending |
| State | `.superpowers/sdd/.message-display/`, one file per message, swept by the hook itself on a one-day cutoff |

**It accumulates by `message_id` and parses at `final`.** The event's own description says it fires
with each batch of newly completed lines; measured, it fires once with the whole message. The hook
is correct under either behaviour, which is why the divergence could be recorded rather than
resolved ([[message-display-fires-once-with-the-whole-message]]).

# The three behaviours that are not obvious from its job

**Fence depth, not fence presence.** A `VAULT-FEEDBACK` fence nested inside another fence is an
example — a rule page or a skill documenting the form — and is ignored. Without this, the
documentation of the channel would file itself every time it was quoted.

**It yields in the turn the file shrinks.** `/handoff` empties the file to its header, and a
recorder that fought the drain would refill what the journal has just taken. The hook remembers the
file's size at the turn's first sighting and files nothing more in a turn where the size has
dropped — **a comparison rather than a judgement about which ritual is running**
([[whoever-filed-a-feedback-line-empties-it]]). **The turn after resumes**, and a selftest case
holds that half.

**An undeclared kind is kept with a note, not dropped.** The vocabulary is four kinds
([[lint-and-process-stop-being-session-kinds-and-decision-joins]]); a line filed under a fifth is
still the session's testimony, and dropping it would make the channel lossy in the direction of
silence — this store's most-recorded failure shape
([[an-instrument-that-fails-towards-nothing-to-do]]).

# What holds it

**Fifteen cases in `scripts/hook-selftest.ps1`**, at `scripts/hook-selftest.ps1:980-1058` for the
registry row: the fence reader in both directions, accumulation until `final`, deduplication by
`message_id`, the drain skip and the resumption after it, the undeclared kind, and exit 0 on a
malformed payload. The suite reads **caught 138, missed 0**, up from 123.

**This is the instrument the feedback rule never had**
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]],
[[speak-the-feedback-in-the-turn-and-the-hook-files-it]]).

# A constraint on its own source that is easy to break by accident

**The `.ps1` must not contain the literal `permissionDecision = 'deny'`, even in a comment.** The
hook register's disposition case greps for that string to decide whether a hook refuses, so a
comment quoting it would make this hook read as a blocker
([[the-system-naming-which-hooks-block]]).

# Why it exists at all

**The rule obliging a session to write the feedback file broke eight recorded times**, every one
because plan mode forbids a session to write files
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]]). The hook is not a reminder: it moves
the writing to a party that is not disarmed.

# It was repaired on 2026-08-24, in the session after the one that built it

**`$OPENS` decides what opens a record.** A record starts at column zero, optionally behind a list
dash, and nowhere else; an indented line is a continuation of the record above it.

**`Split-Records` turns one fence into one entry per kind line.** It used to take the kind off the
first line and apply it to the whole block, so a block carrying four kinds became one entry of the
first kind.

**Both halves came from the same place: two renderings of one rule disagree.** The rendered rule in
the repository's `CLAUDE.md` shows a leading dash and four kinds in one block; the template in
`.superpowers/sdd/vault-feedback.md` shows neither. **The hook understood only the form nobody
follows** ([[a-feedback-record-opens-at-column-zero-and-indentation-marks-a-continuation]],
[[the-feedback-record-opens-at-column-zero-and-the-kind-is-written-without-backticks]]).

**The cost of the defect is measured rather than estimated: nine blocks of that session were filed
as `unknown:`**, about forty lines, each carrying its real kinds inside its own body where nothing
mechanical could see them.

**`pwsh scripts/hook-selftest.ps1` reads `caught 141, missed 0`, exit 0** — from 138 at the
session's start, three cases added. **Four forms of the kind line were checked rather than
reasoned about**: the bare form matches, and the dashed, half-quoted and fully-quoted forms do not.

# It gained a note on an unquoted attribution — 2026-08-26

**A `decision:` record whose shape declaration is *the owner said it* and which carries no guillemet
quotation now draws a note.** Advisory, filed as written, **never a refusal**: the record goes into
the file exactly as it was spoken and the note stands beside it.

**The predicate is the absent quotation and not the alphabet**, against the plan's letter and on the
owner's ratification ([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]],
[[divergence-the-b3-note-was-built-against-the-plans-letter-and-reported-after]]). Measured ground:
`log.md` held 1218 records, 125 of them `decision:`, 81 carrying the mark — 66 with a quotation, 15
without, **and all 15 Cyrillic**.

**It fired a false positive on its own first live encounter**, on a record that discusses the phrase
rather than claiming it, and was anchored to the shape declaration at the head of the record. A case
pins it ([[a-guard-that-matches-a-phrase-anywhere-flags-the-record-that-discusses-it]]).

**Its selftest could not deliver a single non-ASCII byte until this session**, so the case exercising
a Russian quotation had never been possible
([[the-hook-selftest-could-deliver-no-non-ascii-byte-to-any-hook]]). **`powershell -NoProfile -File
scripts/hook-selftest.ps1` reads `caught 148, missed 0`**, from 144. **There is no `pwsh` on this
machine** — the rows above naming it are the shorthand, and `powershell -NoProfile -File` is the
command that runs.

**And a hand-run probe of this hook against the repository copy filed a fabricated record into the
live file** the same day ([[a-register-of-what-each-hook-writes-when-it-is-probed]],
[[testing-a-session-start-hook-with-a-made-up-payload-has-live-side-effects]]).

# It gained a counter and still prints nothing on every path — 2026-08-29

**It now counts the session's own replies that carried no `VAULT-FEEDBACK` block**, and writes that
number into its own state file. It says nothing about it: `MessageDisplay` is the one event that can
see a session's replies and it **cannot speak to the session**, which was measured with a throwaway
probe on the same day ([[a-hook-on-message-display-cannot-speak-to-the-session]]).

**So the reply-silence feature is two hooks and one number** — this one counts and writes,
`remind-the-feedback.ps1` reads and says the sentence
([[the-reply-silence-counter-is-split-between-the-hook-that-sees-and-the-hook-that-speaks]],
[[the-feedback-reminder-hook]]).

**Its disposition is unchanged.** It printed nothing on every path before and it prints nothing on
every path now; what it gained is a second thing it writes.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
