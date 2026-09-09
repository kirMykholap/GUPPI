---
title: "A carriage-return census of the working copy, one advisory line per file, behind `--lint`"
type: proposal
status: current
authority: working-copy-byte-census
basis: measurement
sprint: S3
created: 2026-08-26
decided_by: [[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".gitattributes", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# What it would be

**One advisory line per file carrying CR bytes in the working copy**, printed by
`bash scripts/vault-check.sh --lint`. Not red, not a refusal: a census of bytes that are on disk and
that no existing instrument reports.

# Why nothing reports them today

**The `.gitattributes` LF pin keeps every committed blob clean, and `git status` stays silent about
the working copy.** That is the pin working as designed
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]],
[[markdown-is-pinned-to-lf]]) — and it is exactly why a defect that lives in the working copy is
invisible to every check this repository runs.

**Measured 2026-08-26: 95 of 896 tracked text files carry CR bytes — 22,651 in total. One vault page
is among them.**

**A carried sprint item already names eight vault `.md` files as CRLF on disk** and routes the
question to `/vault-lint`; this proposal is the instrument that item has never had.

# What it is for, and it is diagnosis rather than prevention

**It is the route the owner chose for the Python round-trip incident** rather than a third net
([[file-content-is-written-with-the-tool-and-never-through-a-shell]],
[[a-file-round-tripped-through-pythons-text-mode-loses-a-literal-carriage-return]]). A census will
not stop a rewrite; it makes the aftermath legible, and 1553 added CR bytes in one file would stand
out against a baseline.

# What is open

- **The counting instrument itself is a known trap.** `grep -c $'\r'` returns the file's line count,
  not the CR count, and it has already been used to contradict a correct claim
  ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]).
- **The advisory must sort what it names**, or an unchanged tree prints changed output
  ([[an-advisory-prints-one-line-and-sorts-what-it-names]]).
- **95 lines is a lot of advisory.** Whether the useful form is per file, per class, or a single
  total with a threshold is undecided, and the standing risk is that an always-firing advisory stops
  being read ([[the-tag-density-advisories-move-behind-lint]]).
- **What a session should do about a flagged file** is unstated. On a host where no CR ever reaches
  `awk`, the defect is invisible here and live in the container
  ([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]).

# Its `decided_by:` will need re-pointing

**It names the decision that created the collector**, because no per-topic ruling existed when it
was filed. The ruling that routes the round-trip diagnosis here
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]) is the closer cause and is
where the field goes when the build is authorised.
