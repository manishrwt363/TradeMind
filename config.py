import mysql.connector

from services.logger_service import logger

logger.info("Connecting to MySQL...")

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Lolipop@123",
    database="trademind"
)

logger.info("Database Connected Successfully")

cursor = db.cursor()