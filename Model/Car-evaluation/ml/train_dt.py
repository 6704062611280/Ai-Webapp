import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.preprocess import load_and_preprocess
from sklearn.tree import DecisionTreeClassifier
import pickle

X, X_scaled, y = load_and_preprocess()

model = DecisionTreeClassifier()
model.fit(X, y)  # ❗ ไม่ใช้ scaled

pickle.dump(model, open("dt.pkl", "wb"))

print("Decision Tree saved ✅")