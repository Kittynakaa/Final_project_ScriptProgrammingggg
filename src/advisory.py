"""
NailAdvisory (Business Logic Layer — AI / Explainable Advisory)
===============================================================
ฟีเจอร์ "ที่ปรึกษาสีทาเล็บอัจฉริยะ" (Smart Nail Advisory) ของ Final Sprint

เป็น AI แบบ *rule-based + explainable* กล่าวคือ ไม่ใช่กล่องดำ (black box) แต่
ตัดสินใจจาก "กฎ" ที่อธิบายเหตุผลได้ทุกข้อ โดยรวมผลวิเคราะห์ทั้งหมด
(โทนผิว + ค่า ITA + ทรงเล็บ + ความยาวเล็บ) มาสรุปเป็นคำแนะนำเชิงลึก:

  1. ระดับความมั่นใจของการจำแนกโทนผิว (confidence) — คำนวณจากระยะห่างของ ITA
     ถึงเส้นแบ่ง cool/warm/neutral  (ยิ่งไกลเส้นแบ่ง ยิ่งมั่นใจ)
  2. ทิศทางสีประจำตัว (signature direction) — เย็น/อุ่น/กลาง ควรเล่นโทนไหน
  3. เนื้อสี/ฟินิชที่เหมาะกับความยาวเล็บ (finish)
  4. เคล็ดลับการดูแล/โอกาสใช้งาน (care tip)
  5. explainable_summary — สรุปเหตุผลทั้งหมดเป็นประโยคเดียว

ปลอดภัยกับทุก encoding (ASCII) และไม่พึ่งอินเทอร์เน็ต — ทดสอบได้ 100%
"""

from typing import Dict

from .skin_analyzer import SkinAnalyzer


