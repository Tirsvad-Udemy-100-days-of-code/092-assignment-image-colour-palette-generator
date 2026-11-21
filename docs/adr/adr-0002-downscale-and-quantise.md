# ADR-0002: Downscale and quantise before counting with NumPy

## Metadata

| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [UC-001], [SD-001], [DCD-001] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [a0db9d8] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-012 Go; stand-in review, not independent | [a0db9d8] |

---

## Context

A photo has hundreds of thousands of pixels and thousands of near-identical
shades. Counting exact colours on every pixel is slow for large images and gives a
palette of ten almost equal shades (BC-001 R-1). The reference demo groups shades.

Options evaluated:

1. Count exact RGB values on every pixel.
2. Downscale so the longer side is at most 300 px, then quantise each channel to
   a colour step and count with `numpy.unique(axis=0, return_counts=True)`.
3. Cluster colours with k-means.

## Decision

The image is downscaled to at most 300 px on the longer side, each channel is
moved to the middle of its colour-step bucket (default 24, 1 to 64), and the
colours are counted with `numpy.unique` and ranked with `numpy.argsort`.

## Consequences

Positive:

- Time and memory stay low for any accepted upload (Performance Efficiency).
- Similar shades form one visible colour, so the palette matches what a person
  sees (Functional Suitability, CN-004).
- Pure NumPy, the skill the assignment practises (CN-002); k-means would need
  another dependency or much more code.

Negative:

- A colour shown is the middle of its bucket, not an exact pixel value; with step
  1 the exact colours are counted (BC-001 AS-1).
- Downscaling blends very small details into their neighbours, so a colour that
  covers only a few pixels may not appear.

## Affected Artifacts

- [UC-001]
- [SD-001]
- [DCD-001]

---

[BC-001]: ../business-case.md
[UC-001]: ../use-cases/uc-001-get-colour-palette/uc.md
[SD-001]: ../use-cases/uc-001-get-colour-palette/sd.md
[DCD-001]: ../use-cases/uc-001-get-colour-palette/dcd.md
[a0db9d8]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/a0db9d84abaffb5fe0ddd71de247fad188a9a939
