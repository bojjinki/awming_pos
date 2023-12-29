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

def usrInput_int(message):
    while True:
        try:
            item_count = int(input(message))
        except ValueError:
            print("\nNumber of items must be an integer.\n")
            continue
        else:
            return item_count

def sale_transactions(sale_list = {}):
    sale_barcode = input("\nScan a barcode or end sale transaction (press x): ")

    if (sale_barcode == "x"):
        print("\nEnding sale transaction...\n")
        sale_commit(sale_list)
    else:
        sale_barcode = (sale_barcode,)
        sqlFormula = "SELECT * From Inventory Where Barcode = %s"
        mycursor.execute(sqlFormula, sale_barcode)

        sale_lookup = mycursor.fetchall()

        if (len(sale_lookup) == 1):
            for item in sale_lookup:
                item_count = usrInput_int("Number of items: ")
                print(item[1], ".......... Php ", item[3], "\n")
                item_name = item[1]
                price = item[3]
            
                if (sale_barcode[0] in sale_list):
                    sale_tuple = sale_list[sale_barcode[0]]
                    count = sale_tuple[2] + item_count
                    sale_tuple = (item[0], item_name, count, price)
                    sale_list[sale_barcode[0]] = sale_tuple
                else:
                    if (item_count > 0):
                        sale_tuple = (item[0], item_name, item_count, price)
                        sale_list[sale_barcode[0]] = sale_tuple
            
            sale_transactions(sale_list)
        elif (len(sale_lookup) < 1):
            print("Barcode not in database!\n")
            sale_transactions(sale_list)
        else:
            print("Barcode has duplicates! Report to Kim and cancel transaction\n")
            sale_transactions(sale_list)

def sale_commit(sale_list = {}):
    total_sum = 0
    sale_table = []
    for key in sale_list.keys():
        sale_tuple = sale_list[key]
        total_price = sale_tuple[2]*sale_tuple[3]
        total_sum = total_sum + total_price
        sale_tuple = sale_tuple + (total_price,)
        sale_table.append(list(sale_tuple))
    print(tabulate(sale_table, headers = ["Barcode", "Item Name", "Count", "Price", "Item Total"], tablefmt = "psql"))
    print(tabulate([["Total Sales", total_sum]], tablefmt = "heavy_outline"))

    usr_commit = input("Commit transaction? y/n: ")
    if (usr_commit == 'y' or usr_commit == 'Y'):
        for lists in sale_table:
            now = datetime.now()
            lists.append(now.date())
            lists.append(now.time())
        sql = "INSERT INTO Sales (Barcode, Item_Name, Sale_Count, Price, Total_Price, Date, Time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.executemany(sql,sale_table)
        sale_update(sale_list)
    elif (usr_commit == 'n' or usr_commit == 'N'):
        sale_void(sale_list)
    else:
        print("\nPress y/Y or n/N only. Try again.\n")
        sale_commit(sale_list)

def sale_void(sale_list = {}):
    usr_void = input("Scan barcode to void or press x to end transaction and go back to main menu: ")

    if (usr_void == "x" or usr_void == "X"):
        print("Going back to main menu...")
    else:
        if (usr_void in sale_list.keys()):
            sale_tuple = sale_list[usr_void]
            print(sale_tuple[1], " - ", sale_tuple[2])
            item_count = usrInput_int("Number of items to void: ")
            new_count = sale_tuple[2] - item_count
            if (new_count == 0):
                sale_list.pop(usr_void, None)
            else:
                sale_tuple = list(sale_tuple)
                sale_tuple[2] = new_count
                sale_list[usr_void] = tuple(sale_tuple)
            sale_commit(sale_list)
        else:
            print("\nBarcode not yet scanned. Try again.\n")
            sale_void(sale_list)
            
def sale_update(sale_list = {}):
    update_list = []
    for key in sale_list.keys():
        sale_tuple = sale_list[key]
        sqlFormula_1 = "SELECT * From Inventory Where Barcode = %s"
        mycursor.execute(sqlFormula_1, (key,))
        sale_lookup = mycursor.fetchall()

        for item in sale_lookup:
            stocks = item[4]
            stocks = item[4] - sale_tuple[2]
            update_list.append((stocks, key))        

    sqlFormula_2 = "UPDATE Inventory SET Stocks = %s WHERE Barcode = %s"
    mycursor.executemany(sqlFormula_2, update_list)
    mydb.commit()

    print(mycursor.rowcount, "\nRecord(s) updated\n")





         





    
        

