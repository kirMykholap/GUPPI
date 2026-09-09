# Handoff — 2026-09-09, Slice 0

## Notes from memory

- The owner read the whole map of the old harness and the whole `docs/migration/` set in the
  same session and chose every recommended option. None of the eight decisions was contested;
  the one he asked about first was the volume of ratifications, which D1 answers.
- The old hooks kept firing their advice during this session (pre-task, one-writer, feedback
  block). Ignored on the owner's permission, and they are gone after this slice.
- `docs/migration/` was untracked when it arrived. It is committed in its original form first,
  then moved and edited, so the drafts survive in history exactly as written.
- `CLAUDE.md` at the root already had the product paragraph removed in the working tree
  before this session started; that edit was the owner's and is folded into the rewrite.

## Direct instructions to the librarian

There is no librarian yet. When one exists (Slice 3), the first thing it should materialize is
this folder: the nine ledger lines above map onto `spec.md`, and the Decision pages for cases
1–8 do not exist yet.

## What actually got done

- Branch `migration` from `main` at `047a612`.
- `job_hunt_ai_vault/` → `vault/`; old live wiki folders and registers → `vault/parked/2026-09-09/`;
  the earlier parking → `vault/parked/2026-09-07/`; `harness-map.md` → `docs/harness-map-2026-09-07.md`.
- `vault/wiki/` holds `index.md`, `glossary.md`, `case-schema.md`, four registers and six
  `schema.yaml` + `schema.md` pairs. No page.
- Corrections C1–C14 applied to `index.md`, `glossary.md`, `rule-session-start.md` and
  `README.md`.
- Old harness removed: `.claude/hooks`, `.claude/agents`, `.claude/templates`, `scripts/`,
  `.superpowers/`, six skills. `/grill-me` kept. `settings.json` holds only the default mode.
- `CLAUDE.md` rewritten as a bootstrap with `@import` of the glossary and the Case schema.
- Where the code landed: the three commits above `047a612` on `migration`.
