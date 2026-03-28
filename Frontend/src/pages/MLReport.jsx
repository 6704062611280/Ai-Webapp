function MLReport() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Machine Learning Report</h1>

      <div style={{ border: "1px solid #ccc", padding: "15px", marginTop: "20px" }}>
        <h2>Heart Dataset</h2>
        <p>Model: Logistic Regression / Random Forest</p>
        <p>Accuracy: 0.85</p>
        <p>Description: Used for predicting heart disease risk.</p>
      </div>

      <div style={{ border: "1px solid #ccc", padding: "15px", marginTop: "20px" }}>
        <h2>Car Dataset</h2>
        <p>Model: Decision Tree</p>
        <p>Accuracy: 0.92</p>
        <p>Description: Used for car evaluation classification.</p>
      </div>
    </div>
  );
}

export default MLReport;