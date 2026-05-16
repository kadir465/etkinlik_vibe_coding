import pandas as pd
import os

# Proje kök dizinini belirleme
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Dosya yolları
input_file = os.path.join(BASE_DIR, "data", "raw", "Dataset_V6_Master_Balanced.parquet")
output_file = os.path.join(BASE_DIR, "data", "raw", "Dataset_V6_Master_Balanced_Filtered.csv")

print("Tüm genom taranıyor... Lütfen bekleyin.")

# Parquet dosyasını okuyoruz
df = pd.read_parquet(input_file)

df.to_csv(output_file, index=False)
print(f"\nToplam {len(df)} varyant kaydedildi.")