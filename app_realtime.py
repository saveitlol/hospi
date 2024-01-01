import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
import sqlite3
import customtkinter


def read():
    cursor.execute("SELECT * FROM tabel_pasien")
    rows = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for row in rows:
        tree.insert("", "end", iid=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    root.after(1000, read)

root = tk.Tk()
style =ttk.Style()

root.title("Realtime")
root.geometry('900x400')
# label = customtkinter.CTkLabel(root, text="HALO", fg_color="black")
tree = tb.Treeview(root, columns=("Col1", "Col2", "Col3", "Col4",
                                   "Col5", "Col6", "Col7", "Col8"))
style.configure("tree",
                background="silver",
                foreground="black"
                )
tree.column("#0",width=1)

tree.heading("Col1", text="Nik")
tree.column("Col1",width=50)
tree.heading("Col2", text="Nama")
tree.column("Col2",width=50)
tree.heading("Col3", text="Umur")
tree.column("Col3",width=50)
tree.heading("Col4", text="Gender")
tree.column("Col4",width=50)
tree.heading("Col5", text="Telp")
tree.column("Col5",width=50)
tree.heading("Col6", text="Sakit")
tree.column("Col6",width=50)
tree.heading("Col7", text="Ruang")
tree.column("Col7",width=50)
tree.heading("Col8", text="Status")
tree.column("Col8",width=50)
tree.pack(fill='both',expand=True)
# tree.place(x=50,y=10)
# tree.style(background="silver",foreground="black")
connection = sqlite3.connect("pasien.db")
cursor = connection.cursor()

read()

root.mainloop()