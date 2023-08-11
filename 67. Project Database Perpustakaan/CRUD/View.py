'''
    Module yang berisi tampilan yang akan dilihat oleh user
'''
# import Database
# import Operasi

from .Database import DB_NAME
from . import Operasi
import random
import time
import string


def read_console():
    '''
        Fungsi untuk membaca data yang dimasukkan pada database.

        Jika database tidak ditemukan, maka diasumsikan database belum dibuat.
        Oleh karena itu, akan dilakukan penambahan 1 data terlebih dahulu ke dalam database.
    '''
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

def add_console():
    '''
        Function untuk melakukan penambahan data pada database yang sudah ada
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

    format_input = f"\n{pk};{waktu_buat};{judul};{penulis};{str(tahun)}"
    Operasi.add_db(format_input)
    # print(format_input)

def update_console():
    '''
        Function untuk mengubah data yang telah dimasukkan ke Database sebelumnya...
    '''

    data_baru = []

    print("\nData yang sudah anda masukkan sebelumnya:")
    read_console()

    try:
        update_choice = int(input("Masukkan no Data yang ingin Anda update: "))

        # Membuka dan membaca file database
        with open(file = DB_NAME, mode="r") as file:
            content = file.readlines()
        
        # Iterasi untuk setiap data pada database
        for index, data in enumerate(content):
            data_splited = data.split(';')
            judul = data_splited[2]
            penulis = data_splited[3]
            tahun = data_splited[4]

            # Seleksi pilihan baris data yg ingin diupdate
            if update_choice <= 0 or update_choice > len(content):
                # Masuk kesini jika pilihan tidak benar
                print("Data tidak ditemukan...")
                break
            elif update_choice-1 == index:
                # Masuk kesini jika ditemukan datanya
                print("\nData yang ingin Anda update: ")
                print(f"-Judul\t : {judul}")
                print(f"-Penulis : {penulis}")
                print(f"-Tahun\t : {tahun}")

                print("\nData apa yang ingin Anda update?")
                print("1. Judul")
                print("2. Penulis")
                print("3. Tahun")

                # Menentukan atribut data apa yang ingin diupdate
                atribute_choice = int(input("Masukkan pilihan Anda (1/2/3): "))
                match atribute_choice:
                    case 1:
                        edit = input("\nMasukkan judul yang baru: ")
                        data_splited[2] = edit
                    case 2:
                        edit = input("\nMasukkan penulis yang baru: ")
                        data_splited[3] = edit
                    case 3:
                        edit = input("\nMasukkan tahun yang baru: ")
                        data_splited[4] = edit
                    case other:
                        print("Input salah..")

                # Data terbaru yang sudah dilakukan update, dilakukan join
                data_edit = ';'.join(data_splited)
                data_baru.append(data_edit)
            
            else:
                # Masuk kesini jika ada data, tapi tidak masuk pilihan
                data_baru.append(data)
        
        # Data baru yang telah di-update, dimasukkan ke dalam function update_db(list)
        Operasi.update_db(data_baru)
    except:
        print("Database tidak ditemukan...")
