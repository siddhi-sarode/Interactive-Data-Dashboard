import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Analysis")

# ✅ LOAD DATA FIRST (IMPORTANT)
df = pd.read_csv("data/dataset.csv", encoding="latin1")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ✅ SIDEBAR FILTERS
st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", df['State'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

# Apply filter
df = df[(df['State'] == state) & (df['Category'] == category)]

# Show selection
st.write(f"Selected State: {state} | Category: {category}")

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df.shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"₹{int(total_sales)}")
col2.metric("Total Profit", f"₹{int(total_profit)}")
col3.metric("Total Orders", total_orders)

# Monthly sales chart
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

fig, ax = plt.subplots()
monthly_sales.plot(ax=ax, color='orange')
ax.set_title("Monthly Sales Trend")

st.pyplot(fig)