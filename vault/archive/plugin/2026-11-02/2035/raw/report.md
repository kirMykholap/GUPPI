Librarian, 2026-11-02, session 2035. All 13 entries of `vault/raw/2026-11-02/2035/materialize.yaml` applied with nothing on stderr from any script. The commit is `806f2bb1 docs(vault): librarian, 2026-11-02`, and the tree is clean after it.

**Pages created (10):**
- **decisions (7):** `decision-case-1007`, `decision-case-1008`, `decision-case-1009`, `decision-case-1010`, `decision-case-1010.1`, `decision-case-1010.2`, `decision-case-1010.3`.
- **estimates (1):** `estimate-case-check-sends-one-note-for-a-broad-name`, `passed` by L11.
- **lessons (2):** `lesson-orchestration-defer-reply-frontier-heading-in-english` (`clustered`) and `lesson-ship-test-comment-writes-a-bare-case-reference` (`new`).

**Pages updated (8):**
- **rules (2):** `rule-case-check` by 1010.1 and 1010.2, and `rule-case-build` by 1010.3.
- **estimates (5):**
  - `estimate-retro-loads-on-a-red-command`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` and `estimate-synthesis-keeps-actioned-by-the-mark` now carry `deferred_by` (cases 1007, 1008, 1009).
  - `estimate-case-check-notes-the-files-that-name-what-a-case-changes` has its Criterion set anew by 1010.1, then `passed` by L10.
  - `estimate-case-build-searches-the-names-of-what-it-changes` was set anew by 1010.3 and stands `pending`.
- **insights (1):** `insight-orchestration-acknowledging-reply-keeps-headings-in-english`, changed by the synthesis.

**Marks:**
- No entry is `incomplete` or `failed`.
- The 3 `defer` entries (lines 1–3) carry `exists`.
- No `near`, no `merged`, and `unparsed: []`.

**Pages archived:** none. `guppi cleanup` printed `0 page(s) moved`. `guppi archive` printed nothing on stdout or stderr and exited 0, so it moved and kept no unit. All five sessions of 2026-11-02 are of the run day, which it does not look at.

**What the handoff asked for:**
- **Three defers:** `guppi backlog` went from `7 items` to `11 items`. It added three lines for the deferred Estimates of 1007–1009. The fourth new line is the Insight the synthesis reopened.
- **Two `replace` items of 1010.1 and 1010.2:** both applied to two different passages of the Purpose of `rule-case-check`, as `git diff` shows.
- **Decision lines of Case 1010:** each stands once in the ledger (lines 4–9).
- The handoff gave no instruction to repair an entry, so none was refused.

**Index check:** no Grep was run and nothing was compared. The only `create` (line 7) is an Estimate, which has no index.

**Synthesis:**
- The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 63 lines. The harness saved the output to a file, and I read that file.
- The Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 17 lines.
- **Frontier-heading lesson (L12):** `lesson-orchestration-defer-reply-frontier-heading-in-english` shares its cause with `insight-orchestration-acknowledging-reply-keeps-headings-in-english`. Both copy the English `## Frontier` heading as a literal into a chat in another language.
  - The Insight stood `actioned` with `addressed_by: [[decision-case-1002]]`. The lesson entry carries no `addressed_by`.
  - So I appended an `update` of the Insight: `set: {children: [the two earlier lessons plus the new one], status: open}`. I also appended an `update` setting the lesson `clustered` under it. Both are marked `librarian: synthesis`.
  - The Insight now stands `open` with severity 1, and its `addressed_by` field is unchanged. This pair is reported in the brief.
- **Bare case-reference lesson (L13):** `lesson-ship-test-comment-writes-a-bare-case-reference` joined nothing. No index line names a pointer written without its bracket in a code comment.

**Pages opened for the first three reasons:** `vault/wiki/insights/insight-orchestration-acknowledging-reply-keeps-headings-in-english.md`, for the synthesis. The index line had already settled that the cause is the same. I opened the page for its `children` and `status`, which the `update` entry needs. Outcome: clustered.

**Read of `ledger.md`:** one read, `wc -l` plus the start of each line. It has 13 lines. The yaml holds lines 1–10, 12 and 13, and line 11 is folded into the entry of line 7. Every line is accounted for.

**Flags:**
- No script printed a line on stderr: `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`, `archive`.
- No unticked Spec line holds `guppi sprint-close --apply`.
- **Reopened Insight:** it stands `open` with `addressed_by: [[decision-case-1002]]` still on the page. Both of its earlier children stand archived since session 1548.
- **Handoff note:** `ask-guppi` reported that it made searches of code beyond the one its frame allows.
- No Estimate stands `failed`. I found no contradiction and no MOC candidate.
- I made no read that the frame says my job does not need. `.guppi/guppi/generate.py` and `.guppi/guppi/archive.py` were read as the scripts' own files.
- No hook refused a call.

**Lint total:** 0. `uv run --project .guppi guppi check` printed nothing and exited 0, both before the brief and at the close.

**Files:**
- `C:\PROJECTS\GUPPI\vault\wiki\brief.md`
- `C:\PROJECTS\GUPPI\vault\raw\2026-11-02\2035\materialize.yaml`
