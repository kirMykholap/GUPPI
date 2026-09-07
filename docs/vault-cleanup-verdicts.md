# Cleanup verdicts — one line per family

Hand-written. `scripts/build-families-table.py` reads this file and prints each verdict into
`docs/vault-cleanup-families.md`, which is derived and overwritten whole. That is why the verdicts
live here: a verdict written into the table would be destroyed by the next regeneration, and a
generator recovering one by parsing its own previous output breaks silently.

Format is `- <family name>: <verdict>`, and the family name is spelled exactly as
`job_hunt_ai_vault/authority.md` spells it.

## The three verdicts of part one

- **vault-facing** — the family's text is addressed to the vault's own pages. It becomes one page
  in `wiki/rules/` under `render: authority`, carrying the `authority:` of one of its decisions,
  and the hook hands it over when a page carrying that slug is read. Its decisions are released to
  `archive/`.
- **harness-facing** — the text belongs in a harness or product file and reaches a reader only by
  being rendered into it, which needs `governs:` and a written region. That is a different kind of
  work and a different session. Nothing is built now and **its decisions stay where they are**.
- **none** — the family produces no rule at all, and its decisions stay where they are.

**Only `vault-facing` releases decisions.** The repeal frees a prohibition once the family rule
carrying its clause exists, and the other two verdicts produce no such rule.

## The test applied

*Would somebody touching a page of the vault, carrying a slug of this family, need this text?* If
yes it is `vault-facing`. If the text is instead an instruction to a session, an agent, a script or
the product, it reaches its reader by being rendered into that file and is `harness-facing`.

## What has been acted on

**The 18 `vault-facing` families were discharged on 2026-08-31.** Each became a page in
`wiki/rules/`, and 129 of their decisions moved to
`archive/2026-08-31/2026-08-31-the-families-become-rules/pages/`. **Two did not and never will**:
both carry `target_kind: repeal`, and the archiver refuses such a decision absolutely, because once
the page it cancelled is gone that decision is the only live carrier of the fact. So two
`vault-facing` families still appear in part one of the table holding one prohibition each, and that
is correct rather than unfinished.

**The 35 `harness-facing` families are untouched**, with 164 prohibitions still in
`wiki/decisions/`. Their verdicts stand and are the next session's input.

## Part one

- where a rule's text is sent: vault-facing
- draining a folder into the archive: vault-facing
- retiring a page: vault-facing
- the feedback loop back to the librarian: harness-facing
- a decision's own lifecycle — what it declares, and what closes it: vault-facing
- the sprint and the work that belongs to it: harness-facing
- admitting a frontmatter field: vault-facing
- the ingest: harness-facing
- the per-folder schema: vault-facing
- the selftest of the vault's own scripts: harness-facing
- the tag dictionary and the two languages: vault-facing
- what a page is called and what kind it is: vault-facing
- what the owner said, and what was put in his mouth: vault-facing
- who may write the vault: harness-facing
- a rule page and the slice that travels: vault-facing
- finding a page in this store: harness-facing
- the end of a session: harness-facing
- line endings: harness-facing
- the journal a session writes: harness-facing
- the no-quantity rule: vault-facing
- the pre-task ritual: harness-facing
- the repository's CLAUDE.md: harness-facing
- how the owner is asked: harness-facing
- the brief a session starts from, and what goes stale: harness-facing
- the form of a reply, and the frontier it opens with: harness-facing
- the gate: harness-facing
- the region a rule renders into: vault-facing
- the vacancy table: harness-facing
- a copy of a list drifts: vault-facing
- a file the repository generates: harness-facing
- a number this project quotes: vault-facing
- an advisory rather than a red verdict: harness-facing
- the front end's stack: harness-facing
- the hooks that refuse: harness-facing
- the hooks that stand around a session: harness-facing
- the two job sites: harness-facing
- what `/vault-lint` looks for, and the axes it has not got: harness-facing
- a collection run: harness-facing
- dispatching an agent: harness-facing
- how a measurement is written down: vault-facing
- the permission mode and the approved scope: harness-facing
- a deferral with a proposal behind it, and the decision nobody compiled: vault-facing
- a vacancy that disappeared: harness-facing
- renaming a page: vault-facing
- the harness transcript and what is read out of it: harness-facing
- the injector: harness-facing
- the prose this project writes: harness-facing
- the two pages and how they update themselves: harness-facing
- what actually reaches a subagent: harness-facing
- what the vault is and what its answers are worth: vault-facing
- a dependency of this repository: harness-facing
- the pre-task ledger: harness-facing
- the shell this repository is driven from: harness-facing
