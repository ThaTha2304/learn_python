'''
    __init__.py --> module yang akan dijalankan pertama kali
    ketika melakukan import pada package
'''

import cek # akan menjalankan file __init__.py pada package cek

# misal kita bikin package matematika
# dan hanya melakukan "import matematika"
# agar bisa, kita perlu melakukan import file tambah.py di __init__ pada package matematika
import matematika
from matematika.aritmatika import kali

pangkat3 = matematika.pangkat.perpangkatan(3)
PANGKAT = pangkat3(8)
print(PANGKAT)

TAMBAH = matematika.aritmatika.pertambahan(1,2,3,4,5)
print(TAMBAH)

KALI = matematika.aritmatika.kali.perkalian(1,2,3,4,5)
print(KALI)

KALI_LG = kali.perkalian(1,3,4,5)
print(KALI_LG)