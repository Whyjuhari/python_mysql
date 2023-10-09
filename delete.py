from db_connect import *

cursor = db.cursor()

sql = "DELETE FROM customers WHERE customer_id=%s"
val = (4, )
cursor.execute(sql, val)
db.commit()

print("{} data dihapus".format(cursor.rowcount))
