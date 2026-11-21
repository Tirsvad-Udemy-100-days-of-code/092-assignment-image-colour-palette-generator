# Langkah 4: Enjin

🌐 [English](Step-4-Engine) · [Dansk](Step-4-Engine-da) · **Bahasa Melayu**

Pencapaian `MIL-004`. Cabang dan permintaan tarik: satu untuk langkah ini.

![36 ujian enjin lulus dengan liputan 100 %](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/04-engine-tests.png)

## Apa yang dilakukan

Pengiraan warna, belum ada halaman web. `PillowImageReader` menyahkod fail yang
dimuat naik, menukarnya kepada RGBA dan mengecilkannya supaya sisi panjang
paling banyak 300 px. `find_top_colours` membuang piksel lut sinar,
mengumpulkan rona dan memulangkan sepuluh warna paling kerap sebagai nilai
`ColourShare` dengan kod HEX dan bahagian dalam peratus. `PaletteService`
menggabungkan kedua-duanya. Ujian unit membina imej dalam memori.

## Apa yang diperoleh

- Imej hanyalah tatasusunan. Pillow menyahkodnya, dan `reshape(-1, 4)` menukar
  tatasusunan `(height, width, 4)` kepada senarai piksel (pengetahuan Hari 76
  digunakan).
- Topeng boolean membuang piksel lut sinar dalam satu baris:
  `pixels[pixels[:, 3] >= MIN_VISIBLE_ALPHA, :3]`.
- `np.unique(pixels, axis=0, return_counts=True)` mengira setiap warna yang
  berbeza dalam satu panggilan, dan `np.argsort(-counts)[:10]` memilih sepuluh
  yang paling kerap. Tiada gelung Python ke atas piksel diperlukan.
- Foto mempunyai beribu-ribu rona yang hampir sama. Mengumpulkan setiap saluran
  dalam baldi selebar 24 (`DEFAULT_BUCKET_SIZE`, 1 hingga 64 dibenarkan)
  menjadikannya dikira sebagai satu warna, jadi 10 teratas menunjukkan warna
  sebenar dan bukan sepuluh rona langit.
- Mengecilkan kepada 300 px mengekalkan perkadaran warna dan menjadikan
  pengiraan pantas.
- Kod HEX hanyalah tiga saluran yang ditulis dalam asas 16:
  `f"#{red:02X}{green:02X}{blue:02X}"`.
- Dengan NumPy dalam domain dan Pillow dalam infrastruktur, pengiraan diuji
  dengan tatasusunan biasa tanpa fail imej.
