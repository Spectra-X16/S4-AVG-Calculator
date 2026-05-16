import streamlit as st
import pandas as pd

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

def tp_only(label):
    tp = st.number_input(f"{label} (TP)", min_value=0.0, max_value=20.0, value=10.0, step=0.25)
    formula = f"TP ({tp}) × 1.0 = **{round(tp, 2)}**"
    return tp, formula

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

arch,        arch_f        = exam_only("Architecture systèmes automatisés")
secu,        secu_f        = exam_only("Sécurité électrique")
st.divider()

st.markdown("**Logique combinatoire & séquentielle**")
logique,     logique_f     = exam_td("Logique combinatoire & séquentielle")
tp_logique,  tp_logique_f  = tp_only("TP Logique combinatoire & séquentielle")
st.divider()

st.markdown("**Systèmes asservis linéaires & continus**")
asservis,    asservis_f    = exam_td("Systèmes asservis linéaires & continus")
tp_asservis, tp_asservis_f = tp_only("TP Systèmes asservis linéaires & continus")
st.divider()

numerique,   numerique_f   = exam_td_tp("Méthodes Numériques")
st.divider()

signal,      signal_f      = exam_td("Théorie du Signal")
tec,         tec_f         = exam_td("Techniques d'Expression & Communication")
st.divider()

mesures,     mesures_f     = exam_tp("Mesures électriques & électroniques")

# ── Calculation ───────────────────────────────────────────────────────────────

TOTAL_COEFF = 18

if st.button("Calculate My Average", type="primary"):

    modules = [
        ("Architecture systèmes automatisés",       arch,        1, arch_f),
        ("Sécurité électrique",                     secu,        1, secu_f),
        ("Logique combinatoire & séquentielle",     logique,     2, logique_f),
        ("TP Logique combinatoire & séquentielle",  tp_logique,  1, tp_logique_f),
        ("Systèmes asservis linéaires & continus",  asservis,    3, asservis_f),
        ("TP Systèmes asservis",                    tp_asservis, 1, tp_asservis_f),
        ("Méthodes Numériques",                     numerique,   3, numerique_f),
        ("Théorie du Signal",                       signal,      2, signal_f),
        ("Techniques Expression & Com.",            tec,         2, tec_f),
        ("Mesures électriques & élec.",             mesures,     2, mesures_f),
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

    # ── Full calculation breakdown table ──────────────────────────────────────
    st.subheader("🧮 Full Calculation Breakdown")

    rows = []
    for mod_name, score, coeff, _ in modules:
        weighted = round(score * coeff, 2)
        status   = "✅" if score >= 10 else "❌"
        rows.append({
            "Status": status,
            "Module": mod_name,
            "Score /20": round(score, 2),
            "Coeff": coeff,
            "Score × Coeff": weighted,
        })

    # Totals row
    rows.append({
        "Status": "",
        "Module": "TOTAL",
        "Score /20": "",
        "Coeff": TOTAL_COEFF,
        "Score × Coeff": round(weighted_sum, 2),
    })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown(f"""
**Final Average = Total (Score × Coeff) ÷ Total Coeff**

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
    <h1 style='text-align: center; font-size: 43px; color: #00008B;'>
        Developed by  𝑆𝑝𝑒𝑒𝑒𝑒𝑐𝑡𝑟𝑎 X
    </h1>
    """, unsafe_allow_html=True)