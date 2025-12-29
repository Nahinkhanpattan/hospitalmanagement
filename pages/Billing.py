import streamlit as st
from utils.db_utils import execute_query, fetch_all
import datetime
from utils.ui import inject_responsive_css

inject_responsive_css()
st.header("💳 Billing")

patients = fetch_all("SELECT patient_id, name FROM Patients")
patient_options = patients['name'].tolist()

patient_name = st.selectbox("Select Patient", patient_options)

amount = st.number_input("Amount", min_value=0.0)
description = st.text_area("Description")

if st.button("Generate Bill"):
    patient_id = patients[patients['name'] == patient_name]['patient_id'].iloc[0]
    query = """
    INSERT INTO Billing (patient_id, amount, description, bill_date)
    VALUES (%s,%s,%s,%s)
    """
    execute_query(query, (patient_id, amount, description, datetime.date.today()))
    st.success("Bill generated successfully!")

bills = fetch_all("""
SELECT b.bill_id, p.name as patient_name, b.amount, b.description, b.bill_date
FROM Billing b
JOIN Patients p ON b.patient_id = p.patient_id
""")
st.dataframe(bills, use_container_width=True)
