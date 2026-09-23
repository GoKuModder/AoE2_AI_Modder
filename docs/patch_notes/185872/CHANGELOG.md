# Update 185872 library changelog

## XS scripting and constants

- Added the Update 185872 XS function reference to the documentation and packaged catalogs, including 67 new APIs, two renamed entries, and corrected `xsEffectAmount` train-location parameters.
- Expanded the XS constants catalog from 872 entries to 1,163 unique entries. It now represents all 1,160 records on the current UGC constants page, while preserving three local-only records.
- Added UGC naming aliases and notes for the two malformed Action Type labels; kept the installed spellings `cActionTypeUnload` and `cActionTypeGatherPoint`.
- Compared constants with the installed `Constants.xs` (game file version `101.103.54800.0`). Where UGC values disagreed, the catalog uses the installed values for `cAttributeResearch`, `cNumCivs`, and `cSentinelEndClass`, and documents the discrepancy.
- Added the Update 185872 XS/constants notes, including object attributes 158–166, unit property access, enum families, and the read-only `cUnitOrderId = 10010` relationship to `xsGetUnitProperty`.
- Refreshed the saved UGC constants source snapshot and its source index/manifest from the current constants page.

## Scenario Editor and trigger reference

- Added a 10-record Scenario Editor 185872 overlay and routed scenario-editor update lookups to it.
- Updated trigger attribute, condition, and effect references for the changed fields and labels, and wired the trigger knowledge builder to apply the overlay.
- Updated the trigger and XS agent guides and lookup index so the new scenario fields and XS references are discoverable.
- Added regression assertions for the updated Unit Trait flags and Trait Piece behavior; tests were not executed.

## Retrieval, AI, and modding guides

- Added an AI scripting guide for the update and refreshed its source/retrieval metadata.
- Updated modding attribute and task notes.
- Updated XS validation and retrieval so catalogued built-ins and the refreshed reference content can be found through the packaged knowledge path.
- Added a dedicated XS essentials source for Script Call functions, `extern`, condition loading-time guidance, and DAT/scenario versus XS unit-identifier terminology; indexed it and linked it from agent navigation.
- Rebuilt XS knowledge metadata and manifests and synchronized the generated documentation/package indexes. The `.jsonl` document stores are ignored by Git, so their generated line changes do not appear in `git diff`.

## Why the diff is large

At the time this changelog was written, the tracked diff showed 14,979 insertions and 4,261 deletions across 36 tracked files, for a net increase of 10,718 lines. That snapshot does not include this new changelog or other untracked documents.

Most of the churn comes from data and mirrored copies:

- The saved UGC page was replaced with the current page snapshot. That file alone shows 4,929 inserted and 4,108 deleted lines because it is a full page capture with a changed route, navigation, and generated markup; its net growth is 821 lines.
- The constants catalog is formatted JSON and has both documentation and package copies. Each copy adds about 3,231 lines for the expanded entries.
- The XS function catalog also has documentation and package copies; each adds about 1,549 lines for the new API records and signature updates.
- The remaining changes cover scenario overlays, routing/build support, documentation, and retrieval metadata.

## Verification status

- The XS knowledge builder completed; the generated metadata, manifest, and package copies were checked for matching counts and hashes.
- Catalog JSON parsed, both constant catalog copies matched byte-for-byte, and static checks passed, including `git diff --check`.
- Tests were not run. The scenario catalog builder was not run because `AoE2ScenarioParser` was unavailable in the environment.
