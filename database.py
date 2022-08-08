import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (Name TEXT,Author TEXT,Publisher TEXT,Page_Count INT)")
    con.commit()

def add_data():
    cursor.execute("Insert into library Values('İstanbul Hatırası','Ahmet Ümit','Everest Yayıncılık',561)")
    con.commit()

def add_data2(name,author,publisher,page_count):
    cursor.execute("Insert into library Values(?,?,?,?)",(name,author,publisher,page_count))
    con.commit()

def show_data():
    cursor.execute("Select * From library")
    list = cursor.fetchall()
    print("Contents of library table:")
    for i in list:
        print(i)

def show_data2():
    cursor.execute("Select Name,Author From library")
    list2 = cursor.fetchall()
    print("Contents of library table:")
    for i in list2:
        print(i)

def show_data3(Publisher):
    cursor.execute("Select * from library where Publisher = ?",(Publisher,))
    list3 = cursor.fetchall()
    print("Contents of library table:")
    for i in list3:
        print(i)

def update_data(old_publisher,new_publisher):
    cursor.execute("Update library set Publisher = ? where Publisher = ?",(old_publisher,new_publisher))
    con.commit()

def delete_data(Author):
    cursor.execute("Delete From library where Author = ?",(Author,))
    con.commit()

show_data()

con.close()