---
type: rule
kind: Leaf
purpose: Prevents a Spec from being approved before its decisions were checked against each other and the vault
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/prespec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-hook-gates]]", "[[estimate-prespec-hook-reports-a-method-that-waits-for-another-session]]", "[[estimate-prespec-hook-reports-a-schema-condition-not-met]]", "[[estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session]]", "[[estimate-prespec-hook-reports-a-create-without-a-required-field]]", "[[estimate-prespec-hook-reports-a-pointer-outside-a-bracket]]"]
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
core: true
---

## Purpose

Prevents a Spec from being approved before its decisions were checked against each other
and the vault. `PreToolUse` on `ExitPlanMode`: in a working session with no `prespec`
line of this session's stamp after its `hi`, `uv run --project .guppi guppi prespec` exits 2 with the reason, which
blocks the approval; the `/pre-spec` call leaves the stamped line through `guppi gate`. With the line, the hook finds the plan file of the session by `plan_path` of `.guppi/guppi/ledger.py`, runs on it the judgment of `--check` — the same function, not a copy — and exits 2 with its findings on stderr while it finds one; a line that opens with `note:` does not block, and with no plan file of the session the exit passes on the line alone (case 561.3). A `prespec` of another stamp or `--------` does not count, and a foreign `session-start` resets nothing (case 136.2). An
ordinary session, one without `/hi`, is not gated: no governance applies there. The
same module serves the skill: `uv run --project .guppi guppi prespec --check <plan>` compares the plan
with the session's ledger lines and frontier (cases 59.1–59.3, 59.6); `/pre-spec` runs it, and the hook runs the same judgment at the exit (case 561.3; named `pretask` until case 261). What `--check` compares, the check the skill `/pre-spec` runs, is written in the module docstring of `.guppi/guppi/prespec.py`, beside its code (case 561.1).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: guppi pretask --check lives here and serves /pre-task (case 66) · [[decision-case-66]]
- 2026-09-14 updated: the ExitPlanMode hook binds the pretask mark by the session's stamp, not by position (case 136.2) · [[decision-case-136.2]]
- 2026-09-20 deferred · [[decision-case-259]]
- 2026-09-20 defer by decision-case-259 superseded · [[decision-case-261]]
- 2026-09-20 renamed from `rule-pretask-hook` · [[decision-case-261]]
- 2026-09-20 updated: renamed to rule-prespec-hook — the hook guppi prespec, the mark prespec, the refusal names /pre-spec (case 261) · [[decision-case-261]]
- 2026-09-20 ref `estimate-pretask-hook-gates` → `estimate-prespec-hook-gates` · [[decision-case-261]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-01 updated: the Purpose points to the module docstring of guppi/prespec.py for what the check compares (case 561.1) · [[decision-case-561.1]]
- 2026-10-01 updated: the hook on ExitPlanMode refuses while the check of the plan prints a finding (case 561.3) · [[decision-case-561.3]]
- 2026-10-01 status: built → draft · cascade
- 2026-10-01 status: draft → built · cascade
- 2026-10-05 estimate estimate-prespec-hook-reports-a-method-that-waits-for-another-session added · [[decision-case-670.4]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 status: draft → built · cascade
- 2026-10-07 estimate estimate-prespec-hook-reports-a-schema-condition-not-met added · [[decision-case-714]]
- 2026-10-07 estimate estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session added · [[decision-case-715]]
- 2026-10-09 estimate estimate-prespec-hook-reports-a-create-without-a-required-field added · [[decision-case-748.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 estimate estimate-prespec-hook-reports-a-pointer-outside-a-bracket added · [[decision-case-807.4]]
- 2026-10-14 updated: the old name stands in the bracket of its pointer · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 status: built → draft · cascade
- 2026-10-15 status: draft → built · cascade
