'''
    Module untuk mengenalkan __main__

    __main__ adalah top level code environtment
'''

# __name__ == "__main__" akan terjadi jika ada di file program utama

## 1. __name__ pada file program utama
print(f"Nilai __name__ pada main_app_63.py = '{__name__}'")

## 2. __name__ pada file program eksternal (fungsi.py)
import fungsi

## 3. Contoh penggunaan __main__
### Declare Function
def fungsi_tambah(a,b):
    return a+b

if __name__ == "__main__": # jika python di run dari main_app_63.py, fungsi akan berjalan
    hasil = fungsi_tambah(10,5)
    print(f"Hasil Tambah = {hasil}")

## Import package bernama "math"
'''
    Biasanya, di package, akan ada 3 jenis file:
    1. __init__.py
    2. __main__.py
    3. module-module
'''
import math # ketika ini diimport, maka file yg akan dijalankan terlebih dahulu adalah __main__.py