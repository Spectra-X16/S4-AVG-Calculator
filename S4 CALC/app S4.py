import streamlit as st

st.set_page_config(page_title="S4 Average Calculator", page_icon="🎓")

st.title("🎓 Fourth Semester Average Calculator — Automation Field")

# 1. Get the User's Name
name = st.text_input("Please Write Your Name:", placeholder="e.g. Mohammed")

st.divider()

# ── Helper functions ──────────────────────────────────────────────────────────

def exam_only(label):
    """Single exam mark, no TD/TP."""
    return st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)

def exam_td(label):
    col1, col2 = st.columns(2)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        td = st.number_input(f"{label} (TD)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    return exam * 0.6 + td * 0.4

def exam_tp(label):
    col1, col2 = st.columns(2)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        tp = st.number_input(f"{label} (TP)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    return exam * 0.6 + tp * 0.4

def exam_td_tp(label):
    col1, col2, col3 = st.columns(3)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        td = st.number_input(f"{label} (TD)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col3:
        tp = st.number_input(f"{label} (TP)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    return exam * 0.6 + td * 0.2 + tp * 0.2

# ── Subjects ──────────────────────────────────────────────────────────────────

st.subheader("📘 Modules")

# Coeff 1 — Exam only
arch  = exam_only("Architecture systèmes automatisés")          # coeff 1
secu  = exam_only("Sécurité électrique")                        # coeff 1

st.divider()

# Coeff 2 — Exam + TD + TP
logique = exam_td_tp("Logique combinatoire & séquentielle")     # coeff 2

st.divider()

# Coeff 3 — Exam + TD + TP
asservis  = exam_td_tp("Systèmes asservis linéaires & continus") # coeff 3
numerique = exam_td_tp("Méthodes Numériques")                    # coeff 3

st.divider()

# Coeff 2 — Exam + TD
signal = exam_td("Théorie du Signal")                           # coeff 2
tec    = exam_td("Techniques d'Expression & Communication")     # coeff 2

st.divider()

# Coeff 2 — Exam + TP
mesures = exam_tp("Mesures électriques & électroniques")        # coeff 2

# ── Calculation ───────────────────────────────────────────────────────────────

TOTAL_COEFF = 16  # 1+1+2+3+3+2+2+2

if st.button("Calculate My Average", type="primary"):

    weighted_sum = (
        arch      * 1 +
        secu      * 1 +
        logique   * 2 +
        asservis  * 3 +
        numerique * 3 +
        signal    * 2 +
        tec       * 2 +
        mesures   * 2
    )

    final_avg = round(weighted_sum / TOTAL_COEFF, 2)

    st.divider()
    if final_avg >= 10:
        st.balloons()
        st.success(f"### Average: {final_avg} / 20\nGood Job **{name}**, You Passed! 🎉")
    else:
        st.error(f"### Average: {final_avg} / 20\nGood Luck Next Time **{name}**. 💪")

st.divider()
st.markdown("""
    <h1 style='text-align: center; font-size: 40px; color: #00008B;'>
        Developed by  𝑆𝑝𝑒𝑒𝑒𝑒𝑐𝑡𝑟𝑎 X
    </h1>
    """, unsafe_allow_html=True)