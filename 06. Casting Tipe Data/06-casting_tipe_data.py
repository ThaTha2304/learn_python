# Casting --> mengubah tipe data, misal dari integer ke string, dsb

## 1. INTEGER
print("=== INTEGER ===")
data_int = -1
print("data :", data_int, "==> tipe:", type(data_int))

data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int)
print("data :", data_str, "==> tipe:", type(data_str))
print("data :", data_float, "==> tipe:", type(data_float))
print("data :", data_bool, "==> tipe:", type(data_bool)) # False jika nilai int = 0

## 2. FLOAT
print("\n=== FLOAT ===")
data_float = 0.0
print("data :", data_float, "==> tipe:", type(data_float))

data_str = str(data_float)
data_int = int(data_float) # Dibulatkan ke bawah
data_bool = bool(data_float)
print("data :", data_str, "==> tipe:", type(data_str))
print("data :", data_int, "==> tipe:", type(data_int))
print("data :", data_bool, "==> tipe:", type(data_bool)) # False jika nilai float = 0/0.0

## 3. BOOLEAN
print("\n=== BOOLEAN ===")
data_bool = False
print("data :", data_bool, "==> tipe:", type(data_bool))

data_str = str(data_bool)
data_int = int(data_bool) # True = 1, False = 0
data_float = float(data_bool) # True = 1.0, False = 0.0
print("data :", data_str, "==> tipe:", type(data_str))
print("data :", data_int, "==> tipe:", type(data_int))
print("data :", data_float, "==> tipe:", type(data_float))

## 4. STRING
print("\n=== STRING ===")
data_str = "8"
print("data :", data_str, "==> tipe:", type(data_str))

data_bool = bool(data_str) # False jika string kosong. Selain itu, True
data_int = int(data_str) # Hanya bisa convert string angka (integer)
data_float = float(data_str) # Hanya bisa convert string angka (integer)
print("data :", data_bool, "==> tipe:", type(data_bool))
print("data :", data_int, "==> tipe:", type(data_int))
print("data :", data_float, "==> tipe:", type(data_float))
