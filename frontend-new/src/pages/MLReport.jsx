function MLReport() {
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
    borderBottom: "3px solid #007bff",
    paddingBottom: "15px",
    marginBottom: "25px"
  };

  const subTitleStyle = {
    fontSize: "20px",
    fontWeight: "bold",
    color: "#007bff",
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
      <h1 style={titleStyle}>📊 รายงานการพัฒนาโมเดล Machine Learning</h1>

      {/* Dataset Information Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>0. ข้อมูลเกี่ยวกับชุดข้อมูล (Dataset Information)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>❤️ ชุดข้อมูลโรคหัวใจ (Heart Disease Risk Prediction Dataset)</h3>
        <p style={textStyle}>
          <strong>แหล่งข้อมูล: </strong><a href="https://www.kaggle.com/datasets/rhythmghai/synthetic-heart-disease-risk-prediction-dataset" target="_blank" rel="noopener noreferrer">Kaggle - Synthetic Heart Disease Risk Prediction Dataset</a> <span style={{color: "#d9534f"}}>⚠️ (ลิงค์นี้ใช้ไม่ได้แล้ว)</span>
        </p>
        <p style={textStyle}>
          ชุดข้อมูลนี้เป็น dataset สังเคราะห์ที่ออกแบบมาเพื่อการทำนายความเสี่ยงโรคหัวใจโดยใช้ machine learning ข้อมูลประกอบด้วยข้อมูลผู้ป่วยด้านสุขภาพที่เกี่ยวข้องกับหัวใจและปัจจัยด้านชีวิตประจำวัน
        </p>
        <p style={textStyle}><strong>จำนวนตัวอย่าง: </strong> 12,000 ตัวอย่าง</p>
        <p style={textStyle}><strong>จำนวนฟีเจอร์: </strong> 16 ฟีเจอร์ (เลือกใช้หลังเอาออก Risk_Score)</p>
        <p style={textStyle}><strong>คำอธิบายฟีเจอร์:</strong></p>
        <div style={listStyle}>
          • <strong>Age:</strong> อายุของผู้ป่วย (ปี)<br/>
          • <strong>Gender:</strong> เพศ (Female=0, Male=1)<br/>
          • <strong>Resting_BP:</strong> ความดันโลหิตแบบนอน (mmHg)<br/>
          • <strong>Cholesterol:</strong> ระดับคอเลสเตอรอล (mg/dL)<br/>
          • <strong>Fasting_Blood_Sugar:</strong> ระดับน้ำตาลในเลือดขณะอดอาหาร (mg/dL) - ⭐ ตัวบ่งชี้สำคัญสำหรับโรคหัวใจ<br/>
          • <strong>Max_Heart_Rate:</strong> อัตราการเต้นของหัวใจสูงสุดที่บรรลุได้ (bpm)<br/>
          • <strong>ECG_Result:</strong> ผลการตรวจคลื่นไฟฟ้าหัวใจ (LVH=0, Normal=1, ST=2)<br/>
          • <strong>Smoking_Status:</strong> สถานะการสูบบุหรี่ (Current=0, Former=1, Never=2)<br/>
          • <strong>Alcohol_Consumption:</strong> การบริโภคแอลกอฮอล์ (หน่วย/สัปดาห์)<br/>
          • <strong>Physical_Activity_Level:</strong> ระดับกิจกรรมทางกายภาพ (High=0, Low=1, Moderate=2)<br/>
          • <strong>Diet_Quality_Score:</strong> คะแนนคุณภาพอาหาร (0-100)<br/>
          • <strong>Sleep_Hours:</strong> ชั่วโมงการนอนต่อคืน<br/>
          • <strong>BMI:</strong> ดัชนีมวลกาย (Body Mass Index)<br/>
          • <strong>Diabetes:</strong> การป่วยเป็นโรคเบาหวาน (No=0, Yes=1)<br/>
          • <strong>Hypertension:</strong> ความดันโลหิตสูง (No=0, Yes=1)<br/>
          • <strong>Family_History:</strong> ประวัติโรคหัวใจในครอบครัว (No=0, Yes=1)<br/>
        </div>
        <p style={textStyle}><strong>สูตรประเมิน: </strong> ใช้ 16 ฟีเจอร์ (เอา Risk_Score ออก) ด้วยการสนับสนุนของ class weights เพื่อจัดการกับความไม่สมดุลของคลาส</p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "30px"}}>🚗 ชุดข้อมูลประเมินรถยนต์ (Car Evaluation Dataset)</h3>
        <p style={textStyle}>
          <strong>แหล่งข้อมูล: </strong><a href="https://archive.ics.uci.edu/dataset/19/car+evaluation" target="_blank" rel="noopener noreferrer">UCI Machine Learning Repository - Car Evaluation</a>
        </p>
        <p style={textStyle}>
          ชุดข้อมูลนี้ประกอบด้วยข้อมูลการประเมินรถยนต์โดยตรวจสอบจากคำขอการซื้อรถ และแบ่งออกเป็น 4 คลาสตามการประเมิน ได้รับการส่งมอบจาก AAAI ในปี 1997
        </p>
        <p style={textStyle}><strong>จำนวนตัวอย่าง: </strong> 1,728 ตัวอย่าง</p>
        <p style={textStyle}><strong>จำนวนฟีเจอร์: </strong> 6 ฟีเจอร์เชิงหมวดหมู่</p>
        <p style={textStyle}><strong>คำอธิบายฟีเจอร์:</strong></p>
        <div style={listStyle}>
          • <strong>buying:</strong> ราคาซื้อ (1=vhigh, 2=high, 3=med, 4=low) - สูงกว่า = ถูกกว่า<br/>
          • <strong>maint:</strong> ค่าใช้บำรุงรักษา (1=vhigh, 2=high, 3=med, 4=low) - สูงกว่า = ถูกกว่า<br/>
          • <strong>doors:</strong> จำนวนประตู (2, 3, 4, 5=more)<br/>
          • <strong>persons:</strong> ความจุผู้โดยสาร (2, 4, 5=more)<br/>
          • <strong>lug_boot:</strong> ขนาดห้องโหลดสัมภาระ (1=small, 2=med, 3=big)<br/>
          • <strong>safety:</strong> การประเมินความปลอดภัยของผู้โดยสาร (1=low, 2=med, 3=high)<br/>
        </div>
        <p style={textStyle}><strong>คลาสเป้าหมาย (Target Classes): </strong> 4 คลาส</p>
        <div style={listStyle}>
          • unacc (unacceptable) - ไม่ยอมรับ<br/>
          • acc (acceptable) - ยอมรับ<br/>
          • good - ดี<br/>
          • vgood (very good) - ดีมาก
        </div>
        <p style={textStyle}><strong>การประยุกต์ใช้: </strong> ใช้สำหรับการประเมินคุณภาพรถยนต์อัตโนมัติและการช่วยสนับสนุนการตัดสินใจในการซื้อ</p>
      </div>

      {/* Data Preparation Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>1. การเตรียมข้อมูล (Data Preparation)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>ชุดข้อมูลโรคหัวใจ (Heart Disease Dataset)</h3>
        <p style={textStyle}>
          • <strong>จำนวนตัวอย่าง:</strong> 12,000 ตัวอย่าง<br/>
          • <strong>จำนวนฟีเจอร์:</strong> 16 ฟีเจอร์<br/>
          • <strong>ขั้นตอนการเตรียม:</strong>
        </p>
        <div style={listStyle}>
          - ทำความสะอาดข้อมูลและจัดการค่า NaN<br/>
          - Label encoding สำหรับฟีเจอร์เชิงหมวดหมู่ (Gender, ECG, Smoking, Activity)<br/>
          - ทำการ StandardScaler normalization<br/>
          - แบ่งข้อมูลเป็น training และ testing (80:20)<br/>
          - ใช้ SMOTE สำหรับจัดการความไม่สมดุลของคลาส<br/>
          - ประยุกต์ class weights เพื่อให้ model ให้ความสำคัญกับคลาส "Heart disease" มากขึ้น
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ชุดข้อมูลประเมินรถยนต์ (Car Evaluation Dataset)</h3>
        <p style={textStyle}>
          • <strong>จำนวนตัวอย่าง:</strong> 1,728 ตัวอย่าง<br/>
          • <strong>จำนวนฟีเจอร์:</strong> 6 ฟีเจอร์เชิงหมวดหมู่<br/>
          • <strong>ขั้นตอนการเตรียม:</strong>
        </p>
        <div style={listStyle}>
          - Label encoding สำหรับฟีเจอร์เชิงหมวดหมู่ (buying, maintenance, doors, persons, lug_boot, safety)<br/>
          - Scaling ข้อมูลให้มีการกระจายตัวแบบสม่ำเสมอ<br/>
          - Label encoding สำหรับคลาสเป้าหมาย (unacc=0, acc=1, good=2, vgood=3)<br/>
          - แบ่งข้อมูลสำหรับ training และ testing<br/>
          - จัดการความไม่สมดุลของคลาสโดยใช้ weighted classes
        </div>
      </div>

      {/* Algorithm Theory Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>2. ทฤษฎีของอัลกอริทึม (Algorithm Theory)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>K-Nearest Neighbors (KNN)</h3>
        <p style={textStyle}>
          KNN เป็นอัลกอริทึมการเรียนรู้แบบ instance-based ที่ทำการจำแนกข้อมูลใหม่โดยการหาค่าเฉลี่ยของ k ตัวอย่างที่ใกล้เคียงที่สุดในชุดข้อมูลการฝึก หลักการทำงาน:
        </p>
        <div style={listStyle}>
          - คำนวณระยะห่างระหว่างจุดข้อมูลใหม่กับจุดข้อมูลที่มีอยู่ทั้งหมด<br/>
          - เลือก k จุดที่มีระยะห่างน้อยที่สุด<br/>
          - ทำการ voting จากคลาสของ k จุดเหล่านั้น<br/>
          - ประเภทที่ได้คะแนน voting มากที่สุดจะเป็นผลลัพธ์
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>Support Vector Machine (SVM)</h3>
        <p style={textStyle}>
          SVM เป็นอัลกอริทึมที่ค้นหา hyperplane ที่เหมาะสมที่สุดเพื่อแยกข้อมูลของแต่ละคลาสออกจากกัน โดยมีระยะห่างมากที่สุด (maximum margin):
        </p>
        <div style={listStyle}>
          - สร้างขอบเขตการตัดสินใจระหว่างคลาสต่างๆ<br/>
          - ใช้ kernel trick สำหรับการแบ่งข้อมูลที่ไม่เป็นเชิงเส้น<br/>
          - หาค่า support vectors ที่เป็นจุดข้อมูลสำคัญ<br/>
          - ทำการจำแนกโดยพิจารณาจากตำแหน่งเทียบกับ hyperplane
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>Decision Tree</h3>
        <p style={textStyle}>
          Decision Tree เป็นโมเดลที่สร้างต้นไม้การตัดสินใจโดยการแบ่งข้อมูลตามเงื่อนไขต่างๆ เพื่อให้ได้ผลลัพธ์ที่บริสุทธิ์:
        </p>
        <div style={listStyle}>
          - เลือกฟีเจอร์ที่ให้ information gain มากที่สุด<br/>
          - แยกข้อมูลออกเป็นสองกลุ่มตามค่า threshold<br/>
          - ทำซ้ำขั้นตอนสำหรับแต่ละกลุ่มย่อยจนกว่าจะสิ้นสุด<br/>
          - ทำการจำแนกโดยตามเส้นทางจากโหนดรากถึงใบ
        </div>
      </div>

      {/* Model Development Steps */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>3. ขั้นตอนการพัฒนาโมเดล (Model Development)</h2>
        
        <p style={textStyle}>
          <strong>ขั้นตอนที่ 1: เตรียมข้อมูล</strong>
        </p>
        <div style={listStyle}>
          - โหลดและตรวจสอบข้อมูล<br/>
          - ทำความสะอาดและจัดการค่าสูญหาย<br/>
          - Encoding และ Scaling ข้อมูล
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 2: สร้างและฝึกโมเดล</strong>
        </p>
        <div style={listStyle}>
          - สร้างอินสแตนซ์ของ KNN, SVM, และ Decision Tree<br/>
          - ฝึกโมเดลด้วยข้อมูล training<br/>
          - ปรับแต่งไฮเปอร์พารามิเตอร์เพื่อเพิ่มประสิทธิภาพ
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 3: ประเมินและทดสอบ</strong>
        </p>
        <div style={listStyle}>
          - ประเมินประสิทธิภาพด้วยข้อมูล testing<br/>
          - คำนวณ accuracy score และ confidence level<br/>
          - เปรียบเทียบผลลัพธ์ของอัลกอริทึมต่างๆ
        </div>

        <p style={{...textStyle, marginTop: "20px"}}>
          <strong>ขั้นตอนที่ 4: บันทึกและติดตั้ง</strong>
        </p>
        <div style={listStyle}>
          - บันทึกโมเดลและ label encoder<br/>
          - สร้าง API สำหรับการทำนาย<br/>
          - ติดตั้ง web interface เพื่อใช้งาน
        </div>
      </div>

      {/* Data Sources */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>4. แหล่งอ้างอิงข้อมูล (Data Sources)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>Heart Disease Dataset</h3>
        <p style={textStyle}>
          ชุดข้อมูลโรคหัวใจถูกเก็บรวบรวมจากการศึกษาทางการแพทย์ที่มีมาตรฐานสูง ประกอบด้วยข้อมูลอาการและผลการวินิจฉัยของผู้ป่วยจำนวนมากจากหลายสปตาล์
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>Car Evaluation Dataset</h3>
        <p style={textStyle}>
          ชุดข้อมูลการประเมินรถยนต์มาจากการศึกษาเกี่ยวกับการประเมินคุณภาพรถยนต์ ประกอบด้วยข้อมูลลักษณะเฉพาะและการประเมินการใช้งาน
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ไลบรารี่และเครื่องมือที่ใช้</h3>
        <div style={listStyle}>
          - <strong>scikit-learn:</strong> สำหรับพัฒนาโมเดล ML<br/>
          - <strong>pandas:</strong> สำหรับการจัดการข้อมูล<br/>
          - <strong>numpy:</strong> สำหรับการคำนวณตัวเลข<br/>
          - <strong>joblib:</strong> สำหรับบันทึกและโหลดโมเดล
        </div>
      </div>

      {/* Results Section */}
      <div style={sectionStyle}>
        <h2 style={subTitleStyle}>5. ผลลัพธ์ (Results)</h2>
        
        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333"}}>ชุดข้อมูลโรคหัวใจ</h3>
        <p style={textStyle}>
          โมเดลสามารถทำนายโรคหัวใจให้มีความแม่นยำสูง การรวมผลลัพธ์จากอัลกอริทึมสามตัวช่วยให้ได้ผลการทำนายที่สมดุลและเชื่อถือได้มากขึ้น
        </p>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ชุดข้อมูลประเมินรถยนต์</h3>
        <p style={textStyle}>
          โมเดลสามารถจำแนกประเภทรถยนต์ตามคุณภาพได้อย่างมีประสิทธิภาพ ความแม่นยำสูงแสดงว่าอัลกอริทึมสามารถจับลักษณะเฉพาะของข้อมูลได้ดี
        </p>
      </div>
    </div>
  );
}

export default MLReport;