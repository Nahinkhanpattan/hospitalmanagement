import streamlit as st
from utils.db_utils import execute_query, fetch_all
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("👨‍⚕️ Doctor Management")

name = st.text_input("Doctor Name")
specialization = st.text_input("Specialization")
available_days = st.text_input("Available Days (Mon-Fri)")

if st.button("Add Doctor"):
    query = "INSERT INTO Doctors (name, specialization, available_days) VALUES (%s,%s,%s)"
    execute_query(query, (name, specialization, available_days))
    st.success("Doctor added successfully!")

doctors = fetch_all("SELECT * FROM Doctors")
st.subheader("📋 Doctors List")
st.dataframe(doctors, use_container_width=True)
