import pandas as pd

# Load training data
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Get disease and healthy statistics
disease_data = df[df['target'] == 1]
healthy_data = df[df['target'] == 0]

print("=== DISEASE CASES (target=1) ===")
print(f"Count: {len(disease_data)}")
print(f"\nString columns:")
for col in ['Gender', 'Smoking_Status', 'ECG_Result', 'Physical_Activity_Level']:
    print(f"  {col}:")
    print(f"    {disease_data[col].value_counts().to_dict()}")

print(f"\nNumeric columns (mean):")
numeric_cols = ['Age', 'Resting_BP', 'Cholesterol', 'Fasting_Blood_Sugar', 'Max_Heart_Rate', 
                'Alcohol_Consumption', 'Diet_Quality_Score', 'Sleep_Hours', 'BMI', 
                'Diabetes', 'Hypertension', 'Family_History']
for col in numeric_cols:
    print(f"  {col}: {disease_data[col].mean():.2f}")

# Get first disease case as template
first_disease = disease_data.iloc[0]
print(f"\n=== FIRST DISEASE CASE (READY TO USE) ===")
print("{")
print(f"  age: {int(first_disease['Age'])},")
print(f"  gender: {0 if first_disease['Gender'] == 'Female' else 1},  // {first_disease['Gender']}")
print(f"  restingBp: {int(first_disease['Resting_BP'])},")
print(f"  cholesterol: {int(first_disease['Cholesterol'])},")
print(f"  fastingBloodSugar: {int(first_disease['Fasting_Blood_Sugar'])},")
print(f"  maxHr: {int(first_disease['Max_Heart_Rate'])},")
ecg_map = {'LVH': 0, 'Normal': 1, 'ST': 2}
print(f"  ecgResult: {ecg_map[first_disease['ECG_Result']]},  // {first_disease['ECG_Result']}")
smoking_map = {'Current': 0, 'Former': 1, 'Never': 2}
print(f"  smokingStatus: {smoking_map[first_disease['Smoking_Status']]},  // {first_disease['Smoking_Status']}")
print(f"  alcoholConsumption: {int(first_disease['Alcohol_Consumption'])},")
activity_map = {'High': 0, 'Low': 1, 'Moderate': 2}
print(f"  physicalActivityLevel: {activity_map[first_disease['Physical_Activity_Level']]},  // {first_disease['Physical_Activity_Level']}")
print(f"  dietQualityScore: {int(first_disease['Diet_Quality_Score'])},")
print(f"  sleepHours: {int(first_disease['Sleep_Hours'])},")
print(f"  bmi: {int(first_disease['BMI'])},")
print(f"  diabetes: {int(first_disease['Diabetes'])},")
print(f"  hypertension: {int(first_disease['Hypertension'])},")
print(f"  familyHistory: {int(first_disease['Family_History'])},")
print(f"  riskScore: {int(first_disease['Risk_Score'])}")
print("}")
