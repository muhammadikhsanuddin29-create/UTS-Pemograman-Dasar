# UTS-Pemograman-Dasar
# NetAsset Manager — Aplikasi CLI Pengelolaan Inventaris Perangkat Lab

Aplikasi berbasis Command Line Interface (CLI) yang dibangun menggunakan **Python 3 (Standard Library)** untuk membantu administrator laboratorium mengelola, mencari, memfilter, dan merekapitulasi inventaris perangkat jaringan secara terstruktur.

---

## Struktur Direktori Proyek

```text
uts_pemrograman_dasar_netasset/
│
├── main.py                  # Entry point utama aplikasi CLI
├── README.md                # Dokumentasi proyek & petunjuk penggunaan
│
├── net_manager/             # Package buatan sendiri (Single Responsibility)
│   ├── __init__.py          # Inisialisasi package dan ekspor fungsi publik
│   ├── file_handler.py      # Modul operasi baca/tulis file JSON (I/O)
│   ├── processor.py         # Modul logika pencarian, filter, deduplikasi & rekapitulasi
│   └── validator.py         # Modul defensive programming & validasi input
│
└── data/
    ├── perangkat.json       # File dataset input awal
    └── laporan_rekap.json   # File output hasil ekspor rekapitulasi
```

---

## Fitur Utama & Pemenuhan Spesifikasi UTS

1. **Struktur Data Lengkap (`list`, `dict`, `set`)**:
   - `list` untuk menyimpan koleksi seluruh record perangkat.
   - `dict` untuk merepresentasikan atribut detail tiap perangkat (`id`, `nama`, `lokasi`, `kondisi`, `harga`).
   - `set` untuk mengekstrak daftar lokasi unik (`set comprehension`) serta mencegah duplikasi ID perangkat.
2. **Control Flow & Pythonic Comprehension**:
   - Menggunakan percabangan (`if-elif-else`), perulangan (`while`, `for`), *list comprehension* untuk pencarian/filtering, serta *dictionary comprehension* untuk menghitung jumlah perangkat per ruangan dan per kondisi.
3. **Modularitas & Package (`net_manager`)**:
   - Memisahkan tanggung jawab antara I/O file, validasi input, dan pemrosesan logika bisnis ke dalam modul terpisah.
4. **Exception Handling & Defensive Programming**:
   - Menangani kasus file tidak ditemukan (`FileNotFoundError`), file JSON korup (`JSONDecodeError`), struktur JSON tidak valid, input kosong, angka negatif, serta *edge case* saat dataset kosong `[]`.

---

## Cara Menjalankan Aplikasi

1. Pastikan **Python 3.8+** telah terinstal pada sistem Anda.
2. Buka terminal / Command Prompt, lalu arahkan ke direktori utama proyek:
   ```bash
   cd uts_pemrograman_dasar_netasset
   ```
3. Jalankan aplikasi melalui perintah:
   ```bash
   python main.py
   ```
4. Pilih nomor menu (`1` sampai `5`) sesuai kebutuhan operasional, atau `0` untuk keluar.

---

## Package & Dependency

- **Python Standard Library**: `json`, `os` (Tidak memerlukan instalasi library pihak ketiga).

---

## Catatan Referensi & Bantuan AI

- Referensi sintaks & modul standar: [Python 3 Official Documentation](https://docs.python.org/3/).
- Bantuan AI digunakan sebagai asisten perancangan struktur direktori package, peninjauan *edge case* validasi input, dan penyusunan format dokumentasi.
