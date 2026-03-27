import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocess2 import load_and_preprocess
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle

print("🚀 START TRAIN NN2")

# โหลดข้อมูล
X, X_scaled, y, scaler = load_and_preprocess()

# ---------------- ENCODE TARGET ----------------
le = LabelEncoder()
y = le.fit_transform(y)

# ---------------- SAVE PREPROCESS ----------------
save_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "models")
)
os.makedirs(save_dir, exist_ok=True)

print("✅ preprocessing saved")

# ---------------- MODEL ----------------
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(set(y)), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ---------------- TRAIN ----------------
model.fit(X_scaled, y, epochs=10)

# ---------------- SAVE ----------------
model.save(os.path.join(save_dir, "model.h5"))

print("✅ model.h5 created!")