---
type: lesson
kind: error
root_cause: deferred_section of .guppi/guppi/ratified.py takes any Case whose lines in a reply are all defer for a short-form Case and reads its then fence from the reply, while a Case case-guppi builds holds its defers as task lines in its file, so a full Case with only defer lines passes the case-file check and fails the ratification hook until the main agent shows it again in the short form
status: new
origin: raw/2026-10-17/0027/ledger.md#L59
sprint: plugin
created: 2026-10-17
tags: [hooks, case-build]
---

## Trigger

Case 876, built by case-guppi with only defer lines, was ratified, and the Stop hook guppi ratified refused the acknowledging reply with "case 876: no fence tagged then with its defer items"; case-guppi could not add the fence to the case file, since the case-file check read its lines as task lines and refused them

## Root cause

deferred_section of .guppi/guppi/ratified.py takes any Case whose lines in a reply are all defer for a short-form Case and reads its then fence from the reply, while a Case case-guppi builds holds its defers as task lines in its file, so a full Case with only defer lines passes the case-file check and fails the ratification hook until the main agent shows it again in the short form

## History

- 2026-10-17 created · raw/2026-10-17/0027/ledger.md#L59
