


from tkinter import *
import customtkinter as CTk
from CTkTable import *
import sqlite3
import os

class ToplevelWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = CTk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class PasientManagement:
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Aplikasi Manajemen Pasien')
        app.geometry('1350x600')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        title_label = CTk.CTkLabel(
            app,
            text='Pasien Manajemen',  # Add your desired title here
            font=('Helvetica', 26),
            fg_color="transparent",
            corner_radius=8,
            pady=20
        )
        title_label.pack()

        buttonRiwayat = CTk.CTkButton(
            app,
            text='Riwayat Data',
            command=self.read,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonRiwayat.pack(pady=50, padx=50, anchor='nw')
        buttonRiwayat.place(x=50, y=71)

        button_create = CTk.CTkButton(
            app,
            text='Create Data',
            command=self.createTop,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_create.pack(pady=50, padx=50, anchor='nw')
        button_create.place(x=200, y=71)

        buttonUpdate = CTk.CTkButton(
            app,
            text='Update Data',
            command=self.updateTOP,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonUpdate.pack(pady=50, padx=50, anchor='nw')
        buttonUpdate.place(x=350, y=71)

        buttonDelete = CTk.CTkButton(
            app,
            text='Delete Data',
            command=self.deleteTop,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonDelete.pack(pady=50, padx=50, anchor='nw')
        buttonDelete.place(x=500, y=71)


    def updateTOP(self):
        newUpdate = CTk.CTkToplevel(app)
        newUpdate.title("Update Data")
        newUpdate.geometry('550x450')
        title_label = CTk.CTkLabel(
            newUpdate,
            text='Update Data',  # Add your desired title here
            font=('Helvetica', 20),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        title_label.pack()

        self.nik = CTk.CTkEntry(
            newUpdate,
            placeholder_text='NIK Pasien'
        )
        nik_label = CTk.CTkLabel(
            newUpdate,
            text='Nik Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.nama = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Nama Pasien'
        )
        nama_label = CTk.CTkLabel(
            newUpdate,
            text='Nama Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.umur = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Umur Pasien'
        )
        umur_label = CTk.CTkLabel(
            newUpdate,
            text='Umur Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.gender = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Gender Pasien'
        )
        gender_label = CTk.CTkLabel(
            newUpdate,
            text='Gender Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.telp = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Email Pasien'
        )
        telp_label = CTk.CTkLabel(
            newUpdate,
            text='Email Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.sakit = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Penyakit Pasien'
        )
        sakit_label = CTk.CTkLabel(
            newUpdate,
            text='Penyakit Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.ruang = CTk.CTkOptionMenu(
            newUpdate,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Ruang Reguler", "Ruang VIP"]
        )
        ruang_label = CTk.CTkLabel(
            newUpdate,
            text='Ruang Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )                
        self.status = CTk.CTkOptionMenu(
            newUpdate,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Kritis", "Hidup", "Meninggal"]

        )
        status_label = CTk.CTkLabel(
            newUpdate,
            text='Status Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.nik.place(x=50, y=75)
        nik_label.pack()
        nik_label.place(x=10, y=35)
    
        self.nama.place(x=50, y=145)   
        nama_label.pack()
        nama_label.place(x=10, y=105)

        self.umur.place(x=50, y=225)   
        umur_label.pack()
        umur_label.place(x=10, y=185)

        self.gender.place(x=50, y=295)
        gender_label.pack()
        gender_label.place(x=10, y=255)

        self.telp.place(x=375, y=75)
        telp_label.pack()
        telp_label.place(x=335, y=35)

        self.sakit.place(x=375, y=145)
        sakit_label.pack()
        sakit_label.place(x=335, y=105)

        self.ruang.place(x=375, y=225)
        ruang_label.pack()
        ruang_label.place(x=335, y=185)

        self.status.place(x=375, y=295)
        status_label.pack()
        status_label.place(x=335, y=255)
        self.button_create = CTk.CTkButton(
            newUpdate,
            text='Add',
            command=self.update,
            width=100,
            height=50,
            text_color='white',
            hover_color='#205295',
            fg_color='#0A2647',
            corner_radius=15
        )
        self.button_create.pack(pady=10)
        self.button_create.place(x=225, y=350)

    def createTop(self):
        new = CTk.CTkToplevel(app)
        new.title("Tambah Data")
        new.geometry('550x450')
        
        title_label = CTk.CTkLabel(
            new,
            text='Tambah Data',  # Add your desired title here
            font=('Helvetica', 20),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        title_label.pack()
        # title_label.place(x=10,y=10)

        self.nik = CTk.CTkEntry(
            new,
            placeholder_text='NIK Pasien'
        )
        nik_label = CTk.CTkLabel(
            new,
            text='Nik Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.nama = CTk.CTkEntry(
            new,
            placeholder_text='Nama Pasien'
        )
        nama_label = CTk.CTkLabel(
            new,
            text='Nama Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.umur = CTk.CTkEntry(
            new,
            placeholder_text='Umur Pasien'
        )
        umur_label = CTk.CTkLabel(
            new,
            text='Umur Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.gender = CTk.CTkEntry(
            new,
            placeholder_text='Gender Pasien'
        )
        gender_label = CTk.CTkLabel(
            new,
            text='Gender Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.telp = CTk.CTkEntry(
            new,
            placeholder_text='Email Pasien'
        )
        telp_label = CTk.CTkLabel(
            new,
            text='Email Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.sakit = CTk.CTkEntry(
            new,
            placeholder_text='Penyakit Pasien'
        )
        sakit_label = CTk.CTkLabel(
            new,
            text='Penyakit Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.ruang = CTk.CTkOptionMenu(
            new,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Ruang Reguler", "Ruang VIP"]
        )
        ruang_label = CTk.CTkLabel(
            new,
            text='Ruang Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )                
        self.status = CTk.CTkOptionMenu(
            new,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Aktif", "Inaktif", "Meninggal"]

        )
        status_label = CTk.CTkLabel(
            new,
            text='Status Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        # self.nik.pack(pady = 5,padx =10)
        self.nik.place(x=50, y=75)
        nik_label.pack()
        nik_label.place(x=10, y=35)
        
        # self.nama.pack(pady = 5)
        self.nama.place(x=50, y=145)   
        nama_label.pack()
        nama_label.place(x=10, y=105)

        # self.umur.pack(pady = 5)
        self.umur.place(x=50, y=225)   
        umur_label.pack()
        umur_label.place(x=10, y=185)
        # self.gender.pack(pady = 5)
        self.gender.place(x=50, y=295)
        gender_label.pack()
        gender_label.place(x=10, y=255)
        # self.telp.pack(pady = 5)
        self.telp.place(x=375, y=75)
        telp_label.pack()
        telp_label.place(x=335, y=35)
        # self.sakit.pack(pady = 5)
        self.sakit.place(x=375, y=145)
        sakit_label.pack()
        sakit_label.place(x=335, y=105)
        # self.ruang.pack(pady = 5)
        self.ruang.place(x=375, y=225)
        ruang_label.pack()
        ruang_label.place(x=335, y=185)
        # self.status.pack(pady = 5)
        self.status.place(x=375, y=295)
        status_label.pack()
        status_label.place(x=335, y=255)
        self.button_create = CTk.CTkButton(
            new,
            text='Add',
            command=self.create,
            width=100,
            height=50,
            text_color='white',
            hover_color='#205295',
            fg_color='#0A2647',
            corner_radius=15
        )
        self.button_create.pack(pady=10)
        self.button_create.place(x=225, y=350)
    def deleteTop(self):
        newDelete = CTk.CTkToplevel(app)
        newDelete.title("Delete Data")
        newDelete.geometry('190x150')   
        self.id = CTk.CTkEntry(
            newDelete,
            placeholder_text='Masukan ID'
        )
        self.id.pack(pady = 10)

        button_delete = CTk.CTkButton(
            newDelete,
            text='Delete',
            command=self.delete,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_delete.pack(pady=10)
    def create(self):
        self.cursor.execute('''
            INSERT INTO tabel_pasien (nik, nama, umur, gender, telp, sakit, ruang, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get()))
        self.connection.commit()

    def update(self):
        id = int(self.id.get())
        self.cursor.execute("UPDATE tabel_pasien SET nik = ?, nama = ?, umur = ?, gender = ?, telp = ?, sakit = ?, ruang = ?, status = ? WHERE id = ?", 
                            (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get(), id))
        self.connection.commit()

        self.cursor.execute('SELECT * FROM tabel_pasien')
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def read(self):
        self.cursor.execute('SELECT * FROM tabel_pasien LIMIT 0,10')
        data = self.cursor.fetchall()

        # Get column names from the cursor description
        column_names = [description[0] for description in self.cursor.description]

        # Combine column names and data
        values = [column_names] + [list(row) for row in data]

        table = CTkTable(master=self.app, row=len(values), column=len(values[0]), values=values)
        table.place(x=50, y=150)

    def delete(self):
        id = int(self.id.get())
        self.cursor.execute("DELETE FROM tabel_pasien WHERE id = ?", (id,))
        self.connection.commit()

app = CTk.CTk()
PasientManagement(app)
app.mainloop()
