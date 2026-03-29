import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load
encoders = joblib.load('Backend/models/heart/feature_encoders_heart.pkl')
scaler = joblib.load('Backend/models/heart/scaler.pkl')
cols = joblib.load('Backend/models/heart/columns.pkl')
svm = joblib.load('Backend/models/heart/svm.pkl')

print(f"Encoders: {list(encoders.keys())}")
print(f"Columns: {len(cols)} features")
print(f"SVM classes: {svm.classes_}")
print()

# Test 1: Disease example
test_df = pd.DataFrame([{
    'Age': 65,
    'Gender': 'Male',  # gender=1
    'Resting_BP': 160,
    'Cholesterol': 280,
    'Fasting_Blood_Sugar': 150,
    'Max_Heart_Rate': 90,
    'ECG_Result': 'ST',  # ecgResult=2
    'Smoking_Status': 'Current',  # smokingStatus=0
    'Alcohol_Consumption': 2,
    'Physical_Activity_Level': 'Low',  # physicalActivityLevel=1
    'Diet_Quality_Score': 30,
    'Sleep_Hours': 5,
    'BMI': 30,
    'Diabetes': 1,
    'Hypertension': 1,
    'Family_History': 1
}])[cols]

# Encode
for col in ['Gender', 'ECG_Result', 'Smoking_Status', 'Physical_Activity_Level']:
    if col in encoders:
        test_df[col] = encoders[col].transform(test_df[col])
        print(f"{col}: {test_df[col].values[0]}")

# Scale and predict
test_scaled = scaler.transform(test_df)
pred = svm.predict(test_scaled)
proba = svm.predict_proba(test_scaled)

print(f"\nPrediction: {pred[0]} (0=Healthy, 1=Disease)")
print(f"Probabilities: {proba[0]}")
print(f"Prediction class name: {'Disease' if pred[0] == 1 else 'Healthy'}")
