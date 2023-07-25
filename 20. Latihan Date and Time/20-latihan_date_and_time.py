# Format data date and time di python digunakan library "datetime"

import datetime as dt

print(f"\n{3*'='} Cek Umur Anda {3*'='}")

# Input tanggal
print("\nMasukkan tanggal lahir anda:")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))
tanggal_input = dt.date(tahun, bulan, tanggal)

print(f"Tanggal lahir yang dimasukan (YYYY-MM-DD): {tanggal_input}")

# Hitung umur
hari_ini = dt.date.today()
umur = hari_ini - tanggal_input
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365) // 30
print(umur.days)
print(f"Saat ini, anda berumur: {umur_tahun} tahun, {umur_bulan} bulan")