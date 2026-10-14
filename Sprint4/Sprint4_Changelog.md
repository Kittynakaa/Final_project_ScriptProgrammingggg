## Sprint 4 Changelog

บันทึกการเปลี่ยนแปลงประจำ Sprint 4 (Virtual Try-On, Smart Nail Advisory, DevOps & Project Closure)
ของโปรเจกต์ **ระบบแนะนำสีทาเล็บจากโทนผิว (Nail Color Recommender)**
รูปแบบอิงตาม [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) และ [Semantic Versioning](https://semver.org/)

---

### [4.3.0] — Virtual Try-On Production Fixes

### Fixed

* **สีทาเล็บไม่แสดงบนจอ (ต้องบันทึกรูปก่อนถึงเห็น):** แก้กฎ CSS จาก `canvas{display:none}` (ซึ่งเผลอซ่อน canvas ของ Virtual Try-On) ให้เจาะจงเป็น `#canvas{display:none}` และเพิ่ม `#tryCanvas{display:block}` ทำให้สีแสดงบนจอทันทีโดยไม่ต้องบันทึกรูป
* **สีลงเลยขอบเล็บไปโดนพื้นหลัง:** เพิ่ม **Dark-pixel Clipping** ใน `paintNail()` — ไม่ลงสีบนพิกเซลที่มืดมาก (luminance < 0.30) จึงไม่ทาเลอะพื้นหลังมืดรอบเล็บ

### Changed

* **ปรับขนาด/ตำแหน่งวงรีเล็บให้พอดีขึ้น:** คำนวณขนาดเล็บจาก bounding box ของปลายเล็บที่ตรวจพบจริง แล้วเลื่อนศูนย์กลางไล่ลงมาตามแนวนิ้ว (อิงจุดกึ่งกลางมือจาก skin mask โดยตัดส่วนล่างที่เป็นผ้า/ข้อมือออก)
* **เพิ่มความสดของสี:** ปรับสูตร colorize ให้ผสมความสว่างของสีที่เลือกมากขึ้น เพื่อให้สีเด่นขึ้นบนปลายเล็บสีขาว (French tip) แต่ยังคงแสง-เงาเดิม
* **ซิงก์ป้ายปุ่มภาษา:** เรียก `setLang("th")` ตอนโหลดหน้า ให้ข้อความปุ่ม/คำอธิบายตรงกับ i18n ทั้งหมด

---

### [4.2.0] — Virtual Try-On (ทาสีเล็บจริงบนรูป)

### Added

* **ตรวจจับเล็บอัตโนมัติในเครื่อง (`detectNails()`):** หาปลายเล็บที่สว่าง + อิ่มตัวต่ำ, จัดกลุ่มด้วย Connected Components (flood fill), ใช้ PCA หาทิศทาง/ขนาดของเล็บ และกรองด้วยความใกล้เคียงกับผิว (skin proximity) — ทำงานฝั่ง client ทั้งหมด ไม่พึ่งอินเทอร์เน็ต
* **เครื่องมือลงสีคงแสง-เงา (`paintNail()`):** ลงสีด้วยวิธี colorize ใน HSL (ใช้ hue/saturation ของสีที่เลือก คง luminance เดิมของเล็บ) ให้ผลลัพธ์ดูเป็นธรรมชาติเหมือนทาสีจริง
* **ทาสีอัตโนมัติทันทีหลังวิเคราะห์ + เปลี่ยนสีทันที:** กดวิเคราะห์แล้วระบบทาสีให้ทุกนิ้วเลย และเลือกสีใหม่ (จากพาเลตแนะนำหรือ color picker) เพื่อวาดใหม่ทันที
* **โหมดแตะทาเอง + เครื่องมือปรับแต่ง:** แตะบนเล็บเพื่อทาเฉพาะจุด, สไลเดอร์ขนาดแปรง/ความเข้ม, ปุ่มย้อนกลับ (undo stack), รีเซ็ตกลับรูปต้นฉบับ และบันทึกรูปผลลัพธ์ (`nail_tryon.png`)
* **UI สองภาษา (TH/EN):** ป้ายและคำอธิบายของ Virtual Try-On รองรับทั้งไทยและอังกฤษ

---

### [4.1.0] — Smart Nail Advisory (AI แบบ Explainable)

### Added

* **โมดูลที่ปรึกษา AI (`src/advisory.py`, คลาส `NailAdvisory`):** รวมผลวิเคราะห์ (undertone + ITA + ทรง + ความยาวเล็บ) เป็นคำแนะนำเชิงลึก — ทิศทางสีประจำตัว, **% ความมั่นใจ** (คำนวณจากระยะห่างของ ITA ถึงเส้นแบ่งโทน), ฟินิช/เนื้อสีที่เหมาะ และเคล็ดลับการดูแล แบบ rule-based ที่อธิบายเหตุผลได้ทุกข้อ
* **แสดงผล Advisory ทั้ง CLI และเว็บ:** พิมพ์กล่อง Smart Nail Advisory ในผลลัพธ์ CLI และแสดงเป็นการ์ดบนเว็บ (สองภาษา)
* **Unit Test สำหรับ Advisory:** เพิ่ม 4 เคสใน `tests/test_nail.py` (โครงสร้างผลลัพธ์, % ความมั่นใจไกล/ใกล้เส้นแบ่ง, unknown = 0%, ฟินิชต่างกันตามความยาว) รวมเป็น **21 เคส**

---

### [4.0.0] — DevOps, CI/CD & Repository Restructure

### Added

* **CI Pipeline (`.github/workflows/ci.yml`):** รัน `pytest` อัตโนมัติทุกครั้งที่ push หรือเปิด Pull Request เข้า Branch `main`
* **GitHub Pages Deployment (`.github/workflows/static.yml`):** Deploy เว็บแดชบอร์ด (`index.html`) ขึ้น GitHub Pages อัตโนมัติ
* **`pytest.ini`:** เพิ่มไฟล์คอนฟิกการค้นหา/รันเทสต์
* **โครงสร้าง Repository ราย Sprint:** แยกสแน็ปช็อต `Sprint1/`, `Sprint2/`, `Sprint3/`, `Sprint4/` (แต่ละโฟลเดอร์คือสถานะโค้ดเมื่อจบ Sprint นั้น พร้อม README/รายงาน) และโค้ดเวอร์ชันล่าสุดอยู่ที่ราก repo

### Changed

* **ย้ายเอกสารมาไว้ที่รากโปรเจกต์:** `PLAN.md`, `FLOWCHART.md`, `LEARNINGLOG.md`, `GITHUB_SETUP.md` และเพิ่ม `PRESENTATION_SLIDE_PROMPTS.md`

### Security

* **ไม่ฝังข้อมูลลับในซอร์สโค้ด:** การเชื่อม External API (TheColorAPI) เป็นแบบสาธารณะไม่ต้องใช้ API key และระบบมี Defensive Fallback เมื่อ API ล่ม จึงไม่มี secret ใดต้องเก็บใน repo
