# Handoff — 2026-09-18, the definitions of the categories, the sprint as a kind, Slice 3b deferred again

## Notes from memory

- The session's first `/hi` failed on a lapsed login (the client's login prompt at the same
  moment); the person did `/login` and a second `/hi`. The lesson of 1119 named the
  classifier's model; this session's lesson names the login. The librarian's synthesis may
  cluster the two — the newer one is the cause, the older one the symptom.
- Case 237 was first drafted as an allow entry for `render --sync` and withdrawn after the
  person explained the login and the prompt; the number 237 was reused for the Case that
  was ratified (the withdrawn preview never reached the ledger). The person accepts the
  prompt in Plan Mode as the client's mechanism; the reading of `estimate-permissions` is
  the person's word, taken in the ratification reply — so the page goes `pending` by the
  `update` and `passed` by the estimate line in the same run, as `estimate-ledger-write-lifts`
  did in 1119.
- The definitions (240) came out of a long discussion; the person's own words that settled
  it: "who makes this thing — the developer or the running product"; "MOC — parts the
  person named, a check before a create"; "in the harness a guard is a Rule, a measured
  thing is an Entity"; Research stays as a kind, `failed` on it has two meanings, both
  debt. The person had doubts on the Rule / Entity-Estimate criterion ("пока принимаю, но
  есть сомнения") — a caveat, not a change.
- The universality of the categories is now `rule-morph` in Slice 5 (239), the person's
  framing "the morph mechanism — an initiation at install". The product model line stays
  in the Backlog.
- Slice 3b was deferred once more (242) at the person's choice, with the Insight sentence
  (238) to be written into `rule-work-mode` when the rule is built.
- Retro: `estimate-retro-loads` read `passed`; a lesson on `pretask --session` taking the
  id, not the `hi:` line.

## Direct instructions to the librarian

- Expect, in this yaml: 12 page entries — `create entity-sprint` (with `children` written
  in the item, since the backlink runs only on a create with `ref`), `defer rule-morph`
  (a placeholder, no page today), 10 `update`; 4 `defer` targets that exist
  (`insight-workflow-code-live-before-the-page-it-reads`, `rule-work-mode`,
  `rule-subagent-guppi`, `rule-git-context`, `rule-github-issues` — five slugs, four
  Cases); 8 Rule-class file entries "applied by hand" (`entities-schema`, `rules-schema`,
  `estimates-schema`, `glossary` ×4, `index` ×2); 8 estimate lines, 4 lessons.
- `{supersedes:case 230}` on the first line of 240.1: `decision-case-230` becomes
  `superseded`; `index` has no page, so no `deferred_by` to clear.
- `entity-sprint-migration`: two updates (239 `replace` on Slice 5 and the Backlog; 241
  `set: {kind: Leaf, parent}`). The empty `children` field was already removed by a
  one-off in Work Mode; until the 241 `set` lands, lint prints
  `entities/entity-sprint-migration: schema: missing field children (given kind MOC)` —
  the pattern of `insight-workflow-code-live-before-the-page-it-reads`, expected, not a
  finding. After the run it must be gone.
- The 239 second `replace` spans two lines (the removed Backlog line plus the head of
  the next); `generate.replace` matches on whitespace, so it should apply; check the
  Backlog holds one line after.
- `estimate-permissions`: `pending` by the update, `passed` by the estimate line — the
  page must end `passed`, `rule-permissions` stays `built`.
- Case 244 writes its Criterion under `sections: Criterion` (case 204); the page has
  `method`, so the recut check passes. Cases 235 and 236 recut by the Case's given / when /
  then; both pages have `method`.
- Run `guppi sprint` after `cleanup` and `render`: Slice 5 must render as one line with
  four names, `rule-morph` the fourth; the Backlog one line.
- Possible duplicates: the two `/hi` lessons (1119 classifier, 1252 login) — one cause;
  `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt` is near
  nothing I know of; `lesson-lint-schema-body-table-one-section-per-row` — near nothing.
- Readings after this run, for the brief: `estimate-render-harness-ticks-the-spec` — the
  `uv run guppi render` lines of the 1252 Spec ticked by `render`, and the read line of
  the 1119 Spec (returned to `[ ]`) *not* ticked — that is the live reading of 235;
  `estimate-sprint-renders-the-backlog` — `sprint.md` after `guppi sprint`, the lines of
  Slice 4 and 5 with names — the live reading of 236. Take neither: name them in Readings
  due.
- No `carry.md`; no patch; `gh` unavailable as before.

## What actually got done

- Ratified: 235, 236, 237, 239, 240.1–240.3, 241, 244; deferred 238, 242, 243. Readings
  `passed`: `estimate-case-protocol-loaded`, `-hi-writes-frontier`, `-brief-written`,
  `-permissions`, `-generate-ticks-the-spec`, `-sprint-checks-the-file`,
  `-harness-pipeline`, `-retro-loads`. Lessons: 4.
- Code, commit `6843c93` on `migration`: `guppi/render.py` (`RENDER_LINE`), `guppi/sprint.py`
  (`item_name`, the collapsed line); tests 424 → 425; `make style` clean; `sprint.md`
  rewritten by `guppi sprint`.
- Rule-class by hand: `entities/schema.md`, `rules/schema.md` (the definition and a
  paragraph at the end of `### Enforcement`), `estimates/schema.md`, `glossary.md` (rows
  MOC, Leaf, Entity, Rule, Estimate, Sprint), `index.md` §6 (two paragraphs).
- One-off: `children: []` removed from `entity-sprint-migration`; the reading line of
  `estimate-render-harness-ticks-the-spec` in `raw/2026-09-17/1119/spec.md` back to `[ ]`.
- Not done: every page create, update and defer of this Spec (this run); the readings named
  above; `estimate-sprint-migration-lint-clean` (the close); `estimate-carry-over-writes`
  (a live `/carry`, none yet); Slice 3b (defer 242, the next session's first item);
  `rule-git-context` / `rule-github-issues` (defer 243, the close).
