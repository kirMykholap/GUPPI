---
type: insight
pattern: case-guppi builds a Case on a fact of how an outside tool behaves — what GitHub accepts, which config file pytest reads from the root — that neither the round nor /pre-spec checked, so the fact proves false in Work Mode after the person ratified the Case
status: open
children: ["[[lesson-case-build-recommended-an-unchecked-github-fact]]", "[[lesson-case-build-names-a-pytest-config-the-root-run-does-not-read]]"]
severity: 2
origin: raw/2026-10-15/1959/ledger.md#L73
sprint: plugin
created: 2026-10-15
tags: [tests, case-build, ci, workflow]
---

## Pattern

Two lessons, one cause. In session 1753 case-guppi recommended for Case 804 an option that rested on whether GitHub accepts the built-in Actions account on the bypass list of a ruleset, said it could not read that, and nothing checked GitHub's documentation; the stop task failed with HTTP 422 and Case 804 was built again. In session 1959 Case 823.1 put the pytest marker live and its addopts in .guppi/pyproject.toml without checking which config file a run of pytest from the root of the repository reads; the first full test run ran the live test and warned of an unknown mark, and Work Mode added the same lines to the root pyproject.toml. In both, a fact of a tool outside the vault was taken as given and was not checked before ratification.

## Proposal

One sentence in rule-case-build that when a recommended option rests on how an outside tool behaves — a service, a test runner, a client — case-guppi checks that behaviour in its documentation or by a run before the Case is written, and names the source in context; and that /pre-spec asks ask-guppi for that source. A suggestion, not a decision.

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#L73
