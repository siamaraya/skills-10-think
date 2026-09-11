#!/usr/bin/env python3
"""
Think-10 CLI: Interactive Toolkit for the 10 Thinking Dimensions Cognitive OS
Based on Prof. Dr. Kriengsak Chareonwongsak's "ผู้ชนะ 10 คิด"
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

DIMENSIONS = {
    "1": ("คิดเชิงวิเคราะห์ (Analytical Thinking)", "ลึก (Deep)", "จำแนกองค์ประกอบและหาความสัมพันธ์เชิงเหตุผล (Root Cause)", [
        "ปัญหานี้ประกอบด้วยองค์ประกอบย่อยอะไรบ้าง จัดหมวดหมู่อย่างไรให้ครบถ้วนและไม่ซ้ำซ้อน (MECE)?",
        "อะไรคืออาการภายนอก (Symptoms) และอะไรคือสาเหตุรากเหง้าที่แท้จริง (Root Cause)?",
        "ปัจจัยใดเชื่อมโยงและส่งผลกระทบถึงกันตามสายใยเหตุและผล (Causal Links)?"
    ]),
    "2": ("คิดเชิงวิพากษ์ (Critical Thinking)", "ลึก (Deep)", "ตรวจสอบข้อสมมติฐาน ความถูกต้อง และความน่าเชื่อถือ (Truth Filter)", [
        "ข้อสรุปนี้ตั้งอยู่บนข้อสมมติฐานอะไร และพิสูจน์ได้หรือไม่?",
        "ข้อมูลส่วนใดเป็นข้อเท็จจริง และส่วนใดเป็นเพียงความคิดเห็นหรืออคติ?",
        "หากข้ออ้างสนับสนุนไม่เป็นความจริง ข้อสรุปนี้ยังคงอยู่ได้หรือไม่? มีตรรกะวิบัติหรือไม่?"
    ]),
    "3": ("คิดเชิงสังเคราะห์ (Synthesis Thinking)", "กว้าง (Broad)", "หลอมรวมองค์ประกอบย่อยให้เกิดเป็นสิ่งใหม่หรือแนวคิดใหม่", [
        "เมื่อดึงแก่นของแต่ละแนวคิดออกมา จะนำมาถักทอเป็นสิ่งใหม่ได้อย่างไร?",
        "องค์ประกอบเดิมเหล่านี้สามารถจัดวางบนแกนโครงร่างใหม่อะไรได้บ้าง?",
        "สิ่งที่สร้างขึ้นใหม่นี้มีคุณสมบัติเฉพาะที่เหนือกว่าผลรวมของส่วนย่อยอย่างไร?"
    ]),
    "4": ("คิดเชิงเปรียบเทียบ (Comparative Thinking)", "กว้าง (Broad)", "ค้นหาความเหมือนและความต่างบนเกณฑ์มาตรฐาน (Pattern Recognition)", [
        "สิ่งเหล่านี้มีความเหมือนและความต่างกันในประเด็นใดบ้าง?",
        "อะไรคือเกณฑ์มาตรฐานร่วม (Common Criteria) ที่ใช้ในการเทียบเคียงอย่างเป็นธรรม?",
        "ปรากฏการณ์นี้เทียบเคียงหรืออุปมาอุปไมยได้กับเรื่องใดในศาสตร์อื่น?"
    ]),
    "5": ("คิดเชิงมโนทัศน์ (Conceptual Thinking)", "ลึก (Deep)", "สกัดแก่นแท้นามธรรมให้กลายเป็นความคิดรวบยอด (Essence in 1 Sentence)", [
        "หากต้องสรุปแก่นสาระสำคัญของเรื่องนี้ในประโยคเดียว คืออะไร?",
        "อะไรคือแบบแผนหรือคุณลักษณะร่วมของปรากฏการณ์ทั้งหมดนี้?",
        "โมเดลหรือแผนภาพใดที่สามารถเป็นตัวแทนภาพรวมของความคิดนี้ได้?"
    ]),
    "6": ("คิดเชิงสร้างสรรค์ (Creative Thinking)", "กว้าง (Broad)", "ผลิตแนวคิดแปลกใหม่ ยืดหยุ่น และสร้างคุณค่าเชิงบวก (4 Pillars)", [
        "มีหนทางอื่นที่ตรงกันข้ามกับแนวทางเดิมอย่างสิ้นเชิงหรือไม่ (Inversion)?",
        "หากตัดข้อจำกัดด้านงบประมาณ กฎหมาย และเวลาออกไป จะมีทางออกอย่างไร?",
        "จะนำสองสิ่งที่ไม่น่าจะเกี่ยวข้องกันมารวมกันเพื่อสร้างมูลค่าใหม่อย่างไร?"
    ]),
    "7": ("คิดเชิงประยุกต์ (Applicative Thinking)", "กว้าง (Broad)", "ถ่ายโอนและดัดแปลงหลักการเดิมไปใช้ในบริบทใหม่ (Thinking Left-to-Right)", [
        "แก่นหลักการนี้เคยสำเร็จในบริบทใด และนำมาใช้ที่นี่ได้อย่างไร (Left-to-Right)?",
        "ต้องดัดแปลง ปรับลด หรือขยายส่วนประกอบใดเพื่อให้เข้ากับเงื่อนไขใหม่?",
        "มีข้อควรระวังหรือผลข้างเคียงอะไรบ้างจากการถ่ายโอนความรู้เดิมมาใช้?"
    ]),
    "8": ("คิดเชิงกลยุทธ์ (Strategic Thinking)", "ไกล (Far)", "กำหนดเป้าหมาย ออกแบบชั้นเชิง และสร้างความได้เปรียบ (Leverage & Moat)", [
        "หมุดหมายแห่งชัยชนะสูงสุดคืออะไร และจะวัดผลสำเร็จอย่างไร?",
        "จุดคานงัดที่ออกแรงน้อยที่สุดแต่สร้างผลลัพธ์มหาศาลอยู่ที่ใด?",
        "เตรียมแผนสำรองอย่างไรหากเกิดสถานการณ์พลิกผัน และสร้างความได้เปรียบยั่งยืนอย่างไร?"
    ]),
    "9": ("คิดเชิงบูรณาการ (Integrative Thinking)", "กว้าง (Broad)", "เชื่อมประสานทุกมิติให้กลมกลืนแบบองค์รวม (Expanding & Encompassing)", [
        "ภาพรวมของระบบนี้มีมิติใดที่ยังถูกมองข้ามหรือแยกส่วน (Silo) อยู่บ้าง?",
        "จะสร้างกรอบใหญ่ที่ครอบคลุมและสลายความขัดแย้งของส่วนย่อยได้อย่างไร?",
        "ทำอย่างไรให้ทุกฝ่ายประสานพลังกันเพื่อให้ผลลัพธ์เกิดพลังทวีคูณ (1+1 > 2)?"
    ]),
    "10": ("คิดเชิงอนาคต (Futuristic Thinking)", "ไกล (Far)", "วิเคราะห์แนวโน้ม คาดการณ์ฉากทัศน์ และเตรียมการล่วงหน้า (Scenarios)", [
        "จากอดีตและปัจจุบัน มีแนวโน้มหรือสัญญาณเตือนล่วงหน้าอะไรบ้าง?",
        "ฉากทัศน์ที่เป็นไปได้ทั้งกรณีดีสุด ปกติ และเลวร้ายสุดมีหน้าตาอย่างไร?",
        "ต้องเริ่มลงมือทำอะไรในวันนี้เพื่อกำหนดอนาคตที่พึงประสงค์ในระยะยาว?"
    ])
}

DOSSIER_TEMPLATE = """# บันทึกยุทธศาสตร์ 10 มิติ (10-Think Executive Dossier)
**หัวข้อ/โจทย์ยุทธศาสตร์:** {topic}  
**วันที่จัดทำ:** {date}  
**กรอบการวิเคราะห์:** ผู้ชนะ 10 คิด (กว้าง - ลึก - ไกล)  

