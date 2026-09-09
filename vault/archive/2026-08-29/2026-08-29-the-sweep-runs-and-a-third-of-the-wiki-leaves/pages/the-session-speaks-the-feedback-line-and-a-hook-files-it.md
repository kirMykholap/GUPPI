---
title: "The session speaks the feedback line and a hook files it, because plan mode disarms a writer"
type: decision
status: archived
authority: feedback-recording-mechanism
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/hooks/catch-the-feedback.ps1", ".claude/settings.json", "scripts/hook-selftest.ps1"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-24

**A session no longer writes `.superpowers/sdd/vault-feedback.md`.** It prints a fenced
`VAULT-FEEDBACK` block in its own reply, and `.claude/hooks/catch-the-feedback.ps1`, registered on
`MessageDisplay`, lifts the block out of the message and appends it to the file
([[the-feedback-catcher-hook]]).

**The cause is measured, not guessed.** The rule obliging a session to record a miss in the turn it
notices one **broke eight recorded times**, and every one of them for the same reason: plan mode
forbids a session to write files, so the party the rule binds is disarmed at exactly the moment it
notices something ([[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).
**A tenth instance happened while this was being planned** — a miss about `sprint.md` noticed in plan
mode, carried in the reply until the mode ended.

# What was rejected, and each for a reason of its own

- **A reminder hook.** The proven cause is the mode and not forgetfulness, so a reminder addresses
  nobody's failure ([[knowing-a-rule-is-not-a-mechanism]]).
- **Two recorders on `UserPromptSubmit` and `Stop`.** The harness already writes a complete
  transcript, and they would record what is already recorded
  ([[the-floor-under-a-session-is-read-because-the-record-already-existed]]).
- **A subagent writing on the session's behalf**, priced at **33,471 tokens** for one line.

# What it obliges

- **The successor rule page**, which replaces the one telling a session to write the file
  ([[speak-the-feedback-in-the-turn-and-the-hook-files-it]]). Until it renders, `CLAUDE.md` carries
  the retired instruction and nothing a session reads at startup describes the mechanism
  ([[a-deprecated-rule-does-not-render]]).
- **The catcher yields in the turn the file shrinks.** `/handoff` empties the file, and a recorder
  that fought the drain would refill what the journal just took. It compares two sizes rather than
  judging ([[whoever-filed-a-feedback-line-empties-it]]).
- **A nested `VAULT-FEEDBACK` fence is documentation, not a record.** The hook counts fence depth,
  so a rule page or a skill quoting the form does not file itself.

# The owner said what it is like to use, and that is the acceptance this channel has

> **owner: новый формат когда ты пишешь прямо в чате VAULT FEEDBACK, а скрипт уже пишет в
> .superpowers/sdd/vault-feedback.md - мне очень нравится. Стало удобно, я вижу детали.**

**What changed for him is visibility rather than bookkeeping.** The lines used to land in a
git-ignored file he had no reason to open; now they are in the reply he is already reading
([[the-harness-is-no-longer-visible-to-its-owner]]).

# The instrument this rule finally has

**`scripts/hook-selftest.ps1` gained fifteen cases for the catcher** — the fence reader in both
directions, accumulation until `final`, deduplication by `message_id`, the `/handoff` drain skip
*and* that the turn after it resumes, an undeclared kind kept with a note, and exit 0 on a malformed
payload. The suite reads **caught 138, missed 0**, up from 123.

**That is the first mechanical instrument any of the six instrument-less rules has got**
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]). It moves acceptance criterion 1 of S3
by one member and closes nothing.
