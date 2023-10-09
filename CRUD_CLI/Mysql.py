import mysql.connector 

sd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "why"
)

cursor = sd.cursor()
sql = "create database konn"
cursor.execute(sql)