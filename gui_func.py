import mysql.connector
from tabulate import tabulate
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kea062702!",
    database="Awming"
)

mycursor = mydb.cursor()

def barcode_lookup(barcode):

    barcode = str(barcode)
    sqlFormula = "SELECT * From Inventory Where Barcode = %s"
    mycursor.execute(sqlFormula, (barcode,))

    sale_lookup = mycursor.fetchall()

    if (len(sale_lookup) == 1):
        print(sale_lookup)
    else:
        print("No data.")