---

## 1. แก่นแท้แห่งโจทย์ (Conceptual Essence)
- **นิยามโจทย์แท้จริงใน 1 ประโยค:** [ระบุแก่นแท้ของโจทย์ที่ผ่านการสกัดแล้ว]
- **มโนทัศน์และภาพรวม (The Big Picture):** [ภาพรวมของสถานการณ์]

---

## 2. การขุดค้นเชิงลึก (Deep Dimension Analysis)
- **การคิดเชิงวิเคราะห์ (Root Cause Tree):**
  - อาการภายนอก (Symptoms): 
  - สายใยความสัมพันธ์เชิงเหตุและผล (Causal Links): 
  - รากเหง้าที่แท้จริง (Root Cause - 5 Whys): 
- **การคิดเชิงวิพากษ์ (Truth & Assumption Verification):**
  - ข้อเท็จจริงที่พิสูจน์แล้ว (Verified Facts): 
  - สมมติฐานเดิมที่ต้องท้าทาย (Assumptions Challenged): 
  - อคติหรือตรรกะวิบัติที่ต้องระวัง (Fallacies / Biases): 

---

## 3. ทางออกและนวัตกรรมเชิงกว้าง (Broad Dimension Formulation)
- **การคิดเชิงเปรียบเทียบ (Cross-domain Benchmarks & Metaphors):**
  - กรณีศึกษาเทียบเคียงจากวงการอื่น: 
  - เมทริกซ์เกณฑ์มาตรฐานร่วม (Common Criteria): 
