---
name: handoff
description: Write the handoff note from memory and hand the session to the librarian.
---


Tree: !`git status --porcelain`

If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed `# Handoff — <date>, <slice or topic>` with
three sections: `## Notes from memory` (where the person hesitated, what stayed
unclear, which decisions carried caveats), `## Direct instructions to the
librarian` (what to check first, what may duplicate what), `## What actually got
done` (which Cases closed, where the code landed, what is not done). Write it from
memory; do not re-read the artifacts. Short or empty sections are normal.

Then dispatch the `librarian-guppi` agent with one line: `Materialize <date>.` Wait
for its report and show it to the person unchanged. Do not commit after this.
