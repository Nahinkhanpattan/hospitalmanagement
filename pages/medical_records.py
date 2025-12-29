import streamlit as st
from utils.db_utils import execute_query, fetch_all
import datetime

st.header("🩺 Medical Records")

patients = fetch_all("SELECT patient_id, name FROM Patients")
patient_options = patients['name'].tolist()

patient_name = st.selectbox("Select Patient", patient_options)

diagnosis = st.text_area("Diagnosis")
prescription = st.text_area("Prescription")

if st.button("Add Record"):
    patient_id = patients[patients['name'] == patient_name]['patient_id'].iloc[0]
    query = """
    INSERT INTO Medical_Records (patient_id, diagnosis, prescription, record_date)
    VALUES (%s,%s,%s,%s)
    """
    execute_query(query, (patient_id, diagnosis, prescription, datetime.date.today()))
    st.success("Medical record added!")

records = fetch_all("""
SELECT m.record_id, p.name as patient_name, m.diagnosis, m.prescription, m.record_date
FROM Medical_Records m
JOIN Patients p ON m.patient_id = p.patient_id
""")

st.subheader("📋 Medical Records")
st.table(records)
