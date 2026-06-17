# 🚀 Bulut Ölçeklenebilir E-Ticaret Platformu

Bu proje, bulut bilişim prensiplerini (Cloud Computing), yük dağılımını (Load Balancing) ve otomatik ölçeklendirmeyi (Auto Scaling) demonstrate eden bir e-ticaret uygulamasıdır.

## 🛠️ Kullanılan Teknolojiler
- **Backend:** Python (FastAPI)
- **Veritabanı:** MongoDB Atlas
- **Altyapı:** AWS (EC2, Auto Scaling, Application Load Balancer)
- **Dağıtım:** Git & GitHub

## 🏗️ Mimari Özellikler
* **Yüksek Erişilebilirlik (High Availability):** Trafik, Application Load Balancer aracılığıyla birden fazla sunucuya (AZ) dağıtılmaktadır.
* **Otomatik Ölçeklendirme:** CPU kullanımı %50'yi aştığında, Auto Scaling grubu AWS'de otomatik olarak yeni EC2 instance'ları başlatır.
* **İzlenebilirlik:** Sunucular her istekte kendi IP adreslerini döndürerek yük dağılımını görsel olarak kanıtlar.

## 🧪 Stres Testi
Sistem, `/stress` endpoint'i üzerinden manuel olarak işlemci yükünü %100'e çıkaracak şekilde tetiklenebilir. Bu tetikleme sonucunda AWS Auto Scaling mimarisi devreye girerek yeni sunucu örnekleri oluşturur.

## 💻 Kurulum
1. `git clone https://github.com/canozduzen/proje4-eticaret.git`
2. `.env` dosyasını yapılandırın.
3. Servisi `systemctl` ile başlatın.