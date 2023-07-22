# Width and Multiline

# Data
data_nama = "ThaTha"
data_umur = 21
data_tinggi = 169.5
data_berat = 55.7

# String Standard
format_str = f"Nama: {data_nama}, Umur: {data_umur}, Tinggi: {data_tinggi}, Berat: {data_berat}"
print("\n== Data String ==")
print(format_str)

# String multiline (enter, newline, \n)
format_str = f"Nama: {data_nama}, \nUmur: {data_umur}, \nTinggi: {data_tinggi}, \nBerat: {data_berat}"
print("\n== Data String ==")
print(format_str)

# String multiline (kutip triple)
format_str = f"""
Nama: {data_nama}
Umur: {data_umur}
Tinggi: {data_tinggi}
Berat: {data_berat}
"""
print("\n== Data String ==")
print(format_str)

# Mengatur lebar (width)
format_str = f"""
Nama   : {data_nama}
Umur   : {data_umur:>6}
Tinggi : {data_tinggi:>6}
Berat  : {data_berat:>6}
"""
# Semuanya diatur agar tampil dengan geser kekanan 6 karakter
print(format_str)