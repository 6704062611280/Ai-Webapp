import joblib
import pandas as pd

svm = joblib.load('Backend/models/heart/svm.pkl')
scaler = joblib.load('Backend/models/heart/scaler.pkl')
cols = joblib.load('Backend/models/heart/columns.pkl')

test_df = pd.DataFrame([{
    'Age': 65,
    'Gender': 1,
    'Resting_BP': 160,
    'Cholesterol': 280,
    'Fasting_Blood_Sugar': 150,
    'Max_Heart_Rate': 90,
    'ECG_Result': 2,
    'Smoking_Status': 0,
    'Alcohol_Consumption': 2,
    'Physical_Activity_Level': 1,
    'Diet_Quality_Score': 30,
    'Sleep_Hours': 5,
    'BMI': 30,
    'Diabetes': 1,
    'Hypertension': 1,
    'Family_History': 1
}])[cols]

test_scaled = scaler.transform(test_df)
pred = svm.predict(test_scaled)[0]
proba = svm.predict_proba(test_scaled)[0]

print(f"SVM Prediction: {'Disease' if pred == 1 else 'Healthy'} (Disease prob: {proba[1]:.1%})")
