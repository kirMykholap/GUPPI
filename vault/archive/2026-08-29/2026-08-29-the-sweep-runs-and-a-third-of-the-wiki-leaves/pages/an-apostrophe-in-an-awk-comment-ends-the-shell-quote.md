---
title: "An apostrophe inside an awk comment ends the shell quote and breaks the script at parse time"
type: lesson
status: archived
authority: awk-quote-hazard
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [testing, harness]
---

# What happened

`scripts/vault-check.sh` passes its whole awk program as a **single-quoted shell string**. A comment
written inside that program containing the words *this project's* closed the quote at the
apostrophe. The file stopped parsing — not at run time, at parse time, before any rule ran.

**Caught by `bash -n` in seconds.** That is the whole recovery, and it is why the syntax check is
worth running on a shell script before the suite is.

## The fix is written where the mistake happens

The file now carries a line, immediately above the awk program, forbidding apostrophes below that
point. Not in a document, not in a review checklist, not in a lesson page that someone might grep:
**in the file, at the line where the next author will be typing.**

That is the general form worth keeping: **the fix that cannot be forgotten is the one written where
the mistake happens.** A rule stored anywhere else depends on somebody remembering it exists, and
this project's whole record on that is a list of harness files that went stale with nothing
noticing ([[no-rule-reads-a-harness-file]]).

It is also why a rule that *must* travel gets rendered into its destination rather than cited from
one ([[what-travels-from-a-rule-page-is-a-marked-slice]]).

## The cheap detector

`bash -n <script>` after any edit to a shell script, before anything else. It costs nothing and it
is the only thing that distinguishes *the script is broken* from *the rule is wrong*.

## The general case was diagnosed on 2026-08-17, and it is not about apostrophes

**Eight heredoc constructs were written to files and parsed — all eight parse cleanly.** So the fault is not
the quoting of any one character; it is that **prose travelling inside a shell command string is executed by
the shell it is handed to**. This page is one instance of that; a markdown code span run as a command is
another, and it fired seconds after the first
([[prose-does-not-survive-a-shell-command-string]]).

**The remedy generalises accordingly**: prose is written with the file-writing tool, and a generator reads
its input from a file rather than from an argument. **More escaping cannot help**, which is what the guessed
diagnosis would have produced.

## The warning lives in one of the two awk-carrying scripts, and it is owed to the other

**Measured 2026-08-18: `scripts/vault-check.sh` carries the *no apostrophes* warning in its writer
awk and `scripts/vault-inject.sh` does not.** The separator change of that session edited the one
program without the guard ([[the-injector-writes-the-separator-inside-the-region]]).

**A warning that sits beside one instance of a hazard and not the other is a warning that has been
read as a note about that file.** It is a property of every awk program written inside single
quotes here, and both scripts are that ([[vault-scripts]]). Adding it to the injector's writer awk
is on the harness queue.

# It recurred on 2026-08-22, twice in one edit

**`owner's` and `one's`, written into an `awk` comment inside `scripts/vault-check.sh`**, turned the
gate into a bash syntax error. Two occurrences, one edit, five days after this page was written.

**`bash -n` caught it immediately**, which is the cheap half of the defence and is the whole reason
this cost a minute rather than a debugging session.

**The neighbouring page is about backslashes and this is the same class from another angle**: prose
written through a shell is not prose, and the character that bites is whichever one the quoting layer
happens to own ([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[prose-does-not-survive-a-shell-command-string]]).

**Knowing the rule did not prevent it.** The page existed, it names the exact two words' shape, and
the edit was made anyway ([[knowing-a-rule-is-not-a-mechanism]]).

# It recurred again on 2026-08-23, and this time the page had been cited an hour earlier

**`scripts/vault-check.sh` exited 2 on every invocation until the apostrophe was found.** Same
script, same class, six days after the page and one day after the last recurrence.

**What is new is the aggravation, not the defect.** The session had cited *this page* an hour
earlier that morning, as its reason for choosing `Edit` over `sed` on a different file. **The rule
was not merely known; it had just been acted on** — and the next edit into an `awk` comment carried
an apostrophe anyway ([[knowing-a-rule-is-not-a-mechanism]]).

**That is the third instance and the argument stops being about care.** A defence that has failed
three times while its own page was in front of the party failing it is not a defence. The mechanical
half already exists and is cheap — `bash -n` on the script before running it — and what is missing
is anything that makes it happen rather than be remembered.
