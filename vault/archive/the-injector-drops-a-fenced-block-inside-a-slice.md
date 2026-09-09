---
title: "The injector drops a fenced block inside a `<!-- text -->` slice and still reports success"
type: concept
status: deprecated
authority: injector-fence-defect
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh"]
superseded_by: [[a-fenced-block-inside-a-slice-survives-into-the-destination]]
tags: [harness, testing, vault]
---

# The defect, proved on an isolated copy

**A slice of three lines rendered as one, and the injector printed `1 region(s) rewritten, 0
problem(s)`.** The two lines lost were a fenced code block. Nothing was reported, and rule 12 then
agreed with the truncated region, so the gate was green over text the page does not carry.

**The cause is two lines in the wrong order.** Both extractors in `scripts/vault-inject.sh` open with

```
/^```/ { inb = !inb; next }
inb    { next }
```

before the rule that accumulates slice content. So a fence inside the slice toggles the flag and every
line between the fences is skipped along with the fences themselves.

## The stripping is right and its scope is wrong

**Fence-stripping exists so that a documented example of a marker is not read as a marker.** Without it,
this page, the vault's `CLAUDE.md` and the check's own header would each report the harness broken for
describing itself — and that pass has two recorded scars of the inverse error already
([[an-example-inside-a-code-block-satisfies-a-search]], [[a-region-is-a-paired-comment-named-for-a-rule]]).

**What it should gate is marker *recognition*, not content *copying*.** A fence must stop `<!-- text -->`
inside it from opening a slice; it must not stop the lines of an already-open slice from travelling.
Those are two different questions and one flag is answering both.

## What it blocks today

**The by-hand `rg` recipe in the repository's `CLAUDE.md` cannot become a rule page.** It is a fenced
block, so it would render as nothing — and it therefore stands as unsourced prose in a section that is
otherwise rendered ([[the-repository-claude-md-after-the-rules-left-it]]).

**No existing test would have caught this**, because no rule ships a code block yet. It was found by
hand-probing the mechanism rather than by the suite
([[hand-probe-a-new-mechanism-before-running-the-suite]]).

## What the fix owes

Gate recognition on the fence and let content through, plus **two selftest cases**: a slice carrying a
fence renders it, and a marker inside a fence inside a slice does not close the slice. The second is the
one that keeps the original reason intact.

**Deferred, with the cost stated** ([[what-the-harness-build-waits-on]]). Until it lands, this is a
silent truncation rather than a refusal, which is the failure class this project has recorded most —
a green that examined less than it appeared to
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
