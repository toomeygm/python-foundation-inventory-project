import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#FUNCTIONS

#Show all products list
def all_products_list():
   cursor.execute("SELECT * FROM my_table ORDER BY date DESC")

  # Fetch all the rows from the result
   rows = cursor.fetchall()

   # Print the products in the inventory
   for row in rows:
      print("ID:", row[0])
      print("Item Name:", row[1])
      print("Quantity:", row[2])
      print("Minimum Stock Holdings:", row[3])
      print("Minimum Quantity:", row[4])
      print("Purchase Location:", row[5])
      print("Storage Location:", row[6])
      print("Date:", row[7])
      print("-----------------------")



#Show products list by date
def list_by_date():
   # Specify the desired date
   date = input("Enter the date (YYYY/MM/DD): ")

   # Execute the SELECT query with the WHERE clause
   cursor.execute("SELECT * FROM my_table WHERE date = ?", (date,))

   # Fetch all the rows from the result
   rows = cursor.fetchall()

   # Print the products in the inventory for the specified date
   if rows:
      for row in rows:
         print("ID:", row[0])
         print("Item Name:", row[1])
         print("Quantity:", row[2])
         print("Minimum Stock Holdings:", row[3])
         print("Minimum Quantity:", row[4])
         print("Purchase Location:", row[5])
         print("Storage Location:", row[6])
         print("Date:", row[7])
         print("-----------------------")
   else:
      print("No data exists for this date.")


def insert_new_data():
      id = input("Enter the id of item: ")
      item_name = input("Enter the name of new item: ")
      quantity = input("Enter the quantity of the item: ")
      min_quantity = input("Enter the minimum quantity that should be stored: ")
      purchase_location = input("Enter the name of the place where you purchased the item: ")
      storage_location = input("Enter the location where you want to store your items: ")
      date = input("Enter the date in YYYY/MM/DD format: ")
      try:
         conn.execute(
            "INSERT INTO my_table (id,item_name,quantity,min_quantity,purchase_location,storage_location,date) VALUES(?,?,?,?,?,?,?)",
            (id, item_name, quantity, min_quantity, purchase_location, storage_location, date))
         conn.commit()
         print("New data inserted successfully")
      except Exception as e:
         print(e)
         pass


def delete_data():
   item_name = input("Enter the name of the item that you want to delete: ")

   # Search for items in the database
   cursor.execute("SELECT * FROM my_table WHERE item_name=?", (item_name,))
   result = cursor.fetchone()  # bring the result

   if result:
      # if the item exists
      item_id = result[0]
      cursor.execute("DELETE FROM my_table WHERE id=?", (item_id,))
      conn.commit()
      print(f"Item '{item_name}' is deleted.")
   else:
      # if the item doesn't exist
      print(f"Item '{item_name}' does not exist in your inventory.")

      # Ask users to search again
      choice = input("Do you want to search for the item again? (y/n): ")
      if choice.lower() == "y":
         delete_data()


