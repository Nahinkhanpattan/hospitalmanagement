import streamlit as st
from utils.db_utils import execute_query, fetch_all
import datetime
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("📅 Appointment Booking")

# Fetch patients and doctors
patients = fetch_all("SELECT patient_id, name FROM Patients")
doctors = fetch_all("SELECT doctor_id, name FROM Doctors")

# Safety check
if patients.empty or doctors.empty:
    st.warning("Please add patients and doctors first.")
    st.stop()

# Prepare options
patient_options = list(patients.itertuples(index=False))
doctor_options = list(doctors.itertuples(index=False))

# Select patient and doctor
patient = st.selectbox(
    "Select Patient",
    patient_options,
    format_func=lambda x: x[1]
)

doctor = st.selectbox(
    "Select Doctor",
    doctor_options,
    format_func=lambda x: x[1]
)

# Convert IDs safely (numpy → python int)
patient_id = int(patient[0])
doctor_id = int(doctor[0])

date = st.date_input("Appointment Date", datetime.date.today())

if st.button("Book Appointment"):
    query = """
    INSERT INTO Appointments (patient_id, doctor_id, appointment_date)
    VALUES (%s, %s, %s)
    """
    execute_query(query, (patient_id, doctor_id, date))
    st.success("✅ Appointment booked!")

# Show appointments
appointments = fetch_all("""
SELECT a.appointment_id,
       p.name AS patient_name,
       d.name AS doctor_name,
       a.appointment_date
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id
ORDER BY a.appointment_date DESC
""")

st.subheader("📋 Appointments")
st.dataframe(appointments, use_container_width=True)
