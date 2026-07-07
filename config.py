import mysql.connector

print("Connecting to MySQL...")

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Lolipop@123",
    database="trademind"
)

print("Connected!")

cursor = db.cursor()