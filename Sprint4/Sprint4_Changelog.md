## Sprint 4 Changelog

บันทึกการเปลี่ยนแปลงประจำ Sprint 4 (AI Integration, DevOps, CI/CD & Project Closure)
ของโปรเจกต์ **ระบบแนะนำสีทาเล็บจากโทนผิว (Nail Color Recommender)**
รูปแบบอิงตาม [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) และ [Semantic Versioning](https://semver.org/)

---

### [4.2.0] — Project Closure & Documentation

### Changed

* **ปรับเอกสารจำนวนเคสทดสอบให้ตรงกับจริง:** อัปเดต `TEST.md`, `test_cases/TEST_CASES.md`, `README.md` ให้ระบุ **21 เคส** ตรงกับผล `pytest` จริง และเพิ่มรายการเคสของ Smart Nail Advisory ลงตารางทดสอบ
* **จัดโครงสร้าง Repository ราย Sprint:** จัดสแน็ปช็อต `Sprint1/`, `Sprint2/`, `Sprint3/`, `Sprint4/` (แต่ละโฟลเดอร์คือสถานะโค้ดเมื่อจบ Sprint นั้น พร้อม README/รายงาน) และโค้ดเวอร์ชันล่าสุดอยู่ที่ราก repo
* **ย้ายเอกสารมาไว้ที่รากโปรเจกต์:** `PLAN.md`, `FLOWCHART.md`, `LEARNINGLOG.md`, `GITHUB_SETUP.md` และเพิ่ม `PRESENTATION_SLIDE_PROMPTS.md`

### Fixed

* **Regression Test ปิดโครงการ:** ทดสอบ End-to-End ครบทุกองค์ประกอบ Sprint 1–4 ยืนยันว่าชุดทดสอบอัตโนมัติผ่านครบ 21 เคส และเว็บแดชบอร์ดทำงานถูกต้องทั้งสองภาษา

---

### [4.1.0] — DevOps & CI/CD Pipeline

### Added

* **CI Pipeline (`.github/workflows/ci.yml`):** รัน `pytest` อัตโนมัติทุกครั้งที่ push หรือเปิด Pull Request เข้า Branch `main` เพื่อตรวจคุณภาพโค้ดก่อนรวมเข้าโปรเจกต์
* **GitHub Pages Deployment (`.github/workflows/static.yml`):** Deploy เว็บแดชบอร์ด (`index.html`) ขึ้น GitHub Pages อัตโนมัติเมื่อมีการ push เข้า `main`
* **`pytest.ini`:** เพิ่มไฟล์คอนฟิกการค้นหา/รันเทสต์ (testpaths, python_files ฯลฯ)

### Security

* **ไม่มี Secret ใดต้องเก็บใน repo:** การเชื่อม External API (TheColorAPI) เป็นแบบสาธารณะไม่ต้องใช้ API key และระบบมี Defensive Fallback เมื่อ API ล่ม จึงไม่มีข้อมูลลับต้องฝังในซอร์สโค้ด

---

### [4.0.0] — Smart Nail Advisory (AI แบบ Explainable)

### Added

* **โมดูลที่ปรึกษา AI (`src/advisory.py`, คลาส `NailAdvisory`):** รวมผลวิเคราะห์ (undertone + ITA + ทรง + ความยาวเล็บ) เป็นคำแนะนำเชิงลึก — ทิศทางสีประจำตัว, **% ความมั่นใจ** (คำนวณจากระยะห่างของ ITA ถึงเส้นแบ่งโทน), ฟินิช/เนื้อสีที่เหมาะ และเคล็ดลับการดูแล แบบ rule-based ที่อธิบายเหตุผลได้ทุกข้อ (ไม่ใช่กล่องดำ)
* **แสดงผล Advisory ทั้ง CLI และเว็บ:** พิมพ์กล่อง Smart Nail Advisory ในผลลัพธ์ CLI และแสดงเป็นการ์ดบนเว็บแดชบอร์ด (สองภาษา TH/EN)
* **Unit Test สำหรับ Advisory:** เพิ่ม 4 เคสใน `tests/test_nail.py` (โครงสร้างผลลัพธ์, % ความมั่นใจไกล/ใกล้เส้นแบ่ง, unknown = 0%, ฟินิชต่างกันตามความยาว) รวมชุดทดสอบทั้งโครงการเป็น **21 เคส**

### Changed

* **การแสดงผลลัพธ์ในเว็บ:** เพิ่มการ์ด Advisory ต่อท้ายผลวิเคราะห์โทนผิว โดยคงโฟกัสที่การ "วิเคราะห์โทนผิวและแนะนำสี" เป็นหลัก
