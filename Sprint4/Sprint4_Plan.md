## เอกสารแผนงาน สถาปัตยกรรม และรายงานผลการทดสอบประจำ Sprint 4

**ชื่อโปรเจกต์:** ระบบแนะนำสีทาเล็บจากโทนผิว (Nail Color Recommender / NailTone)

**วิชา:** CP352301 Script Programming | **ภาคการศึกษา:** 1/2569

**ระยะเวลา:** Sprint 4 (สัปดาห์ที่ 15: AI Integration, DevOps, CI/CD Deployment & Project Closure)

---

### 1. วัตถุประสงค์และขอบเขตโครงการ (Project Purpose & Scope)

ต่อยอดจากเว็บแดชบอร์ด client-side ใน Sprint 3 โดยเพิ่มฟีเจอร์ **ที่ปรึกษาสีทาเล็บอัจฉริยะ (Smart Nail Advisory)** แบบ AI ที่อธิบายเหตุผลได้ (explainable) จัดวางระบบ **DevOps / CI-CD** ให้ครบ และปิดโครงการด้วยการทดสอบ End-to-End ครบทั้ง 4 Sprint โดยระบบยังคงโฟกัสที่การ **"วิเคราะห์โทนผิวและแนะนำสี"** เป็นหลัก (ไม่มีฟีเจอร์ทาสีบนรูป) โดยมีขอบเขตดังนี้:

* พัฒนาฟีเจอร์ **Smart Nail Advisory** (`src/advisory.py`) — รวมผลวิเคราะห์ (undertone + ITA + ทรง + ความยาวเล็บ) เป็นคำแนะนำเชิงลึก: ทิศทางสีประจำตัว, **% ความมั่นใจ** (คำนวณจากระยะห่างของ ITA ถึงเส้นแบ่งโทน), ฟินิช/เนื้อสีที่เหมาะ และเคล็ดลับการดูแล — เป็น rule-based ที่อธิบายเหตุผลได้ทุกข้อ ไม่ใช่กล่องดำ
* แสดงผล Advisory ทั้งบน **CLI** และบน **เว็บแดชบอร์ด** (สองภาษา TH/EN)
* เพิ่มชุดทดสอบอัตโนมัติสำหรับ Advisory ให้ครอบคลุม และรวมชุดทดสอบทั้งโครงการเป็น **21 เคส**
* ตั้งค่า **CI/CD Pipeline**: รัน `pytest` อัตโนมัติทุก push/PR (`ci.yml`) และ Deploy เว็บขึ้น **GitHub Pages** อัตโนมัติ (`static.yml`)
* สรุปปิดโครงการ (Project Wrap-up): ทดสอบระบบ End-to-End ครบทุกองค์ประกอบตั้งแต่ Sprint 1–4, ปรับปรุงเอกสาร/คู่มือการใช้งาน (`README.md`, `GITHUB_SETUP.md`) และจัดโครงสร้าง repository ให้ครบตามข้อกำหนดการส่งงาน (`Sprint1/`–`Sprint4/`)

---

### 2. สถาปัตยกรรมระบบ (Modular Architecture & Separation of Concerns)

สถาปัตยกรรมถูกขยายต่อจากสถาปัตยกรรม OOP 3 ชั้นเดิม โดยเพิ่มโมดูลใหม่ของ Sprint 4 เข้าไป ทั้งนี้ยังคงใช้ **Business Logic Layer** และ **Data Access Layer** ชุดเดิมจาก Sprint 1–2 เป็นแกนกลางร่วมกันทั้งฝั่ง CLI และฝั่งเว็บ:

