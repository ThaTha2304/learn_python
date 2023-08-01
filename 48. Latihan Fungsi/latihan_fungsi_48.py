'''
    Episode 48: Latihan Fungsi.

    Program untuk menghitung luas dan keliling (asumsi: segi empat), 
    dengan panjang dan lebar diinput oleh user.
'''
import os

def header():
    '''
    Fungsi untuk menampilkan header program
    '''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING BANGUN DATAR':^40}")
    print(f"{'-'*40}\n")

def input_user():
    '''
    Fungsi untuk melakukan input dari user
    '''
    panjang = int(input("Masukkan panjang bangun datar: "))
    lebar = int(input("Masukkan lebar bangun datar: "))

    return panjang, lebar

def luas(panjang, lebar):
    '''
    Fungsi untuk menghitung luas bangun datar
    '''
    return panjang*lebar

def keliling(panjang, lebar):
    '''
    Fungsi untuk menghitung keliling bangun datar
    '''
    return 2*(panjang+lebar)

def tampilkan_hasil(pesan, nilai):
    '''
    Fungsi untuk menampilkan pesan hasil penghitungan
    '''
    print(f"Nilai dari {pesan} bangun datar = {nilai}")

def opsi_operasi():
    '''
        Fungsi untuk memilih operasi yang diinginkan:
        Operasi yang dimaksud:
        1. Luas
        2. Keliling
        3. Luas dan Keliling
        '''
    while True:
        print('''\nPilihan operasi:
        1. Luas
        2. Keliling
        3. Luas dan Keliling''')
        opsi = int(input("Operasi yang ingin dilakukan? (1/2/3): "))

        if opsi in (1,2,3):
            break
        print(f"Heyy... pilihan anda tidak sesuai --> {opsi}")
    return opsi

# Main Program
while True:
    # Header program
    header()

    # Input data
    PANJANG, LEBAR = input_user()

    # Operasi penghitungan
    LUAS = luas(PANJANG, LEBAR)
    KELILING = keliling(PANJANG, LEBAR)
    
    # Pilih operasi yang ditampilkan
    operasi = opsi_operasi()
    if operasi == 1:
        tampilkan_hasil("luas", LUAS)
    elif operasi == 2:
        tampilkan_hasil("keliling", KELILING)
    else:
        tampilkan_hasil("luas", LUAS)
        tampilkan_hasil("keliling", KELILING)

    # Pemilihan apa mau lanjut ato tidak
    isLanjut = input("\nApakah anda ingin melanjutkan program? (y/n): ")
    if isLanjut == "n":
        break

print("\nTERIMA KASIH~~")
