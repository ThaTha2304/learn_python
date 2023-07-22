# Format String
print("\n== Eps. 18: Format String ==")
nama = "ThaTha"

# 1. Contoh Umum
print("\n-- 1. Contoh Generic --")
# Biasanya, kalo nampilin teks ama variabel macam 'nama', nulis syntax macam ni:
print("Hello " + nama + ". Apa Kabar?")
# Semakin kompleks kalo teks yg mau ditampilin semakin panjang...

# Solusi? --> Format String...
format_str = f"Hello {nama}. Apa Kabar?"
print(format_str)

# 2. Boolean
print("\n-- 2. Boolean --")
boolean = True
format_str = f"Nilai Boolean: {boolean}"
print(format_str)

# 3. Angka
print("\n-- 3. Angka --")
angka = 123.5
format_str = f"Angka: {angka}"
print(format_str)

# 4. Bilangan Bulat (Integer)
print("\n-- 4. Bilangan Bulat (Integer) --")
angka = 123
format_str = f"Angka: {angka:d}"
print(format_str)

# 5. Bilangan Dengan Ordo Ribuan
print("\n-- 5. Bilangan Dengan Ordo Ribuan --")
angka = 1235500
format_str = f"Angka: {angka:,}" # Dikasih pemisah antar ribuan --> 1,235,500 
print(format_str)

# 6. Bilangan Desimal
print("\n-- 6. Bilangan Desimal --")
angka = 123.3255
format_str = f"Angka: {angka:.2f}" # Bilangan desimal, 2 angka dibelakang desimal --> 123.33
print(format_str)
format_str = f"Angka: {angka:.3f}" # Bilangan desimal, 3 angka dibelakang desimal --> 123.326
print(format_str)

# 7. Leading Zero
print("\n-- 7. Leading Zero --")
angka = 123.3255
format_str = f"Angka: {angka:010.3f}" # Akan menampilkan 10 karakter angka
print(format_str)
'''
    Data kita = 123.326 (Pembulatan), panjang = 7 karakter
    Kita bikin format string untuk menampilkan 10 karakter, sehingga masih ada sisa 3 karakter
    3 karakter itu diisi sama angka "0"
    Awal:   123.326
    Jadi:   000123.326
''' 

# 8. Menampilkan Tanda Plus (+) atau Minus (-)
print("\n-- 8. Menampilkan Tanda Plus (+) atau Minus (-) --")
positif = 123
negatif = -123.3255
format_positif = f"Angka: {positif:+d}" # +123
print(format_positif)
format_negatif = f"Angka: {negatif:+.3f}" # -123.326
print(format_negatif)

# 9. Format Persen
print("\n-- 9. Format Persen --")
angka = 0.05
format_str = f"Angka: {angka:.2%}" # Akan menampilkan dalam bentuk persen, dengan 2 angka dibelakang desimal
print(format_str)

# 10. Format Angka Lain (Binary, Octal, Hexadecimal)
print("\n-- 10. Format Angka Lain (Binary, Octal, Hexadecimal) --")
angka = 255
format_binary = f"binary: {bin(255)}"
format_octal = f"octal: {oct(255)}"
format_hex = f"hex: {hex(255)}"
print(format_binary)
print(format_octal)
print(format_hex)

# 11. Operasi Matematika
harga = 10000
jumlah = 5
bayar = f"Tagihan: Rp. {harga*jumlah:,}"
print(bayar)