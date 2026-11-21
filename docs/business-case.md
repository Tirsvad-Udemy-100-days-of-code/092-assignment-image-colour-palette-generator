# Business Case: Image Colour Palette Generator

## Metadata

| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition for the Day 92 assignment | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-001 Go, stand-in, not independent | pending |

---

## Summary

Build a small website where a user uploads an image and gets the 10 most
common colours in it, each as a swatch with its HEX code and its share of the
image. The colour counting uses NumPy, as taught on Day 76 of the course. The
project is the Day 92 assignment of "100 Days of Code: The Complete Python Pro
Bootcamp" and is published in the organisation `Tirsvad-Udemy-100_days_of_code`
as `092-assignment-image-colour-palette-generator`.

**Recommendation: Go.** The cost is the course time budget of about 180
minutes plus documentation, there is no money at stake, and the result is a
reusable, documented example for the course community (S02, S03).

## Problem and Opportunity

Designers copy colour codes from palette sites such as Flat UI Colors. Getting
a palette from one's own image needs a tool. The assignment asks for that tool,
and it is a chance to practise NumPy array work on real image data.

## Objectives

| ID | Objective | Stakeholder concerns |
| --- | --- | --- |
| OBJ-1 | Deliver a working website: upload an image, see its top 10 colours as HEX | CN-001, CN-004 |
| OBJ-2 | Practise NumPy image processing on a real task | CN-002 |
| OBJ-3 | Publish readable, runnable, tested code with clear run instructions | CN-003, CN-005 |
| OBJ-4 | Document each step: README, a wiki in English, Danish and Bahasa Malaysia, a screenshot per step and a reflection journal | CN-003, CN-005, CN-007 |
| OBJ-5 | Keep personal tokens and secrets out of the repository | CN-006 |

Stakeholders and concerns are defined in [SA-001].

## Scope

### In Scope

- A web page with an upload form (PNG, JPEG, GIF, BMP, WebP).
- Colour extraction with NumPy: downscale, quantise, count, top 10, HEX.
- A result page with swatches, HEX codes and the share in percent.
- A user setting for the colour step (how close two colours must be to count
  as one), like the reference demo.
- Error messages for a missing file, an unsupported file and a file that is too
  large.
- Unit tests and web tests with pytest.
- Project files: `pyproject.toml`, `constants.py`, `.gitignore`, `.editorconfig`,
  `Doxyfile`, doxygen comments, `README.md` from the framework template.
- Wiki in en, da and ms, one screenshot per milestone, reflection journal.
- Repository description and topics on the git host.

### Out of Scope

- User accounts, storing uploads after the response, a database.
- Hosting the site on the internet (it runs locally).
- Palette export files (ASE, CSS, JSON); copy of HEX text is enough.
- Machine-learning clustering such as k-means from scikit-learn.

## Cost-Benefit

The benefit is qualitative because this is a learning assignment with no
revenue: a completed course step, a portfolio repository and practice of
NumPy. The cost is time only.

| Item | Estimate |
| --- | --- |
| Course time budget for the build | 180 minutes |
| Planning and review documents | 60 minutes |
| Wiki in three languages, screenshots, reflection | 90 minutes |
| Money | 0 (free, open-source tools) |

## Success Criteria

| ID | Criterion | Target |
| --- | --- | --- |
| SC-1 | A valid upload shows the top colours | Exactly 10 swatches, or every distinct colour when the image has fewer than 10 |
| SC-2 | Response time | Under 2 s for a 12-megapixel JPEG on a normal laptop |
| SC-3 | Tests | 100 % of pytest tests pass; line coverage of `src/` at least 90 % |
| SC-4 | Security scan | opengrep reports 0 findings before every push |
| SC-5 | Runtime dependencies | At most 2 (NumPy, Pillow); everything else is a dev dependency |
| SC-6 | Documentation | Every wiki page exists in en, da and ms; one screenshot per milestone in README and wiki; reflection journal present |
| SC-7 | Delivery | One merged pull request per milestone, each closing its issues |

## Assumptions

Each `Decided by default` entry is a choice made where the assignment is
silent; it stays open to challenge by S01.

| ID | Assumption | Decided by default | Rejected alternative |
| --- | --- | --- | --- |
| AS-1 | "Most common" means most pixels after colour quantisation, not exact RGB values, because photos have thousands of near-identical shades | Yes | Exact RGB counting |
| AS-2 | The image is downscaled so its longer side is at most 300 px before counting; the ranking barely changes and the time stays low | Yes | Count every pixel |
| AS-3 | Default colour step is 24 per channel; the user can choose 1 to 64 | Yes | A fixed step |
| AS-4 | Transparent pixels (alpha below 128) are ignored | Yes | Count them as a colour |
| AS-5 | The web server is Python's standard `http.server` with a small multipart parser and HTML view, so the website adds no runtime dependency | Yes | Flask (familiar from the course, but a third dependency), Django (too large) |
| AS-6 | "Python greater than 3.13" means `requires-python = ">=3.14"` | Yes | `>=3.13` |
| AS-7 | Upload limit is 10 MB | Yes | No limit |

## Constraints

- Python 3.14 or later in a local `.venv`; pytest for tests.
- Runtime dependencies kept to what the task needs.
- Folder structure `src/`, `tests/`, `docs/`; constants in `constants.py`.
- Doxygen comments in the source and a `Doxyfile`.
- Tokens come from `.env`, which is never committed, imported or tested.
- opengrep runs on the Product Owner's computer before each push.
- One branch and one pull request per milestone.
- The wording rules of S01 apply to every artifact.

## Risks

| ID | Risk | Impact | Mitigation |
| --- | --- | --- | --- |
| R-1 | Near-identical shades split one visible colour into many | Palette looks wrong | Quantisation step (AS-1, AS-3); tests with known images |
| R-2 | Very large or malformed image (decompression bomb) | Server hangs or crashes | 10 MB limit, Pillow `MAX_IMAGE_PIXELS`, downscale before NumPy work, error page |
| R-3 | NumPy or Pillow has no wheel for the newest Python | Setup fails for S02 | Pin minimum versions known to ship 3.14 wheels; README states the tested version |
| R-4 | A token is committed | Account misuse | `.env` in `.gitignore`, opengrep and the pre-commit hook before push |
| R-5 | Documentation in three languages overruns the time budget | Late delivery | Short pages; English first, translations follow page by page |

## Methodology

ISO/IEC 25010:2023 quality characteristics in the QC checklists, Larman-style
use case and design artifacts, and the plan-first gate of the framework
(`framework/process/plan-first-gate.md`).

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
