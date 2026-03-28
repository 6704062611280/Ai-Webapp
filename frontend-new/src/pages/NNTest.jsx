import { useState } from "react";

function NNTest() {
  const [heartInputs, setHeartInputs] = useState({
    age: 45,
    cholesterol: 200,
    restingBp: 120
  });
  const [carInputs, setCarInputs] = useState({
    buying: 2,
    maint: 2,
    doors: 4,
    persons: 4,
    lug_boot: 2,
    safety: 3
  });
  const [heartResult, setHeartResult] = useState({});
  const [carResult, setCarResult] = useState({});
  const [heartError, setHeartError] = useState(null);
  const [carError, setCarError] = useState(null);

  const predictHeart = async () => {
    setHeartError(null);
    try {
      const res = await fetch("http://127.0.0.1:8004/predict/heart/nn", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({age: heartInputs.age, cholesterol: heartInputs.cholesterol, resting_bp: heartInputs.restingBp})
      });
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      console.log("Heart NN response:", data);
      if (data.error) {
        throw new Error(data.error);
      }
      setHeartResult({ result: data.result, accuracy: data.accuracy });
    } catch (error) {
      setHeartError(error.message);
    }
  };

  const predictCar = async () => {
    setCarError(null);
    try {
      const res = await fetch("http://127.0.0.1:8004/predict/car/nn", {
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
      console.log("Car NN response:", data);
      if (data.error) {
        throw new Error(data.error);
      }
      setCarResult({ result: data.result, accuracy: data.accuracy });
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
    gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
    gap: "15px",
    marginBottom: "20px"
  };

  const labelStyle = {
    display: "flex",
    flexDirection: "column",
    fontSize: "14px",
    fontWeight: "500",
    color: "#333"
  };

  const inputStyle = {
    padding: "10px",
    marginTop: "5px",
    border: "1px solid #ddd",
    borderRadius: "5px",
    fontSize: "14px"
  };

  const buttonStyle = {
    padding: "12px 28px",
    fontSize: "16px",
    fontWeight: "600",
    backgroundColor: "#28a745",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    marginTop: "10px",
    transition: "background-color 0.3s"
  };

  const resultCardStyle = {
    backgroundColor: "#f0f8f5",
    border: "2px solid #28a745",
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

  const resultValueStyle = {
    fontSize: "18px",
    fontWeight: "bold",
    color: "#28a745",
    marginBottom: "10px"
  };

  const accuracyStyle = {
    fontSize: "16px",
    color: "#666",
    marginTop: "10px"
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
        fontWeight: "600",
        lineHeight: "1.8",
        letterSpacing: "0.5px"
      }}>
        🤖 Neural Network (MLP) Prediction
      </h1>

      {/* Heart Dataset */}
      <div style={cardStyle}>
        <h2 style={{ color: "#dc3545", marginTop: 0, borderBottom: "2px solid #dc3545", paddingBottom: "10px" }}>
          ❤️ Heart Disease Prediction
        </h2>
        
        <div style={inputContainerStyle}>
          <label style={labelStyle}>
            Age
            <input 
              type="number" 
              value={heartInputs.age} 
              onChange={(e) => setHeartInputs({...heartInputs, age: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Cholesterol (mg/dL)
            <input 
              type="number" 
              value={heartInputs.cholesterol} 
              onChange={(e) => setHeartInputs({...heartInputs, cholesterol: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Resting BP (mmHg)
            <input 
              type="number" 
              value={heartInputs.restingBp} 
              onChange={(e) => setHeartInputs({...heartInputs, restingBp: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
        </div>

        <button 
          onClick={predictHeart}
          onMouseEnter={(e) => e.target.style.backgroundColor = "#218838"}
          onMouseLeave={(e) => e.target.style.backgroundColor = "#28a745"}
          style={buttonStyle}
        >
          🔍 Predict Heart Status
        </button>

        {heartError && (
          <div style={errorStyle}>
            <strong>Error:</strong> {heartError}
          </div>
        )}

        {Object.keys(heartResult).length > 0 && !heartError && (
          <div style={resultCardStyle}>
            <h3 style={{ marginTop: 0, color: "#28a745" }}>Prediction Results</h3>
            <table style={resultTableStyle}>
              <tbody>
                <tr style={resultRowStyle}>
                  <td style={{...resultCellStyle, fontWeight: "600", color: "#333", minWidth: "120px"}}>Result</td>
                  <td style={{...resultCellStyle, ...resultValueStyle}}>{heartResult.result || 'N/A'}</td>
                  <td style={{...resultCellStyle, ...accuracyStyle}}>Confidence: {heartResult.accuracy || 0}%</td>
                </tr>
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
          <label style={labelStyle}>
            Buying Price
            <input 
              type="number" 
              value={carInputs.buying} 
              onChange={(e) => setCarInputs({...carInputs, buying: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Maintenance Cost
            <input 
              type="number" 
              value={carInputs.maint} 
              onChange={(e) => setCarInputs({...carInputs, maint: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Doors
            <input 
              type="number" 
              value={carInputs.doors} 
              onChange={(e) => setCarInputs({...carInputs, doors: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Persons (Capacity)
            <input 
              type="number" 
              value={carInputs.persons} 
              onChange={(e) => setCarInputs({...carInputs, persons: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Lug Boot Space
            <input 
              type="number" 
              value={carInputs.lug_boot} 
              onChange={(e) => setCarInputs({...carInputs, lug_boot: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
          <label style={labelStyle}>
            Safety Rating
            <input 
              type="number" 
              value={carInputs.safety} 
              onChange={(e) => setCarInputs({...carInputs, safety: parseFloat(e.target.value) || 0})}
              style={inputStyle}
            />
          </label>
        </div>

        <button 
          onClick={predictCar}
          onMouseEnter={(e) => e.target.style.backgroundColor = "#0056b3"}
          onMouseLeave={(e) => e.target.style.backgroundColor = "#007bff"}
          style={{...buttonStyle, backgroundColor: "#007bff"}}
        >
          🔍 Predict Car Rating
        </button>

        {carError && (
          <div style={errorStyle}>
            <strong>Error:</strong> {carError}
          </div>
        )}

        {Object.keys(carResult).length > 0 && !carError && (
          <div style={{...resultCardStyle, backgroundColor: "#f0f6ff", borderColor: "#007bff"}}>
            <h3 style={{ marginTop: 0, color: "#007bff" }}>Prediction Results</h3>
            <table style={resultTableStyle}>
              <tbody>
                <tr style={resultRowStyle}>
                  <td style={{...resultCellStyle, fontWeight: "600", color: "#333", minWidth: "120px"}}>Result</td>
                  <td style={{...resultCellStyle, color: "#007bff", fontWeight: "bold"}}>{carResult.result || 'N/A'}</td>
                  <td style={{...resultCellStyle, ...accuracyStyle}}>Confidence: {carResult.accuracy || 0}%</td>
                </tr>
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default NNTest;