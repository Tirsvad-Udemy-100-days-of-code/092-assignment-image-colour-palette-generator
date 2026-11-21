# Operation Contract: getPalette

## Metadata

| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-001], [SD-001] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [a5b3ca4] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-015 Go; stand-in review, not independent | [a5b3ca4] |

---

## Operation

`getPalette(image: file bytes, colourStep: whole number 1..64 = 24) : Palette`

Traces to the `getPalette` message of [SSD-001].

## Cross References

UC-001 steps 2 to 5; Domain Model [DM-001]: Image, Pixel, Colour, Colour Step,
Palette, Palette Entry.

## Preconditions

- The visitor has chosen an Image of at most 10 MB.

## Postconditions

- A Palette instance `p` was created and associated with the Image.
- For each of the up to ten most common Colours among the Image's visible Pixels,
  grouped by the Colour Step, a Palette Entry `e` was created and associated with
  `p` and with that Colour.
- `e.rank` was set to its place in the order of how many visible pixels it covers,
  most first; `e.share in percent` was set to its pixels divided by all visible
  pixels, times 100.
- `p.number of colours` was set to the number of Palette Entries (10, or fewer
  when the Image has fewer Colours).
- Nothing is stored; the Image and the Palette are dropped after the reply.

## Exceptions

| Exception | Triggering condition |
| --- | --- |
| No image | The precondition fails: no file was chosen (UC-001 2a) |
| Image too large | The precondition fails: the file is over 10 MB (UC-001 2b) |
| Not a readable image | The file cannot be decoded as an image (UC-001 3a) |
| No visible pixels | Every Pixel has opacity below 128 (UC-001 3b) |

A colour step outside 1 to 64 is moved to the nearest allowed value; it is not an
error.

---

[SSD-001]: ssd.md
[DM-001]: dm.md
[SD-001]: sd.md
[a5b3ca4]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/a5b3ca4135857fa57754cbc63c2203b48fba81df
