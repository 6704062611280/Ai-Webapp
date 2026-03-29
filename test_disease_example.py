"""
Test the fresh model with our disease example
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE

# Replicatetraining process
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

feature_cols = ['Age', 'Gender', 'Resting_BP', 'Cholesterol', 'Fasting_Blood_Sugar',
                'Max_Heart_Rate', 'ECG_Result', 'Smoking_Status', 'Alcohol_Consumption',
                'Physical_Activity_Level', 'Diet_Quality_Score', 'Sleep_Hours', 'BMI',
                'Diabetes', 'Hypertension', 'Family_History']

X = df[feature_cols].copy()
y = df['target']

# Encode
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# SMOTE
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)

# Train
dt = DecisionTreeClassifier(max_depth=12, random_state=42, class_weight='balanced')
dt.fit(X_train_scaled, y_train_balanced)

# Load saved encoders for categorical features
encoders = joblib.load('Backend/models/heart/feature_encoders_heart.pkl')
cols_loaded = joblib.load('Backend/models/heart/columns.pkl')

print(f"Loaded {len(cols_loaded)} cols: {cols_loaded}\n")

# Create our disease example - AS TEXT FIRST
test_df = pd.DataFrame([{
    'Age': 65,
    'Gender': 'Male',
    'Resting_BP': 160,
    'Cholesterol': 280,
    'Fasting_Blood_Sugar': 150,
    'Max_Heart_Rate': 90,
    'ECG_Result': 'ST',
    'Smoking_Status': 'Current',
    'Alcohol_Consumption': 2,
    'Physical_Activity_Level': 'Low',
    'Diet_Quality_Score': 30,
    'Sleep_Hours': 5,
    'BMI': 30,
    'Diabetes': 1,
    'Hypertension': 1,
    'Family_History': 1
}])

# Reorder by columns
test_df = test_df[cols_loaded]

print("Test values before encoding:")
print(test_df.to_string())
print()

# Encode categoricals - the way the training data was encoded
for col in ['Gender', 'ECG_Result', 'Smoking_Status', 'Physical_Activity_Level']:
    if col in encoders:
        test_df[col] = encoders[col].transform(test_df[col])

print("Test values after encoding:")
print(test_df.to_string())
print()

# Scale
test_scaled = scaler.transform(test_df)

# Predict
pred = dt.predict(test_scaled)[0]
proba = dt.predict_proba(test_scaled)[0]

print(f"Decision Tree Prediction: {pred} ({'Disease' if pred == 1 else 'Healthy'})")
print(f"Probabilities: {proba}")
