# Ten Thinking Dimensions Cognitive OS (ผู้ชนะ 10 คิด)

> ระบบปฏิบัติการทางปัญญาสำหรับ AI และมนุษย์ เพื่อการคิดอย่าง **"กว้าง - ลึก - ไกล"** ที่ครบถ้วนและเฉียบคม ถอดรหัสจากผลงานมาสเตอร์พีซชุด *"ผู้ชนะ 10 คิด"* และ *"ลายแทงนักคิด"* ของ **ศาสตราจารย์ ดร.เกรียงศักดิ์ เจริญวงศ์ศักดิ์ (ดร.แดน)**

---

## 🔗 การเชื่อมโยงกับทุก AI แบบ Symlink (Multi-AI Symlink Integration)

ชุดสกิลนี้รองรับการทำ **Symlink (Soft Link)** ไปยัง AI ทุกตัวบนเครื่อง เพื่อให้โค้ดและชุดความคิดอยู่ที่โฟลเดอร์นี้เพียงจุดเดียว (Single Source of Truth) **แก้ไข ปรับปรุง หรือเพิ่มกรณีศึกษาที่นี่ที่เดียว AI ทุกตัวจะอัปเดตตามทันทีโดยไม่ต้องก็อปปี้ซ้ำซ้อน!**

### รันคำสั่ง 1 ครั้งเพื่อเชื่อมโยงกับทุก AI:
```bash
./symlink_all_ais.sh
# หรือรันผ่าน Python
python3 symlink_all_ais.py
```

### รองรับ AI และเครื่องมือชั้นนำทั้งหมด:
| AI / Tool | ตำแหน่งที่ Symlink เชื่อมโยงไป | รูปแบบการทำงาน |
|---|---|---|
| **Antigravity / Gemini** | `~/.gemini/config/skills/ten-thinking-dimensions` และ `~/.gemini/skills/` | โหลดเป็น Native Global Skill อัตโนมัติ |
| **Claude Code** | `~/.claude/commands/` และ `~/.claude/skills/` | รองรับ Native Slash Commands (`/`) ใน CLI |
| **Cursor** | `~/.cursor/rules/ten-thinking-dimensions.mdc` และ `.cursorrules` | บังคับใช้เป็น Global & Workspace AI Rule |
| **Windsurf (Codeium)** | `.windsurfrules` | กฎจิตใต้สำนึกทางปัญญาของ Workspace |
| **Cline** | `~/.cline/skills/ten-thinking-dimensions` และ `.clinerules` | Skill และ Workspace Rules |
| **Roo Code** | `~/.roo/skills/ten-thinking-dimensions` | Roo Coding Agent Skill |
| **Continue.dev** | `~/.continue/skills/ten-thinking-dimensions` | Assistant Context & Prompts |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Workspace Instructions ประจำ Repository |

---

## ⚡ การเรียกใช้โหมดต่างๆ ผ่านคำสั่งทางลัด Slash Command ("/")

คุณสามารถสั่งการ AI ทุกตัวด้วยคำสั่งย่อที่ขึ้นต้นด้วยเครื่องหมาย **Slash (`/`)** ได้ทันที สะดวก รวดเร็ว และแม่นยำ ไม่ต้องพิมพ์อธิบายยาว:

### 📋 สรุปรายการคำสั่งทางลัด:

