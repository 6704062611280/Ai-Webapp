import joblib

encoders = joblib.load("Backend/models/heart/feature_encoders_heart.pkl")

print("Keys in feature_encoders_heart.pkl:")
for key in encoders.keys():
    print(f"  - {key}")
    if hasattr(encoders[key], 'classes_'):
        print(f"    Classes: {list(encoders[key].classes_)}")
