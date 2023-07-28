# LIST --> macam array di bahasa pemrograman lain (array di python pake numpy)
print("\n== LIST ==\n")

# Kumpulan data integer
data_int = [1,2,3,4]
print(f"List integer: {data_int}\n")

# Kumpulan data float
data_float = [1.2, 2.1, 3.0, 4.5]
print(f"List float: {data_float}\n")

# Kumpulan data angka (campuran integer+float)
data_angka = [1, 2, -3.0, 0]
print(f"List angka: {data_angka}\n")

# Kumpulan data string
data_string = ["alpha", 'beta', 'gamma']
print(f"List string: {data_string}\n")

# Kumpulan data boolean
data_bool = [True, False, True]
print(f"List bool: {data_bool}\n")

# Kumpulan data campuran
data_campuran = [1, "Gamma", True, 2.0]
print(f"List campuran: {data_campuran}\n")

# Membuat list dengan range
data_range = list(range(6)) # isinya list dengan angka dari 0-5
print(f"List range: {data_range}\n")

# Membuat list dengan for loop
data_for = [i for i in range(10)] 
print(f"List for: {data_for}\n") # isinya: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Membuat list kuadrat
data_for = [i**2 for i in range(10)] 
print(f"List for: {data_for}\n") # isinya: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Membuat list pake for loop + if
data_for_if = [i for i in range(10) if i%2 == 1] # List yang berisi 'i' yang ada didalam range(10) dan punya kondisi i%2 == 1 (Ganjil)
print(f"List for loop: {data_for_if}\n") # isinya: [1, 3, 5, 7, 9]

data_for_if = [i for i in range(10) if i %2 == 0] # List yang berisi 'i' yang ada didalam range(10) dan punya kondisi i%2 == 0 (Genap)
print(f"List for loop: {data_for_if}\n") # isinya: [0, 2, 4, 6, 8]