| คำสั่ง (Slash Command) | โหมดการทำงาน | ผลลัพธ์และขั้นตอนที่ AI จะดำเนินการ | ตัวอย่างการใช้งานจริง |
|---|---|---|---|
| **`/cps`** | **แก้ปัญหาซับซ้อน (4 ขั้นตอน)** | ชำแหละรากเหง้า (Critical+Analytical) ➔ ออกแบบทางเลือก (Comparative+Creative+Synthesis) ➔ วางคานงัดและอนาคต (Futuristic+Strategic) ➔ บูรณาการสลายขัดแย้ง | `/cps ยอดขายหน้าร้านตก 35% แต่ต้นทุนวัตถุดิบสูงขึ้น 20%` |
| **`/innovate`** | **สร้างนวัตกรรมก้าวกระโดด (6 ระยะ)** | ท่อส่งนวัตกรรม 10-D: หาช่องว่างที่ซ่อนอยู่ ➔ สกัดแก่นคุณค่าใหม่ ➔ ไอเดียนอกกรอบ ➔ สถาปัตยกรรมโมเดลธุรกิจ ➔ คูเมือง Moat ➔ บูรณาการระบบนิเวศ | `/innovate บริการ Subscription กาแฟเพื่อสุขภาพสำหรับพนักงานออฟฟิศ` |
| **`/strategy`** | **ยุทธศาสตร์และคูเมืองป้องกัน** | วางหมากยุทธศาสตร์ 3 ชั้น + ทดสอบ 3 ฉากทัศน์อนาคต (Best/Base/Worst) + กำหนดจุดคานงัดสร้างความได้เปรียบยั่งยืน | `/strategy แผนขยายสาขา 10 เท่าใน 2 ปีแข่งกับเชนยักษ์ใหญ่` |
| **`/council`** | **สภาไตรปัญญา Red Teaming** | จำลอง 3 บทบาทปัญญาถกเถียง: 🎭 ผู้รอบรู้ (ชี้โอกาส/สากล) ปะทะ ⚔️ ผู้ท้าทาย (เจาะจุดอ่อน/จับผิด) ➔ 🧩 ผู้ประสาน (เคาะฉันทามติยุทธศาสตร์) | `/council แผนการลดราคา 50% เพื่อแย่งชิงส่วนแบ่งตลาดในไตรมาสหน้า` |
| **`/blindspot`** | **สแกนตรวจจับจุดบอด 10 มิติ** | ตรวจ 5 โซนอันตราย (แก้แต่อาการ, ด่วนสรุป, ไซโล, มองมิติเดียว, แผนนิ่ง) พร้อมเรดาร์คะแนน กว้าง-ลึก-ไกล และมาตรการอุดรูรั่ว | `/blindspot ตรวจสอบสถาปัตยกรรมระบบชำระเงินและโมเดลข้อมูลนี้` |
| **`/think10`** | **วิเคราะห์ครบ 10 มิติรอบด้าน** | วิเคราะห์ประเด็นผ่านแกนพิกัด 3 มิติ (ลึก-กว้าง-ไกล) ครบถ้วนทั้ง 10 มิติการคิด พร้อมเรดาร์คะแนนความครอบคลุม | `/think10 การนำ Generative AI มาใช้ในกระบวนการจัดซื้อขององค์กร` |
| **`/ground`** | **ตรวจสอบข้อเท็จจริงเชิงประจักษ์** | ค้นหาข้อมูลสถิติล่าสุด ตรวจสอบ Fact vs Opinion จัดระดับความน่าเชื่อถือ และจับอคติหรือการอ้างเกินจริง | `/ground ตลาดกาแฟพิเศษในไทยกำลังอิ่มตัวและจะหดตัวลงในปีหน้า` |
| **`/wizard`** | **รัน Strategy CLI Wizard** | แนะนำคำสั่งรัน Interactive CLI เพื่อตอบคำถามทีละสเต็ป | `/wizard` |

---

### 💡 วิธีใช้งานใน AI แต่ละแพลตฟอร์ม:

1. **ใน Claude Code (Terminal CLI):**
   - เพียงเปิด Terminal พิมพ์ `claude`
   - เมื่อพิมพ์ `/` จะมี **Autocomplete Menu** แสดงรายชื่อคำสั่ง `/cps`, `/innovate`, `/council` ฯลฯ ขึ้นมาให้เลือกทันที!
   - สามารถพิมพ์ต่อท้ายได้เลย เช่น: `/cps ปัญหาลูกค้าลดลง 30%`

