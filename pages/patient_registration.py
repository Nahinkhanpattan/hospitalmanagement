import streamlit as st
from utils.db_utils import execute_query, fetch_all
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("👤 Patient Registration")

name = st.text_input("Name")
age = st.number_input("Age", min_value=0)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
phone = st.text_input("Phone")

if st.button("Register Patient"):
    query = "INSERT INTO Patients (name, age, gender, phone) VALUES (%s,%s,%s,%s)"
    execute_query(query, (name, age, gender, phone))
    st.success("Patient registered successfully!")

st.subheader("📋 Registered Patients")
patients = fetch_all("SELECT * FROM Patients")
st.dataframe(patients, use_container_width=True)
