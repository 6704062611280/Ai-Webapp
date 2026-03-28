import os
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "car.csv")
    file_path = os.path.abspath(file_path)

    print("Loading from:", file_path)

    df = pd.read_csv(file_path)

    # ---------------- CLEAN ----------------
    original_rows = len(df)
    df = df.dropna()
    print(f"Dropped {original_rows - len(df)} rows due to missing values")
    df.columns = df.columns.str.strip()

    print("Columns:", df.columns)

    # ---------------- SPLIT ----------------
    X = df[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]
    y = df["target"]

    # ---------------- ENCODE X ----------------
    X = pd.get_dummies(X)

    print("\nAfter encode:")
    print(X.head())

    # ---------------- ENCODE y 🔥 ----------------
    le = LabelEncoder()
    y = le.fit_transform(y)

    # ---------------- SCALE ----------------
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ---------------- SAVE ----------------
    save_path = os.path.join(base_path, "..", "..", "Backend", "models", "car")
    os.makedirs(save_path, exist_ok=True)

    # save ทุกอย่างที่ต้องใช้ตอน predict
    pickle.dump(scaler, open(os.path.join(save_path, "scaler.pkl"), "wb"))
    pickle.dump(X.columns, open(os.path.join(save_path, "columns.pkl"), "wb"))
    pickle.dump(le, open(os.path.join(save_path, "label_encoder.pkl"), "wb"))

    print("Saved scaler.pkl, columns.pkl, label_encoder.pkl ✅")

    # ---------------- RETURN ----------------
    return X, X_scaled, y, scaler