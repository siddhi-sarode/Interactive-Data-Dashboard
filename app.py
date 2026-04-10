import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("🛒 Indian E-commerce Dashboard")
st.markdown("### 📊 Data Analysis & Insights")

# -------------------- LOAD DATA --------------------
df = pd.read_csv("data/cleaned_data.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# -------------------- SIDEBAR --------------------
st.sidebar.title("🔍 Filters")

state = st.sidebar.selectbox("Select State", df['Region'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == state) & (df['Category'] == category)]

# -------------------- KPI --------------------
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
col3.metric("📦 Total Orders", total_orders)

st.markdown("---")

# -------------------- MONTHLY SALES --------------------
monthly_sales = filtered_df.groupby(
    filtered_df['Order Date'].dt.to_period('M')
)['Sales'].sum()

monthly_sales.index = monthly_sales.index.astype(str)

fig1, ax1 = plt.subplots()
monthly_sales.plot(ax=ax1, color='orange', marker='o', linewidth=2)

ax1.set_title("Monthly Sales Trend", fontsize=14, fontweight='bold')
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax1.grid(True, linestyle='--', alpha=0.5)

# -------------------- TOP PRODUCTS --------------------
top_products = filtered_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig2, ax2 = plt.subplots()
top_products.plot(kind='bar', ax=ax2, color='green')

ax2.set_title("Top 5 Products", fontsize=14, fontweight='bold')
ax2.set_ylabel("Sales")

# -------------------- LAYOUT --------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Sales Trend")
    st.pyplot(fig1)

with col2:
    st.subheader("🏆 Top 5 Products")
    st.pyplot(fig2)

# -------------------- DATA TABLE --------------------
st.subheader("📋 Dataset Preview")
st.dataframe(filtered_df)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | DIY Internship Project")