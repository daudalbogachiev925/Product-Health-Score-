import streamlit as st
from health import load_config, overall_score

st.title("❤️ Product Health Score")
cfg = load_config()

growth = st.slider("Growth, % MoM", -10, 50, 10)
retention = st.slider("Retention D30", 0.0, 1.0, 0.45)
monetization = st.slider("LTV/CAC", 0.0, 5.0, 1.5)
nps = st.slider("NPS", -100, 100, 40)
support = st.slider("Support tickets per user", 0.0, 0.2, 0.05)

vals = {"growth": growth, "retention": retention,
        "monetization": monetization, "nps": nps, "support": support}

total, breakdown = overall_score(vals, cfg)
st.metric("Overall Health Score", total)
st.json(breakdown)
