# Program Konversi Temperature Dari Fahrenheit ke Celcius, Reamur, dan Kelvin

print("\n== PROGRAM KONVERSI SUHU FAHRENHEIT ==\n")

fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("Suhu yang anda masukkan:", fahrenheit, "`Fahrenheit\n")

# Convert ke celcius
celcius = (5/9) * (fahrenheit-32)
print("Suhu dalam celcius:", celcius, "`Celcius")

# Convert ke reamur
reamur = (4/9) * (fahrenheit - 32)
print("Suhu dalam reamur:", reamur, "`Reamur")

# Convert ke kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin:", kelvin, "`Kelvin")