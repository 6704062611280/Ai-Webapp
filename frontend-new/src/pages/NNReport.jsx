function NNReport() {
  const containerStyle = {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "40px 20px",
    backgroundColor: "#f5f5f5",
    minHeight: "100vh"
  };

  const sectionStyle = {
    backgroundColor: "white",
    padding: "30px",
    marginBottom: "25px",
    borderRadius: "8px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  };

  const titleStyle = {
    fontSize: "28px",
    fontWeight: "bold",
    color: "#333",
    borderBottom: "3px solid #28a745",
    paddingBottom: "15px",
    marginBottom: "25px"
  };

  const subTitleStyle = {
    fontSize: "20px",
    fontWeight: "bold",
    color: "#28a745",
    marginTop: "20px",
    marginBottom: "15px"
  };

  const textStyle = {
    fontSize: "15px",
    lineHeight: "1.8",
    color: "#555",
    marginBottom: "15px"
  };

  const listStyle = {
    fontSize: "15px",
    lineHeight: "1.8",
    color: "#555",
    marginLeft: "25px",
    marginBottom: "10px"
  };

  return (
    <div style={containerStyle}>
      <h1 style={titleStyle}>🧠 รายงานการพัฒนาโมเดล Neural Network</h1>

      {/* Dataset Information Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>0. ข้อมูลเกี่ยวกับชุดข้อมูล (Dataset Information)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>
          ❤️ ชุดข้อมูลโรคหัวใจ (Heart Disease Risk Prediction Dataset)
        </h3>
        <p style={textStyle}>
          <strong>แหล่งข้อมูล: </strong>
          <a href="https://www.kaggle.com/datasets/rhythmghai/synthetic-heart-disease-risk-prediction-dataset" target="_blank" rel="noopener noreferrer" style={{color: "#28a745"}}>
            Kaggle - Synthetic Heart Disease Risk Prediction Dataset
          </a> <span style={{color: "#d9534f"}}>⚠️ (ลิงค์นี้ใช้ไม่ได้แล้ว)</span>
        </p>
        <p style={textStyle}>
          <strong>ขนาดชุดข้อมูล:</strong> 12,000 ตัวอย่าง<br/>
          <strong>จำนวนฟีเจอร์:</strong> 16 ฟีเจอร์ (ไม่รวม Risk_Score target)<br/>
          <strong>คลาสที่คาดการณ์:</strong> 2 คลาส (Healthy/Heart disease)
        </p>

        <h4 style={{...subTitleStyle, fontSize: "14px", color: "#555", marginTop: "20px"}}>รายละเอียดฟีเจอร์ (Feature Details):</h4>
        <div style={listStyle}>
          1. <strong>Age</strong>: อายุของผู้ป่วย (ปี)<br/>
          2. <strong>Gender</strong>: เพศ (0=Female, 1=Male)<br/>
          3. <strong>Resting_BP</strong>: ความดันเลือดขณะพัก (mmHg)<br/>
          4. <strong>Cholesterol</strong>: ระดับคอเลสเตอรอล (mg/dL)<br/>
          5. <strong>Fasting_Blood_Sugar</strong>: น้ำตาลในเลือดขณะอดอาหาร (mg/dL) ⭐ <strong>ตัวชี้วัดสำคัญ</strong><br/>
          6. <strong>Max_Heart_Rate</strong>: อัตราการเต้นสูงสุดที่บรรลุ (bpm)<br/>
          7. <strong>ECG_Result</strong>: ผลการทำ ECG (0=LVH, 1=Normal, 2=ST)<br/>
          8. <strong>Smoking_Status</strong>: สถานะการสูบบุหรี่ (0=Current, 1=Former, 2=Never)<br/>
          9. <strong>Alcohol_Consumption</strong>: การบริโภคแอลกอฮอล์ (หน่วย/สัปดาห์)<br/>
          10. <strong>Physical_Activity_Level</strong>: ระดับกิจกรรมทางกายภาพ (0=High, 1=Low, 2=Moderate)<br/>
          11. <strong>Diet_Quality_Score</strong>: คะแนนคุณภาพอาหาร (0-100)<br/>
          12. <strong>Sleep_Hours</strong>: ชั่วโมงการนอนหลับต่อคืน<br/>
          13. <strong>BMI</strong>: ดัชนีมวลกาย (Body Mass Index)<br/>
          14. <strong>Diabetes</strong>: มีโรคเบาหวาน (0=No, 1=Yes)<br/>
          15. <strong>Hypertension</strong>: มีโรคความดันโลหิตสูง (0=No, 1=Yes)<br/>
          16. <strong>Family_History</strong>: มีประวัติโรคหัวใจในครอบครัว (0=No, 1=Yes)
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>หมายเหตุ:</strong> ค่า Fasting_Blood_Sugar เป็นตัวชี้วัดที่สำคัญมากในการวินิจฉัยโรคหัวใจ ผู้ป่วยที่มีโรคหัวใจส่วนใหญ่มีค่า FSB สูงกว่า 140 mg/dL
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "30px"}}>
          🚗 ชุดข้อมูลประเมินรถยนต์ (Car Evaluation Dataset)
        </h3>
        <p style={textStyle}>
          <strong>แหล่งข้อมูล: </strong>
          <a href="https://archive.ics.uci.edu/dataset/19/car+evaluation" target="_blank" rel="noopener noreferrer" style={{color: "#28a745"}}>
            UCI Machine Learning Repository - Car Evaluation
          </a>
        </p>
        <p style={textStyle}>
          <strong>ขนาดชุดข้อมูล:</strong> 1,728 ตัวอย่าง<br/>
          <strong>จำนวนฟีเจอร์:</strong> 6 ฟีเจอร์ (ทั้งหมดเป็นตัวแปรแบบ ordered categorical)<br/>
          <strong>คลาสที่คาดการณ์:</strong> 4 คลาส (unacc, acc, good, vgood)
        </p>

        <h4 style={{...subTitleStyle, fontSize: "14px", color: "#555", marginTop: "20px"}}>รายละเอียดฟีเจอร์และการแมป (Feature Details & Mapping):</h4>
        <div style={listStyle}>
          1. <strong>buying</strong>: ราคาซื้อ (1=vhigh สูงมาก, 2=high สูง, 3=med ปานกลาง, 4=low ต่ำ)<br/>
          2. <strong>maint</strong>: ราคาบำรุงรักษา (1=vhigh สูงมาก, 2=high สูง, 3=med ปานกลาง, 4=low ต่ำ)<br/>
          3. <strong>doors</strong>: จำนวนประตู (2, 3, 4, หรือ 5 5=มากกว่า)<br/>
          4. <strong>persons</strong>: ความจุของผู้โดยสาร (2, 4, หรือ 5 5=มากกว่า)<br/>
          5. <strong>lug_boot</strong>: ขนาดท้ายรถ (1=small เล็ก, 2=med ปานกลาง, 3=big ใหญ่)<br/>
          6. <strong>safety</strong>: การประเมินความปลอดภัย (1=low ต่ำ, 2=med ปานกลาง, 3=high สูง)
        </div>

        <h4 style={{...subTitleStyle, fontSize: "14px", color: "#555", marginTop: "20px"}}>คลาสเป้าหมาย (Target Classes):</h4>
        <div style={listStyle}>
          • <strong>unacc</strong> (Unacceptable - ไม่ยอมรับได้): รถที่ไม่แนะนำในการซื้อ<br/>
          • <strong>acc</strong> (Acceptable - ยอมรับได้): รถที่ยอมรับได้ในราคาที่เหมาะสม<br/>
          • <strong>good</strong> (Good - ดี): รถที่ดีและแนะนำในการซื้อ<br/>
          • <strong>vgood</strong> (Very Good - ดีมาก): รถที่ดีมากและเป็นช่วยในการตัดสินใจซื้อ
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>กรณีการใช้งาน:</strong> ชุดข้อมูลนี้ใช้สำหรับการประเมินอัตโนมัติของคุณภาพรถยนต์และการสนับสนุนการตัดสินใจของผู้ซื้อ
        </p>
      </div>

      {/* Data Preparation Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>1. การเตรียมข้อมูล (Data Preparation)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>ชุดข้อมูลโรคหัวใจ (Heart Disease Dataset)</h3>
        <p style={textStyle}>
          • <strong>จำนวนตัวอย่าง:</strong> 303 ตัวอย่าง<br/>
          • <strong>จำนวนฟีเจอร์:</strong> 3 ฟีเจอร์ (Age, Cholesterol, Resting BP)<br/>
          • <strong>ขั้นตอนการเตรียม:</strong>
        </p>
        <div style={listStyle}>
          - ทำความสะอาดข้อมูลและจัดการค่า NaN<br/>
          - ทำการ normalization โดยใช้ StandardScaler เพื่อให้ค่าอยู่ในช่วง -1 ถึง 1<br/>
          - แบ่งข้อมูลเป็น training และ validation (80:20)<br/>
          - One-hot encoding สำหรับ label ที่มีหลายคลาส
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ชุดข้อมูลประเมินรถยนต์ (Car Evaluation Dataset)</h3>
        <p style={textStyle}>
          • <strong>จำนวนตัวอย่าง:</strong> 1,728 ตัวอย่าง<br/>
          • <strong>จำนวนฟีเจอร์:</strong> 6 ฟีเจอร์ (Buying, Maintenance, Doors, Persons, Lug Boot, Safety)<br/>
          • <strong>ขั้นตอนการเตรียม:</strong>
        </p>
        <div style={listStyle}>
          - Encoding ฟีเจอร์ตัวแปรแบบ categorical เป็นตัวเลข<br/>
          - Scaling ข้อมูลให้มีการกระจายตัวแบบเกาส์เซียน<br/>
          - แบ่งข้อมูลสำหรับ training และ validation<br/>
          - One-hot encoding สำหรับเอาต์พุต (4 คลาส)
        </div>
      </div>

      {/* Network Architecture Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>2. สถาปัตยกรรมของเครือข่ายประสาท (Neural Network Architecture)</h2>
        
        <p style={textStyle}>
          ใช้เครือข่ายประสาทแบบ Multi-Layer Perceptron (MLP) หรือ Dense Neural Network ที่ประกอบด้วยชั้นการประมวลผลหลายชั้น
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>โครงสร้างเครือข่าย</h3>
        <div style={listStyle}>
          <strong>ชุดข้อมูลโรคหัวใจ:</strong><br/>
          - Input Layer: 3 neuron (สำหรับ 3 ฟีเจอร์)<br/>
          - Hidden Layer 1: 32 neuron, Activation: ReLU<br/>
          - Hidden Layer 2: 16 neuron, Activation: ReLU<br/>
          - Output Layer: 2 neuron (Healthy/Heart disease), Activation: Softmax<br/>
          <br/>
          <strong>ชุดข้อมูลประเมินรถยนต์:</strong><br/>
          - Input Layer: 6 neuron (สำหรับ 6 ฟีเจอร์)<br/>
          - Hidden Layer 1: 64 neuron, Activation: ReLU<br/>
          - Hidden Layer 2: 32 neuron, Activation: ReLU<br/>
          - Hidden Layer 3: 16 neuron, Activation: ReLU<br/>
          - Output Layer: 4 neuron (4 คลาส), Activation: Softmax
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>หลักการการทำงาน</h3>
        <div style={listStyle}>
          - <strong>Feedforward Propagation:</strong> ข้อมูลเข้าผ่านแต่ละชั้น โดยคำนวณ weighted sum และใช้ activation function<br/>
          - <strong>ReLU Activation:</strong> ใช้ในชั้น hidden เพื่อเพิ่มความไม่เป็นเชิงเส้น<br/>
          - <strong>Softmax:</strong> ใช้ในชั้น output เพื่อแปลงเป็น probability distribution<br/>
          - <strong>Backpropagation:</strong> ปรับแต่งน้ำหนักตามสัญญาณผิดพลาด<br/>
          - <strong>Optimization:</strong> ใช้ Adam optimizer เพื่อหาค่าน้ำหนักที่เหมาะสม
        </div>
      </div>

      {/* Model Development Steps */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>3. ขั้นตอนการพัฒนาโมเดล (Model Development)</h2>
        
        <p style={textStyle}>
          <strong>ขั้นตอนที่ 1: เตรียมข้อมูล</strong>
        </p>
        <div style={listStyle}>
          - โหลดและตรวจสอบชุดข้อมูล<br/>
          - ทำความสะอาดและปรับค่าข้อมูล<br/>
          - Normalization และ Scaling
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 2: สร้างเครือข่ายประสาท</strong>
        </p>
        <div style={listStyle}>
          - สร้าง Sequential Model โดยใช้ TensorFlow/Keras<br/>
          - เพิ่มชั้นต่างๆ (Dense, Activation)<br/>
          - Compile โมเดลด้วย optimizer, loss function, และ metrics
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 3: ฝึก (Training)</strong>
        </p>
        <div style={listStyle}>
          - ฝึกโมเดลด้วย training data เป็นจำนวน epoch<br/>
          - ตรวจสอบประสิทธิภาพบน validation data หลังแต่ละ epoch<br/>
          - ใช้ Early Stopping เพื่อหลีกเลี่ยง overfitting
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 4: ประเมิน (Evaluation)</strong>
        </p>
        <div style={listStyle}>
          - ประเมินประสิทธิภาพบน test data<br/>
          - คำนวณ accuracy, loss, และ confidence level<br/>
          - วิเคราะห์ผลลัพธ์และปรับปรุง
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 5: บันทึกและติดตั้ง</strong>
        </p>
        <div style={listStyle}>
          - บันทึกโมเดลและ scaler<br/>
          - สร้าง API สำหรับการทำนาย<br/>
          - ติดตั้ง web interface เพื่อใช้งาน
        </div>
      </div>

      {/* Training Details */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>4. รายละเอียดการฝึก (Training Details)</h2>
        
        <div style={listStyle}>
          <strong>ฟังก์ชันการสูญเสีย (Loss Function):</strong> Categorical Crossentropy<br/>
          <strong>Optimizer:</strong> Adam (Learning Rate: 0.001)<br/>
          <strong>Batch Size:</strong> 32<br/>
          <strong>จำนวน Epochs:</strong> 100 (มี Early Stopping)<br/>
          <strong>Validation Split:</strong> 0.2<br/>
          <strong>Metrics:</strong> Accuracy
        </div>
      </div>

      {/* Data Sources */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>5. แหล่งอ้างอิงข้อมูล (Data Sources & Libraries)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>ชุดข้อมูล</h3>
        <p style={textStyle}>
          • Heart Disease Dataset: ข้อมูลผู้ป่วยจากการศึกษาทางการแพทย์<br/>
          • Car Evaluation Dataset: ข้อมูลการประเมินคุณภาพรถยนต์
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ไลบรารี่และเครื่องมือที่ใช้</h3>
        <div style={listStyle}>
          - <strong>TensorFlow 2.17:</strong> สำหรับพัฒนาเครือข่ายประสาท<br/>
          - <strong>Keras:</strong> API ระดับสูงสำหรับสร้างโมเดล<br/>
          - <strong>scikit-learn:</strong> สำหรับ preprocessing และ label encoding<br/>
          - <strong>pandas:</strong> สำหรับจัดการข้อมูล<br/>
          - <strong>numpy:</strong> สำหรับการคำนวณตัวเลข
        </div>
      </div>

      {/* Results Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>6. ผลลัพธ์และสรุป (Results & Summary)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>ชุดข้อมูลโรคหัวใจ</h3>
        <p style={textStyle}>
          เครือข่ายประสาทสามารถเรียนรู้รูปแบบ (patterns) ที่ซ่อนอยู่ในข้อมูล และทำการทำนายโรคหัวใจด้วยความแม่นยำที่สูง เครือข่ายมีขนาดกะทัดรัดเนื่องจากมีจำนวนฟีเจอร์น้อย
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ชุดข้อมูลประเมินรถยนต์</h3>
        <p style={textStyle}>
          เครือข่ายประสาทที่มีชั้น hidden หลายชั้นสามารถจำแนกรถยนต์เป็น 4 ประเภทได้อย่างมีประสิทธิภาพ ความลึกของเครือข่ายช่วยให้สามารถเรียนรู้ความสัมพันธ์ที่ซับซ้อนระหว่างฟีเจอร์ต่างๆ
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ข้อดี-ข้อเสีย</h3>
        <div style={listStyle}>
          <strong>ข้อดี:</strong><br/>
          - สามารถเรียนรู้ความสัมพันธ์ที่ซับซ้อน<br/>
          - ให้ผลลัพธ์ที่แม่นยำสูง<br/>
          - สามารถ generalize ได้ดี<br/>
          <br/>
          <strong>ข้อเสีย:</strong><br/>
          - ต้องใช้ข้อมูลจำนวนมาก<br/>
          - หาค่า hyperparameter ที่เหมาะสมทำให้ยาก<br/>
          - อาจเกิด overfitting ได้ง่าย
        </div>
      </div>
    </div>
  );
}

export default NNReport;