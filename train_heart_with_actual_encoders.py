"""
Train heart models and SAVE the actual label encoders used during training
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, f1_score, roc_auc_score

print("\n" + "="*70)
print("TRAIN & SAVE WITH ACTUAL ENCODERS")
print("="*70 + "\n")

# Load
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

feature_cols = ['Age', 'Gender', 'Resting_BP', 'Cholesterol', 'Fasting_Blood_Sugar',
                'Max_Heart_Rate', 'ECG_Result', 'Smoking_Status', 'Alcohol_Consumption',
                'Physical_Activity_Level', 'Diet_Quality_Score', 'Sleep_Hours', 'BMI',
                'Diabetes', 'Hypertension', 'Family_History']

X = df[feature_cols].copy()
y = df['target']

# Store actual encoders from training
actual_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    actual_encoders[col] = le
    print(f"{col}: {list(zip(le.classes_, le.transform(le.classes_)))}")

print()

# Split, SMOTE, Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

# Class weights
disease_count = (y_train == 1).sum()
healthy_count = (y_train == 0).sum()
weight_disease = healthy_count / (2 * disease_count)
class_weight_dict = {0: 1.0, 1: weight_disease}

print("="*70)
print("TRAINING")
print("="*70)

# DT
print("\n1. DECISION TREE")
dt = DecisionTreeClassifier(max_depth=12, random_state=42, class_weight='balanced')
dt.fit(X_train_scaled, y_train_balanced)
y_pred = dt.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, dt.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
joblib.dump(dt, "Backend/models/heart/dt.pkl")

# KNN
print("\n2. K-NEAREST NEIGHBORS")
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train_scaled, y_train_balanced)
y_pred = knn.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, knn.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
joblib.dump(knn, "Backend/models/heart/knn.pkl")

# SVM
print("\n3. SUPPORT VECTOR MACHINE")
svm = SVC(kernel='rbf', C=100.0, gamma=0.001, class_weight=class_weight_dict, probability=True, random_state=42)
svm.fit(X_train_scaled, y_train_balanced)
y_pred = svm.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, svm.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
joblib.dump(svm, "Backend/models/heart/svm.pkl")

# Save utilities
print("\n" + "="*70)
print("SAVING")
print("="*70)

joblib.dump(feature_cols, "Backend/models/heart/columns.pkl")
joblib.dump(scaler, "Backend/models/heart/scaler.pkl")

le = LabelEncoder()
le.fit([0, 1])
joblib.dump(le, "Backend/models/heart/label_encoder.pkl")

# SAVE THE ACTUAL ENCODERS USED
joblib.dump(actual_encoders, "Backend/models/heart/feature_encoders_heart.pkl")
print("\nActual encoders saved to feature_encoders_heart.pkl")
print("="*70)
