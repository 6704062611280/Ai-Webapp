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
          - ทำการ normalization โดยใช้ StandardScaler<br/>
          - แบ่งข้อมูลเป็น training และ testing (80:20)<br/>
          - Label encoding สำหรับเอาต์พุต (0: Healthy, 1: Heart disease)
        </div>

        <h3 style={{...subTitleStyle, fontSize: "16px", color: "#333", marginTop: "25px"}}>ชุดข้อมูลประเมินรถยนต์ (Car Evaluation Dataset)</h3>
        <p style={textStyle}>
          • <strong>จำนวนตัวอย่าง:</strong> 1,728 ตัวอย่าง<br/>
          • <strong>จำนวนฟีเจอร์:</strong> 6 ฟีเจอร์ (Buying, Maintenance, Doors, Persons, Lug Boot, Safety)<br/>
          • <strong>ขั้นตอนการเตรียม:</strong>
        </p>
        <div style={listStyle}>
          - Encoding ฟีเจอร์ตัวแปรแบบ categorical<br/>
          - Scaling ข้อมูลให้มีการกระจายตัวแบบสม่ำเสมอ<br/>
          - แบ่งข้อมูลสำหรับ training และ evaluation<br/>
          - Label encoding สำหรับชั้นเรียนผลลัพธ์ (unacc, accept, good, vgood)
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