import streamlit as st
from utils.db_utils import fetch_all

st.header("📆 Doctor Schedules")

doctors = fetch_all("SELECT * FROM Doctors")

for index, d in doctors.iterrows():
    st.markdown(f"""
    **👨‍⚕️ {d['name']}**  
    🧠 Specialization: {d['specialization']}  
    📅 Available Days: {d['available_days']}
    """)
    st.divider()
