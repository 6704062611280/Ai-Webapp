# Heart Disease & Car Prediction - Project Setup Guide

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Locally](#running-locally)
- [Training Models](#training-models)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

This project is a web application for predicting:
- **Heart Disease Risk** - Machine Learning & Neural Network models
- **Car Evaluation** - Classification models for car quality assessment

### Tech Stack
- **Frontend**: React + Vite + React Router
- **Backend**: Python Flask
- **ML Libraries**: TensorFlow/Keras, scikit-learn, pandas, numpy
- **Datasets**:
  - Heart Disease: 12,000 synthetic examples (16 features)
  - Car Evaluation: 1,728 examples (6 features)

---

## 📁 Project Structure

```
Ai Webapp/
├── Backend/                          # Flask backend server
│   ├── main.py                      # Main Flask application
│   ├── models/                      # Trained models directory
│   │   ├── car/
│   │   │   └── model.h5            # Car evaluation models
│   │   └── heart/
│   │       └── model.h5            # Heart disease models
│   ├── requirements.txt             # Python dependencies
│   └── README.md                    # Backend documentation
│
├── frontend-new/                    # React frontend
│   ├── src/
│   │   ├── pages/
│   │   │   ├── MLTest.jsx          # ML model testing page
│   │   │   ├── NNTest.jsx          # Neural Network testing page
│   │   │   ├── MLReport.jsx        # ML models documentation
│   │   │   └── NNReport.jsx        # NN model documentation
│   │   ├── components/
│   │   ├── App.jsx                 # Main component
│   │   └── main.jsx                # Entry point
│   ├── package.json                # Node dependencies
│   ├── vite.config.js              # Vite configuration
│   └── index.html                  # HTML template
│
├── Model/                           # Training & preprocessing scripts
│   ├── Car-evaluation/
│   │   ├── car.csv                 # Original dataset
│   │   ├── preprocess.py           # Data preprocessing
│   │   ├── ml/
│   │   │   └── train_ml.py        # Train ML models for cars
│   │   └── nn/
│   │       └── train_nn.py        # Train NN model for cars
│   │
│   └── Heart-disease/
│       ├── synthetic_heart_disease_risk_dataset-2.csv
│       ├── preprocess2.py          # Data preprocessing
│       ├── ml/
│       │   └── train_ml2.py       # Train ML models for heart
│       └── nn/
│           └── train_nn2.py       # Train NN model for heart
│
└── README.md                        # Main project documentation
```

---

## 📦 Prerequisites

### Required Software
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 16+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)

### Required Python Libraries
See `Backend/requirements.txt` and model training scripts

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd "Ai Webapp"
```

### 2. Setup Backend

#### 2.1 Create Python Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies
```bash
cd Backend
pip install -r requirements.txt
cd ..
```

### 3. Setup Frontend

#### 3.1 Install Node Dependencies
```bash
cd frontend-new
npm install
cd ..
```

---

## 🏃 Running Locally

### Option 1: Full Stack (Backend + Frontend)

#### Terminal 1 - Start Backend Server
```bash
cd Backend
python main.py
# Server runs on http://localhost:8004
```

#### Terminal 2 - Start Frontend Development Server
```bash
cd frontend-new
npm run dev
# Frontend runs on http://localhost:5173 (or displayed in terminal)
```

#### 3. Open Browser
Visit: `http://localhost:5173`

### Option 2: Backend Only (API Testing)

```bash
cd Backend
python main.py
```

API Endpoints:
- **Heart Disease Prediction**: `POST http://localhost:8004/predict/heart`
- **Car Evaluation**: `POST http://localhost:8004/predict/car`
- **Health Check**: `GET http://localhost:8004/`

### Option 3: Frontend Only (with Deployed Backend)

Update API URLs in `frontend-new/src/App.jsx` to point to deployed backend:
```javascript
const API_BASE_URL = "https://your-deployed-backend.com";
```

Then run:
```bash
cd frontend-new
npm run dev
```

---

## 🤖 Training Models

### Prerequisites for Training
- Ensure all data files are in place
- Python packages installed: `tensorflow`, `keras`, `scikit-learn`, `pandas`, `numpy`

### Heart Disease Model Training

#### Step 1: Data Preprocessing
```bash
cd "Model/Heart-disease"
python preprocess2.py
```

This creates:
- Scaled features
- Label encoders
- Train/test splits

#### Step 2: Train Machine Learning Models (KNN, SVM, Decision Tree)
```bash
cd ml
python train_ml2.py
```

Models saved to: `Backend/models/heart/`

#### Step 3: Train Neural Network Model
```bash
cd ../nn
python train_nn2.py
```

NN Model saved to: `Backend/models/heart/model.h5`

### Car Evaluation Model Training

#### Step 1: Data Preprocessing
```bash
cd "Model/Car-evaluation"
python preprocess.py
```

#### Step 2: Train Machine Learning Models
```bash
cd ml
python train_ml.py
```

#### Step 3: Train Neural Network Model
```bash
cd ../nn
python train_nn.py
```

### Complete Training Workflow
Run all training steps in sequence:
```bash
# Heart Disease Models
cd Model/Heart-disease
python preprocess2.py
cd ml && python train_ml2.py && cd ..
cd nn && python train_nn2.py && cd ../..

# Car Evaluation Models
cd Model/Car-evaluation
python preprocess.py
cd ml && python train_ml.py && cd ..
cd nn && python train_nn.py
```

---

## 📊 Model Details

### Heart Disease Models
- **Dataset**: 12,000 synthetic examples | 16 features
- **Models**:
  - Decision Tree (DT)
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Neural Network (NN) - 99.95% accuracy
- **Target**: Binary classification (Healthy / Heart disease)
- **Key Features**: Age, Gender, Cholesterol, Fasting Blood Sugar (⭐ critical)

### Car Evaluation Models
- **Dataset**: 1,728 examples | 6 categorical features
- **Models**:
  - Decision Tree
  - KNN
  - SVM
  - Neural Network
- **Target**: 4-class classification (unacc, acc, good, vgood)
- **Features**: Buying price, Maintenance cost, Doors, Capacity, Trunk size, Safety

---

## 🌐 Deployment

### Deploy Backend to Railway.app
```bash
# 1. Create Railway account and project
# 2. Connect GitHub repository
# 3. Set environment variables
# 4. Deploy using railway CLI or GitHub integration
```

### Deploy Frontend to Vercel
```bash
cd frontend-new

# 1. Build optimized version
npm run build

# 2. Deploy to Vercel
vercel
```

---

## 🔧 Troubleshooting

### Backend Issues

**Issue**: Port 8004 already in use
```bash
# Change port in Backend/main.py
app.run(port=8005, debug=True)
```

**Issue**: Module not found errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Issue**: Model files not found
```bash
# Retrain models (see Training Models section)
cd Model/Heart-disease/ml
python train_ml2.py
```

### Frontend Issues

**Issue**: API connection errors
```bash
# Check backend is running: http://localhost:8004
# Verify API_BASE_URL in App.jsx matches backend URL
```

**Issue**: Node modules conflicts
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Model Training Issues

**Issue**: Out of memory errors
```bash
# Reduce batch size in training scripts
# Reduce dataset size for testing
```

**Issue**: TensorFlow/CUDA errors
```bash
# Install CPU version of TensorFlow
pip install tensorflow-cpu
```

---

## 📝 Additional Notes

### Data Files Location
- Heart disease data: `Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv`
- Car evaluation data: `Model/Car-evaluation/car.csv`

### Model File Locations
- All trained models: `Backend/models/heart/` and `Backend/models/car/`
- Keep these files for inference without retraining

### Environment Variables
Create `.env` file in root directory if needed:
```
FLASK_ENV=development
DEBUG=True
```

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review individual README files in `Backend/`, `Model/`, `frontend-new/`
3. Check console/terminal for error messages

---

## 📄 License

[Add appropriate license here]

---

**Last Updated**: March 2026
