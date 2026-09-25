import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "inventory_db",
    "user": "postgres",
    "password": "2525"
}


def get_connection():
    try:
        connection = psycopg.connect(**DB_CONFIG)
        return connection

    except psycopg.Error as error:
        print(f"Database connection error: {error}")
        return None

if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("Database connected successfully!")
        connection.close()