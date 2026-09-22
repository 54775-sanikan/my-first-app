import streamlit as st
import random

st.title("🌏 เกมทายอาหารประจำชาติ")
st.write("ทายว่าอาหารแต่ละอย่างเป็นอาหารประจำชาติของประเทศใด")

# ข้อมูลจากตาราง
data = [
    {"อาหาร": "ต้มยำกุ้ง", "คำใบ้": "สยามเมืองยิ้ม", "ประเทศ": "ประเทศไทย"},
    {"อาหาร": "ซูชิ", "คำใบ้": "แดนอาทิตย์อุทัย", "ประเทศ": "ประเทศญี่ปุ่น"},
    {"อาหาร": "พาสต้า", "คำใบ้": "ที่ตั้งกรุงโรม", "ประเทศ": "ประเทศอิตาลี"},
    {"อาหาร": "กิมจิ", "คำใบ้": "ต้นกำเนิดเพลงแนว K-POP", "ประเทศ": "ประเทศเกาหลีใต้"},
    {"อาหาร": "ทาโก้", "คำใบ้": "ต้นกำเนิดของเหล้าเตกีล่า", "ประเทศ": "ประเทศเม็กซิโก"},
    {"อาหาร": "ครัวซองต์", "คำใบ้": "หอไอเฟล เมืองแฟชั่น", "ประเทศ": "ประเทศฝรั่งเศส"},
    {"อาหาร": "แป้งโรตี", "คำใบ้": "ผงมาซาล่ารสเผ็ด", "ประเทศ": "ประเทศอินเดีย"},
    {"อาหาร": "ติ่มซำ", "คำใบ้": "แดนพญามังกร", "ประเทศ": "ประเทศจีน"},
    {"อาหาร": "แหนมเนือง", "คำใบ้": "ที่ตั้งสุสานโฮจิมินห์", "ประเทศ": "ประเทศเวียดนาม"},
    {"อาหาร": "พายเนื้อ", "คำใบ้": "แดนโคอาลา และ โอเปร่าเฮาส์", "ประเทศ": "ประเทศออสเตรเลีย"}
]

# เริ่มเกม
if "question" not in st.session_state:
    st.session_state.question = random.choice(data)

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

question = st.session_state.question

st.subheader("🍴 คำถาม")
st.write("อาหารนี้มาจากประเทศอะไร?")
st.markdown(f"### {question['อาหาร']}")

st.info(f"💡 คำใบ้: {question['คำใบ้']}")

countries = [item["ประเทศ"] for item in data]

answer = st.selectbox(
    "เลือกคำตอบ",
    ["-- เลือกประเทศ --"] + countries
)

if st.button("ตรวจคำตอบ"):
    if answer == "-- เลือกประเทศ --":
        st.warning("กรุณาเลือกคำตอบก่อน")
    elif answer == question["ประเทศ"]:
        st.success("🎉 ถูกต้อง!")
        st.session_state.score += 1
        st.session_state.answered = True
    else:
        st.error(f"❌ ผิด! คำตอบคือ {question['ประเทศ']}")
        st.session_state.answered = True

st.write(f"### 🏆 คะแนน: {st.session_state.score}")

if st.button("➡️ ข้อถัดไป"):
    st.session_state.question = random.choice(data)
    st.session_state.answered = False
    st.rerun()

if st.button("🔄 เริ่มเกมใหม่"):
    st.session_state.score = 0
    st.session_state.question = random.choice(data)
    st.session_state.answered = False
    st.rerun()
