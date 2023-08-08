'''
    Module untuk belajar write ke external file
    
    (Write & Append)
'''

# 1. Mode Write
## Akan membuat file baru jika tidak ada, dan overwrite isinya
with open(file="data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Hellllo first Line") # Cek di file, maka akan muncul kalimat itu

with open(file="data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Whhaadd?! Overwritee?") # Cek di file, maka akan di overwrite

# 2. Mode Append
with open(file="data2.txt", mode="w", encoding="utf-8") as file:
    file.write("Hellllo first Line\n") # Cek di file, maka akan muncul kalimat itu, biar antar kalimat ada 'enter', maka dikasi "\n"

with open(file="data2.txt", mode="a", encoding="utf-8") as file: # note --> mode = 'a'
    file.write("Append yeahh~") # Cek di file, maka akan muncul kalimat itu

# 3. Mode r+
with open(file="data3.txt", mode="w", encoding="utf-8") as file:
    file.write("Hellllo from data3.txt\n") # Cek di file, maka akan muncul kalimat itu, biar antar kalimat ada 'enter', maka dikasi "\n"

with open(file="data3.txt", mode="r+", encoding="utf-8") as file:
    file.write("Line-1\n")
    file.write("Line-2\n")
    file.write("Line-3\n")

with open(file="data3.txt", mode="r+", encoding="utf-8") as file:
    print(file.readlines(),'\n')
    # File sekarang akan berisi: ['Line-1\n', 'Line-2\n', 'Line-3\n']

with open(file="data3.txt", mode="r+", encoding="utf-8") as file:
    file.write("test-1\n") # menimpa isi text sesuai dengan panjang data

with open(file="data3.txt", mode="r+", encoding="utf-8") as file:
    print(file.readlines(),'\n')
    # File sekarang akan berisi: ['test-1\n', 'Line-2\n', 'Line-3\n']
