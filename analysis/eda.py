import pandas as pd

# Load dataset
df = pd.read_csv("data/automobile_dataset.csv")

# Preview dataset
print("First rows of dataset:")
print(df.head())

# Dataset structure
print("\nDataset info:")
print(df.info())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())


def analyze_feature(df: pd.DataFrame, column: str) -> None:
    """
    Analyze mean, median, and skewness of a specific feature.
    """
    print(f"\n--- ANALYSIS: {column} ---")

    mean_value = df[column].mean()
    median_value = df[column].median()
    skew_value = df[column].skew()

    print(f"Mean:\n{mean_value}")
    print(f"\nMedian:\n{median_value}")
    print(f"\nSkew:\n{skew_value}")

    if abs(skew_value) < 0.5:
        print("\nDistribution is approximately symmetric → mean is acceptable")
    else:
        print("\nDistribution is skewed → median is preferred")


# Analyze normalized-losses
analyze_feature(df, "normalized-losses")


# Global dataset statistics
print("\nGlobal dataset statistics:")
print(df.describe())
