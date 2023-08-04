'''
    # Learn global and local scope.

    ### Recap:

    * Global Scope: bisa diakses dimana aja
    * Local Scope: hanya dapat diakses pada sub-program tertentu aja
'''

# 1.  GLobal variabel --> scopenya global

# Akses variabel dalam function
def say_hi():
    '''
        Function untuk menyapa "NAMA", test global variabel aj si..
    '''
    print(f"Hello World, say Hi to: {NAMA}!") # GLobal variabel masih dapat teraskses diisini

NAMA = "Lisa"
say_hi() # Hello World, say Hi to: Lisa! 
# Note that, u can acces "NAMA", with the function is defined first!

# Akses variabel dalam looping
for i in range (0,5):
    print(f"Loop ke-{i}, say Hi to: {NAMA}!") # Global variabel dapat terakses

# Akses variabel dalam percabangan
if True:
    print(f"It is True. Say Hi to {NAMA}") # GLobal variabel masih dapat terakses

# 2. Local Variabel, scopenya hanya terbatas dimana dia di-assign
def menyapa_local():
    '''
        Test Local Scope
    '''
    nama_local = "Jennie"
    print(f"Local Pride: {nama_local}")

menyapa_local()
# print(f"Local Pride: {nama_local}") --> ini bakalan error, karena "nama_local" didefinisikan didalam function. 
# Hanya dapat diakses dalam function

# 3. Ganti variabel GLobal didalam function
NAMA = "LISA"
USIA = 23

def ganti_nama(nama_baru, usia_baru):
    '''
        FUnction untuk melihat cara ganti variabel global didalam function (Tapi gak works)

        Variabel global, harus dikasih keyword "global" di awalnya
    '''
    NAMA = nama_baru
    USIA = usia_baru

print(f"Nama asli: {NAMA}, usia asli: {USIA}") # Nama asli: LISA, usia asli: 23
ganti_nama("Rose", 19)
print(f"Nama modif: {NAMA}, usia modif: {USIA}") # Nama modif: LISA, usia modif: 23 (Gak berubah)

def ganti_nama_rev(nama_baru, usia_baru):
    '''
        FUnction untuk melihat cara ganti variabel global didalam function, revisi
    '''
    # Variabel NAMA dan USIA merujuk ke global variabel
    global NAMA
    global USIA

    NAMA = nama_baru
    USIA = usia_baru

print(f"Nama asli: {NAMA}, usia asli: {USIA}") # Nama asli: LISA, usia asli: 23
ganti_nama_rev("Rose", 19)
print(f"Nama modif: {NAMA}, usia modif: {USIA}") # Nama modif: Rose, usia modif: 19
