# Step 2: Scaffold

🌐 **English** · [Dansk](Step-2-Scaffold-da) · [Bahasa Melayu](Step-2-Scaffold-ms)

Milestone `MIL-002`. Branch and pull request: one for this step.

![Smoke tests passing in the .venv](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/02-scaffold-tests.png)

## What was done

An empty but runnable Python project: `pyproject.toml` (Python 3.14 or newer,
NumPy and Pillow as runtime dependencies, pytest and pytest-cov for
development), the package `src/colour_palette/` with `constants.py`, three
smoke tests, a `Doxyfile`, a Python `.gitignore`, an `.editorconfig` and
the README with setup steps. The framework's git hooks were installed and
opengrep ran clean before the push.

## What was gained

- `pyproject.toml` replaces `requirements.txt` and `setup.py`: one file
  holds the metadata, the dependencies and the pytest settings.
  `pip install -e ".[dev]"` installs the project and its test tools together.
- The `src/` layout makes the tests import the installed package, not the
  folder they happen to run from, so a missing file shows up in the tests.
- With `constants.py` from the start, values such as the ten colours have one
  home, and a smoke test can check that the defaults are within their limits.
- A green test run before any feature code proves that the `.venv`, the
  install and pytest work, so later failures are about the code.
