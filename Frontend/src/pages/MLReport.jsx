export default function MLReport() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Machine Learning Model</h1>

      <h2>1. Data Preparation</h2>
      <p>
        Dataset ที่ใช้คือ Car Evaluation ซึ่งมี feature เช่น buying, maint,
        doors, persons, lug_boot และ safety โดยทำการ clean ข้อมูล,
        one-hot encoding และ scaling
      </p>

      <h2>2. Algorithms</h2>
      <ul>
        <li>Decision Tree</li>
        <li>K-Nearest Neighbors (KNN)</li>
        <li>Support Vector Machine (SVM)</li>
      </ul>

      <h2>3. Model Development</h2>
      <p>
        ทำการ train model โดยใช้ข้อมูลที่ preprocess แล้ว และประเมินผลด้วย accuracy
      </p>

      <h2>4. Reference</h2>
      <p>UCI Machine Learning Repository</p>
    </div>
  );
}