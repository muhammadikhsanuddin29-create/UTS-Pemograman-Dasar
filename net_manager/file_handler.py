import json
import os


def baca_data_json(filepath: str) -> list:
    """
    Membaca daftar perangkat dari file JSON.

    Args:
        filepath (str): Lokasi path file JSON sumber.

    Returns:
        list: Daftar dictionary data perangkat.

    Raises:
        FileNotFoundError: Jika file tidak ditemukan di path yang ditentukan.
        ValueError: Jika format isi file JSON rusak atau bukan berupa list.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File tidak ditemukan: '{filepath}'")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Format root JSON harus berupa list/array objek.")
            return data
    except json.JSONDecodeError as err:
        raise ValueError(f"File JSON korup atau sintaks tidak valid: {err}")


def simpan_data_json(filepath: str, data) -> bool:
    """
    Menyimpan data (list atau dict) ke dalam file JSON secara rapi.

    Args:
        filepath (str): Lokasi path file tujuan.
        data (list | dict): Data yang akan disimpan.

    Returns:
        bool: True jika penyimpanan berhasil.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return True
