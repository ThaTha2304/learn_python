# Program Konversi Temperature Dari Celcius ke Reamur, Fahrenheit, dan Kelvin

print("\n== PROGRAM KONVERSI SUHU CELCIUS ==\n")

celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu yang anda masukkan:", celcius, "`Celcius\n")

# Convert ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur:", reamur, "`Reamur")

# Convert ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit:", fahrenheit, "`Fahrenheit")

# Convert ke kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin:", kelvin, "`Kelvin")