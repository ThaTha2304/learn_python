'''
    Module untuk belajar try dan exception (try-catch) runtime error

    runtime error: error yg terjadi saat program dijalankan
'''
# package untuk cek apakah suatu nilai adalah "Number" ato tidak (int/float)
from numbers import Number

# Contoh 1: Error karena Pembagi = 0
while(True):
    print("\nContoh 1 - Kalkulator\n")
    angka = int(input("Masukkan angka: "))
    hasil = 0
    try:
        hasil = 10/angka
        print(f"Hasil = {hasil}")

        isDone = input("Lanjutkan? (y/n): ")
        if isDone == 'n':
            break
    except:
        print("Pembagi nol, silahkan masukkan angka pembagi lagi...")

print("\nAkhir dari program 1\n")

# Contoh 2: Error dengan custom message
def tambah (a,b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise TypeError("Input harus angka!") 
    return a+b 

# print(tambah(3,4))
# print(tambah('a','b'))

# Contoh 3: Error ketika baca file
try:
    with open(file="data.txt", mode="r") as file:
        print(file.read())
except:
    print('File tidak ditemukan... Membuat file baru')
    with open(file='data.txt', mode="w", encoding="utf-8") as file:
        file.write("New Line inside...")

print("\nAkhir dari program 2\n")

# Contoh 4: Error dengan pesan yg sudah spesifik, i.e. ZeroDivisionError
try:
    hasil = 10/0
    print(hasil)
except Exception as error_message:
    print(error_message) # division by zero