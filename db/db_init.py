import psycopg2

def init_db():
    try:
        conn = psycopg2.connect(
            database="flask_db",
            user="sabaataha",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id SERIAL PRIMARY KEY,
                question TEXT,
                answer TEXT
            );
        ''')

        conn.commit()
        print("Initialized database schema.")

    except psycopg2.Error as e:
        print("Error initializing database schema:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()