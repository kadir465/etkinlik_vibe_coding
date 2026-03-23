# 🤖 Eğitilmiş Modeller (Trained Models)

Bu klasör, genomik varyant patojenite tahmini için eğitilmiş tüm makine öğrenmesi ve derin öğrenme modellerini içermektedir.

## 📦 Model Dosyaları

| Dosya Adı | Algoritma | Dosya Tipi | Açıklama |
| :--- | :--- | :--- | :--- |
| **model_xgb.pkl** | XGBoost | Joblib / Pickle | Gradyan artırma tabanlı ana model. |
| **model_lgbm.pkl** | LightGBM | Joblib / Pickle | Yüksek performanslı hafif model. |
| **model_adaboost.pkl**| AdaBoost | Joblib / Pickle | Dengelenmiş AdaBoost modeli. |
| **model_gnn.pth** | GNN (GAT) | PyTorch (.pth) | Graf Yapısı üzerinde eğitilmiş derin öğrenme modeli. |
| **model_ftt.pth** | FT-Transformer| PyTorch (.pth) | Tabüler veri için transformer mimarisi. |
| **meta_model_logistic.pkl** | Log. Reg. | Joblib / Pickle | **Stacking** aşamasında diğer modellerin kararlarını birleştiren meta-model. |

## 📐 Ön İşleme Ölçekleyicileri (Scalers)

Derin öğrenme modelleri (GNN ve FT-Transformer) için kullanılan verileri standardize etmek amacıyla kaydedilmiş `StandardScaler` dosyaları:
- `gnn_scaler.pkl`
- `ftt_scaler.pkl`

## 🧩 Modellerin Yüklenmesi

Modelleri yüklemek için ilgili kütüphaneleri (`joblib` veya `torch`) kullanabilirsiniz:

### Python (Joblib Örneği):
```python
import joblib
xgb_model = joblib.load('model/model_xgb.pkl')
```

### PyTorch (pth Örneği):
```python
import torch
# Model sınıfı tanımlandıktan sonra ağırlıklar yüklenebilir
model_gnn.load_state_dict(torch.load('model/model_gnn.pth'))
```
