# Multi Keys & Nested Dictionary

import datetime

# Misal kita punya data mahasiswa:
mahasiswa1 = {
    'nama': 'James Bond',
    'nim': '123101',
    'kelas': '3SD2',
    'lahir': datetime.datetime.strptime("2002-10-23", '%Y-%m-%d')
}

mahasiswa2 = {
    'nama': 'Ethan Hunt',
    'nim': '123102',
    'kelas': '3SI3',
    'lahir': datetime.datetime.strptime("2000-2-29", '%Y-%m-%d')
}

mahasiswa3 = {
    'nama': 'Elsa Faust',
    'nim': '123103',
    'kelas': '3SD2',
    'lahir': datetime.datetime.strptime("2001-9-12", '%Y-%m-%d')
}

# Data-data mahasiswa tersebut, dimasukkan ke dalam dictionary
data_mahasiswa = {
    'MHS001': mahasiswa1,
    'MHS002': mahasiswa2,
    'MHS003': mahasiswa3
}

# Menampilkan data mahasiswa:
print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<7} {'KELAS':<6} {'LAHIR':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    KELAS = data_mahasiswa[KEY]['kelas']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")
    
    print(f"{KEY:<6} {NAMA:<17} {NIM:<7} {KELAS:<6} {LAHIR:<10}")