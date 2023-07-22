# Operasi dan Manipulasi String
print("== Eps. 16: Operasi dan Manipulasi String ==")

# 1. Menyambung String (Concatenate)
print("\n== 1. Concatenate ==")
nama_pertama = "Taufiq"
nama_tengah = "Agung"
nama_akhir = "Kurniawan"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap) # TaufiqAgungKurniawan --> biar antar kata ada spasi, kasih aja spasi setelah +

# Revisi nama_lengkap
nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap) # Taufiq Agung Kurniawan

# 2. Menghitung Panjang String
print("\n== 2. Panjang String ==")
panjang = len(nama_lengkap)
print("Panjang string: " + str(panjang))

# 3. Operator Untuk String
print("\n== 3. Operator String ==")
# Cek apakah ada suatu komponen (karakter/string) pada sebuah string (in)
print("in")
cek = "t"
status = cek in nama_lengkap
print("Apakah '" + cek + "' ada di '" + nama_lengkap + "'? --> " + str(status)) # False --> karena kita cari "t", di bagian nama, adanya "T" (Case-Sensitive)

cek = "T"
status = cek in nama_lengkap
print("Apakah '" + cek + "' ada di '" + nama_lengkap + "'? --> " + str(status)) # True

cek = "awan"
status = cek in nama_lengkap
print("Apakah '" + cek + "' ada di '" + nama_lengkap + "'? --> " + str(status)) # True

# Ini cek komponen gak ada di string (not in)
print("\nnot in")
cek = "t"
status = cek not in nama_lengkap
print("Apakah '" + cek + "' ada di '" + nama_lengkap + "'? --> " + str(status)) # True

# Mengulang String
print("\nMengulang String")
print("yeay_"*10)
print(5*"_wk")

# Indexing
print("\nIndexing")
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-11: " + nama_lengkap[11])
print("Index ke-(-1): " + nama_lengkap[-1]) # Muter ke index terakhir
print("Index ke-[0:5]: " + nama_lengkap[0:6]) # Akan menampilkan karakter dari index ke-0 sampe index ke-5 (index ke 6-1)
print("Index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:10:2]) # Akan menampilkan karakter dari index ke-0 sampe index ke-10, dengan jarak masing-masing karakter = 2(increment = 2)

# Item Paling Kecil
print("\nItem Paling Kecil (min)")
print("Nilai terkecil: " + min(nama_lengkap)) # spasi
# Item Paling Besar
print("\nItem Paling Besar (max)")
print("Nilai terbesar: " + max(nama_lengkap)) # w

# ASCII Code
print("\nASCII Code")
ascii_code = ord(" ") # Menampilkan ASCII Code dari karakter spasi
print("ASCII Code ' ': " + str(ascii_code)) # 32

ascii_code = ord("w") # Menampilkan ASCII Code dari karakter spasi
print("ASCII Code 'w': " + str(ascii_code)) # 119

data = 100
print("Character dengan ASCII Code: " + str(data) + " adalah --> " + chr(data)) # d

# 4. Operator dalam bentuk method (yes, method in OOP)
print("\n== 4. Operator String (Method) ==")
jumlah = nama_lengkap.count("a")
print("Jumlah huruf 'a' pada string: " + nama_lengkap + " adalah: " + str(jumlah))
