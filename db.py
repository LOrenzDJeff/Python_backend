import psycopg2
from psycopg2.extras import RealDictCursor 
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def get_radio_signals():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM radio_signals;")
        signals = cursor.fetchall()
        return signals
    except Exception as error:
        print(f"Ошибка при подключении к базе данных: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()