import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------- PAGE SETUP -------------------
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("🛒 E-commerce Sales Dashboard")
st.markdown("## 📊 Data Analysis & Insights")

# ------------------- LOAD DATA -------------------
df = pd.read_csv("data/dataset.csv", encoding='latin1')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ------------------- SIDEBAR FILTERS -------------------
st.sidebar.header("🔎 Filters")

if st.sidebar.button("🔄 Reset Filters"):
   st.experimental_rerun()

# State filter
state = st.sidebar.selectbox("Select State", df['State'].unique())

# Category filter
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

st.write(f"📍 Selected State: {state} | Category: {category}")

# Apply filters
df = df[(df['State'] == state) & (df['Category'] == category)]

if df.empty:
    st.warning("⚠️ No data available for selected filters")
    st.stop()

st.success("✅ Dashboard updated based on selected filters")

# ------------------- DATE FILTER -------------------
min_date = df['Order Date'].min()
max_date = df['Order Date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

if len(date_range) == 2:
    df = df[
        (df['Order Date'] >= pd.to_datetime(date_range[0])) &
        (df['Order Date'] <= pd.to_datetime(date_range[1]))
    ]

# SALES FILTER
min_sales = int(df['Sales'].min())
max_sales = int(df['Sales'].max())

sales_range = st.sidebar.slider(
    "Select Sales Range",
    min_value=min_sales,
    max_value=max_sales,
    value=(min_sales, max_sales)
)

df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]
# ------------------- SORT OPTION -------------------
sort_option = st.sidebar.selectbox(
    "Sort Sales",
    ["Highest First", "Lowest First"]
)

ascending = True if sort_option == "Lowest First" else False

# ------------------- KPI -------------------
total_sales = int(df['Sales'].sum())
total_profit = int(df['Profit'].sum())
total_orders = df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"₹{total_sales:,}")
col2.metric("📈 Total Profit", f"₹{total_profit:,}")
col3.metric("📦 Total Orders", total_orders)

st.markdown("---")

# ------------------- MONTHLY SALES -------------------
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Sales'].sum()

fig1, ax1 = plt.subplots()
monthly_sales.plot(
    ax=ax1,
    color='orange',
    marker='o',
    linewidth=2
)

ax1.set_title("Monthly Sales Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
ax1.grid(True)

# ------------------- TOP PRODUCTS -------------------
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=ascending)
    .head(5)
)

fig2, ax2 = plt.subplots()
top_products.plot(kind='bar', ax=ax2, color='green')

ax2.set_title("Top 5 Products")
ax2.set_ylabel("Sales")

# ------------------- LAYOUT -------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Sales Trend")
    st.pyplot(fig1)

with col2:
    st.subheader("🏆 Top 5 Products")
    st.pyplot(fig2)

# ------------------- RAW DATA -------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(df)