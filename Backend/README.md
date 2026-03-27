# Car Evaluation – FastAPI Backend

## โครงสร้างโฟลเดอร์

Backend/
├── app.py
├── requirements.txt
├── README.md
└── models/
    ├── dt.pkl
    ├── knn.pkl
    ├── svm.pkl
    ├── scaler.pkl
    ├── columns.pkl
    ├── label_encoder.pkl   ← ✅ สำคัญ
    └── model.h5

## วิธีติดตั้งและรัน

### 1. สร้าง Virtual Environment
cd Backend
python -m venv venv

venv\Scripts\activate

### 2. ติดตั้ง
pip install -r requirements.txt

### 3. วาง Model Files
copy จาก Model/Car-evaluation/

- ml/dt.pkl
- ml/knn.pkl
- ml/svm.pkl
- preprocessing/preprocessing/scaler.pkl
- preprocessing/preprocessing/columns.pkl
- preprocessing/preprocessing/label_encoder.pkl
- nn/model.h5

### 4. รัน
uvicorn app:app --reload --port 8000

## API
GET / → health
GET /health → check models
GET /options → dropdown
POST /predict → predict

## Docs
http://localhost:8000/docs