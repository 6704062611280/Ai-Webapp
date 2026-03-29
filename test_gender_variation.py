import pandas as pd
import joblib
import numpy as np

# Load the models
dt_model = joblib.load("Backend/models/heart/dt.pkl")
heart_columns = joblib.load("Backend/models/heart/columns.pkl")
heart_scaler = joblib.load("Backend/models/heart/scaler.pkl")
heart_label_encoder = joblib.load("Backend/models/heart/label_encoder.pkl")
heart_feature_encoders = joblib.load("Backend/models/heart/feature_encoders_heart.pkl")

# Our current test case is Male (1), let me try Female (0) instead
test_cases = [
    {
        'name': 'Original Male Case',
        'data': {'Age': 70, 'Gender': 'Male', 'Resting_BP': 130, 'Cholesterol': 213, 'Fasting_Blood_Sugar': 120, 'Max_Heart_Rate': 148, 'ECG_Result': 'Normal', 'Smoking_Status': 'Current', 'Alcohol_Consumption': 3, 'Physical_Activity_Level': 'Low', 'Diet_Quality_Score': 35, 'Sleep_Hours': 6, 'BMI': 28, 'Diabetes': 1, 'Hypertension': 1, 'Family_History': 1}
    },
    {
        'name': 'Female Version of Case',
        'data': {'Age': 70, 'Gender': 'Female', 'Resting_BP': 130, 'Cholesterol': 213, 'Fasting_Blood_Sugar': 120, 'Max_Heart_Rate': 148, 'ECG_Result': 'Normal', 'Smoking_Status': 'Current', 'Alcohol_Consumption': 3, 'Physical_Activity_Level': 'Low', 'Diet_Quality_Score': 35, 'Sleep_Hours': 6, 'BMI': 28, 'Diabetes': 1, 'Hypertension': 1, 'Family_History': 1}
    },
    {
        'name': 'Match Dataset Average (Female)',
        'data': {'Age': 66, 'Gender': 'Female', 'Resting_BP': 121.88, 'Cholesterol': 211.31, 'Fasting_Blood_Sugar': 177.41, 'Max_Heart_Rate': 141.30, 'ECG_Result': 'Normal', 'Smoking_Status': 'Current', 'Alcohol_Consumption': 2.58, 'Physical_Activity_Level': 'Moderate', 'Diet_Quality_Score': 4.96, 'Sleep_Hours': 6.07, 'BMI': 25.57, 'Diabetes': 1, 'Hypertension': 1, 'Family_History': 1}
    }
]

print("=== TESTING DIFFERENT DISEASE EXAMPLES ===\n")

for test_case in test_cases:
    print(f"TEST: {test_case['name']}")
    
    # Create DataFrame
    df_test = pd.DataFrame([test_case['data']])
    
    # Encode categorical
    for col in ['Gender', 'ECG_Result', 'Smoking_Status', 'Physical_Activity_Level']:
        if col in heart_feature_encoders:
            df_test[col] = heart_feature_encoders[col].transform(df_test[col])
    
    # Scale
    X_scaled = heart_scaler.transform(df_test[heart_columns].values)
    
    # Predict
    pred = dt_model.predict(X_scaled)
    proba = dt_model.predict_proba(X_scaled)[0]
    
    result_label = 'Healthy' if pred[0] == 0 else 'Disease'
    print(f"  Result: {result_label}")
    print(f"  Probability - Healthy: {proba[0]:.4f}, Disease: {proba[1]:.4f}")
    print()
