---
title: "The vault is verified by use, not by reading: a wrong answer is written down in the turn it is noticed"
type: decision
status: current
authority: fidelity-verification
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-14
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/handoff/SKILL.md", ".claude/skills/vault-ask/SKILL.md", "CLAUDE.md"]
tags: [vault, process]
---

# Verified by use, because verifying by reading is not a check this owner has

**Decided by the owner on 2026-08-14**, from an observation about himself rather than about the
method: the designed fidelity check — sample ten verdicts and read them beside their sources
([[ingest-is-units-and-verdicts]]) — **assumes a reader who can judge an English corpus quickly,
and for this owner that is not the case.** A check that cannot be performed by the person who owns
it is not a check.

**Rejected: verifying by reading.** Not because it is wrong — it has found one thing per ten units,
three ingests running — but because it is the librarian, not the owner, who has been performing it,
and a store checking itself is testimony ([[journal-vault-brief-each-artefact-has-one-owner]]).

**Chosen: verifying by use.** The vault is wrong at the moment it is *asked* and answers badly, and
that moment costs nothing extra because the work was happening anyway. **The observation is
recorded in the turn it is noticed**, never reconstructed at handoff time, because by then the
question, the grep that failed and the page that should have carried it are gone.

## Obliges

- **three files carry the rule** and must keep carrying it: the repository's `CLAUDE.md`,
  `/vault-ask` and `/handoff`. A rule about noticing has to be where the noticing happens;
- **the draft is drained at handoff or it silently rots** — `/handoff` empties
  [[vault-feedback-file]] into section 7 and re-headers it, and `/ingest` files each line into
  `log.md` under its own kind;
- **recording is not arguing.** It costs one line, and whether the corpus changes is the owner's
  call afterwards. A channel that requires a case to be made is a channel nobody uses at 2 a.m.

## Why this is the loop closing rather than a new process

The misses in `log.md` were, until this decision, written by the librarian *about itself* at ingest
time — the party being reviewed reporting the review. This moves the observation to the party that
was let down, in the moment it happened, and leaves the librarian only the filing. See
[[the-librarian-writes-unattended]] for the same division applied to writes, and
[[vectors-are-deferred-not-rejected]] for what those miss lines are evidence *for*: they are the
only test data this store has.

## A divergence against this rule, 2026-08-18, and it is marked late in its own file

**A vault miss was found and not written into `vault-feedback.md` in the turn it appeared.** It was
reported to the owner in chat and filed hours later at the retrospective, with the lateness written
into the line itself. Rejected alternative, as for every divergence: obey the rule.

**Why it looked unnecessary: it had just been said out loud** — which is the exact failure this rule
names, since chat does not survive the session
([[chat-is-not-a-channel-that-survives-the-session]],
[[write-the-miss-into-vault-feedback-before-the-turn-ends]]).

**A second-order defect of the same loop was recorded beside it**: a line written into
`vault-feedback.md` *during* `/ingest` waits a whole session, because `/handoff` drains the file
before `/ingest` writes to it ([[vault-feedback-file]], [[a-queue-only-one-party-can-drain-is-unbounded]]).
