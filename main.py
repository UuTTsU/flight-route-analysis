

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"

df = pd.read_csv(url, header=None, names=[
    "airline", "airline_id", "src_airport", "src_airport_id",
    "dst_airport", "dst_airport_id", "codeshare", "stops", "equipment"
])

# --- Analysis 1: Which airlines have the most routes? ---
top_airlines = df["airline"].value_counts().head(15)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_airlines.values, y=top_airlines.index, palette="Blues_r")
plt.title("Top 15 Airlines by Number of Routes", fontsize=16)
plt.xlabel("Number of Routes")
plt.ylabel("Airline Code")
plt.tight_layout()
plt.savefig("top_airlines.png")
plt.show()

# --- Analysis 2: Most connected airports (busiest hubs) ---
src_counts = df["src_airport"].value_counts().head(15)

plt.figure(figsize=(12, 6))
sns.barplot(x=src_counts.values, y=src_counts.index, palette="Oranges_r")
plt.title("Top 15 Busiest Departure Airports", fontsize=16)
plt.xlabel("Number of Departing Routes")
plt.ylabel("Airport Code")
plt.tight_layout()
plt.savefig("busiest_airports.png")
plt.show()

# --- Analysis 3: Direct vs connecting flights ---
stops_dist = df["stops"].value_counts()

plt.figure(figsize=(8, 5))
stops_dist.plot(kind="bar", color=["#2196F3", "#FF9800", "#4CAF50"])
plt.title("Direct vs Connecting Flights Distribution", fontsize=16)
plt.xlabel("Number of Stops")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("stops_distribution.png")
plt.show()
