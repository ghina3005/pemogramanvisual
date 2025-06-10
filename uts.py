import tkinter as tk
from tkinter import messagebox

def bayar_ukt():
    nim = entry_nim.get()
    nama = entry_nama.get()
    jumlah = entry_jumlah.get()

    if nim and nama and jumlah:
        messagebox.showinfo("Pembayaran", f"Pembayaran UKT berhasil!\n\nNIM: {nim}\nNama: {nama}\nJumlah: {jumlah}")
    else:
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")

# Membuat jendela utama
root = tk.Tk()
root.title("Pembayaran UKT")
root.geometry("300x250")

# Label dan Entry untuk NIM
label_nim = tk.Label(root, text="NIM:")
label_nim.pack(pady=5)
entry_nim = tk.Entry(root)
entry_nim.pack()

# Label dan Entry untuk Nama
label_nama = tk.Label(root, text="Nama:")
label_nama.pack(pady=5)
entry_nama = tk.Entry(root)
entry_nama.pack()

# Label dan Entry untuk Jumlah UKT
label_jumlah = tk.Label(root, text="Jumlah UKT:")
label_jumlah.pack(pady=5)
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol Bayar
tombol_bayar = tk.Button(root, text="Bayar", bg="blue", fg="white", command=bayar_ukt)
tombol_bayar.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()