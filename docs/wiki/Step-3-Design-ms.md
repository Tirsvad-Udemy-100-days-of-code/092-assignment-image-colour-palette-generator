# Langkah 3: Reka Bentuk

🌐 [English](Step-3-Design) · [Dansk](Step-3-Design-da) · **Bahasa Melayu**

Pencapaian `MIL-003`. Cabang dan permintaan tarik: satu untuk langkah ini.

![Kes guna UC-001](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/03-design-use-case.png)

## Apa yang dilakukan

Satu kes guna, `UC-001` *Get the colour palette of an image*, dengan aliran
alternatifnya: tiada fail, fail melebihi 10 MB, fail yang bukan imej, imej yang
lut sinar sepenuhnya, dan kurang daripada sepuluh warna. Dua keputusan direkod
sebagai ADR: `ADR-0001` menyediakan laman dengan `http.server` pustaka
standard, dan `ADR-0002` mengecilkan imej kepada 300 px dan mengumpulkan rona
yang hampir sama sebelum mengira. Kes guna itu kemudian direka bentuk sebagai
model domain, rajah jujukan sistem, kontrak operasi, rajah jujukan dan rajah
kelas reka bentuk, setiap satu disemak sebelum yang seterusnya.

## Apa yang diperoleh

- Aliran alternatif menemui kes sukar sebelum kod. "Bagaimana jika imej lut
  sinar?" menjadi peraturan perniagaan `BR-1`: piksel dengan alpha di bawah
  128 tidak dikira.
- ADR merekod sebabnya, bukan hanya apa. Tanpanya, memilih `http.server`
  berbanding Flask kelihatan seperti terlepas pandang; dengannya, ia keputusan
  untuk mengurangkan kebergantungan masa jalan.
- Rajah kelas reka bentuk memberi nama kepada lapisan sebelum kod:
  `PillowImageReader` (infrastruktur), `find_top_colours` (domain) dan
  `PaletteService` (aplikasi). Dua langkah seterusnya hanya perlu mengisinya.
