# Model Training Guide

## 📌 Quick Reference

- **Heart Disease Models**: `Model/Heart-disease/`
- **Car Evaluation Models**: `Model/Car-evaluation/`
- **Trained Models Output**: `Backend/models/`

---

## 🔄 Complete Training Workflow

### Prerequisites

1. **Python Environment Ready**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. **Install Dependencies**
```bash
cd Backend
pip install -r requirements.txt
cd ..
```

3. **Verify Datasets**
- `Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv` (exists)
- `Model/Car-evaluation/car.csv` (exists)

---

## 💓 Heart Disease Models Training

### Full Training Pipeline

```bash
# Activate environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Navigate to Heart disease directory
cd Model/Heart-disease

# Step 1: Preprocess data
python preprocess2.py

# Step 2: Train ML models (KNN, SVM, Decision Tree)
cd ml
python train_ml2.py
cd ..

# Step 3: Train Neural Network
cd nn
python train_nn2.py
cd ../..
```

### Step-by-Step Explanation

#### Step 1: Data Preprocessing (`preprocess2.py`)

**What it does**:
- Loads the CSV dataset
- Handles missing values
- Transforms categorical features
- Standardizes numerical features
- Splits into train/test sets (80/20)
- Saves preprocessed data and encoders

**Expected Output**:
```
Loading dataset...
Data shape: (12000, 16)
Preprocessing complete
Saved encoders and scalers
```

**Output Files**:
- Train/test data (in memory, used by training scripts)
- Encoders and scalers (saved for inference)

---

#### Step 2: Train ML Models (`ml/train_ml2.py`)

**What it does**:
- Trains 3 machine learning models:
  1. **Decision Tree** - Simple, interpretable
  2. **K-Nearest Neighbors (KNN)** - Distance-based
  3. **Support Vector Machine (SVM)** - Margin-based

**Expected Accuracy**:
- Decision Tree: ~98.33%
- KNN: ~96.63%
- SVM: ~97.58%

**Code Overview**:
```python
# Load preprocessed data
X_train, X_test, y_train, y_test = load_data()

# Train models
dt_model = DecisionTreeClassifier()
knn_model = KNeighborsClassifier()
svm_model = SVC()

# Train
for model in [dt_model, knn_model, svm_model]:
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

# Save models
joblib.dump(dt_model, 'models/dt_model.pkl')
```

**Output**:
- Model files saved to `Backend/models/heart/`
- Accuracy scores printed to console

---

#### Step 3: Train Neural Network (`nn/train_nn2.py`)

**What it does**:
- Creates a deep neural network using TensorFlow/Keras
- Trains on heart disease data
- Validates on test set
- Saves the trained model

**Network Architecture**:
```
Input Layer (16 neurons) 
    ↓
Hidden Layer 1 (64 neurons, ReLU)
    ↓
Hidden Layer 2 (32 neurons, ReLU)
    ↓
Hidden Layer 3 (16 neurons, ReLU)
    ↓
Output Layer (2 neurons, Softmax) → [Healthy, Heart Disease]
```

**Training Parameters**:
- **Optimizer**: Adam (learning rate = 0.001)
- **Loss Function**: Categorical Crossentropy
- **Batch Size**: 32
- **Epochs**: 100 (with Early Stopping)
- **Validation Split**: 0.2

**Expected Accuracy**: ~99.95%

**Training Output**:
```
Epoch 1/100
800/800 [==============================] - 2s 2ms/step - loss: 0.5234 - accuracy: 0.7890
Epoch 2/100
...
Model saved to: Backend/models/heart/model.h5
```

**Output Files**:
- `model.h5` - Complete trained neural network
- `training_history.json` - Training metrics (optional)

---

## 🚗 Car Evaluation Models Training

### Full Training Pipeline

```bash
# Navigate to Car evaluation directory
cd Model/Car-evaluation

# Step 1: Preprocess data
python preprocess.py

# Step 2: Train ML models
cd ml
python train_ml.py
cd ..

# Step 3: Train Neural Network
cd nn
python train_nn.py
cd ../..
```

### Step-by-Step Explanation

#### Step 1: Data Preprocessing (`preprocess.py`)

**What it does**:
- Loads car evaluation CSV (1,728 examples, 6 features)
- All features are categorical (ordinal)
- Encodes features as numbers
- Scales features
- Splits into train/test (80/20)

**Input Features**:
1. **buying** - Car price (vhigh, high, med, low)
2. **maint** - Maintenance cost (vhigh, high, med, low)
3. **doors** - Number of doors (2, 3, 4, 5)
4. **persons** - Passenger capacity (2, 4, more)
5. **lug_boot** - Trunk size (small, med, big)
6. **safety** - Safety rating (low, med, high)

**Output Classes** (4 classes):
- **unacc** - Unacceptable
- **acc** - Acceptable
- **good** - Good
- **vgood** - Very Good

---

#### Step 2: Train ML Models (`ml/train_ml.py`)

**What it does**:
- Trains 3 ML models:
  1. Decision Tree
  2. KNN
  3. SVM

**Training Code**:
```python
# Navigate encoded features
X = df[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]
y = df['class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train models
models = {
    'DecisionTree': DecisionTreeClassifier(),
    'KNN': KNeighborsClassifier(n_neighbors=5),
    'SVM': SVC()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"{name}: {accuracy:.4f}")
```

---

#### Step 3: Train Neural Network (`nn/train_nn.py`)

