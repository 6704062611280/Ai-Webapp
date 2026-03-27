import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocess2 import load_and_preprocess

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import joblib
import pickle

print("🚀 START TRAIN ML2")

# ---------------- LOAD PREPROCESS ----------------
save_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "models")
)

scaler = pickle.load(open(os.path.join(save_dir, "scaler.pkl"), "rb"))
columns = pickle.load(open(os.path.join(save_dir, "columns.pkl"), "rb"))
le = pickle.load(open(os.path.join(save_dir, "label_encoder.pkl"), "rb"))

# ---------------- LOAD DATA ----------------
X, _, y, _ = load_and_preprocess()

# ensure column order (กันพังตอน feature ไม่ตรง)
X = X.reindex(columns=columns, fill_value=0)

# scale ด้วย scaler เดิม
X_scaled = scaler.transform(X)

# encode target
y = le.transform(y)

# ---------------- TRAIN ----------------

# DT
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X, y)
joblib.dump(dt, os.path.join(save_dir, "dt.pkl"))
print("✅ dt.pkl saved")

# KNN
knn = KNeighborsClassifier()
knn.fit(X_scaled, y)
joblib.dump(knn, os.path.join(save_dir, "knn.pkl"))
print("✅ knn.pkl saved")

# SVM
svm = SVC(probability=True)
svm.fit(X_scaled, y)
joblib.dump(svm, os.path.join(save_dir, "svm.pkl"))
print("✅ svm.pkl saved")

print("🎉 ALL MODELS TRAINED SUCCESSFULLY")