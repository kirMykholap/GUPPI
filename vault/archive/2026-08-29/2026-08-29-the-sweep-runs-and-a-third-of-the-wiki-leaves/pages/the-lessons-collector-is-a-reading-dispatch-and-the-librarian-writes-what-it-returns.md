---
title: "The lessons collector is a reading dispatch, and the librarian writes what it returns"
type: decision
status: archived
authority: lessons-collector-write-scope
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/skills/vault-lint/SKILL.md", "scripts/lessons-queue.py"]
tags: [vault, agents, process]
---

# The question he asked

> **owner:** «я считаю что этот агент должен работать паралельно с библиотекарем... ТВое мнение?»

> **owner:** «Получается что агент "lessons collector" должен сам найти уроки, записать и обработать.
> Как финал - подготовить proposals и передать их библиотекарю. То есть паралелить мы не можем?»

# The ruling, 2026-08-25

> **owner:** «Выход - proposal, но ты правильно говоришь что эти proposals должны пройти через
> библиотекаря. И уже библиотекарь должен написать о них в брифе.»

> **owner:** «3) давай попробуем»

**The collector reads and returns; it writes nothing.** It comes back with families and proposal
drafts, and the librarian writes the pages — and writes them into the brief by generation, because
the brief is derived ([[the-librarian-writes-its-log-and-the-brief-carries-what-it-hands-back]]).

**Its read scope is `lessons/` plus `rules/` and `proposals/`.** The queue is defined by what cites a
lesson, so the citing folders are part of its subject
([[lessons-become-a-queue-drained-into-proposals]]).

# Why it may not be a second writer scoped to one folder

**`authority:` is required in `wiki/lessons/_schema.yaml`**, so every new lesson page obliges a slug
in `authority.md`, which rule 13 compares against the tree in both directions. **A writer scoped to
`lessons/` therefore writes three shared registers** — `authority.md`, `tags.md` and `log.md` — **and
contends with the librarian on all three**
([[parallel-librarians-break-the-one-writer-property]],
[[dispatch-librarians-in-parallel-only-for-reading]]).

# What it obliges in the harness

**`.claude/skills/vault-lint/SKILL.md` is rewritten** so the dispatch returns families and drafts
rather than writing `proposals/` and appending a `lint` entry to `log.md` itself. **Its ordering
argument goes with it**: the skill puts that dispatch first *because it writes*, and once it writes
nothing that ground is gone.

**The `lint` entry with its numbers stays in `log.md`**, and nothing is written into the brief by
hand.

# Not done

**The skill is unchanged and the first collector run has not happened.** It has been carried since
2026-08-24 ([[the-instrument-work-and-the-first-lessons-collector-run-move-to-the-next-session]]).
The queue's reading on the day of the ruling, from `uv run python scripts/lessons-queue.py`, which
writes nothing: 157 lessons, 22 cited by a rule, 40 by a proposal, 51 by either, 106 in the queue —
against 140 and 94 on 2026-08-24.

# It ran for the first time on 2026-08-26 and wrote nothing, as designed

**Four numbers from the run.** **104 read** — the whole queue, plus `wiki/rules/` (16) and
`wiki/proposals/` (41); **13 families found**; **5 proposal drafts and 2 appends prepared**;
**11 rejected as singletons.** It took the queue reading twice, opening and closing, both `157 / 104`
at `9950dbd`.

**Cost: 388,649 tokens, 55 tool uses, 17m23s.** First data point for this dispatch; there is no rate.

**Seven `--near` lookups were run before any draft.** Five slugs came back free of collision and one
— `link-sweep-file-class` — returned *already in a group, do not write a second*, which the collector
obeyed ([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

# The five drafts are filed rather than held — 2026-08-26

**The owner selected it**: they go into `wiki/proposals/` now, carrying the `decided_by:` the
collector could honestly supply, rather than being held outside the corpus until he rules on each.

**Filed at the ingest of that date:**
[[a-pretooluse-net-for-a-shell-write-and-a-syntax-check-after-a-script-edit]],
[[a-cr-byte-census-of-the-working-copy-behind-lint]],
[[a-plant-and-revert-helper-for-the-real-tree]],
[[a-register-of-what-each-hook-writes-when-it-is-probed]] — and
[[a-reference-graph-sweep-over-live-to-archive-citations]], **refused in full by the owner** and
filed as refused rather than dropped
([[the-live-to-archive-citation-advisory-is-refused-in-full]]).

**`decided_by:` on the four live ones points at this page**, because no per-topic ruling exists for
any of them. **Each says on its own face that this will need re-pointing** the day he rules — which
is the collector's own warning, carried rather than resolved.

**Two appends rather than new pages**: to [[telling-an-unfilled-retro-from-a-written-one]], whose
predicate is per-file where the family needs one verdict per open line; and to
[[a-quote-is-cyrillic-rule-with-an-advisory-verdict]], moving its reader one hop earlier into the
catcher — **which this session then built**, so that append describes something that exists.

**One finding of the run is about the instrument rather than the corpus**: filing the drafts moves
roughly 25 lessons out of the queue without any of them being acted on
([[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]],
[[the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed]]).

**And the returned result tripped the subagent instruction-shaped-output filter**, on
`settings-json`, because one draft proposes registering a `PreToolUse` matcher in
`.claude/settings.json`. **A reading dispatch that proposes a harness change will trip this every
time it is right to do so.** Relayed as a finding and not acted on.

# Carried again on 2026-08-28, with one change to what it hands back

**It writes a proposal draft into `docs/` rather than returning it in its answer.** That is the shape
named in the journal of 2026-08-28, and it is the only change to the design since the run of
2026-08-26. It is still a reading dispatch as far as `wiki/` is concerned: `docs/` is outside the
store the one-writer rule covers.

**And the owner named the agent itself as the point of the lessons cycle** the same day, in his own
words ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]).

**Who dispatches it changed.** `/ingest` dispatches, in parallel with the decisions agent, and the
librarian never does — it carries no dispatch tool
([[the-ingest-dispatches-the-reading-agents-and-the-librarian-writes-what-they-return]],
[[the-ingest-rewired-so-the-session-dispatches-and-the-librarian-writes]]).

**Not run for a second consecutive session.**
