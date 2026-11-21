# Design: upload an image and get its palette

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [d2dd842] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-006 Go, stand-in, not independent | [d2dd842] |

---

## Purpose

Describe the one user goal and design the code before writing it, so the engine and the website follow an accepted design.

## Target Date

2026-11-24

## Deliverable

UC-001 with its DM, SSD, OC, SD and DCD, and ADRs for the web server and the colour quantisation, each with a `Go` review

## Business Case Objectives

OBJ-1, OBJ-2

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-001

## Go/No-Go Criteria

- UC-001 and each of its design artifacts has an `RC-*` with verdict `Go`
- The project-level `docs/domain-model.md` and `docs/dcd.md` are `Accepted`
- Each `Decided by default` choice of BC-001 that shapes code has an ADR

## Branch and Pull Request

One branch `milestone/mil-003-design` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write use case UC-001 | Upload an image and see its top 10 colours: main flow and the alternative flows for no file, unsupported file and too large file | No | CN-001, CN-004 |
| 2 | Write ADRs | ADR-0001 standard-library `http.server` as web server; ADR-0002 downscale and quantise before counting with NumPy | No | BC-001 AS-1, AS-2, AS-5 |
| 3 | Write the design of UC-001 | DM, SSD, OC, SD and DCD for UC-001, in that order, each reviewed before the next | No | UC-001 |
| 4 | Consolidate the project models | Add UC-001's model to `docs/domain-model.md` and `docs/dcd.md` | No | UC-001 |
| 5 | Screenshot and wiki step page | Screenshot of this step in `docs/images/`, added to the README step list and to a wiki step page in en, da and ms that explains what was learned | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[d2dd842]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/commit/d2dd84230aab12940de05276d6d660dcf93af46c
