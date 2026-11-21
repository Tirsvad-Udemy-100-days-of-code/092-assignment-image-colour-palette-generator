# Langkah 2: Rangka

🌐 [English](Step-2-Scaffold) · [Dansk](Step-2-Scaffold-da) · **Bahasa Melayu**

Pencapaian `MIL-002`. Cabang dan permintaan tarik: satu untuk langkah ini.

![Ujian asap lulus dalam .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/02-scaffold-tests.png)

## Apa yang dilakukan

Projek Python yang kosong tetapi boleh dijalankan: `pyproject.toml` (Python
3.14 atau lebih baharu, NumPy dan Pillow sebagai kebergantungan masa jalan,
pytest dan pytest-cov untuk pembangunan), pakej `src/colour_palette/` dengan
`constants.py`, tiga ujian asap, `Doxyfile`, `.gitignore` Python,
`.editorconfig` dan README dengan langkah pemasangan. Git hooks rangka kerja
dipasang dan opengrep berjalan tanpa penemuan sebelum push.

## Apa yang diperoleh

- `pyproject.toml` menggantikan `requirements.txt` dan `setup.py`: satu fail
  menyimpan metadata, kebergantungan dan tetapan pytest.
  `pip install -e ".[dev]"` memasang projek dan alat ujiannya sekali gus.
- Susun atur `src/` memaksa ujian mengimport pakej yang dipasang, bukan folder
  tempat ujian dijalankan, jadi fail yang hilang kelihatan dalam ujian.
- Dengan `constants.py` dari awal, nilai seperti sepuluh warna mempunyai satu
  tempat, dan ujian asap boleh menyemak bahawa nilai lalai berada dalam hadnya.
- Larian ujian yang hijau sebelum sebarang kod ciri membuktikan bahawa `.venv`,
  pemasangan dan pytest berfungsi, jadi kegagalan kemudian adalah tentang kod.
