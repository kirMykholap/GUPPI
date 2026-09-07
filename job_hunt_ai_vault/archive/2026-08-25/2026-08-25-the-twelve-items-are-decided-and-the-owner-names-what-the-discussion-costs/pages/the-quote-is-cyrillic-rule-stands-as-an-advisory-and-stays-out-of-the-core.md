---
title: "The quote-is-Cyrillic rule stands, its verdict is an advisory, and it stays out of the core"
type: decision
status: deprecated
authority: quote-language-verdict
binding: prohibition
basis: human
sprint: S2
superseded_by: [[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]
decided: 2026-08-21
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", "scripts/vault-check.sh"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-21

> **owner: окей, но не применимо например для случая когда цитата будет на английском. То есть
> правило не универсальное. Я бы оставил, но это точно не может быть CORE, так как слишком
> специфично**

Said of the rule proposed that day: **a block attributed to the owner is written in his own
Russian, and a `vault-check.sh` verdict says so when it is not.** Three things were decided in one
sentence.

**It stands.** The rule is kept rather than dropped for being imperfect.

**Its verdict is an advisory, not red.** A genuine English quotation from the owner exists as a
case, so a red verdict would fire on a correct page. The precedent was named at the time and the
shape already exists here: the filename half of the title rule is an advisory while the title half
is red ([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

**It does not enter the core of the repository's `CLAUDE.md`** — too specific for a file whose
admission test is *what bootstraps the asking, and what is irreversible if missed*
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]).

**Rejected: a red verdict**, on the owner's own counter-example.

# What the verdict can and cannot decide

**An alphabet separates a quotation from a paraphrase. Nothing mechanical separates a faithful
paraphrase from a wrong one**, which is why this rule is paired with a step that puts every
attributed line to the owner before it is written down
([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]).

**English does not prove he did not say it.** Measured the same day: 53 owner-attributed quote
blocks across 44 `wiki/` pages, 25 of them carrying no Cyrillic — and **none of those 25 is in his
words**, which is a reading of the pages rather than something the count proves
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

# It is not built

**Nothing enforces this today.** The rule page, the advisory verdict and its cases are designed and
unbuilt, and the owner set them first in the order of the next session's work
([[a-quote-is-cyrillic-rule-with-an-advisory-verdict]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# It is built, and the advisory prints behind `--lint` — 2026-08-22

**The section above says *"It is not built"*. That stopped being true on this date**, and the
sentence stands as written: it is a true statement about the day it was made
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**Both halves landed.** The rule page is
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]], governing
`.claude/skills/handoff/SKILL.md` and `.claude/skills/ingest/SKILL.md`; the verdict is rule 14 of
`scripts/vault-check.sh`, an advisory exactly as ruled — it prints and never changes the exit code
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

## The channel is `--lint`, and that is a decision of this date rather than a detail of the build

**Behind the flag, not on a bare run.** 27 owner-attributed blocks carry no Cyrillic today, and every
one of them would print on every bare run until the ratification sweep that reads them happens —
**and that sweep waits on the owner**, because the instruction that came with the list is to act only
on what he disowns.

**The finding is a statement about the corpus's history, not about the run in front of you**, which
is the same distinction that moved the tag-density advisories behind the flag and took a bare run
from twenty-one advisories to one. That precedent was named when the choice was made
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]],
[[the-tag-density-advisories-move-behind-lint]]).

**Rejected: a bare run naming all 27**, which trains the reader to skip the advisory block; and
**rejected: a bare-run counter with the list behind the flag**, which keeps a number nobody can act
on in front of every run and splits one finding across two invocations.

## The shape of the output, and it is not free-form

**The count is on the first line and the names are one per line after it** — `path:line`, sorted. A
reader greps the first line for the number and reads the rest as a list, and no name has to be split
out of a sentence. That is the shape the filename advisory already settled
([[the-filename-advisory-prints-one-name-per-line]], [[a-stated-count-drifts-from-the-list-it-heads]]).

## The reader is bytes, and the page carrying the measurement says why

**A `grep` with a Cyrillic character class reported this corpus's split reversed and agreed with
itself across two runs.** The verdict reads UTF-8 lead bytes instead, built under `LC_ALL=C` so no
locale can reinterpret them, and it was proved on planted input before it was wired in
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]],
[[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).

## Raised and not done: the design page is now retirable

**[[a-quote-is-cyrillic-rule-with-an-advisory-verdict]] closes with *"retired with `superseded_by:`
the day it is built or refused"*, and it was built today.** Retiring a proposal is the owner's, and
it is raised here rather than executed ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]],
[[proposals-are-a-folder-not-a-status]]). **One thing on it does not yet live anywhere else** —
whether a paraphrase is demoted to `basis: inference`, offered at the retro and neither taken nor
refused ([[a-question-asked-is-not-a-question-answered]]).

# Retired 2026-08-25 — the middle clause was overturned by the owner

**The verdict is cancelled**, on his ruling that Cyrillic does not mean the words are his
([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]). The rule this page kept —
a block attributed to the owner is written in his own Russian — is untouched, and what replaces the
mechanical predicate is the ratification step in `/retro`.

**Everything above stands as written**, dated to the days it was written on.
