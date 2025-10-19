import pandas as pd
import os

# Step 1: Create sample dataset
data = {
    "Name": ["Ayan", "Arsal", "Abdullah", "Anas", "Ibrahim"],
    "Age": [9, 9, 10, 6, 5],
    "Salary": [50000, 60000, 70000, 80000, 30000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv("data/raw_data.csv", index=False)
print("✅ Raw data saved to data/raw_data.csv")

# Step 2: Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Step 3: Save processed data
df.to_csv("data/processed_data.csv", index=False)
print("✅ Processed data saved to data/processed_data.csv")
