# Operasi List Part 2
print(f"\n== Operasi List ==\n")

data_angka = [1,2,4,1,2,6,7,5,3,0]
print(f"Data Angka: {data_angka}")

data_string = ["Alpha", "Beta", "Gamma"]
print(f"Data String: {data_string}")

# 1. Count Data
print("1. Count Data")
print(f"Count angka 3: {data_angka.count(3)}") # 1
print(f"Count angka 5: {data_angka.count(5)}") # 1
print(f"Count angka 9: {data_angka.count(9)}") # 0

# 2. Ambil Posisi Index
print("\n2. Index Data")
print(f"Index member 'Alpha': {data_string.index('Alpha')}") # 0
print(f"Index member 'Beta': {data_string.index('Beta')}") # 1

# 3. Mengurutkan List
print("\n3. Mengurutkan List")

# A. Min --> Max
print(f"Data Angka Ori: {data_angka}")
data_angka.sort() # Sort data dari terkecil ke terbesar
print(f"Data Angka Modif: {data_angka}")

# B. Max --> Min
data_angka = [1,2,4,1,2,6,7,5,3,0]
print(f"Data Angka Ori: {data_angka}")
data_angka.sort(reverse=True) # Sort data dari terbesar ke terkecil
print(f"Data Angka Modif: {data_angka}")

# 4. Membalikkan Urutan List
print("\n4. Membalikkan Urutan List")
data_angka = [1,2,4,1,2,6,7,5,3,0]
print(f"Data Angka Ori: {data_angka}") # [1, 2, 4, 1, 2, 6, 7, 5, 3, 0]
data_angka.reverse() # Membalikkan urutan
print(f"Data Angka Modif: {data_angka}") # [0, 3, 5, 7, 6, 2, 1, 4, 2, 1]


