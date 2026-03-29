"""
Retrain all heart models with CORRECT 17 features including Risk_Score
This fixes the scaler mismatch issue.
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
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.regularizers import L2
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, f1_score, roc_auc_score

print("\n" + "="*70)
print("RETRAIN HEART MODELS WITH ALL 17 FEATURES (INCLUDING RISK_SCORE)")
print("="*70 + "\n")

# Load data
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Select ALL features except target columns
feature_cols = [col for col in df.columns if col not in ['target', 'target_name', 'Risk_Level']]
X = df[feature_cols].copy()
y = df['target']

print(f"Dataset: {X.shape}")
print(f"Features ({len(feature_cols)}): {feature_cols}")
print(f"Target distribution:\n{y.value_counts()}\n")

# Encode categorical columns
label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

print(f"After encoding: {X.shape}\n")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Train: {X_train.shape}, Test: {X_test.shape}\n")

# Apply SMOTE for full balance
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print(f"After SMOTE: Train {X_train_balanced.shape}")
print(f"Train class distribution: {np.bincount(y_train_balanced)}")
print(f"Test class distribution: {np.bincount(y_test)}\n")

# Fit scaler on training data ONLY
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

print("="*70)
print("TRAINING MODELS")
print("="*70 + "\n")

# Class weights - aggressive for disease
disease_count = (y_train == 1).sum()
healthy_count = (y_train == 0).sum()
weight_disease = healthy_count / (2 * disease_count)
class_weight_dict = {0: 1.0, 1: weight_disease}

print(f"Class weights: Healthy=1.0, Disease={weight_disease:.4f}\n")

# 1. Decision Tree
print("1. DECISION TREE")
dt = DecisionTreeClassifier(max_depth=12, random_state=42, class_weight='balanced')
dt.fit(X_train_scaled, y_train_balanced)
y_pred = dt.predict(X_test_scaled)
y_proba = dt.predict_proba(X_test_scaled)[:, 1]
print(f"  Accuracy: {np.mean(y_pred == y_test):.4f}")
print(f"  F1-Score: {f1_score(y_test, y_pred):.4f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")
joblib.dump(dt, "Backend/models/heart/dt.pkl")

# 2. KNN with distance weights
print("\n2. K-NEAREST NEIGHBORS")
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train_scaled, y_train_balanced)
y_pred = knn.predict(X_test_scaled)
y_proba = knn.predict_proba(X_test_scaled)[:, 1]
print(f"  Accuracy: {np.mean(y_pred == y_test):.4f}")
print(f"  F1-Score: {f1_score(y_test, y_pred):.4f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")
joblib.dump(knn, "Backend/models/heart/knn.pkl")

# 3. SVM - aggressive settings
print("\n3. SUPPORT VECTOR MACHINE")
svm = SVC(kernel='rbf', C=100.0, gamma=0.001, class_weight=class_weight_dict, probability=True, random_state=42)
svm.fit(X_train_scaled, y_train_balanced)
y_pred = svm.predict(X_test_scaled)
y_proba = svm.predict_proba(X_test_scaled)[:, 1]
print(f"  Accuracy: {np.mean(y_pred == y_test):.4f}")
print(f"  F1-Score: {f1_score(y_test, y_pred):.4f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")
joblib.dump(svm, "Backend/models/heart/svm.pkl")

# 4. Neural Network - improved architecture
print("\n4. NEURAL NETWORK")
nn = Sequential([
    layers.Dense(256, activation='relu', kernel_regularizer=L2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    
    layers.Dense(128, activation='relu', kernel_regularizer=L2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.4),
    
    layers.Dense(64, activation='relu', kernel_regularizer=L2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(32, activation='relu', kernel_regularizer=L2(0.001)),
    layers.Dropout(0.2),
    
    layers.Dense(2, activation='softmax')
])

optimizer = keras.optimizers.Adam(learning_rate=0.0005)
nn.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

print("  Training... (this may take a minute)")
history = nn.fit(
    X_train_scaled, y_train_balanced,
    epochs=150, batch_size=32, validation_split=0.2,
    callbacks=[early_stopping], verbose=0
)

y_pred_proba = nn.predict(X_test_scaled)
y_pred = np.argmax(y_pred_proba, axis=1)
print(f"  Accuracy: {np.mean(y_pred == y_test):.4f}")
print(f"  F1-Score: {f1_score(y_test, y_pred):.4f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_pred_proba[:, 1]):.4f}")
nn.save("Backend/models/heart/model.h5")

# Save utilities
print("\n" + "="*70)
print("SAVING UTILITIES")
print("="*70 + "\n")

joblib.dump(feature_cols, "Backend/models/heart/columns.pkl")
joblib.dump(scaler, "Backend/models/heart/scaler.pkl")

# Get label encoder from data
le = LabelEncoder()
le.fit([0, 1])
joblib.dump(le, "Backend/models/heart/label_encoder.pkl")

print(f"✓ Columns: {len(feature_cols)} features")
print(f"✓ Scaler: Trained on {X_train_scaled.shape}")
print(f"✓ Models: DT, KNN, SVM, NN saved\n")

print("="*70)
print("ALL HEART MODELS RETRAINED SUCCESSFULLY!")
print("="*70 + "\n")