2. **ใน Antigravity (Google Gemini):**
   - พิมพ์ในช่องแชทได้ทันที เช่น: `/innovate แพลตฟอร์มจับคู่ฟรีแลนซ์สายสุขภาพ`
   - AI จะตรวจจับ Directive อัตโนมัติและสลับเข้าสู่โหมด 10-D Innovation Pipeline ทันที

3. **ใน Cursor / Windsurf / Cline / Roo Code / Copilot:**
   - พิมพ์ `/council [แผนงาน]` หรือ `/blindspot [โค้ดหรือแผนงาน]` ในกล่อง Prompt หรือ Composer
   - AI ทุกตัวที่เชื่อมโยงกฎไว้จะปฏิบัติตามคำสั่งของโหมดนั้นทันที 100%

---

### 🎯 สูตรและตัวอย่างคำสั่งชั้นยอด (The Golden Prompt Examples)

เพื่อให้ AI แสดงศักยภาพของ 10 มิติการคิดได้ลึกซึ้งสูงสุด แนะนำให้ใช้ **โครงสร้าง 3 องค์ประกอบ**:
> **`/[คำสั่ง] [1. บริบทและสถานการณ์ปัจจุบัน] + [2. ข้อจำกัด/ทรัพยากร] + [3. เป้าหมายที่ต้องการบรรลุ]`**

#### 1. ตัวอย่างกู้วิกฤตธุรกิจ (`/cps`):
```text
/cps บริบท: โรงงานผลิตบรรจุภัณฑ์ต้นทุนเยื่อกระดาษพุ่ง 40% แต่ลูกค้ารายใหญ่ 5 รายขู่จะยกเลิกสัญญาหากขึ้นราคา 
ข้อจำกัด: สภาพคล่องเหลือ 3 เดือน มีพนักงาน 120 คนไม่อยากปลดพนักงาน 
เป้าหมาย: รักษา Margin กำไรขั้นต่ำ 15% และรักษาฐานลูกค้าไว้ครบ 100% ภายในไตรมาสนี้
```

#### 2. ตัวอย่างออกแบบโมเดลธุรกิจนวัตกรรม (`/innovate`):
```text
/innovate โจทย์: ต้องการปฏิวัติธุรกิจร้านแว่นตาท้องถิ่นให้กลายเป็นบริการ Personal Vision Wellness แบบ Subscription รายเดือน 
กลุ่มเป้าหมาย: พนักงานออฟฟิศที่ทำงานหน้าจอเกิน 8 ชั่วโมงต่อวัน มีอาการตาล้าและไมเกรน 
แก่นที่ต้องการ: สกัด Unmet Needs, ดึง Best Practice ข้ามอุตสาหกรรม, และสร้างคูเมืองป้องกันเชนใหญ่เลียนแบบ
```

#### 3. ตัวอย่างวางหมากกลยุทธ์สู้รายใหญ่ (`/strategy`):
```text
/strategy สถานการณ์: สตาร์ทอัพ EdTech กำลังถูกบริษัทยักษ์ใหญ่เปิดตัวคอร์สเรียนฟรีเข้ามาตีตลาด 
จุดแข็งของเรา: ชุมชนเหนียวแน่น มีระบบ Mentor ใกล้ชิด และศิษย์เก่าได้งาน 88% 
โจทย์: วางหมาก 3 ชั้น พร้อมทดสอบ 3 ฉากทัศน์ (Best, Base, Worst) เพื่อสร้าง Network Effect Moat ที่เงินซื้อไม่ได้
```

#### 4. ตัวอย่างสภาไตรปัญญา Red Teaming แผนการลงทุน (`/council`):
```text
/council ข้อเสนอ: บริษัทจะทุ่มเงินสดสำรอง 60% (50 ล้านบาท) เข้าซื้อโรงงานชิ้นส่วน EV เพื่อ Pivot ธุรกิจ 
การดีเบต: ให้ The Omniscient ชี้โอกาสสากล, ให้ The Devil's Advocate ชำแหละความเสี่ยงหนี้แฝงและเทคโนโลยีแบตเตอรี่, 
และให้ The Synthesizer เคาะฉันทามติยุทธศาสตร์และมาตรการป้องกันความเสี่ยง
```

