# Program Konversi Temperature Dari Reamur ke Celcius, Fahrenheit, dan Kelvin

print("\n== PROGRAM KONVERSI SUHU REAMUR ==\n")

reamur = float(input("Masukkan suhu dalam Reamur: "))
print("Suhu yang anda masukkan:", reamur, "`Reamur\n")

# Convert ke celcius
celcius = (5/4) * reamur
print("Suhu dalam celcius:", celcius, "`Celcius")

# Convert ke fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam fahrenheit:", fahrenheit, "`Fahrenheit")

# Convert ke kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam kelvin:", kelvin, "`Kelvin")