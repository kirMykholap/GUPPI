---
type: decision
case: "968"
status: current
create: ["[[estimate-materialize-lifts-a-create-value-by-the-schema]]"]
update: ["[[rule-case-protocol]]"]
origin: raw/2026-10-31/1831/ledger.md#case-968
sprint: plugin
created: 2026-10-31
tags: [harness, schema, session, workflow, ledger]
---

## Problem

A field of a new page whose allowed value is not text, such as `core: true`, reaches the Spec and the page as text, so the page is born without that value, and `case-schema.md` gives no form that avoids it.

## Recommend

- **Where the boolean of a `create` is fixed**
  - Recommended: (c) one shared function, which the copy hook, the librarian's lift and `/pre-spec` import, loads a value as YAML for a field whose allowed values in the schema hold no text.
  - Answer: (c), as recommended.
- **What happens to a value outside the allowed list**
  - Recommended: (a) the hook refuses it with a line that names the field and its allowed values.
  - Answer: (a), as recommended.
- **When the session also changes a page schema**
  - Recommended: (a) the allowed values are still read from the schema on disk.
  - Answer: (a), as recommended.
- **Whether `case-schema.md` describes the form**
  - Recommended: (a) one sentence in the Render of `rule-case-protocol`.
  - Answer: (a), as recommended.
- **How the change is checked**
  - Recommended: (a) a new Estimate on `rule-materialize`.
  - Answer: (a), as recommended.

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#case-968