#### 5. ตัวอย่างสแกนจุดบอดสถาปัตยกรรมระบบ (`/blindspot`):
```text
/blindspot สถาปัตยกรรม: ระบบจัดเก็บข้อมูลลูกค้าใช้ JWT Token ใน LocalStorage และใช้ Cronjob ส่งข้อมูล Transaction ไปประมวลผลบน Third-Party Analytics Tool ทุกเที่ยงคืน 
สแกนหา: 5 โซนอันตราย, ความเสี่ยงด้านความปลอดภัย (XSS, Data Leakage), และข้อขัดแย้งต่อกฎหมาย PDPA/GDPR
```

*(ดูตัวอย่างเจาะลึกเพิ่มเติมได้ที่ [references/golden_prompt_cookbook.md](./.agents/skills/ten-thinking-dimensions/references/golden_prompt_cookbook.md))*

---

## 💻 วิธีนำไปติดตั้งใช้งานกับเครื่องอื่นๆ (Cross-Machine Portability)

ชุดสกิลนี้ถูกออกแบบให้ **Portable 100%** ไม่มี Path ผูกติดกับเครื่องใดเครื่องหนึ่ง (ใช้ Relative Links ทั้งหมด) คุณสามารถนำไปติดตั้งในคอมพิวเตอร์เครื่องอื่น (Mac, Windows, Linux) ได้อย่างง่ายดายผ่าน 4 รูปแบบ:

### วิธีที่ 1: ติดตั้งผ่าน Script 1-Click (ง่ายและสะดวกที่สุด)

#### บน macOS / Linux:
เปิด Terminal ในโฟลเดอร์นี้ แล้วพิมพ์คำสั่ง:
```bash
bash install.sh
# หรือใช้ Python
python3 install.py
```

#### บน Windows:
- ดับเบิลคลิกที่ไฟล์ `install.bat` หรือ
- คลิกขวาที่ `install.ps1` แล้วเลือก *Run with PowerShell* หรือ
- รันคำสั่งผ่าน Command Prompt / PowerShell:
```cmd
python install.py
```

*(สคริปต์จะคัดลอกชุดสกิลทั้งหมดลงในโฟลเดอร์ Global Config ของ Antigravity คือ `~/.gemini/config/skills/ten-thinking-dimensions/` โดยอัตโนมัติ ทำให้ใช้งานได้กับทุกโปรเจกต์ในเครื่องนั้นทันที)*

---

### วิธีที่ 2: แชร์ผ่านไฟล์ ZIP สำเร็จรูป (`ten-thinking-dimensions.zip`)
ในโฟลเดอร์นี้มีไฟล์ `ten-thinking-dimensions.zip` ที่บรรจุสกิลทั้งชุดไว้เรียบร้อยแล้ว:
1. ส่งไฟล์ `ten-thinking-dimensions.zip` ไปยังเครื่องปลายทาง (ผ่าน Email, Flash Drive, Cloud ฯลฯ)
2. บนเครื่องปลายทาง ให้แตกไฟล์ zip ไปไว้ที่:
   - **macOS / Linux:** `~/.gemini/config/skills/`
   - **Windows:** `C:\Users\<ชื่อผู้ใช้>\.gemini\config\skills\`
3. เมื่อแตกไฟล์แล้ว โครงสร้างจะอยู่ที่ `.../skills/ten-thinking-dimensions/SKILL.md` และพร้อมใช้งานทันที!

---

### วิธีที่ 3: ใช้งานผ่าน GitHub / Git Clone
สามารถ Clone จาก Public GitHub Repository ได้ทันที:
```bash
# 1. Clone ลงในเครื่องใหม่
git clone https://github.com/siamaraya/skills-10-think.git
cd skills-10-think

