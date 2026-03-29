import pandas as pd

df = pd.read_csv('Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv')
disease_cases = df[df['target'] == 1].head(5)

print('Real disease examples from dataset:\n')
for idx, (_, row) in enumerate(disease_cases.iterrows()):
    print(f'Disease Case {idx + 1}:')
    print(f'  Age: {row["Age"]:.0f}, Gender: {row["Gender"]}, BP: {row["Resting_BP"]:.0f}, Chol: {row["Cholesterol"]:.0f}')
    print(f'  MaxHR: {row["Max_Heart_Rate"]:.0f}, ECG: {row["ECG_Result"]}, Smoking: {row["Smoking_Status"]}')
    print(f'  Activity: {row["Physical_Activity_Level"]}, Diabetes: {int(row["Diabetes"])}, Hypertension: {int(row["Hypertension"])}')
    print()
