import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load CSV
df = pd.read_csv('data.csv')

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Drop rows with missing values
df.dropna(inplace=True)

# Get summary and transpose it
summary = df.describe(include='all').T

# Format numeric values to 2 decimal places
summary = summary.round(2)

# Fill empty cells with "-"
summary.fillna("-", inplace=True)

# Optional: reset index and rename for cleaner CSV
summary.reset_index(inplace=True)
summary.rename(columns={'index': 'Column'}, inplace=True)

# Save to CSV
summary.to_csv('summary_report.csv', index=False)

print("✅ Clean, readable summary report saved as 'summary_report.csv'")
