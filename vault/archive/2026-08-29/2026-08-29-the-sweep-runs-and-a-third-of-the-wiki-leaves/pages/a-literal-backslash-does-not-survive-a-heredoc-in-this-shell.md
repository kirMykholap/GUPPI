---
title: "A literal backslash does not survive a heredoc or a non-raw Python string in this shell"
type: lesson
status: archived
authority: backslash-through-a-generator
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, process, testing]
---

# What was measured

**Two carriers ate a backslash in one session, and one of them shipped.**

| written | arrived |
|---|---|
| `Join-Path $repoRoot '.claude\rules'` | `.claude` + CR + `ules` |
| `$root.Replace('\', '/')` | `Replace('', '/')` |

**The file passed `[Parser]::ParseFile` and failed at runtime** with *Illegal characters in path* —
so the guard branch was **silently absent**, which is the exact failure this repository has shipped
before ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]], and the `-replace` defect
already recorded on [[session-hooks]]).

**A parse is not a run.** Syntax survives a mangled string literal; behaviour does not.

# The rule that falls out

**Never write a literal backslash through a heredoc or a non-raw Python string.** Use forward
slashes, which PowerShell accepts in paths, or `[char]92`.

**The same shell ate a heredoc again while the retro file was being written**, which is the reason
this is a lesson about the carrier rather than about one script: the failure is in how text reaches
a file, so it recurs wherever text reaches a file
([[prose-does-not-survive-a-shell-command-string]]).

# Why it is filed beside the measurement lessons

**The defect is invisible at every checkpoint that is cheap.** It is not a syntax error, it is not a
lint finding, and it is not visible in a diff unless the reader is looking at that character. What
catches it is running the thing — which is the argument for hand-probing a mechanism before
believing it ([[hand-probe-a-new-mechanism-before-running-the-suite]]).

## Second instance, same session — 2026-08-20

**`scripts/vault-archive.sh` escaped paths for `sed` and the backslashes were lost writing the
script into the file.** `probe/RUNBOOK.md` became `probe&RUNBOOK&md`, and the tool reported
**cited by 0 page(s)** about nine pages that cite it.

**Caught only because the number was checked against a hand count**, which is the second half of
the lesson: the failure is silent and it fails towards *nothing to do*
([[an-instrument-that-fails-towards-nothing-to-do]]).

**The repair was structural rather than a better escape.** No regular expression sees a path any
more: `grep -F` to find, `awk` `index()`/`substr()` to rewrite
([[a-path-is-never-a-pattern]]). **An escaping problem that has bitten twice is answered by not
needing an escape.**

## Fourth instance, and this one is a backtick — 2026-08-20

**A backtick inside a double-quoted PowerShell string is an escape**, so
`` `bash scripts/vault-check.sh` `` reached the caller as `ash scripts/vault-check.sh`: both
delimiters and the `b` were eaten ([[a-backtick-in-a-double-quoted-powershell-string-is-an-escape]]).
**Three live occurrences, in two hooks, and it fired the one time the lock has ever fired.**

**The class is now four in two sessions** — the heredoc backslash, the `sed` path escape, the
`$'\r'` grep ([[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]]), and this one.
**Every one failed towards something plausible rather than towards an error**, which is why none was
caught by reading the output.

**And this instance adds a defence the others did not need**, because there is no way to write a
refusal message that needs no escape: **assert the literal command, not the sentence announcing it**
([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]).

# Every multi-line edit of one session went through a channel that halves one level of escaping — 2026-08-21

**The class above bit five times in a single session**, in five different languages, and the common
factor is the transport rather than any one syntax. What reached the files:

- a broken line continuation, which made `sort` read a file named `n`;
- a `printf` carrying a real tab and a real newline instead of the escapes for them;
- `IFS=$'<TAB>'` where the escape for a tab was meant;
- a PowerShell character class holding a path separator, which is not a valid regular expression —
  reported by PowerShell as a caught exception, so the census it guarded read *could not read* and
  every registration looked absent;
- **an awk program left calling a function that had never been inserted — which the gate then ran,
  and exited 0** ([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).

**The remedy that worked: build every literal from a character code and assert the match count
before writing.** Not *escape more carefully* — the same instruction that had already failed four
times that day ([[knowing-a-rule-is-not-a-mechanism]]).

**It bit once more at the end of the session, on the heredoc writing the retro file**, which is the
same channel this page was written about ([[prose-does-not-survive-a-shell-command-string]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# It bit again on 2026-08-23, on the same channel and the same artefact — the retro file

**A long heredoc failed on backslashes while writing the retro file.** That is the second time this
page's closing sentence has had to be written about the same file: the run of 2026-08-21 ended the
same way, on the same channel.

**Nothing new is learned about the mechanism and that is the finding.** The remedy this page
already prescribes — build every literal from a character code and assert the match count before
writing — was available and was not used, which puts this with the apostrophe as a rule that keeps
being known rather than applied ([[knowing-a-rule-is-not-a-mechanism]],
[[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]).

**The pattern worth naming: it is always the last artefact of the session.** Both instances are the
retro file, written when the session is longest and the heredoc is longest with it.

# A third instance, 2026-08-24, and this one landed inside the file being written to catch it

**A patch script delivered through a shell heredoc turned `\n` inside a Python string literal into a
real line break**, producing an unterminated string in `scripts/session-dialogue-selftest.py` — the
file being written to hold the fence reader that this class of failure keeps breaking.

**The repair that generalises is naming the newline: `NL = chr(10)`.** It is the same remedy this
page already prescribes, applied to the one character that a heredoc, a shell string and a Python
literal each claim the right to interpret. **A named character survives however many layers of
quoting the content passes through**, and nothing else measured here does.

**The instance count matters more than the instance.** The "a tool ate what I wrote" family fired
**six times in one session** while it was being used as the worked example for why it needs a rule:
`grep -lit` with a `-t` that is not a grep option; Python printing Cyrillic to a cp1252 console
([[windows-console-encoding]]); `/tmp` written by Python, which bash maps and Windows does not
([[a-path-is-resolved-by-the-program-that-opens-it-not-by-the-shell-that-launched-it]]);
`echo` collapsing a doubled backslash into invalid JSON for a hook payload; the same `/tmp` again;
and this one.

**The fix the lessons collector should propose for this family is exactly "file content is written
with the Write tool, never through a shell"**, and this is its sixth witness
([[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]],
[[prose-does-not-survive-a-shell-command-string]]).
