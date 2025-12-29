import streamlit as st
from utils.db_utils import fetch_all

st.title("📊 Hospital Dashboard")

patients_count = fetch_all("SELECT COUNT(*) as count FROM Patients")['count'].iloc[0]
doctors_count = fetch_all("SELECT COUNT(*) as count FROM Doctors")['count'].iloc[0]
appointments_count = fetch_all("SELECT COUNT(*) as count FROM Appointments")['count'].iloc[0]
records_count = fetch_all("SELECT COUNT(*) as count FROM Medical_Records")['count'].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("👤 Patients", patients_count)
col2.metric("👨‍⚕️ Doctors", doctors_count)
col3.metric("📅 Appointments", appointments_count)
col4.metric("🩺 Records", records_count)

st.success("Hospital system is running smoothly ✅")
