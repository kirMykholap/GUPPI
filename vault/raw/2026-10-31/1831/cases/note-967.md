# Note — Case 967 (Frontier C10, link graph)

## Questions
Round 1 (answered "agreed" = as recommended):
- Q1 How much this Case covers — rec (a) one Case, a sub-case per part — Answer: (a)
- Q2 Where a hand-off link comes from — rec (b) derived from names in the rendered files, no new field — Answer: (b)
- Q3 Which page describes the command — rec (a) new entity `entity-link-graph` under `entity-guppi` — Answer: (a)
- Q4 How far the command looks — rec (a) one step, both directions, purpose line each — Answer: (a)
Round 2 (answered "agreed" = as recommended):
- Q5 What becomes of the check of prose names — rec (a) no check; not done — Answer: (a)
- Q6 Which texts give a link by a name — rec (b) rendered files and page bodies outside History — Answer: (b)
- Q7 Where the step of `case-guppi` stands — rec (a) frame paragraph, each page and file the Case changes — Answer: (a)
- Q8 How the command is checked — rec (a) new Estimate on entity-link-graph, test + live run — Answer: (a)
- Q9 How the case-guppi step is checked — rec (a) new Estimate on rule-case-build — Answer: (a)
Round 3: Q10 How `case-guppi` gets the output of the command — rec (a) Bash + header hook — Answer: (a)
Round 4: Q10 asked again (same title; docs: a hook allow has no effect in Plan Mode on a non-read-only call) — rec (b) SessionStart hook writes whole graph to an ignored file, builder Greps the block of each page — Answer: (b) "even better"; then the person asked why the graph covers all pages and whether it is read whole. Answered under Fact (no change): the builder reads only the blocks of the pages and files its Case changes, by Grep; the graph covers all pages because the in-links of a page can be found only by reading every page and file. Person: "ok, let's try" — Q10 stays (b).
Round 5 (sent): Q11 Which page describes the hook that writes the graph — rec (a) new Leaf rule `rule-link-graph-at-session-start` under rule-harness, enforcement hook, applies_to entity-link-graph, own Estimate (sub-case 967.3).
Docs read: code.claude.com/docs/en/sub-agents, /permission-modes, /permissions (Hook approvals in plan mode), /hooks (partial).
Hooks: PreToolUse Bash bashguard (heredocs only); PostToolUse event tool, shellwrite; SessionStart event session-start, render --sync; compact recall.

## Read
- case-schema.md, ratification.md, case-example.md (whole); case-966.md (whole)
- ask-guppi.md; rules/entities index Greps
- pages.py 1-120, 212-221; lint.py 105-130, 161-166, 300-380, 455-470; cli.py 45-89; guard.py 1-80; prespec.py 895-940; render.py 70-145, 354-355; bashguard.py whole
- rule-lint, rule-harness, rule-rules-schema 25-84, entity-guppi, rule-case-build (whole), entities/schema.yaml, rule-hook-registry 1-72, rule-guppi-package 1-20
- .claude/settings.json 1-50; .guppi/.gitignore; vault/.gitignore; .gitignore
- estimate-case-build-reads-the-readers-of-a-changed-step (whole); Criteria Then of writes-the-case, reads-by-need-and-in-parts
- tests: test_guppi_package.py (reads .claude/, live pages; asserts .venv/ in .guppi/.gitignore)
- ledger: no error lesson, no addresses mark
- slugs free: entity-link-graph; tags harness, workflow, session, case-build exist

## Design so far
- 967.1 entity-link-graph (Leaf, parent entity-guppi, code_ref .guppi/guppi/links.py), `guppi links <slug|path>`; imports lint.links_of (History dropped), generate.REWORD_PATH_FIELDS, render.render_units, cli.COMMANDS, guard.key/relative; no Decision page read or printed; purpose / root_cause / pattern. entity-guppi purpose + Purpose: new part.
- 967.2 rule-case-build frame paragraph: Grep the block of each changed page/file in the graph file; new estimate on rule-case-build.
- 967.3 (to ask) SessionStart hook `guppi links --write` -> `.guppi/links.md` (ignored); rule-hook-registry pair after render --sync; a hook needs its own Rule (rule-hook-registry Purpose) -> round on which page.

Q10 kept (b) after the Fact. Q11 Which page describes the hook that writes the graph — rec (a) new rule `rule-link-graph-at-session-start` under rule-harness — Answer: (a).

## Open forks
- none

## To do
- Case file written (967.1 command, 967.2 builder step, 967.3 hook). Searches of context re-run, same output. Answer with summary; fix findings by Edit.
- Pre-spec findings 1, 2, 3, 5 fixed: anchor of the whole/parts paragraph, History left out in the then line, context on the Rule-is-a-guard sentence, context on the two case-build Estimates that stand. Siblings 968 and 969 not read (built at the same time).
