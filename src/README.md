# Source (src) Directory

Bu klasör, projenin üretim (production) ve modülerleşme aşamasındaki Python kaynak kodlarını içerir. Notebook'larda geliştirilen kodlar, burada daha sürdürülebilir, modüler ve tekrarlanabilir Python paketlerine (`.py`) dönüştürülür.

## Paket Yapısı

- **`data/`**: Veri çekme, veritabanı bağlantıları, veri temizleme ve raw veriyi formatlama betiklerini içerir.
  - `extract_data.py`: `.parquet` formatındaki devasa boyutlu ham varyant veri tabanını işleyerek `.csv` formatında (veya filtrelenmiş şekilde) model eğitimine hazır hale getiren temel fonksiyondur. Dinamik yol algoritması ile çalışır (bilgisayardan bağımsız).
- **`models/`**: (Planlanan) Notebook'ta bulunan derin öğrenme (GNN, FT-Transformer) ve makine öğrenmesi mimarilerinin sınıflar (classes) ve fonksiyonlar halinde tutulacağı alandır. Eğitim (train) ve tahmin (inference) scriptleri ileride buraya eklenecektir.

Bu yapı, "Spaghetti" koda dönüşmüş Notebook mantığından sıyrılarak Yazılım Mühendisliği pratiklerini (DRY - Don't Repeat Yourself, SOLID vs.) sağlıkta yapay zeka alanına entegre etmeyi sağlar.
