'''
    Module yang berisi tampilan yang akan dilihat oleh user
'''
# import Database
# import Operasi

from .Database import DB_NAME
from . import Operasi


def read_console():
    try:
        with open(file = DB_NAME, mode="r") as file:
            content = file.readlines()
        # Header Tabel
        print("="*105)
        print(f"{'NO':^5}|{'Judul':^45}|{'Penulis':^45}|{'Tahun':^5}")
        print("-"*105)

        # Isi Tabel
        for index, data in enumerate(content):
            data_splited = data.split(';')
            no = index+1
            judul = data_splited[2]
            penulis = data_splited[3]
            tahun = data_splited[4]

            print(f"{no:^5}|{judul:^45}|{penulis:^45}|{tahun:^5}",end="")
            # print(f'{}')
        print(f"\n{105*'='}")

    except:
        print("Database tidak ditemukan...")
        print("Membuat Database baru...\n")
        Operasi.create_db()

    
