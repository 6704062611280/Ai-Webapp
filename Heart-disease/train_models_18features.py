import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from imblearn.over_sampling import SMOTE
import joblib
import os

# Load dataset
df = pd.read_csv('synthetic_heart_disease_risk_dataset-2.csv')

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nValue counts for target:")
print(df.iloc[:, -1].value_counts())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Select features (18 total) - adjust based on actual column names
feature_cols = [col for col in df.columns if col != df.columns[-1]]  # All except last (target)
target_col = df.columns[-1]

print(f"\nUsing {len(feature_cols)} features")

X = df[feature_cols].values
y = df[target_col].values

# Encode target if categorical
le = LabelEncoder()
y_encoded = le.fit_transform(y)

print(f"Classes: {le.classes_}")
print(f"Class distribution before SMOTE: {np.bincount(y_encoded)}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

# Apply SMOTE for balancing
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

print(f"\nClass distribution after SMOTE: {np.bincount(y_train_smote)}")

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_smote)
X_test_scaled = scaler.transform(X_test)

# Calculate class weights
from sklearn.utils.class_weight import compute_class_weight
class_weights = compute_class_weight('balanced', classes=np.unique(y_train_smote), y=y_train_smote)
class_weight_dict = {i: w for i, w in enumerate(class_weights)}
print(f"\nClass weights: {class_weight_dict}")

# Decision Tree
print("\n=== Training Decision Tree ===")
dt = DecisionTreeClassifier(max_depth=10, min_samples_split=5, random_state=42)
dt.fit(X_train_scaled, y_train_smote)
dt_score = dt.score(X_test_scaled, y_test)
print(f"Decision Tree Accuracy: {dt_score:.4f}")

# KNN
print("\n=== Training KNN ===")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train_smote)
knn_score = knn.score(X_test_scaled, y_test)
print(f"KNN Accuracy: {knn_score:.4f}")

# SVM
print("\n=== Training SVM ===")
svm = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True)
svm.fit(X_train_scaled, y_train_smote)
svm_score = svm.score(X_test_scaled, y_test)
print(f"SVM Accuracy: {svm_score:.4f}")

# Neural Network
print("\n=== Training Neural Network ===")
nn = Sequential([
    Dense(64, activation='relu', input_shape=(len(feature_cols),)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(len(le.classes_), activation='softmax')
])

nn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

y_train_cat = to_categorical(y_train_smote, num_classes=len(le.classes_))
y_test_cat = to_categorical(y_test, num_classes=len(le.classes_))

history = nn.fit(
    X_train_scaled, y_train_cat,
    epochs=50,
    batch_size=16,
    class_weight=class_weight_dict,
    validation_data=(X_test_scaled, y_test_cat),
    verbose=1
)

nn_score = nn.evaluate(X_test_scaled, y_test_cat)[1]
print(f"\nNeural Network Accuracy: {nn_score:.4f}")

# Save models
os.makedirs('../Backend/models/heart', exist_ok=True)

joblib.dump(dt, '../Backend/models/heart/dt.pkl')
joblib.dump(knn, '../Backend/models/heart/knn.pkl')
joblib.dump(svm, '../Backend/models/heart/svm.pkl')
joblib.dump(scaler, '../Backend/models/heart/scaler.pkl')
joblib.dump(le, '../Backend/models/heart/label_encoder.pkl')
joblib.dump(feature_cols, '../Backend/models/heart/columns.pkl')

nn.save('../Backend/models/heart/model.h5')

print("\n✅ All models saved successfully!")
print("\nModel Summary:")
print(f"Decision Tree: {dt_score:.2%}")
print(f"KNN: {knn_score:.2%}")
print(f"SVM: {svm_score:.2%}")
print(f"Neural Network: {nn_score:.2%}")
