import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")
st.markdown("### 🚀 Interactive E-Commerce Analytics Dashboard")

# Load data
df = pd.read_csv("data/dataset.csv", encoding="latin1")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Title
st.title("🏠 E-Commerce Dashboard")

st.write("📊 Overview of Sales Data")

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"₹{int(total_sales)}")
col2.metric("📈 Total Profit", f"₹{int(total_profit)}")
col3.metric("📦 Total Orders", total_orders)

# Monthly trend
# -------------------- INSIGHTS --------------------

st.subheader("📌 Key Insights")

top_state = df.groupby('State')['Sales'].sum().idxmax()
top_category = df.groupby('Category')['Sales'].sum().idxmax()
top_product = df.groupby('Product Name')['Sales'].sum().idxmax()

col1, col2, col3 = st.columns(3)

col1.info(f"🏆 Top State: {top_state}")
col2.info(f"🛒 Top Category: {top_category}")
col3.info(f"⭐ Best Product: {top_product}")

# -------------------- APP GUIDE --------------------

st.subheader("🧭 How to Use This Dashboard")

st.markdown("""
- 📊 **Sales Page** → Detailed sales trends & filters  
- 📦 **Products Page** → Product performance analysis  
- 🎯 Use filters to explore data dynamically  

👉 Navigate using sidebar
""")

# -------------------- FOOTER --------------------

st.success("🚀 Built using Streamlit | Data Analysis Project")

