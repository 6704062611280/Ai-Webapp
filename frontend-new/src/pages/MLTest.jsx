import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "https://ai-webapp-production.up.railway.app";

function MLTest() {
  const [heartInputs, setHeartInputs] = useState({
    age: 45,
    gender: 1,
    restingBp: 120,
    cholesterol: 180,
    fastingBloodSugar: 100,
    maxHr: 150,
    ecgResult: 1,
    smokingStatus: 2,
    alcoholConsumption: 0,
    physicalActivityLevel: 1,
    dietQualityScore: 50,
    sleepHours: 7,
    bmi: 24,
    diabetes: 0,
    hypertension: 0,
    familyHistory: 0,
    riskScore: 25
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
      gender: 1,
      restingBp: 120,
      cholesterol: 180,
      fastingBloodSugar: 100,
      maxHr: 150,
      ecgResult: 1,
      smokingStatus: 2,
      alcoholConsumption: 0,
      physicalActivityLevel: 1,
      dietQualityScore: 50,
      sleepHours: 7,
      bmi: 24,
      diabetes: 0,
      hypertension: 0,
      familyHistory: 0,
      riskScore: 25
    });
  };

  const diseaseExample = () => {
    setHeartInputs({
      age: 66,
      gender: 0,
      restingBp: 121,
      cholesterol: 211,
      fastingBloodSugar: 177,
      maxHr: 141,
      ecgResult: 1,
      smokingStatus: 0,
      alcoholConsumption: 2,
      physicalActivityLevel: 2,
      dietQualityScore: 4,
      sleepHours: 6,
      bmi: 25,
      diabetes: 1,
      hypertension: 1,
      familyHistory: 1,
      riskScore: 68
    });
  };

  const moderateExample = () => {
    setHeartInputs({
      age: 55,
      gender: 0,
      restingBp: 140,
      cholesterol: 220,
      fastingBloodSugar: 110,
      maxHr: 120,
      ecgResult: 1,
      smokingStatus: 1,
      alcoholConsumption: 1,
      physicalActivityLevel: 0,
      dietQualityScore: 40,
      sleepHours: 6,
      bmi: 27,
      diabetes: 0,
      hypertension: 1,
      familyHistory: 0,
      riskScore: 50
    });
  };

  // Car Evaluation Example Presets
  const carBadExample = () => {
    setCarInputs({ buying: 1, maint: 1, doors: 2, persons: 2, lug_boot: 1, safety: 1 });
  };

  const carGoodExample = () => {
    setCarInputs({ buying: 4, maint: 4, doors: 4, persons: 5, lug_boot: 3, safety: 3 });
  };

  const carModerateExample = () => {
    setCarInputs({ buying: 2, maint: 2, doors: 3, persons: 4, lug_boot: 2, safety: 2 });
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

        {/* Input Fields - All 17 Features */}
        <div style={inputContainerStyle}>
          <label style={labelStyle}>Age (years) <input type="number" placeholder="20-100" value={heartInputs.age} onChange={(e) => setHeartInputs({...heartInputs, age: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          
          <label style={labelStyle}>Gender
            <select value={heartInputs.gender} onChange={(e) => setHeartInputs({...heartInputs, gender: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">Female</option>
              <option value="1">Male</option>
            </select>
          </label>
          
          <label style={labelStyle}>Resting BP (mmHg) <input type="number" placeholder="90-180 mmHg" value={heartInputs.restingBp} onChange={(e) => setHeartInputs({...heartInputs, restingBp: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          <label style={labelStyle}>Cholesterol (mg/dL) <input type="number" placeholder="100-400 mg/dL" value={heartInputs.cholesterol} onChange={(e) => setHeartInputs({...heartInputs, cholesterol: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          <label style={labelStyle}>Fasting Blood Sugar (mg/dL) ⭐ <input type="number" placeholder="80-300 (Disease: 177)" value={heartInputs.fastingBloodSugar} onChange={(e) => setHeartInputs({...heartInputs, fastingBloodSugar: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          <label style={labelStyle}>Max HR (bpm) <input type="number" placeholder="60-200 bpm" value={heartInputs.maxHr} onChange={(e) => setHeartInputs({...heartInputs, maxHr: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          
          <label style={labelStyle}>ECG Result
            <select value={heartInputs.ecgResult} onChange={(e) => setHeartInputs({...heartInputs, ecgResult: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">LVH (Left Ventricular Hypertrophy)</option>
              <option value="1">Normal</option>
              <option value="2">ST (ST-T Abnormality)</option>
            </select>
          </label>
          
          <label style={labelStyle}>Smoking Status
            <select value={heartInputs.smokingStatus} onChange={(e) => setHeartInputs({...heartInputs, smokingStatus: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">Current Smoker</option>
              <option value="1">Former Smoker</option>
              <option value="2">Never Smoked</option>
            </select>
          </label>
          
          <label style={labelStyle}>Alcohol (units/week) <input type="number" placeholder="0-10 units" value={heartInputs.alcoholConsumption} onChange={(e) => setHeartInputs({...heartInputs, alcoholConsumption: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          
          <label style={labelStyle}>Physical Activity
            <select value={heartInputs.physicalActivityLevel} onChange={(e) => setHeartInputs({...heartInputs, physicalActivityLevel: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">High (Regular Exercise)</option>
              <option value="1">Low (Sedentary)</option>
              <option value="2">Moderate (Occasional)</option>
            </select>
          </label>
          
          <label style={labelStyle}>Diet Quality Score <input type="number" placeholder="0-100 (Higher=Better)" value={heartInputs.dietQualityScore} onChange={(e) => setHeartInputs({...heartInputs, dietQualityScore: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          <label style={labelStyle}>Sleep Hours <input type="number" step="0.5" placeholder="4-12 hours" value={heartInputs.sleepHours} onChange={(e) => setHeartInputs({...heartInputs, sleepHours: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          <label style={labelStyle}>BMI <input type="number" step="0.1" placeholder="15-40 (Normal: 18-25)" value={heartInputs.bmi} onChange={(e) => setHeartInputs({...heartInputs, bmi: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
          
          <label style={labelStyle}>Diabetes
            <select value={heartInputs.diabetes} onChange={(e) => setHeartInputs({...heartInputs, diabetes: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </label>
          
          <label style={labelStyle}>Hypertension
            <select value={heartInputs.hypertension} onChange={(e) => setHeartInputs({...heartInputs, hypertension: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </label>
          
          <label style={labelStyle}>Family History
            <select value={heartInputs.familyHistory} onChange={(e) => setHeartInputs({...heartInputs, familyHistory: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="0">No Family History</option>
              <option value="1">Has Family History</option>
            </select>
          </label>
          
          <label style={labelStyle}>Risk Score <input type="number" placeholder="0-100" value={heartInputs.riskScore} onChange={(e) => setHeartInputs({...heartInputs, riskScore: e.target.value === "" ? "" : parseFloat(e.target.value)})} style={inputStyle} /></label>
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

        {/* Car Presets */}
        <div style={presetButtonContainerStyle}>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#dc3545"}}
            onClick={carBadExample}
          >
            ❌ Poor Car
          </button>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#ffc107", color: "#333"}}
            onClick={carModerateExample}
          >
            ⚠️ Average Car
          </button>
          <button 
            style={{...presetButtonStyle, backgroundColor: "#28a745"}}
            onClick={carGoodExample}
          >
            ✅ Good Car
          </button>
        </div>

        <div style={inputContainerStyle}>
          <label style={labelStyle}>Buying Price
            <select value={carInputs.buying} onChange={(e) => setCarInputs({...carInputs, buying: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="1">vhigh (Very High Price)</option>
              <option value="2">high (High Price)</option>
              <option value="3">med (Medium Price)</option>
              <option value="4">low (Low Price)</option>
            </select>
          </label>
          <label style={labelStyle}>Maintenance Cost
            <select value={carInputs.maint} onChange={(e) => setCarInputs({...carInputs, maint: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="1">vhigh (Very High Cost)</option>
              <option value="2">high (High Cost)</option>
              <option value="3">med (Medium Cost)</option>
              <option value="4">low (Low Cost)</option>
            </select>
          </label>
          <label style={labelStyle}>Number of Doors
            <select value={carInputs.doors} onChange={(e) => setCarInputs({...carInputs, doors: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="2">2 Doors</option>
              <option value="3">3 Doors</option>
              <option value="4">4 Doors</option>
              <option value="5">5+ Doors</option>
            </select>
          </label>
          <label style={labelStyle}>Seating Capacity
            <select value={carInputs.persons} onChange={(e) => setCarInputs({...carInputs, persons: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="2">2 Persons</option>
              <option value="4">4 Persons</option>
              <option value="5">5+ Persons</option>
            </select>
          </label>
          <label style={labelStyle}>Luggage Boot Size
            <select value={carInputs.lug_boot} onChange={(e) => setCarInputs({...carInputs, lug_boot: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="1">small (Small Boot)</option>
              <option value="2">med (Medium Boot)</option>
              <option value="3">big (Large Boot)</option>
            </select>
          </label>
          <label style={labelStyle}>Safety Rating
            <select value={carInputs.safety} onChange={(e) => setCarInputs({...carInputs, safety: parseFloat(e.target.value)})} style={inputStyle}>
              <option value="1">low (Low Safety)</option>
              <option value="2">med (Medium Safety)</option>
              <option value="3">high (High Safety)</option>
            </select>
          </label>
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
