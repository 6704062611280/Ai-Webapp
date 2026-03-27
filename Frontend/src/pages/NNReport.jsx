export default function NNReport() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Neural Network Model</h1>

      <h2>1. Data Preparation</h2>
      <p>
        ใช้ dataset เดียวกับ ML โดยผ่านการ encoding และ scaling ก่อนนำเข้า model
      </p>

      <h2>2. Architecture</h2>
      <ul>
        <li>Input Layer</li>
        <li>Dense Layer (64 neurons)</li>
        <li>Dense Layer (32 neurons)</li>
        <li>Output Layer (Softmax)</li>
      </ul>

      <h2>3. Training</h2>
      <p>
        ใช้ optimizer = Adam และ loss = sparse_categorical_crossentropy
      </p>

      <h2>4. Reference</h2>
      <p>TensorFlow / Keras Documentation</p>
    </div>
  );
}