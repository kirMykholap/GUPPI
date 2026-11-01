## Baseline

`uv run --project .guppi guppi test`: exit 0 — 1896 passed, 6 skipped, 1 deselected.

`uv run --project .guppi guppi check`: exit 1 — 10 lint findings:

rules/rule-ask: status: a page with core: true that is draft
rules/rule-case-build: status: a page with core: true that is draft
rules/rule-close: status: a page with core: true that is draft
rules/rule-handoff: status: a page with core: true that is draft
rules/rule-morph: status: a page with core: true that is draft
rules/rule-orchestration: status: a page with core: true that is draft
rules/rule-skill-approve-spec: status: a page with core: true that is draft
rules/rule-skill-hi: status: a page with core: true that is draft
rules/rule-spec-box: status: a page with core: true that is draft
rules/rule-synthesis: status: a page with core: true that is draft

## Expected red
