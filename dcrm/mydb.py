import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Polina-16062003'
    )

cursorObj = dataBase.cursor()


cursorObj.execute("CREATE DATABASE event")
print("Done")
