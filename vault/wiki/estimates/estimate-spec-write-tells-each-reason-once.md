---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook gives each of its reasons, a refusal or an error, once a stretch, judged by its own refusals in the transcript, and prints nothing with stop_hook_active set and a transcript it cannot read
method: uv run pytest tests/test_ratified.py -k tells_each_reason_once
origin: raw/2026-10-05/0311/ledger.md#case-644.8
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` has a reason to refuse a reply — a refusal of a Case or an error of its own after it read the payload — with `stop_hook_active` set or not, and reads the transcript at `transcript_path`.

Then:
The hook reads its own refusals in the stretch, the records of the transcript after the person's last message, by `own_refusals` of `guppi/ledger.py`.
**＋** A reason that already stands in one of them is not printed again, by `untold` of `guppi/ledger.py`, the function that judges the lines of the ledger hook.
**＋** The hook exits 2 when a reason not yet given is left, and prints only those reasons on stderr. When none is left, it exits 0 and prints nothing.
**＋** With `stop_hook_active` set and a transcript it cannot read, it prints nothing and exits 0.
**－** What the hook writes, removes or checks does not depend on whether a reason is printed.

## History

- 2026-10-05 created · [[decision-case-644.8]]