- **การคิดเชิงสร้างสรรค์ (Divergent Innovations):**
  - ไอเดียนอกกรอบ / การคิดกลับด้าน (Inversion): 
- **การคิดเชิงประยุกต์ (Applicative Transfer: Left-to-Right):**
  - กลไกต้นทาง -> การดัดแปลง -> โซลูชันปลายทาง: 
- **การคิดเชิงสังเคราะห์ (Unified Solution Architecture):**
  - สถาปัตยกรรมโซลูชันที่หลอมรวมแก่นความคิดใหม่: 

---

## 4. ยุทธศาสตร์และฉากทัศน์อนาคต (Far Dimension Foresight)
- **การคิดเชิงอนาคต (Scenarios & Higher-order Impacts):**
  - ผลกระทบระลอกสองและสาม (2nd & 3rd Order): 
  - 3 ฉากทัศน์อนาคต (Best / Base / Worst Cases): 
- **การคิดเชิงกลยุทธ์ (Winning Moves & Moats):**
  - จุดคานงัดสูงสุด (Leverage Point): 
  - คูเมืองความได้เปรียบทางธุรกิจ (Strategic Moat): 
  - สิ่งที่เลือกที่จะไม่ทำ (Strategic Trade-offs): 

---

## 5. แผนภูมิบูรณาการและการขับเคลื่อน (Integrative Execution Plan)
- **การขยายกรอบและคลุมกรอบ (Expanding & Encompassing Alignment):**
  - การจัดสรรและเชื่อมโยง คน • เทคโนโลยี • งบประมาณ • นโยบาย: 
  - การสลายข้อขัดแย้งของ Stakeholders สู่ผลลัพธ์ทวีคูณ (1+1 > 2): 
- **หมุดหมายการลงมือปฏิบัติ (Immediate Action Plan):**
  1. 
  2. 
  3. 
