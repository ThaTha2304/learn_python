# Operator Assignment
print("\n ~~ OPERATOR ASSIGNMENT ~~")

# A. Operasi Aritmatika
# 1. Pertambahan
print("\n== Pertambahan ==")
a = 5
print("Nilai a:", a)
a += 2 # Alternatif: a = a+2
print("a += 2 -->", a)

a += 3 # Alternatif: a = a+3
print("a += 3 -->", a)

# 2. Pengurangan
print("\n== Pengurangan ==")
a = 5
print("Nilai a:", a)
a -= 2 # Alternatif: a = a-2
print("a -= 2 -->", a)

# 3. Perkalian
print("\n== Perkalian ==")
a = 5
print("Nilai a:", a)
a *= 2 # Alternatif: a = a*2
print("a *= 2 -->", a)

# 4. Pembagian
print("\n== Pembagian ==")
a = 5
print("Nilai a:", a)
a /= 2 # Alternatif: a = a/2
print("a /= 2 -->", a)

# 5. Modulus
print("\n== Modulus ==")
a = 5
print("Nilai a:", a)
a %= 2 # Alternatif: a = a%2
print("a %= 2 -->", a)

# 6. Floor Division
print("\n== Floor Division ==")
a = 5
print("Nilai a:", a)
a //= 2 # Alternatif: a = a//2
print("a //= 2 -->", a)

# B. Operasi Bitwise
# 1. OR
print("\n== OR (|) ==")
c = True
print("Nilai c:", c)
c |= False # Alternatif: c = c | False
print("c |= False -->", c)

c = False
print("Nilai c:", c)
c |= False # Alternatif: c = c | False
print("c |= False -->", c)

# 2. AND
print("\n== AND (&) ==")
c = True
print("Nilai c:", c)
c &= False # Alternatif: c = c & False
print("c &= False -->", c)

c = True
print("Nilai c:", c)
c &= True # Alternatif: c = c & False
print("c &= False -->", c)

# 3. XOR
print("\n== XOR (^) ==")
c = True
print("Nilai c:", c)
c ^= False # Alternatif: c = c ^ False
print("c ^= False -->", c)

c = True
print("Nilai c:", c)
c ^= True # Alternatif: c = c ^ False
print("c ^= False -->", c)

# 4. XOR
print("\n== XOR (^) ==")
c = True
print("Nilai c:", c)
c ^= False # Alternatif: c = c ^ False
print("c ^= False -->", c)

c = True
print("Nilai c:", c)
c ^= True # Alternatif: c = c ^ False
print("c ^= False -->", c)

# 5. Shifting
print("\n== Shifting ==")
d = 0b1001
print("Nilai d:", format(d, "08b"))
d >>= 2 # Alternatif: d = d >> 2 (Geser nilai bit 2 ke kanan)
print("d >>= 2 -->", format(d, "08b"))
d = 0b1001
d <<= 4 # Alternatif: d = d << 4 (Geser nilai bit 4 ke kanan)
print("d <<= 4 -->", format(d, "08b"))
