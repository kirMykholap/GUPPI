---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms
method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint
checked: 2026-11-26
origin: raw/2026-10-10/1713/ledger.md#case-756.3
sprint: plugin
created: 2026-10-10
tags: [sprint, readme]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, the person reads `README.md`.
**＋** The person reads it at the root of the branch of the session whose Work Mode wrote it.

Then:
`README.md` says what GUPPI is and what it is for.
**＋** It names the main parts of the project and what each one does.
**＋** It says how to install GUPPI and how to use it.
**＋** It holds a first-person Why on control against cost, an Is it for you section, and how a session goes, from its opening through planning, the Spec, the work and the retro to the handoff and the librarian's run.
**＋** The parts it names are the vault, the harness rendered from the rules, the package with the command `guppi`, and the plugin with the branch `prod`.
**＋** Its install gives the path from GitHub by `#prod`, says that no release has reached `prod` yet, gives the path from a local copy by `guppi ship --allow-draft` and a table of the commands, and its status reads early, opinionated and expensive in tokens, with no figure of cost, beside the MIT license.
**＋** The person says that it describes the project as it stands.

## Result

2026-11-26, /hi of session 1336, README.md at the root of the branch plugin, its sections Why, Is it for you?, How a session goes, Main parts, Install, Use, Status, Contributing and License; the person's answer: the README is fine as it stands, and the person wants to add more information to it, a diagram among it, in a separate Case later

## History

- 2026-10-10 created · [[decision-case-756.3]]
- 2026-10-10 updated: the method names the moment of the reading: the /hi of the session after the one that writes the README · [[decision-case-765]]
- 2026-11-23 updated: the Criterion replaced whole — it reads README.md at the root of the branch of the session that wrote it and names each section the person chose · [[decision-case-1043.1]]
- 2026-11-26 status: pending → passed · raw/2026-11-26/1336/ledger.md#L3
