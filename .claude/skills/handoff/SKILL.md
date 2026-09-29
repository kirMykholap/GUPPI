---
name: handoff
description: Write the handoff note from memory and hand the session to the librarian.
---


Tree: !`git status --porcelain`

If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed `# Handoff — <date>, <slice or topic>` with
three sections: `## Notes from memory` (where the person hesitated, what stayed
unclear, which decisions carried caveats), `## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (the three parts of the close of the Retro: Ratified and What got done as the person approved them; What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in this file, the text of a note for the handoff standing there as the end of its item, and under it the two lines under the frontier — the count of the boxes that wait for the librarian and the slugs of the `read` lines whose slug this session creates or updates). A fact stands in one section only: a Case, a reading, a lesson or an open item named in one section is not named in another (case 468.2). Write it from
memory; do not re-read the artifacts. Short or empty sections are normal.

Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. Wait
for its report and show it to the person unchanged. Do not commit after this.