# 2. รันคำสั่งติดตั้ง (เลือกตาม OS)
./install.sh   # สำหรับ macOS / Linux
# หรือรัน python3 install.py
```

---

### วิธีที่ 4: คัดลอกเฉพาะโปรเจกต์ที่ต้องการใช้งาน (Workspace Level)
หากต้องการใช้เฉพาะกับโปรเจกต์ใดโปรเจกต์หนึ่ง โดยไม่ติดตั้งลงใน Global:
- เพียงแค่คัดลอกโฟลเดอร์ `.agents` จากโฟลเดอร์นี้ ไปวางไว้ที่โฟลเดอร์ Root ของโปรเจกต์เป้าหมาย Antigravity จะตรวจพบสกิลนี้อัตโนมัติเมื่อเปิดโปรเจกต์นั้น

---

## 🧭 สถาปัตยกรรมแกนพิกัด 3 มิติ (The 3D Coordinate System)

```text
                                  ▲
                                  │ แกนความลึก (Deep Dimension)
                                  │ • วิเคราะห์ (Analytical)
                                  │ • วิพากษ์ (Critical)
                                  │ • มโนทัศน์ (Conceptual)
                                  │
    แกนความกว้าง (Broad)          │          แกนความไกล (Far Dimension)
    • เปรียบเทียบ (Comparative)    ┼─────────► • กลยุทธ์ (Strategic)
    • สังเคราะห์ (Synthesis)      │           • อนาคต (Futuristic)
    • สร้างสรรค์ (Creative)       │
    • ประยุกต์ (Applicative)       │
    • บูรณาการ (Integrative)      │
