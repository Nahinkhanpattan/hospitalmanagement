import mysql.connector
from mysql.connector import Error
import dotenv

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=dotenv.get_key(".env", "DB_HOST"),
            user=dotenv.get_key(".env", "DB_USER"),
            password=dotenv.get_key(".env", "DB_PASSWORD"),
            database=dotenv.get_key(".env", "DB_NAME"),
            port=dotenv.get_key(".env", "DB_PORT")
        )

        if conn.is_connected():
            print("✅ MySQL Database Connected Successfully")

        return conn

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)
        return None
