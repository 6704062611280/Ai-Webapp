import joblib

scaler = joblib.load(r'c:\Users\TarO\Desktop\Ai Webapp\Backend\models\heart\scaler.pkl')
print(f'Scaler expects {scaler.n_features_in_} features')

cols = joblib.load(r'c:\Users\TarO\Desktop\Ai Webapp\Backend\models\heart\columns.pkl')
print(f'Columns has {len(cols)} features: {cols}')
