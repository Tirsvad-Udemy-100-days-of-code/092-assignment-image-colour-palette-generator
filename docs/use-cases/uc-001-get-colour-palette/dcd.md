# Design Class Diagram: UC-001 Get the colour palette of an image

## Metadata

| Key | Value |
| --- | --- |
| ID | DCD-001 |
| CrossReference | [DM-001], [SD-001], [OC-001], [ADR-0001], [ADR-0002], [DCD-002] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [bc03eb7] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-017 Go; stand-in review, not independent | [bc03eb7] |

---

## Purpose

The classes, functions and packages that implement [UC-001], one package per
clean architecture layer. Answers CN-003 and CN-005 for S02 and S03.

## Diagram

```plantuml
@startuml
title DCD: Image Colour Palette Generator
skinparam packageStyle rectangle
hide empty members

package "presentation (Delivery)" #FADADD {
  class PaletteRequestHandler <<Controller>> {
    + palette_service : PaletteService
    + do_GET() : None
    + do_POST() : None
    - _discard_body(length : int) : None
    - _send_html(status : HTTPStatus, html : str) : None
  }
  class FormField <<dataclass>> {
    + name : str
    + data : bytes
    + filename : str | None
    + content_type : str
  }
  class multipart_form <<module>> {
    + parse_multipart_form(body : bytes, content_type : str) : dict[str, FormField]
  }
  class html_view <<module>> {
    + render_page(palette, error, preview_uri, bucket_size : int) : str
    + image_data_uri(image_bytes : bytes, content_type : str) : str | None
  }
  class web_server <<module>> {
    + create_server(host : str, port : int, palette_service) : ThreadingHTTPServer
    + read_bucket_size(fields : dict[str, FormField]) : int
  }
}
package "application" #FFF3B0 {
  interface ImageReader <<Protocol>> {
    + read_pixels(image_bytes : bytes) : NDArray[uint8]
  }
  class PaletteService {
    - _image_reader : ImageReader
    + build_palette(image_bytes : bytes, count : int = 10, bucket_size : int = 24) : list[ColourShare]
  }
}
package "infrastructure" #D4E4F7 {
  class PillowImageReader {
    - _max_side : int = 300
    + read_pixels(image_bytes : bytes) : NDArray[uint8]
  }
}
package "domain" #CDEFD3 {
  class ColourShare <<value object>> {
    + rgb : tuple[int, int, int]
    + pixel_count : int
    + percentage : float
    + hex_code : str {property}
  }
  class palette <<module>> {
    + find_top_colours(image : NDArray, count : int = 10, bucket_size : int = 24) : list[ColourShare]
    + quantise_pixels(pixels : NDArray, bucket_size : int) : NDArray
  }
  class colour <<module>> {
    + rgb_to_hex(red : int, green : int, blue : int) : str
  }
}

PaletteRequestHandler "1" --> "1" PaletteService : palette_service
PaletteRequestHandler ..> multipart_form
PaletteRequestHandler ..> html_view
multipart_form ..> FormField : creates
PaletteService "1" o--> "1" ImageReader : _image_reader
PillowImageReader ..|> ImageReader
PaletteService ..> palette
palette ..> ColourShare : creates
ColourShare ..> colour

"presentation (Delivery)" ..> "application"
"presentation (Delivery)" ..> "infrastructure" : wires PillowImageReader\nin create_server
"infrastructure" ..> "application" : implements ImageReader
"application" ..> "domain"
@enduml
```

## Mapping to the Domain Model

| Domain concept | Design element |
| --- | --- |
| Image | `bytes` of the upload, read by `PillowImageReader` |
| Pixel | one row of the NumPy array (red, green, blue, alpha) |
| Colour | `rgb` and `hex_code` of `ColourShare`; `rgb_to_hex` |
| Colour Step | `bucket_size` (1 to 64, default 24) |
| Palette | `list[ColourShare]`, most common first; no own class because it has no behaviour |
| Palette Entry | `ColourShare` (rank is the position in the list, share is `percentage`) |

## Design Notes

- Dependencies point inward: `domain` imports nothing from the other layers;
  `application` owns the `ImageReader` protocol (dependency inversion);
  `infrastructure` implements it; `presentation` wires the parts in
  `create_server` (composition root).
- Every constant lives in `constants.py` (`TOP_COLOUR_COUNT`, `MAX_IMAGE_SIDE`,
  `MAX_UPLOAD_BYTES`, `MIN_VISIBLE_ALPHA`, bucket limits).
- Exceptions: `InvalidImageError` (infrastructure), `PaletteError` (application),
  `FormParseError` (presentation); all extend `ValueError`.
- Method signatures trace to [SD-001] and [OC-001].

---

[DM-001]: dm.md
[SD-001]: sd.md
[OC-001]: oc.md
[ADR-0001]: ../../adr/adr-0001-standard-library-web-server.md
[ADR-0002]: ../../adr/adr-0002-downscale-and-quantise.md
[DCD-002]: ../../dcd.md
[bc03eb7]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/commit/bc03eb7b3cde8c44ce99b8ebf9504f5672cfa2d3
