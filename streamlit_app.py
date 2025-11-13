import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers metadata")

# --- Load cleaned data ---
df = pd.read_csv('cleaned_metadata.csv')

# --- Interactive Year Range ---
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered_df = df[df['year'].between(year_range[0], year_range[1])]

# --- Sample Data ---
st.subheader("Sample Data")
st.write(filtered_df.head())

# --- Publications by Year ---
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_title("Publications by Year")
st.pyplot(fig1)

# --- Top Journals ---
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals.plot(kind='barh', ax=ax2)
ax2.set_title("Top 10 Journals")
st.pyplot(fig2)

# --- Word Cloud of Titles ---
st.subheader("Word Cloud of Titles")
titles = ' '.join(filtered_df['title'].dropna().astype(str))
wc = WordCloud(width=800, height=400, background_color='white').generate(titles)
fig3, ax3 = plt.subplots()
ax3.imshow(wc, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# --- Source Distribution ---
st.subheader("Source Distribution")
fig4, ax4 = plt.subplots()
filtered_df['source_x'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax4)
ax4.set_ylabel('')
ax4.set_title("Distribution of Papers by Source")
st.pyplot(fig4)
