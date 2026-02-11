import pandas as pd

# Load dataset
df = pd.read_csv("data/automobile_dataset.csv")

# Preview dataset
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
