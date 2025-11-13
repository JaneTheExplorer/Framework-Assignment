# Part 1: 
import pandas as pd

df = pd.read_csv('metadata.csv', low_memory=False)
print(df.shape)
print(df.info())
print(df.isnull().sum())

# --- Part 2: Clean and Prepare ---
df_clean = df.dropna(subset=['title', 'abstract', 'publish_time'])
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['year'] = df_clean['publish_time'].dt.year
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))

# Save cleaned data
df_clean.to_csv('cleaned_metadata.csv', index=False)