```text
┌────────────────────────────────────────────────────────────────────────┐
│          MODULE 4: SMART NAIL ADVISORY LAYER (AI, EXPLAINABLE)          │
│  - src/advisory.py (NailAdvisory):                                      │
│      • ทิศทางสีประจำตัว (cool/warm/neutral → jewel/earthy/versatile)     │
│      • % ความมั่นใจ (จากระยะห่างของ ITA ถึงเส้นแบ่งโทน)                  │
│      • ฟินิช/เนื้อสีที่เหมาะกับทรง-ความยาวเล็บ + เคล็ดลับดูแล            │
│  - พอร์ตขึ้นเว็บ (bilingual TH/EN) — rule-based อธิบายเหตุผลได้ทุกข้อ     │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│          MODULE 5: DEVOPS & CI/CD DEPLOYMENT INFRASTRUCTURE             │
│  - .github/workflows/ci.yml     : รัน pytest อัตโนมัติทุก push/PR        │
│  - .github/workflows/static.yml : Deploy เว็บขึ้น GitHub Pages อัตโนมัติ  │
│  - pytest.ini / requirements.txt : คอนฟิกทดสอบและ Dependency             │
└────────────────────────────────────────────────────────────────────────┘

*(ทั้งหมดนี้ยังเรียกใช้ MODULE 1 DATA ACCESS (DataStore, PaletteRenderer)
  และ MODULE 2 BUSINESS LOGIC (SkinAnalyzer, NailRecommender, ColorApiClient)
  ชุดเดิมจาก Sprint 1–2 เป็นแกนกลางร่วมกัน)*
```

---

### 3. นิยามความเสร็จสมบูรณ์ของงาน (Definition of Done - DoD)

งานใน Sprint 4 ถือว่าเสร็จสมบูรณ์ (Done) เมื่อผ่านเกณฑ์ต่อไปนี้ทุกข้อ:

* [x] **Smart Nail Advisory (AI):** แสดงทิศทางสีประจำตัว + % ความมั่นใจ + ฟินิช + เคล็ดลับ ทั้งบน CLI และเว็บ (สองภาษา) แบบ explainable อธิบายเหตุผลได้
* [x] **% ความมั่นใจคำนวณถูกต้อง:** ค่าความมั่นใจสูงขึ้นเมื่อ ITA อยู่ไกลเส้นแบ่งโทน และเป็น 0% เมื่อสรุปโทนผิวไม่ได้ (unknown)
* [x] **ชุดทดสอบอัตโนมัติผ่าน 100%:** `pytest` ครอบคลุม **21 เคส** (undertone/ITA, hex→BGR, suggest/search/filter/sort, External API + fallback, Advisory) ผ่านทั้งหมด
* [x] **CI Pipeline:** `.github/workflows/ci.yml` รัน `pytest` อัตโนมัติทุก push/PR
* [x] **GitHub Pages Deployment:** `.github/workflows/static.yml` deploy `index.html` ขึ้น GitHub Pages อัตโนมัติ เข้าถึงเว็บได้จริง
* [x] **เว็บแดชบอร์ดสองภาษา:** หน้าเว็บวิเคราะห์โทนผิว + แนะนำสี + Advisory รองรับ TH/EN และทำงานฝั่ง client ทั้งหมด
* [x] **Project Closure Regression Test:** ทดสอบ End-to-End ครบทุกองค์ประกอบ Sprint 1–4 และปรับปรุงเอกสาร/คู่มือให้พร้อมส่งมอบ
* [x] **โครงสร้าง Repository ครบตามข้อกำหนด:** แยกสแน็ปช็อต `Sprint1/`–`Sprint4/` พร้อม README/รายงานแต่ละ Sprint และโค้ดเวอร์ชันล่าสุดอยู่ที่ราก repo

---

### 4. แผนการจัดสรรหน้าที่และบทบาทภายในทีม (Team Roles & Responsibilities)

