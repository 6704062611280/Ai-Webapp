import os
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess():
    base_path = os.path.dirname(__file__)

    file_path = os.path.join(base_path, "synthetic_heart_disease_risk_dataset-2.csv")
    file_path = os.path.abspath(file_path)

    print("Loading from:", file_path)

    df = pd.read_csv(file_path)

    # CLEAN
    df = df.dropna()
    df.columns = df.columns.str.strip()

    # SPLIT
    X = df.drop("target", axis=1)
    y = df["target"]

    # ENCODE
    X = pd.get_dummies(X)
    X = X.astype(float)

    # SCALE
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X, X_scaled, y, scaler


# 🔥 เพิ่ม function นี้
def save_preprocess():
    print("🚀 SAVE PREPROCESS (ONCE)")

    X, X_scaled, y, scaler = load_and_preprocess()

    # encode target
    le = LabelEncoder()
    y = le.fit_transform(y)

    save_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "models")
)
    os.makedirs(save_dir, exist_ok=True)

    pickle.dump(scaler, open(os.path.join(save_dir, "scaler.pkl"), "wb"))
    pickle.dump(X.columns, open(os.path.join(save_dir, "columns.pkl"), "wb"))
    pickle.dump(le, open(os.path.join(save_dir, "label_encoder.pkl"), "wb"))

    print("✅ preprocess saved")


# 🔥 ทำให้รันตรงๆ ได้
if __name__ == "__main__":
    save_preprocess()