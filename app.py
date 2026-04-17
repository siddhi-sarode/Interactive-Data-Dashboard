import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CUSTOM CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1, h2, h3 {
    color: #2c3e50;
}
.stMetric {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.stSidebar {
    background-color: #eaf2f8;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Dashboard", layout="wide")
st.success("✅ Dashboard loaded successfully")
st.markdown("### 🚀 Interactive E-Commerce Analytics Dashboard")

# Load data
df = pd.read_csv("data/dataset.csv", encoding="latin1")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Title
st.title("🛒 E-Commerce Analytics Dashboard")
st.markdown("### 📊 Clean & Interactive Data Visualization")
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

