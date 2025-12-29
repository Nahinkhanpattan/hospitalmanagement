import mysql.connector
from db.db_config import get_connection

def init_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Read and execute SQL script
        with open('db/db_init.sql', 'r', encoding='utf-8') as sql_file:
            sql_script = sql_file.read()

            
        # Execute each statement separately
        statements = sql_script.split(';')
        for statement in statements:
            statement = statement.strip()
            if statement:
                cursor.execute(statement)
        
        conn.commit()
        print("✓ Database initialized successfully!")
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    init_database()
