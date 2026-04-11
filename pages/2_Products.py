import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📦 Product Insights")

# ✅ LOAD DATA FIRST
df = pd.read_csv("data/dataset.csv", encoding="latin1")

# ✅ SIDEBAR FILTERS
st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", df['State'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

# Apply filter
df = df[(df['State'] == state) & (df['Category'] == category)]

# Show selection
st.write(f"Selected State: {state} | Category: {category}")

# Top products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig, ax = plt.subplots()
top_products.plot(kind='bar', ax=ax, color='green')

ax.set_title("Top 5 Products")

st.pyplot(fig)

# Show table
st.dataframe(top_products)