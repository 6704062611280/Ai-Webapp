import joblib
import pandas as pd
import numpy as np

# Disease example data
disease_data = {
    'age': 70,
    'gender': 1,  # Male
    'restingBp': 130,
    'cholesterol': 213,
    'fastingBloodSugar': 120,
    'maxHr': 148,
    'ecgResult': 1,  # Normal
    'smokingStatus': 0,  # Current
    'alcoholConsumption': 3,
    'physicalActivityLevel': 1,  # Low
    'dietQualityScore': 35,
    'sleepHours': 6,
    'bmi': 28,
    'diabetes': 1,
    'hypertension': 1,
    'familyHistory': 1,
    'riskScore': 80
}

# Load backend components
try:
    heart_scaler = joblib.load("Backend/models/heart/scaler.pkl")
    heart_columns = joblib.load("Backend/models/heart/columns.pkl")
    heart_feature_encoders = joblib.load("Backend/models/heart/feature_encoders_heart.pkl")
    dt_model = joblib.load("Backend/models/heart/dt.pkl")
    print("✓ All backend files loaded successfully")
except Exception as e:
    print(f"✗ Error loading files: {e}")
    exit(1)

# Simulate what backend does
print("\n=== BACKEND PROCESSING ===")
print(f"Input data: {disease_data}")

# Create DataFrame
df_input = pd.DataFrame([disease_data])
print(f"\nDataFrame shape before processing: {df_input.shape}")
print(f"Columns: {list(df_input.columns)}")
print(f"Values:\n{df_input}")

# Show encoders
print(f"\n=== CATEGORICAL ENCODERS ===")
for col, encoder in heart_feature_encoders.items():
    print(f"{col}: {list(encoder.classes_)}")
    if col in df_input.columns:
        print(f"  Current value: {df_input[col].values[0]}")

# Apply encoding to categorical columns
print(f"\n=== APPLYING CATEGORICAL ENCODING ===")
categorical_cols = ['gender', 'ecgResult', 'smokingStatus', 'physicalActivityLevel']
for col in categorical_cols:
    if col in df_input.columns:
        original_value = df_input[col].values[0]
        print(f"\n{col}:")
        print(f"  Original value: {original_value} (type: {type(original_value).__name__})")
        
        # Check if encoder exists
        if col in heart_feature_encoders:
            # Map integer to text first
            if col == 'gender':
                gender_map = {0: 'Female', 1: 'Male'}
                text_value = gender_map.get(original_value, original_value)
            elif col == 'ecgResult':
                ecg_map = {0: 'LVH', 1: 'Normal', 2: 'ST'}
                text_value = ecg_map.get(original_value, original_value)
            elif col == 'smokingStatus':
                smoking_map = {0: 'Current', 1: 'Former', 2: 'Never'}
                text_value = smoking_map.get(original_value, original_value)
            elif col == 'physicalActivityLevel':
                activity_map = {0: 'High', 1: 'Low', 2: 'Moderate'}
                text_value = activity_map.get(original_value, original_value)
            
            print(f"  Mapped to text: {text_value}")
            df_input.loc[0, col] = text_value
            
            # Encode using encoder
            try:
                encoded = heart_feature_encoders[col].transform([text_value])[0]
                print(f"  Encoded value: {encoded}")
                df_input.loc[0, col] = encoded
            except Exception as e:
                print(f"  ERROR encoding: {e}")
        else:
            print(f"  ERROR: No encoder for {col}")

print(f"\n=== AFTER ENCODING ===")
print(f"DataFrame:\n{df_input}")

# Reorder columns
print(f"\n=== REORDERING COLUMNS ===")
print(f"Expected columns: {heart_columns}")
print(f"Current columns: {list(df_input.columns)}")

try:
    df_input = df_input[heart_columns]
    print(f"✓ Reordered successfully")
except Exception as e:
    print(f"✗ Reorder failed: {e}")
    print(f"Available: {list(df_input.columns)}")

# Scale
print(f"\n=== SCALING ===")
print(f"Scaler expects {heart_scaler.n_features_in_} features")
print(f"DataFrame has {df_input.shape[1]} columns")

try:
    X_scaled = heart_scaler.transform(df_input)
    print(f"✓ Scaling successful")
    print(f"Scaled values:\n{X_scaled}")
except Exception as e:
    print(f"✗ Scaling failed: {e}")
    exit(1)

# Predict
print(f"\n=== PREDICTION WITH DT ===")
try:
    pred = dt_model.predict(X_scaled)
    proba = dt_model.predict_proba(X_scaled)
    print(f"Prediction: {pred[0]}")
    print(f"Classes: {dt_model.classes_}")
    print(f"Probabilities: {dict(zip(dt_model.classes_, proba[0]))}")
except Exception as e:
    print(f"✗ Prediction failed: {e}")
