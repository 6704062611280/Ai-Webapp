import { useState } from "react";

function MLTest() {
  const [heartResult, setHeartResult] = useState(null);
  const [carResult, setCarResult] = useState(null);

  // 🔥 เลือก model (เปลี่ยนได้: knn / svm / dt)
  const model = "knn";

  const predictHeart = async () => {
    const res = await fetch(`http://127.0.0.1:8000/predict/heart/ml/${model}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        age: 45,
        cholesterol: 200,
        blood_pressure: 120
      })
    });

    const data = await res.json();
    setHeartResult(data.result);
  };

  const predictCar = async () => {
    const res = await fetch(`http://127.0.0.1:8000/predict/car/ml/${model}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        buying: 2,
        maint: 2,
        doors: 4,
        persons: 4,
        lug_boot: 2,
        safety: 3
      })
    });

    const data = await res.json();
    setCarResult(data.result);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>ML Test</h1>

      <h2>Heart Prediction ({model})</h2>
      <button onClick={predictHeart}>Predict Heart</button>
      {heartResult !== null && <p>Result: {heartResult}</p>}

      <h2 style={{ marginTop: "30px" }}>
        Car Prediction ({model})
      </h2>
      <button onClick={predictCar}>Predict Car</button>
      {carResult && <p>Result: {carResult}</p>}
    </div>
  );
}

export default MLTest;