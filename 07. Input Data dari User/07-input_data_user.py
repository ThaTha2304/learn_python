# Mengambil data dari yang di-input-kan user
# Untuk mengambil input dari user, gunakan syntax ==> input(<teks yang akan ditampilkan di terminal>)

# Secara default, semua yang dimasukkan user bertipe string, meskipun user memasukkan integer, float, boolean
data_str = input("Masukkan teks: ")
print("data :", data_str, "==> tipe:", type(data_str))

# Jika kita ingin mengambil angka (integer/float), kita casting dulu
## Casting ke integer
angka = int(input("Masukkan angka bulat: "))
print("data :", angka, "==> tipe:", type(angka))

## Casting ke float
angka = float(input("Masukkan angka desimal: "))
print("data :", angka, "==> tipe:", type(angka))

# Kalo boolean, kita bisa memanfaatkan nilai biner (0 = False, 1 = True)
biner = bool(int(input("Masukkan angka biner (0/1): ")))
print("data :", biner, "==> tipe:", type(biner))