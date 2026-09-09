---
title: "The page that must move to `archive/` is moved by a sweep inside `scripts/vault-archive.sh` at the lint stage"
type: decision
status: current
authority: archive-sweep-placement
binding: deferral
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-archive.sh", ".claude/skills/vault-lint/SKILL.md"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-24

> **owner:** «Отправлять в архив должен скрипт на этапе lint. Он проходит по всем записям,
> проверяет поля и двигает куда нужно. Если такого механизма еще нет - записывай, будем строить.»

**Neither the session nor the librarian moves such a page by hand.** A page whose `status:` obliges
it to leave `wiki/` is found and moved by a sweep, at `/vault-lint`.

**And on where it lives: inside `scripts/vault-archive.sh`, not a new script.** That way it inherits
that script's refusals rather than acquiring its own opinion about when a move is allowed — the
refusal that no page leaves without a live page naming it, and the conditional `decided_by:`
requirement on a refused proposal ([[vault-archive-sh]],
[[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]).

**Rejected: a second mover.** Two programs that both move a page and disagree about when are worse
than either.

# No such mechanism exists today, and that is the finding behind the ruling

**`scripts/vault-archive.sh` moves only what it is given as an argument and searches for nothing.**
`.claude/skills/vault-lint/SKILL.md` reads stale `status: current` with a human's eyes and moves
nothing.

**The case that produced it**: `wiki/proposals/a-style-rule-for-the-prose-a-session-writes.md`
carries `status: implemented` and sits in `wiki/proposals/`, where
[[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]] and
`wiki/proposals/_schema.yaml` both say it moves.

# What is deferred, and it is the part that decides behaviour

**The full list of conditions the sweep checks, and what it does when a move is refused, are their
own session.** Nothing here says whether a refusal is a red verdict, an advisory or a queue entry.

# The deferred clause is closed — 2026-08-28

**What the sweep does when a move is refused was the open half of this page, and it is decided**: it
continues, collects the refusals, prints them as a list at the end, and exits non-zero if there was
one ([[the-archive-sweep-continues-past-a-refused-move-and-collects-its-refusals]]).

**The full list of conditions is closed for four folders and open for two.** `lessons/`,
`decisions/`, `proposals/` each have a criterion; `entities/` and `concepts/` were deferred
explicitly the same day ([[entities-and-concepts-get-no-archival-criterion-today]]).

**The sweep itself is still unwritten**, and its design now has a page of its own
([[the-archive-sweep-that-walks-each-folder-and-collects-its-refusals]]).
