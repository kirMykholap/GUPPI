Librarian run, 2026-11-02, session 0254 (`vault/raw/2026-11-02/0254/handoff.md`). All steps ran and the vault is committed as `0040116f docs(vault): librarian, 2026-11-02`. The tree is clean after the commit. `guppi check` now prints 3 lines, not the 1 the handoff expected: `rule-orchestration` blocks the clean build too.

**Pages created (4)**
- decisions 1: `decision-case-1001`
- lessons 2: `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated` (`clustered`) and `lesson-hook-block-reason-is-not-shown-in-the-phone-app` (`new`)
- insights 1: `insight-orchestration-acknowledging-reply-keeps-headings-in-english` (`open`, from the synthesis)

**Pages updated (10)**
- rules 5:
  - `rule-morph`: its `core` line is removed.
  - `rule-permissions` and `rule-guppi-config`: their Purposes are reworded.
  - `rule-clean-branch`: `built → draft` by the cascade.
  - `rule-close`: `draft → built` by the cascade.
- entities 1: `entity-sprint-plugin`, the milestone item of `rule-morph`.
- estimates 3:
  - `estimate-clean-branch-refuses-a-draft-core-page`: Criterion and `method` replaced; `pending`.
  - `estimate-orchestration-acknowledging-reply`: `pending → failed`.
  - `estimate-close-reports-the-run`: `pending → passed`.
- lessons 1: `lesson-acknowledging-reply-labels-left-in-english`, `new → clustered`.

**Incomplete or failed entries:** none. Marks: 13 `applied` (12 entries and 1 `decisions` item); no `exists`, `incomplete`, `near` or `merged`; `unparsed: []`.

**Pages archived:** none. `guppi cleanup` printed `0 page(s) moved`. `guppi archive` printed nothing, exited 0 and moved no unit. It kept `raw/2026-11-02/0039` and `raw/2026-11-02/0254` because it looks only at units dated before the run day, and 0254 is the session of the run.

**Handoff's instructions**
- Checked after `generate`:
  - `rule-morph` carries no `core:` line. A Grep for `^core:` in `rule-morph`, `rule-skill-merge-main` and `rule-skill-pr-review` printed nothing.
  - All four `replace` texts were applied, nothing on stderr: one in `entity-sprint-plugin`, one in `rule-permissions`, two in `rule-guppi-config`.
  - `guppi check` printed 3 lines, not 1. The `rule-morph` line is gone and the `rule-skill-approve-spec` line stays. Two lines are new: `rule-orchestration` (`core: true`, `draft`) draws `status: a page with core: true that is draft`, and `estimate-orchestration-acknowledging-reply` draws `unread: failed`.
- No instruction asked to repair an entry. No read asked for was refused.

**Index check:** the yaml holds no `create` entry other than an Estimate, so I ran no Grep for it.

**Synthesis**
- Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 61 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
- `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated` is clustered with `lesson-acknowledging-reply-labels-left-in-english` under the new Insight. I added 3 entries marked `librarian: synthesis`: 1 `create` in insights and 2 `update` in lessons.
- `lesson-hook-block-reason-is-not-shown-in-the-phone-app` has no pair and stays `new`.

**Pages opened to judge the synthesis** (the index line did not settle it)
- `vault/wiki/lessons/lesson-acknowledging-reply-labels-left-in-english.md`: same root cause, clustered. In both lessons the agent copies the English heading `## Frontier` as a literal.
- `vault/wiki/lessons/lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab.md`: not clustered. It is about the band a mod draws, a different channel from a blocked prompt.

**Ledger read (one, for the `Work` line):** `vault/raw/2026-11-02/0254/ledger.md` has 9 lines. The yaml holds entries for lines 1–9, so every line is accounted for.

**Flags**
- `failed` Estimate: `estimate-orchestration-acknowledging-reply` (L4).
- Contradiction: the handoff says `rule-skill-approve-spec` is the only page that blocks the clean build. `guppi check` also names `rule-orchestration`, whose Estimate `estimate-orchestration-acknowledging-reply` is `failed`.
- `rule-clean-branch` went `built → draft` by the cascade. It carries no `core` and draws no lint line.
- The box at line 169 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md` (`read estimate-close-reports-the-run`) is still unticked, though that reading passed by L8.
- I judged that Case 1001 is the event `estimate-case-build-reads-each-list-of-a-new-member` waits for, so I listed that reading under Work. This is my judgment, flagged in the brief.
- Neither the handoff nor the ledger says whether the reply after `/pre-spec` waited for the person's word. So `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` stays in Readings due.
- Every script printed nothing on stderr: materialize, generate, cleanup, render, sprint, backlog, glossary and archive. No unticked Spec line held `guppi sprint-close --apply`.
- No MOC candidate. No stale defer.
- Reads the frame says my job does not need: none.
- No hook refused a call.

**Lint total:** `guppi check` exits 1 with 3 lines: `status: a page with core: true that is draft` on `rule-orchestration` and on `rule-skill-approve-spec`; `unread: failed` on `estimate-orchestration-acknowledging-reply`.

**Next session** (in `vault/wiki/brief.md`)
- Cases (2):
  - The `failed` `estimate-orchestration-acknowledging-reply`: does the rule need a change, or only a new reading?
  - The handoff's line on the blocking page, with the `rule-orchestration` contradiction.
- Work (5):
  - Readings of `estimate-clean-branch-refuses-a-draft-core-page`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-case-build-searches-the-names-of-what-it-changes` and `estimate-case-build-reads-each-list-of-a-new-member`.
  - The unticked box at line 169 of the archived 2227 Spec.
- Ask the person (3): `estimate-skill-approve-spec-takes-the-spec`, `estimate-orchestration-names-the-typed-approval`, `estimate-spec-box-runs-a-conserved-spec`.
