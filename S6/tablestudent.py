import mysql.connector

db = mysql.connector.connect(user="root",password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

# cursorObject.execute("CREATE DATABASE dbtestowa")
tablestudent = "CREATE TABLE student(imie VARCHAR(60),nazwisko VARCHAR(60), nralb int);"
cursorObject.execute(tablestudent)
print("tabela student została utworzona")
sqldane = "INSERT INTO student(imie,nazwisko,nralb) VALUES(%s,%s,%s)"
val = ("Jan","Kot",43555)
cursorObject.execute(sqldane,val)
db.commit()
print(f" osadzono {cursorObject.rowcount} rekordów")

db.close()
