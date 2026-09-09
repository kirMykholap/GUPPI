---
title: "`grep -c $'\r'` returns the file's line count, and it was used to contradict a correct claim"
type: lesson
status: archived
authority: cr-counting-instrument
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md"]
tags: [process, harness, vault]
---

# The failure, 2026-08-19

**`grep -c $'\r' <file>` does not count CRLF lines. It returns `wc -l`.** In the shell used here the
escape collapses to an **empty pattern**, an empty pattern matches every line, and `-c` counts
matching lines — so the answer is the file's total line count, always.

It was used to check whether a subagent's edits had introduced CRLF. **It reported 232, 59 and 57
against three files of exactly 232, 59 and 57 lines**, and those numbers were quoted to contradict
the subagent's correct claim that the files were clean.

**The honest instrument is `tr -dc '\r' < file | wc -c`.** It reports a **byte count**, which cannot
be confused with a line count, and after the correction it read **zero CR bytes, blob and worktree
alike**.

# Why it survived being read

**The wrong number is large, plausible, and always exactly a real quantity of the file.** It is not
noise and it is not zero; it is a true fact about the file, answering a question nobody asked. A
reader checking *does this look sane* passes it every time.

**It was caught only because the wrong number agreed with a real quantity** — the same total appearing
in three files of three different sizes is what gave it away. That is
[[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]] arriving in a new place:
there the figure agreed with nothing and a second instrument killed it, here it agreed with something
it had no business agreeing with.

# The rule this leaves

**An instrument whose units are the same as the units of the thing it is not measuring cannot be
sanity-checked.** Prefer an instrument whose output is in **different units** from the wrong answer:
bytes where the mistake would report lines, a name where the mistake would report a count. That is
the whole of why `tr -dc | wc -c` is the recommended form and not a shorter `grep`.

**And line endings are a class this project has already been bitten by twice**
([[line-endings-make-git-status-overstate-what-changed]],
[[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]), which is what makes
a command that lies about them worth naming rather than merely correcting.

# What it cost

**A subagent was told it was wrong when it was right.** Nothing was written on the strength of it,
because the contradiction was resolved inside the same turn — but the cost of that shape when it is
not caught is a correct report overridden by a confident number
([[a-subagents-most-believable-sentence-is-the-one-to-measure]]).

## Walked into again on 2026-08-20, by a session that had this page

**Same command, same wrong reading, and it cost a false alarm raised to the owner.** After the
`*.tsv` pin, `LC_ALL=C grep -c $'\r' <file>` reported **97** CR bytes in a coverage sidecar and
**81** in a `_schema.yaml`. **Both are zero** — measured at byte level with `tr -d '\n' | wc -c`
against `tr -d '\r\n' | wc -c`, the counts are identical, and `git ls-files --eol` had said
`i/lf w/lf` all along.

**What it cost:** the owner was told the sidecars were CRLF in the index, that `git add --renormalize`
had failed, and that the session's own commit message was wrong. **All three were false, and the
commit message was right.**

**What it did not cost:** nothing was committed on the strength of it. The correction was still a
chat claim when the instrument was tested
([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

**The page existing did not stop it**, which is the entry worth keeping: this is the same store, the
same command and the same reading, met by a session that could have grepped for it
([[knowing-a-rule-is-not-a-mechanism]], [[deriving-what-the-vault-already-holds-costs-a-round]]).
