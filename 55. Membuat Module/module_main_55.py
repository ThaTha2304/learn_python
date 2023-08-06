'''
    Pengenalan module.

    Module is just like python file.

    File ini kita coba import file dengan nama module langsung..
'''

# Misal kita punya file matematika.py, didalamnya ada function untuk melakukan operasi aritmatika
# seperti penambahan, perkalian, dan pangkat

# Untuk menggunakan module matematika.py, kita import dulu
import matematika

HASIL_TAMBAH = matematika.pertambahan(1,2,3,4,5)
print(f"hasil_pertambahan: {HASIL_TAMBAH}")

HASIL_KALI = matematika.perkalian(1,2,3,4,5)
print(f"hasil_perkalian: {HASIL_KALI}")

pangkat3 = matematika.pangkat(3)
HASIL_PANGKAT = pangkat3(9)
print(f"Hasil Pangkat 9^3 = {HASIL_PANGKAT}")
