# Looping list
print("\n== Looping List & Enumerate ==\n")
# Misal ada data nama-nama peserta:
data_nama = ["Lisa", "Jennie", "Jisoo", "Rose"]
# Untuk mengakses nama, bisa menggunakan beberapa looping:

# 1. For Loop
print("1. For Loop \n")

for nama in data_nama:
    print(f"Nama: {nama}")

# 2. For Loop Pake range
print("\n2. For Loop Pake Range \n")
panjang_data = len(data_nama)

for i in range(panjang_data):
    print(f"Nama: {data_nama[i]}")

# 3. While Loop
print("\n3. While Loop \n")
panjang_data = len(data_nama)
i = 0
while i < panjang_data:
    print(f"Nama: {data_nama[i]}")
    i += 1

# 4. List Comprehension
print("\n4. List Comprehension\n")
# List comprehension --> [aksi(<nama_var>) for <nama_var> in <nama_list>]

# 4.1. Print Data
[print(f"Nama: {nama}") for nama in data_nama]

# 4.2. Manipulasi Data
data_angka = [1,7,8,9,10]
data_angka_kuadrat = [angka**2 for angka in data_angka]
print(f"Data angka: {data_angka}") # [1, 7, 8, 9, 10]
print(f"Data angka kuadrat: {data_angka_kuadrat}") # [1, 49, 64, 81, 100]

# 5. Enumerate --> bisa nampilin data dan indexnya
print("\n5. Enumerate\n")

for index,nama in enumerate(data_nama):
    print(f"Peserta ke-{index}, namanya: {nama}")