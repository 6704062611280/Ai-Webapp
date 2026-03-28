from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import joblib
import pandas as pd
from tensorflow.keras.models import load_model

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5176", "http://127.0.0.1:5176"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= LOAD HEART =================
heart_models = {
    "knn": joblib.load("models/heart/knn.pkl"),
    "svm": joblib.load("models/heart/svm.pkl"),
    "dt": joblib.load("models/heart/dt.pkl"),
}

heart_scaler = joblib.load("models/heart/scaler.pkl")
heart_nn = load_model("models/heart/model.h5")
heart_label_encoder = joblib.load("models/heart/label_encoder.pkl")

# ================= LOAD CAR =================
car_models = {
    "knn": joblib.load("models/car/knn.pkl"),
    "svm": joblib.load("models/car/svm.pkl"),
    "dt": joblib.load("models/car/dt.pkl"),
}

car_scaler = joblib.load("models/car/scaler.pkl")
car_nn = load_model("models/car/model.h5")
car_columns = joblib.load("models/car/columns.pkl")
car_label_encoder = joblib.load("models/car/label_encoder.pkl")

# ================= INPUT =================
class HeartInput(BaseModel):
    age: float
    cholesterol: float
    resting_bp: float


class CarInput(BaseModel):
    buying: float
    maint: float
    doors: float
    persons: float
    lug_boot: float
    safety: float


# ================= HELPER =================
def process_input(scaler, features):
    data = np.array([features])
    return scaler.transform(data)

# Car label mapping
car_label_map = {
    'unacc': 'unaccept',
    'acc': 'accept',
    'good': 'good',
    'vgood': 'very good'
}

# Heart label mapping
heart_label_map = {
    '0': 'Healthy',
    '1': 'Heart disease',
    0: 'Healthy',
    1: 'Heart disease'
}


# ================= ROOT =================
@app.get("/")
def home():
    return {"message": "AI Backend Running 🚀"}


# ================= HEART =================

# 🔥 ML เลือก model ได้
@app.post("/predict/heart/ml/{model_name}")
def heart_ml(model_name: str, data: HeartInput):
    try:
        model = heart_models.get(model_name)

        if model is None:
            return {"error": f"model '{model_name}' not found"}

        features = [data.age, data.cholesterol, data.resting_bp]
        x = process_input(heart_scaler, features)

        result = model.predict(x)
        probs = model.predict_proba(x)[0]
        accuracy = float(np.max(probs)) * 100
        label = str(heart_label_encoder.inverse_transform([int(result[0])])[0])
        label = heart_label_map.get(label, label)

        return {
            "model": model_name,
            "result": label,
            "accuracy": round(accuracy, 2)
        }
    except Exception as e:
        return {"error": str(e)}


# 🔥 NN
@app.post("/predict/heart/nn")
def heart_nn_api(data: HeartInput):
    try:
        features = [data.age, data.cholesterol, data.resting_bp]
        x = process_input(heart_scaler, features)

        result = heart_nn.predict(x)
        accuracy = float(np.max(result[0])) * 100
        pred_class = int(np.argmax(result))
        label = str(heart_label_encoder.inverse_transform([pred_class])[0])
        label = heart_label_map.get(label, label)

        return {
            "model": "nn",
            "result": label,
            "accuracy": round(accuracy, 2)
        }
    except Exception as e:
        return {"error": str(e)}


# ================= CAR =================

buying_map = {1: 'vhigh', 2: 'high', 3: 'med', 4: 'low'}
maint_map = {1: 'vhigh', 2: 'high', 3: 'med', 4: 'low'}
doors_map = {2: '2', 3: '3', 4: '4', 5: '5more'}
persons_map = {2: '2', 4: '4', 5: 'more'}
lug_boot_map = {1: 'small', 2: 'med', 3: 'big'}
safety_map = {1: 'low', 2: 'med', 3: 'high'}

# 🔥 ML เลือก model ได้
@app.post("/predict/car/ml/{model_name}")
def car_ml(model_name: str, data: CarInput):
    try:
        model = car_models.get(model_name)

        if model is None:
            return {"error": f"model '{model_name}' not found"}

        df_input = pd.DataFrame([{
            'buying': buying_map[data.buying],
            'maint': maint_map[data.maint],
            'doors': doors_map[data.doors],
            'persons': persons_map[data.persons],
            'lug_boot': lug_boot_map[data.lug_boot],
            'safety': safety_map[data.safety]
        }])
        df_input = pd.get_dummies(df_input)
        df_input = df_input.reindex(columns=car_columns, fill_value=0)
        x = car_scaler.transform(df_input.values)

        result = model.predict(x)
        probs = model.predict_proba(x)[0]
        accuracy = float(np.max(probs)) * 100
        label = str(car_label_encoder.inverse_transform([int(result[0])])[0])
        label = car_label_map.get(label, label)

        return {
            "model": model_name,
            "result": label,
            "accuracy": round(accuracy, 2)
        }
    except Exception as e:
        return {"error": str(e)}


# 🔥 NN
@app.post("/predict/car/nn")
def car_nn_api(data: CarInput):
    try:
        df_input = pd.DataFrame([{
            'buying': buying_map[data.buying],
            'maint': maint_map[data.maint],
            'doors': doors_map[data.doors],
            'persons': persons_map[data.persons],
            'lug_boot': lug_boot_map[data.lug_boot],
            'safety': safety_map[data.safety]
        }])
        df_input = pd.get_dummies(df_input)
        df_input = df_input.reindex(columns=car_columns, fill_value=0)
        x = car_scaler.transform(df_input.values)

        result = car_nn.predict(x)
        accuracy = float(np.max(result[0])) * 100
        pred_class = int(np.argmax(result))
        label = str(car_label_encoder.inverse_transform([pred_class])[0])
        label = car_label_map.get(label, label)

        return {
            "model": "nn",
            "result": label,
            "accuracy": round(accuracy, 2)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)