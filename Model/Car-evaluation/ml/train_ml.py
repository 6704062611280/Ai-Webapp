import sys
import os

# 🔥 fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocess import load_and_preprocess

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import joblib

# Create directories - use absolute path
save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "Backend", "models", "car"))
os.makedirs(save_dir, exist_ok=True)

# โหลดข้อมูล
X, X_scaled, y, scaler = load_and_preprocess()

# ---------------- DT ----------------
dt = DecisionTreeClassifier()
dt.fit(X, y)
joblib.dump(dt, os.path.join(save_dir, "dt.pkl"))
print("✅ dt.pkl saved")

# ---------------- KNN ----------------
knn = KNeighborsClassifier()
knn.fit(X_scaled, y)   # KNN ต้อง scale
joblib.dump(knn, os.path.join(save_dir, "knn.pkl"))
print("✅ knn.pkl saved")

# ---------------- SVM ----------------
svm = SVC(probability=True)
svm.fit(X_scaled, y)   # SVM ต้อง scale
joblib.dump(svm, os.path.join(save_dir, "svm.pkl"))
print("✅ svm.pkl saved")