# Langkah 5: Laman Web

🌐 [English](Step-5-Website) · [Dansk](Step-5-Website-da) · **Bahasa Melayu**

Pencapaian `MIL-005`. Cabang dan permintaan tarik: satu untuk langkah ini.

![Halaman muat naik](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-upload-form.png)

![10 warna teratas imej contoh](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-top-ten-colours.png)

## Apa yang dilakukan

Halaman dengan medan fail, medan *Colour grouping* dan butang **Find colours**,
disediakan oleh `http.server` daripada pustaka standard. Selepas muat naik,
halaman memaparkan imej di sebelah sepuluh sampel warna, yang paling kerap
dahulu, masing-masing dengan kod HEX dan bahagiannya dalam imej. Klik pada
sampel warna menyalin kod HEX. Fail yang dimuat naik dibaca dalam memori dan
tidak pernah disimpan.

## Apa yang diperoleh

- Cara pelayar menghantar fail: `multipart/form-data`. Modul `cgi` yang dahulu
  menghuraikannya telah dibuang dalam Python 3.13, jadi borang dihuraikan
  dengan `email.parser.BytesParser`.
- Laman web tidak memerlukan rangka kerja web. Dengan pelayan pada pustaka
  standard, NumPy dan Pillow menjadi satu-satunya kebergantungan masa jalan.
- Had diletakkan dalam `constants.py`: muat naik dihadkan kepada 10 MB
  (`MAX_UPLOAD_BYTES`) dan imej kepada 50 juta piksel (`MAX_IMAGE_PIXELS`),
  supaya satu muat naik yang besar tidak dapat menghentikan pelayan.
- Ujian web boleh menjalankan pelayan sebenar pada `127.0.0.1` dan port yang
  bebas, jadi keseluruhan aliran diuji tanpa pelayar.
