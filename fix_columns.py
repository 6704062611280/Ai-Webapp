"""
Fix heart model columns.pkl to include all 17 features
"""

import pandas as pd
import joblib

df = pd.read_csv("Model/Heart-disease/synthetic_heart_disease_risk_dataset-2.csv")

# Get feature columns (exclude target columns)
feature_cols = [col for col in df.columns if col not in ['target', 'target_name', 'Risk_Level']]
print(f"Features to save: {feature_cols}")
print(f"Number of features: {len(feature_cols)}")

# Save columns.pkl
joblib.dump(feature_cols, "Backend/models/heart/columns.pkl")
print(f"\n✓ Saved columns.pkl with {len(feature_cols)} features")
