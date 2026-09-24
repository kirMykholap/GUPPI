---
type: decision
case: "384"
status: current
update: ["[[rule-bash-guard]]", "[[estimate-bash-guard]]"]
supersedes: ["[[decision-case-382]]"]
origin: raw/2026-09-23/1859/ledger.md#case-384
sprint: migration
created: 2026-09-23
tags: [hooks, harness]
---

## Context

`rule-bash-guard` refuses a heredoc with a backslash or with a file write and sends the agent to Write. The agent follows it, and at every Retro reports the refusal as a finding. The refusal is the behaviour the hook was made for, so these reports are noise. The message of the hook (`guppi/bashguard.py`, the function `run`) says what to do, but not that the refusal is normal. Case 382 deferred this; this Case takes it up. Three places quote the message: the How it works of `rule-bash-guard`, the Criterion of `estimate-bash-guard`, and the test; the How it works also names the log line `bashguard: <reason>`, while the code writes `bashguard refused: <reason>`. `estimate-bash-guard` stands in the shape before case 193 — a `### case 127` block, `## Context` and `## Method`, no `method` or `purpose` field — so its Criterion is replaced whole and the fields are set in the same `update`; the lines of the old Criterion on the page's creation and on the registration in `settings.json` leave it, being the bookkeeping of case 127 and not the behaviour of the hook. Every item is an `update` with a `ref`, so no vault query.

## Problem

The message of the hook does not say that the refusal is legal and needs no report, so the agent takes it for an event of the session each time.

## Given

`rule-bash-guard` — the rule; its How it works quotes the message.
**＋** `estimate-bash-guard` — the Estimate of the rule; its Criterion quotes the message.
**＋** `guppi/bashguard.py` — the function `run` prints the message, the module docstring quotes it.
**＋** `tests/test_bashguard.py` — the tests of the refusals check the message.
**＋** `raw/<date>/event_log.md` — the day's event log the hook writes the refusal line to.
**＋** `/dev/null` — the one redirect target that is no file write.
**＋** `decision-case-382` — the deferred decision the Case takes up.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#case-384
