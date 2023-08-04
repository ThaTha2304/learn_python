'''
    Lambda dan Anonymous Function
'''

# 1. Lambda Function
# 1.a. Misal kita punya function untuk menambah dua bilangan
def tambah (a,b):
    '''
        Fungsi untuk menambah dua bilangan (a,b)
    '''
    return a+b

print(tambah(1,3))

# Function tersebut bisa disingkat menjadi:
hasil = lambda a,b: a+b
print(f"Hasil tambah {hasil(1,3)}")

# 1.b. FUnction perpangkatan
def pangkat_2(angka):
    '''
        FUnction kuadrat
    '''
    return angka**2
print(pangkat_2(5))

# Function terebut dalam lambda:
kuadrat = lambda angka: angka**2
print(kuadrat(9))

# 1.c. Filter angka dalam list
data_list = list(range(0,30))
print(f"data_list ori: {data_list}")

## Filter data list menggunakan lambda function (filter data<15)
data_list_filter = list(filter(lambda data:data<15, data_list))
print(f"Data list<15 apa aja? --> {data_list_filter}")

## Filter data yg genap
data_list_filter = list(filter(lambda data:(data%2==0), data_list))
print(f"Data list genap apa aja? --> {data_list_filter}")

## Filter data yg ganjil
data_list_filter = list(filter(lambda data:(data%2==1), data_list))
print(f"Data list ganjil apa aja? --> {data_list_filter}")

# 2. Anonymous Function
## Misal kita ingin menghitung nilai pangkat dari suatu angka tertentu, dengan nilai pangkat dan angka sesuai yg kita masukkan (dinamis)

def pangkat(x):
    '''
        Function menghitung pangkat suatu nilai, dengan menerapkan lambda function
    '''
    return lambda angka: angka**x

# Bikin variabel yg isinya function pangkat, dengan mengirim argumen x=2
pangkat2 = pangkat(2) # --> di function "pangkat", ganti nilai "x" dengan nilai 2
# Akses function pangkat2 dengan argumen nilai=11
print(f"Nilai 11^2 = {pangkat2(angka=11)}") # --> di function "pangkat", ganti nilai "angka" dengan nilai 11

pangkat3 = pangkat(3)
print(f"Nilai 10^3 = {pangkat3(10)}")
