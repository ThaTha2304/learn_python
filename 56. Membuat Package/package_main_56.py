'''
    Belajar Package (folder)

    File-file python bisa dikelompokkan berdasarkan fungsi-fungsi tertentu. 
    File tersebut dapat dikelompokkan didalam suatu folder. Folder itu namanya package.
'''

# Misal kita bikin package dengan nama "matematika".
# Didalam package itu, ada file untuk melakukan operasi pertambahan dan perkalian

# ada beberapa cara untuk melakukan import:
## 1. Langsung import
import matematika.tambah

## 2. Pake from
from matematika import kali

## 3. Pake alias
from matematika.pangkat import perpangkatan as power

TAMBAH = matematika.tambah.pertambahan(1,2,3,4,5)
print(f"Hasil Tambah: {TAMBAH}")

KALI = kali.perkalian(1,4,5,6,7)
print(f"Hasil Kali: {KALI}")

pangkat3 = power(3)
PANGKAT = pangkat3(9)
print(f"Hasil dari 9^3 {PANGKAT}")