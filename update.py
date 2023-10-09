from db_connect import *

cursor = db.cursor()

sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("Anjuhari", "Campalagian", 1)

cursor.execute(sql, val)
db.commit()

print("{} data diubah".format(cursor.rowcount))
