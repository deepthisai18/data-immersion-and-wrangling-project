import pandas as pd
# Load the dataset
data = pd.read_excel("students.xlsx")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Check for missing values
print("\nMissing Values in each column:")
print(data.isnull().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing values (if any)
data = data.fillna(0)

# Save cleaned dataset
data.to_csv("cleaned_students.csv", index=False)

print("\nData wrangling completed. Cleaned file saved as cleaned_students.csv\n")