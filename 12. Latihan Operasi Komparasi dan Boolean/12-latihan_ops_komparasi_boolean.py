# Latihan operasi komparasi dan boolean
# Membuat gabungan area rentang bilangan

# KASUS 1: Angka kurang dari 3 atau lebih dari 10
print("\n=== KASUS 1 ===\n")
# ++++++ 3 ----------- 10 ++++++
# Bilangan yang punya nilai kurang dari 3 atau lebih dari 10 = True

data = float(input("Masukkan angka \nkurang dari 3, lebih dari 10: "))
print("\nAngka yang anda masukkan:", data)

# +++++ 3 ----------------------
# Cek angka kurang dari 3
isKurangDari = data < 3
print("Angka kurang dari 3:", isKurangDari)

# -------------------- 10 +++++
# Cek angka lebih dari 10
isLebihDari = data > 10
print("Angka lebih dari 10:", isLebihDari)

# ++++++ 3 ----------- 10 ++++++
# Cek angka kurang dari 3 atau lebih dari 10
hasil = isKurangDari or isLebihDari
print("Angka yang anda masukkan:", hasil)

print("\n=== KASUS 2 ===\n")

# KASUS 2: Angka kurang dari 10 dan lebih dari 3
# ----- 3 ++++++++++ 10 -----
# Bilangan yang punya nilai kurang dari 10 dan lebih dari 3 = True

data = float(input("Masukkan angka \nlebih dari 3, kurang dari 10: "))
print("\nAngka yang anda masukkan:", data)

# ----- 3 +++++++++++++++++
# Cek angka lebih dari 3
isLebihDari = data > 3
print("Angka lebih dari 3:", isLebihDari)

# +++++++++++++++++ 10 -----
# Cek angka kurang dari 10
isKurangDari = data > 10
print("Angka kurang dari 10:", isKurangDari)

# ----- 3 ++++++++++ 10 -----
# Cek angka kurang dari 10 dan lebih dari 3
hasil = isKurangDari and isLebihDari
print("Angka yang anda masukkan:", hasil)