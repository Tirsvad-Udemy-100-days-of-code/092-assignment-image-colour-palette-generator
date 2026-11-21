# ADR-0001: Python's standard library web server

## Metadata

| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [UC-001], [DCD-001] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [8836599] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-011 Go; stand-in review, not independent | [8836599] |

---

## Context

UC-001 needs a website with one page: an upload form and a result. The course
taught Flask, but S03 (CN-005) and BC-001 AS-5 ask for as few runtime dependencies
as possible, and NumPy and Pillow are already needed for the image work.

Forces: dependency count, how familiar the code is to S02 course participants
(CN-003), effort, and security of a public upload form.

Options evaluated:

1. Python's standard `http.server` with a small multipart parser and an HTML view.
2. Flask, as taught in the course.
3. Django.

## Decision

The website runs on Python's standard `http.server` (`ThreadingHTTPServer`), with
the multipart form read by the standard `email` parser and the page rendered by
a small HTML view.

## Consequences

Positive:

- No runtime dependency besides NumPy and Pillow (Flexibility, CN-005).
- The request handling is visible in the code, which suits a learning project.

Negative:

- More code than Flask: a multipart parser, an upload limit and HTML escaping
  are written by hand and need their own tests (Maintainability).
- `http.server` is not meant for production; the README says the website is for
  local use (Security).
- S02 participants who know Flask see a different style (Interaction Capability).

## Affected Artifacts

- [UC-001]
- [DCD-001]

---

[BC-001]: ../business-case.md
[UC-001]: ../use-cases/uc-001-get-colour-palette/uc.md
[DCD-001]: ../use-cases/uc-001-get-colour-palette/dcd.md
[8836599]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/88365998dcd8a6722bd2b54a499c66f12055eccc
