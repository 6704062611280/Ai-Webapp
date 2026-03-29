import joblib
import pandas as pd
import numpy as np

# Load models and utilities
dt_model = joblib.load("Backend/models/heart/dt.pkl")
heart_scaler = joblib.load("Backend/models/heart/scaler.pkl")
heart_columns = joblib.load("Backend/models/heart/columns.pkl")
heart_label_encoder = joblib.load("Backend/models/heart/label_encoder.pkl")
heart_feature_encoders = joblib.load("Backend/models/heart/feature_encoders_heart.pkl")

print("Model loaded successfully")
print(f"Heart columns: {heart_columns}")
print(f"Scaler expecting {heart_scaler.n_features_in_} features")
print()

# Prepare disease example (exactly as backend would receive it)
disease_data = {
    'age': 70,
    'gender': 1,  # 0=Female, 1=Male
    'restingBp': 130,
    'cholesterol': 213,
    'fastingBloodSugar': 120,
    'maxHr': 148,
    'ecgResult': 1,  # 0=LVH, 1=Normal, 2=ST
    'smokingStatus': 0,  # 0=Current, 1=Former, 2=Never
    'alcoholConsumption': 3,
    'physicalActivityLevel': 1,  # 0=High, 1=Low, 2=Moderate
    'dietQualityScore': 35,
    'sleepHours': 6,
    'bmi': 28,
    'diabetes': 1,
    'hypertension': 1,
    'familyHistory': 1,
    'riskScore': 80
}

# Map integer inputs to categorical text values (EXACTLY as backend does)
gender_map = {0: 'Female', 1: 'Male'}
ecg_map = {0: 'LVH', 1: 'Normal', 2: 'ST'}
smoking_map = {0: 'Current', 1: 'Former', 2: 'Never'}
activity_map = {0: 'High', 1: 'Low', 2: 'Moderate'}

# Create DataFrame with categorical values (before encoding) (EXACTLY as backend does)
df_input = pd.DataFrame([{
    'Age': disease_data['age'],
    'Gender': gender_map.get(int(disease_data['gender']), 'Male'),
    'Resting_BP': disease_data['restingBp'],
    'Cholesterol': disease_data['cholesterol'],
    'Fasting_Blood_Sugar': disease_data['fastingBloodSugar'],
    'Max_Heart_Rate': disease_data['maxHr'],
    'ECG_Result': ecg_map.get(int(disease_data['ecgResult']), 'Normal'),
    'Smoking_Status': smoking_map.get(int(disease_data['smokingStatus']), 'Never'),
    'Alcohol_Consumption': disease_data['alcoholConsumption'],
    'Physical_Activity_Level': activity_map.get(int(disease_data['physicalActivityLevel']), 'Moderate'),
    'Diet_Quality_Score': disease_data['dietQualityScore'],
    'Sleep_Hours': disease_data['sleepHours'],
    'BMI': disease_data['bmi'],
    'Diabetes': disease_data['diabetes'],
    'Hypertension': disease_data['hypertension'],
    'Family_History': disease_data['familyHistory']
}])

print("DataFrame created:")
print(df_input)
print()

# Encode categorical columns using the saved encoders (EXACTLY as backend does)
print("Encoding categorical columns...")
for col in ['Gender', 'ECG_Result', 'Smoking_Status', 'Physical_Activity_Level']:
    if col in heart_feature_encoders:
        print(f"  Encoding {col}: {df_input[col].values[0]} -> ", end='')
        df_input[col] = heart_feature_encoders[col].transform(df_input[col])
        print(df_input[col].values[0])
print()

# Reorder and select columns (EXACTLY as backend does)
print(f"Reordering columns to: {heart_columns}")
df_input = df_input[heart_columns]
print(f"DataFrame shape after reorder: {df_input.shape}")
print()

# Scale (EXACTLY as backend does)
print("Scaling...")
x = heart_scaler.transform(df_input.values)
print(f"Scaled shape: {x.shape}")
print(f"Scaled values: {x}")
print()

# Predict (EXACTLY as backend does)
print("Predicting with DT model...")
result = dt_model.predict(x)
probs = dt_model.predict_proba(x)[0]
print(f"Prediction result: {result}")
print(f"Classes: {dt_model.classes_}")
print(f"Probabilities: {probs}")
print()

# Decode label (EXACTLY as backend does)
accuracy = float(np.max(probs)) * 100
label = str(heart_label_encoder.inverse_transform([int(result[0])])[0])
heart_label_map = {
    '0': 'Healthy',
    '1': 'Heart disease',
    0: 'Healthy',
    1: 'Heart disease'
}
label = heart_label_map.get(label, label)

print(f"Final result: {label}")
print(f"Accuracy: {accuracy:.2f}%")
