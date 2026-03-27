from fastapi import FastAPI
import joblib
import tensorflow as tf
import pandas as pd
import numpy as np

app = FastAPI()

# ---------------- LOAD MODELS ----------------
dt = joblib.load("models/dt.pkl")
knn = joblib.load("models/knn.pkl")
svm = joblib.load("models/svm.pkl")

scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")
le = joblib.load("models/label_encoder.pkl")

model = tf.keras.models.load_model("models/model.h5")

# ---------------- PREPROCESS ----------------
def preprocess_input(data):
    df = pd.DataFrame([data])

    # one-hot
    df = pd.get_dummies(df)

    # align columns
    df = df.reindex(columns=columns, fill_value=0)

    # scale
    X_scaled = scaler.transform(df)

    return df, X_scaled

# ---------------- ROUTES ----------------
@app.get("/")
def root():
    return {"message": "API running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok", "models_loaded": True}

@app.get("/options")
def options():
    return {
        "buying": ["low", "med", "high", "vhigh"],
        "maint": ["low", "med", "high", "vhigh"],
        "doors": ["2", "3", "4", "5more"],
        "persons": ["2", "4", "more"],
        "lug_boot": ["small", "med", "big"],
        "safety": ["low", "med", "high"]
    }

@app.post("/predict")
def predict(data: dict):
    df, X_scaled = preprocess_input(data)

    result = {}

    # Decision Tree
    dt_pred = dt.predict(df)[0]
    result["decision_tree"] = le.inverse_transform([dt_pred])[0]

    # KNN
    knn_pred = knn.predict(X_scaled)[0]
    result["knn"] = le.inverse_transform([knn_pred])[0]

    # SVM
    svm_pred = svm.predict(X_scaled)[0]
    result["svm"] = le.inverse_transform([svm_pred])[0]

    # Neural Network
    nn_pred = model.predict(X_scaled)
    nn_class = int(np.argmax(nn_pred))
    result["neural_network"] = le.inverse_transform([nn_class])[0]

    result["input_summary"] = data

    return result