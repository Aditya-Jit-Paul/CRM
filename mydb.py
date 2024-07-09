import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'aditya98',#django password
)
#preparing cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print("Success!!")