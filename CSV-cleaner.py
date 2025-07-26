import pandas as pd

# Load CSV
df = pd.read_csv('data.csv')

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Drop rows with missing values
df.dropna(inplace=True)

# Basic summary stats
summary = df.describe(include='all')

# Save summary to CSV
summary.to_csv('summary_report.csv')

print("✅ Your CSV is cleaned & summarized.")
