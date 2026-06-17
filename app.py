import os
import math
import socket
import certifi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB Bağlantısı
mongo_client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
db = mongo_client['EticaretDB']
collection = db['urunler']

app = FastAPI()

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "IP Bulunamadi"

@app.get("/", response_class=HTMLResponse)
def ana_sayfa():
    # Eğer veritabanı boşsa şık ürünler ekle
    if collection.count_documents({}) == 0:
        collection.insert_many([
            {"ad": "MacBook Air M3", "fiyat": 45000, "resim": "💻"},
            {"ad": "iPhone 15 Pro", "fiyat": 70000, "resim": "📱"},
            {"ad": "AirPods Pro", "fiyat": 9000, "resim": "🎧"},
            {"ad": "Apple Watch", "fiyat": 15000, "resim": "⌚"}
        ])
    
    # Ürünleri veritabanından çek
    urunler = list(collection.find({}, {"_id": 0}))
    sunucu_ip = get_ip()

    # Modern görünümlü HTML Arayüzü
    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Bulut E-Ticaret</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; text-align: center; padding: 20px; }}
            .header {{ background-color: #2c3e50; color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }}
            .server-info {{ background-color: #e74c3c; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold; display: inline-block; margin-top: 10px; font-size: 18px; }}
            .products {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }}
            .card {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 200px; transition: 0.3s; }}
            .card:hover {{ transform: scale(1.05); }}
            .card h1 {{ font-size: 50px; margin: 0; }}
            .card h3 {{ margin: 15px 0 5px 0; color: #2980b9; }}
            .btn {{ background-color: #27ae60; color: white; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold; }}
            .btn:hover {{ background-color: #2ecc71; }}
            .stress-btn {{ background-color: #c0392b; margin-top: 50px; padding: 15px 30px; font-size: 18px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }}
            .stress-btn:hover {{ background-color: #e74c3c; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 style="margin: 0;">🚀 Bulut Ölçeklenebilir E-Ticaret Platformu</h1>
            <div class="server-info">Aktif Sunucu IP: {sunucu_ip}</div>
        </div>
        
        <div class="products">
    """
    
    # Kartları dinamik olarak oluştur
    for urun in urunler:
        html_content += f"""
            <div class="card">
                <h1>{urun.get('resim', '📦')}</h1>
                <h3>{urun['ad']}</h3>
                <p><strong>{urun['fiyat']} TL</strong></p>
                <button class="btn">Sepete Ekle</button>
            </div>
        """

    # En alta meşhur Stres Testi butonunu koyalım
    html_content += """
        </div>
        <button class="btn stress-btn" onclick="fetch('/stress').then(a=>alert('🔥 İşlemci %100 Yüke Çıktı! AWS Auto Scaling birazdan yeni sunucu açacak...'))">
            ⚠️ AWS Auto Scaling Stres Testini Başlat
        </button>
    </body>
    </html>
    """
    return html_content

@app.get("/stress")
def cpu_stress_testi():
    # İşlemciyi (CPU) %100'e kilitleyen sahte trafik döngüsü
    x = 0.0001
    for i in range(25000000):
        x += math.sqrt(x)
    return {"mesaj": "Stres testi bitti"}