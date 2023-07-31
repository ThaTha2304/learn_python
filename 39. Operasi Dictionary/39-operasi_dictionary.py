# Operator Dictionary

# 0. Assign Data Dictionary mengenai kota-kota di Jakarta
data_dict = {
    'jakpus': 'Jakarta Pusat',
    'jakbar': 'Jakarta Barat',
    'jaktim': 'Jakarta Timur',
    'jaksel': 'Jakarta Selatan',
    'jakut': 'Jakarta Utara'
}

# 1. Panjang Data
LENDICT = len(data_dict)
print(f"Panjang data: {LENDICT}")

# 2. Cek Key Exist atau Tidak
KEY = 'jakpus'
CHECK_KEY = KEY in data_dict # True
print(f"Apakah KEY: '{KEY}' ada di data_dict? --> {CHECK_KEY}") # True

KEY = 'jabar'
CHECK_KEY = KEY in data_dict # False
print(f"Apakah KEY: '{KEY}' ada di data_dict? --> {CHECK_KEY}") # False

# 3. Akses value (read)
## Traditional Way
print(data_dict['jakbar']) # Print valuenya --> "Jakarta Barat"
### Kalo print dengan key yang tidak exist, maka akan error:
# print(data_dict['jabar']) # Error

# Paling aman pake method .get()
print(data_dict.get('jakpus')) # Print valuenya --> "Jakarta Pusat"
print(data_dict.get('jabar')) # Tidak ada key "jabar" di data, akan menghasilkan "none" (default)
print(data_dict.get('jabar', "Key tidak ditemukan")) # Karena key tidak ada, bisa dilakukan modifikasi pada pesan error yang ditampilkan. Output --> "Key tidak ditemukan"

# 4. Update Data
# Update data dengan key "jakbar". Dari "Jakarta Barat", jadi "JAKARTA BARAT"
data_dict['jakbar'] = "JAKARTA BARAT"
print(data_dict) # {'jakpus': 'Jakarta Pusat', 'jakbar': 'JAKARTA BARAT', 'jaktim': 'Jakarta Timur', 'jaksel': 'Jakarta Selatan', 'jakut': 'Jakarta Utara'}

# Buat data baru, dengan key yang belum pernah dimasukkan
data_dict['jateng'] = "Jawa Tengah"
print(data_dict) # {'jakpus': 'Jakarta Pusat', 'jakbar': 'JAKARTA BARAT', 'jaktim': 'Jakarta Timur', 'jaksel': 'Jakarta Selatan', 'jakut': 'Jakarta Utara', 'jateng': 'Jawa Tengah'}

# Selain itu, bisa menggunakan method .update()
data_dict.update({"jakbar" : "Jakarta Barat"})
print(data_dict) # {'jakpus': 'Jakarta Pusat', 'jakbar': 'Jakarta Barat', 'jaktim': 'Jakarta Timur', 'jaksel': 'Jakarta Selatan', 'jakut': 'Jakarta Utara', 'jateng': 'Jawa Tengah'}

# menambah data baru dengan key yang belum pernah dimasukkan
data_dict.update({"jabar" : "Jawa Barat"})
print(data_dict) # {'jakpus': 'Jakarta Pusat', 'jakbar': 'Jakarta Barat', 'jaktim': 'Jakarta Timur', 'jaksel': 'Jakarta Selatan', 'jakut': 'Jakarta Utara', 'jateng': 'Jawa Tengah', 'jabar': 'Jawa Barat'}

# 5. Delete Data
del data_dict['jabar']
print(data_dict) # {'jakpus': 'Jakarta Pusat', 'jakbar': 'Jakarta Barat', 'jaktim': 'Jakarta Timur', 'jaksel': 'Jakarta Selatan', 'jakut': 'Jakarta Utara', 'jateng': 'Jawa Tengah'}
