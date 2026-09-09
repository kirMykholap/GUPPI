---
title: "The sweep runs for real over every criterion, and records what it moved in `log.md`"
type: decision
status: archived
authority: sweep-first-run-order
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh", "log.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-29

**owner:** «Он должен не только напечатать список, а и архивировать его. Действия в log.md. Я думаю
что это именно то, что стоит сделать именно сегодня»

**The sweep runs for real on the day it is built**, not as a dry-run list, and it writes its actions
into `log.md`.

**Taken against the session's recommendation**, which was to hold the 240-page move for a separate
sitting on the ground that the vault only *permits* a page to leave and never *obliges* it.

**And it runs over every criterion the four folders have, including `decided_by:`.** He selected that
from three options, again against the session's recommendation — which was to hold the `decided_by:`
criterion back, because it evicts a decision about one ingest as soon as that ingest is taken, and
four rulings from 2026-08-28 were in the list.

**Rejected: holding the move for a separate sitting; and holding the `decided_by:` criterion back.**

# What it obliges

**239 pages moved**, in 5m16s, all marked `status: archived`, with 1 `sources:` citation rewritten and
0 refused. `wiki/` went from 762 pages to 523 — `decisions/` 341 to 276, `lessons/` 182 to 12,
`proposals/` 49 to 45 ([[vault-archive-sh]], [[the-vault-directory]]).

**The gate is green at 24 s afterwards and the register agrees at 507 slugs.**

**A script now appends to `log.md`.** The one-writer clause names the librarian and is written about
agents; **no page said whether a script may append to the log**, and the question surfaced only
because this ruling ordered it. It is settled in the direction the owner then stated in full
([[log-md-is-filled-mechanically-and-rotates-when-the-sprint-closes]],
[[the-steward-is-scripts-that-run-after-the-librarian]]).

**Reading the corpus after it is different work.** Many pages an older page names as a source or a
successor now live in `archive/`; their `[[wikilinks]]` still resolve, because the link check resolves
against `wiki/` and `archive/` alike.

# What the run does not prove

**Zero refusals was predictable and is not evidence.** Every selected page already had a live citer,
by construction for the `decided_by:` criterion, so the continue-past-a-refusal path decided on
2026-08-28 could not fire on this corpus at all. **Its selftest case is the only proof of it**
([[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]]).

**The corpus is a third smaller and the suite is not measurably cheaper.** The gate reads `wiki/`
alone, so its shared pass shrinks; the suite's per-case sandbox copies the whole tree and `archive/`
stays on disk. The suite read 29m12s at 194 cases against 34m08s at 178 cases five days before — three
readings on three days under different load, which is suggestive and is not a controlled experiment.

**What `/pre-task` lost is unmeasured** ([[what-the-pre-task-lost-to-the-decided-by-criterion-is-unmeasured]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
