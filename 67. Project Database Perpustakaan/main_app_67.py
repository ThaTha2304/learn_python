'''
    Main app for library database project
'''

import os
import CRUD

if __name__ == "__main__":
    # Ambil nama sistem operasi yang digunakan untuk menjalankan program
    sistem_operasi = os.name

    while(True):
        # Buat clear terminal, disesuaikan dengan nama OS
        match sistem_operasi:
            case "posix":
                os.system("clear") # unix, macos
            case "nt":
                os.system("cls") # windows

        # Header Program
        print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
        print(f"{'DATABASE PERPUSTAKAAN':^30}")
        print(f"{'2023':^30}")
        print(30*"=")
        
        # Menu Program
        print("Menu:")
        print("1. Read Data")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        # Input pilihan user dari menu yang disediakan
        user_option = input("Masukkan pilihan anda (1/2/3/4): ")

        # Seleksi input dari user
        match user_option:
            # Menu 1
            case "1":
                print("\nData yang telah dimasukkan ke dalam Database:")
                CRUD.View.read_console()
                
            # Menu 2
            case "2":
                print(f"\n{30*'-'}")
                print("Tambah Data")
                print(30*"-")
            # Menu 3
            case "3":
                print(f"\n{30*'-'}")
                print("Update Data")
                print(30*"-")
            # Menu 4
            case "4":
                print(f"\n{30*'-'}")
                print("Delete Data")
                print(30*"-")
            # Selain 1/2/3/4
            case other:
                print("Input anda salah!")

        # Input user, apakah lanjut program
        is_done = input("\nLanjut? (y/n): ")

        # Seleksi, jika user tidak melanjutkan program, while-loop selesai
        if is_done.lower() == 'n':
            break