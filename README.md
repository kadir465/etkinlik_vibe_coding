# 🧬 Teknofest Sağlıkta Yapay Zeka - Genomik Varyant Patojenite Tahmini

Bu klasör, Teknofest Sağlıkta Yapay Zeka yarışması kapsamında geliştirilen, genomik varyantların patojenite (zararlılık) durumunu tahmin eden gelişmiş makine öğrenmesi modellerini ve veri setlerini içermektedir.

## 🚀 Proje Genel Bakış

Proje, çeşitli genomik annotasyon skorlarını (ESM1b, DANN, GERP, phyloP vb.) girdi olarak alarak bir varyantın hastalık yapıcı (`Pathogenic`) veya zararsız (`Benign`) olup olmadığını en yüksek doğrulukla tahmin etmeyi amaçlar. 

Sistem, tek bir model yerine **Stacking Ensemble** (Yığınlama) mimarisi kullanarak farklı algoritmaların güçlü yanlarını birleştirir:
- **Gradient Boosting Modelleri:** XGBoost ve LightGBM (Tabüler veride yüksek performans)
- **Derin Öğrenme Modelleri:** FT-Transformer (Tabüler veri için özel Transformer) ve GNN (Varyantlar arası benzerlik ilişkilerini kuran Graf Sinir Ağları)
- **Meta-Model:** Logistic Regression (Tüm modellerin çıktılarını ağırlıklandırarak son kararı veren başhekim/karar verici)

---

## 📁 Klasör Yapısı

```bash
data2_model_test/
├── 📊 data/             # Eğitim, doğrulama ve test verileri (.csv)
│   ├── train_dataset.csv
│   ├── valid_dataset.csv
│   └── test_dataset.csv
├── 🤖 model/            # Eğitilmiş model dosyaları (.pkl, .pth) ve ölçekleyiciler
│   ├── model_xgb.pkl, model_lgbm.pkl, model_adaboost.pkl
│   ├── model_gnn.pth, model_ftt.pth
│   └── *_scaler.pkl
├── 🖼️ picture/          # Model performans grafikleri ve analiz görselleştirmeleri
│   ├── teknofest_roc_curve.png
│   ├── teknofest_feature_importance.png
│   └── teknofest_final_performans_tablosu.png
└── 📝 process.ipynb     # Veri ön işleme, eğitim ve analiz süreçlerini içeren ana notebook
```

---

## 📊 Modeller ve Özellikler

| Model Grubu | Algoritmalar | Kullanım Amacı |
| :--- | :--- | :--- |
| **Boosting** | XGBoost, LightGBM, AdaBoost | Yapısal verideki karmaşık ilişkileri yakalamak |
| **Deep Learning** | FT-Transformer | Özellikler arasındaki dikkat (attention) mekanizmasını kullanmak |
| **Graph-based** | GNN (GAT) | Komşu varyantlar arasındaki benzerliği graf yapısı ile modellemek |
| **Ensemble** | Logistic Regression | Diğer modellerin tahminlerini birleştirerek "Konsensüs" kararı vermek |

---

## 🛠️ Temel Özellikler (Features)

Model eğitiminde kullanılan bazı kritik biyoinformatik skorlar:
- **ESM1b Score:** Protein dizilerinden elde edilen evrimsel bilgi.
- **DANN Score:** Derin öğrenme tabanlı varyant skorlama.
- **GERP++ / phyloP / phastCons:** Türler arası korunmuşluk (conservation) skorları.
- **gnomAD / POPMAX AF:** Alel frekansı verileri (popülasyondaki görülme sıklığı).

---

## 📈 Performans Analizi

Modellerin başarısı `picture/` klasörü altındaki görselleştirmelerle detaylandırılmıştır:
1. **ROC Eğrisi:** Modellerin ayırt edicilik gücünü gösterir.
2. **Feature Importance:** Tahmin yapılırken hangi özelliklerin (ESM1b, DANN vb.) daha etkili olduğunu açıklar.
3. **Performans Tablosu:** Accuracy, Precision, Recall ve F1-skor karşılaştırmalarını içerir.

---

## ⚙️ Nasıl Kullanılır?

1. **Bağımlılıklar:** `pandas`, `xgboost`, `lightgbm`, `torch`, `torch_geometric`, `joblib`, `sklearn` kütüphanelerinin yüklü olduğundan emin olun.
2. **Tahmin:** `model/` klasöründeki eğitilmiş modelleri yükleyerek yeni varyant verileri üzerinde patojenite tahmini yapabilirsiniz.
3. **Süreç:** Tüm akışı (veri bölmeden final testine kadar) `process.ipynb` dosyasından takip edebilirsiniz.

---
*Bu çalışma Teknofest Gençlik Projeleri kapsamında hazırlanmıştır.* 💡
