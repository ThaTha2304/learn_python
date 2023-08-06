'''
    Module untuk melakukan perkalian yang ada di dalam package matematika
'''

def perkalian (*args):
    '''
        Function untuk melakukan perkalian
    '''
    hasil = 1
    for angka in args:
        hasil *= angka

    return hasil
