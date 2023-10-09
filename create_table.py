from db_connect import *

cursor = db.cursor()
sql = """CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255)
    )
    """

cursor.execute(sql)
print("Tabel customers berhasil dibuat")