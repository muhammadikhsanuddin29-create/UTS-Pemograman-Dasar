def input_teks_valid(prompt: str) -> str:
    """
    Meminta input string dari pengguna dan memastikan tidak kosong (defensive).

    Args:
        prompt (str): Pesan prompt yang ditampilkan di CLI.

    Returns:
        str: String bersih yang tidak kosong.
    """
    while True:
        nilai = input(prompt).strip()
        if nilai:
            return nilai
        print("[!] Error Input: Kolom ini tidak boleh kosong. Silakan ulangi.")


def input_angka_positif(prompt: str) -> int:
    """
    Meminta input bilangan bulat positif (>= 0) dari pengguna dengan exception handling.

    Args:
        prompt (str): Pesan prompt yang ditampilkan di CLI.

    Returns:
        int: Nilai angka bulat positif yang valid.
    """
    while True:
        mentah = input(prompt).strip()
        try:
            angka = int(mentah)
            if angka < 0:
                print("[!] Error Input: Nilai tidak boleh negatif.")
                continue
            return angka
        except ValueError:
            print(f"[!] Error Input: '{mentah}' bukan angka bulat yang valid.")


def input_kondisi_valid(prompt: str) -> str:
    """
    Memvalidasi input kondisi perangkat agar sesuai dengan kategori standar.

    Args:
        prompt (str): Pesan prompt yang ditampilkan di CLI.

    Returns:
        str: Kondisi perangkat ('Aktif', 'Perbaikan', atau 'Rusak').
    """
    pilihan_sah = {"aktif": "Aktif", "perbaikan": "Perbaikan", "rusak": "Rusak"}
    while True:
        masukan = input(prompt).strip().lower()
        if masukan in pilihan_sah:
            return pilihan_sah[masukan]
        print("[!] Error Input: Pilihan kondisi harus 'Aktif', 'Perbaikan', atau 'Rusak'.")


def validasi_struktur_data(daftar_data: list) -> list:
    """
    Memfilter dan memvalidasi setiap item dictionary dari file JSON agar memiliki
    key wajib dan tipe data yang sesuai (mencegah crash akibat data kotor).

    Args:
        daftar_data (list): Data mentah hasil pembacaan JSON.

    Returns:
        list: Daftar record dictionary yang valid.
    """
    key_wajib = {"id", "nama", "lokasi", "kondisi", "harga"}
    data_bersih = []
    for indeks, item in enumerate(daftar_data, start=1):
        if not isinstance(item, dict):
            print(f"[!] Peringatan: Baris ke-{indeks} bukan objek dictionary, dilewati.")
            continue
        if not key_wajib.issubset(item.keys()):
            print(f"[!] Peringatan: Baris ke-{indeks} kekurangan atribut wajib, dilewati.")
            continue
        if not isinstance(item["harga"], (int, float)) or item["harga"] < 0:
            print(f"[!] Peringatan: Harga tidak valid pada ID '{item.get('id')}', dilewati.")
            continue
        data_bersih.append(item)
    return data_bersih
