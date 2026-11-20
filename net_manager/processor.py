def hapus_duplikat(daftar_perangkat: list) -> list:
    """
    Menghapus data perangkat duplikat berdasarkan atribut 'id' menggunakan struktur data set.

    Args:
        daftar_perangkat (list): List dictionary data perangkat.

    Returns:
        list: List perangkat unik tanpa duplikasi ID.
    """
    id_tercatat = set()
    hasil_unik = []
    for item in daftar_perangkat:
        kode_id = item["id"].strip().upper()
        if kode_id not in id_tercatat:
            id_tercatat.add(kode_id)
            hasil_unik.append(item)
    return hasil_unik


def ambil_lokasi_unik(daftar_perangkat: list) -> set:
    """
    Mengambil seluruh nama lokasi laboratorium unik menggunakan set comprehension.

    Args:
        daftar_perangkat (list): List dictionary data perangkat.

    Returns:
        set: Himpunan nama lokasi unik.
    """
    return {item["lokasi"] for item in daftar_perangkat}


def cari_perangkat(daftar_perangkat: list, kata_kunci: str) -> list:
    """
    Mencari perangkat berdasarkan kecocokan substring pada ID, nama, atau lokasi
    menggunakan list comprehension.

    Args:
        daftar_perangkat (list): List dictionary data perangkat.
        kata_kunci (str): Kata kunci pencarian.

    Returns:
        list: Daftar perangkat yang cocok (mengembalikan list kosong jika tidak ada).
    """
    kunci = kata_kunci.strip().lower()
    if not kunci:
        return []
    return [
        item for item in daftar_perangkat
        if kunci in item["id"].lower()
        or kunci in item["nama"].lower()
        or kunci in item["lokasi"].lower()
    ]


def filter_kondisi(daftar_perangkat: list, kondisi_target: str) -> list:
    """
    Memfilter perangkat berdasarkan status kondisi tertentu menggunakan list comprehension.

    Args:
        daftar_perangkat (list): List dictionary data perangkat.
        kondisi_target (str): Kondisi target ('Aktif', 'Perbaikan', 'Rusak').

    Returns:
        list: Daftar perangkat dengan kondisi yang sesuai.
    """
    target = kondisi_target.strip().lower()
    return [
        item for item in daftar_perangkat
        if item["kondisi"].lower() == target
    ]


def hitung_rekapitulasi(daftar_perangkat: list) -> dict:
    """
    Menghitung statistik rekapitulasi total aset, nilai valuasi, serta pengelompokan
    berdasarkan lokasi dan kondisi menggunakan set dan dictionary comprehension.

    Args:
        daftar_perangkat (list): List dictionary data perangkat.

    Returns:
        dict: Kamus hasil rekapitulasi terstruktur.
    """
    if not daftar_perangkat:
        return {
            "total_perangkat": 0,
            "total_nilai_aset_rp": 0,
            "rekap_per_lokasi": {},
            "rekap_per_kondisi": {}
        }

    lokasi_unik = ambil_lokasi_unik(daftar_perangkat)
    kondisi_unik = {item["kondisi"] for item in daftar_perangkat}

    rekap_lokasi = {
        lok: sum(1 for item in daftar_perangkat if item["lokasi"] == lok)
        for lok in sorted(lokasi_unik)
    }

    rekap_kondisi = {
        kon: sum(1 for item in daftar_perangkat if item["kondisi"] == kon)
        for kon in sorted(kondisi_unik)
    }

    total_nilai = sum(item["harga"] for item in daftar_perangkat)

    return {
        "total_perangkat": len(daftar_perangkat),
        "total_nilai_aset_rp": total_nilai,
        "rekap_per_lokasi": rekap_lokasi,
        "rekap_per_kondisi": rekap_kondisi
    }
