'''
    Membahas semua tentang function:
        Episode 44: Pengenalan Fungsi
        Episode 45: Fungsi dengan Argument
        Episode 46: Fungsi dengan Kembalian (Return)
        Episode 47: Default Argument pada Fungsi
'''

# 1. Fungsi tanpa argumen
print("\n1. Fungsi Tanpa Argumen\n")
def menyapa():
    '''
        Menampilkan string hello world
    '''
    print("Hello World")
    print("Hello Dunia")
menyapa()

# 2. Fungsi dengan Argument
print("\n2. Fungsi dengan Argument\n")
def menyapa_lagi(nama):
    '''
    Menyapa dengan argument, berupa nama
    '''
    print(f"Hello {nama}!")

menyapa_lagi("ThaTha")

# 3. Fungsi dengan Kembalian (Return)
print("\n3. Fungsi dengan Kembalian (Return)\n")
def operasi_aritmatika(angka_1, angka_2):
    '''
    Fungsi untuk menhitung operasi aritmatika antara dua bilangan.
        - Pertambahan (+)
        - Pengurangan (-)
        - Perkalian (*)
        - Pembagian (/)
    '''
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

a,b,c,d = operasi_aritmatika(10,3)
print(f'Pertambahan = {a}')
print(f'Pengurangan = {b}')
print(f'Perkalian = {c}')
print(f'Pembagian = {d}')

# 4. Fungsi dengan Default Argument
print("\n4. Fungsi dengan Default Argument\n")
def perpangkatan(angka, pangkat = 2):
    '''
    Fungsi akan menghitung nilai dari pangkat suatu angka. Nilai default pangkat = 2
    '''
    return angka**pangkat

print(perpangkatan(4,3))
print(perpangkatan(angka=2, pangkat=10))