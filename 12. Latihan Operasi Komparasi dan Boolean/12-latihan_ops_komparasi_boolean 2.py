# Latihan operasi komparasi dan boolean
# Membuat gabungan area rentang bilangan

# KASUS 1: Angka lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11
print("\n=== KASUS 1 ===\n")
# ---- 0 ++++ 5 ---- 8 ++++ 11 ----
# Angka lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11 = True

data = float(input("Masukkan angka \nlebih dari 0, kurang dari 5 \nlebih dari 8, kurang dari 11: "))
print("\nAngka yang anda masukkan:", data)

# Cek ---- 0 ++++ 5 ---- 8 ++++ 11 ----
hasil =  ((data > 0) and (data < 5)) or ((data > 8) and (data < 11))
print("Angka yang anda masukkan:", hasil)

# KASUS 2: Angka kurang dari 10 dan lebih dari 3
print("\n=== KASUS 2 ===\n")
# ++++ 0 ---- 5 ++++ 8 ---- 11 ++++
# Bilangan yang punya nilai kurang dari 0, atau lebih dari 5 dan kurang dari 8, atau lebih dari 11 = True

data = float(input("Masukkan angka \nkurang dari 0,\nlebih dari 5, kurang dari 8\nlebih dari 11: "))
print("\nAngka yang anda masukkan:", data)

# Cek ++++ 0 ---- 5 ++++ 8 ---- 11 ++++
hasil =  data < 0 or (data > 5 and data < 8) or data > 11
print("Angka yang anda masukkan:", hasil)