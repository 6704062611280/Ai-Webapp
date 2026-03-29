import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

print("Checking Heart Dataset and Model")

# Load dataset
df = pd.read_csv('Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv')
print(f"\nDataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"\nTarget distribution:\n{df['Risk_Score'].value_counts()}")
print(f"\nRisk_Score min: {df['Risk_Score'].min()}, max: {df['Risk_Score'].max()}")

# Check if classes are already encoded in Risk_Score
if df['Risk_Score'].max() <= 1:
    print("\nRisk_Score is 0-1 range (probably already binary or ratio)")
    # Convert to binary: 0.5 threshold for Healthy vs Disease
    y = (df['Risk_Score'] > 0.5).astype(int)
    print(f"Binary distribution (>0.5): {np.unique(y, return_counts=True)}")
else:
    print("\nRisk_Score is in larger range, need to bin it")
    
# Load saved label encoder
try:
    le = pickle.load(open('Backend/models/heart/label_encoder.pkl', 'rb'))
    print(f"\nLabel Encoder classes: {le.classes_}")
except:
    print("Could not load label encoder")

# Load NN model and check its architecture
try:
    nn = load_model('Backend/models/heart/model.h5')
    print(f"\nNN Model summary:")
    nn.summary()
except Exception as e:
    print(f"Could not load model: {e}")
