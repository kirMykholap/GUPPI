---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether each Stop hook of GUPPI finds its own refusals in the transcript by its name at the head of the text after the bracket, whatever the bracket holds, by one function of ledger.py, so that a held lesson is asked about once and a line told once a stretch is told once
method: "uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_onward.py .guppi/tests/test_casecheck.py .guppi/tests/test_ratified.py, whose refusals stand under [command hook <n>] and under the command; by hand, at the Retro of the session that creates this Estimate: each Stop hook feedback record of the main transcript of that session under ~/.claude/projects/ after the commit of the change read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-04/0807/ledger.md#case-1035.1
sprint: plugin
created: 2026-11-04
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
A `Stop` hook `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi onward` or `guppi onward --plan`, as `.claude/settings.json` registers it, fires at the end of a reply of the main agent, and the stretch of the transcript at `transcript_path` holds refusals of `Stop` hooks.
**＋** The ledger hook holds a fresh `lesson[error]` line with no mark, and the agent writes the line again in its next reply.

Then:
A refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:`, and each of its lines that opens with a bracket and `]: ` holds the text of one hook.
**＋** A refusal is a hook's own when its text after the bracket opens with the name of the hook and a colon, such as `ledger:`, whatever the bracket holds: `[command hook <n>]` or the command of the hook.
**＋** The name of a hook is the words of its command after ` guppi `, so it stays when the start of the command changes.
**＋** Every line that these hooks print on stderr at a `Stop` opens with the name of the hook and a colon.
**＋** One function of `.guppi/guppi/ledger.py` makes this judgment, and `refusals`, `own_refusals` and `sent_back_last` use it for each of the five hooks.
**＋** The ledger hook asks about the held line once, and the line written again in the next reply lands in the session's ledger at the `Stop` of that reply.
**＋** Each line that one of these hooks tells once a stretch is told once, and `guppi casecheck` stops at its third refusal of one reason.
**－** A refusal whose text after the bracket opens with the name of another hook is no refusal of this hook, and `onward:` and `onward --plan:` never match each other.
**－** No hook reads the number in `[command hook <n>]`.

## Result

2026-11-20, uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_onward.py .guppi/tests/test_casecheck.py .guppi/tests/test_ratified.py: 653 passed; the main transcript of session 0807 (f7321efe) holds two Stop hook feedback records, both `[command hook 6]: onward: …` of the --plan run before the change, and none after the commit 2a058181 at this reading

## History

- 2026-11-20 created · [[decision-case-1035.1]]
- 2026-11-20 status: pending → passed · raw/2026-11-04/0807/ledger.md#L54
