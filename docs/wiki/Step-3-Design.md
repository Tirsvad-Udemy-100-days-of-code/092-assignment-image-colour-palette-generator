# Step 3: Design

🌐 **English** · [Dansk](Step-3-Design-da) · [Bahasa Melayu](Step-3-Design-ms)

Milestone `MIL-003`. Branch and pull request: one for this step.

![Use case UC-001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/03-design-use-case.png)

## What was done

One use case, `UC-001` *Get the colour palette of an image*, with its
alternative flows: no file, a file over 10 MB, a file that is not an image, a
fully transparent image, and fewer than ten colours. Two decisions were
recorded as ADRs: `ADR-0001` serves the site with the standard library's
`http.server`, and `ADR-0002` scales the image down to 300 px and groups
near-identical shades before counting. The use case was then designed as a
domain model, a system sequence diagram, an operation contract, a sequence
diagram and a design class diagram, each reviewed before the next.

## What was gained

- The alternative flows found the hard cases before the code did. "What if the
  image is transparent?" became business rule `BR-1`: pixels with alpha below
  128 are not counted.
- An ADR records why, not only what. Without one, the choice of
  `http.server` over Flask looks like an oversight; with one, it is a
  decision to keep runtime dependencies down.
- The design class diagram gave the layers their names before any code:
  `PillowImageReader` (infrastructure), `find_top_colours` (domain) and
  `PaletteService` (application). The next two steps only had to fill them in.
