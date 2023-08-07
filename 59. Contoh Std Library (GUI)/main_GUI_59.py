'''
    Module yang berisi implementasi salah satu standard library di python: tkinter

    tkinter digunakan untuk membuat GUI di Python
'''

# Package yang digunakan
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Initialisasi window
window = tk.Tk() # buat objek dengan nama "window"
window.configure(bg="lightgrey") # atur warna background
window.geometry("300x200") # atur size window
window.resizable(False,False) # atur apakah window pada sumbu x dan y bisa di atur sizenya ato ndk
window.title("Sapa Dia!") # atur judul windownya

# Variabel dan Function
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''
        Function akan dijalankan ketika tombol di klik
    '''
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}!"
    showinfo(title="Whaddup!", message=pesan)

# Frame Input
input_frame = ttk.Frame(window)
# Penempatan komponen-komponen GUI ada banyak: 1) Grid, 2) Pack, 3) Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen
## 1. Label Nama Depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

## 2. Entry Nama Depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

## 3. Label Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

## 4. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

## 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol_sapa.pack(padx=10, pady=10, fill="x", expand=True)

# Main Loop Window
window.mainloop()