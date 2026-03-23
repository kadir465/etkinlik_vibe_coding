import pandas as pd

# Dosya uzantısı .parquet
file_path = r"C:\Users\kadir\OneDrive\Masaüstü\teknofest_saglıkt_YZ\pull_the_dataset\new_set\mdoel_test\data2_model_test\Dataset_V6_Master_Balanced.parquet" 
print("Tüm genom taranıyor... Lütfen bekleyin.")

# Parquet dosyasını tüm sütunlarıyla okuyoruz
df = pd.read_parquet(file_path)


df.to_csv("Dataset_V6_Master_Balanced_Filtered.csv", index=False)
print(f"\nToplam {len(df)} varyant kaydedildi.")