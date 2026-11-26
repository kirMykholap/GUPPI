---
type: estimate
kind: QA
status: pending
target: "[[entity-guppi-repository]]"
purpose: Whether README.md explains the terms it uses, shows the path of one decision from the person's answer to the rendered harness file in a Mermaid diagram, and shows one short example question of a round, as the person confirms
method: "by hand, after the handoff of the session whose Work Mode writes the new parts of README.md: the person's answer on README.md, read at the root of the branch of that session at a /hi after that handoff; the estimate line keeps the person's answer"
origin: raw/2026-11-26/2333/ledger.md#case-1074
sprint: plugin
created: 2026-11-26
tags: [readme, github]
---

## Criterion

When:
The person reads `README.md` at the root of the branch of the session whose Work Mode wrote its new parts.

Then:
`README.md` has a section that explains the terms it uses: Case, Frontier, Spec, Estimate, ratify, vault page and librarian.
**＋** A section says what one signed decision leaves: a line in the ledger of the session, a part of the Spec, a vault page after the librarian's run and, for a rule, the harness file rendered from it.
**＋** That section holds a diagram of that path, from the person's answer to the harness file that the hooks enforce in the next session.
**＋** The diagram stands in `README.md` as a fenced block tagged `mermaid`, which GitHub draws as a picture.
**＋** A section shows one shortened question of a round: its title, what holds now, two options and the recommended answer.
**＋** The person says that the new parts explain GUPPI to a newcomer.
**－** No section that `README.md` holds today is removed.

## History

- 2026-11-27 created · [[decision-case-1074]]
