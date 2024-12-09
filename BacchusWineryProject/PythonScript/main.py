# Miles Shinsato
# Nardos Gebremedhin
# Jessica Long-Heinicke
# Joseph Ayo
# Adrian Marquez


# Import Statements
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "winery_user",
    "password": "wine",
    "host": "127.0.0.1",
    "database": "winerycase",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    # Display the data from the Suppliers table
    cursor = db.cursor()
    cursor.execute("SELECT SupplierID, Name, ContactInfo, DeliverySchedule, PerformanceRating FROM Suppliers")
    supplier = cursor.fetchall()

    print("DISPLAYING Suppliers DATA")
    for supplier in supplier:
        try:
            print(f"Supplier ID: {supplier[0]}")
            print(f"Name: {supplier[1]}")
            print(f"Contact Info: {supplier[2]}")
            print(f"Delivery Schedule: {supplier[3]}")
            print(f"Performance Rating: {supplier[4]}")
            print("-" * 20)
        except IndexError:
            print(f"Error: Incomplete data for supplier: {supplier}")
    db.commit()

    # Display the data from the Inventory table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Inventory")
    inventorys = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Inventory in inventorys:
        print(f"Item ID: {inventorys[0]}\nItem Name: {inventorys[1]}\nQuantity: {inventorys[2]}"
              f"\nReorder Level: {inventorys[3]}\nSupplier ID: {inventorys[4]}\n")
    db.commit()

    # Display the data from the Wines table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Wines")
    wine = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Wines in wine:
        print(f"Wine ID: {wine[0]}\nWine Name: {wine[1]}\nType: {wine[2]}"
              f"\nPrice: {wine[3]}\nStock: {wine[4]}\n")
    db.commit()

    # Display the data from the Distributors table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Distributors")
    distributor = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Distributors in distributor:
        print(f"Distributor ID: {distributor[0]}\nName: {distributor[1]}\nContact Info: {distributor[2]}"
              f"\nSales Quota: {distributor[3]}")
    db.commit()

    # Display the data from the Orders table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Orders")
    order = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Orders in order:
        print(f"Order ID: {order[0]}\nOrder Date: {order[1]}\nStatus: {order[2]}"
              f"\nDistributor ID: {order[3]}\nWine ID: {order[4]}\n")
    db.commit()

    # Display the data from the Employees table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Employees")
    employee = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Employees in employee:
        print(f"Employee ID: {employee[0]}\nName: {employee[1]}\nRole: {employee[2]}"
              f"\nDepartment ID: {employee[3]}")
    db.commit()

    # Display the data from the Departments table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Departments")
    department = cursor.fetchall()
    print("DISPLAYING Suppliers DATA")
    for Departments in department:
        print(f"Department ID: {department[0]}\nDepartment Name: {department[1]}\n")
    db.commit()

    # Display the data from the TimeTracking table
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM TimeTracking")
    timetrackings = cursor.fetchall()
    print("DISPLAYING TimeTracking DATA")
    for TimeTracking in timetrackings:
        print(f"Time Tracking ID: {timetrackings[0]}\nEmployee ID: {timetrackings[1]}\nClock In: {timetrackings[2]}"
              f"\nClock Out: {timetrackings[3]}\nDate: {timetrackings[4]}\n")
    db.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
