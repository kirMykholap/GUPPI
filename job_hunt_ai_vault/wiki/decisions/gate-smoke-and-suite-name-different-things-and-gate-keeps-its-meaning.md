---
title: "`gate`, `smoke` and `suite` name different things, and `gate` keeps the meaning it already had"
type: decision
status: current
authority: check-system-naming
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-26

*(the owner selected it, against calling the fast selftest a gate.)*

| name | what it is |
|---|---|
| **gate** | `bash scripts/vault-check.sh` alone. It reads the **live corpus**, builds no sandbox and breaks nothing. Sixteen rules. **21.5 s on a 682-file corpus** |
| **smoke** | a fast run over what the session actually touched. **It does not exist and must be built** ([[the-smoke-runner-is-built-first-thing-next-session]]) |
| **suite** | the full sweep ([[the-selftest-is-a-mutation-test-of-the-gate]]) |

# The word was the whole point

**`gate` already names the thing being checked.** Using it for the checker would put one word on both
sides of the same sentence.

**This project has paid for that exact shape once.** For three days *retrospective* meant both the
end of a session and a sprint-level ritual, and the ambiguity put two live, contradictory answers in
the vault about when `/ingest` runs
([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]],
[[the-end-of-a-session-is-a-retrospective]]).

# Rejected

**Rejected: calling the fast narrowed selftest run "the gate".** It was the natural shorthand and it
is the collision above.

*(This page's title read "are three names for three things" until the gate's own title rule caught it
the same day — a title carries no measurable quantity, and the table above is the list
([[a-title-names-what-is-counted-instead-of-counting-it]]).)*
