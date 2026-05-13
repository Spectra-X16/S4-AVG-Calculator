import streamlit as st

st.set_page_config(page_title="S4 Average Calculator", page_icon="🎓")

st.title("🎓 Forth Semester Average Calculator For Automation Field")

# 1. Get the User's Name
name = st.text_input("Please Write Your Name:", placeholder="e.g.Mohammed")

st.divider()

# Helper function to create two columns for Exam and TD/TP
def get_subject_marks(subject_name, label_exam="Exam", label_td="TD"):
    col1, col2 = st.columns(2)
    with col1:
        exam = st.number_input(f"{subject_name} ({label_exam})", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        td = st.number_input(f"{subject_name} ({label_td})", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    return exam, td

# 2. Collect Marks for Main Subjects (Exam/TD/Coeff)
subjects = {
    "Analyse 3": (3, "TD"),
    "Vibration-Waves": (2, "TD"),
    "FD-Electronics 1": (2, "TD"),
    "FD-Electrotechnics 1": (2, "TD"),
    "Python": (2, "TP"),
    "Probability and Statistics": (2, "TD"),
}

weighted_sum = 0
for sub, (coeff, td_label) in subjects.items():
    exam, td = get_subject_marks(sub, label_td=td_label)
    weighted_sum += ((exam * 0.6) + (td * 0.4)) * coeff

st.divider()

# 3. Collect Extra Marks (TPs and Minor Subjects)
st.subheader("Additional Modules")
c1, c2 = st.columns(2)
with c1:
    tp_vib = st.number_input("TP Vibration-Waves", 0.0, 20.0, 10.0)
    tp_elec = st.number_input("TP Electronique & Electrotech", 0.0, 20.0, 10.0)
with c2:
    energy = st.number_input("Energies et Environnement", 0.0, 20.0, 10.0)
    genie_elec = st.number_input("Etat de l'art de Génie Electrique", 0.0, 20.0, 10.0)

# 4. Calculation Logic
if st.button("Calculate My Average", type="primary"):
    total_sum = weighted_sum + (tp_vib * 1) + (tp_elec * 1) + (energy * 1) + (genie_elec * 1)
    final_avg = round(total_sum / 17, 2)

    st.divider()
    if final_avg >= 10:
        st.balloons() # Fun animation for passing!
        st.success(f"### Average: {final_avg} \nGood Job **{name}**, You Passed!")
    else:
        st.error(f"### Average: {final_avg} \nGood Luck Next Time **{name}**.")
st.divider()
st.markdown("""
    <h1 style='text-align: center; font-size: 40px; color: #00008B;'>
        Developed by  𝑆𝑝𝑒𝑒𝑒𝑒𝑐𝑡𝑟𝑎 X
    </h1>
    """, unsafe_allow_html=True)