```

1. **แกนความลึก (Deep):** ขุดค้นรากเหง้าปัญหา (Root Cause) กรองข้อเท็จจริงปราศจากอคติ และสกัดแก่นแท้ใน 1 ประโยค
2. **แกนความกว้าง (Broad):** เชื่อมโยงข้ามศาสตร์ แตกไอเดียนอกกรอบ ถ่ายโอนโมเดลสำเร็จ และสลายความขัดแย้งของระบบ
3. **แกนความไกล (Far):** ฉายภาพฉากทัศน์อนาคต ดักจับสัญญาณเตือนภัย และวางจุดคานงัดเพื่อสร้างความได้เปรียบยั่งยืน

---

## 📊 ตารางสรุป 10 มิติการคิด (The 10 Thinking Dimensions)

| มิติการคิด | แกนพิกัด | เป้าประสงค์ทางปัญญา | คำถามแกนกลาง (Core Prompt) |
|---|---|---|---|
| **1. คิดเชิงวิเคราะห์ (Analytical)** | **ลึก** | ผ่าโครงสร้างระบบ หารากเหง้า (MECE & 5 Whys) | *"เรื่องนี้ประกอบด้วยส่วนย่อยอะไร และส่งผลกระทบถึงกันอย่างไร?"* |
| **2. คิดเชิงวิพากษ์ (Critical)** | **ลึก** | กรองความจริง จับอคติ ตรวจตรรกะวิบัติ | *"เรื่องนี้จริงแท้แค่ไหน มีหลักฐานอะไร และมีอคติซ่อนอยู่หรือไม่?"* |
| **3. คิดเชิงสังเคราะห์ (Synthesis)** | **กว้าง** | ถักทอสิ่งย่อยเป็นสิ่งใหม่ โมเดลใหม่ (บันได 7 ขั้น) | *"นำแก่นสาระเหล่านี้มาถักทอจัดระเบียบใหม่เป็นอะไรได้บ้าง?"* |
| **4. คิดเชิงเปรียบเทียบ (Comparative)** | **กว้าง** | หาความเหมือนในความต่าง / ความต่างในความเหมือน | *"สิ่งเหล่านี้เหมือนและต่างกันอย่างไรตามเกณฑ์มาตรฐานนี้?"* |
| **5. คิดเชิงมโนทัศน์ (Conceptual)** | **ลึก** | สกัดแก่นแท้นามธรรมสู่ความคิดรวบยอดใน 1 ประโยค | *"อะไรคือแก่นแท้และสาระสำคัญสูงสุดของเรื่องนี้?"* |
| **6. คิดเชิงสร้างสรรค์ (Creative)** | **กว้าง** | แตกไอเดีย 4 เสาหลัก (ริเริ่ม, ยืดหยุ่น, คล่อง, ประณีต) | *"มีทางเลือกอื่นที่แปลกใหม่และสร้างคุณค่าได้มากกว่านี้ไหม?"* |
| **7. คิดเชิงประยุกต์ (Applicative)** | **กว้าง** | Thinking Left-to-Right ถ่ายโอนและดัดแปลงข้ามบริบท | *"จะนำกลไกความสำเร็จนี้ไปดัดแปลงใช้กับสถานการณ์ใหม่ได้อย่างไร?"* |
| **8. คิดเชิงกลยุทธ์ (Strategic)** | **ไกล** | หาจุดคานงัด เดินหมากหลายชั้น สร้างคูเมือง (Moat) | *"จะวางหมากอย่างไรเพื่อสร้างความเป็นต่อและบรรลุชัยชนะสูงสุด?"* |
| **9. คิดเชิงบูรณาการ (Integrative)** | **กว้าง** | ขยายกรอบและคลุมกรอบ สลายไซโล (1+1 > 2) | *"จะขยายและคลุมกรอบเพื่อสลายความขัดแย้งและผสานพลังได้อย่างไร?"* |
| **10. คิดเชิงอนาคต (Futuristic)** | **ไกล** | ดักจับสัญญาณเตือน อ่าน Megatrends วาง 3 ฉากทัศน์ | *"ในอนาคตจะเกิดฉากทัศน์ใด และต้องเตรียมพร้อมอย่างไรตั้งแต่วันนี้?"* |

---

## 🚀 2 เครื่องมือขับเคลื่อนหลัก (Dual Execution Engines)

### Engine A: Complex Problem Solving (4 ขั้นตอน)
1. **Deconstruction & Verification:** Critical (กรองความจริง) + Analytical (ผ่า Root Cause) + Conceptual (นิยามโจทย์ 1 ประโยค)
2. **Solution Generation & Formulation:** Comparative (Benchmarking) + Creative (นอกกรอบ) + Applicative (ดัดแปลง) + Synthesis (ถักทอแพ็กเกจโซลูชัน)
3. **Strategic Foresight & Impact Evaluation:** Futuristic (ประเมินผลระลอก 2-3 และ 3 ฉากทัศน์) + Strategic (ค้นหาจุดคานงัด)
4. **Systemic Implementation & Alignment:** Integrative (ขยายกรอบและคลุมกรอบ สลายขัดแย้ง สู่ความสำเร็จทวีคูณ)

### Engine B: The 10-D Transformative Innovation Pipeline (6 ระยะ)
1. **Uncovering Latent Gaps:** Analytical (ชำแหละ Value Chain) + Critical (ท้าทายความเชื่อเดิม)
2. **Formulating Core Conceptual Value:** Conceptual (สกัด Unmet Needs สู่ Value Proposition)
3. **Cross-boundary Ideation:** Comparative (เทียบเคียงข้ามอุตสาหกรรม) + Creative (คิดกลับด้าน Inversion)
4. **Prototype Architecture:** Applicative (ถ่ายโอนเทคโนโลยี Left-to-Right) + Synthesis (หลอมรวมโมเดลธุรกิจ)
5. **Future Alignment & Strategic Moat:** Futuristic (ทดสอบ Megatrends) + Strategic (สร้างคูเมือง Moat)
6. **Ecosystem Integration:** Integrative (สร้างระบบนิเวศพันธมิตรสู่พลังทวีคูณ)

---

## 📁 โครงสร้างชุดสกิล (File Architecture)

```text
Skills 10 Think/
├── README.md                                 # คู่มือและการติดตั้งข้ามเครื่อง
├── install.py                                # Universal Cross-Platform Installer
├── install.sh                                # 1-Click Installer สำหรับ macOS/Linux
├── install.bat                               # 1-Click Installer สำหรับ Windows CMD
├── install.ps1                               # 1-Click Installer สำหรับ Windows PowerShell
├── ten-thinking-dimensions.zip               # ZIP Bundle พร้อมแชร์และแตกไฟล์ใช้งานทันที
├── .agents/skills/ten-thinking-dimensions/
│   ├── SKILL.md                              # สกิลหลักและตัวควบคุมการทำงาน (Relative Links 100%)
│   ├── references/                           # คลังคู่มือเฉพาะทาง 14 ฉบับ
│   ├── examples/                             # คลังกรณีศึกษาจริง 3 ภาคอุตสาหกรรม
│   │   ├── case_study_business_turnaround.md # ธุรกิจกาแฟและสุขภาวะชุมชน
│   │   ├── case_study_ai_saas_platform.md    # นวัตกรรม Enterprise AI SaaS
│   │   └── case_study_manufacturing_cost_crisis.md # กู้วิกฤตโรงงานและการผลิต
│   └── scripts/
│       └── think10_cli.py                    # เครื่องมือ CLI + Interactive Strategy Wizard
```

---

## 🛠 วิธีการใช้งาน (Usage Guide)

### 1. เรียกใช้งานผ่าน AI Agent ในบทสนทนา:
สามารถพิมพ์สั่ง Antigravity ในโปรเจกต์ใดๆ ก็ได้ เช่น:
- *"ช่วยวิเคราะห์ปัญหาต้นทุนพุ่งและลูกค้ายกเลิกสัญญา ด้วยกระบวนการแก้ปัญหาซับซ้อนของ 10 คิด"*
- *"ช่วยคิดนวัตกรรมโมเดลธุรกิจ Enterprise AI SaaS ด้วย 10-D Innovation Pipeline"*
- *"ช่วยตรวจสอบความสมเหตุสมผลของแผนงานนี้ด้วยการคิดเชิงวิพากษ์และวิเคราะห์เชิงลึก"*

### 2. รันโหมดผู้ช่วยทีละขั้นตอน (Interactive Strategy Wizard):
ตอบคำถามนำทางทีละขั้นตอน แล้วระบบจะคอมไพล์สรุปออกมาเป็นไฟล์ Markdown Executive Dossier ให้อัตโนมัติ:
```bash
python3 .agents/skills/ten-thinking-dimensions/scripts/think10_cli.py wizard
```
*(รองรับ 3 โหมด: `1` แก้ปัญหาซับซ้อน [CPS], `2` ท่อส่งนวัตกรรม [Innovation], `3` ตรวจสอบรอบทิศ [Full 10-D])*

### 3. คำสั่ง CLI อื่นๆ:
```bash
# แสดงรายชื่อ 10 มิติการคิด
python3 .agents/skills/ten-thinking-dimensions/scripts/think10_cli.py list

# ดูคำถามตรวจสอบความคิดของมิติที่ต้องการ
python3 .agents/skills/ten-thinking-dimensions/scripts/think10_cli.py check analytical
python3 .agents/skills/ten-thinking-dimensions/scripts/think10_cli.py check กลยุทธ์

# สร้างไฟล์โครงร่างบันทึกยุทธศาสตร์ (Executive Dossier) สำหรับโจทย์ใหม่
python3 .agents/skills/ten-thinking-dimensions/scripts/think10_cli.py scaffold --topic "การแก้ปัญหายอดขายตกต่ำ" --out report.md
```

