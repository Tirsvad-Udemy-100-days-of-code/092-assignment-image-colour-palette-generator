# Website: upload page and palette result

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [4152bcb] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-008 Go, stand-in, not independent | [4152bcb] |

---

## Purpose

Put the engine behind a simple website, so a user can upload an image and see the palette as the assignment asks.

## Target Date

2026-11-26

## Deliverable

A standard-library `http.server` website with an upload form and a result page of swatches with HEX codes, with web tests

## Business Case Objectives

OBJ-1, OBJ-3

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-004

## Go/No-Go Criteria

- Web tests against a test server pass for a valid upload and every error flow
- The page shows the uploaded image and 10 swatches with HEX codes and share
- Uploads over 10 MB and non-images get a clear message, not an error trace
- opengrep reports 0 findings; code review against `qc-programming-python.md` is `Go`

## Branch and Pull Request

One branch `milestone/mil-005-website` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Upload form | Presentation layer: multipart parser and page with a file input, the colour step setting and a submit button | Yes | UC-001 |
| 2 | Result page | Show the uploaded image and the swatches with HEX codes and share in percent | Yes | UC-001 |
| 3 | Error handling | Messages for no file, unsupported file and a file over 10 MB | Yes | UC-001 |
| 4 | Web tests | Tests against the server started on a free local port for the main flow and each alternative flow | Yes | UC-001 |
| 5 | Screenshot and wiki step page | Screenshot of this step in `docs/images/`, added to the README step list and to a wiki step page in en, da and ms that explains what was learned | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[4152bcb]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/4152bcb453201a7da2019cc9a96018ebed7a7b9e
