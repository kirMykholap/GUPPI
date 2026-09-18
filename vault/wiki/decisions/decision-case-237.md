---
type: decision
case: "237"
status: current
update: ["[[estimate-permissions]]", "[[rule-permissions]]"]
origin: raw/2026-09-18/1252/ledger.md#case-237
sprint: migration
created: 2026-09-18
tags: [harness, session]
---

## Context

`rule-permissions` (`built`) renders `allow` in `.claude/settings.json` — nine entries for the working files of the session — and promises in its Purpose that the session writes them "without asking". Its one Estimate `estimate-permissions` stands `passed`; its Criterion asks for a live probe "asked or not asked", and its Result holds "returned without a prompt" — read by the agent. The agent does not see the client's prompt: an approved call returns to it exactly as one that was not asked. The person sees it: in Plan Mode the prompt appears before every edit outside the plan file, allow list or not, and the person approves it each time. The Case touches `estimate-permissions`; the Purpose of the rule changes by one sentence, which touches no Estimate.

## Problem

The Criterion assigns the reading to an observer who cannot observe, and the page holds `passed` on what the agent did not see. The promise "without asking" does not hold in Plan Mode by the client's mechanism, and the person accepts that — but it has to stand in the Estimate, not in memory.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-237
