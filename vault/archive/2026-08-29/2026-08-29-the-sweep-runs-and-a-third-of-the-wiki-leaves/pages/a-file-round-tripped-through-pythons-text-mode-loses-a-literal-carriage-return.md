---
title: "A file round-tripped through Python's text mode loses a literal carriage return, and the gate it corrupted still passes `bash -n`"
type: lesson
status: archived
authority: text-mode-round-trip
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# What happened, 2026-08-26

**A helper script written to prove the new guards read and rewrote `scripts/vault-check.sh` with
`read_text` / `write_text`.** Text mode converts every lone `\r` to `\n` on read and every `\n` to
`\r\n` on write.

**The file carries three literal CR bytes inside three awk regexes whose job is to strip carriage
returns.** All three became line breaks, and the gate went red with `awk: unexpected newline`.

**Damage: 1553 CR bytes added and three bytes destroyed.** The three destroyed are the whole of it;
the 1553 are noise the LF pin would have hidden at the next commit
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

**Not broken before this session** — verified by stashing the session's changes and watching the
gate exit 0, rather than assumed from the diff. Repaired by restoring from git and re-applying both
edits by hand.

# The part that matters is that no cheap check would have caught it

**`bash -n` passes on the corrupted file**, verified. So the syntax net that the shell-write proposal
offers as its second half would have said nothing here
([[a-pretooluse-net-for-a-shell-write-and-a-syntax-check-after-a-script-edit]]).

**And the corruption is invisible to a reader**: the file looks right, the diff is 1553 line
endings, and the three bytes that matter are three characters inside three regexes.

# The class, and where it is filed

**"File content passed through an intermediary that rewrote it" is one class**, and this repository
already had six members of it — heredoc, apostrophe, `sed`, `grep`, backslash, `TMPDIR`
([[prose-does-not-survive-a-shell-command-string]],
[[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]). This is the seventh, and it arrived
**through Python rather than through a shell**, which is what the ruling of the same day had to be
scoped against ([[file-content-is-written-with-the-tool-and-never-through-a-shell]]).

**No third net was invented for it** (owner, 2026-08-26). The written rule stays narrow — the shell
— and the diagnostic half is carried by the CR-byte census
([[a-cr-byte-census-of-the-working-copy-behind-lint]]). **So this lesson names a hole that is open on
purpose**, which is the honest state rather than a gap nobody noticed.
