---
title: "`harness:` joins the feedback vocabulary as a kind of its own, rather than the template being corrected"
type: decision
status: current
authority: harness-feedback-kind
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".superpowers/sdd/vault-feedback.md", "job_hunt_ai_vault/log.md"]
tags: [process, vault, harness]
---

# The ruling, 2026-08-19

**`harness:` is a kind of feedback line in its own right** — a change to the files that instruct an
agent, **decided** this session.

**Rejected: amending `.claude/templates/handoff.md`** so that harness items are `process:` lines the
writer routes by hand. That would have folded a **decided work item** into `process:`, which is a
kind for **findings** ([[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]]). The two are
different objects: a finding is something noticed about the ritual, and a harness line is something
already decided about a file.

## What it resolves

[[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]] recorded the mismatch: the
template routed `- harness:` lines to its `Harness` section while the file being drained defined no
such kind, so **the routing named a token that could not appear**. That page said one of the two
documents is wrong and it is not a session's to choose which. The owner chose the file.

## The vocabulary lives in a pair of files and they have to match

**`.superpowers/sdd/vault-feedback.md` has it; `log.md`, the librarian's copy of the same list, did
not** — recorded in the journal's own `Deferred` section as the half left undone. **This ingest adds
it to `log.md`**, and the two lists now name the same kinds.

**That is a copy the store has already flagged.** Adding a word by hand in both places is exactly
the mechanism [[process-is-a-feedback-kind-for-the-ritual-not-the-corpus]] warned about; the durable
fix it names is a `wiki/rules/` page with a region in each file, and **it is designed nowhere**
([[no-rule-reads-a-harness-file]], [[a-copied-list-drifts-and-a-sweep-cannot]]).

## What it obliges

- **A harness line is written the moment the change is decided**, not at the end
  ([[a-harness-change-is-recorded-when-it-is-decided]]).
- **`/ingest` files it under its own kind.** A `Harness` section is a work queue, and its lines
  arrive in `log.md` as `- harness:` rather than being translated into another kind.
- **The channel's failure mode is unchanged and is silence**: nothing checks that the section was
  written to ([[vault-feedback-file]]).

# It held a second time on 2026-08-24, and the owner refused to have that reading signed as his

**The vocabulary was re-cut into four session kinds, and folding `harness` into `decision` was
proposed and rejected** — this page had already refused that exact shape, a decided work item folded
into a kind that carries findings, and **a `/pre-task` found it before the plan was approved**
([[lint-and-process-stop-being-session-kinds-and-decision-joins]]).

**The decision to keep `harness` is the session's own, and it is written in the session's voice.**
It was argued from this page and carried in a plan the owner approved. At the retro he refused the
attribution:

> **owner: это не мое решение, а твое. Сейчас - я могу сказать что частично согласен с ним. Но
> приписывать это решение как мое - нельзя.**

**His position is partial agreement, not ratification**, and it is recorded that way rather than
rounded up ([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]],
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

**That exchange is the reason a plan's ratification list now names each line's source**
([[every-line-of-a-plans-ratification-list-carries-its-source]]): approving a plan and having said
the thing are different acts, and nothing in the chain marked which one a line came from.

**The duplication this page flagged is unchanged.** The vocabulary is still five hand-kept copies
across five files, and the durable fix — a region in each — is still designed nowhere.
