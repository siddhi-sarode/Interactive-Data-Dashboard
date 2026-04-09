import pandas as pd
import random

print("🚀 Starting Data Cleaning...")

# Load dataset
try:
    df = pd.read_csv('data/dataset.csv', encoding='latin1')
    print("✅ Dataset loaded successfully")
except Exception as e:
    print("❌ Error loading dataset:", e)
    exit()

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

print("\n📊 Columns in dataset:")
print(df.columns)

# Convert date column safely
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    print("✅ Order Date converted")
else:
    print("⚠️ 'Order Date' column not found")

# Handle missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Convert Region to Indian states (optional but good for project)
if 'Region' in df.columns:
    indian_states = ['Maharashtra', 'Delhi', 'Karnataka', 'Gujarat', 'Tamil Nadu']
    df['Region'] = [random.choice(indian_states) for _ in range(len(df))]
    print("✅ Converted to Indian regions")

# Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)

print("\n🎉 Data cleaning completed successfully!")
print(f"📁 Cleaned file saved as: data/cleaned_data.csv")