"""

def cmd_list(args):
    print("\n========================================================")
    print("  ชุดความคิด 10 มิติ (The 10 Thinking Dimensions OS)")
    print("========================================================\n")
    for k, (name, axis, desc, questions) in DIMENSIONS.items():
        print(f"[{k.rjust(2)}] {name}")
        print(f"     แกนพิกัด: {axis}")
        print(f"     เป้าประสงค์: {desc}")
        print()

def cmd_check(args):
    key = args.dim
    found = False
    for k, (name, axis, desc, questions) in DIMENSIONS.items():
        if key.lower() in k or key.lower() in name.lower() or key.lower() in axis.lower():
            found = True
            print(f"\n========================================================")
            print(f"  {name}")
            print(f"  แกนพิกัด: {axis} | เป้าหมาย: {desc}")
            print(f"========================================================\n")
            print("คำถามตรวจสอบความคิด (Thinking Prompts):")
            for q in questions:
                print(f"  • {q}")
            print()
    if not found:
        print(f"ไม่พบมิติการคิดที่ตรงกับ: {key}")
        print("ลองใช้ตัวเลข 1-10 หรือคำค้นหา เช่น analytical, วิเคราะห์, deep, ลึก, กลยุทธ์")

def cmd_scaffold(args):
    topic = args.topic or "โจทย์ยุทธศาสตร์ใหม่"
    out_file = args.out or f"10think_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    content = DOSSIER_TEMPLATE.format(
        topic=topic,
        date=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"สร้างเทมเพลต 10-Think Executive Dossier เรียบร้อยแล้ว:")
    print(f"  -> {Path(out_file).resolve()}")

def prompt_user(question, default=""):
    try:
        user_val = input(f"\n{question}\n[ตอบ / กด Enter เพื่อข้าม]: ").strip()
        return user_val if user_val else default
    except (EOFError, KeyboardInterrupt):
        return default

def cmd_wizard(args):
    print("\n========================================================")
    print("  🧙 Think-10 Interactive Strategy Wizard")
    print("  เครื่องมือนำทางการคิดอย่างเป็นระบบ (กว้าง - ลึก - ไกล)")
    print("========================================================\n")

    mode = args.mode
    if not mode:
        print("กรุณาเลือกโหมดการทำงาน:")
        print("  [1] แก้ไขปัญหาที่ซับซ้อน (Complex Problem Solving Protocol - 4 ขั้น)")
        print("  [2] ท่อส่งนวัตกรรม 10 มิติ (The 10-D Innovation Pipeline - 6 ระยะ)")
        print("  [3] ประเมินรอบทิศครบ 10 มิติ (Full 10-D Cognitive Audit)")
        choice = prompt_user("เลือกโหมด [1/2/3]: ", default="1")
        mode = choice

    topic = args.topic
    if not topic:
        topic = prompt_user("ระบุชื่อหัวข้อหรือโจทย์ยุทธศาสตร์ของคุณ:", default="โจทย์ยุทธศาสตร์")

    out_file = args.out or f"dossier_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    answers = {}

    if mode == "1":
        print(f"\n--- เริ่มต้นโปรโตคอลแก้ปัญหาซับซ้อน 4 ขั้นตอน: {topic} ---")
        print("\n[ขั้นที่ 1: ชำแหละและถอดรหัสปัญหา (Deconstruction & Verification)]")
        answers["critical"] = prompt_user("1.1 คิดเชิงวิพากษ์: ข้อเท็จจริงที่พิสูจน์แล้วคืออะไร และมีสมมติฐานใดที่ต้องท้าทาย?")
        answers["analytical"] = prompt_user("1.2 คิดเชิงวิเคราะห์: ผ่าโครงสร้างระบบ 5 Whys อะไรคือสาเหตุรากเหง้า (Root Cause)?")
        answers["conceptual"] = prompt_user("1.3 คิดเชิงมโนทัศน์: สรุปนิยามโจทย์แท้จริงใน 1 ประโยคคมชัด?")

        print("\n[ขั้นที่ 2: ระดมทางเลือกและออกแบบโซลูชัน (Solution Generation)]")
        answers["comparative"] = prompt_user("2.1 คิดเชิงเปรียบเทียบ: มีกรณีศึกษาใดจากวงการอื่นที่นำมาเทียบเคียงได้ (Benchmarking)?")
        answers["creative"] = prompt_user("2.2 คิดเชิงสร้างสรรค์: หากคิดกลับด้าน (Inversion) หรือไร้ข้อจำกัด มีไอเดียนอกกรอบอะไรบ้าง?")
        answers["applicative"] = prompt_user("2.3 คิดเชิงประยุกต์: ถอดรหัสความสำเร็จจากศาสตร์อื่นมาดัดแปลงใช้หน้างานนี้อย่างไร (Left-to-Right)?")
        answers["synthesis"] = prompt_user("2.4 คิดเชิงสังเคราะห์: หลอมรวมชิ้นส่วนทางเลือกเป็น Solution Package ใหม่อย่างไร?")

        print("\n[ขั้นที่ 3: วางตำแหน่งกลยุทธ์และประเมินอนาคต (Strategic Foresight)]")
        answers["futuristic"] = prompt_user("3.1 คิดเชิงอนาคต: ผลกระทบระลอก 2-3 และฉากทัศน์ Best/Base/Worst เป็นอย่างไร?")
        answers["strategic"] = prompt_user("3.2 คิดเชิงกลยุทธ์: จุดคานงัดสูงสุด (Leverage Point) และคูเมืองป้องกัน (Moat) คืออะไร?")

        print("\n[ขั้นที่ 4: เชื่อมประสานระบบและการลงมือทำ (Systemic Implementation)]")
        answers["integrative"] = prompt_user("4.1 คิดเชิงบูรณาการ: สลายความขัดแย้งของ Stakeholders และประสานระบบทุกฝ่ายอย่างไร (1+1 > 2)?")
        answers["actions"] = prompt_user("4.2 ก้าวแรกและแผนปฏิบัติการ 3 ข้อทันที:")

        content = f"""# บันทึกยุทธศาสตร์แก้ปัญหาซับซ้อน (Complex Problem Solving Dossier)
