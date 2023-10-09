from db_connect import *

cursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
    ("Juhari", "Jakarta"),
    ("WhyJuhari", "Surabaya"),
    ("Anju", "Bandung"),
    ("Friday", "Amerika")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
