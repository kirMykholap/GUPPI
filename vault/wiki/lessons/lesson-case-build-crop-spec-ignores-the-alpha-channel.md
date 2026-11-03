---
type: lesson
kind: error
root_cause: case-guppi worded the options of the crop and the task of Case 1016 from the size of the picture alone and did not read its mode, so the white padding of the task threw away the transparency the source held
status: new
origin: raw/2026-11-03/0316/ledger.md#L32
sprint: plugin
created: 2026-11-03
tags: [case-build, plugin]
---

## Trigger

Case 1016 set the icon as the guppy picture padded with white to a square, Work Mode wrote it so, and at the stop the person asked for a transparent background, which the source .guppi/icon_guppi.png already had (RGBA, alpha 0 around the fish)

## Root cause

case-guppi worded the options of the crop and the task of Case 1016 from the size of the picture alone and did not read its mode, so the white padding of the task threw away the transparency the source held

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#L32
