import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, f1_score, roc_auc_score
from imblearn.over_sampling import SMOTE
from sklearn.utils.class_weight import compute_class_weight
from tensorflow import keras
from tensorflow.keras import layers
import warnings
warnings.filterwarnings('ignore')

print("\n" + "="*60)
print("RETRAIN HEART MODELS WITH IMPROVED DISEASE DETECTION")
print("="*60 + "\n")

df_heart = pd.read_csv('Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv')
feature_cols = [col for col in df_heart.columns if col not in ['target', 'Risk_Score', 'Risk_Level']]
X = df_heart[feature_cols].copy()
y = df_heart['target'].copy()

print(f"Dataset: {X.shape}")
print(f"Target distribution:\n{y.value_counts()}")

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
print(f"\nClasses: {target_encoder.classes_}")
print(f"Class 0 (Healthy): {(y_encoded == 0).sum()}, Class 1 (Disease): {(y_encoded == 1).sum()}")

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

print(f"\nBefore SMOTE:")
print(f"  Train: Class 0={sum(y_train==0)}, Class 1={sum(y_train==1)}")

# Apply SMOTE with 1.0 sampling (full balance) for disease detection
smote = SMOTE(k_neighbors=5, random_state=42, sampling_strategy=1.0)
X_train, y_train = smote.fit_resample(X_train, y_train)

print(f"After SMOTE:")
print(f"  Train: Class 0={sum(y_train==0)}, Class 1={sum(y_train==1)}")

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Test set: Class 0={sum(y_test==0)}, Class 1={sum(y_test==1)}")

# ====== AGGRESSIVE CLASS WEIGHTS FOR DISEASE DETECTION ======
# Penalize false negatives (missing disease) much more
disease_count = (y_train == 1).sum()
healthy_count = (y_train == 0).sum()
weight_disease = healthy_count / (2 * disease_count)  # Much higher weight for disease class
weight_healthy = 1.0

class_weight_dict = {0: weight_healthy, 1: weight_disease}
print(f"\nClass weights (aggressive for disease detection):")
print(f"  Healthy: {weight_healthy:.4f}")
print(f"  Disease: {weight_disease:.4f}")

# ================== TRAIN MODELS ==================
print("\n" + "="*60)
print("TRAINING MODELS")
print("="*60)

# ===== Decision Tree =====
print("\n1. DECISION TREE")
dt = DecisionTreeClassifier(
    max_depth=12,
    min_samples_split=8,
    min_samples_leaf=3,
    class_weight='balanced',
    random_state=42
)
dt.fit(X_train_scaled, y_train)
dt_pred = dt.predict(X_test_scaled)
dt_acc = accuracy_score(y_test, dt_pred)
dt_f1 = f1_score(y_test, dt_pred)
dt_auc = roc_auc_score(y_test, dt.predict_proba(X_test_scaled)[:, 1])

print(f"  Accuracy: {dt_acc:.4f}")
print(f"  F1-Score: {dt_f1:.4f}")
print(f"  ROC-AUC: {dt_auc:.4f}")
print(f"  Classification Report:")
print(classification_report(y_test, dt_pred, target_names=['Healthy', 'Disease']))
pickle.dump(dt, open('Backend/models/heart/dt.pkl', 'wb'))

# ===== KNN =====
print("\n2. K-NEAREST NEIGHBORS")
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train_scaled, y_train)
knn_pred = knn.predict(X_test_scaled)
knn_acc = accuracy_score(y_test, knn_pred)
knn_f1 = f1_score(y_test, knn_pred)
knn_proba = knn.predict_proba(X_test_scaled)
knn_auc = roc_auc_score(y_test, knn_proba[:, 1]) if len(np.unique(knn_proba[:, 1])) > 1 else 0

print(f"  Accuracy: {knn_acc:.4f}")
print(f"  F1-Score: {knn_f1:.4f}")
print(f"  ROC-AUC: {knn_auc:.4f}")
print(f"  Classification Report:")
print(classification_report(y_test, knn_pred, target_names=['Healthy', 'Disease']))
pickle.dump(knn, open('Backend/models/heart/knn.pkl', 'wb'))

# ===== SVM =====
print("\n3. SUPPORT VECTOR MACHINE")
svm = SVC(
    kernel='rbf',
    C=100.0,  # Increased penalty for misclassification
    gamma=0.001,  # Smaller gamma for softer boundaries
    class_weight=class_weight_dict,
    probability=True,
    random_state=42
)
svm.fit(X_train_scaled, y_train)
svm_pred = svm.predict(X_test_scaled)
svm_acc = accuracy_score(y_test, svm_pred)
svm_f1 = f1_score(y_test, svm_pred)
svm_auc = roc_auc_score(y_test, svm.predict_proba(X_test_scaled)[:, 1])

print(f"  Accuracy: {svm_acc:.4f}")
print(f"  F1-Score: {svm_f1:.4f}")
print(f"  ROC-AUC: {svm_auc:.4f}")
print(f"  Classification Report:")
print(classification_report(y_test, svm_pred, target_names=['Healthy', 'Disease']))
pickle.dump(svm, open('Backend/models/heart/svm.pkl', 'wb'))

# ===== NEURAL NETWORK =====
print("\n4. NEURAL NETWORK")

# Better architecture for disease detection
nn = keras.Sequential([
    layers.Input(shape=(X_train_scaled.shape[1],)),
    
    layers.Dense(256, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    
    layers.Dense(128, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.4),
    
    layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
    layers.Dropout(0.2),
    
    layers.Dense(2, activation='softmax')
])

nn.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0005),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Early stopping with patience
early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=20,
    restore_best_weights=True,
    verbose=0
)

# Train with high class weight for disease
history = nn.fit(
    X_train_scaled, y_train,
    validation_data=(X_test_scaled, y_test),
    epochs=150,
    batch_size=16,
    class_weight=class_weight_dict,
    callbacks=[early_stopping],
    verbose=0
)

nn_pred = np.argmax(nn.predict(X_test_scaled, verbose=0), axis=1)
nn_acc = accuracy_score(y_test, nn_pred)
nn_f1 = f1_score(y_test, nn_pred)
nn_proba = nn.predict(X_test_scaled, verbose=0)[:, 1]
nn_auc = roc_auc_score(y_test, nn_proba)

print(f"  Accuracy: {nn_acc:.4f}")
print(f"  F1-Score: {nn_f1:.4f}")
print(f"  ROC-AUC: {nn_auc:.4f}")
print(f"  Classification Report:")
print(classification_report(y_test, nn_pred, target_names=['Healthy', 'Disease']))

nn.save('Backend/models/heart/model.h5')

# Save preprocessing
pickle.dump(scaler, open('Backend/models/heart/scaler.pkl', 'wb'))
pickle.dump(target_encoder, open('Backend/models/heart/label_encoder.pkl', 'wb'))
pickle.dump(feature_cols, open('Backend/models/heart/columns.pkl', 'wb'))
pickle.dump(label_encoders, open('Backend/models/heart/feature_encoders.pkl', 'wb'))

print("\n" + "="*60)
print("✓ HEART MODELS RETRAINED WITH IMPROVED DISEASE DETECTION")
print("="*60)
