import sys
import os

# 🔥 fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocess import load_and_preprocess
import tensorflow as tf

# โหลดข้อมูล
X, X_scaled, y, scaler = load_and_preprocess()

# model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# train
model.fit(X_scaled, y, epochs=10)

# save model
model.save("../../Backend/models/car/model.h5")

print("✅ model.h5 created!")