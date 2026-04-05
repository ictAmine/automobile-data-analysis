import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/automobile_dataset.csv")

# Remove missing values
data = df["normalized-losses"].dropna()

# Create figure
plt.figure(figsize=(10,6))

# Histogram
plt.hist(data, bins=20)

# Labels
plt.title("Risk Distribution of Automobile Losses")
plt.xlabel("Normalized Losses")
plt.ylabel("Number of Vehicles")

# Show plot
plt.show()
