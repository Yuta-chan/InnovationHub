import pymysql
from dotenv import load_dotenv
import os
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def configure():
    load_dotenv()
configure()

db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")

# database connection
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


try:
    # read image
    img = cv2.imread('test2.png')
    # pasamos a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # distinguimos los umbrales
    _, thre = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # quitamos el ruido
    image = cv2.medianBlur(thre, 3) # impares
    # extract text
    text1 = pytesseract.image_to_string(thre)
    text2 = pytesseract.image_to_string(image)
    print(text1)
    print(text2)
except Exception as e:
    print(f"Error reading image: {e}")