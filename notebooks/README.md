# Notebooks Directory

Bu klasör, araştırmacıların ve veri bilimcilerin modelleme süreçlerini adım adım görmesi, test etmesi ve veri ile etkileşime girmesi için oluşturulmuş interaktif Jupyter Notebook (`.ipynb`) dosyalarını barındırır.

## Dosyalar

- **`01_data_process_and_modeling.ipynb`**: Tüm sürecin kalbi olan ana çalışma dosyasıdır. İçerisinde sırasıyla şu işlemler gerçekleştirilir:
  1. **Keşifsel Veri Analizi (EDA):** Veri setinin yüklenmesi, istatistiklerinin çıkarılması, korelasyonların incelenmesi.
  2. **Veri Ön İşleme:** Eksik değerlerin (Missing Values) doldurulması, dengesiz sınıf (Class Imbalance) problemlerinin çözümü, eğitim-doğrulama-test setlerinin bölünmesi (`../data/` klasörüne kayıt) ve StandardScaler ile ölçeklendirme.
  3. **Model Eğitimi:** XGBoost, LightGBM, AdaBoost, FT-Transformer ve GNN modellerinin ayrı ayrı eğitilmesi ve hiperparametre optimizasyonu (`../models/` klasörüne kayıt).
  4. **Ensemble & Meta-Model:** Logistic Regression kullanılarak tüm modellerin çıktılarının birleştirilmesi (Konsensüs tahmini).
  5. **Değerlendirme (Evaluation):** F1-Score, Accuracy, ROC Curve hesaplamaları ve özellik önem (Feature Importance) analizlerinin çıkartılması (`../reports/figures/` klasörüne kayıt).

## Kullanım
Jupyter arayüzünü veya VS Code'u kullanarak notebook'ları çalıştırabilirsiniz.
Hücreler yukarıdan aşağıya doğru sırasıyla çalıştırılacak şekilde tasarlanmıştır.

```bash
jupyter notebook notebooks/01_data_process_and_modeling.ipynb
```
