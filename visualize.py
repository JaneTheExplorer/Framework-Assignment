# visualize.py
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv('cleaned_metadata.csv')

# --- Publications by Year ---
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.show()

# --- Top Journals ---
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_journals.plot(kind='barh')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.show()

# --- Word Cloud of Titles ---
titles = ' '.join(df['title'].dropna())
wc = WordCloud(width=800, height=400, background_color='white').generate(titles)
plt.figure(figsize=(10,6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.show()

# --- Source Distribution ---
plt.figure(figsize=(6,6))
df['source_x'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Papers by Source')
plt.ylabel('')
plt.show()
