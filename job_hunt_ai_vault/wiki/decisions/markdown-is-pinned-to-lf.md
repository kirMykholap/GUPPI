---
title: "Markdown is pinned to LF, and the rule was not widened past it"
type: decision
status: current
authority: line-ending-policy
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", ".gitattributes"]
tags: [process, vault]
---

# Decided 2026-08-16: `*.md text eol=lf`, and nothing else

`.gitattributes` had pinned exactly one pattern, `*.sh text eol=lf`, written for the container's
entrypoint. It gained a second on `5e864f1`: **`*.md text eol=lf`**.

**Why LF and not CRLF.** `*.sh` is already LF; the index was already LF everywhere; and the vault's
tooling is `awk` and `bash`, on the host and in the container alike. Pinning to the form the tools
already read costs nothing, and pinning to the other form would have rewritten the index.

**Rejected: widening the rule to `*.py` and `*.html`.** `tests/` holds parser fixtures, and their
bytes are not changing inside a commit about line endings. The narrower rule is the one whose blast
radius can be stated.

## What the measurement said before the change

Working copy at `86823e3`, by extension, CR-containing against pure-LF:

| extension | CR-containing | pure LF |
|---|---|---|
| `md` | 97 | 64 |
| `py` | 89 | 8 |
| `sh` | 5 | 1 |
| `html` | 16 | 0 |

**The split is repo-wide and not a property of markdown** — which is the reading that stopped the
rule being widened on the spot rather than the one that argued for widening it. Five vault scripts
sat at `w/crlf` under `attr/text eol=lf` and git said nothing about them.
`docker-entrypoint.sh` was `w/lf`, so the container was never at risk.

## The commit was one file, not the number the deferral was priced at

The deferral this discharges was priced as *"one commit that rewrites 59 files and nothing else"*
([[line-endings-make-git-status-overstate-what-changed]], and finding #4 of
[[the-audits-findings-are-owed-to-the-owner]]). **Measured at `86823e3` before doing it: all
161 tracked `.md` were already `i/lf` in the index**, so the commit changed exactly one file,
`.gitattributes` itself. The 52-against-59 split that produced the estimate was **the working copy
only** and had never reached a blob.

Why a working-copy difference can keep `git status` red without ever reaching a blob is the
mechanism rather than the decision: [[the-stale-stat-cache-behind-git-status]].

## What it obliges

**`.gitattributes` is still unpinned itself**, so it warns on its own commit. That was left alone
deliberately — it is outside the scope of the finding it belongs to — and it is one row of
[[structure-work-agreed-and-not-executed]].

## The pattern the rule does not cover, noticed 2026-08-17

**`*.coverage.tsv` is not pinned.** The sidecars are read by `vault-coverage.sh` exactly as the
pages are read by `vault-check.sh`, and they have already been bitten once: git rewrote every
sidecar to CRLF on a checkout, `journal` became `journal\r`, and **317 of 411 verdicts across three
sources turned into `BAD VERDICT` lines** — the gate went red on a line ending
([[line-endings-make-git-status-overstate-what-changed]], [[vault-scripts]]).

**The script now strips a trailing CR from both fields**, so the damage is mitigated in code rather
than in git. That is the weaker of the two places to fix it: the strip is one script's defence, and
the next tool to read a sidecar starts without it.

**Not widened here.** The rejected widening above was argued on blast radius, and this pattern was
not on the table when the decision was taken — extending a decision is not an ingest's act. Recorded
so that the next edit to `.gitattributes` has the case in front of it.

## Widened on 2026-08-17, and the rule for widening is now written down

**`*.ps1` and `*.json` were pinned**, after an edit script's LF anchors matched nothing in a CRLF
file. The decision above is untouched by it: the widening it rejected was to `*.py` and `*.html`,
and those are still unpinned on the same blast-radius argument. What is new is the general form —
**a file class is pinned after it costs something, never before** —
[[a-file-class-is-pinned-after-it-costs-something]], where the measured outcome of that day is
recorded.

`*.coverage.tsv` is still unpinned, and the section above is still the reason it is only recorded.
