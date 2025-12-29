from db.db_config import get_connection
import pandas as pd

def execute_query(query, values=None):
    conn = get_connection()
    cursor = conn.cursor()

    if values:
        # convert numpy types to native python types
        values = tuple(
            int(v) if hasattr(v, "item") else v
            for v in values
        )

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def fetch_all(query, values=None):
    conn = get_connection()
    cursor = conn.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return pd.DataFrame(data, columns=columns)
