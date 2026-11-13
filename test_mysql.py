
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test Database Connection
try:
    mydb = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD")
    )

    if mydb.is_connected():
        print("Successfully connected to MySQL!")

    mydb.close()

except mysql.connector.Error as e:
    print("MySQL Connection Error:", e)


