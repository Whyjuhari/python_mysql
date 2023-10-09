from db_connect import *

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_mainan")

print("Database berhasil dibuat!")