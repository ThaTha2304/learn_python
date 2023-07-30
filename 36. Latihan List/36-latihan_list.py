# Program CR (Create-Read) Database Buku

list_buku = []

while True:
    print("\n== PROGRAM DATABASE BUKU ==")
    
    # Input Data Buku
    print("\nMasukkan Data Buku:")
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t: ")
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    # Daftar Buku yang telah dimasukkan
    print("\n== Daftar Buku yang Telah Dimasukkan ==")
    for index, buku in enumerate(list_buku):
        print(f"Data Buku ke-{index+1}:")
        print(f"\tJudul   : {buku[0]}")
        print(f"\tPenulis : {buku[1]}")
    print("-"*20)

    print(20*"=")
    
    # Mau lanjut programnya ato ndak?
    isContinue = input("Apakah anda ingin menambahkan data yang lain (y/n)?: ")
    
    if isContinue == "n":
        break