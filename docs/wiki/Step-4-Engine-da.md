# Trin 4: Motor

🌐 [English](Step-4-Engine) · **Dansk** · [Bahasa Melayu](Step-4-Engine-ms)

Milepæl `MIL-004`. Branch og pull request: én for dette trin.

![36 motortests består med 100 % dækning](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/04-engine-tests.png)

## Hvad blev gjort

Farveoptællingen, endnu uden en webside. `PillowImageReader` afkoder uploaden,
konverterer den til RGBA og skalerer den, så den lange side højst er 300 px.
`find_top_colours` fjerner gennemsigtige pixels, samler nuancerne og
returnerer de ti mest almindelige farver som `ColourShare`-værdier med en
HEX-kode og en andel i procent. `PaletteService` binder de to sammen.
Enhedstestene bygger deres billeder i hukommelsen.

## Hvad vi lærte

- Et billede er bare et array. Pillow afkoder det, og `reshape(-1, 4)` gør et
  `(height, width, 4)`-array til en liste af pixels (viden fra dag 76 i brug).
- En boolsk maske fjerner gennemsigtige pixels på én linje:
  `pixels[pixels[:, 3] >= MIN_VISIBLE_ALPHA, :3]`.
- `np.unique(pixels, axis=0, return_counts=True)` tæller hver forskellig farve
  i ét kald, og `np.argsort(-counts)[:10]` vælger de ti mest almindelige. Der
  er ikke brug for en Python-løkke over pixels.
- Et foto har tusindvis af næsten ens nuancer. Når hver kanal grupperes i
  intervaller på 24 (`DEFAULT_BUCKET_SIZE`, 1 til 64 tilladt), tæller de som
  én farve, så top 10 viser rigtige farver i stedet for ti nuancer af himlen.
- Nedskalering til 300 px bevarer farvernes forhold og gør optællingen hurtig.
- En HEX-kode er blot de tre kanaler skrevet i 16-talssystemet:
  `f"#{red:02X}{green:02X}{blue:02X}"`.
- Når NumPy bor i domænet og Pillow i infrastrukturen, kan optællingen testes
  med almindelige arrays uden billedfiler.
