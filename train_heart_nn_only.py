"""
Train only the Heart Neural Network with improved disease detection
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.regularizers import L2
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, f1_score, roc_auc_score

print("\n" + "="*60)
print("TRAIN HEART NEURAL NETWORK ONLY")
print("="*60 + "\n")

# Load data
df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Select features (skip target columns)
feature_cols = [col for col in df.columns if col not in ['target', 'target_name']]
X = df[feature_cols].copy()
y = df['target']

print(f"Dataset before encoding: {X.shape}")
print(f"Target distribution:\n{y.value_counts()}\n")

# Encode categorical features
label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

print(f"Dataset after encoding: {X.shape}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Apply SMOTE for full balance
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

print(f"After SMOTE: Train {X_train_scaled.shape}, Test {X_test_scaled.shape}")
print(f"Train class distribution: {np.bincount(y_train_balanced)}")
print(f"Test class distribution: {np.bincount(y_test)}\n")

# ============== NEURAL NETWORK ==============
print("4. TRAINING NEURAL NETWORK")
print("-" * 60)

# Create model with improved architecture
nn = Sequential([
    layers.Dense(256, activation='relu', kernel_regularizer=L2(0.001), input_shape=(X_train_scaled.shape[1],)),
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

# Compile with lower learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.0005)
nn.compile(
    optimizer=optimizer,
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Early stopping callback
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=20,
    restore_best_weights=True
)

# Train
print("Training... (this may take a minute)")
history = nn.fit(
    X_train_scaled, y_train_balanced,
    epochs=150,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=0
)

# Evaluate
y_pred_proba = nn.predict(X_test_scaled)
y_pred = np.argmax(y_pred_proba, axis=1)

accuracy = np.mean(y_pred == y_test)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba[:, 1])

print(f"  Accuracy: {accuracy:.4f}")
print(f"  F1-Score: {f1:.4f}")
print(f"  ROC-AUC: {auc:.4f}")
print(f"  Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Healthy', 'Disease']))

# Save model
nn.save("Backend/models/heart/model.h5")
print(f"\n✓ Model saved to Backend/models/heart/model.h5")

# Summary
print("\n" + "="*60)
print("HEART NN TRAINING COMPLETE")
print("="*60)