**Network Architecture**:
```
Input Layer (6 neurons)
    ↓
Hidden Layer 1 (32 neurons, ReLU)
    ↓
Hidden Layer 2 (16 neurons, ReLU)
    ↓
Output Layer (4 neurons, Softmax) → [unacc, acc, good, vgood]
```

**Training Parameters**:
- **Optimizer**: Adam
- **Loss**: Categorical Crossentropy
- **Epochs**: 100
- **Batch Size**: 16

**Expected Accuracy**: ~95%+

---

## 📊 Monitoring Training Progress

### Console Output to Watch

**Successful Training**:
```
Epoch 1/100: loss=0.523, accuracy=0.789
Epoch 2/100: loss=0.412, accuracy=0.845
...
Epoch 100/100: loss=0.089, accuracy=0.956
Model saved successfully!
```

### Red Flags ⚠️

| Warning | Solution |
|---------|----------|
| `loss: NaN` | Reduce learning rate |
| `Accuracy stuck at ~50%` | Check data labels encoding |
| `Out of memory` | Reduce batch size |
| `File not found` | Check data file path |

---

## 🔍 Verifying Trained Models

### Test ML Models

```python
import joblib
import numpy as np

# Load model
dt = joblib.load('Backend/models/heart/dt_model.pkl')

# Test prediction
test_input = np.array([[66, 0, 130, 200, 177, 100, 1, 0, 3, 1, 75, 7, 25, 0, 1, 1]])
prediction = dt.predict(test_input)
print(f"Prediction: {prediction}")  # Should be 1 (Heart disease)
```

### Test Neural Network

```python
from tensorflow import keras
import numpy as np

# Load model
model = keras.models.load_model('Backend/models/heart/model.h5')

# Test prediction
test_input = np.array([[66, 0, 130, 200, 177, 100, 1, 0, 3, 1, 75, 7, 25, 0, 1, 1]])
test_input = test_input.reshape(1, -1)
prediction = model.predict(test_input)
print(f"Healthy: {prediction[0][0]:.4f}, Disease: {prediction[0][1]:.4f}")
```

---

## 🐛 Troubleshooting Training

### Issue: "FileNotFoundError: No such file or directory: '...csv'"

**Solution**:
```bash
# Make sure you're in correct directory
cd Model/Heart-disease  # or Model/Car-evaluation
ls  # Verify CSV file exists
```

### Issue: "ModuleNotFoundError: No module named 'tensorflow'"

**Solution**:
```bash
pip install tensorflow keras scikit-learn pandas numpy
```

### Issue: Training very slow

**Causes & Solutions**:
- **CPU-only TensorFlow**: Install GPU version or use smaller dataset
- **Large batch size**: Reduce batch size in training script
- **Too many epochs**: Reduce epochs (set to 50 for testing)

### Issue: Model accuracy is bad (~50% for binary classification)

**Possible causes**:
1. Data preprocessing issue
2. Feature encoding incorrect
3. Bad hyperparameters
4. Imbalanced dataset

**Debug steps**:
```bash
# Check preprocessed data
python
>>> import joblib
>>> X = joblib.load('path/to/X_train.pkl')
>>> print(X.shape, X.min(), X.max())
```

---

## 🚀 Retraining with New Data

### If you have new Heart Disease data:

```bash
cd Model/Heart-disease

# 1. Replace CSV file with your data
# cp your_data.csv synthetic_heart_disease_risk_dataset-2.csv

# 2. Run full pipeline
python preprocess2.py
cd ml && python train_ml2.py && cd ..
cd nn && python train_nn2.py
```

### If you have new Car Evaluation data:

```bash
cd Model/Car-evaluation
# cp your_data.csv car.csv
python preprocess.py
cd ml && python train_ml.py && cd ..
cd nn && python train_nn.py
```

---

## 📈 Hyperparameter Tuning

### Machine Learning Models (scikit-learn)

**Decision Tree**:
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
    max_depth=10,           # Limit tree depth
    min_samples_split=5,    # Minimum samples to split
    min_samples_leaf=2      # Minimum samples per leaf
)
```

**KNN**:
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(
    n_neighbors=3,  # Try 3, 5, 7
    weights='distance'  # Weight by distance
)
```

**SVM**:
```python
from sklearn.svm import SVC
model = SVC(
    kernel='rbf',           # 'linear', 'poly', 'rbf'
    C=1.0,                  # Regularization strength
    gamma='scale'
)
```

### Neural Network (TensorFlow/Keras)

```python
model = Sequential([
    Dense(64, activation='relu', input_dim=16),
    Dropout(0.3),           # Prevent overfitting
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(2, activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.001),  # Try 0.0001, 0.01
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=16,          # Try 8, 32, 64
    validation_split=0.2,
    callbacks=[EarlyStopping(patience=10)]
)
```

---

## ✅ Checklist Before Deployment

- [ ] All models trained successfully
- [ ] Model accuracy meets requirements (>95%)
- [ ] Model files saved in `Backend/models/`
- [ ] Tested predictions with sample data
- [ ] No errors in training logs
- [ ] Verified model files are not corrupted

---

## 📝 Training Notes

**Last Successful Training**: March 2026

**Heart Disease Models**:
- Dataset: 12,000 examples
- Best NN Accuracy: 99.95%

**Car Evaluation Models**:
- Dataset: 1,728 examples
- Best Accuracy: 95%+

---

## 🔗 Related Documentation

- `SETUP.md` - Full project setup
- `LOCAL_DEVELOPMENT.md` - Running locally
- `Backend/README.md` - API documentation
- Model training scripts in `Model/` directory

---

**Happy Training!** 🤖
