import streamlit as st

st.set_page_config(page_title="S4 Average Calculator", page_icon="🎓")

st.title("🎓 S4 Average Calculator — Automation Field")

# 1. Get the User's Name
name = st.text_input("Please Write Your Name:", placeholder="e.g. Mohammed")

st.divider()

# ── Helper functions ──────────────────────────────────────────────────────────

def exam_only(label):
    exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    formula = f"Exam ({exam}) × 1.0 = **{round(exam, 2)}**"
    return exam, formula

def exam_td(label):
    col1, col2 = st.columns(2)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        td = st.number_input(f"{label} (TD)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    score = exam * 0.6 + td * 0.4
    formula = f"Exam ({exam}) × 0.6  +  TD ({td}) × 0.4 = **{round(score, 2)}**"
    return score, formula

def exam_tp(label):
    col1, col2 = st.columns(2)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        tp = st.number_input(f"{label} (TP)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    score = exam * 0.6 + tp * 0.4
    formula = f"Exam ({exam}) × 0.6  +  TP ({tp}) × 0.4 = **{round(score, 2)}**"
    return score, formula

def exam_td_tp(label):
    col1, col2, col3 = st.columns(3)
    with col1:
        exam = st.number_input(f"{label} (Exam)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col2:
        td = st.number_input(f"{label} (TD)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    with col3:
        tp = st.number_input(f"{label} (TP)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    score = exam * 0.6 + td * 0.2 + tp * 0.2
    formula = f"Exam ({exam}) × 0.6  +  TD ({td}) × 0.2  +  TP ({tp}) × 0.2 = **{round(score, 2)}**"
    return score, formula

# ── Subjects ──────────────────────────────────────────────────────────────────

st.subheader("📘 Modules")

arch,      arch_f      = exam_only("Architecture systèmes automatisés")         # coeff 1
secu,      secu_f      = exam_only("Sécurité électrique")                       # coeff 1
st.divider()
logique,   logique_f   = exam_td_tp("Logique combinatoire & séquentielle")      # coeff 2
st.divider()
asservis,  asservis_f  = exam_td_tp("Systèmes asservis linéaires & continus")   # coeff 3
numerique, numerique_f = exam_td_tp("Méthodes Numériques")                      # coeff 3
st.divider()
signal,    signal_f    = exam_td("Théorie du Signal")                           # coeff 2
tec,       tec_f       = exam_td("Techniques d'Expression & Communication")     # coeff 2
st.divider()
mesures,   mesures_f   = exam_tp("Mesures électriques & électroniques")         # coeff 2

# ── Calculation ───────────────────────────────────────────────────────────────

TOTAL_COEFF = 16  # 1+1+2+3+3+2+2+2

if st.button("Calculate My Average", type="primary"):

    modules = [
        ("Architecture systèmes automatisés",  arch,      1, arch_f),
        ("Sécurité électrique",                secu,      1, secu_f),
        ("Logique combinatoire & séquentielle",logique,   2, logique_f),
        ("Systèmes asservis linéaires",        asservis,  3, asservis_f),
        ("Méthodes Numériques",                numerique, 3, numerique_f),
        ("Théorie du Signal",                  signal,    2, signal_f),
        ("Techniques Expression & Com.",       tec,       2, tec_f),
        ("Mesures électriques & élec.",        mesures,   2, mesures_f),
    ]

    weighted_sum = sum(score * coeff for _, score, coeff, _ in modules)
    final_avg    = round(weighted_sum / TOTAL_COEFF, 2)

    st.divider()

    # ── Per-module results ────────────────────────────────────────────────────
    st.subheader("📊 Module Results")

    for mod_name, score, coeff, formula in modules:
        weighted = round(score * coeff, 2)
        status   = "✅" if score >= 10 else "❌"
        with st.expander(f"{status}  {mod_name}   —   Score: {round(score, 2)}/20   |   Coeff: {coeff}   |   Weighted: {weighted}"):
            st.markdown(f"**Module formula:** {formula}")
            st.markdown(f"**Contribution to average:** {round(score, 2)} × {coeff} = **{weighted}**")

    st.divider()

    # ── Full calculation breakdown ────────────────────────────────────────────
    st.subheader("🧮 Full Calculation Breakdown")

    contributions = "  +  ".join(
        [f"({round(score, 2)} × {coeff})" for _, score, coeff, _ in modules]
    )
    st.markdown(f"""
**Step 1 — Weighted sum of all modules:**

{contributions} = **{round(weighted_sum, 2)}**

---

**Step 2 — Divide by total coefficients ({TOTAL_COEFF}):**

{round(weighted_sum, 2)} ÷ {TOTAL_COEFF} = **{final_avg} / 20**
""")

    st.divider()

    # ── Final result ──────────────────────────────────────────────────────────
    if final_avg >= 10:
        st.success(f"### 🎉 Final Average: {final_avg} / 20\nGood Job **{name}**, You Passed!")
    else:
        st.error(f"### Final Average: {final_avg} / 20\nGood Luck Next Time **{name}**. 💪")

st.divider()
st.markdown("""
    <h1 style='text-align: center; font-size: 45px; color: #0064FF;'>
        Developed by  𝑆𝑝𝑒𝑒𝑒𝑒𝑐𝑡𝑟𝑎 X
    </h1>
    """, unsafe_allow_html=True)