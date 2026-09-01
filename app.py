from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")

def index():

    conn =  sqlite3.connect('harcamalar.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM harcamalar")
    sonuclar = cursor.fetchall()
    cursor.execute("SELECT SUM(miktar) FROM harcamalar")
    toplam = cursor.fetchone()[0]
    cursor.execute("SELECT kategori, SUM(miktar) FROM harcamalar GROUP BY kategori")
    kategori_toplamlari = cursor.fetchall()

    conn.close()

    return render_template('index.html',
                            harcamalar = sonuclar,
                            toplam=toplam ,
                            kategori_toplamlari=kategori_toplamlari) 


@app.route("/ekle", methods = ["POST"])

def ekle():
    miktar = request.form["miktar"]
    kategori = request.form["kategori"]
    tarih = request.form["tarih"]
    aciklama = request.form["aciklama"]

    conn = sqlite3.connect("harcamalar.db")
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO harcamalar (miktar, kategori, tarih, aciklama)
            VALUES (?, ?, ?, ?)
            """, (miktar, kategori, tarih, aciklama))

    conn.commit()
    conn.close()

    return "Veri başarıyla kaydedildi."


if __name__ == "__main__":
    app.run(debug=True)