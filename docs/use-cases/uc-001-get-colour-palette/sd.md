# Sequence Diagram: getPalette

## Metadata

| Key | Value |
| --- | --- |
| ID | SD-001 |
| CrossReference | [OC-001], [DCD-001], [ADR-0001], [ADR-0002] |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-016 Go; stand-in review, not independent | pending |

---

## Purpose

How the classes realise the postconditions of [OC-001] `getPalette`, grouped by
the clean architecture layers. Answers CN-002 (where NumPy does the work) and
CN-003 (readable names) for S01 and S02.

## Diagram

```plantuml
@startuml
title SD-001: getPalette
actor Visitor
box "Delivery" #FADADD
  participant ":PaletteRequestHandler" as Handler <<Controller>>
  participant "parse_multipart_form" as Parser
  participant "render_page" as View
end box
box "Application" #FFF3B0
  participant ":PaletteService" as Service
end box
box "Infrastructure" #D4E4F7
  participant ":PillowImageReader" as Reader
end box
box "Domain" #CDEFD3
  participant "find_top_colours" as Finder
  participant ":ColourShare" as Share
end box

Visitor -> Handler : POST / (image, bucket_size)
activate Handler
alt Content-Length is 0
  Handler --> Visitor : 400 "Please choose an image"
else Content-Length over MAX_UPLOAD_BYTES
  Handler --> Visitor : 413 "The image is too large"
else upload accepted
  Handler -> Parser : parse_multipart_form(body, content_type)
  activate Parser
  Parser --> Handler : fields
  deactivate Parser
  Handler -> Service : build_palette(image_bytes, bucket_size)
  activate Service
  Service -> Reader : read_pixels(image_bytes)
  activate Reader
  note right of Reader : downscale to 300 px, RGBA (ADR-0002)
  alt not an image
    Reader --> Service : raise InvalidImageError
  end
  Reader --> Service : pixels (H x W x 4)
  deactivate Reader
  Service -> Finder : find_top_colours(pixels, count, bucket_size)
  activate Finder
  note right of Finder : drop alpha < 128, quantise,\nnumpy.unique + argsort (ADR-0002)
  alt no visible pixels
    Finder --> Service : raise ValueError
    Service --> Handler : raise PaletteError
  end
  loop up to TOP_COLOUR_COUNT times
    Finder -> Share ** : create(rgb, pixel_count, percentage)
  end
  Finder --> Service : list of ColourShare
  deactivate Finder
  Service --> Handler : palette
  deactivate Service
  Handler -> View : render_page(palette, preview_uri, bucket_size)
  activate View
  View --> Handler : HTML
  deactivate View
  Handler --> Visitor : 200 page with image and palette
end
deactivate Handler
@enduml
```

## Notes

- GRASP Controller: `PaletteRequestHandler` receives the system operation and
  only delegates; `PaletteService` is the use case controller.
- The application layer owns the `ImageReader` protocol; `PillowImageReader`
  implements it, so calls from Application to Infrastructure go through the inner
  layer's interface.
- The exceptions of OC-001 are the `alt` fragments; each ends in an error page
  (status 400 or 413) rendered by `render_page(error=...)`.

---

[OC-001]: oc.md
[DCD-001]: dcd.md
[ADR-0001]: ../../adr/adr-0001-standard-library-web-server.md
[ADR-0002]: ../../adr/adr-0002-downscale-and-quantise.md
