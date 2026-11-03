---
type: decision
case: "1016"
status: current
create: ["[[estimate-clean-branch-ships-the-plugin-icon]]"]
update: ["[[rule-clean-branch]]"]
origin: raw/2026-11-03/0316/ledger.md#case-1016
sprint: plugin
created: 2026-11-03
tags: [ci, plugin, git]
---

## Problem

The plugin `guppi` has no icon, so `claude plugin validate` notes `ICON_MISSING` and a listing in Anthropic's directory would show no picture.

## Recommend

- **Does the clean version get an icon now**
  - Recommended: (b) no icon now; a defer page ties it to the submission to Anthropic's directory.
  - Answer: (a) add the icon now, since the item is taken up.
- **Where the image file lives in this repository**
  - Recommended: (a) one file `plugin/icon.png`, copied to `icon.png` at the root of the clean version, the two originals leaving `.guppi/`.
  - Answer: (a); replaced by the question on where the icon stands in the clean version.
- **Which picture and which crop**
  - Recommended: no recommendation, since how the directory shows the icon is not checked; each option a PNG of 512 by 512 pixels.
  - Answer: (b) the whole fish without the word, padded with white to a square.
- **Who makes the cropped file**
  - Recommended: (a) Work Mode crops it by a one-off script with Pillow, and the person looks at the result.
  - Answer: agreed, (a).
- **How the icon is checked**
  - Recommended: (a) a new Estimate, `estimate-clean-branch-ships-the-plugin-icon`, checked by a test of `.guppi/tests/test_ship.py`.
  - Answer: agreed, (a).
- **Where the icon stands in the clean version**
  - Recommended: (d) in `.guppi/` as `.guppi/icon.png`, the manifest naming `./.guppi/icon.png`, with no change to `guppi ship` or to the install skill.
  - Answer: agreed, (d).

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#case-1016
