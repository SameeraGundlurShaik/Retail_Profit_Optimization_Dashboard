import pandas as pd

print("✅ START retail_etl")

# Load raw retail dataset
df = pd.read_csv("data/raw_superstore.csv")

print("Raw shape:", df.shape)
print("Columns:", df.columns.tolist())

# Convert date columns
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], errors="coerce")

# Convert numeric columns
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# Drop missing important values
df = df.dropna(subset=["Order_ID", "Order_Date", "Sales", "Profit", "Discount", "Quantity"])

# Remove duplicates
df = df.drop_duplicates()

# Derived columns
df["order_year"] = df["Order_Date"].dt.year
df["order_month"] = df["Order_Date"].dt.month
df["order_month_name"] = df["Order_Date"].dt.strftime("%b")

df["profit_margin"] = (df["Profit"] / df["Sales"]).round(4)

def discount_bucket(x):
    if x == 0:
        return "No Discount"
    elif x <= 0.10:
        return "Low (0-10%)"
    elif x <= 0.20:
        return "Medium (11-20%)"
    else:
        return "High (>20%)"

df["discount_bucket"] = df["Discount"].apply(discount_bucket)

# Save output
df.to_csv("data/clean_orders.csv", index=False)

print("✅ Saved: data/clean_orders.csv")
print("Clean shape:", df.shape)
print("✅ END retail_etl")
