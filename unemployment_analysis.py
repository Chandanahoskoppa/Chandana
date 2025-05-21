# unemployment_analysis.py
# Author: Chandana H G
# Data Science Internship - Task 2: Unemployment Analysis with Python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

# Step 1: Download dataset from KaggleHub
path = kagglehub.dataset_download("gokulrajkmv/unemployment-in-india")
print("✅ Dataset downloaded to:", path)

# Step 2: Load the dataset
file_path = f"{path}/Unemployment in India.csv"
data = pd.read_csv(file_path)

# Step 3: Preprocess and clean data
print("\n📊 First 5 rows of dataset:")
print(data.head())

print("\n🧼 Checking for missing values:")
print(data.isnull().sum())

# Rename columns for clarity
data.columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)', 
                'Estimated Employed', 'Estimated Labour Participation Rate (%)', 'Area']

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Step 4: Data Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('📈 Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average unemployment by area type
plt.figure(figsize=(6, 5))
sns.boxplot(x='Area', y='Estimated Unemployment Rate (%)', data=data)
plt.title("📊 Unemployment Rate Distribution by Area Type (Urban/Rural)")
plt.tight_layout()
plt.show()

# Step 5: Summary statistics
print("\n📌 Summary Statistics:")
print(data[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].describe())
