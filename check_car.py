import pandas as pd

# Check car dataset structure
df = pd.read_csv('Model/Car-evaluation/car.csv')
print("Car dataset columns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.head())
print("\nClass distribution:")
print(df['class'].value_counts())
print("\nValues in each column:")
for col in df.columns[:-1]:
    print(f"{col}: {df[col].unique()[:5]}")
