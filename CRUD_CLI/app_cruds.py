from db_connect import *

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



