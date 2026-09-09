---
title: "An exit code read through a pipe belongs to the last stage, so it is a measurement only when nothing is downstream"
type: concept
status: current
authority: exit-code-through-a-pipe
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [process, testing, harness]
---

# The mechanism

```
bash selftest.sh | tail -20          # the status is tail's
bash selftest.sh > f; grep SELFTEST f # the status is grep's
```

**Both are 0 whenever the last stage succeeds, which it always does.** `tail` succeeds on any input;
`grep` succeeds on any input that matches. Neither has any relationship to what the subject returned,
and neither reports that it has replaced it.

**So a shell that shows a command's status shows the status of the pipeline**, and a pipeline is
whatever was typed to make the output readable. The reading habit that produces this is not carelessness
about exit codes — it is care about **output**: a long run is piped through `tail` or greppped precisely
because the reader wants the summary line.

# The consequence, which is a false negative in the reassuring direction

`scripts/vault-check-selftest.sh` ends on `[ "$fail" -eq 0 ]`, so **its exit code has always been its
score**. Measured with one case planted broken it returns **1**
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

Read through a pipe it returned 0 at `caught 24, missed 96` exactly as it did at `caught 119, missed 1`,
and a decision was drawn from that — *the exit code does not read the score* — which is false
([[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]]).

**The failure is not that the number is wrong. It is that the instrument answers a different question
and the answer is well-formed**, which is the family this store already holds twice
([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

# The habit that catches all of it, and it is one line

**Capture the status into a variable on the very next statement**, never through `|` and never after a
trailing `grep`:

```
bash selftest.sh > f; rc=$?
grep SELFTEST f; echo "exit=$rc"
```

**A measurement of a command's status is only a measurement when nothing is downstream of it.** The
same rule states the `grep -c`-over-zero-matches case from the other end: a compound command ending in
a `grep` that finds nothing reports the whole task as failed while the number it produced is right.

# The other half of it, found in the same script — 2026-08-19

**This page is about the LAST stage's status being taken for the whole. There is a mirror**: under
`set -o pipefail`, the FIRST stage's **death** is taken for the whole
([[a-quiet-grep-at-the-end-of-a-pipe-reports-a-match-as-a-failure]]).

`grep -q` exits on its first match and closes the pipe; the `printf` upstream dies of SIGPIPE; and
`pipefail` — which exists precisely so a pipeline's status is not the last stage's alone — makes 141
the pipeline's status. **So a match that was found reads as a test that failed.**

**Measured on one output under one `set -uo pipefail`**: piped gives `FALSE (status 141)`,
`grep -q … <<<"$out"` gives `TRUE`. **It sat in nine places in `scripts/vault-check-selftest.sh`**,
one of them failing towards green.

**The habit at the foot of this page still catches both** — capture the status on the very next
statement, never through a pipe — and it gains a companion for the case where the pipe is the
*predicate* rather than the reader: **use a herestring, which is a file descriptor and cannot be
broken this way.**

# It happened twice in one session on 2026-08-23, against a page that already existed

**The first reading of `scripts/vault-check-selftest.sh` reported `exit 0` while the suite exited
1.** The status came through a pipe and belonged to the last stage; the suite's own verdict —
`caught 157, missed 1` — was in the text that had just been read past.

**Recorded again rather than assumed to be covered.** This page has existed since 2026-08-19, it
names the exact habit that prevents it, and the reading was taken anyway. **The correct reading, at
the end of that session, was taken from the command's own invocation and says so in the journal** —
`caught 158, missed 0`, exit 0 — which is the habit working when it is applied
([[vault-scripts]]).

**It is not a coincidence that the pipe hid a `missed 1`.** The dangerous direction of a misread
exit code is the one that reads green, and every instance this store has recorded has failed that
way ([[an-instrument-that-fails-towards-nothing-to-do]],
[[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).

# Four times in one session — 2026-08-23, and the store's own page was cited after the third

**The section above records two occurrences on 2026-08-23. There were four**, in the second session
of that day, and they are not all pipes:

- **`grep -c` printing `0` exits 1**, which broke three `&&` chains. The count was correct and the
  status said failure, because "no matches" is `grep`'s failure condition and a count of zero is
  what that looks like when you asked for a number instead of a match.
- **`bash <suite> | tail -25` reported exit 0 while the suite had `missed 1`** — the pipe case this
  page is named for, and the truncation hid the diagnosis as well
  ([[a-truncated-report-hides-the-line-it-was-run-for]]).

**The page was cited after the third occurrence rather than before the first.** That is the finding
worth keeping: **knowing the page exists is not the mechanism.** A store that holds the answer and a
session that reaches for it are two different things, and only the second prevents anything.

## The same shape without a pipe: a chain that broke and reported success anyway

**A `python -c` failed on quoting, `&&` skipped the `cat` that was to write two feedback lines, and
an unconditional `echo` on the next line printed `recorded.`** Nothing had been recorded.

**The `echo` is the defect, not the failure.** A status line written unconditionally after a chain
reports the *intention* of the chain rather than its outcome — which is the same substitution as
reading a pipeline's last stage: something that always says the reassuring thing stands where a
measurement should be ([[an-instrument-that-fails-towards-nothing-to-do]]).

**The habit that catches both is the one this page already gives**, applied to the write as well as
to the read: the confirmation goes inside the chain, or it is not a confirmation.
