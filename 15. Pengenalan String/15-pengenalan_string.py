# String pada Python

# A. Cara membuat String
# 1. Assignment string pada variabel
data = "Ini contoh string..."
print(data)

# 2. Menggunakan single quote ('...')/double quote("...")
print('contoh single quote')
print("contoh double quote")
print('Mix antara single quote dengan "double quote"')
print("Mix antara double quote dengan 'single quote'")

# 3. Menggunakan tanda \
#   - Membuat tanda ' menjadi string
print('Sholat Jum\'at ya di Hari Jum\'at dong...')

#   - Backlash
print('c:\\user\\mac')

#   - tab
print("ini\t\tjauh\t\tlooh...")

#   - backspace
print("ini \bdeketan")

#   - newline
print("Baris pertama.\nBaris kedua.") # LF --> line feed --> unix (macOS, linux)
print("Baris pertama.\rBaris kedua.") # CR --> carriage return --> commodore, acorn, lisp (Bahasa pemrograman yang lama-lama)
print("Baris pertama.\r\nBaris kedua.") # CRLF --> line feed, carriage return --> windows

# B. String Literal atau Raw
# Watchout
print("c:\new folder") # Nama directory jadi tidak sesuai..

# Solusi? --> Gunakan Raw String
print(r'c:\new folder')

# Multiline literal string
print("""
    Nama    : Lisa
    Kelas   : 3SD2
""")


# Multiline literal string dan raw
print(r"""
    Nama    : Lisa
    Kelas   : 3SD2\newyork
    Website : www.lisa.com/newID
""")

