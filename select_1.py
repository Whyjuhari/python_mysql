from db_connect import *


cursor = db.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)