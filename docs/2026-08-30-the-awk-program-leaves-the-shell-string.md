---
title: "The awk program leaves the single-quoted shell string and becomes a file"
type: proposal
status: current
authority: awk-program-delivery
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["job_hunt_ai_vault/raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/rules/_schema.yaml"]
tags: [harness, testing, vault]
---

# What it would be

**`scripts/vault-check.sh` stops passing its awk program as a single-quoted shell argument and
passes it as `awk -f <program-file>`.** The program moves to a file beside the script — one file,
read by awk, never parsed by the shell and never counted against the argument list.

**The same move is owed to `scripts/vault-inject.sh`**, which carries the second awk program in this
repository and has never carried the apostrophe warning the check has
([[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]], [[vault-scripts]]).

# The two failures this answers, and why they are one proposal

**They came from one comment block, an hour apart, on 2026-08-30.**

- **The size limit.** 1.7 KB of comments added inside the embedded program pushed the argument past
  the per-argument size limit. `xargs` printed `cannot fit single argument within argument list size
  limit` **to stderr only**, the frontmatter pass produced nothing, and `vault-check.sh` went on
  exiting 0. The one visible symptom was all twenty registered tags reported as used on no page,
  which reads as a corpus problem and is not one. `vault-check-selftest.sh` run in that state
  reported **caught 162, missed 49** — forty-nine red cases passing by default.
- **The quoting.** An apostrophe in a comment inside the same block closed the single quote and the
  next backtick became a command substitution. Loud, and fixed in minutes.

**One carrier produces both.** The single-quoted string is what makes prose in the program the
shell's business at all, and it is what makes the program's size an argument's size. `awk -f`
removes the carrier rather than defending against each failure separately.

# The headroom, measured

| reading | bytes in the program region |
|---|---|
| at `0da5e96` | 78,516 |
| after this session | 79,149 |
| fails on this machine | 82,425 |

**Under four kilobytes of headroom before this session, and nothing measured it.** The limit is a
property of the platform, the program only grows, and the failure is silent in the direction that
gets published.

# What it would take

- Move the program region of `scripts/vault-check.sh` into a file and invoke it with `awk -f`.
- Do the same for `scripts/vault-inject.sh`.
- Delete the *no apostrophes below this line* warning from both, because the hazard it names is
  gone rather than merely known ([[knowing-a-rule-is-not-a-mechanism]]).
- Re-run `scripts/vault-check-selftest.sh` whole and compare the caught/missed pair against the
  last clean reading. **A green run is not the acceptance test**; the count is.

# What is open

- **Whether the sandbox copy list needs the new file.** A gate rule that runs a script is coupled to
  the suite's sandbox copy list, and the coupling is total
  ([[a-gate-rule-that-runs-a-script-is-coupled-to-the-suites-sandbox-copy-list]]). A program file the
  copy list does not know about turns every case red at once.
- **Whether the check's `--lint` and `--rules` modes select different programs**, which decides
  whether this is one file or several.
- **What the selftest asserts about the new shape.** The repair landed today is a case asserting the
  gate writes nothing to stderr; that case is about the symptom and stays useful either way.

# What it would oblige

**A silent pass becomes impossible to reach by growth.** Today any author adding a paragraph to a
comment can disarm the frontmatter pass without a verdict firing, and the store has no instrument
that measures the distance to that cliff.

**The stderr assertion stays regardless.** It is the general guard — a gate that writes to stderr and
exits 0 is a gate that stopped checking — and it is cheaper than knowing where every limit is.

# What this does not cover

**It does not repair `bash -n` not being run.** That is the other half of the apostrophe class and it
already has a design: the second net of
[[a-pretooluse-net-for-a-shell-write-and-a-syntax-check-after-a-script-edit]], unbuilt since
2026-08-26. This proposal removes the hazard; that one catches the next author.
