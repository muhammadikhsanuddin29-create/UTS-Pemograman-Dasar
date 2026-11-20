import os
from net_manager import (
    baca_data_json,
    simpan_data_json,
    cari_perangkat,
    filter_kondisi,
    hitung_rekapitulasi,
    hapus_duplikat,
    input_teks_valid,
    input_angka_positif,
    input_kondisi_valid,
    validasi_struktur_data
)

FILE_INPUT = os.path.join("data", "perangkat.json")
FILE_OUTPUT = os.path.join("data", "laporan_rekap.json")


def tampilkan_tabel(daftar: list) -> None:
    """Menampilkan list perangkat dalam format tabel rapi di CLI."""
    if not daftar:
        print("\n[i] Tidak ada data perangkat untuk ditampilkan.")
        return

    garis = "-" * 82
    print(f"\n{garis}")
    print(f"{'ID':<10} | {'Nama Perangkat':<24} | {'Lokasi':<18} | {'Kondisi':<10} | {'Harga (Rp)':>12}")
    print(garis)
    for item in daftar:
        print(
            f"{item['id']:<10} | "
            f"{item['nama'][:24]:<24} | "
            f"{item['lokasi'][:18]:<18} | "
            f"{item['kondisi']:<10} | "
            f"{item['harga']:>12,}"
        )
    print(garis)


def tambah_data_baru(daftar_perangkat: list) -> list:
    """Menangani alur input perangkat baru dari pengguna dan mencegah duplikasi ID."""
    print("\n--- Tambah Data Perangkat Jaringan ---")
    kode_id = input_teks_valid("Masukkan ID Perangkat (mis. NET-006): ").upper()

    # Cek duplikasi ID sebelum menambah
    if any(item["id"].upper() == kode_id for item in daftar_perangkat):
        print(f"[!] Gagal: Perangkat dengan ID '{kode_id}' sudah terdaftar!")
        return daftar_perangkat

    nama = input_teks_valid("Masukkan Nama Perangkat            : ")
    lokasi = input_teks_valid("Masukkan Lokasi Lab/Ruangan        : ")
    kondisi = input_kondisi_valid("Masukkan Kondisi (Aktif/Perbaikan/Rusak): ")
    harga = input_angka_positif("Masukkan Harga Aset (Rp)           : ")

    record_baru = {
        "id": kode_id,
        "nama": nama,
        "lokasi": lokasi,
        "kondisi": kondisi,
        "harga": harga
    }
    daftar_perangkat.append(record_baru)
    simpan_data_json(FILE_INPUT, daftar_perangkat)
    print(f"[+] Berhasil menambahkan '{nama}' ({kode_id}) dan menyimpan ke '{FILE_INPUT}'.")
    return daftar_perangkat


def jalankan_aplikasi() -> None:
    """Fungsi utama pengendali alur menu CLI."""
    print("==========================================================")
    print("   NETASSET MANAGER - Sistem Inventaris Perangkat Lab     ")
    print("==========================================================")

    try:
        data_mentah = baca_data_json(FILE_INPUT)
        data_tervalidasi = validasi_struktur_data(data_mentah)
        daftar_perangkat = hapus_duplikat(data_tervalidasi)
        print(f"[+] Berhasil memuat {len(daftar_perangkat)} data perangkat unik dari '{FILE_INPUT}'.")
    except (FileNotFoundError, ValueError) as err:
        print(f"[!] Peringatan Awal: {err}")
        print("[i] Memulai program dengan daftar inventaris kosong.")
        daftar_perangkat = []

    while True:
        print("\nMenu Utama:")
        print("1. Tampilkan Semua Perangkat")
        print("2. Cari Perangkat (ID / Nama / Lokasi)")
        print("3. Filter Perangkat Berdasarkan Kondisi")
        print("4. Tambah Perangkat Baru")
        print("5. Hitung Rekapitulasi & Ekspor Laporan JSON")
        print("0. Keluar")

        pilihan = input("\nPilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_tabel(daftar_perangkat)

        elif pilihan == "2":
            keyword = input_teks_valid("Masukkan kata kunci pencarian: ")
            hasil = cari_perangkat(daftar_perangkat, keyword)
            print(f"\n[i] Ditemukan {len(hasil)} perangkat untuk kata kunci '{keyword}':")
            tampilkan_tabel(hasil)

        elif pilihan == "3":
            kondisi = input_kondisi_valid("Filter kondisi (Aktif/Perbaikan/Rusak): ")
            hasil = filter_kondisi(daftar_perangkat, kondisi)
            print(f"\n[i] Ditemukan {len(hasil)} perangkat dengan kondisi '{kondisi}':")
            tampilkan_tabel(hasil)

        elif pilihan == "4":
            daftar_perangkat = tambah_data_baru(daftar_perangkat)

        elif pilihan == "5":
            rekap = hitung_rekapitulasi(daftar_perangkat)
            print("\n--- Ringkasan Rekapitulasi Aset ---")
            print(f"Total Perangkat : {rekap['total_perangkat']} unit")
            print(f"Total Nilai Aset: Rp {rekap['total_nilai_aset_rp']:,}")
            print("Distribusi Lokasi:")
            for lok, jml in rekap["rekap_per_lokasi"].items():
                print(f"  - {lok}: {jml} unit")
            print("Status Kondisi:")
            for kon, jml in rekap["rekap_per_kondisi"].items():
                print(f"  - {kon}: {jml} unit")

            simpan_data_json(FILE_OUTPUT, rekap)
            print(f"\n[+] Laporan berhasil diekspor ke '{FILE_OUTPUT}'.")

        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan NetAsset Manager. Sampai jumpa!")
            break

        else:
            print("[!] Pilihan tidak valid. Silakan masukkan angka 0 sampai 5.")


if __name__ == "__main__":
    jalankan_aplikasi()