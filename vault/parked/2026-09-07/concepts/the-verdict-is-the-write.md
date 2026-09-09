---
title: "Writing the page is not a step after the verdict — the verdict is the write"
type: concept
status: current
authority: verdict-semantics
basis: human
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", "scripts/vault-coverage.sh"]
tags: [vault, process]
---

# `page:X` is a claim that the content landed in X

When the librarian writes `page:X` against a source line, **it must create or update X in that same
act.** The verdict is not a plan to compile the unit later and not a note that X is where the unit
*would* go: it is the assertion that X now says what the source said.

Stated because the opposite reading is available and comfortable — a sidecar can be filled in one
pass and the pages written in another, and every line of it will look exactly the same afterwards.

## The script enforces the weak half and cannot reach the strong half

`scripts/vault-coverage.sh` checks that the named page **exists and is non-empty**:

```
BAD VERDICT <src>:<line>  page:<n> does not exist in the wiki
```

That catches a mistyped name, which is the realistic failure — it turns "compiled" into "lost"
silently. **It cannot check that the page says what the source said.** A verdict naming a page that
exists but never received the claim passes, identifiers and all, exactly as
[[ingest-is-units-and-verdicts]] says of coverage generally: coverage is free, fidelity is not.

So the discipline is the only thing holding the strong half, and the discipline is: **write the
page, then write the verdict.** In that order, the verdict is a record of something that happened.
In the other order it is a promise, and [[a-deferred-check-must-be-run-when-its-condition-arrives]]
is this project's most expensive record of what promises are worth.

## `elsewhere:` is the verdict with a hole in it, and it has already opened

`elsewhere:CLAUDE.md` says a claim belongs to a file **the vault does not own and cannot watch**.
`page:` at least names something inside the store, where every rule in `vault-check.sh` applies to
it; `elsewhere:` names a file anyone may cut tomorrow.

**It has happened once, measurably.** The migration of 2026-08-13 filed the language rule's
boundary — *what predates 2026-08-05 stays Russian, do not mass-translate it, do not rename
existing tests* — as `elsewhere:CLAUDE.md`. That file was cut to a map on 2026-08-14 and the
paragraph went with it. For one day the rule existed nowhere: not in the repository, not in the
vault, and the sidecar still reported `INGEST COMPLETE`, correctly, because coverage asks whether a
unit was **accounted for**, never whether the account is still true.
[[the-language-rule-applies-only-to-new-work]] is the page that now holds it. *(Retired on 2026-08-15: the rule is now deferral rather than exemption — [[english-is-the-rule-and-the-russian-past-is-deferred]] — and the successor corrects this very episode: the owner deleted that paragraph **deliberately**, so the verdict was right when written and the text's disappearance was a decision. The hole in the store was the same either way, which is the point this page makes.)*

So: **prefer `page:` where the claim is durable knowledge**, and treat `elsewhere:CLAUDE.md` as a
statement about *today's* division of files. When a rule file is cut, every unit ever filed against
it is owed a re-read — which is what the ingest of 2026-08-14 was asked to do block by block, and
what found this.

**The re-read now has a second legal outcome: *the owner meant it*.** The paragraph above was
deleted on purpose, and a verdict of `elsewhere:` cannot tell a loss from a deletion — nor can any
check here. Seven verdicts point at the repository's `CLAUDE.md` and eleven at the vault's own,
measured at `14d3d51`, and every one of them is a claim with no custodian:
[[the-paragraph-was-deleted-on-purpose]].

What checks fidelity instead is the acceptance run ([[the-acceptance-questions]]) and, since
2026-08-14, the vault being wrong in front of someone using it
([[feedback-is-recorded-in-the-turn-it-is-noticed]]).
