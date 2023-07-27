# Control Flow (Pass, Continue, Break)

# 1. Pass
print("\n== 1. Pass ==\n")
angka = 0
while angka < 5:
    pass 
    '''
        Misalnya ingin buat loop, tapi masih bikin kerangkanya aja, isinya belum ada. Di python kalo loop kosongan kek gitu bakalan error. So, that's why kita tambahin syntax pass di dalamnya.

        Pass semacam dummy, gabakalan eksekusi apa-apa
    '''
    angka += 1
print("End of Pass Example.\n")

angka = 0
while angka < 5:
    print(f"Loop ke-{angka}")
    if angka == 3:
        pass
        print("Wuidii") # Tetap ditampilkan, meski ada pass
    angka += 1
print("End of Pass Example.\n")

# 2. Continue
print("\n== 2. Continue ==\n")

angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        continue # Loop ke-3 akan di-skip
    print(f"Loop ke-{angka}")
print("End of Continue Example.\n")

# 3. Break
print("\n== 3. Break ==\n")

angka = 0
while angka < 10:
    print(f"Loop ke-{angka}")
    angka += 1
    if angka == 6:
        break # Hanya menampilkan sampai loop ke-5
print("End of Break Example.\n")