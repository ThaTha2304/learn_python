a = 10
b = 3

# 1. Pertambahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# 2. Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# 3. Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# 4. Pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil)

# 5. Eksponen/Pangkat (**)
hasil = a ** b
print(a, "**", b, "=", hasil)

# 6. Modulus (%)
hasil = a % b
print(a, "%", b, "=", hasil)

# 7. Floor Division --> hasil pembagian dibulatkan kebawah (//)
hasil = a // b
print(a, "//", b, "=", hasil)

# == PRIORITAS OPERASI/OPERATIONAL PRECEDENCE ==
'''
    Urutan Prioritas Operasi:
    1. ()
    2. Eksponen
    3. Perkalian dkk (* / * // %)
    4. Pertambahan dkk (+ -)
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)