import mysql.connector

db = mysql.connector.connect(user="root",password='abc123',host='127.0.0.1',port=3306)
cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE dbtestowa")

db.close()
