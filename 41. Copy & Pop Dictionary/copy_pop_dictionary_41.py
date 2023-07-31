# Copy and Pop Dictionary

# COPY DICTIONARY
# Misal ada dictionary yg berisi kota-kota sbb:
kota_kota = {
    'jakpus': 'Jakarta Pusat',
    'jakbar': 'Jakarta Barat',
    'jaktim': 'Jakarta Timur',
}

# copy dictionary
cities = kota_kota
# Ketika ditampilkan, keduanya akan menampilkan hasil yang sama...
print(f"Kota_kota --> {kota_kota}\n")
print(f"cities --> {cities}\n")

# misal dilakukan perubahan pada salah satu key
kota_kota['jakpus'] = 'JAKARTA PUSAT'
# Ketika ditampilkan, keduanya akan menampilkan hasil yang sama...
print(f"Kota_kota --> {kota_kota}\n")
print(f"cities --> {cities}\n")
# Perubahan di dict kota_kota juga berpengaruh di dict cities
# Untuk mengatasi hal ini, digunakan method .copy()

kota_kota = {
    'jakpus': 'Jakarta Pusat',
    'jakbar': 'Jakarta Barat',
    'jaktim': 'Jakarta Timur',
}

# copy dictionary
cities = kota_kota.copy()

# misal dilakukan perubahan pada salah satu key
kota_kota['jakpus'] = 'JAKARTA PUSAT'
# Perubahan pada dict kota_kota tidak akan mempengaruhi dict cities...
print(f"Kota_kota --> {kota_kota}\n")
print(f"cities --> {cities}\n")

# POP DICTIONARY
# A. .pop()
# Misal ingin mengambil data dari salah satu key saja
data_jakbar = kota_kota.pop("jakbar") #--> .pop(key)
print(f"Data Jakbar: {data_jakbar}") # akan menampilkan valuenya: Jakarta Barat
print(f"Kota_kota --> {kota_kota}\n") # hanya ada jakpus dan jaktim (jakbar sudah di-pop)

# B. .popitems()
# Ingin mengambil data dari item terakhir dari data dict
data_terakhir = kota_kota.popitem()
print(f"Data terakhir pada dict: {data_terakhir}") # akan menghasilkan tuples pasangan key-value
print(f"Kota_kota --> {kota_kota}\n") # hanya ada jakpus, jaktim sudah di-pop (jaktim item terakhir)
