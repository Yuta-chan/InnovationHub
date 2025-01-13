
import pymysql
import creds
from dotenv import load_dotenv
import os

print(creds.db_host)
print(creds.db_user)
print(creds.db_password)
print(creds.db_name)
credds = load_dotenv()
print(credds)
db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")
print(os.getenv("db_host"))
print(db_host)
print(db_user)

def get_db_connection():
    """Connect to MySQL database."""
    try:
        print("Connecting to DataBase...")
        return pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
    except Exception as e:
        print(f"Error connecting to DataBase: {e}")
        return None
con = get_db_connection()

def get_db_connection_val():
    """Connect to MySQL database."""
    try:
        print("Connecting to DataBase...")
        return pymysql.connect(
            host=creds.db_host,
            user=creds.db_user,
            password=creds.db_password,
            database=creds.db_name
        )
    except Exception as e:
        print(f"Error connecting to DataBase: {e}")
        return None
con = get_db_connection()