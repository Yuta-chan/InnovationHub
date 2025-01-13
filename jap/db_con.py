import pymysql
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
configure()

db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")

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