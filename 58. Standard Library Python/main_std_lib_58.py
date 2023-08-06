'''
    Beberapa Standard Library pada Python:

    https://docs.python.org/3.8/library/index.html

    *sesuaikan dengan versi python yg diinstal
'''

# 1. Library untuk menampilkan waktu
import datetime

# menampilkan waktu sekarang
waktu = datetime.datetime.now()
print(f"Sekarang: {waktu}")

# Menampilkan Hari
print(f"Sekarang hari: {waktu.strftime('%A')}")

# Menampilkan Tahun
print(f"Sekarang Tahun: {waktu.year}, bulan: {waktu.month}, tanggal: {waktu.day}")

# 2. Library collections data
from collections import Counter

# Misal kita ada data list:
data_list = ["1","4","4","2","4","6","7","3","2","5","6","9","1","9","8"]
# Kita ingin menghitung jumlah data yg unik
unique_data = Counter(data_list)
print(unique_data)

# 3. Library untuk akses file (io)
import io 

file = io.open('file_txt.txt', "r")
print(file.read())