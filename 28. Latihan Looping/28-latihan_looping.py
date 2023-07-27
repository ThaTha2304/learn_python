# Latihan Looping (Membentuk pola segitiga)
# Membentuk pola segitiga dengan sisi 5
"""
+
++
+++
++++
+++++
"""

sisi = 5
index = 1
# 1. Menggunakan for loop
print("1. For Loop Start")
for i in range(sisi):
    print("+"*index)
    index += 1

print("For Loop End\n")

# 2. Menggunakan while loop

index = 1
print("2. While Loop Start")
while True:
    print("+"*index)
    index += 1

    if index > sisi:
        break

print("While Loop End\n")

# 3. Menggunakan while loop --> hanya print segitiga ganjil
'''
*
***
*****
'''
index = 1
print("3. While Loop Start")
while True:
    if index%2:
        # True (Ganjil) --> print
        print("+"*index)
        index += 1
    else:
        # False (Genap) --> skip
        index += 1
        continue

    # Kalo index udah melebihi sisi yang ditentukan, loop selesai
    if index > sisi:
        break

print("While Loop End\n")

# 4. Menggunakan while loop --> hanya print segitiga ganjil, layout ke tengah
'''
  *
 ***
*****
'''
index = 1
spasi = sisi//2
print("3. While Loop Start")
while True:
    if index%2:
        # True (Ganjil) --> print
        print(" "*spasi,"+"*index)
        index += 1
        spasi -= 1
    else:
        # False (Genap) --> skip
        index += 1
        continue

    # Kalo index udah melebihi sisi yang ditentukan, loop selesai
    if index > sisi:
        break

print("While Loop End\n")

# 5. Menggunakan while loop --> hanya print segitiga ganjil, layout ketupat
'''
  *
 ***
*****
 ***
  *
'''
sisi = 2
index = 1
spasi = sisi//2
print("5. While Loop Start")

# Segitiga bagian atas
while True:
    if index%2:
        # True (Ganjil) --> print
        print(" "*spasi,"+"*index)
        index += 1
        spasi -= 1
    else:
        # False (Genap) --> skip
        index += 1
        continue

    # Kalo index udah melebihi sisi yang ditentukan, loop selesai
    if index > sisi:
        break

# Segitiga bagian bawah
index -= 3
spasi = 1
while True:
    if index%2:
        # True (Ganjil) --> print
        print(" "*spasi,"+"*index)
        index -= 1
        spasi += 1
    else:
        # False (Genap) --> skip
        index -= 1
        continue

    # Kalo index udah melebihi sisi yang ditentukan, loop selesai
    if index<=0:
        break
print("While Loop End\n")