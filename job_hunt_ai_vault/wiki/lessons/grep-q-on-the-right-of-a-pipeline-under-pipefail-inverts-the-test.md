---
title: "`grep -q` on the right of a pipeline under `set -o pipefail` inverts the test it is written to make"
type: lesson
status: current
authority: pipefail-grep-q
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh"]
tags: [harness, testing, process]
---

# The failure

**`grep -q` exits on its first match.** The process upstream of it in the pipeline is then writing into
a closed pipe and dies of `SIGPIPE`. Under `set -o pipefail` the **pipeline** reports that failure, so
the whole test comes back false **exactly when the pattern matched**.

```sh
# reads as "if nothing matched, refuse"; actually refuses whenever something DID match
if ! printf '%s\n' "$candidates" | sed -n "$expr" | grep -q .; then
    refuse "selection matched nothing"
fi
```

**Written into `scripts/vault-archive.sh` as the empty-selection refusal**, it fired on every substring
that *did* match, and passed silently on the one case it existed for.

# How it was caught

**By running the case, within a minute.** The refusal was built with its own selftest case in the same
change, and the case is what said so — not review, not reading it back
([[a-planted-offender-is-proved-by-reading-it-back]]).

**Nothing about it is visible in the source.** The two constructs are correct on their own and the
interaction is invisible unless you already know it; `shellcheck` does not warn about it either.

# The repair, and where it generalises

**Collect the output and test it, or take the exit code off something that reads its input to the
end.** What must not survive is a short-circuiting consumer at the right-hand end of a pipeline whose
status is being asked under `pipefail`.

**The class is wider than `grep -q`:** `head`, `read`, and any consumer that stops early do the same
thing to the process feeding them.

**The code carries the reason and this is the lesson.** A comment in the script explains the fix to
whoever reads that line; it does not reach anyone writing the same shape somewhere else, which is what
a page here is for ([[a-boundary-stronger-in-prose-than-in-code]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
