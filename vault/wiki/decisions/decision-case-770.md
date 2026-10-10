---
type: decision
case: "770"
status: current
create: ["[[estimate-cleanup-files-a-session-by-its-sprint]]"]
origin: raw/2026-10-10/1913/ledger.md#case-770
sprint: plugin
created: 2026-10-10
tags: [harness, librarian, sprint]
---

## Problem

In the session that opens a sprint, `guppi cleanup` files archived pages under the closed sprint, since it reads `sprint.md` before `guppi sprint` rewrites it.

## Recommend

- **Where does cleanup take the sprint name from?**
  - Recommended: (a) the session's own record, as `guppi archive` does: the `sprint` field of the `materialize.yaml` of the session of the run, else `sprint.md`, in one function that `guppi archive`, `guppi cleanup` and `guppi generate` import.
  - Answer: agreed, (a).
- **What happens to the two pages already filed under `migration`?**
  - Recommended: (a) move them in Work Mode to `vault/archive/plugin/2026-10-10/1713/decisions/`.
  - Answer: agreed, (a).
- **How is the fix checked?**
  - Recommended: (a) a new check of its own, `estimate-cleanup-files-a-session-by-its-sprint`, by `uv run pytest tests/test_cleanup.py -k sprint`; `estimate-cleanup-moves` stays as it is.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fix of a finding of `/pre-spec`: name `estimate-generate-writes`, whose Criterion says a created page takes the `sprint` of the yaml, and keep it true.
  - Taken: `given` names it, and `context` says why its Criterion stays true under the shared function.

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#case-770
