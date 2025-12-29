import os
import streamlit as st
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=st.secrets.get("DB_HOST", os.getenv("DB_HOST")),
            user=st.secrets.get("DB_USER", os.getenv("DB_USER")),
            password=st.secrets.get("DB_PASSWORD", os.getenv("DB_PASSWORD")),
            database=st.secrets.get("DB_NAME", os.getenv("DB_NAME")),
            port=int(st.secrets.get("DB_PORT", os.getenv("DB_PORT")))
        )

        if conn.is_connected():
            print("✅ MySQL Database Connected Successfully")

        return conn

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)
        return None
