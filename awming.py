import mysql.connector
import sale

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kea062702!",
    database="Awming"
)

mycursor = mydb.cursor()

def main_menu():
    print("==================================")
    print("Main Menu")
    print("==================================")
    print("1 : Make a Sale")
    print("2 : Record an Incoming Stock")
    print("3 : Record an Outgoing Stock")
    print("0 : Quit\n")

    selection = input("To start a transaction, please select a number: ")

    if (selection == '0'):
        print("Quitting\n")
    elif (selection == '1'):
        print("\nMaking a sale...\n")
        sale.sale_transactions()
    elif (selection == '2'):
        print("Recording an incoming transaction...\n")
    elif (selection == '3'):
        print("Recording an outgoing transaction...\n")
    else:
        print("Incorrect selection...\n")
        main_menu()

def main():
    print("Welcome to Aw-Ming's Pet Supplies!\n")
    main_menu()



    

if __name__ == "__main__":
    main()