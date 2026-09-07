---
title: "A comment that quotes the literal a sweep looks for is counted by that sweep"
type: lesson
status: current
authority: sweep-counts-its-own-comment
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The failure

**`--list` finds an inline case in `scripts/vault-check-selftest.sh` by the literal `report "..."`.**
The comment above the sweep explains what it looks for **by quoting exactly that string** — so a case
named `...` appeared in every listing the flag ever produced.

**It had been wrong since the flag was built** and nothing saw it. `--list` reported **182** cases where
the file holds **181**; it now skips comment lines.

# Why nothing caught it

**The file's own header has promised since 2026-08-24 that a case pins `--list` against the number a
real run reports. No such case existed.** The comment asserted a guard that was not there
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

**So the register the comment said was guarded was not guarded**, and the one instrument that would
have caught this was the one the file claimed to have. The case was written on 2026-08-29 and **fired
for the first time, agreeing at 194** ([[vault-scripts]]).

# The general shape

**Documentation that quotes a machine-read literal is inside the machine's input.** A sweep over a file
cannot tell an example of a pattern from a use of it, and neither can `sed` when it rewrites slugs —
the same blindness cost this store two quoted sentences during the rename sweep of 2026-08-19.

**Two repairs exist and only one of them is durable:**

- **Skip the region the literal is explained in** — comments, fenced blocks — which is what was done.
- **Write the explanation so it does not contain the literal**, which relies on nobody restoring it
  later.

**And the durable half is neither: it is the case that compares the count to a real run.** A derived
list is single, not correct ([[a-suite-section-is-derived-from-where-a-case-sits]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# It happened again the same day, to a different instrument, and it is now a family of five — 2026-08-29

**`record-the-smoke.ps1` matches `SMOKE-EXIT:\s*(\d+)` against a command's output, and three live pages
document that marker.** So `cat` of any of them writes a green smoke row for a run that never happened,
and the gate on `/handoff` reads it ([[the-smoke-gate-hooks]]).

**Three false green rows stand for 2026-08-29**, two of them written by a read-only `grep` that was
counting the occurrences — **the defect firing on its own investigation**, from inside a subagent with
no write tool.

**The family is five instances in seventeen days**, and this page is the only one of them still live —
the other three were archived by the sweep of 2026-08-29. **That is the argument for a proposal rather
than a sixth page**: [[an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it]] carries
the family whole and would retire this page.

**It is not retired by this ingest.** The drain of `lessons/` into `proposals/` is itself an unbuilt
design, and retiring a lesson on the strength of a proposal nobody has accepted would be executing it
([[lessons-become-a-queue-drained-into-proposals]]).

**And this page was already `CITED` when it recurred.** The queue counts a citation from outside
`lessons/` as the loop's end state; this page had two such citations and the failure happened again
anyway ([[a-citation-is-not-a-test-in-a-corpus-this-densely-linked]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
