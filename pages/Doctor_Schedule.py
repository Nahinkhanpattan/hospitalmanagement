import streamlit as st
from utils.db_utils import fetch_all
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("📆 Doctor Schedules")

doctors = fetch_all("SELECT * FROM Doctors")

for index, d in doctors.iterrows():
    st.markdown(f"""
    **👨‍⚕️ {d['name']}**  
    🧠 Specialization: {d['specialization']}  
    📅 Available Days: {d['available_days']}
    """)
    st.divider()
