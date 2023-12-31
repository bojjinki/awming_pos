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

def barcode_lookup(barcode, item_list):

    barcode = str(barcode)
    sqlFormula = "SELECT * From Inventory Where Barcode = %s"
    mycursor.execute(sqlFormula, (barcode,))

    sale_lookup = mycursor.fetchall()

    if (len(sale_lookup) == 1):
        
        displayList = sale_lookup[0]

        if (barcode in item_list.keys()):
            tuple = item_list[barcode]
            count = tuple[1] + 1
            price = count*displayList[3]
            item_list[barcode] = (tuple[0], count, price)
        else:
            count = 1
            price = count*displayList[3]
            item_list[barcode] = (displayList[1], count, price)
    
    return item_list

    
    