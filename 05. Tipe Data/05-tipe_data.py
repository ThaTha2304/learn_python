# Tipe-tipe data pada python

# 1. Angka satuan bulat (integer)
data_integer = 10
print("data :", data_integer, "==> tipe:", type(data_integer))

# 2. Angka desimal (float)
data_float = 10.51
print("data :", data_float, "==> tipe:", type(data_float))

# 3. Kumpulan character (string)
data_string = "Lalisa"
print("data :", data_string, "==> tipe:", type(data_string))

# 4. Biner (True/False) (boolean)
data_bool = True
print("data :", data_bool, "==> tipe:", type(data_bool))

# 5. Bilangan kompleks (complex)
data_complex = complex(6,5)
print("data :", data_complex, "==> tipe:", type(data_complex))

# 6. Tipe data dari bahasa C (complex)
from ctypes import c_long
data_c_long = c_long(1055)
print("data :", data_c_long, "==> tipe:", type(data_c_long))