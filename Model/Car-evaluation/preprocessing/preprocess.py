import os
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

def load_and_preprocess():
    # path
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "car.csv")
    file_path = os.path.abspath(file_path)

    print("Loading from:", file_path)

    df = pd.read_csv(file_path)

    # ---------------- CLEAN ----------------
    df = df.dropna()
    df.columns = df.columns.str.strip()

    print("Columns:", df.columns)

    # ---------------- SPLIT ----------------
    X = df.drop("target", axis=1)   # ✅ แก้ตรงนี้
    y = df["target"]

    # ---------------- ENCODE ----------------
    X = pd.get_dummies(X)

    print("\nAfter encode:")
    print(X.head())

    # ---------------- SCALE ----------------
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ---------------- SAVE ----------------
    save_path = os.path.join(base_path, "preprocessing")
    os.makedirs(save_path, exist_ok=True)

    pickle.dump(scaler, open(os.path.join(save_path, "scaler.pkl"), "wb"))
    pickle.dump(X.columns, open(os.path.join(save_path, "columns.pkl"), "wb"))

    print("Saved scaler.pkl and columns.pkl ✅")

    return X, X_scaled, y