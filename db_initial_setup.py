import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kea062702!"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Awming")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kea062702!",
    database = "Awming"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE Table Inventory (Barcode VARCHAR(255), Item_Name VARCHAR(255), Category VARCHAR(255), Price INT, Stocks INT)")
mycursor.execute("CREATE Table Sales (Barcode VARCHAR(255), Item_Name VARCHAR(255), Sale_Count INT, Price INT, Total_Price INT, Date DATE, Time TIME)")
mycursor.execute("CREATE Table Incoming (Barcode VARCHAR(255), Item_Name VARCHAR(255), Price INT, Previous_Stocks INT, Added_Stocks INT, New_Total_Stocks INT, Incoming_Price INT, New_Total_Price INT, Date DATE, Time TIME)")


val = []
with open('inventory_consolidation.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    line_count = 0
    for lines in csvFile:
        if (line_count != 0):
            lines = tuple(lines)
            val.append(lines) 

        line_count += 1

    sql = "INSERT INTO Inventory (Barcode, Item_Name, Category, Price, Stocks) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(sql, val)
    mydb.commit()

    mycursor.execute("SHOW TABLES")

    print("Awming database and essential tables created.")


        
        

