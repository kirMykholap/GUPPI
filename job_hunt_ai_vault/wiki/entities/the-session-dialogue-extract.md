---
title: "`session-dialogue.py` and the extract it writes, which is the first reader the transcript has had"
type: entity
status: current
authority: session-dialogue-extract
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "scripts/session-dialogue.py", "scripts/session-dialogue-selftest.py", ".claude/hooks/session-brief.ps1"]
tags: [harness, process, retrieval]
---

# The script and its two files

**Appeared 2026-08-24.** Stdlib only, run through `uv`.

| Property | |
|---|---|
| Script | `scripts/session-dialogue.py` |
| Input | the transcript named by `.superpowers/sdd/session-transcript.path`, written by `session-brief.ps1` at `SessionStart` |
| Fallback | the newest `.jsonl` in the store — **and it says so when it falls back**, because a silently wrong session is worse than no extract |
| Output | `.superpowers/sdd/session-dialogue.md`, git-ignored, living one session |
| Holds | 32 selftest cases in `scripts/session-dialogue-selftest.py` — the fence reader in both directions, the speaker classifier, and every refusal |

**It refuses loudly with counts rather than emitting an empty file.** An empty extract and a session
that said nothing look identical, and the ritual reading it would report *nothing to discuss*
([[an-instrument-that-fails-towards-nothing-to-do]]).

**It must reconfigure stdout**: the host console is cp1252 and the extract is mostly Russian
([[windows-console-encoding]]).

# What it extracts

Owner turns, session replies, **every `AskUserQuestion` with its answer**, and every feedback mark.
Measured on the session that built it: **13 owner turns, 46 replies, 3 menus with 3 answers, 6
marks, 132 KB from a 0.6 MB transcript.** On the session of 2026-08-22: **25 owner turns, 94
replies, 11 menus with 11 answers, 225 KB.**

# It is a third transit file, and it owes the paragraph the other two carry

`.superpowers/sdd/retro.md` and `.superpowers/sdd/vault-feedback.md` each say why they exist as
files rather than as memory ([[vault-feedback-file]], [[the-retro-step]]). **This one does not yet
say why it is a third file rather than folded into one of them**, and the journal names that as
owed.

# The defect found at its first real use, and it was fixed the same day

**It labelled system-injected content as owner turns.** In the extract of its own session, turn 95
was a background-task notification and turn 99 was the body of the `/retro` skill; both arrive as
user-role text blocks and both were rendered under `## N. owner`. A retro reading that file could
have attributed a task notification to him — **the exact class the ratification apparatus exists
against**, of which 53 instances were once found across 44 pages
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

**The separator is `origin.kind`**, and the classifier now reads it
([[a-transcript-carries-what-was-said-and-not-what-was-reasoned]]). **Found by reading the extract
at the first real use of step 0** — which is the step that exists to stop reading from memory.

# What it is for

`/retro` step 0 runs it and builds its list of open questions from the file
([[the-floor-under-a-session-is-read-because-the-record-already-existed]]). **Four of one retro's
fifteen open questions came from the feedback marks; eleven were found by reading the extract** —
the only measurement this channel has of what the marks miss, and it says they miss two thirds.

# It gained `resolve_menus` and four counters — 2026-08-26

**A menu resolves to one of four states rather than two**, and the script now says which
([[a-menu-resolves-to-a-state-and-an-interrupt-counts-as-an-answer]]). `session-dialogue-selftest.py`
reads **caught 52, missed 0**, from 32.

**Swept over 40 transcripts the same day: 193 menus — 192 answered by selection, 1 answered in prose
after an interrupt, 0 still open, 0 lost.** The defect the split corrects fired **once** across every
transcript on disk.

