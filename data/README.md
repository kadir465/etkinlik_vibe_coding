# Data Directory

Bu klasör, Teknofest Sağlıkta Yapay Zeka Genomik Varyant Patojenite Tahmini projesinde kullanılan veri setlerini barındırır. Modellerin performansı, verinin işlenme ve ölçeklenme kalitesine doğrudan bağlıdır.

## Klasör Yapısı

- **`raw/`**: İşlenmemiş, ham haldeki biyoinformatik veri setlerini tutar. Genellikle çok yüksek boyutlu olup `.parquet` ve dev `.csv` formatındadır. İçerisindeki verilerde eksik değerler, ölçeklenmemiş özellikler ve gereksiz sütunlar bulunabilir.
- **`processed/`**: Eğitim, doğrulama ve test aşamaları için temizlenmiş, normalize edilmiş, eksik değerleri doldurulmuş ve ML algoritmalarına hazır haldeki verileri tutar (`train_dataset.csv`, `valid_dataset.csv`, `test_dataset.csv`).

## Temel Biyoinformatik Özellikler (Features)

Veri setlerinde yer alan temel genomik annotasyon skorları aşağıdadır:

- **ESM1b Score:** Evrimsel Ölçekli Modelleme. Bir varyantın protein diziliminde oluşturduğu etkiyi tahmin eden dil modeli tabanlı skordur.
- **DANN Score:** Derin Sinir Ağı tabanlı bir varyant zararlılık skoru (0 ile 1 arası). 1'e yaklaştıkça patojenite ihtimali artar.
- **GERP++ / phyloP / phastCons:** Farklı türler arası evrimsel korunmuşluğu (conservation) gösteren skorlardır. Yüksek korunmuşluk, varyantın kritik bir bölgede olduğunu gösterir.
- **gnomAD / POPMAX AF:** Alel frekansı değerleri. Popülasyonda çok sık görülen varyantlar genellikle hastalık yapıcı (pathogenic) değildir.

## Uyarı
Ham `.parquet` verileri çok büyük olabildiği için Git takip listesinden (`.gitignore` üzerinden) çıkarılmıştır. Eğer veri setini sıfırdan indirecekseniz veya çıkaracaksanız `src/data/extract_data.py` betiğini kullanabilirsiniz.
