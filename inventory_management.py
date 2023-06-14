#import pandas as pd
#import sqlite3

#conn = sqlite3.connect("inventory.db")

#conn.execute("""CREATE TABLE if not exists my_table (item_name TEXT PRIMARY KEY NOT NULL, quantity INT, purchase_location TEXT, storage_location TEXT);""")

#print("Table created successfully")


#populate_data = True

#conn.close()

#for row in conn.execute("select * from my_table"):
    #print(row)


import pandas as pd
import sqlite3

# Connetct Database
conn = sqlite3.connect('inventory.db')
print ("Opened database successfully")

#Check Database works
cursor = conn.execute("SELECT id, item_name, quantity from my_table")
for row in cursor:
   print ("ID = ", row[0])
   print ("ITEM_NAME = ", row[1])
   print ("QUANTITY = ", row[2]), "\n"

print ("Operation done successfully")
conn.close()