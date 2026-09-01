import sqlite3

conn = sqlite3.connect('harcamalar.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE harcamalar ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    miktar REAL,
    kategori TEXT,
    tarih TEXT,
    aciklama TEXT
)
""")

conn.commit()

conn.close()