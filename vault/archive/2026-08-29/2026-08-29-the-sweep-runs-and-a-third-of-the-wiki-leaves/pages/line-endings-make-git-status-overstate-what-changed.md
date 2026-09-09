---
title: "git status flagged files that git diff found unchanged: a line-ending churn overstates a session's diff"
type: lesson
status: archived
authority: line-ending-churn
basis: measurement
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md"]
tags: [process, vault]
---

# The alarm says 23; the change is 6

**Measured 2026-08-14**, twice — once by the session, once by the ingest that followed it:

```
git status --short    23 modified files
git diff --numstat     6 files with content:
                       CLAUDE.md, the three skills (handoff, ingest, vault-ask), tags.md, log.md
```

*(The title read "git status flagged 23 files and 6 had changed: a line-ending churn overstates a
session's diff" until 2026-08-18, and the block above is where those readings now live, as evidence
rather than as a headline. **They were a reading of one past day** and could not drift — 2026-08-14
is over. That reasoning stood in a `quantity:` line until the field was rejected and the rule made
unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]): a number that genuinely
cannot drift still leaves the title, because the mechanism that let a page say so has been
withdrawn. The title now names the instruments that disagreed instead of quoting what each
returned ([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is a correction in
place rather than a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]).)*

The other **17 differ only in their line endings**, with byte-identical content. The session could
not identify the cause and recorded it as unknown; `vault-check.sh` was exonerated by experiment
(15 modified before a run, 15 after, same md5, same mtime), and the `PreToolUse` hook contains no
write at all.

**Two measurements the journal did not have**, taken during the ingest of 2026-08-14:

- `git diff` emits, for each of those files,
  `warning: in the working copy of '<path>', LF will be replaced by CRLF the next time Git touches
  it`. So the working copy holds **LF** where this repository's configuration wants CRLF:
  `core.autocrlf=true`, and `.gitattributes` pins only `*.sh text eol=lf` — markdown is not
  mentioned there at all;
- on a sampled file (`wiki/entities/dou-ua.md`) the working copy is **byte-identical to the
  committed blob** — same md5 as `git show HEAD:<path>` — and `git diff -- <path>` prints nothing,
  **while `git status --short` keeps listing it as modified.**

Those two together name the shape — something rewrote the files with Unix endings in a tree whose
checkout convention is CRLF — and still do not name the writer. **The cause remains unidentified**,
and the honest reading is that `git status` is reporting a stat-level difference that no content
comparison reproduces.

**A third measurement, 2026-08-15, by the first `/vault-lint`: the corpus is split, not converted.**
Of 111 pages in `wiki/` and `archive/`, **52 hold CRLF and 59 hold LF**, none mixed within a file.
So this is not one event that rewrote a tree — it is the ordinary state of a store whose files are
written by several tools under `core.autocrlf=true` with no rule for `*.md`, and it will keep
producing the overstatement above at whatever rate pages are touched. The size of the churn is now
a knowable number before a session starts, which is the only part of this a librarian can supply;
the `.gitattributes` line that would end it is still the owner's, and pinning `*.md` would rewrite
59 files in one commit.

## Why it is worth a page instead of a shrug

**`git status` overstates what changed, and that is the shape of alarm this project has already
learned not to read.** A false alarm printed beside a true one trains the reader past both — the
same reasoning that made two of `vault-check.sh`'s conditions advisories rather than errors
([[vault-scripts]]), and that took mtime out of both staleness checks
([[staleness-checks-run-at-different-times-and-ask-different-questions]], [[the-brief-is-stamped-with-its-commit]]).

It also lands squarely on **step 8 of an ingest**, where the librarian compares the journal's
`commits:` claim against the tree: a bare file count is not evidence of work, and the number to
quote there is `git diff --numstat`, with the status count named separately as noise.

## What would settle it

`.gitattributes` is where the answer belongs, and this repository **has one** — with a single rule
in it, `*.sh text eol=lf`, written for a different reason entirely: a shell script with CRLF breaks
the container's entrypoint. **Markdown is not mentioned**, so every `.md` here follows
`core.autocrlf` and depends on what wrote it last. Pinning `*.md` the same way would settle the
churn; that is a change to the repository, and the owner's to make rather than an ingest's.

Until then, `git diff --numstat` is what to quote and `git status --short` is what to distrust.

**Deferred explicitly on 2026-08-15**, as one of the six audit findings owed to the owner
([[the-audits-findings-are-owed-to-the-owner]]). The two consequences were priced against each
other and neither is free: **fixing it is one commit that rewrites 59 files and nothing else**;
not fixing it means **every session reads `git status` twice**, for as long as the store is
written. The overstatement is not an event that happened once — it is the standing state.

This is not the first thing a carriage return has cost this project — the earlier ones are on
[[session-hooks]] and [[vault-scripts]], including the evening a stray `
` in a coverage sidecar
turned 317 verdicts into `BAD VERDICT` and made the ingest gate red one minute after a merge.

## The cause was identified on 2026-08-16, and it is not a line ending

**The paragraph above that says "the cause remains unidentified" is superseded by a measurement,
not by an argument.** The index caches each entry's stat **size**; rewriting a file into the other
line-ending form leaves the blob identical, so `git add --renormalize` never restats the entry and
the cached size stays at the old form's. The mechanism, the `git ls-files --debug` figures, and the
two remedies — `git add -A`, and delete-then-checkout rather than `git checkout-index -f` — are
[[the-stale-stat-cache-behind-git-status]].

**The advice on this page is unchanged by that**: quote `git diff --numstat`, distrust
`git status --short`. What changes is that the fix is now a command rather than a mystery.

## The price this page quoted was wrong, measured 2026-08-16

This page priced the `.gitattributes` fix as **"one commit that rewrites 59 files and nothing
else"**, and finding #4 of [[the-audits-findings-are-owed-to-the-owner]] repeats it. Measured
at `86823e3` before the fix was made: **all 161 tracked `.md` were already `i/lf` in the index**,
so the commit changed **exactly one file**. The 52-against-59 split is **the working copy only** and
never reached a blob — which is the same stale-stat mechanism above, seen from the other end.

The estimate is left where it stands, as what was believed when the deferral was made. The
correction belongs beside it and not inside it.

**The fix was taken on `5e864f1`** — `*.md text eol=lf`, with the reasons, the rejected widening and
the per-extension measurement: [[markdown-is-pinned-to-lf]].

## A second source of the same noise, and it is not git

**An editor is reformatting vault pages.** Markdown table alignment in [[vault-feedback-file]] was
rewritten on 2026-08-16 by something that was neither the session nor the librarian — content
byte-identical, padding changed. It produces a diff on a page nobody edited, which is the same class
of false alarm as the churn above, and it is worth knowing before it is mistaken for a librarian
write ([[the-librarian-writes-unattended]]). It will keep happening.
