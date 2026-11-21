# Refleksion

🌐 [English](Reflection) · **Dansk** · [Bahasa Melayu](Reflection-ms)

## Sådan greb jeg projektet an

Jeg planlagde, før jeg kodede: en Business Case, en interessentanalyse og seks
milepæle, hver med sin egen branch og pull request. Designet (use case, ADR'er
og diagrammer) kom før motoren, og motoren kom før hjemmesiden, så hvert trin
byggede på et testet trin.

## Hvad var let

- At tælle farver med NumPy. Når billedet er et array, klarer
  `np.unique(axis=0, return_counts=True)` og `np.argsort` hele opgaven på to
  linjer.
- At omregne RGB til HEX med en f-string.
- At teste motoren: billeder bygget i hukommelsen med kendte farver giver
  præcise forventede resultater.

## Hvad var svært

- At få farver, der ser rigtige ud. Tæller man de nøjagtige farver i et foto,
  får man ti nuancer af den samme himmel, så nuancerne måtte samles, og
  intervallets størrelse er en afvejning mellem detaljer og en brugbar palet.
- At læse uploaden uden et webframework. Modulet `cgi` er væk i Python 3.13, så
  multipart-formularen læses med `email.parser`.
- Gennemsigtige billeder, som er lette at glemme, indtil use casen spørger til
  dem.

## Hvad jeg vil gøre anderledes næste gang

- Beslutte skærmbilledet til hvert trin allerede under planlægningen, så det
  tages, når trinnet merges, og ikke bagefter.
- Skrive use casens alternative forløb endnu tidligere. De fandt de fleste af
  de fejltilfælde, hjemmesiden senere skulle håndtere.

## Største lærdom

Et billede er bare et NumPy-array, og de fleste spørgsmål om billeder er
spørgsmål om arrays. Det svære er ikke optællingen, men at beslutte, hvad "den
samme farve" betyder.
