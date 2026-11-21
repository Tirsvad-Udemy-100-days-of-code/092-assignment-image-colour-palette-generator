# Trin 5: Hjemmeside

🌐 [English](Step-5-Website) · **Dansk** · [Bahasa Melayu](Step-5-Website-ms)

Milepæl `MIL-005`. Branch og pull request: én for dette trin.

![Upload-siden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-upload-form.png)

![De 10 mest almindelige farver i eksempelbilledet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-top-ten-colours.png)

## Hvad blev gjort

En side med et filfelt, et felt til *Colour grouping* og en
**Find colours**-knap, leveret af `http.server` fra standardbiblioteket. Efter
uploaden viser siden billedet ved siden af ti farveprøver, den mest almindelige
først, hver med sin HEX-kode og sin andel af billedet. Et klik på en farveprøve
kopierer HEX-koden. Uploaden læses i hukommelsen og gemmes aldrig.

## Hvad vi lærte

- Hvordan en browser sender en fil: `multipart/form-data`. Modulet `cgi`,
  som tidligere læste den, blev fjernet i Python 3.13, så formularen læses i
  stedet med `email.parser.BytesParser`.
- En hjemmeside behøver ikke et webframework. Når serveren bruger
  standardbiblioteket, er NumPy og Pillow de eneste afhængigheder ved kørsel.
- Grænser hører hjemme i `constants.py`: uploaden er begrænset til 10 MB
  (`MAX_UPLOAD_BYTES`) og billedet til 50 millioner pixels
  (`MAX_IMAGE_PIXELS`), så én stor upload ikke kan stoppe serveren.
- Webtests kan starte den rigtige server på `127.0.0.1` og en ledig port, så
  hele forløbet testes uden en browser.
