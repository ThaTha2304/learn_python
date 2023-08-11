'''
    Module yang berisi operasi-operasi pada program (CRUD)
'''
from .Database import DB_NAME

import random
import time
import string

def read_db():
    '''
        Function untuk membaca database (Coming Soon)
    '''
    print("read DB")

def create_db():
    '''
        Function membuat database baru
    '''
    pk = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    waktu_buat = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    judul = input("Masukkan Judul Buku\t\t: ")
    if len(judul) > 255:
        judul = judul[:255]
    penulis = input("Masukkan Penulis Buku\t\t: ")
    if len(penulis) > 255:
        penulis = penulis[:255]

    while(True):
        try:
            tahun = int(input("Masukkan Tahun Terbit Buku\t: "))
            if len(str(tahun)) == 4:
                break
            print("Format tahun harus 4 digit (YYYY)\n")
        except:
            print("Format tahun harus angka (YYYY)\n")
    
    print("\nData yang Anda masukkan:")
    print(f"- Judul: {judul}")
    print(f"- Penulis: {penulis}")
    print(f"- Tahun: {tahun}")

    format_input = f"{pk};{waktu_buat};{judul};{penulis};{str(tahun)}"

    try:
        with open(file = DB_NAME, mode="w", encoding='utf-8') as file:
            file.write(format_input)
    except:
        print("Whoops... Data tidak masuk ke DB :()")

def add_db(format_input):
    '''
        Function untuk menambahkan (append) data ke dalam Database
    '''
    try:
        with open(file = DB_NAME, mode="a", encoding='utf-8') as file:
            file.write(format_input)
    except:
        print("Whoops... Data tidak masuk ke DB :(")

def update_db(data_baru):
    '''
        Function untuk melakukan update pada data yang sudah dimasukkan ke Database
    '''
    try:
        with open(file = DB_NAME, mode="w", encoding='utf-8') as file:
            file.writelines(data_baru)
        print("\nData berhasil di-update...")
    except:
        print("Whoops... Data tidak masuk ke DB :(")