**Its own session's extract is the case with no counter at all: 6 owner turns, 65 session replies,
zero menus asked, 4 `VAULT-FEEDBACK` blocks filed.** Every ruling of that day arrived in prose, and
nothing in the harness notices a retro that asks nothing
([[divergence-the-retro-filed-no-feedback-block-while-it-ran]],
[[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]).

# The attention list groups by filed block rather than by line, and some marks are misfiled — 2026-08-26

**A defect in `scripts/session-dialogue.py`, found and not repaired.** The section heading of a group
is taken from **the first line of each fenced block**, and every other line in that block lands under
it.

**Measured on the session of 2026-08-26: four `miss:` records filed under `## measure` and one under
`## decision`.** A reader auditing the session by section does not find them.

**It was found by reading the extract whole** — the thing the session had argued was unnecessary
because its own context already held the conversation. The extract carries a **derived** list that no
context contains ([[an-argument-from-the-context-i-already-hold-cannot-see-a-derived-artefact]],
[[the-session-extract-is-read-whole-at-every-retro]]).

**Deferred to S3 as a harness line**, because the repair moves with a 52-case selftest in
`scripts/session-dialogue-selftest.py`
([[the-grouping-defect-in-the-dialogue-extract-is-an-s3-harness-line]]). **Until it lands, every
retro's own kind counts are wrong in a way nothing announces.**

## Its second session's counters, for the series

**2026-08-26: menus asked 0, in a session that took thirty-six decisions.** Every ruling arrived in
the owner's own prose ([[divergence-the-retros-menu-step-was-answered-in-enumerated-prose]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*

# A second session with zero menus, and the reading cuts the other way — 2026-08-26

**20 owner turns, 64 session replies, zero menus.** Every ruling of the check-system session arrived
in his own words, in prose, and every option set was a numbered list he answered by number.

**The warning the retro skill carries is about the opposite case** — a session whose every ruling
arrives through a menu is one the owner did not frame — **and this is its mirror**, for the second
day running ([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]).

**The grouping defect reproduced in the same extract**: several feedback blocks landed under a
`## - miss` heading rather than under their own turn. It is S3's item 27 and it is unfixed
([[the-grouping-defect-in-the-dialogue-extract-is-an-s3-harness-line]]).

# The reading of 2026-08-28

**12 owner turns, 77 session replies, 15 feedback marks, zero menus, 193,109 bytes.** The marks
yielded 48 `decision:` lines, which are 24 distinct decisions each listed twice.

**Zero menus means every ruling that day arrived as prose**, so nothing in the session came back as
the result of a tool ([[a-menu-resolves-to-a-state-and-an-interrupt-counts-as-an-answer]]).

**The extract was read by its marks rather than whole**, on the session's own judgement that context
had never compacted and all twelve owner turns were available verbatim. **That weakens step 0 of the
ritual**, whose ground is that memory at the end of a long session is a compression of itself — and
the only party who can check that claim is the session, about itself
([[the-session-extract-is-read-whole-at-every-retro]]).

**And the marks carry decisions and nothing else.** The retro's open-questions list held 17 items and
none of them came from a mark: a fork closed silently and a mistake corrected in flight are invisible
to that channel by construction.

# The reading of 2026-08-29, and the in-turn marking caught everything — 2026-08-29

**13 owner turns, 33 session replies, ZERO menus, 15 feedback marks, in a 200,564-byte file** — larger
than the 15–30k tokens the retro skill quotes for it.

**All 26 decision marks were caught in the turn; the session added none from memory.** That is 26 of 26,
against roughly five of six on the previous session. **It does not mean nothing was missed** — a decision
neither marked nor remembered is invisible to both readings, which is the one thing this instrument
cannot measure about itself.

**Zero menus is the second consecutive session at zero**, and it is the evidence behind the third
recorded refusal of the retro's menu step ([[the-retro-step]],
[[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]).

**The grouping defect in `scripts/session-dialogue.py` is unrepaired.** The owner said «чиним» on
2026-08-29 and it was not built, so every retro until then still misfiles some marks
([[the-grouping-defect-in-the-dialogue-extract-is-an-s3-harness-line]]).

# A reading of 2026-08-30, and the skill's own cost figure is four times under

**The extract of 2026-08-30 reports 32 owner turns, 78 session replies, zero menus, 31 feedback marks
and 3 system blocks, in a 373,768-byte file** — against the *"15-30k tokens"* the retro skill quotes
for it.

**It means the skill's cost figure is stale on a long session.** It does **not** mean the file is
useless; it means reading it whole is a decision rather than a default.

**That session read the owner's 32 turns in full and not the 78 replies**, on the ground that nothing
had been compacted and no menu was used — the two reasons the step exists.

> [!NOTE] RAISED, NOT RESOLVED
> **[[the-session-extract-is-read-whole-at-every-retro]]** is a live `prohibition` in the owner's own
> words of 2026-08-26, and it is him refusing exactly this conditionalisation. **The partial read of
> 2026-08-30 diverges from it**, and the journal does not record it as a divergence. **Only the owner
> may narrow that rule**; the librarian records the gap and hands it back.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, extended 2026-08-30.)*
