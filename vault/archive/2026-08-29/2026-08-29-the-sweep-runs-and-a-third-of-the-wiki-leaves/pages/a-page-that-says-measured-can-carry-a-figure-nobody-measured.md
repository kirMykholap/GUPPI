---
title: "A page that says measured can carry a figure nobody measured"
type: lesson
status: archived
authority: measured-claim-unmeasured
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md"]
tags: [vault, testing, process]
---

# Two of them on one page, in one session, and both fell to one command

**`tests/unit/*boundary*.py`, recorded as "six files, measured".** Six files do match the glob. The
set the AST rule exists to protect is the files importing `_ast_boundary`, and there are **three**;
the glob reaches **one** of them, because two are spelled `boundaries` and the pattern demands
`boundary`. One `ls` ([[moving-a-rule-into-claude-rules-with-a-paths-scope]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]).

**"23 inbound links", carried as the price of the worst rename.** It does not reproduce at any
commit checked. One `grep` ([[a-page-rename-is-sed-and-verify]]).

# Why the word *measured* is the aggravation rather than the defence

**A figure labelled measured is not re-measured.** It reads as provenance, it is quoted verbatim by
the next reader, and it travels: the 23 went from a `miss:` line into two decision pages and
`index.md` without anyone counting, and the glob went into a table headed *Measured*.

**Both were measured — of the wrong thing.** Six files really do match that glob; the mistake is
that matching the glob was not the question. That is the failure mode: the number is honest and the
predicate under it was never stated, so nothing about the number can reveal it
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]],
[[a-claim-asserted-from-prose-rather-than-from-the-file]]).

# The cheap defence, and it is the same one twice

**Run the command beside the claim.** Both defects cost one command each and both were found by a
reader who ran it instead of quoting the page — the same habit that pays on a subagent's report
([[a-subagents-most-believable-sentence-is-the-one-to-measure]]).

**Write what was counted, not only how many.** *"Six files match `tests/unit/*boundary*.py`"* is
checkable and would have been checked; *"six files, measured"* is not a claim about anything in
particular. The store already requires the number to carry its conclusion
([[an-unsourced-number-is-dropped-not-chosen]]); this adds that it must carry its predicate.
