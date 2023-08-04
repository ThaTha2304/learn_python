'''
    *args
    **kargs (keyword-args)
'''

# Fungsi biasa
def tambah (angka_1, angka_2):
    '''
        Fungsi untuk melakukan penambahan dua angka
    '''
    hasil = angka_1 + angka_2
    return hasil

print(tambah(2,3)) # 5

# Usecase: misal ingin melakukan penambahan dengan jumlah argumen banyak, kan kita tidak mungkin juga bikin argumen banyak-banyak di fungsinya.
# Oleh karena itu, kita pake *args
def tambah_hints(*args):
    '''
        Fungsi untuk melakukan penambahan dua angka, tapi pake *args.

        Nama parameter sebenernya bebas, gak harus "*args". Bisa aja pake "*data"
    '''
    print(f"Isi dari args: {args}") # ini akan jadi tuple

    hasil = 0
    for angka in args:
        hasil += angka
    
    print(f"Hasil penjumlahan= {hasil}\n")

tambah_hints(1,2,3,4,5,6,7,8,9)

# **kargs
# usecase, misal kita bikin kalkulator sederhana. Selain memasukkan angka ke dalam fungsi, kita juga memasukkan "keyword" ke dalam fungsi juga. Misal "opsi = kali". Sehingga di dalam fungsi bisa ditambahkan pemilihan kalo milih "kali", akan dilakukan proses perkalian... dsb...
def operasi_matematika(*args, **kargs):
    print(args) # akan berisi tuple data args
    print(kargs) # akan berisi dictionary isinya parameter dengan keyword

    if kargs['opsi'] == "tambah":
        hasil = 0
        for angka in args:
            hasil += angka
        print(f"Hasil penambahan: {hasil}\n")
    elif kargs['opsi'] == "kali":
        hasil = 1
        for angka in args:
            hasil *= angka
        print(f"Hasil perkalian: {hasil}\n")

operasi_matematika(1,2,3,4,5, opsi="tambah")
operasi_matematika(1,2,3,4,5, opsi="kali") #*args = 1,2,3,4,5; **kargs = {'opsi':'kali'}