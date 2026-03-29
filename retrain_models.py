import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.utils.class_weight import compute_class_weight
from tensorflow import keras
from tensorflow.keras import layers
import os

# Load dataset
df = pd.read_csv('Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv')
print(f"✓ Dataset shape: {df.shape}")

# Remove non-predictive columns
df = df.drop(['Risk_Level'], axis=1)  # Remove Risk_Level (text representation of target)

# Select all 17 features (excluding target: 'target')
feature_cols = [col for col in df.columns if col != 'target']
X = df[feature_cols].copy()
y = df['target'].copy()

print(f"✓ Features: {feature_cols}")
print(f"✓ Feature count: {len(feature_cols)}")

# Encode categorical columns
categorical_columns = X.select_dtypes(include=['object']).columns
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le
    print(f"  - Encoded {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"✓ Train set: {X_train.shape[0]}, Test set: {X_test.shape[0]}")

# Apply SMOTE only to training data
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
print(f"✓ After SMOTE: {X_train_balanced.shape[0]} samples")

# Fit StandardScaler ONLY on training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)

print(f"✓ Scaler fitted with {X_train_scaled.shape[1]} features")

# Save scaler
with open('Backend/models/heart/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Save column names
with open('Backend/models/heart/columns.pkl', 'wb') as f:
    pickle.dump(feature_cols, f)

# Save label encoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train_balanced)
y_test_encoded = label_encoder.transform(y_test)

with open('Backend/models/heart/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print(f"✓ Scaler, columns, and label encoder saved")

# Compute class weights
class_weights_array = compute_class_weight('balanced', classes=np.unique(y_train_encoded), y=y_train_encoded)
class_weight_dict = {i: w for i, w in enumerate(class_weights_array)}
print(f"✓ Class weights: {class_weight_dict}")

# Train models
print("\n--- Training Models ---")

# Decision Tree
dt = DecisionTreeClassifier(max_depth=10, min_samples_split=5, random_state=42)
dt.fit(X_train_scaled, y_train_encoded)
dt_acc = accuracy_score(y_test_encoded, dt.predict(X_test_scaled))
with open('Backend/models/heart/dt.pkl', 'wb') as f:
    pickle.dump(dt, f)
print(f"✓ Decision Tree: {dt_acc:.4f}")

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train_encoded)
knn_acc = accuracy_score(y_test_encoded, knn.predict(X_test_scaled))
with open('Backend/models/heart/knn.pkl', 'wb') as f:
    pickle.dump(knn, f)
print(f"✓ KNN: {knn_acc:.4f}")

# SVM
svm = SVC(kernel='rbf', C=1.0, gamma='scale')
svm.fit(X_train_scaled, y_train_encoded)
svm_acc = accuracy_score(y_test_encoded, svm.predict(X_test_scaled))
with open('Backend/models/heart/svm.pkl', 'wb') as f:
    pickle.dump(svm, f)
print(f"✓ SVM: {svm_acc:.4f}")

# Neural Network
nn_model = keras.Sequential([
    layers.Input(shape=(X_train_scaled.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(16, activation='relu'),
    layers.Dense(len(np.unique(y_train_encoded)), activation='softmax')
])

nn_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

nn_model.fit(
    X_train_scaled, y_train_encoded,
    validation_data=(X_test_scaled, y_test_encoded),
    epochs=50,
    batch_size=16,
    class_weight=class_weight_dict,
    verbose=0
)

nn_acc = nn_model.evaluate(X_test_scaled, y_test_encoded, verbose=0)[1]
nn_model.save('Backend/models/heart/model.h5')
print(f"✓ Neural Network: {nn_acc:.4f}")

print("\n✓✓✓ All models trained and saved successfully! ✓✓✓")
