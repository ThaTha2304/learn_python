# Latihan Dictionary Gaes...

import datetime
import os
import random
import string

# Template Dictionary Mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '000000',
    'kelas': 'XXXX',
    'lahir': datetime.datetime.strptime("2002-10-23", '%Y-%m-%d')
}

# Dictionary Data Mahasiswa
data_mahasiswa = {}

while True:
    # Buat dictionary baru, dengan key ambil dari dict template
    mahasiswa_input = dict.fromkeys(mahasiswa_template.keys())

    os.system('cls') # buat ngebersihin terminal
    print(f"{'DATABASE MAHASISWA':^20}")
    print("-"*20,"\n")

    # Input data mahasiswa
    NAMA_MHS = input("Nama Mahasiswa\t\t: ")
    NIM_MHS = input("NIM Mahasiswa\t\t: ")
    KELAS_MHS = input("Kelas Mahasiswa\t\t: ")
    TANGGAL_LAHIR = input("Tanggal Lahir (1-31)\t: ")
    BULAN_LAHIR = input("Bulan Lahir (1-12)\t: ")
    TAHUN_LAHIR = input("Tahun Lahir (YYYY)\t: ")
    format_tanggal = f"{TAHUN_LAHIR}-{BULAN_LAHIR}-{TANGGAL_LAHIR}" # Format tanggal lahir

    # Assign data dari input user ke dict
    mahasiswa_input['nama'] = NAMA_MHS
    mahasiswa_input['nim'] = NIM_MHS
    mahasiswa_input['kelas'] = KELAS_MHS
    mahasiswa_input['lahir'] = datetime.datetime.strptime(format_tanggal, '%Y-%m-%d')
    # Buat key, otomatis random setiap iterasi
    # Gabungkan string kosong dengan string random, uppercase, 6 karakter
    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    # Tambah dictionary mahasiswa_input ke dict data_mahasiswa
    data_mahasiswa.update({KEY:mahasiswa_input})

    # Menampilkan data mahasiswa yang telah ditambahkan
    print(f"\n{'DATA MAHASISWA':^50}\n")
    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<7} {'KELAS':<6} {'LAHIR':<10}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        KELAS = data_mahasiswa[KEY]['kelas']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<7} {KELAS:<6} {LAHIR:<10}")
    
    # Cek apakah mau lanjut nambah data ato ndak?
    isLanjut = input("\nApakah anda ingin menambah data lagi? (y/n): ")

    if isLanjut == "n":
        break

print("\nTERIMA KASIH...\n")
