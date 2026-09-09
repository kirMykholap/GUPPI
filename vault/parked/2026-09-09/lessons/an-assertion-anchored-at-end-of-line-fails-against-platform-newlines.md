---
title: "An assertion anchored at end-of-line fails against platform newlines"
type: lesson
status: current
authority: crlf-anchored-assertion
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/hook-selftest.ps1"]
tags: [testing, harness, process]
---

# The incident

**A selftest case reported a miss against a mechanism that was already correct.** The assertion
anchored its match at end-of-line, and in a CRLF file the end-of-line anchor sits after the carriage
return — so the pattern was looking for the text immediately before a position that always has a
`\r` in front of it.

**The mechanism was right and the instrument was wrong**, which is the expensive direction: the
session spent the time on the subject rather than on the test.

# The family

**This project pins file classes rather than arguing about newlines**
([[the-yaml-class-is-pinned-to-lf]], [[a-file-class-is-pinned-after-it-costs-something]]). That
settles what is on disk; it does not settle what a pattern written on this platform assumes.

# The rule

**An assertion about the end of a line matches the line's content, not the file's bytes.** Trim
before you anchor, or anchor at something the platform does not decorate.

# The same fact on the writing side, and it puts the carriage return inside a filename — 2026-08-31

**`pathlib.write_text` translates `\n` to `\r\n` on this host unless it is handed `newline="\n"`.** A
list of paths generated for `bash scripts/vault-archive.sh` was written without it, and the archiver
refused the first entry with `no such file` — **the `\r` was inside the name**, not after it. Caught by
a refusal on the first item rather than by anyone reading the file, which is the archiver working as
designed.

**A file class pinned in `.gitattributes` does not reach this.** The LF pinning settles what is on disk
in the repository; a file the repository *generates and never commits* is outside it entirely, and so
is anything a script hands to another script through a pipe.

**A third mechanism, same fact, and it produced a false negative.** Piping a Python script's `--slugs`
output into `comm` on this host compared `slug\r` against `slug` and returned an **empty intersection
where five entries existed**. An empty result from a set operation reads as a clean answer, which is
the direction that hides a defect.

**So the rule generalises past the reading side: a generated line carries whatever the writer
decorated it with, whoever the writer was.** Name the newline where a line is produced, not only where
it is matched.

*(Extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
