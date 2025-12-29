import streamlit as st
from utils.db_utils import fetch_all
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("🔍 Patient Search & History")

patients = fetch_all("SELECT patient_id, name FROM Patients")
patient_options = patients['name'].tolist()

patient_name = st.selectbox("Select Patient", patient_options)

st.subheader("📅 Appointments")
patient_id = patients[patients['name'] == patient_name]['patient_id'].iloc[0]
appointments = fetch_all(f"""
SELECT appointment_date, d.name as doctor_name
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE patient_id = {patient_id}
""")
st.dataframe(appointments, use_container_width=True)

st.subheader("🩺 Medical Records")
records = fetch_all(f"""
SELECT diagnosis, prescription, record_date
FROM Medical_Records
WHERE patient_id = {patient_id}
""")
st.dataframe(records, use_container_width=True)
