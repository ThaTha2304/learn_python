# Operator bitwise (masing-masing bit)

a = 9 # 00001001
b = 5 # 00000101

# 1. Bitwise OR (|)
print("== 1. OR (|) ==")
c = a | b
print("Nilai:", a, ", biner:", format(a, "08b")) 
print("Nilai:", b, ", biner:", format(b, "08b"))
print("======================= (|)")
print("Nilai:", c, ", biner:", format(c, "08b")) # 13 --> 00001101

# 2. Bitwise AND (&)
print("\n== 2. AND (&) ==")
c = a & b
print("Nilai:", a, ", biner:", format(a, "08b"))
print("Nilai:", b, ", biner:", format(b, "08b"))
print("======================= (&)")
print("Nilai:", c, ", biner:", format(c, "08b")) # 1 --> 00000001

# 3. Bitwise XOR (^)
print("\n== 3. XOR (^) ==")
c = a ^ b
print("Nilai:", a, ", biner:", format(a, "08b"))
print("Nilai:", b, ", biner:", format(b, "08b"))
print("======================= (^)")
print("Nilai:", c, ", biner:", format(c, "08b")) # 12 --> 00001100

# 4. Bitwise NOT (~)
'''
    Bitwise NOT --> kebalikannya
    ~0 = -1
    ~1 = -2
    ~2 = -3 
    ...
    dsb
'''
print("\n== 4. NOT (~) ==")
c = ~a
print("Nilai:", a, ", biner:", format(a, "08b"))
print("======================= (~)")
print("Nilai:", c, ", biner:", format(c, "08b")) # -10 --> -0001010

# KALO EMANG BENER-BENER DI FLIP MASING-MASING NILAI BIT, GUNAKAN INI:
a = 9
c = ~a
print("Nilai:", a, ", biner:", format(a, "08b"))
print("======================= (~)")
print("Nilai:", c, ", biner:", format(c&0xFF, "08b")) # -10 --> 11110110

# 5. Shifting
## 5.a. Shifting Right (>>)
print("\n== 5. SHIFTING RIGHT (>>) ==")
c = a>>2 # Nilai bit geser 2 ke kanan
print("Nilai:", a, ", biner:", format(a, "08b")) # 00001001
print("======================= (>>)")
print("Nilai:", c, ", biner:", format(c, "08b")) # 00000010

c = a>>1 # Nilai bit geser 1 ke kanan
print("\nNilai:", a, ", biner:", format(a, "08b")) # 00001001
print("======================= (>>)")
print("Nilai:", c, ", biner:", format(c, "08b"))   # 00000100

## 5.b. Shifting Left (<<)
print("\n== 5. SHIFTING LEFT (<<) ==")
c = a<<2 # Nilai bit geser 2 ke kiri
print("Nilai:", a, ", biner:", format(a, "08b")) # 00001001
print("======================= (<<)")
print("Nilai:", c, ", biner:", format(c, "08b")) # 00100100

c = a<<4 # Nilai bit geser 4 ke kiri
print("\nNilai:", a, ", biner:", format(a, "08b")) # 00001001
print("======================= (<<4")
print("Nilai:", c, ", biner:", format(c, "08b"))   # 10010000
