---
title: "A selector written for one discharge shape cannot see a new one, and it fails by selecting less"
type: lesson
status: current
authority: selector-blind-to-a-new-discharge
basis: code
sprint: S3
created: 2026-08-31
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# The incident, 2026-08-31

**`bash scripts/vault-archive.sh --sweep` does not select a discharged prohibition.** Its `decisions/`
selector takes `status: deprecated`, `binding: divergence`, `status: processed`, and slugs named in
some page's `decided_by:`. **A rule page's `decided_by:` names exactly one decision** — the gate
reddens any other shape — so a family of fourteen prohibitions discharges **one** page through that
arm.

**About 57 of 293 would have moved.** The remaining ~236 needed named batches, and named mode exits 2
on the first refusal, so the run was done as a `--dry-run` first — which collects refusals and moves
nothing — and then as named batches. **129 pages moved.**

# The class

**A selector is an opinion about what may leave, and a new way of discharging a page does not add
itself to that opinion.** The family rule is a discharge shape that did not exist when the selector was
written: one live page carrying the clauses of many decisions, linked from each clause but named in
`decided_by:` only once.

**It fails in the safe direction and that is why it is easy to miss.** Selecting too few reads as
*nothing qualifies today*, which is a legitimate answer on most days. Selecting too many would have
moved live constraints out of the reader's reach and been caught in the same minute.

**The refusal machinery worked exactly as designed and did not help.** `--dry-run` collects refusals
and the archiver refuses per page, so every page it was *given* was judged correctly. Nothing in the
design asks whether the right pages were offered.

# What follows

**When a new discharge shape is ratified, the selector is part of the change.** Otherwise the sweep
goes on being run and goes on reporting a small number, and the gap is discovered by somebody counting
by hand.

**A batch list is generated with an explicit newline.** The first attempt wrote the path list with
`pathlib.write_text` and no `newline="\n"`, so Python translated the endings and the archiver refused
the first file with `no such file` — the carriage return was inside the filename
([[an-assertion-anchored-at-end-of-line-fails-against-platform-newlines]]).

**This sits against, rather than contradicts,
[[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]]**, whose claim is that the sweep
inherits refusals instead of acquiring an opinion. **Its refusals are inherited; its selection is an
opinion**, and that is the half the page does not cover.

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
