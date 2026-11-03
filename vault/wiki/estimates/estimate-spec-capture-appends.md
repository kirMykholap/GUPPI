---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-capture]]"
method: "pytest in .guppi/tests/test_spec.py with piped payloads against a temp vault; by hand, at the approval of a plan in a session: the spec.md of that session read against the Criterion"
checked: 2026-09-27
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, workflow]
core: true
---

## Criterion

When:
`ExitPlanMode` is approved, and `uv run --project .guppi guppi spec` runs on its `PostToolUse` with the plan in `tool_response.plan`.

Then:
In a session with a `hi`, the plan is appended to `raw/<hi date>/<hi HHMM>/spec.md` — a `---` separator when the file has content, the stamp `<!-- approved HH:MM:SS · session xxxxxxxx -->` and the plan text — once, even when the hook runs twice.
**＋** A second approval of the same session appends under `---` and its stamp.
**＋** The hook changes nothing that stands in the file: earlier documents, the sections the `Stop` hook of `rule-spec-write` wrote and a `## Deferred` section stay as they are, and `uv run --project .guppi guppi materialize` reads their Cases.
**－** Without a `hi` the hook exits 2 naming the session, and the file is untouched.
**－** The payload of another tool writes nothing: exit 0.

## Result

2026-09-27, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
