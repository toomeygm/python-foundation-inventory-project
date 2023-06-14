import pandas as pd
import sqlite3

conn = sqlite3.connect("inventory.db")

conn.execute("""CREATE TABLE if not exists my_table (item_name TEXT PRIMARY KEY NOT NULL,
             quantity INT,
             purchase_location TEXT,
             storage_location TEXT);""")

print("Table created successfully")


#populate_data = True

#conn.close()

#for row in conn.execute("select * from my_table"):
    #print(row)
