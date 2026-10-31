Librarian run for session 2026-10-31/2307 is done. It is committed as 5d534880 `docs(vault): librarian, 2026-10-31`, and `git status` printed nothing after the commit. No entry failed, and no script printed anything on stderr. `guppi check` printed 15 lines (exit 1), including one new `ref` finding on a lesson created this run.

**Pages created (10)**
- decisions: 5 (`decision-case-972` to `decision-case-976`)
- estimates: 3 (`estimate-prespec-hook-reports-a-wait-off-its-form` passed; `estimate-sprint-plugin-check-finds-no-bare-slug-link` and `estimate-case-build-reads-the-readers-of-a-new-files-folder` pending)
- lessons: 2 (`lesson-ledger-reading-writes-a-bare-wikilink` and `lesson-orchestration-shows-a-round-after-own-text`, both `new`)

**Pages updated (19)**
- estimates: 10
  - four readings went pending to passed: `estimate-close-commits`, `estimate-estimates-schema-checked`, `estimate-materialize-lifts-a-create-value-by-the-schema`, `estimate-link-graph-at-session-start-writes-the-file`
  - `estimate-link-graph-prints-the-neighbours` (Case 973)
  - `estimate-rules-schema-checked`, now pending (Case 975)
  - the four Estimates deferred by Case 976
- rules: 6. Cases changed `rule-case-build` and `rule-rules-schema`. `rule-prespec-hook` gained an Estimate in its list. The cascade moved `rule-estimates-schema`, `rule-link-graph-at-session-start` and `rule-materialize` from draft to built, and `rule-rules-schema` from built to draft.
- entities: 2 (`entity-glossary`; `entity-sprint-plugin` gained an Estimate in its list)
- insights: 1 (`insight-case-build-changes-a-step-without-reading-its-readers`, now actioned by `decision-case-974`)

**Entry marks**
- `materialize` wrote 20 entries for 2307 and added 0 to the yamls of 0128, 0431 and 1831.
- All 19 entries of the 2307 yaml are `applied`. 4 carry `exists` (the defers of ledger lines 14–17).
- No entry is `failed`, `incomplete`, `near`, `librarian` or `merged`, and `unparsed: []`.
- Ledger: I read `vault/raw/2026-10-31/2307/ledger.md` once to count its lines. It has 20 lines. The yaml covers lines 1–17, 19 and 20, and line 18 is folded into the `create` of line 5, so every line is accounted for.

**Archived**
- `cleanup` moved `lesson-case-build-names-a-file-without-the-readers-of-its-folder` to `vault/archive/plugin/2026-11-01/2307/lessons/`, after its Insight went actioned.
- `guppi archive` moved three units: `raw/2026-10-31/0128`, `raw/2026-10-31/0431` and `raw/2026-10-31/1831`, each to `archive/plugin/2026-10-31/<id>/raw`.
- It kept session 2307, the session of this run.
- The 0431 and 1831 Specs it moved still hold unticked `read` boxes: 4 in 0431 and 5 in 1831. The brief gives their archived paths.

**Index check and synthesis**
- Index check: every `create` entry was an Estimate, so I ran no category Grep.
- Synthesis Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 59 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
- Neither new lesson shares a root cause with a lesson or an Insight, so I added no entry and both stay `new`.
- I opened no page to settle same, near or a cluster.

**Pages opened because a script named them in an error**
- `guppi check` named `lesson-ledger-reading-writes-a-bare-wikilink` in a `ref` finding. I searched the page for `[[`: line 18, its `## Root cause`, holds the bare `[[slug]]` copied from ledger line 19. That is the very form the lesson records, and lint reads it as a link to a page. The page stays as generated.

**The handoff's checks** (by `git diff` and Grep)
- Case 973: only the `## Result` and one History line of `estimate-link-graph-prints-the-neighbours` changed, and `[[slug]]` now stands in a code span. Its status, Criterion and method did not change.
- Case 974: the Insight is actioned and its lesson moved to the archive.
- Case 975: each of the three new texts stands once in its page and once in the rendered file (`vault/wiki/rules/schema.yaml`, `vault/wiki/glossary.md`).
- Case 976: the `deferred_by` lists now end with `decision-case-976`.
- I refused no instruction of the handoff.

**Flags**
- 3 failed Estimates, all deferred by Cases 971 and 976: `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-shows-the-built-case`.
- The `ref` finding on `lesson-ledger-reading-writes-a-bare-wikilink` above. The brief lists it under Cases of the next session as a defect.
- Stale defers in `backlog.md`: `rule-spec-box` (put off in 8 sessions), `estimate-orchestration-shows-the-built-case` (4), `rule-ratification` (2), `estimate-case-build-reads-each-list-of-a-new-member` (2), `estimate-orchestration-names-related-cases-in-the-dispatch` (2).
- The `backlog.md differs from its sources` line from the handoff's baseline is gone from `guppi check` after `guppi backlog` rewrote the file.
- No MOC candidates and no contradictions seen. I made no read outside what the frame says my job needs.

**Lint total:** `guppi check` printed 15 lines, exit 1:
- 11 `status: a page with core: true that is draft`
- 3 `unread: failed` (the three failed Estimates)
- 1 `ref` (the new lesson)

The new brief is at `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
