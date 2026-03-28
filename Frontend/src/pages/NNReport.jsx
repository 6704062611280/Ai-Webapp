function NNReport() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Neural Network Report</h1>

      <div style={{ border: "1px solid #ccc", padding: "15px", marginTop: "20px" }}>
        <h2>Heart Dataset</h2>
        <p>Model: Neural Network</p>
        <p>Accuracy: 0.90</p>
        <p>Description: Deep learning model for heart prediction.</p>
      </div>

      <div style={{ border: "1px solid #ccc", padding: "15px", marginTop: "20px" }}>
        <h2>Car Dataset</h2>
        <p>Model: Neural Network</p>
        <p>Accuracy: 0.95</p>
        <p>Description: Deep learning classification for car dataset.</p>
      </div>
    </div>
  );
}

export default NNReport;