import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw_data.csv")

print("Raw Shape:", df.shape)
print("Raw Columns:", list(df.columns))

# Remove duplicates
df = df.drop_duplicates()

# Drop missing values (simple cleaning for now)
df = df.dropna()

# Clean column names (SQL friendly)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ---------- Feature Engineering (Unique Columns) ----------

# Average percentage (uses all columns ending with _p)
score_cols = [c for c in df.columns if c.endswith("_p")]
if score_cols:
    df["avg_percentage"] = df[score_cols].mean(axis=1).round(2)

# Placed flag
if "status" in df.columns:
    df["placed_flag"] = df["status"].astype(str).str.lower().apply(
        lambda x: 1 if x == "placed" else 0
    )

# Salary numeric + bucket
if "salary" in df.columns:
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    df["salary_bucket"] = pd.cut(
        df["salary"],
        bins=[0, 200000, 400000, 600000, 1000000],
        labels=["0-2L", "2-4L", "4-6L", "6L+"]
    )

# Save cleaned dataset
df.to_csv("data/clean_data.csv", index=False)

print("✅ Cleaning Completed!")
print("Clean Shape:", df.shape)
print("Saved: data/clean_data.csv")