**หัวข้อ:** {topic}  
**วันที่:** {date_str}  
**เครื่องมือ:** The 10 Thinking Dimensions Cognitive OS  

---

## 1. การถอดรหัสและสกัดแก่นแท้โจทย์
- **นิยามโจทย์แท้จริงใน 1 ประโยค (เชิงมโนทัศน์):** {answers.get('conceptual') or '[ไม่ได้ระบุ]'}
- **การตรวจสอบความจริงและสลายอคติ (เชิงวิพากษ์):** {answers.get('critical') or '[ไม่ได้ระบุ]'}
- **การผ่าโครงสร้างและรากเหง้า (เชิงวิเคราะห์):** {answers.get('analytical') or '[ไม่ได้ระบุ]'}

---

## 2. ทางออกและนวัตกรรมโซลูชัน
- **กรณีศึกษาเทียบเคียงข้ามวงการ (เชิงเปรียบเทียบ):** {answers.get('comparative') or '[ไม่ได้ระบุ]'}
- **ทางเลือกนอกกรอบและการคิดกลับด้าน (เชิงสร้างสรรค์):** {answers.get('creative') or '[ไม่ได้ระบุ]'}
- **การถ่ายโอนและดัดแปลงข้ามศาสตร์ (เชิงประยุกต์):** {answers.get('applicative') or '[ไม่ได้ระบุ]'}
- **สถาปัตยกรรมแพ็กเกจโซลูชัน (เชิงสังเคราะห์):** {answers.get('synthesis') or '[ไม่ได้ระบุ]'}

---

## 3. ยุทธศาสตร์และฉากทัศน์อนาคต
- **การประเมินฉากทัศน์และผลกระทบระยะยาว (เชิงอนาคต):** {answers.get('futuristic') or '[ไม่ได้ระบุ]'}
- **จุดคานงัดและปราการความได้เปรียบ (เชิงกลยุทธ์):** {answers.get('strategic') or '[ไม่ได้ระบุ]'}

---

## 4. แผนภูมิบูรณาการและการขับเคลื่อนจริง
- **การประสานระบบและสลายความขัดแย้ง (เชิงบูรณาการ):** {answers.get('integrative') or '[ไม่ได้ระบุ]'}
- **หมุดหมายปฏิบัติการทันที:** 
{answers.get('actions') or '[ไม่ได้ระบุ]'}
"""
    elif mode == "2":
        print(f"\n--- เริ่มต้นท่อส่งนวัตกรรม 10 มิติ (6 Stages): {topic} ---")
        answers["stage1"] = prompt_user("ระยะที่ 1: ค้นหาช่องว่างที่ซ่อนอยู่ (Value Chain Pain Points & ท้าทายความเชื่อเดิม):")
        answers["stage2"] = prompt_user("ระยะที่ 2: ตกผลึกแก่นคุณค่าใหม่ (Unmet Needs สู่ Value Proposition ใน 1 ประโยค):")
        answers["stage3"] = prompt_user("ระยะที่ 3: กระโดดข้ามพรมแดนเดิม (เทียบเคียงข้ามอุตสาหกรรม & พลิกกลับด้าน Inversion):")
        answers["stage4"] = prompt_user("ระยะที่ 4: สร้างสถาปัตยกรรมต้นแบบ (ถ่ายโอนเทคโนโลยี & หลอมรวมโมเดลธุรกิจ):")
        answers["stage5"] = prompt_user("ระยะที่ 5: ฉายภาพอนาคตและสร้างปราการ (ทดสอบ Megatrends & สร้างคูเมือง Moat):")
        answers["stage6"] = prompt_user("ระยะที่ 6: หลอมรวมระบบนิเวศนวัตกรรม (ผนึกพันธมิตรและผู้ใช้งานสู่ Synergy):")

        content = f"""# บันทึกท่อส่งนวัตกรรม 10 มิติ (Transformative Innovation Dossier)
**หัวข้อนวัตกรรม:** {topic}  
**วันที่:** {date_str}  
**เครื่องมือ:** The 10-D Innovation Pipeline  

---

## ระยะที่ 1: ค้นหาช่องว่างที่ซ่อนอยู่ (Uncovering Latent Gaps)
{answers.get('stage1') or '[ไม่ได้ระบุ]'}

## ระยะที่ 2: ตกผลึกแก่นคุณค่าใหม่ (Formulating Core Conceptual Value)
{answers.get('stage2') or '[ไม่ได้ระบุ]'}

