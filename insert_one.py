from db_connect import *

cursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dian", "Mataran")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
