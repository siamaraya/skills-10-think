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

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    elif args.command == "check":
        cmd_check(args)
    elif args.command == "scaffold":
        cmd_scaffold(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
