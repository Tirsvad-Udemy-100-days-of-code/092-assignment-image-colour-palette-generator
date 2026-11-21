# Install

🌐 **English** · [Dansk](Install-da) · [Bahasa Melayu](Install-ms)

Create a local virtual environment in `.venv`, upgrade pip and install the project with its test tools. You need Python 3.14 or newer.

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows (PowerShell):

```powershell
py -3.14 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the app and open <http://127.0.0.1:8000>. Stop it with `Ctrl+C`.

```bash
python -m colour_palette
```

Run the tests:

```bash
python -m pytest
```
