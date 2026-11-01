The librarian run for session 1721 is committed (`d749763a docs(vault): librarian, 2026-11-01`) and the tree is clean. `guppi check` still prints 10 lines and exits 1. Each line is a core page that stands `draft`, and the new `rule-skill-approve-spec` is one of them.

**Pages created (19):**
- decisions 13: 982, 982.1, 982.2, 982.3, 983, 984, 985, 986, 987, 987.1, 987.2, 988, 989
- rules 1: `rule-skill-approve-spec` (`draft`, `core: true`)
- estimates 2: `estimate-skill-approve-spec-takes-the-spec` and `estimate-orchestration-names-the-typed-approval`, both `pending`
- lessons 2: L34 (`clustered`) and L35 (`new`)
- insights 1: `insight-frontier-line-closed-by-the-case-built-on-its-item` (`open`, severity 3)

**Pages updated:**
- rules 13: 11 by Cases, plus `rule-plan-mode` (it gained the child `rule-skill-approve-spec`) and `rule-ratification` (`draft → built` by the cascade).
- entities 1: `entity-glossary`.
- estimates 10: 4 went to `passed` (L30–L33) and 6 stay `pending`.
- insights 1: `insight-plugin-cli-withholds-approval-of-a-long-plan` went `open → actioned`, with `addressed_by: decision-case-987.1`.
- lessons 2: both now `clustered` under the new Insight.

**Marks:** all 39 entries and all 13 `decisions` items are `applied`. No entry is marked `incomplete`, `failed`, `exists` or `unparsed`. There are 2 `near` marks and 4 `librarian: synthesis` entries.

**Pages archived:**
- Cleanup moved 3 pages: `decision-case-957` (superseded by 987.1) and the two lessons of the actioned Insight, `lesson-plugin-cli-withholds-approval-of-a-long-plan` and `lesson-plugin-cli-withholds-approval-in-every-window`.
- `guppi archive` printed nothing on stdout or stderr. It moved no unit and gave no reason for keeping `vault/raw/2026-11-01/0141/`, which stays in `raw/`.

**Handoff instructions:** I checked all four and carried them all out; none asked for a repair.
- `estimate-close-reports-the-run` and `estimate-handoff-dispatches` no longer carry `deferred_by`, and `backlog.md` no longer lists them.
- The render wrote `.claude/skills/approve-spec/SKILL.md`, and `.claude/settings.json` now holds `guppi spec --typed` under `UserPromptSubmit`.
- The paired updates of `rule-orchestration`, `rule-case-build` and `rule-spec-box` were all applied.
- The CLI-approval Insight now stands `actioned` with `addressed_by: decision-case-987.1`.

**Index check:**
- `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 89 lines. I marked `rule-skill-approve-spec` `near: rule-spec-capture`, because the hook that takes the plan file on `/approve-spec` is set in `rule-spec-capture`.
- `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 61 lines. I marked L34 `near: lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case`. L35 has no near page.
- No entry was merged.

**Synthesis:**
- The lessons Grep printed 61 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14.
- L34 forms a new Insight with two older lessons. All three close a Frontier line `· case N` because a Case was built on the item, though no decision line of that Case takes the item off its list.
- L35 joined nothing. No index line names two rule texts that ask opposite forms of the same reply.

**Pages I opened:**
- `vault/wiki/lessons/lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case.md` and `vault/wiki/lessons/lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page.md`. I read their Trigger and Root cause because the index lines did not settle whether they share L34's root cause. Both share it and are now clustered.
- `vault/raw/2026-11-01/1721/ledger.md`, the one read for the `Work` line. It has 35 lines and the yaml has one entry for each, so the yaml accounts for every line.

**Flags:**
- The two `near` marks above.
- A contradiction (L35): the hook of `rule-prespec-onward` asks the reply to open with `STOP:`, while the check of `rule-case-check` notes any line before a showing. The handoff's "For the next session" already carries it.
- A count mismatch: the handoff's Debt says 59 boxes wait for the librarian. The committed `spec.md` held 50 unticked boxes; this run ticked 44 and 6 `read` boxes stay.
- Lint: the 10 core `draft` pages (`rule-ask`, `rule-case-build`, `rule-close`, `rule-handoff`, `rule-morph`, `rule-orchestration`, `rule-skill-approve-spec`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`).
- A read beyond the frame: I grepped the `status:` line of `vault/wiki/decisions/decision-case-957.md` to report what the cascade did to it in Where things stand. The handoff did not ask for it.
- Nothing else: no script wrote to stderr, no hook refused a call, there are no stale defers and no Estimate is `failed`.

**Lint total:** 10 (`guppi check`, exit 1).

Files are in `c:\PROJECTS\GUPPI\vault\`:
- wiki\brief.md
- raw\2026-11-01\1721\materialize.yaml
