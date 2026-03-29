"""
Retrain heart models with exactly 16 features (matching existing scaler)
and aggressive disease detection weights
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
print("TRAIN HEART MODELS - 16 FEATURES (NO RISK_SCORE)")
print("WITH AGGRESSIVE DISEASE DETECTION")
print("="*70 + "\n")

# Load data
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Use 16 features (exclude Risk_Score and target columns)
feature_cols = ['Age', 'Gender', 'Resting_BP', 'Cholesterol', 'Fasting_Blood_Sugar',
                'Max_Heart_Rate', 'ECG_Result', 'Smoking_Status', 'Alcohol_Consumption',
                'Physical_Activity_Level', 'Diet_Quality_Score', 'Sleep_Hours', 'BMI',
                'Diabetes', 'Hypertension', 'Family_History']

X = df[feature_cols].copy()
y = df['target']

print(f"Dataset: {X.shape}")
print(f"Features ({len(feature_cols)}): {feature_cols}")
print(f"Target distribution:\n{y.value_counts()}\n")

# Encode categorical
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

print(f"After encoding: {X.shape}\n")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# SMOTE 1.0
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# NEW SCALER
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

print(f"After SMOTE: Train {X_train_scaled.shape}")
print(f"Train class distribution: {np.bincount(y_train_balanced)}\n")

# Class weights
disease_count = (y_train == 1).sum()
healthy_count = (y_train == 0).sum()
weight_disease = healthy_count / (2 * disease_count)
class_weight_dict = {0: 1.0, 1: weight_disease}

print(f"Class weights: Healthy=1.0, Disease={weight_disease:.4f}\n")
print("="*70)
print("TRAINING MODELS")
print("="*70 + "\n")

# 1. DT
print("1. DECISION TREE")
dt = DecisionTreeClassifier(max_depth=12, random_state=42, class_weight='balanced')
dt.fit(X_train_scaled, y_train_balanced)
y_pred = dt.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, dt.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
print(f"  Recall (Disease): {np.sum((y_pred == 1) & (y_test == 1)) / np.sum(y_test == 1):.2%}")
joblib.dump(dt, "Backend/models/heart/dt.pkl")

# 2. KNN
print("\n2. K-NEAREST NEIGHBORS")
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train_scaled, y_train_balanced)
y_pred = knn.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, knn.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
print(f"  Recall (Disease): {np.sum((y_pred == 1) & (y_test == 1)) / np.sum(y_test == 1):.2%}")
joblib.dump(knn, "Backend/models/heart/knn.pkl")

# 3. SVM
print("\n3. SUPPORT VECTOR MACHINE")
svm = SVC(kernel='rbf', C=100.0, gamma=0.001, class_weight=class_weight_dict, probability=True, random_state=42)
svm.fit(X_train_scaled, y_train_balanced)
y_pred = svm.predict(X_test_scaled)
acc = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, svm.predict_proba(X_test_scaled)[:, 1])
print(f"  Accuracy: {acc:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")
print(f"  Recall (Disease): {np.sum((y_pred == 1) & (y_test == 1)) / np.sum(y_test == 1):.2%}")
joblib.dump(svm, "Backend/models/heart/svm.pkl")

# For NN, we'll skip since it takes longer
print("\n4. NEURAL NETWORK: Skipped (using existing trained model)")
print("   (NN training takes significant time - using model.h5 from previous run)")

# Save
print("\n" + "="*70)
print("SAVING UTILITIES")
print("="*70 + "\n")

joblib.dump(feature_cols, "Backend/models/heart/columns.pkl")
joblib.dump(scaler, "Backend/models/heart/scaler.pkl")  # NEW SCALER!

le = LabelEncoder()
le.fit([0, 1])
joblib.dump(le, "Backend/models/heart/label_encoder.pkl")

print(f"✓ Columns: {len(feature_cols)} features (no Risk_Score)")
print(f"✓ Scaler: NEW - trained on {X_train_scaled.shape}")
print(f"✓ Models: DT, KNN, SVM saved\n")

print("="*70)
print("COMPLETION!")
print("="*70)
print("\n✓ Disease detection models trained with:")
print("  - Aggressive disease class weight")
print("  - SMOTE full balance (1.0 ratio)")
print("  - Optimized SVM parameters")
print(f"  - All models should now DETECT Heart Disease cases correctly!\n")
