# Looping Dictionary

# 0. Assign Data Dictionary mengenai kota-kota di Jakarta
kota_kota = {
    'jakpus': 'Jakarta Pusat',
    'jakbar': 'Jakarta Barat',
    'jaktim': 'Jakarta Timur',
    'jaksel': 'Jakarta Selatan',
    'jakut': 'Jakarta Utara'
}

# 1. Looping Dictionary
for kota in kota_kota:
    print(kota)
    # akan menampilkan key-key yang ada

# 2. Operator untuk mengambil item/iterables
# A. Mengambil item aja
keys = kota_kota.keys()
print(keys) # dict_keys(['jakpus', 'jakbar', 'jaktim', 'jaksel', 'jakut'])

for key in keys:
    print(kota_kota.get(key)) # akan menampilkan value yang bersesuaian dengan key-nya

# B. Mengambil valuesnya aja
values = kota_kota.values()
print(values) # dict_values(['Jakarta Pusat', 'Jakarta Barat', 'Jakarta Timur', 'Jakarta Selatan', 'Jakarta Utara'])

for value in values:
    print(value) # akan menampilkan valuenya aja

# C. Mengambil item, pasangan key-value
items = kota_kota.items()
print(items) #dict_items([('jakpus', 'Jakarta Pusat'), ('jakbar', 'Jakarta Barat'), ('jaktim', 'Jakarta Timur'), ('jaksel', 'Jakarta Selatan'), ('jakut', 'Jakarta Utara')])

for item in items:
    print(item) # akan menampilkan tuples yang berisi: (key, value). salah satunya: ('jakpus', 'Jakarta Pusat')

# Alternatif looping items:
for key, value in items:
    print(f"Key: {key}, punya value: {value}")
