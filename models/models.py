import sqlite3

connection = sqlite3.connect('pasien.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tabel_pasien (
    id INTEGER PRIMARY KEY,
    nik INTEGER,
    nama VARCHAR(255),
    umur VARCHAR(255),
    gender VARCHAR(255),
    telp VARCHAR(255),
    sakit VARCHAR(255),
    ruang VARCHAR(255),
    status VARCHAR(255)
);
''')
connection.commit()
connection.close()