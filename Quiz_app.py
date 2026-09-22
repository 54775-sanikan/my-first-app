import streamlit as st
import random

st.set_page_config(
    page_title="Challenge Quiz Game",
    page_icon="🍜",
    layout="centered"
)

# -------------------------
# ข้อมูลคำถาม
# -------------------------
questions = [
    {
        "country": "ประเทศไทย",
        "food": "ต้มยำกุ้ง",
        "options": ["อินโดนีเซีย", "ประเทศไทย", "มาเลเซีย", "เวียดนาม"]
    },
    {
        "country": "ญี่ปุ่น",
        "food": "ซูชิ",
        "options": ["จีน", "เกาหลีใต้", "ญี่ปุ่น", "ไทย"]
    },
    {
        "country": "ฝรั่งเศส",
        "food": "ครัวซองต์",
        "options": ["ฝรั่งเศส", "อิตาลี", "สเปน", "เยอรมนี"]
    },
    {
        "country": "อิตาลี",
        "food": "พิซซ่า",
        "options": ["ฝรั่งเศส", "อิตาลี", "จีน", "เม็กซิโก"]
    },
    {
        "country": "เกาหลีใต้",
        "food": "กิมจิ",
        "options": ["ญี่ปุ่น", "จีน", "เกาหลีใต้", "เวียดนาม"]
    },
    {
        "country": "จีน",
        "food": "เป็ดปักกิ่ง",
        "options": ["จีน", "ไทย", "อินเดีย", "ญี่ปุ่น"]
    },
    {
        "country": "อินเดีย",
        "food": "แกงกะหรี่",
        "options": ["อินเดีย", "จีน", "ฝรั่งเศส", "สเปน"]
    },
    {
        "country": "สเปน",
        "food": "ปาเอยา",
        "options": ["อิตาลี", "สเปน", "ฝรั่งเศส", "โปรตุเกส"]
    },
    {
        "country": "เม็กซิโก",
        "food": "ทาโก้",
        "options": ["เม็กซิโก", "บราซิล", "สเปน", "อิตาลี"]
    },
    {
        "country": "เวียดนาม",
        "food": "เฝอ",
        "options": ["ไทย", "จีน", "เวียดนาม", "เกาหลีใต้"]
    }
]

# -------------------------
# เริ่มต้นค่า
# -------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "questions" not in st.session_state:
    st.session_state.questions = questions.copy()
    random.shuffle(st.session_state.questions)

if "number" not in st.session_state:
    st.session_state.number = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "finished" not in st.session_state:
    st.session_state.finished = False


# -------------------------
# หน้าหลัก
# -------------------------
if not st.session_state.started:

    st.title("🌎 Challenge Quiz Game")
    st.header("🍜 เกมทายอาหารประจำชาติ")

    st.write("ทดสอบความรู้เกี่ยวกับอาหารประจำชาติจากทั่วโลก")

    st.divider()

    st.info("🎮 เกมมีทั้งหมด 10 ข้อ")

    if st.button("▶️ เริ่มเกม", use_container_width=True):
        st.session_state.started = True
        st.rerun()


# -------------------------
# หน้าเกม
# -------------------------
elif not st.session_state.finished:

    number = st.session_state.number
    q = st.session_state.questions[number]

    st.subheader(
        f"ข้อที่ {number + 1} / {len(st.session_state.questions)}"
    )

    st.write("### 🍽️ คำถาม")
    st.write(f"อาหาร **{q['food']}** เป็นอาหารประจำชาติของประเทศใด?")

    answer = st.radio(
        "เลือกคำตอบ",
        q["options"],
        key=f"answer_{number}"
    )

    if st.button("✅ ตอบ", use_container_width=True):

        if answer == q["country"]:
            st.success("🎉 ถูกต้อง!")
            st.session_state.score += 1
        else:
            st.error(f"❌ ผิด! คำตอบคือ {q['country']}")

        if number + 1 < len(st.session_state.questions):
            st.session_state.number += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()


# -------------------------
# หน้าผลคะแนน
# -------------------------
else:

    st.title("🏆 จบเกมแล้ว!")

    score = st.session_state.score

    st.metric(
        "คะแนนของคุณ",
        f"{score} / 10"
    )

    if score >= 8:
        st.success("🌟 ดีมาก!")
    elif score >= 5:
        st.info("👍 ดี!")
    elif score >= 1:
        st.warning("📚 ควรปรับปรุง")
    else:
        st.error("🔄 ลองใหม่อีกครั้ง")

    st.divider()

    if st.button("🔄 เล่นอีกครั้ง", use_container_width=True):
        st.session_state.started = False
        st.session_state.number = 0
        st.session_state.score = 0
        st.session_state.finished = False
        random.shuffle(st.session_state.questions)
        st.rerun()
