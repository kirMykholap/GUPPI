---
title: "A region is a paired HTML comment named for a rule's slug, alone at column zero"
type: concept
status: current
authority: region-form
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [harness, testing]
---

# The form

```
<!-- rule: some-slug -->
...the rendered text...
<!-- /rule: some-slug -->
```

**Alone on its line, at column zero.** The file owns the skeleton; the page owns the text
([[what-travels-from-a-rule-page-is-a-marked-slice]]). A rule is corrected in one place and
rendered into the file that carries it.

## What rule 11 calls broken

Unclosed; a close with no open; a close carrying the wrong slug; nesting; **one slug marking two
regions in the same file**; a marker not alone at column zero; a region whose
`wiki/rules/<slug>.md` does not exist; and an unterminated code fence. A governed file with no
region at all is an advisory instead ([[a-governed-file-with-no-region-is-an-advisory]]).

## Fenced blocks and inline code spans are stripped before anything is looked for

Otherwise a file **documenting the marker form** — this one, the vault's `CLAUDE.md`, the check's
own header — would report itself broken by quoting the syntax it explains.

The stripping pass already existed and its two scars are exactly this error: prose inside a
`<script>` block satisfying an id search for a slice and a half, and a fenced example link read as
a real one ([[an-example-inside-a-code-block-satisfies-a-search]]).

## An unterminated fence is reported, and that is not tidiness

**A fence opened and never closed swallows every marker below it.** The file would then report
**zero regions rather than broken ones** — it would join the advisory list and read as merely
un-marked-up, which is a state nobody investigates.

Silence that looks like cleanliness is the failure this repository has repeated most: a check that
passes because it examined nothing ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]),
and `vault-check.sh` has printed `ok` having read nothing before now ([[vault-scripts]]).

## Detection and judgement are separate steps

Anything that looks like a marker is picked up; anything that is not exactly the form is named
malformed — [[a-marker-is-detected-loosely-and-judged-strictly]].
