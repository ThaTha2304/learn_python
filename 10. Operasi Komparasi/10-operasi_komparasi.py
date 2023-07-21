# Operasi Komparasi
# < > <= >= == != is isnot

a = 2
b = 4

# Lebih dari (>)
print("\n== Lebih Dari (>) ==")
hasil = a > 3
print(a, '>', 3, "=", hasil)
hasil = b > 3
print(b, '>', 3, "=", hasil)
hasil = a > b
print(a, '>', b, "=", hasil)

# Kurang dari (<)
print("\n== Lebih Dari (<) ==")
hasil = a < 3
print(a, '<', 3, "=", hasil)
hasil = b < 3
print(b, '<', 3, "=", hasil)
hasil = a < b
print(a, '<', b, "=", hasil)

# Lebih dari sama dengan (>=)
print("\n== Lebih Dari (>=) ==")
hasil = a >= 3
print(a, '>=', 3, "=", hasil)
hasil = b >= 3
print(b, '>=', 3, "=", hasil)
hasil = a >= b
print(a, '>=', b, "=", hasil)

# Kurang dari sama dengan (<=)
print("\n== Lebih Dari (<=) ==")
hasil = a <= 3
print(a, '<=', 3, "=", hasil)
hasil = b <= 3
print(b, '<=', 3, "=", hasil)
hasil = a <= b
print(a, '<=', b, "=", hasil)

# Sama dengan (==)
print("\n== Lebih Dari (==) ==")
hasil = a == 3
print(a, '==', 3, "=", hasil)
hasil = b == 3
print(b, '==', 3, "=", hasil)
hasil = a == b
print(a, '==', b, "=", hasil)

# Tidak sama dengan (!=)
print("\n== Lebih Dari (!=) ==")
hasil = a != 3
print(a, '!=', 3, "=", hasil)
hasil = b != 3
print(b, '!=', 3, "=", hasil)
hasil = a != b
print(a, '!=', b, "=", hasil)

# Komparasi object identity (address)

print("\n== KOMPARASI OBJECT IDENTITY ==")
print("Contoh 1. x dan y punya nilai yang sama")
x = 3
y = 3
print("x:", x, ", id:", hex(id(x)))
print("y:", y, ", id:", hex(id(y)))
# Kedua objek punya id yang sama

# is --> compare id dua objek sama atau tidak
print("\n== is ==")
hasil = x is y
print("x is y:", hasil)

# is not --> compare id dua objek beda atau tidak
print("\n== is not ==")
hasil = x is not y
print("x is not y:", hasil)

print("\nContoh 2. x dan y punya nilai yang beda")
x = 3
y = 4
print("x:", x, ", id:", hex(id(x)))
print("y:", y, ", id:", hex(id(y)))
# Kedua objek punya id yang berbeda

# is --> compare id dua objek sama atau tidak
print("\n== is ==")
hasil = x is y
print("x is y:", hasil)

# is not --> compare id dua objek beda atau tidak
print("\n== is not ==")
hasil = x is not y
print("x is not y:", hasil)