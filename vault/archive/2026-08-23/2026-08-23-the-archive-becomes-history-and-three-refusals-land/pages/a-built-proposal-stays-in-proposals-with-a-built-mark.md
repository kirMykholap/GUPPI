---
title: "A proposal that was built stays in `wiki/proposals/` with a `built` mark, rather than moving to `archive/`"
type: decision
status: deprecated
authority: built-proposal-disposition
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified/handoffs/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified.md"]
tags: [vault, process, harness]
supersedes: "[[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]"
superseded_by: "[[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]"
---

> [!NOTE] RETIRED 2026-08-23
> **The owner reversed this ruling the day after he gave it.** An implemented proposal now moves to
> `archive/`, on the ground that the archive is history rather than a verdict, and the successor
> page carries the claim
> ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]). **The half of
> this page that survives is the argument about the relation**: `superseded_by:` is still the wrong
> relation for a proposal that was built, and the successor says so in his own terms. Read this page
> only to answer *why did we change this*.

# The ruling, 2026-08-22, and he said it rewrites what stood before it

> **owner: я считаю, что proposal который построен должен оставаться в wiki/proposals с пометкой built. А не уезжать в архив. Это решение теперь актуальное и должно переписать те, что были ранее**

**Two things in one sentence.** A built proposal **stays where it is**, `wiki/proposals/`, and it
**carries a mark saying it was built**. The move to `archive/` is refused, and the clause naming that
move is not merely superseded by accident — **he said the earlier decisions are rewritten by this
one**, which is why this page carries `supersedes:` rather than standing beside them.

**What is rewritten, named rather than implied:**

| what stood | where it stood |
|---|---|
| *a built proposal is retired to `archive/` with `superseded_by:`*, after a check that nothing on it lives only there | the `prohibition` of 2026-08-18, now `deprecated` ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]) |
| *a proposal is `current` while it stands, and `deprecated` with `superseded_by:` once it is built **or** refused* | one clause of [[proposals-are-a-folder-not-a-status]], dated where it stands rather than removed |

**The refused half of the earlier ruling is only the built half.** Nothing here says what becomes of
a proposal that is **refused**, and the earlier page's answer for that case — retire it, it has a
successor of the right kind — is untouched by his words. That asymmetry is the ground below.

# The hole that produced it: `superseded_by:` is a relation a built proposal has no partner for

**Supersession is a relation for a changed claim** — the successor asserts the same thing
differently. That is the vault's own definition, in the `status` and supersession section of its
`CLAUDE.md`, and it is why a title corrected in place is not one
([[a-title-corrected-in-place-is-not-a-supersession]]).

**A built proposal has no successor of that kind.** The pages recording what was built assert
something else: *this is how it works*. A concept page describing the injector does not say
differently what the proposal for an injector said — it says a different thing about a different
subject.

- **A refused proposal can have such a successor.** The decision refusing it makes the same claim
  the other way, and [[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]] is
  that shape working.
- **A built one cannot.** The rule as written asked for a relation that does not exist in the case
  it was written for, and every built retirement to date has satisfied it by pointing at whatever
  page happened to carry the most of the work.

**This is the defect deferred on 2026-08-16 being answered rather than deferred again.** *Two
statuses cannot carry three states* is exactly what [[the-proposal-status-cannot-tell-built-from-refused]]
recorded and declined to fix; the owner has now fixed one of the three
([[a-question-asked-is-not-a-question-answered]]).

# What it obliges, and none of it is built

**The mark does not exist.** On the day the ruling was given, `wiki/proposals/_schema.yaml` does not
know it, rule 2 of `bash scripts/vault-check.sh` does not admit it, and the corpus therefore
disagrees with its own ruling until that work lands.

**Whether the mark is a third `status` value or a field of its own is his, and he deferred it:**

> **owner: built статус обсудим подробно на следующей сессии**

**The tension is his own to resolve and it is already written down.** [[proposals-are-a-folder-not-a-status]]
argues, on 2026-08-15, that *"a third status value would have been a second vocabulary to keep in
step with the first"* — which is an argument against one of the two shapes he is choosing between.
**It is quoted here so the next session has it in front of him**, not to prejudge the answer.

**Until the mark exists, a built proposal is left `current` in `wiki/proposals/` and says in prose
that it was built.** That is the state the ruling produces, and it costs the folder its own query.

## The cost, stated because the folder was created for the query it breaks

**`rg -l "^status: current" wiki/proposals` was the answer to *what did we plan and never do***, and
[[proposals-are-a-folder-not-a-status]] names that query as the reason the category exists at all.
**A built proposal staying `current` puts a built thing in that answer.** So the mark is not
cosmetic: it is what has to carry the distinction the `status` field used to carry, and until it
lands the query over-reports.

**The failure direction is the safe one and it is still a failure.** Over-reporting shows a reader a
page that was built; under-reporting would hide a design nobody has executed, which is the loss the
folder exists to prevent.

# What the ruling does not answer, and is not decided here

- **The proposals already retired to `archive/` under the old rule.** About thirty pages left
  `wiki/` before this date, and whether any of them comes back is not in his words. **Not decided,
  and raised in the brief.**
- **The check the old ruling required before a move** — *read the page whole and move what lives
  only there onto a page* — has no move left to stand before. It is not carried forward here as an
  obligation and it is not struck: what a page holds that lives nowhere else is still worth moving,
  and now nothing is lost if it is not.
- **Whether `refused` gets a mark of its own.** He named one word, `built`.
