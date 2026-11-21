# System Sequence Diagram: UC-001 Get the colour palette of an image

## Metadata

| Key | Value |
| --- | --- |
| ID | SSD-001 |
| CrossReference | [UC-001], [DM-001], [OC-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted after review RC-014 Go; stand-in review, not independent | pending |

---

## Purpose

The system operations of [UC-001] Get the colour palette of an image, with the
system as a black box.

## Main Success Scenario

```plantuml
@startuml
title SSD-001: UC-001 Get the colour palette of an image
actor Visitor
participant ":System" as System
Visitor -> System : openPage()
System --> Visitor : upload form
Visitor -> System : getPalette(image, colourStep)
System --> Visitor : image and palette (HEX codes, shares)
@enduml
```

Steps 1 and 2 of UC-001 are the `getPalette` message; steps 3 to 5 are its return.
Step 6 (copying a HEX code) happens in the visitor's browser and asks nothing of
the system.

## Alternative Flows

```plantuml
@startuml
title SSD-001: UC-001 alternative flows
actor Visitor
participant ":System" as System
Visitor -> System : getPalette(image, colourStep)
alt 2a no image chosen
  System --> Visitor : "Please choose an image"
else 2b image over 10 MB
  System --> Visitor : "The image is too large"
else 3a not a readable image
  System --> Visitor : "The file is not an image that can be read"
else 3b only transparent pixels
  System --> Visitor : "The image has no visible pixels"
end
@enduml
```

Flow 5a needs no own diagram: the return of `getPalette` simply lists fewer than
ten colours.

---

[UC-001]: uc.md
[DM-001]: dm.md
[OC-001]: oc.md