class NailAdvisory:
    """ประเมินผลวิเคราะห์ทั้งหมดเพื่อสร้างคำแนะนำเชิงลึกที่อธิบายเหตุผลได้"""

    # ทิศทางสีประจำแต่ละโทนผิว (เหตุผลประกอบ)
    DIRECTION = {
        "cool": (
            "Cool / Jewel",
            "ผิวโทนเย็น (undertone อมชมพู-ฟ้า) ขับสีกลุ่มอัญมณีและเมทัลลิกเงิน "
            "เช่น ม่วงพลัม ฟ้าคราม แดงอมฟ้า และโครมเงิน ได้สวยที่สุด",
        ),
        "warm": (
            "Warm / Earthy",
            "ผิวโทนอุ่น (undertone อมเหลือง-ทอง) เข้ากับสีเอิร์ธโทนและทองคำ "
            "เช่น นู้ดคาราเมล ส้มปะการัง เขียวมะกอก และกลิทเตอร์ทอง",
        ),
        "neutral": (
            "Neutral / Versatile",
            "ผิวโทนกลางเล่นได้ทั้งโทนเย็นและอุ่น เน้นสีคลาสสิกอย่างแดงเลือดหมู "
            "นู้ดชมพู และเทาชาร์โคล เป็นสีที่ใส่ได้ทุกโอกาส",
        ),
        "unknown": (
            "Unknown",
            "ภาพมีพิกเซลผิวน้อยเกินไป ยังสรุปโทนผิวไม่ได้ — "
            "ลองถ่ายให้เห็นผิวรอบเล็บชัดขึ้นในแสงธรรมชาติ",
        ),
    }

    @classmethod
    def _confidence(cls, undertone: str, ita: float) -> int:
        """
        ความมั่นใจ (%) ของการจำแนกโทนผิว — ยิ่ง ITA ห่างจากเส้นแบ่งยิ่งมั่นใจ
        อธิบายได้: ค่าใกล้เส้น 10/28 องศา = ก้ำกึ่ง = มั่นใจน้อย
        """
        if undertone == "unknown":
            return 0
        if undertone == "cool":
            margin = ita - SkinAnalyzer.ITA_COOL          # เลยเส้น cool ไปมากเท่าไร
        elif undertone == "warm":
            margin = SkinAnalyzer.ITA_WARM - ita          # ต่ำกว่าเส้น warm มากเท่าไร
        else:  # neutral — อยู่กลางช่วง ยิ่งใกล้กึ่งกลางยิ่งมั่นใจ
            mid = (SkinAnalyzer.ITA_WARM + SkinAnalyzer.ITA_COOL) / 2
            half = (SkinAnalyzer.ITA_COOL - SkinAnalyzer.ITA_WARM) / 2
            margin = half - abs(ita - mid)
        # แปลง margin (องศา) เป็น % โดยอิ่มตัวที่ ~18 องศา
        conf = 50 + min(max(margin, 0.0), 18.0) / 18.0 * 49
        return int(round(conf))

    @classmethod
    def _finish(cls, nail_shape: str, nail_length: str) -> str:
        """เนื้อสี/ฟินิชที่เหมาะกับความยาว/ทรงเล็บ (อธิบายเหตุผล)"""
        if nail_length == "short" or nail_shape == "round":
            return ("เล็บสั้น/ทรงกลม: เน้นฟินิชเงากระจก (glossy) สีเดียวเกลี้ยง "
                    "หรือ micro-French ขอบบาง เพื่อให้นิ้วดูเรียวยาวขึ้น")
        if nail_shape in ("oval", "almond"):
            return ("ทรงรี/อัลมอนด์: เหมาะกับไล่เฉด ombré แนวตั้ง หรือออโรร่ามุก "
                    "ช่วยเสริมความอ่อนช้อยของทรงเล็บ")
        if nail_shape in ("square", "squoval"):
            return ("ทรงเหลี่ยม/สโควอล: เล่นลายกราฟิกเส้นคม คู่สีตัดกัน "
                    "หรือเนื้อแมตต์ ให้ดูเฉียบคม")
        return ("เล็บยาว/สตีลเลตโต: ใส่ลูกเล่นได้เต็มที่ เช่น ปั้นนูน 3D "
                "กลิทเตอร์ หรือ chrome สะท้อนแสง")

    @classmethod
    def _care_tip(cls, nail_length: str) -> str:
        """เคล็ดลับการดูแลตามความยาวเล็บ"""
        if nail_length == "long":
            return "เล็บยาวควรทาเบสโค้ตเสริมความแข็งแรงและเติมท็อปโค้ตทุก 3 วันกันบิ่น"
        if nail_length == "short":
            return "เล็บสั้นดูแลง่าย ทาบำรุงคิวติเคิลสม่ำเสมอเพื่อให้โคนเล็บสุขภาพดี"
        return "ทาเบสโค้ตก่อนลงสีทุกครั้งเพื่อกันสีติดเล็บเหลืองและช่วยให้สีติดทน"

    @classmethod
    def advise(cls, undertone: str, ita: float,
               nail_shape: str, nail_length: str) -> Dict[str, object]:
        """
        รวมผลวิเคราะห์ทั้งหมด -> คืน dict คำแนะนำเชิงลึกที่อธิบายเหตุผลได้
        """
        label, reason = cls.DIRECTION.get(undertone, cls.DIRECTION["unknown"])
        confidence = cls._confidence(undertone, ita)
        finish = cls._finish(nail_shape, nail_length)
        care = cls._care_tip(nail_length)

        summary = (
            f"[AI Advisory] โทนผิว {undertone} (ITA {ita:.1f}, มั่นใจ {confidence}%) "
            f"-> ทิศทางสี {label}. {finish} | {care}"
        )

        return {
            "undertone": undertone,
            "ita": round(float(ita), 1),
            "confidence": confidence,          # 0-99 (%)
            "direction": label,                # ป้ายทิศทางสี
            "direction_reason": reason,         # เหตุผล (explainable)
            "finish": finish,                   # ฟินิช/เนื้อสีที่เหมาะ
            "care_tip": care,                   # เคล็ดลับดูแล
            "explainable_summary": summary,     # สรุปเหตุผลประโยคเดียว
        }
