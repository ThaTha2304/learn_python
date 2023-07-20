# Program Konversi Temperature Dari Kelvin ke Celcius, Reamur, dan Fahrenheit

print("\n== PROGRAM KONVERSI SUHU KELVIN ==\n")

kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("Suhu yang anda masukkan:", kelvin, "`Kelvin\n")

# Convert ke celcius
celcius = kelvin - 273
print("Suhu dalam celcius:", celcius, "`Celcius")

# Convert ke reamur
reamur = (4/5) * (kelvin - 273)
print("Suhu dalam reamur:", reamur, "`Reamur")

# Convert ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit:", fahrenheit, "`Fahrenheit")