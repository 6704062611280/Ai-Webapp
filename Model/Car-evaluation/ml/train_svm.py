import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.preprocess import load_and_preprocess
from sklearn.svm import SVC
import pickle

X, X_scaled, y = load_and_preprocess()

model = SVC(probability=True)
model.fit(X_scaled, y)

pickle.dump(model, open("svm.pkl", "wb"))

print("SVM saved ✅")