def update_data():
   # Get data from the most recent date
   cursor.execute('SELECT * FROM my_table WHERE date = (SELECT MAX(date) FROM my_table)')
   latest_data = cursor.fetchall()

   if latest_data:
      for data in latest_data:
         id, item_name, quantity, min_quantity, purchase_location, storage_location, date = data
         print(
            f"ID: {id}, Name: {item_name}, Quantity: {quantity}, Minimum Quantity: {min_quantity}, Purchase location: {purchase_location}, Storage location: {storage_location}, Date: {date}")

         # Get the changed information
         new_quantity = input(f"New Quantity: ")
         new_min_quantity = input(f"New Minimum Quantity (Press Enter, if there is no change): ")
         new_purchase_location = input(f"New Purchase Location (Press Enter, if there is no change): ")
         new_storage_location = input(f"New Storage Location (Press Enter, if there is no change): ")
         new_date = input(f"New Date(in YYYY/MM/DD format): ")

         if new_quantity:
            quantity = int(new_quantity)
         if new_min_quantity:
            min_quantity = int(new_min_quantity)
         if new_purchase_location:
            purchase_location = new_purchase_location
         if new_storage_location:
            storage_location = new_storage_location
         if new_date:
            date = new_date

         # Save as new data
         cursor.execute(
            "INSERT INTO my_table (id, item_name, quantity, min_quantity, purchase_location, storage_location, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id, item_name, quantity, min_quantity, purchase_location, storage_location, date))

         conn.commit()
         print("New data updated successfully.")

      cursor.execute(
         "SELECT item_name, quantity, min_quantity FROM my_table WHERE date = (SELECT MAX(date) FROM my_table) AND quantity <= min_quantity")
      low_quantity_items = cursor.fetchall()

      # Show user a list of items they need to buy if their inventory is below the minimum stock level
      if low_quantity_items:
         print("The following items need to be purchased:")
         for item in low_quantity_items:
            item_name, quantity, min_quantity = item
            print(f"- {item_name}: (Current Quantity: {quantity} / Minimum Stock Holdings: {min_quantity})")
      else:
         print("No items need to be purchased.")


   else:
      print("No data found.")


# Connect Database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

x = 1
print("Opened database successfully")

# Get storage location of all items
GET_STORAGE_LOCATION = "SELECT storage_location FROM my_table;"
def get_storage_location(conn):
   with conn:
      cursor = conn.execute(GET_STORAGE_LOCATION).fetchmany(10)
      for row in cursor:
         print(row)

get_storage_location(conn)

"""This function is useful for creating graphs and analyzing data, 
since it gets all instances of an item
The LIMIT clause can be used to constrain the number of rows returned"""
def get_all_item_instances():
   cursor =  conn.execute("SELECT item_name, Date FROM my_table WHERE id = 1 LIMIT 5")

   rows = cursor.fetchall()
   for x in rows:
      print(x)

get_all_item_instances()

# VISUALIZING DATA USING MATPLOTLIB
print("*******************************")

#read db as df using SQL Alchemy, a Python SQL toolkit
df = pd.read_sql_query("SELECT id, item_name, quantity, purchase_location, Date FROM my_table ORDER BY Date DESC", conn)
df["Date"] = pd.to_datetime(df["Date"])

#Group products by location they were bought
df.groupby("purchase_location")["item_name"].nunique().plot(kind="bar", color = "pink")
plt.ylabel("Item quantity")
plt.xticks(rotation=45, ha='right')
plt.show()

# Visualization Consumption of product by month for item id 1 (Mehl Typ 405 25 kg)
ypoints = np.array([40, 5, 30, 15, 30, 12, 30, 8, 30, 5, 30, 8, 35])
plt.plot(ypoints, "o:m", ls = ":")
plt.xlabel("Bi-monthly inventory from 01/12/2022 to 01/06/2023")
plt.ylabel("Quantity of item (Flour Type 405 25 kg)")
plt.show()

 # Visualization Consumption of product by month for item id 5 (Butter (250g*20/box)
ypoints = np.array([10, 2, 7, 5, 8, 5, 8, 5, 10, 3, 10, 5, 10])
plt.plot(ypoints, "o:g", ls = ":")
plt.xlabel("Bi-monthly inventory from 01/12/2022 to 01/06/2023")
plt.ylabel("Quantity of item (Butter (250g*20/box)")
plt.show()

print("*************************")

while(x):
   print("Press 1 to show all products in inventory")
   print("Press 2 to show products list by date")
   print("Press 3 to insert new item")
   print("Press 4 to delete the data")
   print("press 5 to update data")

   name = input("Choose an Operation to perform ")
   if(name == "1"):
      all_products_list()
   elif(name =="2"):
      list_by_date()
   elif(name =="3"):
      insert_new_data()
   elif(name =="4"):
      delete_data()
   elif(name =="5"):
      update_data()

conn.close()
x = 0


