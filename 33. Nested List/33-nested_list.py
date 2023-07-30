# Data list tradisional:
list_biasa = [1,2,3,4]
print(f"List biasa: {list_biasa}\n") # [1, 2, 3, 4]

# Nested list
list_0 = [1,2]
list_1 = [3,4]

list_nested = [list_0, list_1]
print(f"List nested: {list_nested}\n") # [[1, 2], [3, 4]]

# Use case, misal ada data peserta dalam bentuk list
peserta_1 = ["Lisa",20,"Perempuan"]
peserta_2 = ["Suga",21,"Laki-laki"]
peserta_3 = ["Irene",25,"Perempuan"]

list_peserta = [peserta_1, peserta_2, peserta_3]
print(f"List peserta: {list_peserta}\n") # [['Lisa', 20, 'Perempuan'], ['Suga', 21, 'Laki-laki'], ['Irene', 25, 'Perempuan']]

## Print lebih rapi
for peserta in list_peserta:
    print(f"Nama\t\t: {peserta[0]}")
    print(f"Usia\t\t: {peserta[1]}")
    print(f"Jenis kelamin\t: {peserta[2]}\n")