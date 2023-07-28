# Operasi pada List
print("\n== Operasi Pada List ==\n")

# 1. Akses Data
print("== 1. Akses Data ==")
## misal ada list yg berisi 3 data
myList = ["Alpha", "Beta", "Gamma"]
## index:  0 (-3)   1 (-2)  2 (-1)
print(f"Data List: {myList}")
print(f"Data List index ke-0: {myList[0]}")
print(f"Data List index terakhir (-1): {myList[-1]}")

# 2. Panjang Data pada List
print("\n== 2. Panjang Data pada List ==")
print(f"Panjang data pada list (len): {len(myList)}") # 3

# 3. Manipulasi Data pada List
print("\n== 3. Manipulasi Data pada List ==")

# A. Menambahkan list pada posisi (index) tertentu
print(f"Data List Ori: {myList}") # ['Alpha', 'Beta', 'Gamma']
myList.insert(1, "Sigma") # Masukkan "Sigma" pada index ke-1
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Beta', 'Gamma']

# B. Menambahkan data di akhir list
myList.append("Zetta") # Masukkan "Zetta" di akhir list
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Beta', 'Gamma', 'Zetta']

# C. Menambah List dengan List
newList = ["Phi", "Psi", "Lambda", "Tau"]
myList.extend(newList)
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Beta', 'Gamma', 'Zetta', 'Phi', 'Psi', 'Lambda', 'Tau']

# 4. Mengubah Data
print("\n== 4. Mengubah Data ==")
# Ubah Data pada Index ke-2 menjadi "Theta"
print(f"Data List Ori: {myList}") # ['Alpha', 'Sigma', 'Beta', 'Gamma', 'Zetta', 'Phi', 'Psi', 'Lambda', 'Tau']
print(f"Data index ke-2 ori: {myList[2]}") # Beta
myList[2] = "Theta"
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Theta', 'Gamma', 'Zetta', 'Phi', 'Psi', 'Lambda', 'Tau']
print(f"Data index ke-2 modif: {myList[2]}") # Theta

# 5. Remove Data
print("\n== 5. Remove Data ==")

# A. Remove Data tertentu
print(f"Data List Ori: {myList}") # ['Alpha', 'Sigma', 'Beta', 'Gamma', 'Zetta', 'Phi', 'Psi', 'Lambda', 'Tau']
myList.remove("Phi")
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Theta', 'Gamma', 'Zetta', 'Psi', 'Lambda', 'Tau']
# myList.remove("alpha") --> bakalan error, karena gaada data "alpha" (case-sensitive)

# B. Remove data paling akhir
print(f"Data List Ori: {myList}") # ['Alpha', 'Sigma', 'Theta', 'Gamma', 'Zetta', 'Psi', 'Lambda', 'Tau']
pops = myList.pop()
print(f"Data List Modif: {myList}") # ['Alpha', 'Sigma', 'Theta', 'Gamma', 'Zetta', 'Psi', 'Lambda']
print(f"Data that popped: {pops}") # Tau

# C. Remove data paling awal (index ke-0)
print(f"Data List Ori: {myList}") # ['Alpha', 'Sigma', 'Theta', 'Gamma', 'Zetta', 'Psi', 'Lambda', 'Tau']
pops = myList.pop(0)
print(f"Data List Modif: {myList}") # ['Sigma', 'Theta', 'Gamma', 'Zetta', 'Psi', 'Lambda']
print(f"Data that popped: {pops}") # Alpha