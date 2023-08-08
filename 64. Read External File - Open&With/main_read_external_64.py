'''
    Module untuk belajar cara read external file, dengan menggunakan "Open" dan "With" Statement
'''

# 0. Misal kita punya nama-nama kota di Jakarta, ada di file "jakarta.txt"

# 1. Open
file = open(file="jakarta.txt", mode="r")

print(f"Readable? : {file.readable()}") # True --> karena mode="r"
print(f"Writeable? : {file.writable()}") # False

## Baca seluruh file
# print(file.read()) # --> akan menampilkan semuanya yg ada di file

## Baca per-baris # --> hanya menampilkan per baris
# print(file.readline()) # Jakarta Timur\n --> baris pertama
# print(file.readline()) # Jakarta Selatan\n --> baris pertama
# print(file.readline()) # Jakarta Barat\n --> baris pertama

## Baca semua baris sebagai list
print(file.readlines()) # ['Jakarta Timur\n', 'Jakarta Selatan\n', 'Jakarta Barat\n', 'Jakarta Utara\n', 'Jakarta Pusat']

## Setelah selesai akses file, jangan lupa close file
print(f"Apakah file sudah di-close? : {file.closed}") # False
file.close()
print(f"Apakah file sudah di-close? : {file.closed}") # True

# 2. With --> auto nge-close
with open(file="jakarta.txt", mode="r") as file:
    print(file.readlines())
    print(f"Apakah file sudah di-close? : {file.closed}") # False
print(f"Apakah file sudah di-close? : {file.closed}") # True