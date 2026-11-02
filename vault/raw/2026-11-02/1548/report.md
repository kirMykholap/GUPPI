Librarian report, 2026-11-02 (session 1548; handoff `vault/raw/2026-11-02/1548/handoff.md`)

The run finished and its work is committed as `2a52c139 docs(vault): librarian, 2026-11-02`. `guppi check` prints no line and exits 0. The tree was clean after the commit.

**Pages created (9)**
- decisions 5: `decision-case-1005`, `decision-case-1005.1`, `decision-case-1005.2`, `decision-case-1005.3`, `decision-case-1006`.
- estimates 1: `estimate-case-check-notes-the-files-that-name-what-a-case-changes`, set `passed` by L10.
- lessons 2:
  - `lesson-case-check-names-note-lists-hundreds-of-files` (`new`).
  - `lesson-frontier-closer-appended-without-ticking-the-box` (`clustered`).
- insights 1: `insight-orchestration-frontier-closer-leaves-the-box-open`. The synthesis made it; it stands `open` with severity 2.

**Pages updated (7)**
- rules 2:
  - `rule-case-check`, by 1005.1.
  - `rule-case-build`, by 1005.2 and 1005.3.
- estimates 3:
  - `estimate-case-build-searches-the-names-of-what-it-changes`: `failed → pending`, Criterion, `purpose` and `method` set anew.
  - `estimate-case-build-reads-each-list-of-a-new-member`: `failed → pending`, Criterion set anew.
  - `estimate-orchestration-acknowledging-reply`: `failed → passed` by L7, then `passed → passed` by L9. Its `## Result` holds the text of L9, which is what the handoff asked for.
- insights 1: `insight-orchestration-acknowledging-reply-keeps-headings-in-english` set `actioned` with `addressed_by: [[decision-case-1002]]`, severity 0. It stays live.
- lessons 1: `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`, `new → clustered`.

**Entries marked incomplete or failed:** none. Every entry and every item of `decisions` carries `applied`, and `unparsed: []`.

**Pages archived (2)**
- `lesson-acknowledging-reply-labels-left-in-english` and `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated`.
- `generate` archived them when the Insight was actioned, and `cleanup` moved them to `vault/archive/plugin/2026-11-02/1548/lessons/`.
- `guppi archive` printed nothing, exited 0, and moved or kept no unit.

**Flags**
- `near`: the entry of `lesson-frontier-closer-appended-without-ticking-the-box` carries `near: lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`. Both now stand clustered under the new Insight.
- `rule-case-build` and `rule-orchestration` still carry `status: draft` and `core: true`, but `guppi check` names neither. This answers the handoff's question for C1.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` is listed under Work. The handoff says Cases 1005 and 1006 were ratified again after `/pre-spec`. Whether that reply waits for the person's word is in the session transcript, which I did not read.
- No `failed` Estimate, no MOC candidate and no stale defer. `deferred_by` points to `decision-case-907` and `decision-case-949`, and both pages exist.
- No line on the stderr of `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` or `archive`. No unticked Spec line held `guppi sprint-close --apply`.
- Reads the frame says my job does not need: none. No hook refused a call. No repair was asked or refused.

**Lint total:** `guppi check` exits 0 with 0 lines.

**Index check**
- Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 62 lines. The output was saved to a file, and I read that file.
- L11 matched no line, so it stayed a `create`.
- For L12 the index line did not settle same or near, so I opened `vault/wiki/lessons/lesson-orchestration-closes-a-frontier-line-by-its-closer-alone.md`. Outcome: near, not the same page. It has the same cause but happened in another session (0141 L19), so the entry stayed a `create` with `near`. This follows the run of session 0254, which clustered a repeat of one cause rather than merging it.

**Synthesis**
- Greps: `^(root_cause|deferred_by):` over lessons printed 62 lines; `^(pattern|deferred_by):` over insights printed 16 lines.
- L12 was clustered with `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` under the new `insight-orchestration-frontier-closer-leaves-the-box-open`. That added 3 entries marked `librarian: synthesis`: 1 `create` in insights and 2 `update` in lessons. Neither lesson carries `addressed_by`, so the Insight was born `open`.
- L11 had no pair and stays `new`.

**Ledger read:** `wc -l vault/raw/2026-11-02/1548/ledger.md` counts 12 lines. The yaml covers lines 1–9, 11 and 12, and line 10 is folded into the entry of line 2, so every line is accounted for.

**Brief:** rewritten in full at `c:\PROJECTS\GUPPI\vault\wiki\brief.md`.
- Next session, Cases (6):
  - C1, with the check result.
  - The breadth of the note of names (L11).
  - Defer `estimate-synthesis-keeps-actioned-by-the-mark`.
  - W1 and W2 need a Work Mode run from the Claude Code CLI.
  - Defer `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (from Debt).
  - Defer `estimate-retro-loads-on-a-red-command` (from Debt).
- Next session, Work (1): `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`.
- Next session, Ask the person: none.
