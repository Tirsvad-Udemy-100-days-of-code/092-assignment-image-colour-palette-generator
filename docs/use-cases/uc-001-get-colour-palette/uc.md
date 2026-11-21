# Use Case UC-001: Get the colour palette of an image

## Metadata

| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [SA-001], [BC-001], [MIL-003], [DM-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-010 Go; stand-in review, not independent | pending |

---

## Purpose

Describe the one user goal of the project: a visitor gives an image and gets its
ten most common colours as HEX codes. Answers CN-001, CN-003 and CN-004 for S01
and S02.

## Use Case

| Field | Value |
| --- | --- |
| Name | Get the colour palette of an image |
| Format | Fully Dressed |
| Scope | Image Colour Palette Generator (the website) |
| Level | User goal |
| Primary actor | Visitor (anyone who opens the website, for example S01 or an S02 course participant) |

## Stakeholders and Interests

| Stakeholder | Interest |
| --- | --- |
| S01 Course participant | The assignment works end to end and practises NumPy image processing (CN-001, CN-002) |
| S02 Udemy course participants | The result is comparable with the reference demo: ten colours with HEX codes (CN-004) |
| S03 GitHub viewers | The website shows the idea clearly with few dependencies (CN-005) |

## Preconditions

- The visitor has an image file (a photo, a drawing or a screenshot).
- The website is running and the visitor has opened it.

## Postconditions

- Success: the visitor sees the image beside its palette: up to ten colours, most
  common first, each with its HEX code and its share of the image in percent.
- Failure: the visitor sees a message that says why no palette was made; nothing
  is kept.

## Main Success Scenario

1. The visitor chooses an image and, if they want, how close two shades must be to
   count as one colour (the colour step).
2. The visitor asks for the palette.
3. The system reads the image and leaves out transparent parts (BR-1).
4. The system groups near-identical shades by the colour step (BR-2) and counts how
   much of the image each colour covers.
5. The system shows the image and the ten most common colours, most common first,
   each with its HEX code and share in percent (BR-3).
6. The visitor copies the HEX codes they need.

## Alternative Flows

- 2a. The visitor asks for the palette without choosing an image: the system asks
  for an image; the use case goes back to step 1.
- 2b. The image is larger than 10 MB (BR-4): the system says the image is too large
  and names the limit; back to step 1.
- 3a. The file is not an image the system can read: the system says so; back to
  step 1.
- 3b. The image is fully transparent: the system says there are no visible colours;
  back to step 1.
- 5a. The image has fewer than ten colours after grouping: the system shows the
  colours it found.

No step includes or extends another use case; UC-001 is the only use case.

## Business Rules

| ID | Step | Rule |
| --- | --- | --- |
| BR-1 | 3 | A part of the image whose opacity is below half (alpha below 128) is transparent and is not counted (BC-001 AS-4) |
| BR-2 | 4 | The colour step is 1 to 64 per channel, 24 when the visitor does not choose one; 1 counts exact colours (BC-001 AS-1, AS-3) |
| BR-3 | 5 | A palette holds at most ten colours (assignment) |
| BR-4 | 2 | An image larger than 10 MB is refused (BC-001 AS-7) |

---

[SA-001]: ../../stakeholder-analysis.md
[BC-001]: ../../business-case.md
[MIL-003]: ../../milestones/mil-003-design.md
[DM-001]: dm.md
[SSD-001]: ssd.md
