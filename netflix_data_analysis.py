import pandas as pd
import matplotlib.pyplot as plt

# Sample Netflix data
data = {
    "Title": ["Inception", "Stranger Things", "Extraction", "The Irishman", "Dark"],
    "Type": ["Movie", "TV Show", "Movie", "Movie", "TV Show"],
    "Country": ["USA", "USA", "India", "USA", "Germany"],
    "Year": [2010, 2016, 2020, 2019, 2017]
}

# Convert data to a table
df = pd.DataFrame(data)

# Print the data
print("Data Table:")
print(df)

# Count of Movies vs TV Shows
print("\nType Count:")
print(df["Type"].value_counts())

# Plot chart
df["Type"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
