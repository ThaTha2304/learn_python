# Operasi Logika/Boolean
# not, or, and, xor


# 1. NOT (Kebalikannya)
print("\n== NOT ==")
a = True
c = not a

print("Data a:", a) # True
print("NOT a:", c) # False

# 2. OR (Bernilai true jika minimal satu ada yg true)
print("\n== OR ==")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c) # False

a = True
b = False
c = a or b
print(a, "OR", b, "=", c) # True

a = False
b = True
c = a or b
print(a, "OR", b, "=", c) # True

a = True
b = True
c = a or b
print(a, "OR", b, "=", c) # True

# 3. AND (Bernilai true jika semuanya true)
print("\n== AND ==")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c) # False

a = True
b = False
c = a and b
print(a, "AND", b, "=", c) # False

a = False
b = True
c = a and b
print(a, "AND", b, "=", c) # False

a = True
b = True
c = a and b
print(a, "AND", b, "=", c) # True

# 4. XOR (^) (Bernilai true jika hanya ada satu yang true)
print("\n== XOR ==")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c) # False

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c) # True

a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c) # True

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c) # False