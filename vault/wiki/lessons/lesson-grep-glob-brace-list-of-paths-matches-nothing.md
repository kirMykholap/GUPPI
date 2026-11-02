---
type: lesson
kind: knowledge
root_cause: a Grep over vault/wiki/ with the glob {rules/rule-harness.md,entities/entity-guppi.md}, a brace list of paths with their folders, printed nothing, while **/{rule-harness,entity-guppi}.md and {rule-harness,entity-guppi}.md printed the purpose lines of both pages and the appended !**/decisions/** took nothing from them, so a glob that names pages in a brace list names them by bare file name, with no folder
status: new
source: probe of case-guppi in the build of Case 999, session 0039, vault/raw/2026-11-02/0039/cases/case-999.md context
origin: raw/2026-11-02/0039/ledger.md#L15
sprint: plugin
created: 2026-11-02
tags: [harness, case-build]
---

## Trigger

in the /pre-spec of session 0039 ask-guppi ran two Greps over vault/wiki/ whose glob was a brace list of file paths and got no match where the word stands; case-guppi then tried the forms for the new Render of rule-case-build

## Root cause

a Grep over vault/wiki/ with the glob {rules/rule-harness.md,entities/entity-guppi.md}, a brace list of paths with their folders, printed nothing, while **/{rule-harness,entity-guppi}.md and {rule-harness,entity-guppi}.md printed the purpose lines of both pages and the appended !**/decisions/** took nothing from them, so a glob that names pages in a brace list names them by bare file name, with no folder

## History

- 2026-11-02 created · raw/2026-11-02/0039/ledger.md#L15