| บทบาท (Role) | สมาชิกที่รับผิดชอบ | ภารกิจหลักใน Sprint 4 |
| --- | --- | --- |
| **Planner / Team Leader** | _____________ | • ออกแบบ logic ของ Smart Nail Advisory (ทิศทางสี + สูตร % ความมั่นใจ)<br>• วางแผนการปิดโครงการและโครงสร้าง repository ราย Sprint<br>• จัดทำเอกสารสรุปแผนงานและรายงานปิดโครงการภาพรวมทั้ง 4 Sprint |
| **Coder** | _____________ | • พัฒนา `src/advisory.py` (NailAdvisory) และพอร์ตขึ้นเว็บ (สองภาษา)<br>• ตั้งค่า CI/CD (`ci.yml`, `static.yml`) และ `pytest.ini`<br>• ปรับปรุงการแสดงผล Advisory ใน CLI และบนหน้าเว็บ |
| **Debugger / QA** | _____________ | • เขียน Unit Test ของ Advisory และตรวจความถูกต้องของ % ความมั่นใจ<br>• ทดสอบการแสดงผลบนเว็บ (สองภาษา) และตรวจ CI/CD ผ่าน<br>• ทำ Regression Test รวบยอดทั้งโครงการ (pytest 21 เคส) ก่อนส่งมอบ |

> _(เติมชื่อ/รหัสสมาชิก และปรับการหมุนเวียนบทบาทให้ตรงกับที่กลุ่มทำจริง)_

---

### 5. ผลการทดสอบระบบและตารางขอบเขตระบบ (QA Testing & Edge Cases Results)

ผู้ทดสอบ (Debugger / QA) ได้ทดสอบฟีเจอร์ของ Sprint 4 ทั้งบนเว็บ, CLI และชุดทดสอบอัตโนมัติ โดยมีผลการทดสอบดังนี้:

| ลำดับ | กรณีทดสอบ (Test Case) | อินพุตนำเข้า (Test Input) | พฤติกรรมที่คาดหวัง vs ผลการทดสอบจริง | สถานะ |
| --- | --- | --- | --- | --- |
| **1** | **วิเคราะห์โทนผิว (Happy Path)** | อัปรูปมือ/เล็บ แล้วกดวิเคราะห์ | ระบบตรวจผิว → คำนวณ ITA → สรุป undertone (cool/warm/neutral) และแนะนำพาเลตสีได้ถูกต้อง | **PASSED** |
| **2** | **Undertone = unknown (ผิวน้อย)** | ภาพที่มีพิกเซลผิวน้อยเกินไป | ระบบคืนค่า `unknown` อย่างปลอดภัยไม่ crash และ Advisory แสดง 0% ความมั่นใจ | **PASSED** |
| **3** | **แนะนำสีตามทรง/ความยาวเล็บ** | เลือกทรง/ความยาวต่างกัน | คำแนะนำพาเลตปรับตามทรง/ความยาว (เช่น เล็บสั้น → micro-French, เล็บยาว → statement 3D) | **PASSED** |
| **4** | **Smart Nail Advisory: โครงสร้าง** | `NailAdvisory.advise("cool",40,"almond","long")` | คืนครบทุกคีย์ (direction, confidence, finish, care, explainable_summary) และ direction ขึ้นต้น "Cool" | **PASSED** |
| **5** | **Advisory: % ความมั่นใจ** | ITA 45 เทียบกับ 29 (โทน cool) | ค่า ITA ที่ไกลเส้นแบ่งให้ความมั่นใจมากกว่า และอยู่ในช่วง 0–99% | **PASSED** |
| **6** | **Advisory: ฟินิชตามความยาว** | เล็บสั้น vs เล็บยาว | คำแนะนำฟินิช/เนื้อสีต่างกันตามความยาวเล็บ | **PASSED** |
| **7** | **External API + Defensive Fallback** | ดึงชื่อสีจาก TheColorAPI ขณะ API ล่ม/ไม่มีเน็ต | ใช้ชื่อสีสำรอง (fallback) แทน ไม่ crash และระบุแหล่งที่มา (ออนไลน์/สำรอง) ถูกต้อง | **PASSED** |
| **8** | **ค้นหา / กรอง / เรียงคำแนะนำ** | `search`, `filter_by_tag`, `sort_by_palette_size` | คืนผลลัพธ์ถูกต้องตามคำค้น/แท็ก/จำนวนสีในพาเลต | **PASSED** |
| **9** | **ชุดทดสอบอัตโนมัติรวบยอด** | `pytest -v` ที่ราก repo | ผ่านทั้งหมด **21 เคส** | **PASSED** |
| **10** | **CI/CD: pytest อัตโนมัติ** | Push โค้ดเข้า Branch `main` / เปิด PR | `.github/workflows/ci.yml` ติดตั้ง `requirements.txt` และรัน `pytest` อัตโนมัติผ่าน | **PASSED** |
| **11** | **CI/CD: Deploy GitHub Pages** | Push โค้ดเว็บเข้า Branch `main` | `.github/workflows/static.yml` deploy `index.html` ขึ้น GitHub Pages อัตโนมัติ เข้าถึงเว็บได้จริง | **PASSED** |
| **12** | **เว็บสองภาษา (TH/EN)** | กดสลับภาษาบนหน้าเว็บ | ข้อความทั้งหน้า (รวมผล Advisory) สลับไทย/อังกฤษถูกต้อง | **PASSED** |

