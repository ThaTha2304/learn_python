'''
    Module pertambahan yang ada di package matematika
'''

def pertambahan(*args):
    '''
        Function untuk melakukan pertambahan
    '''
    hasil = 0
    for angka in args:
        hasil += angka

    return hasil