'''
    File ini mencoba import file dengan "from"
'''

from matematika import pertambahan, perkalian
from matematika import pangkat

HASIL_PERTAMBAHAN = pertambahan(5,6,7,8,9,10)
print(f"Hasil pertambahan: {HASIL_PERTAMBAHAN}")

HASIL_PERKALIAN = perkalian(12,13,234,123124)
print(f"Hasil perkalian: {HASIL_PERKALIAN}")

pangkat4 = pangkat(4)
HASIL_PANGKAT = pangkat4(5)
print(f"Hasil dari 5^4 = {HASIL_PANGKAT}")
