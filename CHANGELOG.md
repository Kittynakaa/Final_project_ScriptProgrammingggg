# Changelog

บันทึกการเปลี่ยนแปลงสำคัญของโปรเจกต์ **ระบบแนะนำสีทาเล็บจากโทนผิว**
รูปแบบอิงตาม [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
และใช้ [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

---

## [v0.4.0] — Final Sprint: DevOps, CI/CD & AI Integration
### Added
- **ฟีเจอร์ AI — Smart Nail Advisory** (`src/advisory.py`, คลาส `NailAdvisory`):
  ที่ปรึกษาสีทาเล็บแบบ *rule-based + explainable* (อธิบายเหตุผลได้ทุกข้อ ไม่ใช่กล่องดำ)
  รวมผลวิเคราะห์ทั้งหมด (undertone + ITA + ทรง + ความยาวเล็บ) เป็นคำแนะนำเชิงลึก:
  ทิศทางสีประจำตัว, **% ความมั่นใจ** (คำนวณจากระยะห่างของ ITA ถึงเส้นแบ่งโทน),
  ฟินิช/เนื้อสีที่เหมาะ และเคล็ดลับการดูแล
- แสดงกล่อง Smart Nail Advisory ทั้งในผลลัพธ์ CLI และบนเว็บแดชบอร์ด (สองภาษา TH/EN)
- **CI/CD Pipeline** (`.github/workflows/ci.yml`): รัน `pytest` อัตโนมัติทุก push/PR
- เพิ่มชุดทดสอบ `NailAdvisory` 4 เคส รวมเป็น **21 เคส** (ผ่าน 100%)
- เพิ่ม `pytest.ini` ตั้งค่าการค้นหาเทสต์

### Changed
- **ปรับโครงสร้าง repository ใหม่** ให้แยกเป็นสแน็ปช็อตราย Sprint: `Sprint1/`,
  `Sprint2/`, `Sprint3/` (แต่ละโฟลเดอร์คือสถานะโค้ดเมื่อจบ Sprint นั้น พร้อม `README.md`)
  ส่วนโค้ดเวอร์ชันล่าสุด/สมบูรณ์อยู่ที่ราก repo
- ย้ายเอกสาร (`PLAN.md`, `FLOWCHART.md`, `LEARNINGLOG.md`, `GITHUB_SETUP.md`) มาไว้ที่รากโปรเจกต์
- เพิ่ม `PRESENTATION_SLIDE_PROMPTS.md` (โครงบทนำเสนอ 5 ส่วน)

### Roles (Final Sprint)
- **Planner:** ออกแบบ logic ของ Smart Nail Advisory และวางโครงสร้าง repo ราย Sprint
- **Coder:** พัฒนา `NailAdvisory` + พอร์ตขึ้นเว็บ และตั้งค่า CI/CD
- **Debugger:** เขียนเทสต์ advisory, ตรวจความถูกต้อง % ความมั่นใจ, ตรวจ CI ผ่าน

---

## [v0.3.0] — Sprint 3: Web Dashboard & GitHub Pages Deployment
### Added
- `index.html`: หน้าเว็บแดชบอร์ด client-side — อัปโหลดรูป → วิเคราะห์โทนผิว (skin mask + ITA ใน JavaScript) → แนะนำพาเลตสี
- รองรับสองภาษา (TH/EN toggle) และดีไซน์ Glassmorphism
- ดึงชื่อสีจริงจาก TheColorAPI ในฝั่งเบราว์เซอร์ พร้อม fallback
- `.github/workflows/static.yml`: Deploy หน้าเว็บขึ้น GitHub Pages อัตโนมัติ

### Roles (Sprint 3)
- **Planner:** ออกแบบ flow หน้าเว็บและ UI สองภาษา
- **Coder:** พอร์ตอัลกอริทึม ITA/skin mask เป็น JavaScript + หน้าเว็บ
- **Debugger:** ทดสอบการวิเคราะห์ในเบราว์เซอร์และตั้งค่า GitHub Pages deploy

---

## [v0.2.1] — Sprint 2 (เพิ่มเติม): External API Integration
### Added
- `src/api_client.py` (`ColorApiClient`): เชื่อม External API (TheColorAPI) ดึงชื่อสีจริงของแต่ละโค้ดสีในพาเลต
- ระบบ Defensive Fallback: ใช้ชื่อสีสำรองเมื่อ API ล่ม/ไม่มีเน็ต โปรแกรมไม่ล่ม
- แสดงชื่อสี + แหล่งที่มา (API/สำรอง) ในผลลัพธ์ CLI
- เพิ่มชุดทดสอบ API (`test_fallback_color_names_exist`, `test_enrich_palette_structure`) รวมเป็น 17 เคส

---

## [v0.2.0] — Sprint 2: Image Analysis, Recommender & File I/O
### Added
- `SkinAnalyzer`: ตรวจจับผิว (YCrCb + morphology) และประเมินโทนผิวด้วย ITA (CIE Lab)
- `NailRecommender`: แนะนำสีแบบ rule-based พร้อม search / filter_by_tag / sort
- ระบบ data-driven: โหลดกฎพาเลตจาก `data/palette_rules.json`
- `DataStore`: บันทึกประวัติผลวิเคราะห์ลง `output/history.json`
- `PaletteRenderer`: วาดและบันทึกภาพพาเลตเป็น `.png`
- ชุดทดสอบอัตโนมัติ `tests/test_nail.py` (15 เคส, ผ่าน 100%)

### Changed
- ย้ายคำแนะนำสำหรับเล็บสั้น (micro-French) ให้แสดงลำดับต้น จึงปรากฏใน 6 อันดับแรก

### Roles (Sprint 2)
- **Planner:** ออกแบบกฎ Undertone → Palette และ Definition of Done
- **Coder:** พัฒนา SkinAnalyzer, NailRecommender, DataStore, PaletteRenderer
- **Debugger:** เขียน unit tests, ตรวจ Edge Cases และ Exception Handling

---

## [v0.1.0] — Sprint 1: CLI Foundation & OOP Architecture Skeleton
### Added
- โครงไดเรกทอรี `src/`, `data/`, `tests/`, `docs/`, `output/`
- โครงคลาส OOP: `NailApp`, `Suggestion`, `AnalysisResult`
- CLI 2 โหมด (โต้ตอบ / ระบุอาร์กิวเมนต์) พร้อม Input Validation
- จัดการข้อผิดพลาด: ไฟล์ไม่พบ, ไฟล์ไม่ใช่รูป, `KeyboardInterrupt` / `EOFError`
- `PLAN.md` กำหนดขอบเขตงานและ Definition of Done

### Roles (Sprint 1)
- **Planner:** วางสถาปัตยกรรม 3 เลเยอร์ และ Definition of Done
- **Coder:** พัฒนาโครง CLI และการรับ/ตรวจสอบ input
- **Debugger:** ทดสอบการทำงานเบื้องต้นและการจัดการข้อผิดพลาด

---

## [Unreleased] — Roadmap (ต่อยอดในอนาคต)
- ปรับความแม่นยำการตรวจจับ "เล็บ" ให้แยกจากผิวได้ดีขึ้น และเก็บ Edge Cases เพิ่ม
- ต่อยอด AI: virtual try-on ทาสีบนเล็บจริง / โมเดล ML จำแนกทรงเล็บ-โทนผิวอัตโนมัติ
