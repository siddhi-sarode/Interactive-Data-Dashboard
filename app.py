import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("🛒 Indian E-commerce Dashboard")

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.selectbox("Select State", df['Region'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == region) & (df['Category'] == category)]

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{int(filtered_df['Sales'].sum())}")
col2.metric("Total Profit", f"₹{int(filtered_df['Profit'].sum())}")
col3.metric("Total Orders", filtered_df.shape[0])

# KPI Cards
col1.metric("💰 Total Sales", f"₹{int(filtered_df['Sales'].sum())}")
col2.metric("📈 Total Profit", f"₹{int(filtered_df['Profit'].sum())}")
col3.metric("📦 Total Orders", filtered_df.shape[0])


# 🔥 ADD FROM HERE ↓↓↓

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")

df['Month'] = pd.to_datetime(df['Order Date']).dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

fig3, ax3 = plt.subplots(figsize=(10,5))

monthly_sales.plot(ax=ax3, marker='o', linewidth=2)

ax3.set_title("Monthly Sales Trend")
ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")
ax3.grid(True)

st.pyplot(fig3)
# Top 5 Products
st.subheader("🏆 Top 5 Products")

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig4, ax4 = plt.subplots()
top_products.plot(kind='bar', ax=ax4)
st.pyplot(fig4)


# Correlation Heatmap
st.subheader("🔥 Correlation Heatmap")

fig5, ax5 = plt.subplots()
sns.heatmap(df[['Sales','Profit','Quantity','Discount']].corr(), annot=True, cmap='coolwarm', ax=ax5)
st.pyplot(fig5)

# Chart 1
st.subheader("Sales by Sub-Category")
fig, ax = plt.subplots()
filtered_df.groupby('Sub-Category')['Sales'].sum().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Chart 2
st.subheader("Profit vs Sales")
fig2, ax2 = plt.subplots()
sns.scatterplot(x='Sales', y='Profit', data=filtered_df, ax=ax2)
st.pyplot(fig2)