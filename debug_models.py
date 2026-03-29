"""
Debug: Train a fresh DT and test if it detects disease
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE

# Load
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Features
feature_cols = ['Age', 'Gender', 'Resting_BP', 'Cholesterol', 'Fasting_Blood_Sugar',
                'Max_Heart_Rate', 'ECG_Result', 'Smoking_Status', 'Alcohol_Consumption',
                'Physical_Activity_Level', 'Diet_Quality_Score', 'Sleep_Hours', 'BMI',
                'Diabetes', 'Hypertension', 'Family_History']

X = df[feature_cols].copy()
y = df['target']  # 0=Healthy, 1=Disease

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
X_test_scaled = scaler.transform(X_test)

# TRAIN DT
dt_fresh = DecisionTreeClassifier(max_depth=12, random_state=42, class_weight='balanced')
dt_fresh.fit(X_train_scaled, y_train_balanced)

# TEST ON actual disease cases in test set
disease_indices = np.where(y_test == 1)[0]
print(f"Found {len(disease_indices)} disease cases in test set\n")

# Test on first few disease cases
for i in disease_indices[:3]:
    x_case = X_test_scaled[[i]]
    pred = dt_fresh.predict(x_case)[0]
    print(f"Case {i}: Actual=1 (Disease), Predicted={pred}, Correct={pred==1}")

# Also test on first few healthy cases
healthy_indices = np.where(y_test == 0)[0]
print(f"\nFound {len(healthy_indices)} healthy cases in test set\n")

for i in healthy_indices[:3]:
    x_case = X_test_scaled[[i]]
    pred = dt_fresh.predict(x_case)[0]
    print(f"Case {i}: Actual=0 (Healthy), Predicted={pred}, Correct={pred==0}")

# Compare with saved model
dt_saved = joblib.load("Backend/models/heart/dt.pkl")

print(f"\n\nCOMPARISON - Disease case 0:")
x_case = X_test_scaled[[disease_indices[0]]]
pred_fresh = dt_fresh.predict(x_case)[0]
pred_saved = dt_saved.predict(x_case)[0]
print(f"Fresh model: {pred_fresh}")
print(f"Saved model: {pred_saved}")

if pred_fresh != pred_saved:
    print("\n⚠️  MODELS DIFFER! The saved model might be broken.")
