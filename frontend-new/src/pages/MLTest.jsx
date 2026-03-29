import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "https://ai-webapp-production.up.railway.app";

function MLTest() {
  const [heartInputs, setHeartInputs] = useState({
    age: 45,
    cholesterol: 200,
    restingBp: 120,
    maxHr: 150,
    oldpeak: 0,
    riskScore: 25,
    fastingBloodSugar: 100,
    stSlope: 2,
    stSegment: 1,
    numMajorVessels: 0,
    exerciseInducedAngina: 0,
    smoking: 2,
    diabetic: 0,
    familyHistory: 0,
    sedentaryMinutes: 180,
    sleepDuration: 7,
    bmi: 24,
    alcoholConsumption: 0
  });

  const [carInputs, setCarInputs] = useState({
    buying: 2,
    maint: 2,
    doors: 4,
    persons: 4,
    lug_boot: 2,
    safety: 3
  });

  const [heartResults, setHeartResults] = useState({});
  const [carResults, setCarResults] = useState({});
  const [heartError, setHeartError] = useState(null);
  const [carError, setCarError] = useState(null);

  const models = ["knn", "svm", "dt"];

  // Heart Disease Example Presets
  const healthyExample = () => {
    setHeartInputs({
      age: 45,
      cholesterol: 180,
      restingBp: 120,
      maxHr: 150,
      oldpeak: 0,
      riskScore: 25,
      fastingBloodSugar: 100,
      stSlope: 2,
      stSegment: 1,
      numMajorVessels: 0,
      exerciseInducedAngina: 0,
      smoking: 2,
      diabetic: 0,
      familyHistory: 0,
      sedentaryMinutes: 180,
      sleepDuration: 7,
      bmi: 24,
      alcoholConsumption: 0
    });
  };

  const diseaseExample = () => {
    setHeartInputs({
      age: 60,
      cholesterol: 280,
      restingBp: 160,
      maxHr: 100,
      oldpeak: 2.5,
      riskScore: 72,
      fastingBloodSugar: 150,
      stSlope: 0,
      stSegment: 0,
      numMajorVessels: 2,
      exerciseInducedAngina: 1,
      smoking: 1,
      diabetic: 1,
      familyHistory: 1,
      sedentaryMinutes: 480,
      sleepDuration: 5,
      bmi: 28,
      alcoholConsumption: 2
    });
  };

  const moderateExample = () => {
    setHeartInputs({
      age: 50,
      cholesterol: 200,
      restingBp: 130,
      maxHr: 120,
      oldpeak: 1,
      riskScore: 55,
      fastingBloodSugar: 105,
      stSlope: 1,
      stSegment: 1,
      numMajorVessels: 1,
      exerciseInducedAngina: 0,
      smoking: 0,
      diabetic: 0,
      familyHistory: 1,
      sedentaryMinutes: 300,
      sleepDuration: 6,
      bmi: 26,
      alcoholConsumption: 1
    });
  };

  const predictHeart = async () => {
    setHeartError(null);
    const results = {};
    try {
      for (const model of models) {
        const res = await fetch(`${API_URL}/predict/heart/ml/${model}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(heartInputs)
        });
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        const data = await res.json();
        console.log(`Heart ${model} response:`, data);
        if (data.error) {
          throw new Error(data.error);
        }
        results[model] = data.result;
        results[`${model}Acc`] = data.accuracy;
      }
      setHeartResults(results);
    } catch (error) {
      setHeartError(error.message);
    }
  };

  const predictCar = async () => {
    setCarError(null);
    const results = {};
    try {
      for (const model of models) {
        const res = await fetch(`${API_URL}/predict/car/ml/${model}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(carInputs)
        });
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        const data = await res.json();
        console.log(`Car ${model} response:`, data);
        if (data.error) {
          throw new Error(data.error);
        }
        results[model] = data.result;
        results[`${model}Acc`] = data.accuracy;
      }
      setCarResults(results);
    } catch (error) {
      setCarError(error.message);
    }
  };

  const containerStyle = {
    width: "100%",
    margin: "0 auto",
    padding: "30px 20px",
    backgroundColor: "#f8f9fa",
    minHeight: "100vh"
  };

  const cardStyle = {
    backgroundColor: "white",
    borderRadius: "10px",
    padding: "25px",
    marginBottom: "30px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    border: "1px solid #e0e0e0"
  };

  const inputContainerStyle = {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
    gap: "15px",
    marginBottom: "20px"
  };

  const presetButtonContainerStyle = {
    display: "flex",
    gap: "10px",
    marginBottom: "20px",
    flexWrap: "wrap"
  };

  const labelStyle = {
    display: "flex",
    flexDirection: "column",
    fontSize: "13px",
    fontWeight: "500",
    color: "#333"
  };

  const inputStyle = {
    padding: "8px",
    marginTop: "4px",
    border: "1px solid #ddd",
    borderRadius: "4px",
    fontSize: "13px"
  };

  const buttonStyle = {
    padding: "12px 28px",
    fontSize: "16px",
    fontWeight: "600",
    backgroundColor: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    marginTop: "10px",
    transition: "background-color 0.3s"
  };

  const presetButtonStyle = {
    padding: "8px 16px",
    fontSize: "14px",
    fontWeight: "500",
    color: "white",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
    transition: "background-color 0.3s"
  };

  const resultCardStyle = {
    backgroundColor: "#f0f6ff",
    border: "2px solid #007bff",
    borderRadius: "8px",
    padding: "20px",
    marginTop: "20px"
  };

  const resultTableStyle = {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "10px"
  };

  const resultRowStyle = {
    borderBottom: "1px solid #e0e0e0"
  };

  const resultCellStyle = {
    padding: "12px",
    textAlign: "left"
  };

  const errorStyle = {
    padding: "15px",
    backgroundColor: "#f8d7da",
    color: "#721c24",
    border: "1px solid #f5c6cb",
    borderRadius: "5px",
    marginTop: "15px"
  };

  return (
    <div style={containerStyle}>
      <h1 style={{
        textAlign: "center",
        color: "#333",
        marginBottom: "40px",
        fontSize: "36px",
        fontWeight: "600"
      }}>
        🤖 Machine Learning (KNN, SVM, Decision Tree) Prediction
      </h1>

      {/* Heart Dataset */}
      <div style={cardStyle}>
        <h2 style={{ color: "#dc3545", marginTop: 0, borderBottom: "2px solid #dc3545", paddingBottom: "10px" }}>
          ❤️ Heart Disease Prediction (18 Features)
        </h2>

        {/* Example Presets */}
        <div style={presetButtonContainerStyle}>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#28a745"}}
            onClick={healthyExample}
          >
            📊 Load Healthy Example
          </button>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#dc3545"}}
            onClick={diseaseExample}
          >
            ⚠️ Load Disease Example
          </button>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#ffc107", color: "#333"}}
            onClick={moderateExample}
          >
            📈 Load Moderate Example
          </button>
        </div>

        {/* Input Fields - All 18 Features */}
        <div style={inputContainerStyle}>
          <label style={labelStyle}>Age <input type="number" value={heartInputs.age} onChange={(e) => setHeartInputs({...heartInputs, age: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Cholesterol (mg/dL) <input type="number" value={heartInputs.cholesterol} onChange={(e) => setHeartInputs({...heartInputs, cholesterol: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Resting BP (mmHg) <input type="number" value={heartInputs.restingBp} onChange={(e) => setHeartInputs({...heartInputs, restingBp: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Max HR (bpm) <input type="number" value={heartInputs.maxHr} onChange={(e) => setHeartInputs({...heartInputs, maxHr: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Oldpeak <input type="number" step="0.1" value={heartInputs.oldpeak} onChange={(e) => setHeartInputs({...heartInputs, oldpeak: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Risk Score (0-100) <input type="number" value={heartInputs.riskScore} onChange={(e) => setHeartInputs({...heartInputs, riskScore: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Fasting Blood Sugar (mg/dL) <input type="number" value={heartInputs.fastingBloodSugar} onChange={(e) => setHeartInputs({...heartInputs, fastingBloodSugar: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>ST Slope (0-2) <input type="number" value={heartInputs.stSlope} onChange={(e) => setHeartInputs({...heartInputs, stSlope: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>ST Segment (0-1) <input type="number" value={heartInputs.stSegment} onChange={(e) => setHeartInputs({...heartInputs, stSegment: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Num Major Vessels (0-4) <input type="number" value={heartInputs.numMajorVessels} onChange={(e) => setHeartInputs({...heartInputs, numMajorVessels: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Exercise Angina (0-1) <input type="number" value={heartInputs.exerciseInducedAngina} onChange={(e) => setHeartInputs({...heartInputs, exerciseInducedAngina: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Smoking (0-2) <input type="number" value={heartInputs.smoking} onChange={(e) => setHeartInputs({...heartInputs, smoking: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Diabetic (0-1) <input type="number" value={heartInputs.diabetic} onChange={(e) => setHeartInputs({...heartInputs, diabetic: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Family History (0-1) <input type="number" value={heartInputs.familyHistory} onChange={(e) => setHeartInputs({...heartInputs, familyHistory: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Sedentary Minutes <input type="number" value={heartInputs.sedentaryMinutes} onChange={(e) => setHeartInputs({...heartInputs, sedentaryMinutes: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Sleep Duration (hours) <input type="number" step="0.5" value={heartInputs.sleepDuration} onChange={(e) => setHeartInputs({...heartInputs, sleepDuration: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>BMI <input type="number" step="0.1" value={heartInputs.bmi} onChange={(e) => setHeartInputs({...heartInputs, bmi: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Alcohol (units/week) <input type="number" value={heartInputs.alcoholConsumption} onChange={(e) => setHeartInputs({...heartInputs, alcoholConsumption: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
        </div>

        <button style={buttonStyle} onClick={predictHeart}>🔮 Predict Heart Disease</button>

        {heartError && <div style={errorStyle}>{heartError}</div>}
        {Object.keys(heartResults).length > 0 && (
          <div style={resultCardStyle}>
            <h3 style={{ marginTop: 0, color: "#dc3545" }}>Results</h3>
            <table style={resultTableStyle}>
              <tbody>
                {models.map((model) => (
                  <tr key={model} style={resultRowStyle}>
                    <td style={{...resultCellStyle, fontWeight: "600"}}>{model.toUpperCase()}</td>
                    <td style={{...resultCellStyle, color: "#dc3545", fontWeight: "bold"}}>{heartResults[model]}</td>
                    <td style={{...resultCellStyle, fontSize: "13px"}}>Accuracy: {heartResults[`${model}Acc`]?.toFixed(1)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Car Dataset */}
      <div style={cardStyle}>
        <h2 style={{ color: "#007bff", marginTop: 0, borderBottom: "2px solid #007bff", paddingBottom: "10px" }}>
          🚗 Car Evaluation Prediction
        </h2>

        <div style={inputContainerStyle}>
          <label style={labelStyle}>Buying (0-4) <input type="number" value={carInputs.buying} onChange={(e) => setCarInputs({...carInputs, buying: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Maintenance (0-4) <input type="number" value={carInputs.maint} onChange={(e) => setCarInputs({...carInputs, maint: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Doors <input type="number" value={carInputs.doors} onChange={(e) => setCarInputs({...carInputs, doors: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Persons <input type="number" value={carInputs.persons} onChange={(e) => setCarInputs({...carInputs, persons: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Luggage Boot <input type="number" value={carInputs.lug_boot} onChange={(e) => setCarInputs({...carInputs, lug_boot: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
          <label style={labelStyle}>Safety <input type="number" value={carInputs.safety} onChange={(e) => setCarInputs({...carInputs, safety: parseFloat(e.target.value) || 0})} style={inputStyle} /></label>
        </div>

        <button style={buttonStyle} onClick={predictCar}>🔮 Evaluate Car</button>

        {carError && <div style={errorStyle}>{carError}</div>}
        {Object.keys(carResults).length > 0 && (
          <div style={resultCardStyle}>
            <h3 style={{ marginTop: 0, color: "#007bff" }}>Results</h3>
            <table style={resultTableStyle}>
              <tbody>
                {models.map((model) => (
                  <tr key={model} style={resultRowStyle}>
                    <td style={{...resultCellStyle, fontWeight: "600"}}>{model.toUpperCase()}</td>
                    <td style={{...resultCellStyle, color: "#007bff", fontWeight: "bold"}}>{carResults[model]}</td>
                    <td style={{...resultCellStyle, fontSize: "13px"}}>Accuracy: {carResults[`${model}Acc`]?.toFixed(1)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default MLTest;
