'''
    Import module dengan alias
'''

# Terserah penamaan aliasnya
from matematika import pertambahan as add
from matematika import perkalian as times
from matematika import pangkat as power_ranger

HASIL_PERTAMBAHAN = add(5,4,3,1,2,7,9)
print(f"Hasil pertambahan: {HASIL_PERTAMBAHAN}")

HASIL_PERKALIAN = times(4,5,6,7,8)
print(f"Hasil perkalian: {HASIL_PERKALIAN}")

pangkat5 = power_ranger(5)
HASIL_PANGKAT = pangkat5(7)
print(f"Hasil dari 7^5: {HASIL_PANGKAT}")