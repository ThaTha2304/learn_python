# Misal ada list:
list_0 = [1,2]
list_1 = [3,4]

# Buat nested list
list_nested = [list_0, list_1, -32]
print(f"List nested: {list_nested}\n") # [[1, 2], [3, 4]]

# Kita lakukan copy
list_nested_copy = list_nested.copy()

# Address list
print(f"Address list nested ori: {hex(id(list_nested))}") # 0x258a3dd3840
print(f"Address list nested copy: {hex(id(list_nested_copy))}") # 0x258a3dd30c0
# Secara keseluruhan, listnya punya address yg beda

# address salah satu member list
print(f"Address list nested ori: {hex(id(list_nested[0]))}") # 0x1aeb8758480
print(f"Address list nested copy: {hex(id(list_nested_copy[0]))}") # 0x1aeb8758480
# isi dari listnya, yakni list, punya address yang sama. Konsekuensi--> kalo diubah pada list_nested ori, akan mengubah pada list_nested_copy

# Ubah data member list pada list ori
list_nested[0][0] = 30
print(f"\nList nested ori: {list_nested}") # [[30, 2], [3, 4], -32] # Ubah di ori, copy juga ikut berubah
print(f"List nested copy: {list_nested_copy}\n") # [[30, 2], [3, 4], -32]

# Misal ubah data integernya
list_nested[2] = 0
print(f"\nList nested ori: {list_nested}") # [[30, 2], [3, 4], 0] # kalo integer, ubah di ori, tidak berpengaruh di copy
print(f"List nested copy: {list_nested_copy}\n") # [[30, 2], [3, 4], -32]


# untuk mengatasi permasalahan list itu, digunakan deepcopy dari library copy
from copy import deepcopy

list_nested = [list_0, list_1, -32]
list_nested_deep = deepcopy(list_nested)

# Address list
print(f"Address list nested ori: {hex(id(list_nested))}") # 0x1cf504764c0
print(f"Address list nested deep: {hex(id(list_nested_deep))}") # 0x1cf504764c0
# Secara keseluruhan, listnya punya address yg beda

# address salah satu member list
print(f"Address list nested ori: {hex(id(list_nested[0]))}") # 0x1cf50428640
print(f"Address list nested deep: {hex(id(list_nested_deep[0]))}") # 0x1cf50476f80
# isi dari listnya, yakni list, punya address yang beda, sehingga ketika dilakukan perubahan pada list yg asli, yg copy tidak ikut berubah..

# Ubah data
list_nested[1][0] = 1234
print(f"\nList nested ori: {list_nested}") # [[30, 2], [1234, 4], -32]
print(f"List nested copy: {list_nested_copy}") # [[30, 2], [1234, 4], -32]
print(f"List nested deep: {list_nested_deep}\n") # [[30, 2], [3, 4], -32] # Ketika menggunakan deepcopy, meskipun dilakukan perubahan pada ori, tidak berubah..