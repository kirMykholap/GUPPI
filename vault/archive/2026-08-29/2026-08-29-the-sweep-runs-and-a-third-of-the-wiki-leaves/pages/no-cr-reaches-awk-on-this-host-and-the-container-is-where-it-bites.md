---
title: "No carriage return reaches awk on this host, which makes a real defect invisible here and live in the container"
type: lesson
status: archived
authority: awk-text-mode-asymmetry
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check.sh", ".gitattributes"]
tags: [harness, testing, vault]
---

# The measurement

**GNU Awk 5.4.0 under this shell reads CRLF in text mode.** Fed a file whose bytes are
`  - title\r\n`, it reports `length($0) == 9`, not 10, and an unpatched loader printed `title` with
no trailing carriage return.

**So every `sub(/\r$/, "")` in `scripts/vault-check.sh` is inert on this machine** — including the
one the page pass carries with a comment explaining why it is needed.

# Where it is not inert

**The container.** These scripts also run under `docker compose`, on Linux, where `gawk` reads the
bytes as they are. That is the same asymmetry `.gitattributes` already pins `*.sh` for, in its own
words: *"CRLF ломает строку запуска… и даёт no such file or directory на entrypoint"*.

**A defect invisible on the host and live in the container is worse than one that fires
everywhere**, because the host is where every check is run and every measurement is taken. It also
explains why the page pass's guard looks like superstition from here — it is a guard against a
platform this machine is not.

# What it corrected about the session's own claim

**The two schema loaders were reported as a latent defect left alone**, on the reasoning that the
`*.yaml` pin made them unreachable. **Both halves of that reasoning were wrong in different
directions**: they were unreachable *on this host* for an entirely different reason, and they were
**never** unreachable in the container.

**The pin is still right and the fix is still right**
([[the-yaml-class-is-pinned-to-lf]]). What is corrected is the argument, and correcting an argument
that reached a correct conclusion is worth the line — the next reader inherits the argument, not the
conclusion ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

# The habit

**A guard whose absence you cannot demonstrate is not thereby unnecessary.** Before deciding a
`\r` strip is dead code, ask which platform the question is being asked on — this store has met that
character on at least four occasions and each time on a different mechanism
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[line-endings-make-git-status-overstate-what-changed]],
[[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).
