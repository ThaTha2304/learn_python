# Operasi String (Methods)

# 1. Mengubah Case pada String
data = "aKu keChEe AbiEzZ"
print("Normal: " + data)

# Lower Case
data = data.lower()
print("Lower: " + data)

# Upper Case
data = data.upper()
print("Upper: " + data)

# 2. Method isX untuk pengecekan
# Cek upper case
cek = "HALLO"
print("Apakah string: '" + cek + "' upper? --> " + str(cek.isupper())) # True

# Cek lower case
cek = "HALLO"
print("Apakah string: '" + cek + "' lower? --> " + str(cek.islower())) # False

# isalpha --> cek alphabetic string (True jika hanya ada karakter alfabet saja)
cek = "HALLO"
print("Apakah string: '" + cek + "' alpha? --> " + str(cek.isalpha())) # True
cek = "HALLO123"
print("Apakah string: '" + cek + "' alpha? --> " + str(cek.isalpha())) # False

# isalnum --> cek string alpha-numeric (True jika hanya ada karakter alfabet dan angka saja)
cek = "Hallo123"
print("Apakah string: '" + cek + "' alnum? --> " + str(cek.isalnum())) # True
cek = "Hallo 123"
print("Apakah string: '" + cek + "' alnum? --> " + str(cek.isalnum())) # False

# isdecimal --> cek string 
cek = "123H"
print("Apakah string: '" + cek + "' decimal? --> " + str(cek.isdecimal())) # False
cek = "12334.0"
print("Apakah string: '" + cek + "' decimal? --> " + str(cek.isdecimal())) # False
cek = "12334"
print("Apakah string: '" + cek + "' decimal? --> " + str(cek.isdecimal())) # True

# isspace --> True jika karakter = whitespace (spasi, newline, tab)
cek = "123 34"
print("Apakah string: '" + cek + "' space? --> " + str(cek.isspace())) # False

cek = " "
print("Apakah string: '" + cek + "' space? --> " + str(cek.isspace())) # True
cek = "\n"
print("Apakah string: '" + cek + "' space? --> " + str(cek.isspace())) # True
cek = "\t"
print("Apakah string: '" + cek + "' space? --> " + str(cek.isspace())) # True

# istitle --> True jika setiap kata pada string huruf kapital
cek = "It Is Okay Not To Be Okay"
print("Apakah string: '" + cek + "' title? --> " + str(cek.istitle())) # True
cek = "It's Okay Not To Be Okay"
print("Apakah string: '" + cek + "' title? --> " + str(cek.istitle())) # False

# 3. Pengecekan --> startswith() dan endswith()
cek = "Hari ini adalah Hari Sabtu"
cek_start = cek.startswith("Hari")
print("String: '" + cek +"' startswith : 'Hari' ==> " + str(cek_start) ) # True
cek_start = cek.startswith("hari")
print("String: '" + cek +"' startswith : 'hari' ==> " + str(cek_start) ) # False (Case sensitive)

cek_end = cek.endswith("Sabtu")
print("String: '" + cek +"' endswith : 'Sabtu' ==> " + str(cek_end) ) # True
cek_end = cek.endswith("sabtu")
print("String: '" + cek +"' endswith : 'sabtu' ==> " + str(cek_end) ) # False (Case sensitive)

# 4. join() dan split()
shop = ['Apple', 'Banana', 'Mango']
print(shop)
gabung = ' '.join(shop)
print(gabung)

shop = "Apple Banana Mango"
pisah = gabung.split()
print(pisah)

# 5. Alokasi Karakter (rjust(), ljust(), center())
kanan = "kanan".rjust(10) # Rata kanan dengan 10 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(10) # rata kiri dengan 10 karakter
print("'" + kiri + "'")

tengah ="tengah".center(10) # rata tengah dengan 10 karakter
print("'" + tengah + "'")

tengah ="tengah".center(10,'-') # rata tengah dengan 10 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")