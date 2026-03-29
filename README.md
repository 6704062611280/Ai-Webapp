# Heart Disease & Car Prediction

> A web application for predicting heart disease risk and evaluating car quality using Machine Learning and Neural Network models.

## 🚀 Quick Start

### For First-Time Users
1. **Read**: [SETUP.md](SETUP.md) - Complete project setup guide
2. **Run**: [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md) - Start coding locally in 5 minutes
3. **Train**: [MODEL_TRAINING.md](MODEL_TRAINING.md) - Train custom models

### Already Set Up?
```bash
# Terminal 1: Start Backend
cd Backend && python main.py

# Terminal 2: Start Frontend
cd frontend-new && npm run dev
```

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [SETUP.md](SETUP.md) | Complete project setup, prerequisites, installation |
| [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md) | Quick local development (5-minute setup) |
| [MODEL_TRAINING.md](MODEL_TRAINING.md) | Training ML and NN models from scratch |
| [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md) | Organizing project files & scripts |
| [Backend/README.md](Backend/README.md) | API documentation & endpoints |

---

## 🎯 What Does This App Do?

### Heart Disease Prediction
- **Input**: 16 health parameters (age, cholesterol, blood pressure, etc.)
- **Output**: Risk prediction (Healthy or Heart Disease)
- **Models**: Decision Tree, KNN, SVM, Neural Network
- **Data**: 12,000 synthetic examples

### Car Evaluation
- **Input**: 6 car features (price, maintenance, doors, capacity, trunk, safety)
- **Output**: Quality classification (unacc, acc, good, vgood)
- **Models**: Decision Tree, KNN, SVM, Neural Network
- **Data**: 1,728 examples

---

## 🛠️ Technology Stack

**Frontend**
- React 19
- Vite (build tool)
- React Router (navigation)

**Backend**
- Python Flask (API server)
- TensorFlow/Keras (neural networks)
- scikit-learn (ML models)
- pandas, numpy (data processing)

**Deployment**
- Backend: Railway.app
- Frontend: Vercel

---

## 📁 Project Structure

```
Ai Webapp/
├── Backend/              # Flask API
├── frontend-new/        # React + Vite UI
├── Model/               # Data & training scripts
├── scripts/             # Development tools (optional)
├── SETUP.md            # Setup guide
├── LOCAL_DEVELOPMENT.md # Quick start
├── MODEL_TRAINING.md   # Training guide
└── README.md           # This file
```

---

## 🔗 Key Links

- **API Base**: http://localhost:8004
- **Frontend**: http://localhost:5173
- **Kaggle (Heart Data)**: [Synthetic Heart Disease Dataset](https://www.kaggle.com/datasets/rhythmghai/synthetic-heart-disease-risk-prediction-dataset) ⚠️ (Link unavailable)
- **UCI (Car Data)**: [Car Evaluation Dataset](https://archive.ics.uci.edu/dataset/19/car+evaluation)

---

## 📊 Model Performance

| Model | Heart Disease | Car Evaluation |
|-------|---------------|----------------|
| Decision Tree | 98.33% | 96%+ |
| KNN | 96.63% | 95%+ |
| SVM | 97.58% | 94%+ |
| Neural Network | 99.95% 🥇 | 95%+ |

---

## 🚀 Getting Help

1. **Can't start the app?** → Read [SETUP.md](SETUP.md) → [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md)
2. **Want to train models?** → Read [MODEL_TRAINING.md](MODEL_TRAINING.md)
3. **API issues?** → Check [Backend/README.md](Backend/README.md)
4. **Want to clean up?** → See [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md)

---

## ✅ Checklist for New Users

- [ ] Read [SETUP.md](SETUP.md)
- [ ] Create Python virtual environment
- [ ] Install dependencies (Backend & frontend-new)
- [ ] Start Backend: `cd Backend && python main.py`
- [ ] Start Frontend: `cd frontend-new && npm run dev`
- [ ] Visit http://localhost:5173
- [ ] Test predictions (click "Load disease Example")

---

## 📝 For Project Maintainers

- Models saved in: `Backend/models/heart/` and `Backend/models/car/`
- Training scripts in: `Model/Heart-disease/` and `Model/Car-evaluation/`
- Frontend code in: `frontend-new/src/`
- API endpoints in: `Backend/main.py`

---

## 🤝 Contributing

To fork and contribute to this project:

1. Clone the repository
2. Follow setup in [SETUP.md](SETUP.md)
3. Create your feature branch
4. Test locally with [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md)
5. Train custom models with [MODEL_TRAINING.md](MODEL_TRAINING.md) if needed

---

## 📄 License

[Add your license here]

---

**Last Updated**: March 2026  
**Frontend Name**: Heart disease & Car predict  
**Status**: ✅ Active Development
