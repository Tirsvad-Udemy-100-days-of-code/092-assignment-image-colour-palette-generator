# Engine: find the top colours with NumPy

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [4152bcb] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-007 Go, stand-in, not independent | [4152bcb] |

---

## Purpose

Build and test the colour extraction on its own, without the website, so the core of the assignment is proven first.

## Target Date

2026-11-25

## Deliverable

The domain module that turns image bytes into the top 10 colours as HEX with their share, with unit tests

## Business Case Objectives

OBJ-2, OBJ-3

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-003

## Go/No-Go Criteria

- All unit tests pass; line coverage of the module at least 90 %
- A test image with known colours returns exactly those colours and shares
- A 12-megapixel JPEG is processed in under 2 s
- opengrep reports 0 findings; code review against `qc-programming-python.md` is `Go`

## Branch and Pull Request

One branch `milestone/mil-004-engine` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load and downscale an image | Infrastructure `PillowImageReader`: read upload bytes, convert to RGBA, downscale so the longer side is at most 300 px, return a NumPy array | Yes | UC-001 |
| 2 | Quantise and count colours | Snap each channel to the colour step, drop transparent pixels, count unique colours with `numpy.unique` | Yes | UC-001 |
| 3 | Return the top colours as HEX | Domain `find_top_colours` (`numpy.unique` and `argsort`) returns the top 10 as `ColourShare` (HEX and share in percent); application `PaletteService` ties reader and domain together | Yes | UC-001 |
| 4 | Unit tests for the engine | Tests with generated images: one colour, fewer than 10 colours, more than 10, transparency, colour step limits | Yes | UC-001 |
| 5 | Screenshot and wiki step page | Screenshot of this step in `docs/images/`, added to the README step list and to a wiki step page in en, da and ms that explains what was learned | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[4152bcb]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/4152bcb453201a7da2019cc9a96018ebed7a7b9e
