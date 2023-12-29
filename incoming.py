import mysql.connector
import sale
from tabulate import tabulate
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kea062702!",
    database="Awming"
)

mycursor = mydb.cursor()

def in_transactions(in_list = {}):
    in_barcode = input("\nScan a barcode or end incoming transaction (press x): ")

    if (in_barcode == "x"):
        print("\nEnding incoming transaction...\n")
        in_commit(in_list)
    else:
        in_barcode = (in_barcode,)
        sqlFormula = "SELECT * From Inventory Where Barcode = %s"
        mycursor.execute(sqlFormula, in_barcode)

        in_lookup = mycursor.fetchall()

        if (len(in_lookup) == 1):
            for item in in_lookup:
                print("\nPhp", item[3], item[1], " - ", item[4])
                item_count = sale.usrInput_int("Number of items: ")
                item_name = item[1]
                stocks = item[4]
                price = item[3]
            
                if (in_barcode[0] in in_list):
                    sale_tuple = in_list[in_barcode[0]]
                    new_count = sale_tuple[2] + item_count
                    sale_tuple = (item[0], item_name, price, stocks, item_count, new_count)
                    in_list[in_barcode[0]] = sale_tuple
                else:
                    if (item_count > 0):
                        new_count = stocks + item_count
                        sale_tuple = (item[0], item_name, price, stocks, item_count, new_count)
                        in_list[in_barcode[0]] = sale_tuple
            in_transactions(in_list)
        elif (len(in_lookup) < 1):
            print("Barcode not in database!\n")
            in_transactions(in_list)
        else:
            print("Barcode has duplicates! Report to Kim and cancel transaction\n")
            in_transactions(in_list)
            #TO-DO: Add database for errors

def in_commit(in_list = {}):
    total_sum = 0
    in_table = []
    for key in in_list.keys():
        in_tuple = in_list[key]
        in_total_price = in_tuple[2]*in_tuple[4]
        new_total_price = in_tuple[2]*in_tuple[5]
        total_sum = total_sum + in_total_price
        in_tuple = in_tuple + (in_total_price, new_total_price)
        in_table.append(list(in_tuple))
    print(tabulate(in_table, headers = ["Barcode", "Item Name", "Price", "Previous Stocks", "Added Stocks", "New Total Stocks", "Incoming Price", "New Total Price"], tablefmt = "psql"))
    print(tabulate([["Total Incoming Price", total_sum]], tablefmt = "heavy_outline"))
   
    usr_commit = input("Commit transaction? y/n: ")
    if (usr_commit == 'y' or usr_commit == 'Y'):
        for lists in in_table:
            now = datetime.now()
            lists.append(now.date())
            lists.append(now.time())
        sql = "INSERT INTO Incoming (Barcode, Item_Name, Price, Previous_Stocks, Added_Stocks, New_Total_Stocks, Incoming_Price, New_Total_Price, Date, Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.executemany(sql, in_table)
        in_update(in_list)
    elif (usr_commit == 'n' or usr_commit == 'N'):
        in_void(in_list)
    else:
        print("\nPress y/Y or n/N only. Try again.\n")
        in_commit(in_list)

def in_void(in_list = {}):
    usr_void = input("Scan barcode to void or press x to end transaction and go back to main menu: ")

    if (usr_void == "x" or usr_void == "X"):
        print("Going back to main menu...")
    else:
        if (usr_void in in_list.keys()):
            in_tuple = in_list[usr_void]
            print(in_tuple[1], " - ", in_tuple[5])
            item_count = sale.usrInput_int("Number of items to void: ")
            new_count = in_tuple[5] - item_count
            if (new_count == 0):
                in_list.pop(usr_void, None)
            else:
                in_tuple = list(in_tuple)
                in_tuple[5] = new_count
                in_list[usr_void] = tuple(in_tuple)
            in_commit(in_list)
        else:
            print("\nBarcode not yet scanned. Try again.\n")
            in_void(in_list)

def in_update(in_list = {}):
    update_list = []
    for key in in_list.keys():
        in_tuple = in_list[key]
        sqlFormula_1 = "SELECT * From Inventory Where Barcode = %s"
        mycursor.execute(sqlFormula_1, (key,))
        in_lookup = mycursor.fetchall()

        for item in in_lookup:
            stocks = item[4]
            stocks = item[4] + in_tuple[4]
            update_list.append((stocks, key))        

    sqlFormula_2 = "UPDATE Inventory SET Stocks = %s WHERE Barcode = %s"
    mycursor.executemany(sqlFormula_2, update_list)
    mydb.commit()

    print("\n", mycursor.rowcount, "Record(s) updated\n")

