---
type: decision
case: "481"
status: archived
defer: ["[[rule-prespec-script-skips-code-spans]]"]
superseded_by: ["[[decision-case-589.1]]"]
origin: raw/2026-09-28/1318/ledger.md#case-481
sprint: migration
created: 2026-09-28
tags: []
---

## Context

Case 476.3 made the pre-spec finding look for a letter outside the script of `documentation_lang` in the name, `context` and `problem` of a Case. The `context` and `problem` of every Case hold slugs and paths in code spans, and they are Latin. For `en` this changes nothing. For a documentation language of another script, such as `ru`, each of those slugs is a letter outside the script, so the finding would stand on almost every Case. Work Mode of session 1318 found this while writing the tests of 476.3; the name after the heading's dash is judged alone, which the fix of that session covers, but the code spans are not.

## Problem

The finding cannot tell a word written in the wrong language from a slug or path in a code span, so for a documentation language that is not written in Latin script it reports every Case.

## Deferred

### [[rule-prespec-script-skips-code-spans]]

The pre-spec language finding judges the prose of a name, context or problem without its code spans, so a Latin slug in a code span is no letter outside the script of the documentation language

## History

- 2026-09-28 created · raw/2026-09-28/1318/ledger.md#case-481
- 2026-10-02 superseded by decision-case-589.1 · [[decision-case-589.1]]
- 2026-10-02 archived · superseded
- 2026-10-02 archived · cleanup
