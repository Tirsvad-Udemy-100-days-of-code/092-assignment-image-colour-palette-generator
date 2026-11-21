# Trin 3: Design

🌐 [English](Step-3-Design) · **Dansk** · [Bahasa Melayu](Step-3-Design-ms)

Milepæl `MIL-003`. Branch og pull request: én for dette trin.

![Use case UC-001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/03-design-use-case.png)

## Hvad blev gjort

Én use case, `UC-001` *Get the colour palette of an image*, med sine
alternative forløb: ingen fil, en fil over 10 MB, en fil der ikke er et billede,
et helt gennemsigtigt billede og færre end ti farver. To beslutninger blev
skrevet ned som ADR'er: `ADR-0001` leverer siden med standardbibliotekets
`http.server`, og `ADR-0002` skalerer billedet ned til 300 px og samler næsten
ens nuancer før optællingen. Derefter blev use casen designet som domænemodel,
systemsekvensdiagram, operationskontrakt, sekvensdiagram og designklassediagram,
hver gennemgået før den næste.

## Hvad vi lærte

- De alternative forløb fandt de svære tilfælde, før koden gjorde. "Hvad hvis
  billedet er gennemsigtigt?" blev forretningsregel `BR-1`: pixels med alpha
  under 128 tælles ikke med.
- En ADR skriver hvorfor, ikke kun hvad. Uden den ligner valget af
  `http.server` frem for Flask en forglemmelse; med den er det en beslutning om
  at holde afhængighederne ved kørsel nede.
- Designklassediagrammet gav lagene deres navne før koden:
  `PillowImageReader` (infrastruktur), `find_top_colours` (domæne) og
  `PaletteService` (applikation). De næste to trin skulle bare udfylde dem.
