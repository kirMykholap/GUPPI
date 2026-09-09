---
title: "A `PreToolUse` net for a shell write into a tracked file, and a syntax check after any script edit"
type: proposal
status: current
authority: shell-write-net
basis: inference
sprint: S3
created: 2026-08-26
decided_by: [[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [harness, testing, process]
---

# What it would be

**Two nets, and they catch different things.**

1. **A `PreToolUse` branch on `Bash`** matching a heredoc, or a redirect into a tracked text file.
   It would fire before the write, where the content still exists as written.
2. **`bash -n` after any `.sh` edit**, as a cheap syntax net on the file class this repository
   breaks most often.

**Registering the first means a matcher on `Bash` in `.claude/settings.json`** — the same surface
the existing hooks use ([[session-hooks]], [[hooks-in-the-settings-file-apply-inside-subagents]]).

# The family it comes from

**Seven recorded members, six of them found in the lessons queue by the collector and one outside
it**, each a carrier eating what was written:

- [[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]]
- [[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]
- [[tmpdir-is-empty-in-this-shell-so-a-path-built-from-it-lands-at-the-root]]
- [[a-path-is-resolved-by-the-program-that-opens-it-not-by-the-shell-that-launched-it]]
- [[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]
- [[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]]
- [[prose-does-not-survive-a-shell-command-string]] — the anchor outside the queue

# What the family's own newest member says about the design

**The session that this proposal was filed by corrupted `scripts/vault-check.sh` on the same day,
and neither net would have caught it.** The corruption came through Python's text mode, not through
a shell, and **`bash -n` passes on the corrupted file** — verified
([[a-file-round-tripped-through-pythons-text-mode-loses-a-literal-carriage-return]]).

**So this proposal is narrower than the class it was assembled from, and knowingly so.** The owner
ruled that no third net is invented for the Python case and that the diagnosis is carried by the
CR-byte census instead ([[file-content-is-written-with-the-tool-and-never-through-a-shell]],
[[a-cr-byte-census-of-the-working-copy-behind-lint]]).

# What is open

- **The predicate for "a tracked text file".** A heredoc into `/dev/null` or into a scratch path is
  ordinary work, and a matcher that fires on all of them will be turned off — the standing risk this
  store already records about advisories ([[the-tag-density-advisories-move-behind-lint]],
  [[name-only-non-zero-counters]]).
- **Whether it refuses or advises.** This repository has one refusing hook and a recorded rule that
  advisory is not automatically the right default
  ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).
- **Where `bash -n` runs.** `PostToolUse` on `Edit` is the obvious place and is not free; nothing
  measures the current hook budget per edit.

# Its `decided_by:` will need re-pointing

**It points at the decision that created the collector**, because no per-topic ruling existed when
it was filed. The written rule the owner ordered the same day
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]) is the closer cause, and this
field moves to whatever decision authorises the build.
