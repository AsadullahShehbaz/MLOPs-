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
df.to_csv("data/dataset.csv", index=False)
print("✅ Raw data saved to data/raw_data.csv")

