---
title: "A rule-usage axis for `/vault-lint`"
type: proposal
status: current
authority: rule-usage-counting
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/skills/vault-lint/SKILL.md"]
decided_by: [[the-rule-usage-axis-for-lint-is-recorded-and-explicitly-not-built]]
tags: [vault, process, harness]
---

# Raised 2026-08-20, to be considered next session and deliberately not built

> **owner:** «у нас есть процесс lint... будет хорошим решением после ingest запускать еще и lint,
> который будет "смотреть lessons", "мерять как часто вызываются или пропускаются правила (для
> этого нужен счетчик)" и формировать предложение добавить/убрать. Это предложение сейчас не
> делаем, но я хочу его рассмотреть на следующей сессии.»

**The idea:** `/vault-lint` reads `lessons/`, counts how often each rule fires or is skipped, and
proposes additions and removals.

# The axis is empty today

**What `/vault-lint` does now is entirely about the corpus's internal consistency** —
contradictions, stale `status: current`, missing pages, orphans, broken links, tag drift. **Nothing
about rules.** No instrument in this project answers *which rules are earning their place*.

# What the proposal has to answer, found while recording it

**The counter already exists, for one rule.** The pre-task ledger records invocations and skips
([[the-pre-task-ledger]]), and the pipe from it — ledger to `/handoff`, journal, `/ingest`, corpus —
is already closed. **So this is generalising a working prototype rather than inventing a mechanism**,
and the two are different tasks with different risks: the prototype cost a hook, a library, a script
and a divergence, and it counts one rule.

**`after every ingest` re-argues a decision of 2026-08-20.** `/vault-lint` runs once a sprint, and
the density advisories moved behind `--lint` precisely because printing them on every run buried the
one advisory that was about that run ([[the-tag-density-advisories-move-behind-lint]],
[[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]). **The cadence half of
the proposal inherits that problem exactly; the rule-usage half does not.**

# What it would oblige

- **A counter per rule**, which for most rules has no event to hang on: `/pre-task` acquired one only
  because a plan and a first write are observable, and *ask before you weaken a rule* has no such
  moment ([[no-rule-reads-a-harness-file]]).
- **A verdict about what a low count means.** A rule that never fires may be dead, or may be working
  perfectly — nobody has done the thing it forbids. Counting cannot separate those, and proposing a
  removal on the count alone would retire the rules that are succeeding.

**It is `current` while it stands, and retires with `superseded_by:` the day it is built or refused**
([[proposals-are-a-folder-not-a-status]],
[[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
