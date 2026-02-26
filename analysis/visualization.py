import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/automobile_dataset.csv")

# Remove missing values for this feature
data = df["normalized-losses"].dropna()

# Create histogram
plt.hist(data, bins=20)

# Labels
plt.title("Distribution of Normalized Losses")
plt.xlabel("Normalized Losses")
plt.ylabel("Frequency")

# Show plot
plt.show()
