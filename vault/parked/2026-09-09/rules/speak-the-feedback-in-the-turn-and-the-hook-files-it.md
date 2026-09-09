---
title: "Speak the feedback in the turn you notice it, and the hook files it"
type: rule
status: current
governs: [CLAUDE.md, .claude/skills/handoff/SKILL.md]
render: region
basis: human
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "CLAUDE.md", ".claude/skills/vault-ask/SKILL.md", ".claude/skills/handoff/SKILL.md", ".claude/hooks/catch-the-feedback.ps1"]
decided_by: [[the-session-speaks-the-feedback-line-and-a-hook-files-it]]
supersedes: [[write-the-miss-into-vault-feedback-before-the-turn-ends]]
tags: [harness, vault, process]
---

# What travels

<!-- text -->
**When the vault answers wrong — or anything else worth recording goes wrong — say it in your reply
in that same turn**, inside a fenced `VAULT-FEEDBACK` block. **You never write**
`.superpowers/sdd/vault-feedback.md` **yourself.** A hook on `MessageDisplay` lifts the block out of
your message and files it, which is what makes the channel usable in plan mode, where a session
cannot write a file at all.

```VAULT-FEEDBACK
- miss: what the vault failed to supply, and where that surfaced
- measure: a number, with what it does and does not mean
- decision: what was decided, by whom, and against what - naming which shape it is:
  the owner said it, the owner selected it, or the session understood it
- harness: a decided change to the files that instruct an agent
```

A `VAULT-FEEDBACK` fence nested inside another fence is an example and is ignored, so the block
above files nothing. `/handoff` drains the file into `Feedback to the librarian` and `/ingest` files
each line under the kind it names. **Recording is not arguing**: it costs a line, and whether the
corpus changes is the owner's call, later.
<!-- /text -->

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# What changed from the rule this replaces

**The claim changed, which is why this is a supersession and not an edit.**
[[write-the-miss-into-vault-feedback-before-the-turn-ends]] told a session to *write one line into
the file*; a session now *speaks* the line and writes nothing. A page whose claim changes is
replaced, and the retired one keeps its slug and goes to `archive/`
([[a-title-corrected-in-place-is-not-a-supersession]]).

**The rename is free here and is not free anywhere else.** The old slug says *write the miss into
the file*, which is now wrong in its verb and in its object; a supersession mints a new address
rather than moving an old one, so nothing is stranded
([[a-page-rename-is-sed-and-verify]]).

# Why the mechanism had to change rather than the reminder

**The rule broke eight recorded times and never once through forgetfulness.** Plan mode forbids a
session to write files, so the party the rule binds is disarmed exactly when it notices something
([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).
A tenth instance happened while the replacement was being planned.

**The rejected alternatives, and what each was rejected for**, are on the decision behind this page
([[the-session-speaks-the-feedback-line-and-a-hook-files-it]]): a reminder hook, two recorders on
events the transcript already covers, and a subagent priced at 33,471 tokens for one line.

# Why it governs three files and not the file it writes about

**The three are the ones the decision obliges to carry the rule** — the repository's `CLAUDE.md`,
`/vault-ask` and `/handoff` — because a rule about noticing has to be where the noticing happens
([[feedback-is-recorded-in-the-turn-it-is-noticed]]). They were three hand-written copies until
today, and regions exist to remove exactly that
([[marked-regions-and-the-prose-outside-them]], [[the-harness-is-compiled-not-maintained]]).

**`.superpowers/sdd/vault-feedback.md` is deliberately NOT a target, and a `/pre-task` caught the
plan that made it one.** The file is git-ignored and `/handoff` empties it to its header every
session, so the injector would find a governed destination with no region, report it, and exit 1 —
which reddens rule 12, and `lock-the-librarian.ps1` reads a red gate as a refusal to dispatch the
only writer able to clear it ([[a-rule-may-not-govern-a-file-the-ritual-empties]],
[[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

# The vocabulary in the slice is four kinds and it is a decided list

`miss:`, `measure:`, `decision:`, `harness:`. **`lint:` and `process:` stopped being session kinds
on 2026-08-24** and stay the librarian's own words in `log.md`
([[lint-and-process-stop-being-session-kinds-and-decision-joins]]).

**`decision:` names which of the retro's three shapes it is** — *the owner said it*, *the owner
selected it*, *the session understood it* — because 58 of the 254 feedback lines ever written were
decisions with no kind of their own, and 21 of those sat under `process:` including direct owner
rulings ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

# This rule has an instrument, and it is the first of the six to get one

**`scripts/hook-selftest.ps1` carries fifteen cases for the catcher**, which is what observes this
rule now: the fence reader in both directions, accumulation until `final`, deduplication by
`message_id`, the drain skip and the resumption after it, an undeclared kind kept with a note, and
exit 0 on a malformed payload ([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

**What it does not observe is the judgement** — *this answer was wrong* — which is the half no check
can have ([[rules-becomes-a-type-of-its-own]]). The instrument holds the channel, not the noticing.

# Where it renders, and what the injector is trusted with here

Three regions, one per destination, each a paired comment named for this page's slug
([[a-region-is-a-paired-comment-named-for-a-rule]]). **The slice carries a fenced block**, and the
injector dropped a fenced block inside a slice once and reported success
([[the-injector-drops-a-fenced-block-inside-a-slice]]). It was fixed at `e83ce28` and two selftest
cases hold it; the region was still read by eye at the ingest that wrote this page.
