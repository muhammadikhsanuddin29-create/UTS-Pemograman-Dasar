"""
Package net_manager
Berisi modul-modul terpisah untuk mengelola data inventaris perangkat jaringan
dengan menerapkan prinsip Single Responsibility.
"""

from .file_handler import baca_data_json, simpan_data_json
from .processor import (
    cari_perangkat,
    filter_kondisi,
    ambil_lokasi_unik,
    hitung_rekapitulasi,
    hapus_duplikat
)
from .validator import (
    input_teks_valid,
    input_angka_positif,
    input_kondisi_valid,
    validasi_struktur_data
)
