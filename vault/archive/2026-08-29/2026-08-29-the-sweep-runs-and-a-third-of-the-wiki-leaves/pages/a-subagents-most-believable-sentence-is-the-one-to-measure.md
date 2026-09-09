---
title: "A subagent's most believable sentence is the one to measure, and the one that failed sat inside a section headed *what you should know*"
type: lesson
status: archived
authority: believable-subagent-claim
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "CLAUDE.md", ".gitattributes"]
tags: [agents, process, vault]
---

# The incident, 2026-08-18

The librarian reported, while verifying its write of the map page:

> *"All 116 lines of `CLAUDE.md` are CRLF in the working tree today; the run will convert it."*

**Measured: `tr -cd '\r' < CLAUDE.md | wc -c` is 0**, and `.gitattributes` has pinned `*.md text
eol=lf` since 2026-08-17 ([[markdown-is-pinned-to-lf]]). Believed, it would have sent someone
hunting a line-ending conversion that never happens, or "fixing" one.

**Two other claims in the same report verified exactly** — the slice's md5 and byte count, and the
prose overlap in the destination. So the failure is not the reporting habit; it is one unmeasured
assertion sitting inside a report whose other assertions were measured.

# What makes this sentence the dangerous one

**It was offered as a reason not to misread the coming diff**, in a section headed *what you should
know* — that is, framed as context rather than as a finding, which is exactly the framing a reader
does not audit. A claim presented as a caveat gets less scrutiny than a claim presented as a result,
and it earns none of that discount.

**And it was plausible.** Line endings are the kind of fact nobody checks because it has been true
before: this repository has a whole lesson about `git status` overstating a diff for exactly this
reason ([[line-endings-make-git-status-overstate-what-changed]]). The false claim was in the shape
of a true one the corpus already carries.

# The rule that comes out of it

**Measure the sentence you would not have thought to question.** In a report that is mostly measured,
the unmeasured line is invisible by contrast — every neighbour carries a number, so the reader's
guard is already down when the one without a number arrives.

This is the same class as [[a-claim-asserted-from-prose-rather-than-from-the-file]] and
[[generated-text-can-lie-about-the-mechanism-that-generates-it]], with one addition: **the
believability is produced by the surrounding accuracy**, so a more careful agent makes this failure
harder to see rather than less likely.

## It paid twice in one session — 2026-08-18

**Once as a confirmation.** Before the librarian returned on rule 10, the same detector was run
independently against filenames: **13 firing, 7 answered, 6 real**. The librarian came back with the
identical split, derived separately — two instruments agreeing, which is the only reading of a
subagent's report that is worth anything ([[measurement-settled-what-argument-could-not]]).

**Twice as a correction.** The same habit caught a glob that covered one of the three files it
claimed ([[moving-a-rule-into-claude-rules-with-a-paths-scope]]) and dissolved the "23 inbound
links" price that had travelled through three pages unchallenged
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]], [[a-page-rename-is-sed-and-verify]]).

**The asymmetry is the point.** Confirming cost one command; the two corrections each cost one
command as well, and each was on a sentence that read as the most solid line in its report.
