---
title: "The floor under a session is read, because the record already existed and nothing read it"
type: decision
status: current
authority: session-floor-reading
binding: prohibition
basis: measurement
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "scripts/session-dialogue.py", ".claude/skills/retro/SKILL.md"]
tags: [harness, process, agents]
---

# The ruling, 2026-08-24

**Nothing new records what a session said. Something reads what was already recorded.**
`scripts/session-dialogue.py` extracts one session's dialogue from the harness transcript and
writes `.superpowers/sdd/session-dialogue.md`; `/retro` runs it as step 0 and builds its list of
open questions from that file rather than from memory ([[the-session-dialogue-extract]]).

# The measurement that decided it

**The Claude Code transcript store for this project holds 37 files and 255 MB, and
`rg -in transcript .claude/ scripts/` returns zero.** The complete record of every session had
existed for the life of the project and **nothing in the repository read it.**

**Dialogue is 2–4% of a transcript**: 24.9 KB of a 0.6 MB file for the deciding session; median
130 KB across the 37, largest 221 KB, 5.8 MB in total. So the extract is affordable for a ritual
that runs once per session ([[the-unreadable-mass-is-in-the-plans-not-the-vault]]).

# What was rejected

**A second recorder** — hooks on `UserPromptSubmit` and `Stop` that write what was said. They would
record what is already recorded, and a prompt hook cannot see the half that matters:
**`AskUserQuestion` answers are in the transcript**, and in one measured session **8 of 10 rulings
arrived through a menu** ([[a-transcript-carries-what-was-said-and-not-what-was-reasoned]]).

# What it obliges

- **`/retro` step 0 runs the extractor**, and steps 1 and 5 build their lists from the file. Both
  must report how many items came from the feedback marks and how many were found by reading — that
  difference is the only measurement this channel will ever have of what the marks miss
  ([[the-retro-step]]).
- **The extraction stays temporary.** `.superpowers/sdd/session-dialogue.md` is git-ignored and
  lives one session; it is a third transit file beside `retro.md` and `vault-feedback.md`, and it
  owes the paragraph the other two carry about why it is a third file rather than folded into one
  of them ([[vault-feedback-file]]).
- **`session-brief.ps1` writes the transcript path** to `.superpowers/sdd/session-transcript.path`
  at `SessionStart`, because the extractor cannot otherwise name which of 37 files is this session
  ([[session-hooks]]).

# What it bought on the first run, which is the argument for keeping it

**An attribution question was answered in seconds that no previous retro could answer at all.** The
owner asked whether «порог не назначаем» had been his words; it was turn 38, verbatim, found by
searching the text. **Every previous retro answered that class of question from memory, hours
later — which is how 53 owner-attributed blocks reached 44 pages**
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]],
[[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]).
