---
title: "The LF pin protects the committed blob and not the working copy, and `git status` says nothing either way"
type: lesson
status: archived
authority: lf-pin-working-copy-blindness
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", ".gitattributes"]
tags: [process, harness, vault]
---

# The measurement, 2026-08-19

`job_hunt_ai_vault/raw/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md` is **CRLF in every
one of its 337 lines on disk**, while its committed blob is clean LF — **and `git status` reports it
unmodified.**

`text eol=lf` normalises on the way *in*, so the working copy and the blob compare equal after
normalisation and git has nothing to say. **One file of 374 in the vault carries it**, found only
because a rename sweep made someone measure CR bytes across the whole tree.
`tr -dc '\r' < file | wc -c` is the instrument
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]).

# It is the inverse of the recorded lesson, and that is why it is dangerous

[[line-endings-make-git-status-overstate-what-changed]] records `git status` naming 23 files where
`git diff` found 6 — the command **overstating** a difference. Here it is **silent while every line
ending in the file differs.**

**A reader who has learned the first lesson will trust `git status` in exactly the case where it says
nothing.** The two belong beside each other for that reason: one teaches that the command exaggerates,
and the untaught corollary is that it can also be blind.

# What the pin actually promised, and it delivered the opposite here

The pin's own stated reason, on [[markdown-is-pinned-to-lf]] and repeated on
[[a-file-class-is-pinned-after-it-costs-something]]:

> *"it changes nothing about the repository and everything about the **working copy**, which is what
> scripts that edit these files actually read"*

**That is the half it did not deliver.** The pin governs what enters the repository. **A tool that
writes a file after checkout leaves CRLF on disk and nothing reports it** — and the vault's tooling is
`awk` and `bash` reading the working copy, which is precisely the reader the pin was bought for.

# What it does not mean

**It is not an argument against the pin.** Without it the blob would be CRLF too, and every diff would
be noise. The pin is doing the job it can do.

**The gap is that no instrument watches the working copy.** Nothing in the harness measures CR bytes,
nothing reports a converted file, and `git status` is the tool everyone reaches for. Naming the
instrument is what this page is for; whether the harness should carry a check is undecided and is a
cost question ([[a-file-class-is-pinned-after-it-costs-something]]).

# The scale of it, measured a week later — 2026-08-26

**115 tracked files were CRLF in the working copy against a clean LF index**, including
`.claude/hooks/ask-the-vault.ps1`, whose class had been pinned since 2026-08-17. **So the pin had
protected the blob and nothing else, for nine days, across most of the repository.**

**`git status` was clean throughout**, exactly as this page says it would be.

**The instrument that reads it, and the one that does not.** `tr -dc '\r' < file | wc -c` counts CR
bytes; `grep -c $'\r' file` counts *lines containing* one and is a different number
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]).

**The repair is `rm` plus `git checkout`, and `git checkout-index -a -f` does not do it.** The
checkout-index form was tried first and left every file as it was; removing the file and checking it
out again performs the conversion. After the sweep, zero remain and `git status` is clean.

**The fix for the class of it is a default rather than a longer list** — `* text=auto eol=lf` at the
head of `.gitattributes`, decided the same day
([[a-file-class-is-pinned-after-it-costs-something]]).

**And a bulk sweep of 115 files is exactly where an exception gets lost.** One member of that list was
a file the owner had ruled untouched that morning
([[divergence-a-bulk-renormalisation-swept-a-file-the-owner-had-ruled-untouched]]).
