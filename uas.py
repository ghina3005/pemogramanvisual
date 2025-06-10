import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

DB = "ukt.db"

# Inisiasi database
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pembayaran (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nim TEXT NOT NULL,
            nama TEXT NOT NULL,
            jumlah INTEGER NOT NULL,
            waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Simpan data pembayaran ke DB
def simpan_ke_db(nim, nama, jumlah):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO pembayaran (nim, nama, jumlah) VALUES (?, ?, ?)",
                (nim, nama, jumlah))
    conn.commit()
    conn.close()

# Tampilkan riwayat dari DB ke Treeview
def muat_riwayat():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, nim, nama, jumlah, waktu FROM pembayaran ORDER BY waktu DESC")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

# Fungsi saat tombol Bayar diklik
def bayar_ukt():
    nim = entry_nim.get().strip()
    nama = entry_nama.get().strip()
    jumlah = entry_jumlah.get().strip()

    if not nim or not nama or not jumlah:
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return
    if not jumlah.isdigit():
        messagebox.showwarning("Peringatan", "Jumlah UKT harus berupa angka!")
        return

    jumlah_int = int(jumlah)
    simpan_ke_db(nim, nama, jumlah_int)
    messagebox.showinfo("Pembayaran", f"Pembayaran UKT berhasil!\n\nNIM: {nim}\nNama: {nama}\nJumlah: {jumlah_int}")
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    muat_riwayat()

# Setup GUI
init_db()
root = tk.Tk()
root.title("Pembayaran UKT")
root.geometry("600x500")

frm_input = tk.Frame(root)
frm_input.pack(pady=10)

tk.Label(frm_input, text="NIM:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nim = tk.Entry(frm_input)
entry_nim.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frm_input, text="Nama:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_nama = tk.Entry(frm_input)
entry_nama.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frm_input, text="Jumlah UKT:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_jumlah = tk.Entry(frm_input)
entry_jumlah.grid(row=2, column=1, padx=5, pady=5)

btn_bayar = tk.Button(frm_input, text="Bayar", bg="blue", fg="white", width=15, command=bayar_ukt)
btn_bayar.grid(row=3, column=0, columnspan=2, pady=10)

# Treeview untuk riwayat
cols = ("ID", "NIM", "Nama", "Jumlah", "Waktu")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", stretch=True)
tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

scroll = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Muat riwayat saat startup
muat_riwayat()

root.mainloop()