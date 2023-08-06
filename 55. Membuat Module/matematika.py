'''
    Module operasi aritmatika

    1. Pertambahan
    2. Perkalian
    3. Perpangkatan
'''

def pertambahan (*args):
    '''
        Function pertambahan
    '''
    hasil = 0
    for angka in args:
        hasil += angka

    return hasil

def perkalian (*args):
    '''
        Function perkalian
    '''
    hasil = 1
    for angka in args:
        hasil *= angka

    return hasil

def pangkat (n:int):
    '''
        Function perpangkatan

        * n = pangkatnya
        * angka = bilangan yang ingin dipangkatkan
    '''
    return lambda angka:angka**n