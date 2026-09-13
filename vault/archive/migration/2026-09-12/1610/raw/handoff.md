# Handoff — 2026-09-12, session K: settings.json as a MOC, the render in the librarian's phase

## Notes from memory

The owner reshaped Case 85 three times before it settled, and the final shape is his. I
opened with the guard returning an allow decision; he said the guard is beside the point
and asked for `permissions.allow` with a Rule page of its own. I answered that a second
page cannot render into `settings.json`; he proposed a MOC over the file with partial
children; then he asked whether the MOC could hold the whole file and let children splice
into it, by the `rule-claude-md` pattern. That is what 85.2 says. The one ugly corner is
that the comma between two JSON keys lives in the body of a child page, so reordering the
children moves the comma; the MOC's Estimate (the assembled file parses) is what catches
it.

Twice he asked for a plain explanation rather than a decision — what `source` is for, and
what Case 88 is actually about. Both times the answer was that the text, not the code, was
wrong, and neither Case changed after the explanation. He also asked whether
`render --check` could gate the render instead of 89.4; it cannot, because it exits 1
whenever a file merely differs, which after `generate` is always, and it knows no JSON.

Case 92 took the practice over the text: `ref` stands on every decision line. The
alternative would have contradicted `CLAUDE.md` and four sessions of ledgers.

Two closings were mine to judge. F47 (no upstream, `gh` not logged in) I closed as `work`
with no defer, because `sprint.md` already carries it as a Slice 5 line. F45 I narrowed at
the defer: only the missing `## Insight` section is page-shaped (Case 96); the failed and
pending Estimates stay with the brief.

## Direct instructions to the librarian

**Do not run `uv run guppi render` this run, and commit `vault/` only.** Case 89.1 adds a
render step to your frame and 89.2 widens your commit, but the file you are reading is
rendered from `rule-documentation` and `rule-close` only after your `generate`. Both take
effect at the next session. The governed files stay for the next session start.

Check first, after `generate`:

- `rule-settings.children` ends as exactly `[rule-default-mode, rule-permissions,
  rule-hook-registry]`, no duplicate. The create carries the list, and `generate` also
  appends the two child creates by their `ref` — the two together may double an entry.
- `rule-harness.children` holds `rule-settings` in the slot the 85.2 update names, and no
  longer `rule-hook-registry`, whose `parent` moves to `rule-settings` by the `set` of
  85.3.
- Three pages are updated twice in this one run: `rule-render-harness` (85.1, 88.1, 89.4),
  `rule-materialize` (87, 90.1), `rule-documentation` (89.1, 90.3). Every criterion block
  should land. If a `replace` is reported absent or not unique, name the pair in the report
  and leave it.
- Case 99 replaces prose on `estimate-hook-registry-rendered`, `rule-pretask`,
  `rule-materialize` and `rule-harness`. The `rule-pretask` pair anchors on text that case
  90.2 writes earlier in the same run; if it fails, say so plainly — it means the 90.2
  entry did not apply.

**Repair nothing in the yaml.** The entries of the earlier run on this date keep their old
marks, three of them `incomplete: [source]`; case 87 says they are not rewritten, and the
five pages they name were backfilled by a one-off in Work Mode. Case 90.3 makes a repair an
instruction you refuse and name; this handoff asks for none.

No new tags: `harness`, `render`, `session` and `hooks` all exist.

## What actually got done

- One commit, `0ed3afb`: the code of the Spec, the two Rule-class files by hand, the
  `source` backfill on five lesson pages, and the render of the six governed files that
  `render --sync` wrote at session start (the first item of the previous brief).
- Ratified: 85.1–85.5, 86, 87, 88.1, 88.2, 89.1–89.4, 90.1–90.3, 91, 92, 99. Deferred:
  93–98.
- Code in four files: `render.py` (the bare splice into a comment-less file, the JSON gate
  before the write), `materialize.py` (`source` from the braces, the named Estimate),
  `pretask.py` (the fifth form finding), `guard.py` (the event line on a refusal).
- Readings passed and written: `estimate-governed-files-hook-refuses` (`failed` → `passed`,
  its third live clause now holds), `estimate-materialize-assembles`,
  `estimate-pretask-reconciles`.
- Not done: 19 of the Spec's 40 tasks. Eight readings need your run
  (`estimate-settings`, `estimate-permissions`, `estimate-default-mode`,
  `estimate-hook-registry-rendered`, `estimate-documentation-completes`,
  `estimate-close-commits`, `estimate-render-harness-reproduces`,
  `estimate-claude-md-rendered`); two need the next session start
  (`estimate-case-protocol-loaded`, `estimate-render-sync-reports`); the rest are the pages
  your run writes.
- `make test` 267 green, `make style` clean. `guppi lint` not run since the commit.
- Four `estimate_slug` lines were added to the Spec after the owner approved it: cases
  85.1, 88.1, 89.4 and 87 change the contract of a page with two Estimates, and the check
  that catches this was written in the same Spec by 90.2. The names come from the
  `ratification` section of those Cases. The lesson is
  `lesson-pretask-runs-before-the-check-it-adds`.
