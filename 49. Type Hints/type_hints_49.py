'''
    Type Hints --> sesuai namanya, digunakan untuk mengetahui tipe data yang digunakan pada suatu fungsi. 
    Mengingat fungsi pada python lebih longgar pada penggunaan tipe data, tidak kayak java
'''

def tambah (angka_1, angka_2):
    '''
        Fungsi untuk melakukan penambahan dua angka
    '''
    hasil = angka_1 + angka_2
    return hasil

print(tambah(2,3)) # 5

def tambah_hints(angka_1:int, angka_2:int)->int:
    '''
        Fungsi untuk melakukan penambahan dua angka, tapi pake type hints.

        Sekarang kalo nama fungsinya di-hover, akan muncul tipe data yang diinginkan.
        Meskipun kalo dimasukkannya tidak sesuai dengan tipe data, program akan tetap jalan.
        
        Tidak strict kayak Java.
    '''
    hasil = angka_1 + angka_2
    return hasil


print(tambah_hints(2,3)) # 5
print(tambah_hints(2.3,3)) # 5.3 --> program akan tetap jalan, tapi ada warning (dari extensions)
