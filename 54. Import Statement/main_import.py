'''
    Main apps for practicing import statement...
'''

# Import statement digunakan untuk mengambil dari file external (.py)

## Usecase 1: Menyambung program dari external
### Misal ada file "program_print.py" yang menampilkan "hello world"
import program_print # Hello World! I'm from 'program_print.py'!

## Usecase 2: Import file dengan data
### Misal pada file "test_variabel.py", ada data list

#### Akses data --> <nama_import>.<nama_data>
import test_variable
print(f"Data pada 'test_variable.py': {test_variable.data}")

## Usecase 3: Import file dengan function
### Misal pada file "tambah.py", ada function untuk menambah dua angka
import tambah

HASIL = tambah.penjumlahan(2.43, 9.123)
print(f"{HASIL:.3f}") # Untuk menampilkan hasil dengan tiga angka dibelakang koma
