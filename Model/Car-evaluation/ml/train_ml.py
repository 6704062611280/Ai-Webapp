import sys
import os

# 🔥 fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.preprocess import load_and_preprocess

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import joblib

# โหลดข้อมูล
X, X_scaled, y, scaler = load_and_preprocess()

# ---------------- DT ----------------
dt = DecisionTreeClassifier()
dt.fit(X, y)
joblib.dump(dt, "dt.pkl")
print("✅ dt.pkl saved")

# ---------------- KNN ----------------
knn = KNeighborsClassifier()
knn.fit(X_scaled, y)   # KNN ต้อง scale
joblib.dump(knn, "knn.pkl")
print("✅ knn.pkl saved")

# ---------------- SVM ----------------
svm = SVC()
svm.fit(X_scaled, y)   # SVM ต้อง scale
joblib.dump(svm, "svm.pkl")
print("✅ svm.pkl saved")