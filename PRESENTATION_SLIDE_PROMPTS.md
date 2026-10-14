# Presentation Slide Prompts — Live Demo (โครงสร้าง 5 ส่วน)

ชุด Prompt / โครงบทสำหรับสร้างสไลด์และเตรียมนำเสนอสด (Live Demo) ของโปรเจกต์
**ระบบแนะนำสีทาเล็บจากโทนผิว (Nail Color Recommender)** ตามโครงสร้าง 5 ส่วนหลัก
ของวิชา CP352301 Script Programming

---

### ส่วนที่ 1: ปัญหา สถาปัตยกรรม และการออกแบบ (20%)
```text
เน้นปัญหา: การเลือกสีทาเล็บให้เข้ากับ "โทนผิว" เป็นเรื่องที่คนส่วนใหญ่ตัดสินใจยาก
และมักลองผิดลองถูก — ระบบนี้วิเคราะห์โทนผิวจากรูปถ่ายให้อัตโนมัติแล้วแนะนำพาเลตสี

นำเสนอสถาปัตยกรรม OOP 3 ชั้น:
  - Presentation : NailApp / CLI (src/cli.py), เว็บแดชบอร์ด (index.html)
  - Business Logic : SkinAnalyzer, NailRecommender, NailAdvisory, ColorApiClient, Models
  - Data Access : DataStore (palette_rules.json / history.json), PaletteRenderer

พร้อมตารางหมุนเวียนบทบาท (Role Rotation Matrix) ของสมาชิกใน 4 Sprint
(Planner / Coder / Debugger)
```

### ส่วนที่ 2: Stack เทคโนโลยีและมาตรฐานการพัฒนา (10%)
```text
Tech Stack: Python 3.x (OOP), OpenCV + NumPy (Computer Vision: YCrCb skin mask,
CIE Lab / ITA), requests + TheColorAPI (External API ดึงชื่อสีจริง),
Pillow/Matplotlib, pytest (ชุดทดสอบอัตโนมัติ), เว็บ client-side (HTML/CSS/JS)

กระบวนการพัฒนา: Agile ราย Sprint + Keep a Changelog / Semantic Versioning,
ระบบ data-driven (แก้กฎสีได้ใน JSON ไม่ต้องแตะโค้ด),
Responsible AI Learning Log (docs: LEARNINGLOG.md)
```

### ส่วนที่ 3: การสาธิตฟังก์ชันและการทดสอบจริง (40% — Live Demo หลัก)
```text
สาธิตสด:
  1) รัน CLI:  python main.py hand.jpg almond long
     → แสดงโทนผิว + ค่า ITA + พาเลตสีพร้อม "ชื่อสีจริง" จาก TheColorAPI
     → แสดงกล่อง 🤖 Smart Nail Advisory (ทิศทางสี + % ความมั่นใจ + ฟินิช + เคล็ดลับ)
     → บันทึกภาพพาเลต (output/) และประวัติ (history.json)
  2) เปิดเว็บแดชบอร์ด (index.html / GitHub Pages): อัปโหลดรูป → วิเคราะห์ในเบราว์เซอร์
     → สลับภาษา TH/EN
  3) สาธิต search / filter / sort คำแนะนำ
```

### ส่วนที่ 4: ปัญหาทางเทคนิค การแก้ไข และการเปรียบเทียบ (15%)
```text
ปัญหาที่พบและวิธีแก้:
  - API ล่ม / ไม่มีเน็ต / timeout → Defensive Fallback (FALLBACK_COLOR_NAMES)
    โปรแกรมไม่ crash และบอกผู้ใช้ว่าดึงชื่อสีจาก "ออนไลน์" หรือ "สำรอง"
  - ภาพมีพิกเซลผิวน้อย → คืนค่า "unknown" อย่างปลอดภัย (ไม่เดามั่ว)
  - แยกเล็บจากผิว → ใช้ YCrCb + morphology + เลือก connected component ที่ใหญ่สุด
  - Exception handling: ไฟล์ไม่พบ / ไม่ใช่รูป / Ctrl+C / Ctrl+D
```

### ส่วนที่ 5: DevOps, CI/CD Pipeline & AI Integration (15%)
```text
  - CI/CD ผ่าน GitHub Actions: รัน pytest ทุก push/PR (.github/workflows/ci.yml)
  - Deploy เว็บขึ้น GitHub Pages อัตโนมัติ (.github/workflows/static.yml)
  - ฟีเจอร์ AI: Smart Nail Advisory — rule-based + explainable
    (อธิบายเหตุผลทุกคำแนะนำได้ ไม่ใช่กล่องดำ) รวมผลวิเคราะห์ทั้งหมด
    (undertone + ITA + ทรง + ความยาว) เป็นคำแนะนำเชิงลึก + % ความมั่นใจ
  - แนวทางต่อยอด: virtual try-on ทาสีบนเล็บจริง, โมเดล ML จำแนกทรงเล็บอัตโนมัติ
```
