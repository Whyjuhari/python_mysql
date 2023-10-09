from app_cruds import *
import os

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

