# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Intan Anugra Salsabila  
NIM: 2225250154  
Kelas: ...

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan

python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan

| Kategori | Syarat | Contoh Masukan |
|---|---|---|
| Ditolak | Nilai ujian bukan 0-100 | 105 |
| Ditolak | Nilai tugas bukan 0-100 | -5 |
| Ditolak | Kehadiran bukan 0-100 | 110 |
| Tidak memenuhi syarat kehadiran | Kehadiran < 80% | 75% |
| Predikat A | Nilai akhir >= 85 | 86 |
| Predikat B | Nilai akhir >= 70 | 73 |
| Predikat C | Nilai akhir >= 60 | 60 |
| Predikat D | Nilai akhir >= 50 | 53 |
| Predikat E | Nilai akhir < 50 | 36 |
| Lulus | Predikat A, B, atau C | C |
| Belum lulus | Predikat D atau E | D |

## Hasil Pengujian

| No | Ujian | Tugas | Kehadiran | Nilai Akhir | Keluaran Aktual | Status |
|---|---:|---:|---:|---:|---|---|
| 1 | 90 | 80 | 95 | 86.00 | Predikat A, Lulus | Berhasil |
| 2 | 75 | 70 | 85 | 73.00 | Predikat B, Lulus | Berhasil |
| 3 | 60 | 60 | 80 | 60.00 | Predikat C, Lulus | Berhasil |
| 4 | 55 | 50 | 90 | 53.00 | Predikat D, Belum lulus | Berhasil |
| 5 | 40 | 30 | 100 | 36.00 | Predikat E, Belum lulus | Berhasil |
| 6 | 90 | 90 | 75 | 90.00 | Tidak memenuhi syarat kehadiran | Berhasil |
| 7 | 105 | 80 | 90 | - | Penolakan rentang nilai ujian | Berhasil |
| 8 | 80 | -5 | 90 | - | Penolakan rentang nilai tugas | Berhasil |
| 9 | 80 | 80 | abc | - | Penolakan tipe | Berhasil |

## Refleksi

Salah satu masukan tidak valid yang diuji adalah kehadiran kurang dari 80 persen. Meskipun nilai akhir tinggi, mahasiswa tetap tidak memenuhi syarat kehadiran. Program menangani kondisi tersebut dengan memeriksa kehadiran sebelum menentukan predikat.