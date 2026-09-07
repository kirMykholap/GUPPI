---
title: "The growth alarm measures the brief itself, and its threshold is measured, not invented, over the sprint that collects sizes and raises no alarm"
type: decision
status: current
authority: growth-signal
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md"]
tags: [process, vault]
---

# The alarm is the brief's own size

**Decided on 2026-08-13.** Sprints exist so that the brief does not grow; a sprint running two
months would hand back the 129 KB handoff under a new name. Something must bound it.

**Rejected: a calendar time-box.** Its value in team Scrum is forecasting and cadence, neither of
which applies to one person working evenings, and the one thing it would give — a forced
retrospective — a per-session handoff already gives.

**So the measure is the disease rather than a proxy for it.** An overgrown sprint is visible as an
overgrown brief. The librarian generates the brief anyway and knows its size for free; over
threshold it says so in the brief's first line — *"S4 has run 11 sessions, the brief is 6.2 KB
against a threshold of 4.5 — is the goal still one goal?"* **As a question, never a verdict.**
Splitting, narrowing or closing is the owner's call, exactly as closure is
([[a-sprint-closes-on-its-goal]]).

## The threshold is calibrated, not invented

An earlier draft named 4 KB outright; that number was made up. The procedure instead:

- **sprint 1 collects data and raises no alarm.** The librarian records the brief's size in
  `log.md` every session, as `- measure: brief=<bytes>`;
- **at sprint 1's retrospective** we have the growth curve and, more importantly, the owner's
  answer to one question: *"did the brief get long?"* That answer is the ground truth — size is
  only its proxy, and only he knows when he began skimming rather than reading;
- **from sprint 2** the threshold is 3–4× the size he called comfortable.

*(The title read "The growth alarm measures the brief itself, and its threshold is measured in
sprint 1 rather than invented" until 2026-08-18, and the bullets above are where that sprint is
named. **1 was never a count**: it is a sprint's identifier, and later sprints arriving cannot make
it wrong. That reasoning stood in a `quantity:` line until the field was rejected and the rule made
unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), which withdrew the only way
a page had to declare itself exempt — **a number that is genuinely an identifier still leaves the
title**. A code span around it was rejected as a dodge for exactly this shape, because this corpus
writes such numbers in plain prose, so the title names the sprint by what it does — collect the
sizes and raise no alarm — instead of numbering it
([[a-title-names-what-is-counted-instead-of-counting-it]]). Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

Also rejected: baselining from the first brief of a sprint and alarming at 4×. The first brief is
abnormally small because almost nothing has happened yet, not because it is healthy; from a 0.4 KB
baseline a healthy brief would trip by the third session, **and an alarm that always fires stops
being read.**

Secondary counters — sessions in the sprint, new pages, how many times the goal changed — explain
*why* the brief swelled and are shown alongside. They are context; the alarm is the size. The
brief's place among the three artefacts: [[journal-vault-brief-each-artefact-has-one-owner]].