## ระยะที่ 3: กระโดดข้ามพรมแดนเดิม (Cross-boundary Ideation)
{answers.get('stage3') or '[ไม่ได้ระบุ]'}

## ระยะที่ 4: สร้างสถาปัตยกรรมต้นแบบ (Prototype Architecture)
{answers.get('stage4') or '[ไม่ได้ระบุ]'}

## ระยะที่ 5: ฉายภาพอนาคตและสร้างปราการทางธุรกิจ (Future Alignment & Strategic Moat)
{answers.get('stage5') or '[ไม่ได้ระบุ]'}

## ระยะที่ 6: หลอมรวมระบบนิเวศนวัตกรรม (Ecosystem Integration)
{answers.get('stage6') or '[ไม่ได้ระบุ]'}
"""
    else:
        # Full 10-D Mode
        print(f"\n--- เริ่มต้นประเมินครบ 10 มิติ: {topic} ---")
        for k, (name, axis, desc, questions) in DIMENSIONS.items():
            print(f"\n[{k}] {name} (แกน: {axis})")
            answers[k] = prompt_user(f"{desc}\n{questions[0]}")
        content = f"# บันทึกการประเมินครบ 10 มิติ (Full 10-D Cognitive Audit)\n**หัวข้อ:** {topic}\n**วันที่:** {date_str}\n\n---\n\n"
        for k, (name, axis, desc, questions) in DIMENSIONS.items():
            content += f"### [{k}] {name} ({axis})\n**คำตอบ/การประเมิน:** {answers.get(k) or '[ไม่ได้ระบุ]'}\n\n"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n========================================================")
    print(f"🎉 สร้างบันทึกยุทธศาสตร์เสร็จสมบูรณ์!")
    print(f"  -> บันทึกที่ไฟล์: {Path(out_file).resolve()}")
    print(f"========================================================\n")

def cmd_scan(args):
    target_path = args.file
    raw_text = args.text

    if target_path:
        p = Path(target_path)
        if not p.exists():
            print(f"Error: ไม่พบไฟล์ {target_path}")
            return
        text = p.read_text(encoding="utf-8")
        source_name = p.name
    elif raw_text:
        text = raw_text
        source_name = "ข้อความที่ป้อน"
    else:
        print("กรุณาระบุไฟล์ผ่าน --file หรือข้อความผ่าน --text")
        return

    text_lower = text.lower()

    # Keyword patterns for cognitive scanning
    DIMENSION_KEYWORDS = {
        "1": (["root cause", "สาเหตุ", "5 why", "mece", "แยกส่วน", "วิเคราะห์", "ต้นตอ", "ปัจจัย", "สายใย", "causal", "breakdown"], "วิเคราะห์ (Analytical)", "ลึก"),
        "2": (["fact", "ข้อเท็จจริง", "สมมติฐาน", "assumption", "อคติ", "bias", "ตรรกะ", "fallacy", "พิสูจน์", "หลักฐาน", "evidence"], "วิพากษ์ (Critical)", "ลึก"),
        "3": (["สังเคราะห์", "synthesis", "หลอมรวม", "ถักทอ", "โมเดลใหม่", "framework", "แพ็กเกจ", "emergent", "thesis", " antithesis"], "สังเคราะห์ (Synthesis)", "กว้าง"),
        "4": (["เปรียบเทียบ", "compare", "benchmark", "เหมือน", "ต่าง", "เกณฑ์", "criteria", "อุปมา", "metaphor", "เทียบเคียง"], "เปรียบเทียบ (Comparative)", "กว้าง"),
        "5": (["มโนทัศน์", "concept", "แก่นแท้", "ใน 1 ประโยค", "สารัตถะ", "big picture", "ภาพรวม", "ความคิดรวบยอด", "essence"], "มโนทัศน์ (Conceptual)", "ลึก"),
        "6": (["สร้างสรรค์", "creative", "นอกกรอบ", "กลับด้าน", "inversion", "ทางเลือกใหม่", "divergent", "originality", "บ้าบิ่น"], "สร้างสรรค์ (Creative)", "กว้าง"),
        "7": (["ประยุกต์", "applicative", "left to right", "ถ่ายโอน", "ดัดแปลง", "ย่อส่วน", "ปรับใช้", "ต้นทาง", "ปลายทาง", "adapt"], "ประยุกต์ (Applicative)", "กว้าง"),
        "8": (["กลยุทธ์", "strategic", "คานงัด", "leverage", "คูเมือง", "moat", "ความเป็นต่อ", "ได้เปรียบ", "trade-off", "หมาก"], "กลยุทธ์ (Strategic)", "ไกล"),
        "9": (["บูรณาการ", "integrative", "องค์รวม", "holistic", "ขยายกรอบ", "คลุมกรอบ", "1+1 > 2", "synergy", "สลายไซโล", "พันธมิตร"], "บูรณาการ (Integrative)", "กว้าง"),
        "10": (["อนาคต", "futuristic", "megatrend", "สัญญาณเตือน", "ฉากทัศน์", "scenario", "best case", "worst case", "ระยะยาว", "foresight"], "อนาคต (Futuristic)", "ไกล")
    }

    scores = {}
    word_count = len(text.split())

    for k, (keywords, name, axis) in DIMENSION_KEYWORDS.items():
        hits = sum(text_lower.count(kw) for kw in keywords)
        # Calculate dynamic score based on density and presence
        if hits == 0:
            score = 1.0
        elif hits == 1:
            score = 3.5
        elif hits == 2:
            score = 5.5
        elif hits == 3:
            score = 7.5
        elif hits >= 4:
            score = min(10.0, 8.5 + (hits - 4) * 0.5)
        scores[k] = round(score, 1)

    deep_score = round((scores["1"] + scores["2"] + scores["5"]) / 3, 1)
    broad_score = round((scores["3"] + scores["4"] + scores["6"] + scores["7"] + scores["9"]) / 5, 1)
    far_score = round((scores["8"] + scores["10"]) / 2, 1)
    overall_balance = round((deep_score + broad_score + far_score) / 3, 1)

    print("\n========================================================")
    print(f"  🔍 Cognitive Blindspot Scanner: {source_name}")
    print(f"  ความยาวเนื้อหา: {word_count} คำ | ดัชนีความสมบูรณ์รอบทิศ: {overall_balance}/10")
    print("========================================================\n")

    def print_bar(label, val):
        bars = int(val)
        bar_str = "█" * bars + "░" * (10 - bars)
        return f"{label.ljust(22)}: {str(val).rjust(4)}/10 [{bar_str}]"

    print("📊 คะแนน 3 แกนพิกัดหลัก (Core 3D Coordinates):")
    print("  " + print_bar("แกนความลึก (Deep)", deep_score) + (" ✅ ยอดเยี่ยม" if deep_score >= 7 else " ⚠️ ควรเจาะลึกเพิ่ม"))
    print("  " + print_bar("แกนความกว้าง (Broad)", broad_score) + (" ✅ ยอดเยี่ยม" if broad_score >= 7 else " ⚠️ ควรขยายมุมมอง"))
    print("  " + print_bar("แกนความไกล (Far)", far_score) + (" ✅ ยอดเยี่ยม" if far_score >= 7 else " ⚠️ วิกฤต จุดบอดระยะยาว"))
    print()

    print("📋 คะแนนเจาะลึกรายมิติความคิดทั้ง 10 ด้าน:")
    for k, (keywords, name, axis) in DIMENSION_KEYWORDS.items():
        print(f"  [{k.rjust(2)}] " + print_bar(f"{name} ({axis})", scores[k]))
    print()

    # Blindspot identification
    sorted_dims = sorted(scores.items(), key=lambda x: x[1])
    lowest_k, lowest_score = sorted_dims[0]
    second_lowest_k, second_lowest_score = sorted_dims[1]

    print("========================================================")
    print("⚠️ การวิเคราะห์จุดบอดทางความคิด (Cognitive Blindspot Diagnostic):")
    print("========================================================")

    if lowest_score <= 4.0:
        low_name = DIMENSION_KEYWORDS[lowest_k][1]
        print(f"🚨 จุดบอดวิกฤตอันดับ 1: [{lowest_k}] {low_name} (คะแนน: {lowest_score}/10)")
        if lowest_k == "1":
            print("   -> แผนงานนี้ขาดการวิเคราะห์ Root Cause เชิงระบบ อาจกำลังเสียเวลาแก้ปัญหาที่เพียงแค่อาการภายนอก")
        elif lowest_k == "2":
            print("   -> แผนงานนี้ขาดการตรวจสอบข้อเท็จจริงและสมมติฐาน เสี่ยงต่อการตัดสินใจบนอคติหรือตรรกะวิบัติ")
        elif lowest_k == "5":
            print("   -> แผนงานนี้ขาดแก่นแท้ใน 1 ประโยค (Essence) ข้อความยาวเกินไปจนสูญเสียจุดโฟกัส")
        elif lowest_k == "6":
            print("   -> แผนงานนี้ติดหล่มกรอบเดิม ขาดความคิดสร้างสรรค์แบบก้าวกระโดดหรือการคิดกลับด้าน (Inversion)")
        elif lowest_k == "7":
            print("   -> แผนงานนี้ขาดการประยุกต์และดัดแปลงโมเดลสำเร็จข้ามศาสตร์ อาจกำลังประดิษฐ์ล้อซ้ำใหม่")
        elif lowest_k == "8":
            print("   -> แผนงานนี้ขาด 'จุดคานงัด' และ 'คูเมืองความได้เปรียบ' (Moat) คู่แข่งสามารถลอกเลียนแบบได้ง่าย")
        elif lowest_k == "9":
            print("   -> แผนงานนี้เสี่ยงต่อการทำงานแบบแยกส่วน (Silo) ขาดการประสานประโยชน์ของ Stakeholders ทุกฝ่าย")
        elif lowest_k == "10":
            print("   -> แผนงานนี้ตาบอดต่ออนาคต ขาดการวางฉากทัศน์ Best/Worst Case และไม่เตรียมรับมือ Megatrends")

    if second_lowest_score <= 4.5:
        second_name = DIMENSION_KEYWORDS[second_lowest_k][1]
        print(f"⚠️ จุดที่ควรเสริมเพิ่ม: [{second_lowest_k}] {second_name} (คะแนน: {second_lowest_score}/10)")

    if lowest_score > 4.0:
        print("🎉 ยินดีด้วย! แผนงานของคุณมีการกระจายมิติความคิดได้อย่างสมดุลในเกณฑ์ดี ไร้จุดบอดวิกฤต")

    print("\n💡 คำแนะนำยกระดับ:")
    print(f"  รันคำสั่งตรวจสอบคำถามเฉพาะมิตินี้: python3 think10_cli.py check {lowest_k}\n")

def main():
    parser = argparse.ArgumentParser(description="10 Thinking Dimensions Cognitive OS CLI")
    subparsers = parser.add_subparsers(dest="command")

    # list
    p_list = subparsers.add_parser("list", help="แสดงรายชื่อมิติการคิดทั้ง 10 มิติ")

    # check
    p_check = subparsers.add_parser("check", help="ดูคำถามตรวจสอบความคิดของมิตินั้นๆ")
    p_check.add_argument("dim", help="หมายเลขมิติ (1-10) หรือชื่อมิติ เช่น analytical, critical, ลึก")

    # scaffold
    p_scaffold = subparsers.add_parser("scaffold", help="สร้างไฟล์เทมเพลต 10-Think Executive Dossier")
    p_scaffold.add_argument("--topic", "-t", help="ชื่อหัวข้อหรือโจทย์ยุทธศาสตร์")
    p_scaffold.add_argument("--out", "-o", help="ชื่อไฟล์ผลลัพธ์ (.md)")

    # wizard
    p_wizard = subparsers.add_parser("wizard", help="รัน Interactive Wizard เพื่อตอบคำถามและสร้างรายงานทีละขั้นตอน")
    p_wizard.add_argument("--mode", "-m", choices=["1", "2", "3"], help="เลือกโหมด (1: CPS, 2: Innovation, 3: Full 10-D)")
    p_wizard.add_argument("--topic", "-t", help="ชื่อหัวข้อหรือโจทย์ยุทธศาสตร์")
    p_wizard.add_argument("--out", "-o", help="ชื่อไฟล์ผลลัพธ์ (.md)")

    # scan
    p_scan = subparsers.add_parser("scan", help="สแกนเอกสารหรือข้อความเพื่อประเมินคะแนน 10 มิติและตรวจหาจุดบอด")
    p_scan.add_argument("--file", "-f", help="พาธของไฟล์ Markdown/Text ที่ต้องการสแกน")
    p_scan.add_argument("--text", "-t", help="ข้อความสั้นที่ต้องการสแกนโดยตรง")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    elif args.command == "check":
        cmd_check(args)
    elif args.command == "scaffold":
        cmd_scaffold(args)
    elif args.command == "wizard":
        cmd_wizard(args)
    elif args.command == "scan":
        cmd_scan(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
