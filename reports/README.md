# Reports & Figures Directory

Bu klasör, eğitilen Stacking Ensemble mimarisinin, algoritmaların teker teker ve birlikte gösterdikleri başarı test sonuçlarını görselleştiren materyalleri içerir. Raporlama ve sunumlar (Teknofest jüri sunumu vb.) için üretilen dosyalar burada saklanır.

## Grafikler ve Anlamları

- **`teknofest_roc_curve.png`**: (Receiver Operating Characteristic) modellerin zararlı (`Pathogenic`) ile zararsız (`Benign`) varyantları birbirinden ayırma gücünü gösterir. Eğri sol üst köşeye ne kadar yakınsa model o kadar başarılıdır.
- **`teknofest_model_accuracy_comparison.png` & `teknofest_final_performans_tablosu.png`**: Tüm algoritmaların Accuracy (Doğruluk), Precision (Kesinlik), Recall (Duyarlılık) ve F1-Score bağlamında karşılaştırıldığı bar/tablo grafikleri. Meta-modelin başarısı bu tablolarda kıyaslanabilir.
- **`teknofest_feature_importance.png` & `teknofest_all_models_importance.png`**: XGBoost ve LightGBM gibi modellerin tahmin yaparken biyoinformatik özelliklerden (ESM1b, DANN, gnomAD AF vs.) hangisine ne kadar ağırlık/önem verdiğini gösteren analizlerdir.
- **`teknofest_consensus_importance.png`**: Nihai Meta-Modelin (Konsensüs) alt modellere (Örn: GNN %20, XGB %40, vb.) ne kadar ağırlık verdiğini oranlar. 
- **`teknofest_grouped_importance.png`**: Özelliklerin gruplanmış haldeki önem derecelerini sunar (Örn: "Evrimsel Skorlar", "Derin Öğrenme Skorları", "Alel Frekansları").

Bu grafikler, modelin neye göre karar verdiğini açıklanabilir kılmak (Explainable AI - XAI) ve tıp uzmanlarına güven vermek için kritik öneme sahiptir.
