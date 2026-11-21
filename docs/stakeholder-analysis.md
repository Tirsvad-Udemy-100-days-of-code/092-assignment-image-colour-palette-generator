# Stakeholder Analysis: Image Colour Palette Generator

## Metadata

| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition with S01 to S03 | [4152bcb] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-002 Go, stand-in, not independent | [4152bcb] |

---

## Stakeholders

| ID | Stakeholder | Role and context | Power | Interest | Strategy |
| --- | --- | --- | --- | --- | --- |
| S01 | Course participant | Product Owner, developer and reviewer of every artifact; owns the repository | High | High | Manage Closely |
| S02 | Udemy coursists | Fellow students who share code and compare solutions to Day 92 | Low | High | Keep Informed |
| S03 | GitHub and Gitea viewers | People who browse the repository for ideas | Low | Low | Monitor |

## Power/Interest Grid

| | Low interest | High interest |
| --- | --- | --- |
| **High power** | (none) | S01 |
| **Low power** | S03 | S02 |

## Concern Register

| ID | Raised by | Concern (business language) | Quality characteristic (ISO/IEC 25010) | Business Case objective |
| --- | --- | --- | --- | --- |
| CN-001 | S01 | The assignment works end to end and is finished within the course time | Functional Suitability | OBJ-1 |
| CN-002 | S01 | The work practises NumPy image processing from Day 76 | Functional Suitability | OBJ-2 |
| CN-003 | S02 | Code is readable and runnable, with function names that match the assignment's words (upload, colours, palette, HEX) | Maintainability, Interaction Capability | OBJ-3, OBJ-4 |
| CN-004 | S02 | Results are comparable with the reference demo: top 10 colours with HEX codes | Functional Suitability | OBJ-1 |
| CN-005 | S03 | The repository has a clear description, topics and README, and few runtime dependencies | Interaction Capability, Flexibility | OBJ-3, OBJ-4 |
| CN-006 | S01 | Personal tokens in `.env` never reach the repository | Security | OBJ-5 |
| CN-007 | S01 | Each step is documented with a screenshot and what was learned, in en, da and ms | Interaction Capability | OBJ-4 |

## Conflicts and Resolutions

| Conflict | Between | Resolution |
| --- | --- | --- |
| Few runtime dependencies (CN-005) against a readable web app and real image decoding (CN-003, CN-004) | S03, S02 | Accept exactly NumPy and Pillow; the website uses the standard library (BC-001 AS-5, SC-5); test tools are dev dependencies only |
| Full review workflow of the framework against the 180-minute course budget (CN-001) | S01 with itself | One use case, lean artifacts; documents are short and reviewed once per milestone |
| Readers in three languages (CN-007) against time (CN-001) | S01, S02 | English is authoritative and written first; da and ms follow page by page in the same milestone, kept short |

## Communication Plan

| Stakeholder | Channel | Frequency | Deliverable | Milestones |
| --- | --- | --- | --- | --- |
| S01 | Pull requests and the project chat | Every milestone | Plan, review records, merged pull request | MIL-001 to MIL-006 |
| S02 | Udemy Q&A and the repository README | Once, at release | Link to the repository and run instructions | MIL-006 |
| S03 | Repository description, topics, README, wiki | Continuous after publication | Public pages | MIL-002, MIL-006 |

---

[BC-001]: ./business-case.md
[4152bcb]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/4152bcb453201a7da2019cc9a96018ebed7a7b9e
