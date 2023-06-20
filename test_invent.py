#import pandas as pd
#import sqlite3

#conn = sqlite3.connect("inventory.db")

#conn.execute("""CREATE TABLE if not exists my_table (item_name TEXT PRIMARY KEY NOT NULL, quantity INT, purchase_location TEXT, storage_location TEXT);""")

#print("Table created successfully")


#populate_data = True

#conn.close()

#for row in conn.execute("select * from my_table"):
    #print(row)


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(inventory.db)

fig = plt.figure()
axes = fig.add_subplot(1,1,1)
axes.bar([1,2,3,4], [3,5,7,25], tick_label = ["A", "B", "C", "D"])
plt.show()

#df["Date"] = df["Date"].strptime(' ')
#GET_ITEM_BY_DATE = "SELECT id, Date FROM my_table GROUP BY id"



select * from my_table
left join item_table
on item_table.item_id = my_table.item_id
def get_all_item_instances_bar(id):
   fig = plt.figure()
   axes = fig.add_subplot(1, 1, 1)
   axes.bar(
      range(len(id)),
      [id[1] for i in id]
   )
   plt.show()

   cursor =  conn.execute("SELECT item_name, Date FROM my_table WHERE id = 1 LIMIT 5")

   rows = cursor.fetchall()
   for x in rows:
      print(x)

get_all_item_instances_bar()


#fig = px.bar (df(my_table?), x = 'species'(item_name), y = 'location'(Date))
#fig.show() .....use as templated



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
      print("Purchase Location:", row[3])
      print("Storage Location:", row[4])
      print("Date:", row[5])
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
         print("Purchase Location:", row[3])
         print("Storage Location:", row[4])
         print("Date:", row[5])
         print("-----------------------")
   else:
      print("No data exists for this date.")

list_by_date()

def insert_new_data():
   id = input("Enter the id of item: ")
   item_name = input("Enter the name of new item: ")
   quantity = input("Enter the quantity of the item: ")
   purchase_location = input("Enter the name of the place where you purchased the item: ")
   storage_location = input("Enter the location where you want to store your items: ")
   date = input("Enter the date in YYYY/MM/DD format: " )
   try:
      conn.execute("INSERT INTO my_table (id,item_name,quantity,purchase_location,storage_location,date)\
                   values ("+"'" +str(id) +"','"+ str(item_name) +"','" + str(quantity) + "', '" +str(purchase_location) +"', '" +str(storage_location) +"', '" +str(date) +"')");
      conn.commit()
      print("Data inserted successfully")
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

#def update_data():
#def purchase_list():



# Connect Database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

x = 1
print("Opened database successfully")

# Get storage location of all items
GET_STORAGE_LOCATION = "SELECT storage_location FROM my_table;"
def get_storage_location(conn):
   with conn:
      cursor = conn.execute(GET_STORAGE_LOCATION).fetchall()
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

#Seperate code in terminal
print("***************************")

while(x):
   print("Press 1 to show all products in inventory")
   print("Press 2 to show products list by date")
   print("Press 3 to insert new item")
   print("Press 4 to delete the data")

   name = input("Choose an Operation to perform ")
   if(name == "1"):
      all_products_list()
   elif(name =="2"):
      list_by_date()
   elif(name =="3"):
      insert_new_data()
   elif(name =="4"):
      delete_data()

      conn.close()
      x = 0

