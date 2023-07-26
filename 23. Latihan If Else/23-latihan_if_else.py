# Program Kalkulator Sederhana
print("\n== Program Kalkulator Sederhana ==\n")

print("""Pilihan Operasi:
    1. Perkalian (*)
    2. Pembagian (/)
    3. Pertambahan (+)
    4. Pengurangan (-)
    """)
operator = input("Masukkan operator (1/2/3/4): ")
operand1 = float(input("\nMasukkan angka pertama: "))
operand2 = float(input("Masukkan angka Kedua: "))

if operator == "1":
    hasil = operand1*operand2
    print(f"Hasil dari: {operand1}*{operand2} = {hasil}")
elif operator == "2":
    hasil = operand1/operand2
    print(f"Hasil dari: {operand1}/{operand2} = {hasil}")
elif operator == "3":
    hasil = operand1+operand2
    print(f"Hasil dari: {operand1}+{operand2} = {hasil}")
elif operator == "4":
    hasil = operand1-operand2
    print(f"Hasil dari: {operand1}-{operand2} = {hasil}")
else:
    print(f"Hmm..? --> {operator}?????")