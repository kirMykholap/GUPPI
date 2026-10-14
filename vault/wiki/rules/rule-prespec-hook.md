---
type: rule
kind: Leaf
purpose: Prevents a Spec from being approved before its decisions were checked against each other and the vault
status: built
enforcement: hook
implementation_ref: [guppi/prespec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, hooks, harness]
core: true
---

## Purpose

Prevents a Spec from being approved before its decisions were checked against each other
and the vault. `PreToolUse` on `ExitPlanMode`: in a working session with no `prespec`
line of this session's stamp after its `hi`, `uv run guppi prespec` exits 2 with the reason, which
blocks the approval; the `/pre-spec` call leaves the stamped line through `guppi gate`. With the line, the hook finds the plan file of the session by `plan_path` of `guppi/ledger.py`, runs on it the judgment of `--check` — the same function, not a copy — and exits 2 with its findings on stderr while it finds one; a line that opens with `note:` does not block, and with no plan file of the session the exit passes on the line alone. A `prespec` of another stamp or `--------` does not count, and a foreign `session-start` resets nothing. An
ordinary session, one without `/hi`, is not gated: no governance applies there. The
same module serves the skill: `uv run guppi prespec --check <plan>` compares the plan
with the session's ledger lines and frontier; `/pre-spec` runs it, and the hook runs the same judgment at the exit. What `--check` compares, the check the skill `/pre-spec` runs, is written in the module docstring of `guppi/prespec.py`, beside its code.

## History

- 2026-10-14 shipped with GUPPI
