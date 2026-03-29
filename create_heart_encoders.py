"""
Create and save label encoders for heart categoricalfeatures
"""

import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# These are the categorical columns in the data
categorical_cols = {
    'Gender': ['Female', 'Male'],
    'ECG_Result': ['LVH', 'Normal', 'ST'],
    'Smoking_Status': ['Current', 'Former', 'Never'],
    'Physical_Activity_Level': ['High', 'Low', 'Moderate']
}

# Create and fit label encoders
feature_encoders = {}

for col, categories in categorical_cols.items():
    le = LabelEncoder()
    le.fit(categories)
    feature_encoders[col] = le
    print(f"{col}:")
    for i, cat in enumerate(categories):
        print(f"  {cat} → {le.transform([cat])[0]}")
    print()

# Save
joblib.dump(feature_encoders, "Backend/models/heart/feature_encoders_heart.pkl")
print("✓ Saved feature_encoders_heart.pkl")

# Map for display
mappings = {
    'Gender': {0: 'Female', 1: 'Male'},
    'ECG_Result': {0: 'LVH', 1: 'Normal', 2: 'ST'},
    'Smoking_Status': {0: 'Current', 1: 'Former', 2: 'Never'},
    'Physical_Activity_Level': {0: 'High', 1: 'Low', 2: 'Moderate'}
}

print("\nUsage in API:")
print("- gender: 0=Female, 1=Male")
print("- ecgResult: 0=LVH, 1=Normal, 2=ST")
print("- smokingStatus: 0=Current, 1=Former, 2=Never")
print("- physicalActivityLevel: 0=High, 1=Low, 2=Moderate")
