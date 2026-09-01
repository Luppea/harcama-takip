# Harcama Takip Uygulaması

Flask ve SQLite kullanılarak geliştirilmiş basit bir harcama takip uygulaması. Kullanıcı harcamalarını (miktar, kategori, tarih, açıklama) kaydedebilir, tüm harcamaları listeleyebilir, toplam ve kategoriye göre gruplanmış toplamları görebilir.

## Özellikler

- Harcama ekleme (form üzerinden)
- Tüm harcamaların listelenmesi
- Genel toplam hesaplama
- Kategoriye göre gruplanmış toplamlar

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- HTML / Jinja2

## Kurulum

1. Repoyu klonla:

git clone https://github.com/kullaniciadin/harcama-takip.git
cd harcama-takip

2. Sanal ortam oluştur ve aktif et:
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

3. Gerekli paketleri kur:

pip install flask

4. Uygulamayı çalıştır:

python app.py
