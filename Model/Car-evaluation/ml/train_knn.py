import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.preprocess import load_and_preprocess
from sklearn.neighbors import KNeighborsClassifier
import pickle

X, X_scaled, y = load_and_preprocess()

model = KNeighborsClassifier()
model.fit(X_scaled, y)

pickle.dump(model, open("knn.pkl", "wb"))

print("KNN saved ✅")