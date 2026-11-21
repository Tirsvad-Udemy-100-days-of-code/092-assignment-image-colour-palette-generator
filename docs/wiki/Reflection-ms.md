# Refleksi

🌐 [English](Reflection) · [Dansk](Reflection-da) · **Bahasa Melayu**

## Cara saya mendekati projek ini

Saya merancang sebelum menulis kod: Kes Perniagaan, Analisis Pihak
Berkepentingan dan enam pencapaian, setiap satu dengan cabang dan permintaan
tarik sendiri. Reka bentuk (kes guna, ADR dan rajah) datang sebelum enjin, dan
enjin sebelum laman web, jadi setiap langkah berdiri di atas langkah yang telah
diuji.

## Apa yang mudah

- Mengira warna dengan NumPy. Apabila imej menjadi tatasusunan,
  `np.unique(axis=0, return_counts=True)` dan `np.argsort` melakukan seluruh
  kerja dalam dua baris.
- Menukar RGB kepada HEX dengan f-string.
- Menguji enjin: imej yang dibina dalam memori dengan warna yang diketahui
  memberikan hasil jangkaan yang tepat.

## Apa yang sukar

- Mendapatkan warna yang kelihatan betul. Mengira warna tepat dalam foto
  memberikan sepuluh rona langit yang sama, jadi rona perlu dikumpulkan, dan
  saiz baldi ialah pertukaran antara perincian dan palet yang berguna.
- Membaca muat naik tanpa rangka kerja web. Modul `cgi` telah tiada dalam
  Python 3.13, jadi borang multipart dihuraikan dengan `email.parser`.
- Imej lut sinar, yang mudah dilupakan sehingga kes guna bertanya tentangnya.

## Apa yang akan saya lakukan secara berbeza lain kali

- Menentukan tangkapan skrin bagi setiap langkah semasa merancang, supaya ia
  diambil apabila langkah digabungkan dan bukan selepasnya.
- Menulis aliran alternatif kes guna lebih awal lagi. Ia menemui kebanyakan
  kes ralat yang kemudiannya perlu dikendalikan oleh laman web.

## Pengajaran terbesar

Imej hanyalah tatasusunan NumPy, dan kebanyakan soalan tentang imej ialah
soalan tentang tatasusunan. Bahagian yang sukar bukanlah pengiraan, tetapi
menentukan maksud "warna yang sama".
