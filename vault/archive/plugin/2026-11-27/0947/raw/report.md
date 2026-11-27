Librarian run for session 0947 (2026-11-27) is done. The vault is committed as eb4ab3e9 `docs(vault): librarian, 2026-11-27`, and the tree is clean after the commit.

**Pages created** (`git status`, `log.md`)
- decisions 17: `decision-case-1076`, `1077`, `1077.1`–`1077.5`, `1078`, `1078.1`–`1078.4`, `1079`, `1079.1`, `1079.2`, `1080`, `1081`
- estimates 9: two are `pending` (`estimate-guppi-repository-readme-shows-the-first-sketch`, `estimate-spec-write-shows-the-map-in-the-plan-view`) and seven are `passed`
- lessons 1: `lesson-frontier-line-closed-in-two-edits`, now `clustered`

**Pages updated**
- entities 2: `entity-guppi-repository`, `entity-sprint-plugin`
- estimates 5:
  - `passed`: `estimate-case-build-names-a-stale-line-of-another-case`, `estimate-guppi-repository-readme-shows-the-path-of-a-decision`, `estimate-brief-written`
  - `pending`: `estimate-carry-over-writes`, `estimate-hi-writes-frontier`
- insights 1: `insight-orchestration-frontier-closer-leaves-the-box-open`
- rules 9: `rule-brief`, `rule-carry-over`, `rule-case-build`, `rule-clean-branch`, `rule-orchestration`, `rule-prespec`, `rule-skill-hi`, `rule-spec-write`, `rule-work-mode`

**Entries marked incomplete or failed:** none. All 47 entries and decision records carry `applied`. No entry is marked `near` and `unparsed: []`. The two defers (1080, 1081) carry `exists: true`.

**Pages archived:** `guppi cleanup` moved 0 pages. `guppi archive` moved the unit `raw/2026-11-26/2333` to `archive/plugin/2026-11-26/2333/raw` and printed nothing on stderr. It kept `raw/2026-11-27/0947` because that is the session of this run.

**Index check and synthesis**
- Every `create` entry is an Estimate, so no category Grep ran for a create.
- For the one `lesson` entry I ran two Greps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines. None is the same or near.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- I opened `vault/wiki/insights/insight-orchestration-frontier-closer-leaves-the-box-open.md` because its index line did not settle whether it shares the lesson's root cause. Outcome: the lesson joins it. Both cases are a Frontier line closed by partial edits instead of one edit of the whole line.
- I added two entries marked `librarian: synthesis`:
  - an `update` of the Insight that adds the child and sets `status: open`. It was `actioned` by `decision-case-1069.1`, and the lesson entry carries no `addressed_by`, so `addressed_by` stays as it is.
  - an `update` of the lesson to `clustered` under that Insight.

**Ledger read:** `vault/raw/2026-11-27/0947/ledger.md`, read once for its line count and for lines the yaml does not account for. It has 35 lines and every one is accounted for: lines 1–26, 30 and 35 are entries, and lines 27, 28, 29, 31, 32, 33 and 34 are folded into the `create` entries of their Estimates.

**Handoff instructions:** I carried out all of them and refused none.
- Each `old` of 1077.2 (three) and 1078.3 (two) hit `rule-orchestration` once (Grep) before `generate`. The yaml holds 1077.2 before 1078.3.
- `code_ref` holds `plugin/assets/GUPPI.png`.
- The `rule-clean-branch` update (ledger line 26) is applied.

**Hook refusal:** `frontierguard` refused one Bash command of mine because its text named `frontier.md`. That command counted the hits of the `old` strings. I did the check again with the Grep tool, as the refusal says.

**Flags raised**
- One read my frame says the job does not need: a `grep` of `stop:` over `vault/raw/2026-11-27/0947/spec.md`, which also printed lines of the Cases. I made it for the Next session, to see whether the event of `estimate-work-mode-runs-the-style-check-before-a-stop` stands in session 0947. It does: ticked `stop:` tasks at lines 505, 671, 674 and 715. The handoff did not ask for this read.
- The synthesis reopened `insight-orchestration-frontier-closer-leaves-the-box-open`, and it now stands in `backlog.md`. The backlog went from 4 to 7 items.
- Handoff observation: the brief of session 2333 named an event for `estimate-orchestration-leaves-the-number-to-case-guppi` that did not occur.
- Handoff observation: for `estimate-case-build-names-a-stale-line-of-another-case`, the branches of the Criterion where another Case or the Case itself needs a fix did not arise.
- Handoff note: Case 1081 defers `rule-spec-write`, which 1078.1 changes in the same session.
- Handoff observation: `guppi agents` counts each call made inside Code Mode code as a call, so its count does not compare the two sessions. The two measured sessions also ran at the same time.
- Handoff note: the Excalidraw board could not be read by WebFetch, and many names on the exported picture are outdated.
- `generate`, `sprint-close` (no unticked Spec line holds it, so it did not run), `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed no line on stderr.

**Lint total:** `guppi check` exited 0 with no line, both before the brief and at the close.

The new brief is `c:\PROJECTS\GUPPI\vault\wiki\brief.md`. Its Next session holds 3 Cases, 1 Work item (`estimate-work-mode-runs-the-style-check-before-a-stop`) and 1 Ask line (`estimate-guppi-repository-readme-shows-the-first-sketch`). The yaml with the synthesis entries is `c:\PROJECTS\GUPPI\vault\raw\2026-11-27\0947\materialize.yaml`.
