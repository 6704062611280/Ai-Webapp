import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.utils.class_weight import compute_class_weight
from tensorflow import keras
from tensorflow.keras import layers
import warnings
warnings.filterwarnings('ignore')

print("\nRETRAINING HEART MODELS WITH BETTER IMBALANCE HANDLING\n")

df_heart = pd.read_csv('Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv')
feature_cols = [col for col in df_heart.columns if col not in ['target', 'Risk_Score', 'Risk_Level']]
X = df_heart[feature_cols].copy()
y = df_heart['target'].copy()

print(f"Heart dataset: {X.shape}")
print(f"Target distribution: {y.value_counts().to_dict()}")

# Label encode categorical columns
label_encoders = {}
for col in X.columns:
    if X[col].dtype == 'object':
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        label_encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)
print(f"Classes: {target_encoder.classes_}")
print(f"Class 0 (Healthy): {(y_encoded == 0).sum()}, Class 1 (Disease): {(y_encoded == 1).sum()}")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

print(f"\nBefore SMOTE - Train: Class 0={sum(y_train==0)}, Class 1={sum(y_train==1)}")

# Apply SMOTE with higher k_neighbors for better balancing
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=0.8)  # Balance to 80% of majority
X_train, y_train = smote.fit_resample(X_train, y_train)

print(f"After SMOTE - Train: Class 0={sum(y_train==0)}, Class 1={sum(y_train==1)}")

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Test set: Class 0={sum(y_test==0)}, Class 1={sum(y_test==1)}")

# Compute class weights
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = {i: w for i, w in enumerate(class_weights)}
print(f"Class weights: {class_weight_dict}")

# ================== TRAIN MODELS ==================
print("\nTraining models...")

# Decision Tree
dt = DecisionTreeClassifier(max_depth=15, min_samples_split=5, min_samples_leaf=2, random_state=42)
dt.fit(X_train_scaled, y_train)
dt_pred = dt.predict(X_test_scaled)
dt_acc = accuracy_score(y_test, dt_pred)
print(f"\n  DT: {dt_acc:.4f}")
print(f"    Train: {accuracy_score(y_train, dt.predict(X_train_scaled)):.4f}")
print(f"    Class report:\n{classification_report(y_test, dt_pred, target_names=['Healthy', 'Disease'])}")
pickle.dump(dt, open('Backend/models/heart/dt.pkl', 'wb'))

# KNN
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train_scaled, y_train)
knn_pred = knn.predict(X_test_scaled)
knn_acc = accuracy_score(y_test, knn_pred)
print(f"\n  KNN: {knn_acc:.4f}")
print(f"    Train: {accuracy_score(y_train, knn.predict(X_train_scaled)):.4f}")
print(f"    Class report:\n{classification_report(y_test, knn_pred, target_names=['Healthy', 'Disease'])}")
pickle.dump(knn, open('Backend/models/heart/knn.pkl', 'wb'))

# SVM
svm = SVC(kernel='rbf', C=10.0, gamma='scale', probability=True, class_weight='balanced')
svm.fit(X_train_scaled, y_train)
svm_pred = svm.predict(X_test_scaled)
svm_acc = accuracy_score(y_test, svm_pred)
print(f"\n  SVM: {svm_acc:.4f}")
print(f"    Train: {accuracy_score(y_train, svm.predict(X_train_scaled)):.4f}")
print(f"    Class report:\n{classification_report(y_test, svm_pred, target_names=['Healthy', 'Disease'])}")
pickle.dump(svm, open('Backend/models/heart/svm.pkl', 'wb'))

# ================== NEURAL NETWORK ==================
print("\n  NN: Training...")

# Better architecture with deeper network
nn = keras.Sequential([
    layers.Input(shape=(X_train_scaled.shape[1],)),
    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.4),
    
    layers.Dense(64, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(32, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.2),
    
    layers.Dense(16, activation='relu'),
    layers.Dense(2, activation='softmax')
])

nn.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train with more epochs and early stopping
early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

history = nn.fit(
    X_train_scaled, y_train,
    validation_data=(X_test_scaled, y_test),
    epochs=100,
    batch_size=32,
    class_weight=class_weight_dict,
    callbacks=[early_stopping],
    verbose=0
)

nn_pred = np.argmax(nn.predict(X_test_scaled, verbose=0), axis=1)
nn_acc = accuracy_score(y_test, nn_pred)
print(f"    Final accuracy: {nn_acc:.4f}")
print(f"    Train: {accuracy_score(y_train, np.argmax(nn.predict(X_train_scaled, verbose=0), axis=1)):.4f}")
print(f"    Class report:\n{classification_report(y_test, nn_pred, target_names=['Healthy', 'Disease'])}")

nn.save('Backend/models/heart/model.h5')

# Save preprocessing
pickle.dump(scaler, open('Backend/models/heart/scaler.pkl', 'wb'))
pickle.dump(target_encoder, open('Backend/models/heart/label_encoder.pkl', 'wb'))
pickle.dump(feature_cols, open('Backend/models/heart/columns.pkl', 'wb'))
pickle.dump(label_encoders, open('Backend/models/heart/feature_encoders.pkl', 'wb'))

print("\n✓ Heart models retrained with better handling!")
