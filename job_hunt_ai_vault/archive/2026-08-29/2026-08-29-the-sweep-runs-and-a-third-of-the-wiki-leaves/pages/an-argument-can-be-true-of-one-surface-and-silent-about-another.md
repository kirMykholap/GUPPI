---
title: "A ritual's argument can be true of one surface and silent about another"
type: lesson
status: archived
authority: argument-surface-scope
basis: measurement
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# The incident, 2026-08-21

**[[the-ritual-records-itself-rather-than-being-detected]] says a hook cannot detect a `/pre-task`**,
because a pre-task and a vault-ask are the same dispatch to the same agent and differ only in prompt
wording — so a hook would have to match on wording, which is asserting the sentence rather than the
condition.

**That is true of the *dispatch* surface, and it says nothing about the *skill* surface.** It could
not have: when it was written, the ritual's only observable act was the dispatch. Since the ritual
gained a first phase that is a skill invocation, the surface exists and carries the skill's name in
a structured field.

**Measured rather than argued.** A probe was registered on `PreToolUse` with matcher `Skill|Write`,
where `Write` is a control known to fire — so a run with a `Write` row and no `Skill` row would have
meant `Skill` is not matchable, and a run with neither would have meant the hook never loaded
([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]):

```
tool=Write | event=PreToolUse | skill=       | input_keys=content,file_path
tool=Skill | event=PreToolUse | skill=sprint | input_keys=args,skill
```

**So the hook sees which skill, by name.**

# The failure class, which is not "the page was wrong"

**The page is not wrong. It is answering about somewhere else.** Nothing in its text says which
surface its argument ranges over, because at the time there was only one — and an argument whose
scope is implicit reads as universal the moment a second surface appears.

**This is invisible in the direction of confidence.** A reader looking for *can a hook detect this?*
finds a page that says no, with a good reason, and stops. The page cannot tell them that the
question it answered is narrower than the one they asked
([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

# What did not move, and it is the half that decided the design

**The page's second argument survives intact**: inferring that a ritual ran fails by staying silent
in exactly the case the mechanism exists for. The recording direction is the safe one, and the
`Skill`-surface finding does not touch it — which is why the design that was about to be built, a
hook on the `Skill` tool, **would have bought zero seconds at the cost of the one property the
mechanism exists for** ([[an-instrument-that-fails-towards-nothing-to-do]]).

# The repair

**Date the scope onto the page rather than retiring it.** A page answering about one surface gets a
section naming which surface, and the measurement as its evidence — the same treatment a figure
about one day gets ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**And the general form for a reader**: when a page says *X cannot be detected*, ask what it was
observing when it said so. This corpus's arguments about mechanisms are arguments about the surfaces
that existed when they were written, and the harness grows surfaces
([[no-rule-reads-a-harness-file]]).
