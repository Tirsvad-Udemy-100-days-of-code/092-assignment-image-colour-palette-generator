# Pemasangan

🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

Cipta persekitaran maya setempat dalam `.venv`, naik taraf pip dan pasang projek bersama alat ujiannya. Anda memerlukan Python 3.14 atau lebih baharu.

Linux dan macOS:

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

Jalankan aplikasi dan buka <http://127.0.0.1:8000>. Hentikannya dengan `Ctrl+C`.

```bash
python -m colour_palette
```

Jalankan ujian:

```bash
python -m pytest
```
