import pandas as pd
import joblib
import numpy as np

# Load training data
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"\nTarget distribution:")
print(df['target'].value_counts())

# Find disease examples
disease_cases = df[df['target'] == 1].head(3)
healthy_cases = df[df['target'] == 0].head(3)

print(f"\n=== DISEASE EXAMPLES ===")
print(disease_cases[['Age', 'Gender', 'Max_Heart_Rate', 'Smoking_Status', 'Diabetes', 'Hypertension', 'target']])

print(f"\n=== HEALTHY EXAMPLES ===")
print(healthy_cases[['Age', 'Gender', 'Max_Heart_Rate', 'Smoking_Status', 'Diabetes', 'Hypertension', 'target']])

# Now load the model and test on first disease case
dt_model = joblib.load("Backend/models/heart/dt.pkl")
heart_columns = joblib.load("Backend/models/heart/columns.pkl")
heart_scaler = joblib.load("Backend/models/heart/scaler.pkl")
heart_label_encoder = joblib.load("Backend/models/heart/label_encoder.pkl")
heart_feature_encoders = joblib.load("Backend/models/heart/feature_encoders_heart.pkl")

print(f"\n=== MODEL INFO ===")
print(f"DT features: {dt_model.n_features_in_}")
print(f"DT classes: {dt_model.classes_}")
print(f"Expected columns: {heart_columns}")

# Get first disease case and prepare it
disease_case = disease_cases.iloc[0].copy()
print(f"\n=== TESTING FIRST DISEASE CASE ===")
print(f"Original values:") 
print(disease_case[heart_columns])

# Encode categorical columns
df_test = pd.DataFrame([disease_case[heart_columns]])
print(f"\nBefore encoding: {df_test.to_dict('records')[0]}")

for col in ['Gender', 'ECG_Result', 'Smoking_Status', 'Physical_Activity_Level']:
    if col in heart_feature_encoders:
        original = df_test[col].values[0]
        df_test[col] = heart_feature_encoders[col].transform(df_test[col])
        print(f"  {col}: {original} -> {df_test[col].values[0]}")

# Scale
X_scaled = heart_scaler.transform(df_test.values)

# Predict
pred = dt_model.predict(X_scaled)
proba = dt_model.predict_proba(X_scaled)[0]

print(f"\nPrediction: {pred[0]}")
print(f"Probabilities: {proba}")
print(f"Classes: {dict(zip(dt_model.classes_, proba))}")

label = str(heart_label_encoder.inverse_transform([int(pred[0])])[0])
print(f"Label: {label}")
