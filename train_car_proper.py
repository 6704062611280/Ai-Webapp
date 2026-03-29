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
import warnings
warnings.filterwarnings('ignore')

print("\nTRAINING CAR MODELS WITH PROPER ENCODING\n")

df_car = pd.read_csv('Model/Car-evaluation/car.csv')
feature_cols = [col for col in df_car.columns if col != 'target']
X = df_car[feature_cols].copy()
y = df_car['target'].copy()

# Label encode EVERYTHING (features AND target)
label_encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

print(f"Car dataset: {X.shape}")
print(f"Classes: {target_encoder.classes_}")
print(f"Feature columns: {feature_cols}")

# Split and balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Class weights
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = {i: w for i, w in enumerate(class_weights)}

# Train models
print("\nTraining models...")

dt = DecisionTreeClassifier(max_depth=10, min_samples_split=5, random_state=42)
dt.fit(X_train_scaled, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test_scaled))
print(f"  DT: {dt_acc:.4f}")
pickle.dump(dt, open('Backend/models/car/dt.pkl', 'wb'))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
knn_acc = accuracy_score(y_test, knn.predict(X_test_scaled))
print(f"  KNN: {knn_acc:.4f}")
pickle.dump(knn, open('Backend/models/car/knn.pkl', 'wb'))

svm = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True)
svm.fit(X_train_scaled, y_train)
svm_acc = accuracy_score(y_test, svm.predict(X_test_scaled))
print(f"  SVM: {svm_acc:.4f}")
pickle.dump(svm, open('Backend/models/car/svm.pkl', 'wb'))

nn = keras.Sequential([
    layers.Input(shape=(X_train_scaled.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(16, activation='relu'),
    layers.Dense(len(np.unique(y_train)), activation='softmax')
])
nn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
nn.fit(
    X_train_scaled, y_train,
    validation_data=(X_test_scaled, y_test),
    epochs=50,
    batch_size=16,
    class_weight=class_weight_dict,
    verbose=0
)
nn_acc = nn.evaluate(X_test_scaled, y_test, verbose=0)[1]
print(f"  NN: {nn_acc:.4f}")
nn.save('Backend/models/car/model.h5')

# Save preprocessing info
pickle.dump(scaler, open('Backend/models/car/scaler.pkl', 'wb'))
pickle.dump(target_encoder, open('Backend/models/car/label_encoder.pkl', 'wb'))
pickle.dump(feature_cols, open('Backend/models/car/columns.pkl', 'wb'))
pickle.dump(label_encoders, open('Backend/models/car/feature_encoders.pkl', 'wb'))

print("\n✓ Car models saved with proper encoding!")
