# Trin 2: Skelet

🌐 [English](Step-2-Scaffold) · **Dansk** · [Bahasa Melayu](Step-2-Scaffold-ms)

Milepæl `MIL-002`. Branch og pull request: én for dette trin.

![Røgtestene består i .venv](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/02-scaffold-tests.png)

## Hvad blev gjort

Et tomt, men kørbart Python-projekt: `pyproject.toml` (Python 3.14 eller
nyere, NumPy og Pillow som afhængigheder ved kørsel, pytest og pytest-cov til
udvikling), pakken `src/colour_palette/` med `constants.py`, tre røgtests,
en `Doxyfile`, en Python-`.gitignore`, en `.editorconfig` og README med
opsætningstrin. Frameworkets git hooks blev installeret, og opengrep kørte uden
fund før push.

## Hvad vi lærte

- `pyproject.toml` erstatter `requirements.txt` og `setup.py`: én fil
  rummer metadata, afhængigheder og pytest-indstillinger.
  `pip install -e ".[dev]"` installerer projektet og testværktøjerne på én gang.
- `src/`-strukturen får testene til at importere den installerede pakke og
  ikke den mappe, de tilfældigvis køres fra, så en manglende fil viser sig i
  testene.
- Med `constants.py` fra starten har værdier som de ti farver ét sted at bo,
  og en røgtest kan kontrollere, at standardværdierne ligger inden for deres
  grænser.
- En grøn testkørsel før nogen funktionskode viser, at `.venv`, installationen
  og pytest virker, så senere fejl handler om koden.
