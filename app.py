import streamlit as st
from utils.ui import inject_responsive_css

st.set_page_config(page_title="Hospital Management System", layout="wide")
inject_responsive_css()

st.title("🏥 Hospital Management System")
st.markdown("""
Use the sidebar to navigate:
- Patient Registration
- Doctor Management
- Appointment Booking
- Medical Records
- Doctors
""")
st.caption("Mobile-friendly layout (responsive CSS applied) ✅")