---

### 6. สรุปบทเรียนประจำ Sprint (Sprint Retrospective)

### 🌟 Wow! (จุดเด่นที่ทำได้ดีมาก)

1. **AI แบบ Explainable:** Smart Nail Advisory อธิบายเหตุผลของทุกคำแนะนำได้ (ไม่ใช่กล่องดำ) พร้อม **% ความมั่นใจ** ที่คำนวณจากระยะห่างของค่า ITA ถึงเส้นแบ่งโทน ทำให้ผู้ใช้เข้าใจและเชื่อถือผลได้ และยังเป็น AI ที่ไม่ต้องเทรนโมเดลหนักหรือพึ่งเซิร์ฟเวอร์ภายนอก
2. **CI/CD ครบวงจรและอัตโนมัติ:** ทุกการ push จะรัน `pytest` ตรวจคุณภาพโค้ดและ deploy เว็บขึ้น GitHub Pages ให้อัตโนมัติ ลดงานมือและกันโค้ดเสียหลุดขึ้น main
3. **สถาปัตยกรรมใช้ซ้ำได้ดี:** Business Logic และ Data Access จาก Sprint 1–2 ถูกนำมาใช้ร่วมกันทั้ง CLI และเว็บโดยไม่ต้องเขียนซ้ำ การเพิ่ม Advisory จึงทำได้สะอาดและกระทบส่วนอื่นน้อย

---

### 💡 Whoops! (ปัญหาที่พบและแนวทางการแก้ไข)

1. **จำนวนเคสทดสอบในเอกสารไม่ตรงกับที่รันจริง:**
* *ปัญหา:* ช่วงแรกเอกสาร `TEST.md` / `TEST_CASES.md` ระบุ 15 เคส แต่หลังเพิ่มเทสต์ External API และ Advisory จำนวนจริงเพิ่มเป็น 17 แล้วเป็น 21 ทำให้เอกสารไม่ตรงกับผล `pytest`
* *แนวทางแก้ไข:* ปรับเอกสารทั้งหมดให้ตรงกับจำนวนจริง (21 เคส) เพิ่มรายการเคส Advisory ลงตาราง และทำ Regression ยืนยันว่าผ่านครบทุกเคส

2. **ไฟล์ GitHub Actions Workflow เขียนผ่านเครื่องมือภายนอกไม่ได้:**
* *ปัญหา:* ไฟล์ใน `.github/workflows/` เป็นไฟล์ที่ถูกป้องกัน (protected) การคัดลอกผ่านเครื่องมืออัตโนมัติบางตัวจึงถูกปฏิเสธ
* *แนวทางแก้ไข:* รวมไฟล์ workflow ไว้ในแพ็กเกจส่งมอบ (zip) และอัปขึ้น GitHub ผ่าน `git push` โดยตรง ซึ่งนำไฟล์ `.github/workflows/` ขึ้นไปได้ครบถ้วน
