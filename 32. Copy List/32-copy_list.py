# Copy List
print("\n== Copy List ==\n")

# Assign List
a = ["Gamma", "Theta", "Sigma"]
b = a # Assign variabel b 

# Kalo di print, hasilnya akan sama
print(f"a : {a}") # ['Gamma', 'Theta', 'Sigma']
print(f"b : {b}") # ['Gamma', 'Theta', 'Sigma']

# Misal ubah member
print("\nUbah Member \n")
print("Original:")
print(f"a : {a}") # ['Gamma', 'Theta', 'Sigma']
print(f"b : {b}") # ['Gamma', 'Theta', 'Sigma']

a[0] = "Alpha"

print("Modif:")
print(f"a : {a}") # ['Alpha', 'Theta', 'Sigma']
print(f"b : {b}") # ['Alpha', 'Theta', 'Sigma']

print("\nUbah Member (Lagi)\n")
print("Original:")
print(f"a : {a}") # ['Gamma', 'Theta', 'Sigma']
print(f"b : {b}") # ['Gamma', 'Theta', 'Sigma']

b[2] = "Beta"

print("Modif:")
print(f"a : {a}") # ['Alpha', 'Theta', 'Beta']
print(f"b : {b}") # ['Alpha', 'Theta', 'Beta']

# Jika dilakukan perubahan, baik pada list a maupun list b, keduanya akan ada perubahan...
# Memori kedua list?
print("\nMemori List\n")
print(f"Memory a: {hex(id(a))}") # 0x1f9b11c8500
print(f"Memory b: {hex(id(b))}") # 0x1f9b11c8500
# Keduanya punya memori yang sama, so, kalo ada perubahan di salah satu list, maka kedua list akan terpengaruh...

# Solusinya gimana dong???
print("\nSolusi Copy List\n")

c = a.copy()
print(f"a : {a}") # ['Alpha', 'Theta', 'Beta']
print(f"b : {b}") # ['Alpha', 'Theta', 'Beta']
print(f"c : {c}") # ['Alpha', 'Theta', 'Beta']

# Perubahan pada a
a.pop()
print("Modif pada a...")
print(f"a : {a}") # ['Alpha', 'Theta']
print(f"b : {b}") # ['Alpha', 'Theta']
print(f"c : {c}") # ['Alpha', 'Theta', 'Beta'] # List c tidak terpengaruh

# Perubahan pada c
c.append("Phi")
print(f"a : {a}") # ['Alpha', 'Theta']
print(f"b : {b}") # ['Alpha', 'Theta']
print(f"c : {c}") # ['Alpha', 'Theta', 'Beta', 'Phi'] # Hanya list C yang bertambah, sedangkan list a dan b tetap...
