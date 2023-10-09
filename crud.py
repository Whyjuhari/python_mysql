import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="why"
)


cursor = db.cursor()
cursor.execute("CREATE DATABASE tryTesting")
print("database berhasil dibuat")
cursor.execute("USE tryTesting")
print("database berhasil digunakan")
cursor.execute("CREATE TABLE customers (customer_id int auto_increment primary key, name varchar(25) not null, address varchar(20) not null)")
print("tabel berhasil dibuat")




# Fungsi stop 
def stop():
    stop = input("Do You Want To Continue?[Y/n] : ")
    if stop == "n":
        return True
    return False


# Fungsi untuk menambahkan data
def insert_data(db):
    while True:
        name = input("Masukkan Nama      : ")
        address = input("Masukkan Alamat : ")

        val = (name, address)
        cursor = db.cursor()

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil ditambahkan!".format(cursor.rowcount))

        if stop():
            break


# Fungsi untuk menampilkan data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Data tidak ada")
    else:
        for data in results:
            print(data)


# Fungsi untuk mengubah data
def update_data(db):
    while True:
        cursor = db.cursor()
        show_data(db)

        id = input("Masukkan customer_id : ")
        name = input("Masukkan Nama      : ")
        address = input("Masukkan Alamat : ")


        sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
        val = (name, address, id)
        cursor.execute(sql, val)

        db.commit()

        print("{} data berhasil diubah".format(cursor.rowcount))
        
        if stop():
            break

# Fungsi untuk menghapus data
def delete_data(db):
    while True:
        cursor = db.cursor()
        show_data(db)
        id = input("Masukkan customer_id : ")
        sql = "DELETE FROM customers WHERE customer_id=%s"
        val = (id,)
        cursor.execute(sql, val)

        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

        if stop():
            break

# Fungsi untuk mencari data
def search_data(db):
    while True:
        cursor = db.cursor()
        keywoard = input("Masukkan keywoard : ")

        sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
        val = ("%{}%".format(keywoard), "%{}%".format(keywoard))

        cursor.execute(sql, val)
        results = cursor.fetchall()

        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

        if stop():
            break


# Menu
next = False
while (not next):
    print("=== APLIKASI DATABASE PYTHON V CLI")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. keluar")


    menu = int(input("Pilih menu -> "))


    if menu == 1:
        insert_data(db)       
    elif menu == 2:
        show_data(db)
    elif menu == 3:
        update_data(db)        
    elif menu == 4:
        delete_data(db)
    elif menu == 5:
        search_data(db)
    elif menu == 0:
        next = True
        os.system("clear")

    else:
        print("Menu salah!")


